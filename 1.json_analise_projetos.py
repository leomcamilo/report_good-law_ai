#!/usr/bin/env python3
"""
Análise de Projetos da Lei do Bem - DataFrame Pandas
====================================================

Este script executa a consulta SQL consolidada dos projetos da Lei do Bem
e carrega os dados em um DataFrame pandas para análise e processamento.

Configuração do banco: PostgreSQL
Database: dbs_mctic2
Schema: public
"""

import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text
import numpy as np
import warnings
from typing import Optional, Dict, Any, List
import logging
import json
import os
from datetime import datetime

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Suprimir warnings do pandas
warnings.filterwarnings('ignore')

class CarregadorDadosAglomeradosLeiDoBem:
    """Classe para análise de projetos da Lei do Bem usando dados do PostgreSQL."""
    
    def __init__(self):
        """
        Inicializa o analisador com as configurações de banco.
        """
        self.config_db = {
            'user': 'ia_budy',
            'password': 'ia_budy',
            'host': 'localhost',
            'port': 5432,
            'database': 'dbs_mctic2'
        }
        self.engine = None
        self.df_projetos = None
        
    def conectar_banco(self) -> bool:
        """
        Estabelece conexão com o banco PostgreSQL.
        
        Returns:
            bool: True se conexão bem-sucedida, False caso contrário
        """
        try:
            # Criar string de conexão
            connection_string = (
                f"postgresql://{self.config_db['user']}:{self.config_db['password']}"
                f"@{self.config_db['host']}:{self.config_db['port']}/{self.config_db['database']}"
            )
            
            # Criar engine SQLAlchemy
            self.engine = create_engine(connection_string)
            
            # Testar conexão
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
                
            logger.info("✅ Conexão com banco estabelecida com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao conectar com banco: {e}")
            return False
    
    def carregar_dados(self) -> Optional[pd.DataFrame]:
        """
        Executa a consulta SQL e carrega os dados em um DataFrame pandas.
        
        Returns:
            pd.DataFrame: DataFrame com os dados dos projetos ou None se erro
        """
        if not self.engine:
            logger.error("❌ Conexão com banco não estabelecida")
            return None
            
        try:
            # Query SQL baseada no arquivo descricao dos projetos.sql
            # Substituindo ";" por "," nas colunas concatenadas
            query_sql = """
            select 
            lst.idprenchimentosituacaoanalise as id_empresa_ano
            ,lst.nranobase as ano_referencia
            , replace(concat('CNPJ: '::text , lst.nrcnpj::text ,' RAZÃO SOCIAL :'::text , lst.norazaosocial::text, ' ATIVIDADE ECONOMICA :'::text, lst.noatividadeeconomica::text,' Cd ATIV.ECONOMICA IBGE :'::text, lst.cdatividadeeconomicaibge::text, ' PORTE '::text, lst.notipoportepessoajuridica::text, ' ID EMPRESA/ANO :'::text, lst.idprenchimentosituacaoanalise), ';', ',') as empresa
            , replace(concat('NÚMERO: '::text, daproj.nritem::text ,' ID ÚNICO: '::text, daproj.iddadoanaliseprojeto::text ,' NOME: '::text, daproj.noprojeto::text ,' DESCRIÇÃO: '::text, daproj.dsprojeto::text ,' TIPO (PA ou DE): '::text, daproj.tppbpade::text ,' AREA: '::text, daproj.dsareaprojeto::text ,' PALAVRAS CHAVE: '::text, daproj.dspalavrachave::text ,' NATUREZA: '::text, daproj.tpnatureza::text ,' ELEMENTO TECNOLÓGICO: '::text, daproj.dselementotecnologico::text ,' DESAFIO TECNOLÓGICO: '::text, daproj.dsdesafiotecnologico::text ,' METODOLOGIA: '::text, daproj.dsmetodologiautilizada::text ,' INFORMAÇÃO COMPLEMENTAR: '::text, daproj.dsinformacaocomplementar::text ,' RESULTADO ECONÔMICO: '::text, daproj.dsresultadoeconomico::text ,' RESULTADO INOVAÇÃO: '::text, daproj.dsresultadoinovacao::text ,' DESCRIÇÃO RH: '::text, daproj.dsrecursoshumanos::text ,' DESCRIÇÃO MATERIAIS: '::text, daproj.dsrecursosmateriais::text ,' SETOR PARA ANALISE DO PROJETO: '::text, do_set.nosetor::text), ';', ',') as projeto
            , replace(concat('CICLO MAIOR QUE 1 ANO: '::text, daproj.icciclomaior::text , ' ATIVIDADE PDI CONTINUADA ANO ANTERIOR :'::text, daproj.dsatividadepdicontinuadaanobase::text), ';', ',') as projeto_multianual
            
            from tbdadoempresamarco dem
            left join listaempresasporanobasesituacaoanalise lst on lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
            left join tbdadoanaliseprojeto daproj on daproj.idprenchimentosituacaoanalise  = dem.idprenchimentosituacaoanalise
            --
            --DO
            --
            left join tbanaliseobjetomarcoprojeto do_aomproj on do_aomproj.idmarcoanalise = dem.idmarcoanalisedo and do_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbanaliseat do_aat on do_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto and do_aat.idmarcoanalise = dem.idmarcoanalisedo
            left join tbsituacaoanaliseat do_saat on do_saat.idanaliseat = do_aat.idanaliseat and do_saat.icativo 
            left join tbsetor do_set on do_set.idsetor = do_saat.idsetor
            where lst.nranobase = 2023
            order by lst.idprenchimentosituacaoanalise, daproj.nritem
            """
            
            logger.info("🔍 Executando consulta SQL...")
            
            # Executar query e carregar em DataFrame
            self.df_projetos = pd.read_sql_query(query_sql, self.engine)
            
            logger.info(f"✅ Dados carregados: {len(self.df_projetos)} projetos encontrados")
            logger.info(f"📊 Colunas disponíveis: {len(self.df_projetos.columns)}")
            
            # Log das empresas encontradas
            if not self.df_projetos.empty:
                empresas_encontradas = self.df_projetos['empresa'].str.extract(r'RAZÃO SOCIAL :([^A-Z]*?)(?=[^A-Z]|$)')[0].str.strip().unique()
                logger.info(f"📋 Amostra de empresas encontradas: {list(empresas_encontradas[:5])}")  # Limitar a 5 para evitar spam
            
            return self.df_projetos
            
        except Exception as e:
            logger.error(f"❌ Erro ao executar consulta: {e}")
            return None


