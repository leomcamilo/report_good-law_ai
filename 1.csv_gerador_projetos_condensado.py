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
import os

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Suprimir warnings do pandas
warnings.filterwarnings('ignore')

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
                
            logger.info("✅ Conexão com banco estabelecida com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao conectar com banco: {e}")
            return False
    
    def carregar_dados_detalhados(self) -> Optional[pd.DataFrame]:
        """
        Executa a consulta SQL detalhada (projeto_justificativas_resultados_pessoas.sql) e carrega os dados em um DataFrame pandas.
        
        Returns:
            pd.DataFrame: DataFrame com os dados detalhados dos projetos ou None se erro
        """
        if not self.engine:
            logger.error("❌ Conexão com banco não estabelecida")
            return None
            
        try:
            # Query SQL baseada no arquivo projeto_justificativas_resultados_pessoas.sql
            query_sql = """
            select lst.idprenchimentosituacaoanalise as id_empresa_ano
            , lst.nranobase as ano_referencia
            --
            -- Projeto - caracterização
            --
            , do_setor.nosetor as setor
            , daproj.tpnatureza as natureza
            , daproj.tppbpade as tipo_pesquisa
            , concat('CNPJ: '::text , lst.nrcnpj::text ,' RAZÃO SOCIAL:'::text , lst.norazaosocial::text, ' ATIVIDADE ECONOMICA:'::text, lst.noatividadeeconomica::text,' Cd ATIV.ECONOMICA IBGE:'::text, lst.cdatividadeeconomicaibge::text, ' PORTE:'::text, lst.notipoportepessoajuridica::text, ' ID EMPRESA/ANO:'::text, lst.idprenchimentosituacaoanalise) as Empresa
            , concat('NÚMERO: '::text, daproj.nritem::text ,' ID ÚNICO: '::text, daproj.iddadoanaliseprojeto::text ,' NOME: '::text, daproj.noprojeto::text ,' DESCRIÇÂO: '::text, daproj.dsprojeto::text ,' AREA: '::text, daproj.dsareaprojeto::text ,' PALAVRAS CHAVE: '::text, daproj.dspalavrachave::text ,' ELEMENTO TECNOLÓGICO: '::text, daproj.dselementotecnologico::text ,' DESAFIO TECNOLÓGICO: '::text, daproj.dsdesafiotecnologico::text ,' METODOLOGIA: '::text, daproj.dsmetodologiautilizada::text ,' INFORMAÇÃO COMPLEMENTAR: '::text, daproj.dsinformacaocomplementar::text  ) as projeto
            , concat('CICLO MAIOR QUE 1 ANO: '::text, daproj.icciclomaior::text , ' ATIVIDADE PDI CONTINUADA ANO ANTERIOR :'::text, daproj.dsatividadepdicontinuadaanobase::text) as projeto_multianual
            , concat('ECONOMICO: '::text, daproj.dsresultadoeconomico::text ,' INOVACAO: '::text, daproj.dsresultadoinovacao::text ) as projeto_resultados
            --
            -- DO analise
            --
            , do_comite.nocomite as do_comite
            , do_saat.idunicopessoaanalise as do_id_at
            , do_nd1.dsnotadimensao as do_relevancia_invocao
            , do_nd2.dsnotadimensao as do_relevancia_resultado
            , do_nd3.dsnotadimensao as do_relevancia_final
            , concat( do_aomproj.dsobservacaogeral::text,' / ' ,do_aomproj.dsobservacaopadrao::text) as do_observacao
            , do_aomproj.dsjustificativapadrao as do_justificativa_livre
            , concat(do_a_proj.do_japroj_nojustificativaanalise::text,' / '::text, do_a_proj.do_japroj_notitulojustificativaanalise::text,' / '::text, do_a_proj.do_japroj_nocorpojustificativaanalise::text,' / '::text, do_a_proj.do_japroj_norodapejustificativaanalise::text,' / '::text, do_a_proj.do_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as do_justificativa_padronizada
            , do_a_proj.do_tjaproj_notipojustificativaanalise as do_tipo_justificativa
            , do_taaproj.notipoavaliacaoanalise as do_resultado_analise
            --
            -- Parecer
            --
            , p_hsa.idunicopessoa as p_id_analista_mcti
            , concat( p_aomproj.dsobservacaogeral::text,' / ' ,p_aomproj.dsobservacaopadrao::text) as p_observacao
            , p_aomproj.dsjustificativapadrao as p_justificativa_livre
            , concat(p_a_proj.p_japroj_nojustificativaanalise::text,' / '::text, p_a_proj.p_japroj_notitulojustificativaanalise::text,' / '::text, p_a_proj.p_japroj_nocorpojustificativaanalise::text,' / '::text, p_a_proj.p_japroj_norodapejustificativaanalise::text,' / '::text, p_a_proj.p_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as p_justificativa_padronizada
            , p_a_proj.p_tjaproj_notipojustificativaanalise as p_tipo_justificativa
            , p_taaproj.notipoavaliacaoanalise as p_resultado_analise
            --
            -- DO contestacao
            --
            , do_c_aomprojc.dsjustificativacontestacao as empresa_do_contestacao
            , do_c_comite.nocomite as do_c_comite
            , do_c_saat.idunicopessoaanalise as do_c_id_at
            , do_c_nd1.dsnotadimensao as do_c_relevancia_invocao
            , do_c_nd2.dsnotadimensao as do_c_relevancia_resultado
            , do_c_nd3.dsnotadimensao as do_c_relevancia_final
            , concat( do_c_aomproj.dsobservacaogeral::text,' / ' ,do_c_aomproj.dsobservacaopadrao::text) as do_c_observacao
            , do_c_aomproj.dsjustificativapadrao as do_c_justificativa_livre
            , concat(do_c_a_proj.do_c_japroj_nojustificativaanalise::text,' / '::text, do_c_a_proj.do_c_japroj_notitulojustificativaanalise::text,' / '::text, do_c_a_proj.do_c_japroj_nocorpojustificativaanalise::text,' / '::text, do_c_a_proj.do_c_japroj_norodapejustificativaanalise::text,' / '::text, do_c_a_proj.do_c_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as do_c_justificativa_padronizada
            , do_c_a_proj.do_c_tjaproj_notipojustificativaanalise as do_c_tipo_justificativa
            , do_c_taaproj.notipoavaliacaoanalise as do_c_resultado_analise
            --
            -- Parecer contestacao
            --
            , p_c_aomprojc.dsjustificativacontestacao as empresa_parecer_contestacao
            , p_c_hsa.idunicopessoa as p_c_id_analista_mcti
            , concat( p_c_aomproj.dsobservacaogeral::text,' / ' ,p_c_aomproj.dsobservacaopadrao::text) as p_c_observacao
            , p_c_aomproj.dsjustificativapadrao as p_c_justificativa_livre
            , concat(p_c_a_proj.p_c_japroj_nojustificativaanalise::text,' / '::text, p_c_a_proj.p_c_japroj_notitulojustificativaanalise::text,' / '::text, p_c_a_proj.p_c_japroj_nocorpojustificativaanalise::text,' / '::text, p_c_a_proj.p_c_japroj_norodapejustificativaanalise::text,' / '::text, p_c_a_proj.p_c_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as p_c_justificativa_padronizada
            , p_c_a_proj.p_c_tjaproj_notipojustificativaanalise as p_c_tipo_justificativa
            , p_c_taaproj.notipoavaliacaoanalise as p_c_resultado_analise
            --
            -- Recurso Administrativo
            --
            , ra_aomprojc.dsrecursoadministrativo as empresa_recurso_administrativo
            , ra_hsa.idunicopessoa as ra_id_analista_mcti
            , concat( ra_aomproj.dsobservacaogeral::text,' / ' ,ra_aomproj.dsobservacaopadrao::text) as ra_observacao
            , ra_aomproj.dsjustificativapadrao as ra_justificativa_livre
            , concat(ra_a_proj.ra_japroj_nojustificativaanalise::text,' / '::text, ra_a_proj.ra_japroj_notitulojustificativaanalise::text,' / '::text, ra_a_proj.ra_japroj_nocorpojustificativaanalise::text,' / '::text, ra_a_proj.ra_japroj_norodapejustificativaanalise::text,' / '::text, ra_a_proj.ra_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as ra_justificativa_padronizada
            , ra_a_proj.ra_tjaproj_notipojustificativaanalise as ra_tipo_justificativa
            , ra_taaproj.notipoavaliacaoanalise as ra_resultado_analise
            from tbdadoanaliseprojeto daproj
            left join tbdadoempresamarco dem on dem.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise 
            left join listaempresasporanobasesituacaoanalise lst on lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
            --
            -- DO
            --
            left join tbmarcoanalise do_ma on do_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanalisedo = do_ma.idmarcoanalise
            left join tbanaliseat do_aat on do_aat.idmarcoanalise = do_ma.idmarcoanalise and do_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbsituacaoanaliseat do_saat on do_saat.idanaliseat = do_aat.idanaliseat and do_saat.icativo 
            left join tbsetor do_setor on do_setor.idsetor = do_saat.idsetor 
            left join tbcomite do_comite on do_comite.idcomite = do_saat.idapoiotecnico 
            left join tbavaliacaonotaprojeto do_anproj on do_anproj.idanaliseat = do_aat.idanaliseat
            left join tbanaliseobjetomarcoprojeto do_aomproj on do_aomproj.idmarcoanalise = do_ma.idmarcoanalise and do_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
            left join tbnotadimensao do_nd1 on do_nd1.cdnotadimensao = do_anproj.cdnotadimensaoinovacao 
            left join tbnotadimensao do_nd2 on do_nd2.cdnotadimensao = do_anproj.cdnotadimensaoresultado  
            left join tbnotadimensao do_nd3 on do_nd3.cdnotadimensao = do_anproj.cdnotafinal
            left join tbtipoavaliacaoanalise do_taaproj on do_taaproj.idtipoavaliacaoanalise = do_aomproj.idtipoavaliacaoanalise
            left join( 	
                    select 	do_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(do_japroj.nojustificativaanalise,' || ') as do_japroj_nojustificativaanalise
                        ,STRING_AGG(do_japroj.notitulojustificativaanalise,' || ') as do_japroj_notitulojustificativaanalise
                        ,STRING_AGG(do_japroj.nocorpojustificativaanalise,' || ') as do_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(do_japroj.norodapejustificativaanalise,' || ') as do_japroj_norodapejustificativaanalise
                        ,STRING_AGG(do_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as do_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(do_tjaproj.notipojustificativaanalise,' || ') as do_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa do_aomprojj
                    left join tbjustificativaanalise do_japroj on do_japroj.idjustificativaanalise = do_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise do_tjaproj on do_tjaproj.cdtipojustificativaanalise = do_japroj.cdtipojustificativaanalise
                    group by do_aomprojj.idanaliseobjetomarcoprojeto ) do_a_proj on do_a_proj.idanaliseobjetomarcoprojeto = do_aomproj.idanaliseobjetomarcoprojeto
            --
            --PARECER
            --
            left join tbmarcoanalise p_ma on p_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanaliseparecer = p_ma.idmarcoanalise
            left join tbanaliseobjetomarcoprojeto p_aomproj on p_aomproj.idmarcoanalise = p_ma.idmarcoanalise and p_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbtipoavaliacaoanalise p_taaproj on p_taaproj.idtipoavaliacaoanalise = p_aomproj.idtipoavaliacaoanalise
            left join( 	
                    select 	p_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(p_japroj.nojustificativaanalise,' || ') as p_japroj_nojustificativaanalise
                        ,STRING_AGG(p_japroj.notitulojustificativaanalise,' || ') as p_japroj_notitulojustificativaanalise
                        ,STRING_AGG(p_japroj.nocorpojustificativaanalise,' || ') as p_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(p_japroj.norodapejustificativaanalise,' || ') as p_japroj_norodapejustificativaanalise
                        ,STRING_AGG(p_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as p_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(p_tjaproj.notipojustificativaanalise,' || ') as p_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa p_aomprojj
                    left join tbjustificativaanalise p_japroj on p_japroj.idjustificativaanalise = p_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise p_tjaproj on p_tjaproj.cdtipojustificativaanalise = p_japroj.cdtipojustificativaanalise
                    group by p_aomprojj.idanaliseobjetomarcoprojeto ) p_a_proj on p_a_proj.idanaliseobjetomarcoprojeto = p_aomproj.idanaliseobjetomarcoprojeto		
            left join(
                    select hsa1.idhistoricosituacaoanalise, hsa1.idmarcoanalise, hsa1.idunicopessoa 
                    from tbhistoricosituacaoanalise hsa1
                    where hsa1.idhistoricosituacaoanalise in 
                    (	select max(hsa2.idhistoricosituacaoanalise )
                        from tbhistoricosituacaoanalise hsa2
                        where hsa2.cdtiposituacaomarco = 2
                        group by hsa2.idmarcoanalise )		
                    ) p_hsa on p_hsa.idmarcoanalise = p_ma.idmarcoanalise 
            --
            --DO CONTESTACAO
            --
            left join tbmarcoanalise do_c_ma on do_c_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanalisedocontestacao = do_c_ma.idmarcoanalise
            left join tbanaliseat do_c_aat on do_c_aat.idmarcoanalise = do_c_ma.idmarcoanalise and do_c_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbsituacaoanaliseat do_c_saat on do_c_saat.idanaliseat = do_c_aat.idanaliseat and do_c_saat.icativo 
            left join tbsetor do_c_setor on do_c_setor.idsetor = do_c_saat.idsetor 
            left join tbcomite do_c_comite on do_c_comite.idcomite = do_c_saat.idapoiotecnico 
            left join tbavaliacaonotaprojeto do_c_anproj on do_c_anproj.idanaliseat = do_c_aat.idanaliseat
            left join tbanaliseobjetomarcoprojeto do_c_aomproj on do_c_aomproj.idmarcoanalise = do_c_ma.idmarcoanalise and do_c_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
            left join tbnotadimensao do_c_nd1 on do_c_nd1.cdnotadimensao = do_c_anproj.cdnotadimensaoinovacao 
            left join tbnotadimensao do_c_nd2 on do_c_nd2.cdnotadimensao = do_c_anproj.cdnotadimensaoresultado  
            left join tbnotadimensao do_c_nd3 on do_c_nd3.cdnotadimensao = do_c_anproj.cdnotafinal
            left join tbtipoavaliacaoanalise do_c_taaproj on do_c_taaproj.idtipoavaliacaoanalise = do_c_aomproj.idtipoavaliacaoanalise
            left join tbanaliseobjetomarcoprojetocontestacao do_c_aomprojc on do_c_aomprojc.idmarcoanalise = do_c_aomproj.idmarcoanalise and do_c_aomprojc.idanaliseobjetomarcoprojetocontestacao = do_c_aomproj.idanaliseobjetomarcoprojeto
            left join tbtipoavaliacaoanalise do_c_taaprojc on do_c_taaprojc.idtipoavaliacaoanalise = do_c_aomprojc.idtipoavaliacaoanalisecontestacao
            left join( 	
                    select 	do_c_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(do_c_japroj.nojustificativaanalise,' || ') as do_c_japroj_nojustificativaanalise
                        ,STRING_AGG(do_c_japroj.notitulojustificativaanalise,' || ') as do_c_japroj_notitulojustificativaanalise
                        ,STRING_AGG(do_c_japroj.nocorpojustificativaanalise,' || ') as do_c_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(do_c_japroj.norodapejustificativaanalise,' || ') as do_c_japroj_norodapejustificativaanalise
                        ,STRING_AGG(do_c_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as do_c_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(do_c_tjaproj.notipojustificativaanalise,' || ') as do_c_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa do_c_aomprojj
                    left join tbjustificativaanalise do_c_japroj on do_c_japroj.idjustificativaanalise = do_c_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise do_c_tjaproj on do_c_tjaproj.cdtipojustificativaanalise = do_c_japroj.cdtipojustificativaanalise
                    group by do_c_aomprojj.idanaliseobjetomarcoprojeto ) do_c_a_proj on do_c_a_proj.idanaliseobjetomarcoprojeto = do_c_aomproj.idanaliseobjetomarcoprojeto
            --
            --PARECER CONTESTACAO
            --
            left join tbmarcoanalise p_c_ma on p_c_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanaliseparecercontestacao = p_c_ma.idmarcoanalise
            left join tbanaliseobjetomarcoprojeto p_c_aomproj on p_c_aomproj.idmarcoanalise = p_c_ma.idmarcoanalise and p_c_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbtipoavaliacaoanalise p_c_taaproj on p_c_taaproj.idtipoavaliacaoanalise = p_c_aomproj.idtipoavaliacaoanalise
            --
            left join tbanaliseobjetomarcoprojetocontestacao p_c_aomprojc on p_c_aomprojc.idmarcoanalise = p_c_aomproj.idmarcoanalise and p_c_aomprojc.idanaliseobjetomarcoprojetocontestacao  = p_c_aomproj.idanaliseobjetomarcoprojeto
            left join tbtipoavaliacaoanalise p_c_taaprojc on p_c_taaprojc.idtipoavaliacaoanalise = p_c_aomprojc.idtipoavaliacaoanalisecontestacao
            left join( 	
                    select 	p_c_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(p_c_japroj.nojustificativaanalise,' || ') as p_c_japroj_nojustificativaanalise
                        ,STRING_AGG(p_c_japroj.notitulojustificativaanalise,' || ') as p_c_japroj_notitulojustificativaanalise
                        ,STRING_AGG(p_c_japroj.nocorpojustificativaanalise,' || ') as p_c_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(p_c_japroj.norodapejustificativaanalise,' || ') as p_c_japroj_norodapejustificativaanalise
                        ,STRING_AGG(p_c_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as p_c_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(p_c_tjaproj.notipojustificativaanalise,' || ') as p_c_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa p_c_aomprojj
                    left join tbjustificativaanalise p_c_japroj on p_c_japroj.idjustificativaanalise = p_c_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise p_c_tjaproj on p_c_tjaproj.cdtipojustificativaanalise = p_c_japroj.cdtipojustificativaanalise
                    group by p_c_aomprojj.idanaliseobjetomarcoprojeto ) p_c_a_proj on p_c_a_proj.idanaliseobjetomarcoprojeto = p_c_aomproj.idanaliseobjetomarcoprojeto		
            left join(
                    select hsa1.idhistoricosituacaoanalise, hsa1.idmarcoanalise, hsa1.idunicopessoa 
                    from tbhistoricosituacaoanalise hsa1
                    where hsa1.idhistoricosituacaoanalise in 
                    (	select max(hsa2.idhistoricosituacaoanalise )
                        from tbhistoricosituacaoanalise hsa2
                        where hsa2.cdtiposituacaomarco = 15
                        group by hsa2.idmarcoanalise )		
                    ) p_c_hsa on p_c_hsa.idmarcoanalise = p_c_ma.idmarcoanalise 
            --
            --RECURSO ADMINISTRATIVO
            --
            left join tbmarcoanalise ra_ma on ra_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanaliseparecercontestacao = ra_ma.idmarcoanalise
            left join tbanaliseobjetomarcoprojeto ra_aomproj on ra_aomproj.idmarcoanalise = ra_ma.idmarcoanalise and ra_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            left join tbtipoavaliacaoanalise ra_taaproj on ra_taaproj.idtipoavaliacaoanalise = ra_aomproj.idtipoavaliacaoanalise
            --
            left join tbanaliseobjetomarcoprojetocontestacao ra_aomprojc on ra_aomprojc.idmarcoanalise = ra_aomproj.idmarcoanalise and ra_aomprojc.idanaliseobjetomarcoprojetocontestacao  = ra_aomproj.idanaliseobjetomarcoprojeto
            left join tbtipoavaliacaoanalise ra_taaprojc on ra_taaprojc.idtipoavaliacaoanalise = ra_aomprojc.idtipoavaliacaoanalisecontestacao
            left join( 	
                    select 	ra_aomprojj.idanaliseobjetomarcoprojeto
                        ,STRING_AGG(ra_japroj.nojustificativaanalise,' || ') as ra_japroj_nojustificativaanalise
                        ,STRING_AGG(ra_japroj.notitulojustificativaanalise,' || ') as ra_japroj_notitulojustificativaanalise
                        ,STRING_AGG(ra_japroj.nocorpojustificativaanalise,' || ') as ra_japroj_nocorpojustificativaanalise
                        ,STRING_AGG(ra_japroj.norodapejustificativaanalise,' || ') as ra_japroj_norodapejustificativaanalise
                        ,STRING_AGG(ra_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as ra_japroj_notitulojustificativagrupoobjetoanaliseindividual
                        ,STRING_AGG(ra_tjaproj.notipojustificativaanalise,' || ') as ra_tjaproj_notipojustificativaanalise
                    from tbanaliseobjetomarcoprojetojustificativa ra_aomprojj
                    left join tbjustificativaanalise ra_japroj on ra_japroj.idjustificativaanalise = ra_aomprojj.idjustificativaanalise
                    left join tbtipojustificativaanalise ra_tjaproj on ra_tjaproj.cdtipojustificativaanalise = ra_japroj.cdtipojustificativaanalise
                    group by ra_aomprojj.idanaliseobjetomarcoprojeto ) ra_a_proj on ra_a_proj.idanaliseobjetomarcoprojeto = ra_aomproj.idanaliseobjetomarcoprojeto		
            left join(
                    select hsa1.idhistoricosituacaoanalise, hsa1.idmarcoanalise, hsa1.idunicopessoa 
                    from tbhistoricosituacaoanalise hsa1
                    where hsa1.idhistoricosituacaoanalise in 
                    (	select max(hsa2.idhistoricosituacaoanalise )
                        from tbhistoricosituacaoanalise hsa2
                        where hsa2.cdtiposituacaomarco = 36
                        group by hsa2.idmarcoanalise )		
                    ) ra_hsa on ra_hsa.idmarcoanalise = ra_ma.idmarcoanalise 
            --where lst.nranobase = 2020
            """
            
            logger.info("🔍 Executando consulta SQL detalhada...")
            
            # Executar query e carregar em DataFrame
            self.df_projetos_detalhado = pd.read_sql_query(query_sql, self.engine)
            
            logger.info(f"✅ Dados detalhados carregados: {len(self.df_projetos_detalhado)} projetos encontrados")
            logger.info(f"📊 Colunas disponíveis: {len(self.df_projetos_detalhado.columns)}")
            
            # Log das empresas encontradas
            if not self.df_projetos_detalhado.empty:
                empresas_encontradas = self.df_projetos_detalhado['empresa'].unique()
                logger.info(f"📋 Amostra de empresas encontradas: {list(empresas_encontradas[:5])}")
            
            return self.df_projetos_detalhado
            
        except Exception as e:
            logger.error(f"❌ Erro ao executar consulta detalhada: {e}")
            return None


