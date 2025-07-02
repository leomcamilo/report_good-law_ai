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

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Suprimir warnings do pandas
warnings.filterwarnings('ignore')

class CarregadorDadosLeiDoBem:
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
                empresas_encontradas = self.df_projetos['empresa'].str.extract(r'RAZÃO SOCIAL :([^A-Z]*?)(?=[A-Z]|$)')[0].str.strip().unique()
                logger.info(f"📋 Amostra de empresas encontradas: {list(empresas_encontradas[:5])}")  # Limitar a 5 para evitar spam
            
            return self.df_projetos
            
        except Exception as e:
            logger.error(f"❌ Erro ao executar consulta: {e}")
            return None

class AnalisadorProjetosLeiDoBem:
    """Classe para análise de projetos da Lei do Bem usando dados do PostgreSQL."""
    
    def __init__(self):
        """Inicializa o analisador."""
        self.df_projetos = None
        self.empresas_filtro = None
    
    def processar_dados(self) -> Dict[str, Any]:
        """
        Processa e analisa os dados carregados.
        
        Returns:
            Dict: Dicionário com estatísticas e insights dos dados
        """
        if self.df_projetos is None or self.df_projetos.empty:
            logger.error("❌ Nenhum dado disponível para processamento")
            return {}
        
        logger.info("🔄 Processando dados...")
        
        # Estatísticas básicas simples
        stats = {
            'total_projetos': len(self.df_projetos),
            'total_empresas': self.df_projetos['id_empresa_ano'].nunique(),
            'ano_base': self.df_projetos['ano_referencia'].iloc[0] if not self.df_projetos.empty else None
        }
        
        # Extrair razão social das empresas da coluna concatenada
        razoes_sociais = self.df_projetos['empresa'].str.extract(r'RAZÃO SOCIAL :([^A-Z]*?)(?=[A-Z]|$)')[0].str.strip()
        empresas_stats = razoes_sociais.value_counts()
        stats['distribuicao_empresas'] = empresas_stats.to_dict()
        
        logger.info("✅ Processamento concluído")
        return stats
    
    def salvar_dados(self, formato: str = 'csv', nome_arquivo: str = None) -> bool:
        """
        Salva o DataFrame em arquivo.
        
        Args:
            formato (str): Formato do arquivo ('csv', 'excel', 'parquet')
            nome_arquivo (str): Nome do arquivo (opcional)
        
        Returns:
            bool: True se salvou com sucesso, False caso contrário
        """
        if self.df_projetos is None or self.df_projetos.empty:
            logger.error("❌ Nenhum dado disponível para salvar")
            return False
        
        try:
            # Criar diretório tabelas_csv_xlsx se não existir
            import os
            diretorio_destino = "tabelas_csv_xlsx"
            os.makedirs(diretorio_destino, exist_ok=True)
            
            if not nome_arquivo:
                empresas_filtradas = "_".join([emp.replace('%', '').replace(' ', '_').upper() for emp in self.empresas_filtro[:2]])
                nome_arquivo = f"projetos_lei_do_bem_2023_{empresas_filtradas}"
            
            if formato.lower() == 'csv':
                arquivo = os.path.join(diretorio_destino, f"{nome_arquivo}.csv")
                self.df_projetos.to_csv(arquivo, index=False, encoding='utf-8', sep=';')
            elif formato.lower() == 'excel':
                arquivo = os.path.join(diretorio_destino, f"{nome_arquivo}.xlsx")
                self.df_projetos.to_excel(arquivo, index=False)
            elif formato.lower() == 'parquet':
                arquivo = os.path.join(diretorio_destino, f"{nome_arquivo}.parquet")
                self.df_projetos.to_parquet(arquivo, index=False)
            else:
                logger.error(f"❌ Formato não suportado: {formato}")
                return False
            
            logger.info(f"💾 Dados salvos em: {arquivo}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar arquivo: {e}")
            return False
    
    def gerar_relatorio(self, stats: Dict[str, Any]) -> str:
        """
        Gera um relatório resumido dos dados.
        
        Args:
            stats (Dict): Estatísticas dos dados
        
        Returns:
            str: Relatório formatado
        """
        relatorio = """
        ===== RELATÓRIO DE ANÁLISE - PROJETOS LEI DO BEM =====
        
        📊 ESTATÍSTICAS GERAIS:
        • Total de Projetos: {total_projetos:,}
        • Total de Empresas: {total_empresas:,}
        • Ano Base: {ano_base}
        
        🏢 DISTRIBUIÇÃO POR EMPRESAS:
        """.format(**stats)
        
        for empresa, count in stats.get('distribuicao_empresas', {}).items():
            relatorio += f"        • {empresa}: {count:,} projetos\n"
        
        relatorio += "\n        ====================================================="
        
        return relatorio


def main():
    """Função principal para execução do script."""
    print("🚀 Iniciando Análise de Projetos da Lei do Bem\n")
    
    # Criar instâncias das classes
    carregador = CarregadorDadosLeiDoBem()
    analisador = AnalisadorProjetosLeiDoBem()
    
    print("📋 Carregando todos os projetos do ano base (sem filtro de empresa).")
    
    # Conectar ao banco
    if not carregador.conectar_banco():
        print("❌ Falha na conexão com banco. Encerrando...")
        return None, None
    
    # Carregar dados
    df = carregador.carregar_dados()
    if df is None:
        print("❌ Falha ao carregar dados. Encerrando...")
        return None, None
    
    # Transferir dados para o analisador
    analisador.df_projetos = df
    analisador.empresas_filtro = ["TODAS_AS_EMPRESAS"]  # Para uso no nome do arquivo
    
    print(f"\n📋 Resumo dos dados carregados:")
    print(f"   • Shape: {df.shape}")
    print(f"   • Colunas: {list(df.columns[:5])}... (primeiras 5)")
    print(f"   • Tipos de dados: {df.dtypes.value_counts().to_dict()}")
    
    # Processar dados
    stats = analisador.processar_dados()
    
    # Gerar e exibir relatório
    relatorio = analisador.gerar_relatorio(stats)
    print(relatorio)
    
    # Salvar dados
    print("\n💾 Salvando dados...")
    analisador.salvar_dados('csv')
    analisador.salvar_dados('excel')
    
    print("\n✅ Análise concluída! O DataFrame está disponível na variável 'analisador.df_projetos'")
    print("\n🔧 Para usar o DataFrame interativamente:")
    print("   df = analisador.df_projetos")
    print("   print(df.head())")
    print("   print(df.info())")
    
    return analisador, carregador


if __name__ == "__main__":
    # Executar análise
    resultado = main()
    
    if resultado[0] is not None:
        analisador, carregador = resultado
        
        # Disponibilizar DataFrame para uso interativo
        if analisador and analisador.df_projetos is not None:
            df = analisador.df_projetos
            print(f"\n🎯 DataFrame 'df' disponível com {len(df)} registros")
            print("\nExemplos de uso:")
            print("# Ver primeiras linhas")
            print("df.head()")
            print("\n# Filtrar por empresa")
            print("df[df['lst_norazaosocial'].str.contains('BANCO')]")
            print("\n# Agrupar por empresa")
            print("df.groupby('lst_norazaosocial').size()")
            print("\n# Estatísticas de valores")
            print("df['do_aat_vltotaldeclarado'].describe()")
    else:
        print("❌ Execução interrompida devido a erros.")