class CarregadorDadosLeiDoBem:
    """Classe para carregar dados detalhados dos projetos da Lei do Bem usando query linha única."""
    
    def __init__(self):
        """
        Inicializa o carregador com as configurações de banco.
        """
        self.config_db = {
            'user': 'ia_budy',
            'password': 'ia_budy',
            'host': 'localhost',
            'port': 5432,
            'database': 'dbs_mctic2'
        }
        self.engine = None
        self.df_projetos_detalhado = None
        
    def conectar_banco(self) -> bool:
        """
        Estabelece conexão com o banco PostgreSQL.
        
        Returns:
            bool: True se conexão bem-sucedida, False caso contrário
        """
        try:
            # Criar string de conexão
            connection_string = (
                f"postgresql://{self.config_db['user']}:{self.config_db['password']}"
                f"@{self.config_db['host']}:{self.config_db['port']}/{self.config_db['database']}"
            )
            
            # Criar engine SQLAlchemy
            self.engine = create_engine(connection_string)
            
            # Testar conexão
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
                
            logger.info("✅ Conexão com banco estabelecida com sucesso (CarregadorDadosLeiDoBem)")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao conectar com banco (CarregadorDadosLeiDoBem): {e}")
            return False
    
    def carregar_dados_detalhados(self) -> Optional[pd.DataFrame]:
        """
        Executa a consulta SQL detalhada (projeto_linha_unica.sql) e carrega os dados em um DataFrame pandas.
        
        Returns:
            pd.DataFrame: DataFrame com os dados detalhados dos projetos ou None se erro
        """
        if not self.engine:
            logger.error("❌ Conexão com banco não estabelecida")
            return None
            
        try:
            # Query SQL baseada no arquivo projeto_linha_unica.sql
            query_sql = """
                        select daproj.nritem
            , lst.nranobase as lst_nranobase
            , lst.nrcnpj as lst_nrcnpj
            , lst.norazaosocial as lst_norazaosocial
            , lst.idprenchimentosituacaoanalise as lst_idprenchimentosituacaoanalise
            , lst.noatividadeeconomica as lst_noatividadeeconomica
            , lst.cdatividadeeconomicaibge as lst_cdatividadeeconomicaibge
            , lst.notipoportepessoajuridica as lst_notipoportepessoajuridica
            , dem.idprenchimentosituacaoanalise as dem_idprenchimentosituacaoanalise
            , dem.idmarcoanalisedo as dem_idmarcoanalisedo
            , dem.nrmarcoanalisedo as dem_nrmarcoanalisedo
            , dem.dtmarcoanalisedo as dem_dtmarcoanalisedo
            , dem.idmarcoanaliseparecer as dem_idmarcoanaliseparecer
            , dem.nrmarcoanaliseparecer as dem_nrmarcoanaliseparecer
            , dem.dtmarcoanaliseparecer as dem_dtmarcoanaliseparecer
            , dem.idmarcoanalisecontestacao as dem_idmarcoanalisecontestacao
            , dem.nrmarcoanalisecontestacao as dem_nrmarcoanalisecontestacao
            , dem.dtmarcoanalisecontestacao as dem_dtmarcoanalisecontestacao
            , dem.idmarcoanalisedocontestacao as dem_idmarcoanalisedocontestacao
            , dem.nrmarcoanalisedocontestacao as dem_nrmarcoanalisedocontestacao
            , dem.dtmarcoanalisedocontestacao as dem_dtmarcoanalisedocontestacao
            , dem.idmarcoanaliseparecercontestacao as dem_idmarcoanaliseparecercontestacao
            , dem.dtmarcoanaliseparecercontestacao as dem_dtmarcoanaliseparecercontestacao
            , dem.nrmarcoanaliseparecercontestacao as dem_nrmarcoanaliseparecercontestacao
            , dem.idmarcoanaliserecurso as dem_idmarcoanaliserecurso
            , dem.dtmarcoanaliserecurso as dem_dtmarcoanaliserecurso
            , dem.nrmarcoanaliserecurso as dem_nrmarcoanaliserecurso
            , dem.idmarcoanaliseparecerrecurso as dem_idmarcoanaliseparecerrecurso
            , dem.nrmarcoanaliseparecerrecurso as dem_nrmarcoanaliseparecerrecurso
            , dem.dtmarcoanaliseparecerrecurso as dem_dtmarcoanaliseparecerrecurso
            , dem.nrmarcoanalisecontestacaocodigoautencidade as dem_nrmarcoanalisecontestacaocodigoautencidade
            , dem.nrmarcoanaliserecursocodigoautencidade as dem_nrmarcoanaliserecursocodigoautencidade
            , daproj.nritem as daproj_nritem
            , daproj.noprojeto as daproj_noprojeto
            , daproj.dsprojeto as daproj_dsprojeto
            , daproj.tppbpade as daproj_tppbpade
            , daproj.dsareaprojeto as daproj_dsareaprojeto
            , daproj.dspalavrachave as daproj_dspalavrachave
            , daproj.tpnatureza as daproj_tpnatureza
            , daproj.dselementotecnologico as daproj_dselementotecnologico
            , daproj.dsdesafiotecnologico as daproj_dsdesafiotecnologico
            , daproj.dsmetodologiautilizada as daproj_dsmetodologiautilizada
            , daproj.icciclomaior as daproj_icciclomaior
            , daproj.dsinicioatividade as daproj_dsinicioatividade
            , daproj.dsprevisaotermino as daproj_dsprevisaotermino
            , daproj.dsinformacaocomplementar as daproj_dsinformacaocomplementar
            , daproj.dsresultadoeconomico as daproj_dsresultadoeconomico
            , daproj.dsresultadoinovacao as daproj_dsresultadoinovacao
            , daproj.dsrecursoshumanos as daproj_dsrecursoshumanos
            , daproj.dsrecursosmateriais as daproj_dsrecursosmateriais
            , daproj.dsatividadepdicontinuadaanobase as daproj_dsatividadepdicontinuadaanobase
            , dapempcoop.nritem as dapempcoop_nritem
            , dapempcoop.nrcnpj as dapempcoop_nrcnpj
            , dapempcoop.dsrazaosocial as dapempcoop_dsrazaosocial
            , dapempcoop.dsdescricao as dapempcoop_dsdescricao
            , do_taat.notipoanaliseat as do_taat_notipoanaliseat
            , do_aat.dscaminhoarquivoanalise as do_aat_dscaminhoarquivoanalise
            , do_aat.vltotaldeclarado as do_aat_vltotaldeclarado
            , do_aat.vltotalparecer as do_aat_vltotalparecer
            , do_aat.vltotalcontestacao as do_aat_vltotalcontestacao
            , do_traat.notiporesultadoanalise as do_traat_notiporesultadoanalise
            , do_traat.dstiporesultadoanalise as do_traat_dstiporesultadoanalise
            , do_tsa.notiposituacaoanalise as do_tsa_notiposituacaoanalise
            , do_set.nosetor as do_set_nosetor
            , do_saat.idmomentopessoaanalise as do_saat_idmomentopessoaanalise
            , do_saat.idunicopessoaanalise as do_saat_idunicopessoaanalise
            , do_saat.dtiniciosituacaoanalise as do_saat_dtiniciosituacaoanalise
            , do_saat.dtfimsituacaoanalise as do_saat_dtfimsituacaoanalise
            , do_saat.icativo as do_saat_icativo
            , do_saat.idapoiotecnico as do_saat_idapoiotecnico
            , do_anproj.icpdienvolveuparceriaict as do_anproj_icpdienvolveuparceriaict
            , do_anproj.icpdicontribuiupesquisabasica as do_anproj_icpdicontribuiupesquisabasica
            , do_anproj.icpditecnologiacamenteinovadordisruptivel as do_anproj_icpditecnologiacamenteinovadordisruptivel
            , do_anproj.icpdirelacionadaprojetos as do_anproj_icpdirelacionadaprojetos
            , do_anproj.icpdiaderenciaods as do_anproj_icpdiaderenciaods
            , do_anproj.cdfatorajustedimensaoinovacao as do_anproj_cdfatorajustedimensaoinovacao
            , do_anproj.icresultadogeraimpactoeconimicopositivo as do_anproj_icresultadogeraimpactoeconimicopositivo
            , do_anproj.icresultadoestimuladesenvolvimentoregional as do_anproj_icresultadoestimuladesenvolvimentoregional
            , do_anproj.icresultadogeraimpactosocialpositivo as do_anproj_icresultadogeraimpactosocialpositivo
            , do_anproj.icresultadoimpactaformacaoprofissionalpositivamente as do_anproj_icresultadoimpactaformacaoprofissionalpositivamente
            , do_anproj.icresultadoestimulaproducaonacional as do_anproj_icresultadoestimulaproducaonacional
            , do_anproj.cdfatorajustedimensaoresultado as do_anproj_cdfatorajustedimensaoresultado
            , do_nd1.dsnotadimensao as do_nd1_dsnotadimensao_invocao
            , do_nd2.dsnotadimensao as do_nd2_dsnotadimensao_resultado
            , do_nd3.dsnotadimensao as do_nd3_dsnotadimensao_final
            , do_aomproj.icjustificativapadraoalterada as do_aomproj_icjustificativapadraoalterada
            , do_aomproj.dsjustificativapadrao as do_aomproj_dsjustificativapadrao
            , do_aomproj.dsobservacaogeral as do_aomproj_dsobservacaogeral
            , do_aomproj.icreanalisado as do_aomproj_icreanalisado
            , do_aomproj.dsobservacaopadrao as do_aomproj_dsobservacaopadrao
            , do_aomproj.dscaminhoarquivoanalise as do_aomproj_dscaminhoarquivoanalise
            , do_aomproj.dsjustificativaparecerdo as do_aomproj_dsjustificativaparecerdo
            , do_aomproj.icmantemresposta as do_aomproj_icmantemresposta
            , do_aomproj.dsobservacaogeraldo as do_aomproj_dsobservacaogeraldo
            , do_aomproj.icmantemrespostaobservacao as do_aomproj_icmantemrespostaobservacao
            , do_aomproj.vltotaldeclarado as do_aomproj_vltotaldeclarado
            , do_a_proj.do_japroj_nojustificativaanalise
            , do_a_proj.do_japroj_notitulojustificativaanalise
            , do_a_proj.do_japroj_nocorpojustificativaanalise
            , do_a_proj.do_japroj_norodapejustificativaanalise
            , do_a_proj.do_japroj_notitulojustificativagrupoobjetoanaliseindividual
            , do_a_proj.do_tjaproj_notipojustificativaanalise
            , do_taaproj.notipoavaliacaoanalise as do_taaproj_notipoavaliacaoanalise
            , p_aomproj.icjustificativapadraoalterada as p_aomproj_icjustificativapadrao
            , p_aomproj.dsjustificativapadrao as p_aomproj_dsjustificativapadrao
            , p_aomproj.dsobservacaogeral as p_aomproj_dsobservacaogeral
            , p_aomproj.icreanalisado as p_aomproj_icreanalisado
            , p_aomproj.dsobservacaopadrao as p_aomproj_dsobservacaopadrao
            , p_aomproj.dscaminhoarquivoanalise as p_aomproj_dscaminhoarquivoanalise
            , p_aomproj.dsjustificativaparecerdo as p_aomproj_dsjustificativaparecerdo
            , p_aomproj.icmantemresposta as p_aomproj_icmantemresposta
            , p_aomproj.dsobservacaogeraldo as p_aomproj_dsobservacaogeraldo
            , p_aomproj.icmantemrespostaobservacao as p_aomproj_icmantemrespostaobservacao
            , p_aomproj.vltotaldeclarado as p_aomproj_vltotaldeclarado
            , p_a_proj.p_japroj_nojustificativaanalise
            , p_a_proj.p_japroj_notitulojustificativaanalise
            , p_a_proj.p_japroj_nocorpojustificativaanalise
            , p_a_proj.p_japroj_norodapejustificativaanalise
            , p_a_proj.p_japroj_notitulojustificativagrupoobjetoanaliseindividual
            , p_a_proj.p_tjaproj_notipojustificativaanalise
            , p_taaproj.notipoavaliacaoanalise as p_taaproj_notipoavaliacaoanalise
            , do_c_taat.notipoanaliseat as do_c_taat_notipoanaliseat
            , do_c_aat.dscaminhoarquivoanalise as do_c_aat_dscaminhoarquivoanalise
            , do_c_aat.vltotaldeclarado as do_c_aat_vltotaldeclarado
            , do_c_aat.vltotalparecer as do_c_aat_vltotalparecer
            , do_c_aat.vltotalcontestacao as do_c_aat_vltotalcontestacao
            , do_c_traat.notiporesultadoanalise as do_c_traat_notiporesultadoanalise
            , do_c_traat.dstiporesultadoanalise as do_c_traat_dstiporesultadoanalise
            , do_c_tsa.notiposituacaoanalise as do_c_tsa_notiposituacaoanalise
            , do_c_set.nosetor as do_c_set_nosetor
            , do_c_saat.idmomentopessoaanalise as do_c_saat_idmomentopessoaanalise
            , do_c_saat.idunicopessoaanalise as do_c_saat_idunicopessoaanalise
            , do_c_saat.dtiniciosituacaoanalise as do_c_saat_dtiniciosituacaoanalise
            , do_c_saat.dtfimsituacaoanalise as do_c_saat_dtfimsituacaoanalise
            , do_c_saat.icativo as do_c_saat_icativo
            , do_c_saat.idapoiotecnico as do_c_saat_idapoiotecnico
            , do_c_anproj.icpdienvolveuparceriaict as do_c_anproj_icpdienvolveuparceriaict
            , do_c_anproj.icpdicontribuiupesquisabasica as do_c_anproj_icpdicontribuiupesquisabasica
            , do_c_anproj.icpditecnologiacamenteinovadordisruptivel as do_c_anproj_icpditecnologiacamenteinovadordisruptivel
            , do_c_anproj.icpdirelacionadaprojetos as do_c_anproj_icpdirelacionadaprojetos
            , do_c_anproj.icpdiaderenciaods as do_c_anproj_icpdiaderenciaods
            , do_c_anproj.cdfatorajustedimensaoinovacao as do_c_anproj_cdfatorajustedimensaoinovacao
            , do_c_anproj.icresultadogeraimpactoeconimicopositivo as do_c_anproj_icresultadogeraimpactoeconimicopositivo
            , do_c_anproj.icresultadoestimuladesenvolvimentoregional as do_c_anproj_icresultadoestimuladesenvolvimentoregional
            , do_c_anproj.icresultadogeraimpactosocialpositivo as do_c_anproj_icresultadogeraimpactosocialpositivo
            , do_c_anproj.icresultadoimpactaformacaoprofissionalpositivamente as do_c_anproj_icresultadoimpactaformacaoprofissionalpositivamente
            , do_c_anproj.icresultadoestimulaproducaonacional as do_c_anproj_icresultadoestimulaproducaonacional
            , do_c_anproj.cdfatorajustedimensaoresultado as do_c_anproj_cdfatorajustedimensaoresultado
            , do_c_nd1.dsnotadimensao as do_c_nd1_dsnotadimensao_inovacao
            , do_c_nd2.dsnotadimensao as do_c_nd2_dsnotadimensao_resultado
            , do_c_nd3.dsnotadimensao as do_c_nd3_dsnotadimensao_final
            , do_c_aomproj.icjustificativapadraoalterada as do_c_aomproj_icjustificativapadraoalterada
            , do_c_aomproj.dsjustificativapadrao as do_c_aomproj_dsjustificativapadrao
            , do_c_aomproj.dsobservacaogeral as do_c_aomproj_dsobservacaogeral
            , do_c_aomproj.icreanalisado as do_c_aomproj_icreanalisado
            , do_c_aomproj.dsobservacaopadrao as do_c_aomproj_dsobservacaopadrao
            , do_c_aomproj.dscaminhoarquivoanalise as do_c_aomproj_dscaminhoarquivoanalise
            , do_c_aomproj.dsjustificativaparecerdo as do_c_aomproj_dsjustificativaparecerdo
            , do_c_aomproj.icmantemresposta as do_c_aomproj_icmantemresposta
            , do_c_aomproj.dsobservacaogeraldo as do_c_aomproj_dsobservacaogeraldo
            , do_c_aomproj.icmantemrespostaobservacao as do_c_aomproj_icmantemrespostaobservacao
            , do_c_aomproj.vltotaldeclarado as do_c_aomproj_vltotaldeclarado
            , do_c_a_proj.do_c_japroj_nojustificativaanalise
            , do_c_a_proj.do_c_japroj_notitulojustificativaanalise
            , do_c_a_proj.do_c_japroj_nocorpojustificativaanalise
            , do_c_a_proj.do_c_japroj_norodapejustificativaanalise
            , do_c_a_proj.do_c_japroj_notitulojustificativagrupoobjetoanaliseindividual
            , do_c_a_proj.do_c_tjaproj_notipojustificativaanalise
            , do_c_taaproj.notipoavaliacaoanalise as do_c_taaproj_notipoavaliacaoanalise
            , do_c_aomprojc.dsjustificativacontestacao as do_c_aomprojc_dsjustificativacontestacao
            , do_c_aomprojc.dsjustificativapadrao as do_c_aomprojc_dsjustificativapadrao
            , do_c_aomprojc.dsconsideracaoobservacaogeral as do_c_aomprojc_dsconsideracaoobservacaogeral
            , do_c_aomprojc.dsobservacaogeralparecer as do_c_aomprojc_dsobservacaogeralparecer
            , do_c_aomprojc.dsrecursoadministrativo as do_c_aomprojc_dsrecursoadministrativo
            , do_c_aomprojc.dsobservacaorecursoadministrativo as do_c_aomprojc_dsobservacaorecursoadministrativo
            , do_c_taaprojc.notipoavaliacaoanalise as do_c_taaprojc_notipoavaliacaoanalise
            , do_c_aomprojc.icsolicitacaoreanalise as do_c_aomprojc_icsolicitacaoreanalise
            , p_c_aomproj.icjustificativapadraoalterada as p_c_aomproj_icjustificativapadrao
            , p_c_aomproj.dsjustificativapadrao as p_c_aomproj_dsjustificativapadrao
            , p_c_aomproj.dsobservacaogeral as p_c_aomproj_dsobservacaogeral
            , p_c_aomproj.icreanalisado as p_c_aomproj_icreanalisado
            , p_c_aomproj.dsobservacaopadrao as p_c_aomproj_dsobservacaopadrao
            , p_c_aomproj.dscaminhoarquivoanalise as p_c_aomproj_dscaminhoarquivoanalise
            , p_c_aomproj.dsjustificativaparecerdo as p_c_aomproj_dsjustificativaparecerdo
            , p_c_aomproj.icmantemresposta as p_c_aomproj_icmantemresposta
            , p_c_aomproj.dsobservacaogeraldo as p_c_aomproj_dsobservacaogeraldo
            , p_c_aomproj.icmantemrespostaobservacao as p_c_aomproj_icmantemrespostaobservacao
            , p_c_aomproj.vltotaldeclarado as p_c_aomproj_vltotaldeclarado
            , p_c_a_proj.p_c_japroj_nojustificativaanalise
            , p_c_a_proj.p_c_japroj_notitulojustificativaanalise
            , p_c_a_proj.p_c_japroj_nocorpojustificativaanalise
            , p_c_a_proj.p_c_japroj_norodapejustificativaanalise
            , p_c_a_proj.p_c_japroj_notitulojustificativagrupoobjetoanaliseindividual
            , p_c_a_proj.p_c_tjaproj_notipojustificativaanalise
            , p_c_taaproj.notipoavaliacaoanalise as p_c_taaproj_notipoavaliacaoanalise
            , do_c_aomprojc.dsjustificativacontestacao as p_c_aomprojc_dsjustificativacontestacao
            , do_c_aomprojc.dsjustificativapadrao as p_c_aomprojc_dsjustificativapadrao
            , do_c_aomprojc.dsconsideracaoobservacaogeral as p_c_aomprojc_dsconsideracaoobservacaogeral
            , do_c_aomprojc.dsobservacaogeralparecer as p_c_aomprojc_dsobservacaogeralparecer
            , do_c_aomprojc.dsrecursoadministrativo as p_c_aomprojc_dsrecursoadministrativo
            , do_c_aomprojc.dsobservacaorecursoadministrativo as p_c_aomprojc_dsobservacaorecursoadministrativo
            , p_c_taaprojc.notipoavaliacaoanalise as p_c_taaprojc_notipoavaliacaoanalise
            , p_c_aomprojc.icsolicitacaoreanalise as p_c_aomprojc_icsolicitacaoreanalise
            , ra_aomproj.icjustificativapadraoalterada as ra_aomproj_icjustificativapadrao
            , ra_aomproj.dsjustificativapadrao as ra_aomproj_dsjustificativapadrao
            , ra_aomproj.dsobservacaogeral as ra_aomproj_dsobservacaogeral
            , ra_aomproj.icreanalisado as ra_aomproj_icreanalisado
            , ra_aomproj.dsobservacaopadrao as ra_aomproj_dsobservacaopadrao
            , ra_aomproj.dscaminhoarquivoanalise as ra_aomproj_dscaminhoarquivoanalise
            , ra_aomproj.dsjustificativaparecerdo as ra_aomproj_dsjustificativaparecerdo
            , ra_aomproj.icmantemresposta as ra_aomproj_icmantemresposta
            , ra_aomproj.dsobservacaogeraldo as ra_aomproj_dsobservacaogeraldo
            , ra_aomproj.icmantemrespostaobservacao as ra_aomproj_icmantemrespostaobservacao
            , ra_aomproj.vltotaldeclarado as ra_aomproj_vltotaldeclarado
            , ra_a_proj.ra_japroj_nojustificativaanalise
            , ra_a_proj.ra_japroj_notitulojustificativaanalise
            , ra_a_proj.ra_japroj_nocorpojustificativaanalise
            , ra_a_proj.ra_japroj_norodapejustificativaanalise
            , ra_a_proj.ra_japroj_notitulojustificativagrupoobjetoanaliseindividual
            , ra_a_proj.ra_tjaproj_notipojustificativaanalise
            , ra_taaproj.notipoavaliacaoanalise as ra_taaproj_notipoavaliacaoanalise
            , ra_aomprojc.dsjustificativacontestacao as ra_aomprojc_dsjustificativacontestacao
            , ra_aomprojc.dsjustificativapadrao as ra_aomprojc_dsjustificativapadrao
            , ra_aomprojc.dsconsideracaoobservacaogeral as ra_aomprojc_dsconsideracaoobservacaogeral
            , ra_aomprojc.dsobservacaogeralparecer as ra_aomprojc_dsobservacaogeralparecer
            , ra_aomprojc.dsrecursoadministrativo as ra_aomprojc_dsrecursoadministrativo
            , ra_aomprojc.dsobservacaorecursoadministrativo as ra_aomprojc_dsobservacaorecursoadministrativo
            , ra_taaprojc.notipoavaliacaoanalise as ra_taaprojc_notipoavaliacaoanalise
            , ra_aomprojc.icsolicitacaoreanalise as ra_aomprojc_icsolicitacaoreanalise
            from tbdadoempresamarco dem
            left join listaempresasporanobasesituacaoanalise lst on lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
            left join tbdadoanalisepreenchimento dapree on dapree.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise
            left join tbdadoanaliseprojeto daproj on daproj.idprenchimentosituacaoanalise  = dem.idprenchimentosituacaoanalise
            left join tbdadoanaliseprojetoempresacooperadora dapempcoop on dapempcoop.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
            --
            --DO
            --
            left join tbanaliseobjetomarcoprojeto do_aomproj on do_aomproj.idmarcoanalise = dem.idmarcoanalisedo and do_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbtipoavaliacaoanalise do_taaproj on do_taaproj.idtipoavaliacaoanalise = do_aomproj.idtipoavaliacaoanalise
            left join tbanaliseat do_aat on do_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto and do_aat.idmarcoanalise = dem.idmarcoanalisedo
            left join tbtipoanaliseat do_taat on do_taat.cdtipoanaliseat = do_aat.cdtipoanaliseat 
            left join tbtiporesultadoanaliseat do_traat on do_traat.cdtiporesultadoanalise = do_aat.cdtiporesultadoanalise
            left join tbsituacaoanaliseat do_saat on do_saat.idanaliseat = do_aat.idanaliseat and do_saat.icativo 
            left join tbavaliacaonotaprojeto do_anproj on do_anproj.idanaliseat = do_aat.idanaliseat
            left join tbnotadimensao do_nd1 on do_nd1.cdnotadimensao = do_anproj.cdnotadimensaoinovacao 
            left join tbnotadimensao do_nd2 on do_nd2.cdnotadimensao = do_anproj.cdnotadimensaoresultado  
            left join tbnotadimensao do_nd3 on do_nd3.cdnotadimensao = do_anproj.cdnotafinal 
            left join tbtiposituacaoanalise do_tsa on do_tsa.idtiposituacaoanalise = do_saat.idtiposituacaoanalise
            left join tbsetor do_set on do_set.idsetor = do_saat.idsetor
            left join( 	
                    select 	do_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(do_japroj.nojustificativaanalise,CHR(10)) as do_japroj_nojustificativaanalise
                        ,STRING_AGG(do_japroj.notitulojustificativaanalise,CHR(10)) as do_japroj_notitulojustificativaanalise
                        ,STRING_AGG(do_japroj.nocorpojustificativaanalise,CHR(10)) as do_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(do_japroj.norodapejustificativaanalise,CHR(10)) as do_japroj_norodapejustificativaanalise
                        ,STRING_AGG(do_japroj.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as do_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(do_tjaproj.notipojustificativaanalise,CHR(10)) as do_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa do_aomprojj
                    left join tbjustificativaanalise do_japroj on do_japroj.idjustificativaanalise = do_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise do_tjaproj on do_tjaproj.cdtipojustificativaanalise = do_japroj.cdtipojustificativaanalise
                    group by do_aomprojj.idanaliseobjetomarcoprojeto ) do_a_proj on do_a_proj.idanaliseobjetomarcoprojeto = do_aomproj.idanaliseobjetomarcoprojeto
            --
            --PARECER
            --
            left join tbanaliseobjetomarcoprojeto p_aomproj on p_aomproj.idmarcoanalise = dem.idmarcoanaliseparecer and p_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbtipoavaliacaoanalise p_taaproj on p_taaproj.idtipoavaliacaoanalise = p_aomproj.idtipoavaliacaoanalise
            left join( 	
                    select 	p_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(p_japroj.nojustificativaanalise,CHR(10)) as p_japroj_nojustificativaanalise
                        ,STRING_AGG(p_japroj.notitulojustificativaanalise,CHR(10)) as p_japroj_notitulojustificativaanalise
                        ,STRING_AGG(p_japroj.nocorpojustificativaanalise,CHR(10)) as p_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(p_japroj.norodapejustificativaanalise,CHR(10)) as p_japroj_norodapejustificativaanalise
                        ,STRING_AGG(p_japroj.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as p_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(p_tjaproj.notipojustificativaanalise,CHR(10)) as p_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa p_aomprojj
                    left join tbjustificativaanalise p_japroj on p_japroj.idjustificativaanalise = p_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise p_tjaproj on p_tjaproj.cdtipojustificativaanalise = p_japroj.cdtipojustificativaanalise
                    group by p_aomprojj.idanaliseobjetomarcoprojeto ) p_a_proj on p_a_proj.idanaliseobjetomarcoprojeto = p_aomproj.idanaliseobjetomarcoprojeto
            --
            --DO CONTESTACAO
            --
            left join tbanaliseobjetomarcoprojeto do_c_aomproj on do_c_aomproj.idmarcoanalise = dem.idmarcoanalisedocontestacao and do_c_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbtipoavaliacaoanalise do_c_taaproj on do_c_taaproj.idtipoavaliacaoanalise = do_c_aomproj.idtipoavaliacaoanalise
            left join tbanaliseat do_c_aat on do_c_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto and do_c_aat.idmarcoanalise = dem.idmarcoanalisedocontestacao
            left join tbtipoanaliseat do_c_taat on do_c_taat.cdtipoanaliseat = do_c_aat.cdtipoanaliseat 
            left join tbtiporesultadoanaliseat do_c_traat on do_c_traat.cdtiporesultadoanalise = do_c_aat.cdtiporesultadoanalise
            left join tbsituacaoanaliseat do_c_saat on do_c_saat.idanaliseat = do_c_aat.idanaliseat and do_c_saat.icativo
            left join tbavaliacaonotaprojeto do_c_anproj on do_c_anproj.idanaliseat = do_c_aat.idanaliseat
            left join tbnotadimensao do_c_nd1 on do_c_nd1.cdnotadimensao = do_c_anproj.cdnotadimensaoinovacao 
            left join tbnotadimensao do_c_nd2 on do_c_nd2.cdnotadimensao = do_c_anproj.cdnotadimensaoresultado  
            left join tbnotadimensao do_c_nd3 on do_c_nd3.cdnotadimensao = do_c_anproj.cdnotafinal 
            left join tbtiposituacaoanalise do_c_tsa on do_c_tsa.idtiposituacaoanalise = do_c_saat.idtiposituacaoanalise
            left join tbanaliseobjetomarcoprojetocontestacao do_c_aomprojc on do_c_aomprojc.idmarcoanalise = do_c_aomproj.idmarcoanalise and do_c_aomprojc.idanaliseobjetomarcoprojetocontestacao  = do_c_aomproj.idanaliseobjetomarcoprojeto
            left join tbtipoavaliacaoanalise do_c_taaprojc on do_c_taaprojc.idtipoavaliacaoanalise = do_c_aomprojc.idtipoavaliacaoanalisecontestacao
            left join tbsetor do_c_set on do_c_set.idsetor = do_c_saat.idsetor
            left join( 	
                    select 	do_c_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(do_c_japroj.nojustificativaanalise,CHR(10)) as do_c_japroj_nojustificativaanalise
                        ,STRING_AGG(do_c_japroj.notitulojustificativaanalise,CHR(10)) as do_c_japroj_notitulojustificativaanalise
                        ,STRING_AGG(do_c_japroj.nocorpojustificativaanalise,CHR(10)) as do_c_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(do_c_japroj.norodapejustificativaanalise,CHR(10)) as do_c_japroj_norodapejustificativaanalise
                        ,STRING_AGG(do_c_japroj.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as do_c_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(do_c_tjaproj.notipojustificativaanalise,CHR(10)) as do_c_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa do_c_aomprojj
                    left join tbjustificativaanalise do_c_japroj on do_c_japroj.idjustificativaanalise = do_c_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise do_c_tjaproj on do_c_tjaproj.cdtipojustificativaanalise = do_c_japroj.cdtipojustificativaanalise
                    group by do_c_aomprojj.idanaliseobjetomarcoprojeto ) do_c_a_proj on do_c_a_proj.idanaliseobjetomarcoprojeto = do_c_aomproj.idanaliseobjetomarcoprojeto
            --
            --PARECER CONTESTACAO
            --
            left join tbanaliseobjetomarcoprojeto p_c_aomproj on p_c_aomproj.idmarcoanalise = dem.idmarcoanaliseparecercontestacao and p_c_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbtipoavaliacaoanalise p_c_taaproj on p_c_taaproj.idtipoavaliacaoanalise = p_c_aomproj.idtipoavaliacaoanalise
            left join tbanaliseobjetomarcoprojetocontestacao p_c_aomprojc on p_c_aomprojc.idmarcoanalise = p_c_aomproj.idmarcoanalise and p_c_aomprojc.idanaliseobjetomarcoprojetocontestacao  = p_c_aomproj.idanaliseobjetomarcoprojeto
            left join tbtipoavaliacaoanalise p_c_taaprojc on p_c_taaprojc.idtipoavaliacaoanalise = p_c_aomprojc.idtipoavaliacaoanalisecontestacao
            left join( 	
                    select 	p_c_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(p_c_japroj.nojustificativaanalise,CHR(10)) as p_c_japroj_nojustificativaanalise
                        ,STRING_AGG(p_c_japroj.notitulojustificativaanalise,CHR(10)) as p_c_japroj_notitulojustificativaanalise
                        ,STRING_AGG(p_c_japroj.nocorpojustificativaanalise,CHR(10)) as p_c_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(p_c_japroj.norodapejustificativaanalise,CHR(10)) as p_c_japroj_norodapejustificativaanalise
                        ,STRING_AGG(p_c_japroj.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as p_c_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(p_c_tjaproj.notipojustificativaanalise,CHR(10)) as p_c_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa p_c_aomprojj
                    left join tbjustificativaanalise p_c_japroj on p_c_japroj.idjustificativaanalise = p_c_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise p_c_tjaproj on p_c_tjaproj.cdtipojustificativaanalise = p_c_japroj.cdtipojustificativaanalise
                    group by p_c_aomprojj.idanaliseobjetomarcoprojeto ) p_c_a_proj on p_c_a_proj.idanaliseobjetomarcoprojeto = p_c_aomproj.idanaliseobjetomarcoprojeto
            --
            --RECURSO ADMINISTRATIVO
            --
            left join tbanaliseobjetomarcoprojeto ra_aomproj on ra_aomproj.idmarcoanalise = dem.idmarcoanaliseparecerrecurso and ra_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbtipoavaliacaoanalise ra_taaproj on ra_taaproj.idtipoavaliacaoanalise = ra_aomproj.idtipoavaliacaoanalise
            left join tbanaliseobjetomarcoprojetocontestacao ra_aomprojc on ra_aomprojc.idmarcoanalise = ra_aomproj.idmarcoanalise and ra_aomprojc.idanaliseobjetomarcoprojetocontestacao  = ra_aomproj.idanaliseobjetomarcoprojeto
            left join tbtipoavaliacaoanalise ra_taaprojc on ra_taaprojc.idtipoavaliacaoanalise = ra_aomprojc.idtipoavaliacaoanalisecontestacao
            left join( 	
                    select 	ra_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(ra_japroj.nojustificativaanalise,CHR(10)) as ra_japroj_nojustificativaanalise
                        ,STRING_AGG(ra_japroj.notitulojustificativaanalise,CHR(10)) as ra_japroj_notitulojustificativaanalise
                        ,STRING_AGG(ra_japroj.nocorpojustificativaanalise,CHR(10)) as ra_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(ra_japroj.norodapejustificativaanalise,CHR(10)) as ra_japroj_norodapejustificativaanalise
                        ,STRING_AGG(ra_japroj.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as ra_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(ra_tjaproj.notipojustificativaanalise,CHR(10)) as ra_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa ra_aomprojj
                    left join tbjustificativaanalise ra_japroj on ra_japroj.idjustificativaanalise = ra_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise ra_tjaproj on ra_tjaproj.cdtipojustificativaanalise = ra_japroj.cdtipojustificativaanalise
                    group by ra_aomprojj.idanaliseobjetomarcoprojeto ) ra_a_proj on ra_a_proj.idanaliseobjetomarcoprojeto = ra_aomproj.idanaliseobjetomarcoprojeto
            where lst.nranobase = 2023
            order by dem.idprenchimentosituacaoanalise, daproj.nritem
            """
            
            logger.info("🔍 Executando consulta SQL detalhada (projeto_linha_unica)...")
            
            # Executar query e carregar em DataFrame
            self.df_projetos_detalhado = pd.read_sql_query(query_sql, self.engine)
            
            logger.info(f"✅ Dados detalhados carregados: {len(self.df_projetos_detalhado)} projetos encontrados")
            logger.info(f"📊 Colunas disponíveis: {len(self.df_projetos_detalhado.columns)}")
            
            # Log das empresas encontradas
            if not self.df_projetos_detalhado.empty:
                empresas_encontradas = self.df_projetos_detalhado['lst_norazaosocial'].unique()
                logger.info(f"📋 Amostra de empresas encontradas: {list(empresas_encontradas[:5])}")  # Limitar a 5 para evitar spam
            
            return self.df_projetos_detalhado
            
        except Exception as e:
            logger.error(f"❌ Erro ao executar consulta detalhada: {e}")
            return None
    
    def salvar_dados_detalhados_json(self, nome_arquivo: str = None) -> bool:
        """
        Salva o DataFrame detalhado em formato JSON.
        
        Args:
            nome_arquivo (str): Nome do arquivo (opcional)
        
        Returns:
            bool: True se salvou com sucesso, False caso contrário
        """
        if self.df_projetos_detalhado is None or self.df_projetos_detalhado.empty:
            logger.error("❌ Nenhum dado detalhado disponível para salvar")
            return False
        
        try:
            # Criar diretório json_longo se não existir
            diretorio_destino = "json_longo"
            os.makedirs(diretorio_destino, exist_ok=True)
            
            if not nome_arquivo:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                nome_arquivo = f"projetos_lei_do_bem_2023_DETALHADO_LINHA_UNICA_{timestamp}"
            
            # Converter DataFrame para dicionário
            dados_dict = self.df_projetos_detalhado.to_dict('records')
            
            # JSON compacto - apenas os dados
            arquivo = os.path.join(diretorio_destino, f"{nome_arquivo}.json")
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados_dict, f, ensure_ascii=False, separators=(',', ':'))
            
            # Obter tamanho do arquivo
            tamanho_mb = round(os.path.getsize(arquivo) / 1024 / 1024, 2)
            logger.info(f"💾 Dados detalhados salvos em: {arquivo} ({tamanho_mb} MB)")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar arquivo JSON detalhado: {e}")
            return False