def main():
    """
    Função principal para executar a análise de projetos da Lei do Bem.
    """
    print("🚀 Iniciando análise de projetos da Lei do Bem...")
    print("=" * 60)
    
    # Carregar dados detalhados
    print("\n📊 CARREGANDO DADOS DETALHADOS...")
    carregador = CarregadorDadosLeiDoBem()
    
    if not carregador.conectar_banco():
        print("❌ Falha na conexão com banco. Encerrando...")
        return
    
    df_detalhado = carregador.carregar_dados_detalhados()
    if df_detalhado is None:
        print("❌ Falha ao carregar dados detalhados. Encerrando...")
        return
    
    print(f"✅ Dados detalhados carregados: {len(df_detalhado)} registros")
    print(f"📊 Colunas disponíveis: {len(df_detalhado.columns)}")
    
    # Mostrar informações básicas dos dados
    if not df_detalhado.empty:
        empresas_unicas = df_detalhado['empresa'].unique()
        print(f"📋 Total de empresas encontradas: {len(empresas_unicas)}")
        print(f"📋 Amostra de empresas: {list(empresas_unicas[:5])}")
    
    # Salvar dados detalhados
    print("\n💾 SALVANDO DADOS DETALHADOS...")
    
    # Criar diretório csv_longo se não existir
    diretorio_csv_longo = "csv_longo"
    os.makedirs(diretorio_csv_longo, exist_ok=True)
    
    try:
        # Salvar arquivo CSV na pasta csv_longo
        arquivo_csv_longo = os.path.join(diretorio_csv_longo, "projetos_lei_do_bem_JUSTIFICATIVAS_RESULTADOS_PESSOAS.csv")
        df_detalhado.to_csv(arquivo_csv_longo, index=False, encoding='utf-8', sep=';')
        print(f"✅ Dados detalhados salvos em: {arquivo_csv_longo}")
        
    except Exception as e:
        print(f"❌ Erro ao salvar dados detalhados: {e}")
    
    print("\n🎉 Análise concluída!")
    print("=" * 60)
    print("📁 Dados detalhados salvos no diretório: csv_longo/")
    print("📋 Arquivo pronto para próximas etapas do pipeline.")


if __name__ == "__main__":
    main()
