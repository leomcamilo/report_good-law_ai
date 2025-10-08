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
        Executa a consulta SQL detalhada (projeto_linha_unica.sql) e carrega os dados em um DataFrame pandas.
        
        Returns:
            pd.DataFrame: DataFrame com os dados detalhados dos projetos ou None se erro
        """
        if not self.engine:
            logger.error("❌ Conexão com banco não estabelecida")
            return None
            
        try:
            # Query SQL para carregar TODOS os dados da base (sem filtros)
            query_sql = """
            SELECT 
                lst.idprenchimentosituacaoanalise as id_empresa_ano,
                lst.nranobase as ano_referencia,
                lst.norazaosocial as empresa_razao_social,
                lst.nrcnpj as cnpj,
                lst.noatividadeeconomica as atividade_economica,
                lst.cdatividadeeconomicaibge as codigo_atividade_ibge,
                lst.notipoportepessoajuridica as porte_empresa,
                daproj.nritem as numero_projeto,
                daproj.iddadoanaliseprojeto as id_projeto,
                daproj.noprojeto as nome_projeto,
                daproj.dsprojeto as descricao_projeto,
                daproj.tppbpade as tipo_projeto,
                daproj.dsareaprojeto as area_projeto,
                daproj.dspalavrachave as palavras_chave,
                daproj.tpnatureza as natureza,
                daproj.dselementotecnologico as elemento_tecnologico,
                daproj.dsdesafiotecnologico as desafio_tecnologico,
                daproj.dsmetodologiautilizada as metodologia,
                daproj.dsinformacaocomplementar as informacao_complementar,
                daproj.dsresultadoeconomico as resultado_economico,
                daproj.dsresultadoinovacao as resultado_inovacao,
                daproj.dsrecursoshumanos as descricao_rh,
                daproj.dsrecursosmateriais as descricao_materiais,
                daproj.icciclomaior as ciclo_maior_1_ano,
                daproj.dsatividadepdicontinuadaanobase as atividade_pdi_continuada,
                do_set.nosetor as setor_analise
            FROM tbdadoempresamarco dem
            LEFT JOIN listaempresasporanobasesituacaoanalise lst ON lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
            LEFT JOIN tbdadoanaliseprojeto daproj ON daproj.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise
            LEFT JOIN tbanaliseobjetomarcoprojeto do_aomproj ON do_aomproj.idmarcoanalise = dem.idmarcoanalisedo AND do_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
            LEFT JOIN tbanaliseat do_aat ON do_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto AND do_aat.idmarcoanalise = dem.idmarcoanalisedo
            LEFT JOIN tbsituacaoanaliseat do_saat ON do_saat.idanaliseat = do_aat.idanaliseat AND do_saat.icativo 
            LEFT JOIN tbsetor do_set ON do_set.idsetor = do_saat.idsetor
            WHERE lst.nranobase IS NOT NULL
            ORDER BY lst.idprenchimentosituacaoanalise, daproj.nritem;
            """
            
            logger.info("🔍 Executando consulta SQL detalhada...")
            
            # Executar query e carregar em DataFrame usando o método correto
            with self.engine.connect() as conn:
                self.df_projetos_detalhado = pd.read_sql(text(query_sql), conn)
            
            logger.info(f"✅ Dados detalhados carregados: {len(self.df_projetos_detalhado)} projetos encontrados")
            logger.info(f"📊 Colunas disponíveis: {len(self.df_projetos_detalhado.columns)}")
            
            # Log das estatísticas gerais
            if not self.df_projetos_detalhado.empty:
                empresas_encontradas = self.df_projetos_detalhado['empresa_razao_social'].nunique()
                anos_encontrados = self.df_projetos_detalhado['ano_referencia'].nunique()
                logger.info(f"📋 Total de empresas únicas: {empresas_encontradas}")
                logger.info(f"📅 Anos de referência: {sorted(self.df_projetos_detalhado['ano_referencia'].dropna().unique())}")
            
            return self.df_projetos_detalhado
            
        except Exception as e:
            logger.error(f"❌ Erro ao executar consulta detalhada: {e}")
            return None


def main():
    """
    Função principal para executar a análise de projetos da Lei do Bem.
    """
    print("🚀 Iniciando importação completa de projetos da Lei do Bem...")
    print("=" * 60)
    
    # Carregar TODOS os dados
    print("\n📊 CARREGANDO TODOS OS DADOS DA BASE...")
    carregador = CarregadorDadosLeiDoBem()
    
    if not carregador.conectar_banco():
        print("❌ Falha na conexão com banco. Encerrando...")
        return
    
    df_detalhado = carregador.carregar_dados_detalhados()
    if df_detalhado is None:
        print("❌ Falha ao carregar dados detalhados. Encerrando...")
        return
    
    print(f"✅ TODOS os dados carregados: {len(df_detalhado)} registros")
    print(f"📊 Colunas disponíveis: {len(df_detalhado.columns)}")
    
    # Mostrar informações básicas dos dados
    if not df_detalhado.empty:
        empresas_unicas = df_detalhado['empresa_razao_social'].nunique()
        anos_referencia = sorted(df_detalhado['ano_referencia'].dropna().unique())
        projetos_com_setor = df_detalhado['setor_analise'].notna().sum()
        
        print(f"📋 Total de empresas únicas: {empresas_unicas}")
        print(f"📅 Anos de referência: {anos_referencia}")
        print(f"📊 Projetos com setor de análise: {projetos_com_setor}")
        print(f"💼 Tipos de empresa: {df_detalhado['porte_empresa'].value_counts().to_dict()}")
        
        # Mostrar informações sobre as colunas
        print("\n📋 Informações sobre as colunas:")
        print(f"📊 Shape do DataFrame: {df_detalhado.shape}")
        print(f"💾 Tamanho estimado em memória: {df_detalhado.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
    
    # Salvar TODOS os dados
    print("\n💾 SALVANDO TODOS OS DADOS...")
    
    # Criar diretório csv_longo se não existir
    diretorio_csv_longo = "csv_longo"
    os.makedirs(diretorio_csv_longo, exist_ok=True)
    
    try:
        # Salvar arquivo CSV completo na pasta csv_longo
        arquivo_csv_longo = os.path.join(diretorio_csv_longo, "projetos_resultados_pessoas_valores.csv")
        df_detalhado.to_csv(arquivo_csv_longo, index=False, encoding='utf-8', sep=';')
        
        # Verificar o tamanho do arquivo salvo
        tamanho_arquivo = os.path.getsize(arquivo_csv_longo) / 1024 / 1024
        print(f"✅ TODOS os dados salvos em: {arquivo_csv_longo}")
        print(f"📁 Tamanho do arquivo: {tamanho_arquivo:.2f} MB")
        
        # Estatísticas finais
        print("\n📊 ESTATÍSTICAS FINAIS:")
        print(f"📋 Total de registros salvos: {len(df_detalhado):,}")
        print(f"📋 Total de empresas únicas: {df_detalhado['empresa_razao_social'].nunique():,}")
        print(f"📋 Total de projetos únicos: {df_detalhado['id_projeto'].nunique():,}")
        
    except Exception as e:
        print(f"❌ Erro ao salvar dados completos: {e}")
    
    print("\n🎉 Importação completa concluída!")
    print("=" * 60)
    print("📁 TODOS os dados salvos no diretório: csv_longo/")
    print("📋 Arquivo completo pronto para análises subsequentes.")


if __name__ == "__main__":
    main()