def main():
    """
    Função principal para executar a análise de projetos da Lei do Bem.
    """
    print("🚀 Iniciando análise de projetos da Lei do Bem...")
    print("=" * 60)
    
    # 1. Carregar dados aglomerados
    print("\n📊 CARREGANDO DADOS AGLOMERADOS...")
    carregador_aglomerado = CarregadorDadosAglomeradosLeiDoBem()
    
    if not carregador_aglomerado.conectar_banco():
        print("❌ Falha na conexão com banco. Encerrando...")
        return
    
    df_aglomerado = carregador_aglomerado.carregar_dados()
    if df_aglomerado is None:
        print("❌ Falha ao carregar dados aglomerados. Encerrando...")
        return
    
    # 2. Mostrar informações básicas dos dados aglomerados
    print("\n🔄 PROCESSANDO DADOS AGLOMERADOS...")
    print(f"✅ Dados aglomerados carregados: {len(df_aglomerado)} registros")
    print(f"📊 Colunas disponíveis: {list(df_aglomerado.columns)}")
    
    if not df_aglomerado.empty:
        # Extrair informações das empresas
        empresas_info = df_aglomerado['empresa'].str.extract(r'RAZÃO SOCIAL :([^,]*),')[0].str.strip()
        empresas_unicas = empresas_info.dropna().unique()
        print(f"📋 Total de empresas encontradas: {len(empresas_unicas)}")
        print(f"📋 Amostra de empresas: {list(empresas_unicas[:5])}")
    
    # 3. Salvar dados aglomerados em JSON
    print("\n💾 SALVANDO DADOS AGLOMERADOS EM JSON...")
    
    # Criar diretório json_outputs se não existir
    diretorio_destino = "json_outputs"
    os.makedirs(diretorio_destino, exist_ok=True)
    
    try:
        # Converter DataFrame para dicionário
        dados_dict = df_aglomerado.to_dict('records')
        
        # Salvar JSON
        arquivo_json = os.path.join(diretorio_destino, "projetos_lei_do_bem_2023_AGLOMERADOS.json")
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(dados_dict, f, ensure_ascii=False, separators=(',', ':'))
        
        tamanho_mb = round(os.path.getsize(arquivo_json) / 1024 / 1024, 2)
        print(f"✅ Dados aglomerados salvos em JSON: {arquivo_json} ({tamanho_mb} MB)")
        
    except Exception as e:
        print(f"❌ Erro ao salvar dados aglomerados em JSON: {e}")
    
    # 4. Carregar dados detalhados usando CarregadorDadosLeiDoBem
    print("\n📊 CARREGANDO DADOS DETALHADOS...")
    carregador_detalhado = CarregadorDadosLeiDoBem()
    
    if not carregador_detalhado.conectar_banco():
        print("❌ Falha na conexão com banco para dados detalhados.")
    else:
        df_detalhado = carregador_detalhado.carregar_dados_detalhados()
        if df_detalhado is not None:
            print(f"✅ Dados detalhados carregados: {len(df_detalhado)} registros")
            print(f"📊 Colunas disponíveis: {len(df_detalhado.columns)}")
            
            # Salvar dados detalhados na pasta json_longo
            print("\n💾 SALVANDO DADOS DETALHADOS NA PASTA JSON_LONGO...")
            if carregador_detalhado.salvar_dados_detalhados_json():
                print("✅ Dados detalhados salvos em JSON (json_longo)")
            
            # Também salvar dados detalhados na pasta json_outputs
            print("\n💾 SALVANDO DADOS DETALHADOS NA PASTA JSON_OUTPUTS...")
            
            try:
                # Criar diretório json_outputs se não existir
                diretorio_json_outputs = "json_outputs"
                os.makedirs(diretorio_json_outputs, exist_ok=True)
                
                # Converter DataFrame para dicionário
                dados_detalhados_dict = df_detalhado.to_dict('records')
                
                # Salvar JSON detalhado
                arquivo_json_detalhado = os.path.join(diretorio_json_outputs, "projetos_lei_do_bem_2023_DETALHADO_TODAS_AS_EMPRESAS.json")
                with open(arquivo_json_detalhado, 'w', encoding='utf-8') as f:
                    json.dump(dados_detalhados_dict, f, ensure_ascii=False, separators=(',', ':'))
                
                tamanho_mb_detalhado = round(os.path.getsize(arquivo_json_detalhado) / 1024 / 1024, 2)
                print(f"✅ Dados detalhados salvos em JSON (json_outputs): {arquivo_json_detalhado} ({tamanho_mb_detalhado} MB)")
                
            except Exception as e:
                print(f"❌ Erro ao salvar dados detalhados em JSON (json_outputs): {e}")
        else:
            print("❌ Falha ao carregar dados detalhados")
    
    print("\n🎉 Análise concluída!")
    print("=" * 60)
    print("📁 Arquivos aglomerados salvos no diretório: json_outputs/")
    print("📁 Arquivos detalhados salvos no diretório: json_longo/")
    print("📋 Verifique os arquivos gerados para análise posterior.")


if __name__ == "__main__":
    main()
