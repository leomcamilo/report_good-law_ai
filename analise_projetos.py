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
from typing import Optional, Dict, Any
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Suprimir warnings do pandas
warnings.filterwarnings('ignore')

class AnalisadorProjetosLeiDoBem:
    """Classe para análise de projetos da Lei do Bem usando dados do PostgreSQL."""
    
    def __init__(self):
        """Inicializa o analisador com as configurações de banco."""
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
            # Query SQL consolidada (extraída do arquivo public.sql)
            query_sql = """
            -- CONSULTA CONSOLIDADA: UMA LINHA POR PROJETO COM TODO O FLUXO DO PROCESSO
            -- Baseada na transcrição da reunião e estrutura do MER da Lei do Bem

            WITH base_projetos AS (
                -- Dados básicos do projeto e empresa
                SELECT 
                    -- IDENTIFICAÇÃO PRINCIPAL
                    proj.iddadoanaliseprojeto,
                    proj.idprenchimentosituacaoanalise,
                    proj.nritem as projeto_numero,
                    proj.noprojeto as projeto_nome,
                    proj.dsprojeto as projeto_descricao,
                    
                    -- DADOS DA EMPRESA
                    emp.nranobase as empresa_ano_base,
                    emp.nrcnpj as empresa_cnpj,
                    emp.norazaosocial as empresa_razao_social,
                    
                    -- DADOS DO PREENCHIMENTO (FASE 1)
                    preen.tporganismo as preen_tipo_organismo,
                    preen.vlreceitaliquida as preen_receita_liquida,
                    preen.nrtotalfuncionario as preen_total_funcionarios,
                    preen.nrmediopesquisadordedicacaoexclusiva as preen_pesquisadores_exclusivos,
                    preen.pcrecursoproprio as preen_percentual_recurso_proprio,
                    
                    -- DADOS DO PROJETO (DETALHES TÉCNICOS)
                    proj.tppbpade as projeto_tipo_pesquisa,
                    proj.dsareaprojeto as projeto_area,
                    proj.dspalavrachave as projeto_palavras_chave,
                    proj.tpnatureza as projeto_natureza,
                    proj.dselementotecnologico as projeto_elemento_tecnologico,
                    proj.dsdesafiotecnologico as projeto_desafio_tecnologico,
                    proj.dsmetodologiautilizada as projeto_metodologia,
                    proj.dsinicioatividade as projeto_inicio,
                    proj.dsprevisaotermino as projeto_previsao_termino
                    
                FROM tbdadoanaliseprojeto proj
                INNER JOIN tbdadoanalisepreenchimento preen 
                    ON proj.idprenchimentosituacaoanalise = preen.idprenchimentosituacaoanalise
                INNER JOIN listaempresasporanobasesituacaoanalise emp 
                    ON preen.idprenchimentosituacaoanalise = emp.idprenchimentosituacaoanalise
            ),

            marcos_do AS (
                -- ANÁLISE DO (FASE 2)
                SELECT 
                    ma.idprenchimentosituacaoanalise,
                    aom.iddadoanaliseprojeto,
                    ma.idmarcoanalise as do_id_marco,
                    ma.nrmarcoanalise as do_numero_marco,
                    ma.dsobservacao as do_observacao,
                    aom.dsjustificativapadrao as do_justificativa,
                    aom.dsobservacaogeral as do_observacao_geral,
                    aom.vltotaldeclarado as do_valor_declarado,
                    ta.notipoavaliacaoanalise as do_tipo_avaliacao,
                    CASE 
                        WHEN ta.idtipoavaliacaoanalise = 1 THEN 'NÃO RECOMENDADO'
                        WHEN ta.idtipoavaliacaoanalise = 2 THEN 'RECOMENDADO PARCIALMENTE' 
                        WHEN ta.idtipoavaliacaoanalise = 3 THEN 'RECOMENDADO'
                        ELSE 'AGUARDANDO ANÁLISE'
                    END as do_resultado
                FROM tbmarcoanalise ma
                INNER JOIN tbanaliseobjetomarcoprojeto aom 
                    ON ma.idmarcoanalise = aom.idmarcoanalise
                LEFT JOIN tbtipoavaliacaoanalise ta 
                    ON aom.idtipoavaliacaoanalise = ta.idtipoavaliacaoanalise
                WHERE ma.cdtipomarcoanalise = 1  -- DO/Consolidação
            ),

            marcos_parecer AS (
                -- PARECER (FASE 3)
                SELECT 
                    ma.idprenchimentosituacaoanalise,
                    ma.idmarcoanalise as parecer_id_marco,
                    ma.nrmarcoanalise as parecer_numero_marco,
                    ma.dsobservacao as parecer_observacao,
                    mdc.dsconclusao as parecer_conclusao,
                    mdc.dsobservacaodo as parecer_observacao_do,
                    mdc.vltotaldispendio as parecer_total_dispendio,
                    mdc.vlaprovado as parecer_valor_aprovado,
                    mdc.vlglosa as parecer_valor_glosa,
                    mdc.nrtotalprojeto as parecer_total_projetos,
                    mdc.nrtotalaprovado as parecer_projetos_aprovados,
                    mdc.nrtotalreprovado as parecer_projetos_reprovados,
                    rm.noresultadomarcoanalise as parecer_resultado
                FROM tbmarcoanalise ma
                LEFT JOIN tbmarcoanalisedadoconsolidado mdc 
                    ON ma.idmarcoanalise = mdc.idmarcoanalise
                LEFT JOIN tbresultadomarcoanalise rm 
                    ON ma.cdresultadomarcoanalise = rm.cdresultadomarcoanalise
                WHERE ma.cdtipomarcoanalise = 2  -- Parecer
            ),

            marcos_contestacao AS (
                -- CONTESTAÇÃO (FASE 4)
                SELECT 
                    ma.idprenchimentosituacaoanalise,
                    ma.idmarcoanalise as contestacao_id_marco,
                    ma.nrmarcoanalise as contestacao_numero_marco,
                    apc.dsjustificativacontestacao as contestacao_justificativa,
                    apc.dsjustificativapadrao as contestacao_resposta_padrao,
                    apc.dsconsideracaoobservacaogeral as contestacao_consideracao,
                    apc.dsobservacaogeralparecer as contestacao_obs_parecer,
                    apc.dsrecursoadministrativo as contestacao_recurso_adm,
                    apc.icsolicitacaoreanalise as contestacao_solicita_reanalise
                FROM tbmarcoanalise ma
                LEFT JOIN tbanaliseobjetomarcoprojetocontestacao apc 
                    ON ma.idmarcoanalise = apc.idmarcoanalise
                WHERE ma.cdtipomarcoanalise = 3  -- Contestação
            )

            -- CONSULTA PRINCIPAL: CONSOLIDAÇÃO DE TODAS AS FASES
            -- FILTRO: APENAS PROJETOS DE 2023 (conforme query original)
            SELECT 
                -- === IDENTIFICAÇÃO ===
                bp.iddadoanaliseprojeto,
                bp.idprenchimentosituacaoanalise,
                bp.projeto_numero,
                bp.projeto_nome,
                
                -- === EMPRESA ===
                bp.empresa_ano_base,
                bp.empresa_cnpj,
                bp.empresa_razao_social,
                
                -- === FASE 1: PREENCHIMENTO ===
                bp.preen_tipo_organismo,
                bp.preen_receita_liquida,
                bp.preen_total_funcionarios,
                bp.preen_pesquisadores_exclusivos,
                bp.preen_percentual_recurso_proprio,
                
                -- === DADOS TÉCNICOS DO PROJETO ===
                bp.projeto_tipo_pesquisa,
                bp.projeto_area,
                bp.projeto_natureza,
                bp.projeto_elemento_tecnologico,
                bp.projeto_desafio_tecnologico,
                bp.projeto_metodologia,
                bp.projeto_inicio,
                bp.projeto_previsao_termino,
                SUBSTRING(bp.projeto_descricao, 1, 200) as projeto_descricao_resumo,
                
                -- === FASE 2: ANÁLISE DO ===
                md.do_id_marco,
                md.do_numero_marco,
                md.do_resultado,
                md.do_valor_declarado,
                md.do_tipo_avaliacao,
                SUBSTRING(md.do_justificativa, 1, 200) as do_justificativa_resumo,
                SUBSTRING(md.do_observacao_geral, 1, 200) as do_observacao_resumo,
                
                -- === FASE 3: PARECER ===
                mp.parecer_id_marco,
                mp.parecer_numero_marco,
                mp.parecer_resultado,
                mp.parecer_valor_aprovado,
                mp.parecer_valor_glosa,
                mp.parecer_projetos_aprovados,
                mp.parecer_projetos_reprovados,
                SUBSTRING(mp.parecer_conclusao, 1, 200) as parecer_conclusao_resumo,
                
                -- === FASE 4: CONTESTAÇÃO ===
                mc.contestacao_id_marco,
                mc.contestacao_numero_marco,
                mc.contestacao_solicita_reanalise,
                SUBSTRING(mc.contestacao_justificativa, 1, 200) as contestacao_justificativa_resumo,
                SUBSTRING(mc.contestacao_resposta_padrao, 1, 200) as contestacao_resposta_resumo,
                
                -- === INDICADORES DE PROGRESSO ===
                CASE WHEN md.do_id_marco IS NOT NULL THEN 1 ELSE 0 END as passou_analise_do,
                CASE WHEN mp.parecer_id_marco IS NOT NULL THEN 1 ELSE 0 END as passou_parecer,
                CASE WHEN mc.contestacao_id_marco IS NOT NULL THEN 1 ELSE 0 END as teve_contestacao,
                
                -- === STATUS ATUAL ===
                CASE 
                    WHEN mc.contestacao_id_marco IS NOT NULL THEN 'CONTESTAÇÃO'
                    WHEN mp.parecer_id_marco IS NOT NULL THEN 'PARECER CONCLUÍDO'
                    WHEN md.do_id_marco IS NOT NULL THEN 'ANÁLISE DO CONCLUÍDA'
                    ELSE 'PREENCHIMENTO'
                END as status_atual_processo

            FROM base_projetos bp
            LEFT JOIN marcos_do md 
                ON bp.idprenchimentosituacaoanalise = md.idprenchimentosituacaoanalise 
                AND bp.iddadoanaliseprojeto = md.iddadoanaliseprojeto
            LEFT JOIN marcos_parecer mp 
                ON bp.idprenchimentosituacaoanalise = mp.idprenchimentosituacaoanalise
            LEFT JOIN marcos_contestacao mc 
                ON bp.idprenchimentosituacaoanalise = mc.idprenchimentosituacaoanalise

            -- FILTRO: APENAS PROJETOS DO ANO BASE 2023
            WHERE bp.empresa_ano_base = 2023

            -- Ordenação por empresa e projeto
            ORDER BY 
                bp.empresa_razao_social,
                bp.projeto_numero;
            """
            
            logger.info("🔍 Executando consulta SQL...")
            
            # Executar query e carregar em DataFrame
            self.df_projetos = pd.read_sql_query(query_sql, self.engine)
            
            logger.info(f"✅ Dados carregados: {len(self.df_projetos)} projetos encontrados")
            logger.info(f"📊 Colunas disponíveis: {len(self.df_projetos.columns)}")
            
            return self.df_projetos
            
        except Exception as e:
            logger.error(f"❌ Erro ao executar consulta: {e}")
            return None
    
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
        
        # Estatísticas básicas
        stats = {
            'total_projetos': len(self.df_projetos),
            'total_empresas': self.df_projetos['empresa_cnpj'].nunique(),
            'ano_base': self.df_projetos['empresa_ano_base'].iloc[0]
        }
        
        # Análise por status do processo
        status_counts = self.df_projetos['status_atual_processo'].value_counts()
        stats['distribuicao_status'] = status_counts.to_dict()
        
        # Análise por fases
        stats['projetos_analise_do'] = self.df_projetos['passou_analise_do'].sum()
        stats['projetos_com_parecer'] = self.df_projetos['passou_parecer'].sum()
        stats['projetos_com_contestacao'] = self.df_projetos['teve_contestacao'].sum()
        
        # Análise de valores (quando disponível)
        valores_declarados = self.df_projetos['do_valor_declarado'].dropna()
        if not valores_declarados.empty:
            stats['valor_total_declarado'] = valores_declarados.sum()
            stats['valor_medio_projeto'] = valores_declarados.mean()
        
        valores_aprovados = self.df_projetos['parecer_valor_aprovado'].dropna()
        if not valores_aprovados.empty:
            stats['valor_total_aprovado'] = valores_aprovados.sum()
            stats['taxa_aprovacao_valor'] = (valores_aprovados.sum() / valores_declarados.sum() * 100) if not valores_declarados.empty else 0
        
        # Análise por área de projeto
        if 'projeto_area' in self.df_projetos.columns:
            areas_counts = self.df_projetos['projeto_area'].value_counts().head(10)
            stats['top_areas_projeto'] = areas_counts.to_dict()
        
        # Análise por tipo de organismo
        if 'preen_tipo_organismo' in self.df_projetos.columns:
            organismo_counts = self.df_projetos['preen_tipo_organismo'].value_counts()
            stats['distribuicao_organismos'] = organismo_counts.to_dict()
        
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
            if not nome_arquivo:
                nome_arquivo = f"projetos_lei_do_bem_2023"
            
            if formato.lower() == 'csv':
                arquivo = f"{nome_arquivo}.csv"
                self.df_projetos.to_csv(arquivo, index=False, encoding='utf-8')
            elif formato.lower() == 'excel':
                arquivo = f"{nome_arquivo}.xlsx"
                self.df_projetos.to_excel(arquivo, index=False)
            elif formato.lower() == 'parquet':
                arquivo = f"{nome_arquivo}.parquet"
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
        
        🔄 PROGRESSO POR FASES:
        • Projetos com Análise DO: {projetos_analise_do:,}
        • Projetos com Parecer: {projetos_com_parecer:,}
        • Projetos com Contestação: {projetos_com_contestacao:,}
        
        📋 DISTRIBUIÇÃO POR STATUS:
        """.format(**stats)
        
        for status, count in stats.get('distribuicao_status', {}).items():
            relatorio += f"        • {status}: {count:,}\n"
        
        if 'valor_total_declarado' in stats:
            relatorio += f"""
        💰 ANÁLISE FINANCEIRA:
        • Valor Total Declarado: R$ {stats['valor_total_declarado']:,.2f}
        • Valor Médio por Projeto: R$ {stats['valor_medio_projeto']:,.2f}
        """
            
            if 'valor_total_aprovado' in stats:
                relatorio += f"        • Valor Total Aprovado: R$ {stats['valor_total_aprovado']:,.2f}\n"
                relatorio += f"        • Taxa de Aprovação: {stats['taxa_aprovacao_valor']:.1f}%\n"
        
        if 'top_areas_projeto' in stats:
            relatorio += "\n        🔬 TOP 5 ÁREAS DE PROJETO:\n"
            for i, (area, count) in enumerate(list(stats['top_areas_projeto'].items())[:5], 1):
                relatorio += f"        {i}. {area}: {count:,}\n"
        
        relatorio += "\n        ====================================================="
        
        return relatorio


def main():
    """Função principal para execução do script."""
    print("🚀 Iniciando Análise de Projetos da Lei do Bem\n")
    
    # Inicializar analisador
    analisador = AnalisadorProjetosLeiDoBem()
    
    # Conectar ao banco
    if not analisador.conectar_banco():
        print("❌ Falha na conexão com banco. Encerrando...")
        return
    
    # Carregar dados
    df = analisador.carregar_dados()
    if df is None:
        print("❌ Falha ao carregar dados. Encerrando...")
        return
    
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
    
    return analisador


if __name__ == "__main__":
    # Executar análise
    analisador = main()
    
    # Disponibilizar DataFrame para uso interativo
    if analisador and analisador.df_projetos is not None:
        df = analisador.df_projetos
        print(f"\n🎯 DataFrame 'df' disponível com {len(df)} registros")
        print("\nExemplos de uso:")
        print("# Ver primeiras linhas")
        print("df.head()")
        print("\n# Filtrar por status")
        print("df[df['status_atual_processo'] == 'PARECER CONCLUÍDO']")
        print("\n# Agrupar por empresa")
        print("df.groupby('empresa_razao_social').size()")
        print("\n# Estatísticas de valores")
        print("df['do_valor_declarado'].describe()")
