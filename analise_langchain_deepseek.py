#!/usr/bin/env python3
"""
Análise de Projetos Lei do Bem com LangChain + DeepSeek
======================================================

Este script carrega os dados dos projetos da Lei do Bem e utiliza
o LangChain com a API do DeepSeek para análise avançada dos dados.
"""

import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from datetime import datetime
import logging
import re
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AnalisadorLeiDoBemLangChain:
    def __init__(self):
        self.engine = None
        self.llm = None
        self.prompt_template = self._carregar_prompt_template()
        
    def _carregar_prompt_template(self):
        """Carrega o template de prompt do arquivo prompt.md"""
        try:
            with open('prompt.md', 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            logger.warning("Arquivo prompt.md não encontrado. Usando prompt padrão.")
            return self._get_prompt_padrao()
    
    def _get_prompt_padrao(self):
        """Retorna um prompt padrão caso o arquivo não seja encontrado"""
        return """
        Analise os dados de projetos da Lei do Bem fornecidos e identifique:
        1. Padrões de decisão entre as fases DO e Parecer
        2. Inconsistências no processo
        3. Características das empresas e projetos
        4. Propostas de otimização
        
        Apresente sua análise de forma estruturada e objetiva.
        """
    
    def conectar_banco(self):
        """Conecta ao banco PostgreSQL"""
        try:
            # Configurações do banco
            config = {
                'user': os.getenv('POSTGRES_USER', 'ia_budy'),
                'password': os.getenv('POSTGRES_PASSWORD', 'ia_budy'),
                'host': os.getenv('POSTGRES_HOST', 'localhost'),
                'port': os.getenv('POSTGRES_PORT', '5432'),
                'database': os.getenv('POSTGRES_DB', 'dbs_mctic2')
            }
            
            # Criar engine SQLAlchemy
            connection_string = f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
            self.engine = create_engine(connection_string)
            
            logger.info("Conexão com banco estabelecida com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao conectar com banco: {e}")
            return False
    
    def configurar_llm(self):
        """Configura o modelo LLM DeepSeek"""
        try:
            api_key = os.getenv('DEEPSEEK_API_KEY')
            if not api_key:
                logger.error("Chave da API DeepSeek não encontrada. Configure DEEPSEEK_API_KEY no arquivo .env")
                return False
            
            self.llm = ChatOpenAI(
                model="deepseek-chat",
                openai_api_key=api_key,
                openai_api_base="https://api.deepseek.com",
                temperature=0.3,
                max_tokens=4000
            )
            
            logger.info("LLM DeepSeek configurado com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao configurar LLM: {e}")
            return False
    
    def _limpar_sql(self, sql_content):
        """Remove comentários finais e prepara SQL para execução"""
        try:
            # Remover comentários de bloco no final (/* ... */)
            sql_content = re.sub(r'/\*.*?\*/', '', sql_content, flags=re.DOTALL)
            
            # Remover comentários de linha (--) 
            lines = sql_content.split('\n')
            clean_lines = []
            for line in lines:
                # Manter apenas a parte antes do comentário --
                if '--' in line:
                    line = line.split('--')[0]
                clean_lines.append(line)
            
            sql_content = '\n'.join(clean_lines)
            
            # Remover espaços extras e quebras de linha desnecessárias
            sql_content = re.sub(r'\s+', ' ', sql_content)
            sql_content = sql_content.strip()
            
            # Garantir que termina com ponto e vírgula
            if not sql_content.endswith(';'):
                sql_content += ';'
            
            return sql_content
            
        except Exception as e:
            logger.error(f"Erro ao limpar SQL: {e}")
            return sql_content
    
    def carregar_dados(self, max_rows=100):
        """Carrega os dados da consulta SQL"""
        try:
            # Ler a consulta SQL do arquivo
            sql_file_path = os.path.expanduser('~/.dbclient/storage/1750170051954@@127.0.0.1@5432@dbs_mctic2@public/public.sql')
            
            with open(sql_file_path, 'r', encoding='utf-8') as f:
                query = f.read()
            
            # Limpar o SQL
            query = self._limpar_sql(query)
            
            # Remover LIMIT existente (se houver)
            query = re.sub(r'LIMIT\s+\d+\s*;?\s*$', '', query, flags=re.IGNORECASE)
            
            # Remover ponto e vírgula final para adicionar LIMIT
            query = query.rstrip(';').strip()
            
            # Adicionar LIMIT para otimizar o processamento
            if max_rows:
                query += f" LIMIT {max_rows};"
            
            logger.info(f"Executando consulta com LIMIT {max_rows}")
            
            # Executar consulta
            df = pd.read_sql_query(query, self.engine)
            
            logger.info(f"Dados carregados: {len(df)} registros, {len(df.columns)} colunas")
            return df
            
        except Exception as e:
            logger.error(f"Erro ao carregar dados: {e}")
            # Log da query para debug
            if 'query' in locals():
                logger.debug(f"Query problemática: {query[-200:]}")  # Últimos 200 caracteres
            return None
    
    def preparar_dados_para_llm(self, df):
        """Prepara um resumo dos dados para envio ao LLM"""
        try:
            # Informações gerais
            info_geral = f"""
INFORMAÇÕES GERAIS DOS DADOS:
- Total de projetos: {len(df)}
- Período: {df['empresa_ano_base'].min()} a {df['empresa_ano_base'].max()}
- Colunas disponíveis: {len(df.columns)}

ESTATÍSTICAS BÁSICAS:
"""
            
            # Estatísticas por fase
            if 'do_resultado' in df.columns:
                do_stats = df['do_resultado'].value_counts()
                info_geral += f"\nResultados Análise DO:\n{do_stats.to_string()}\n"
            
            if 'parecer_resultado' in df.columns:
                parecer_stats = df['parecer_resultado'].value_counts()
                info_geral += f"\nResultados Parecer:\n{parecer_stats.to_string()}\n"
            
            # Estatísticas financeiras
            if 'do_valor_declarado' in df.columns:
                valores_do = df['do_valor_declarado'].dropna()
                if len(valores_do) > 0:
                    info_geral += f"\nValores Declarados (DO):\n{valores_do.describe().to_string()}\n"
            
            if 'parecer_valor_aprovado' in df.columns:
                valores_parecer = df['parecer_valor_aprovado'].dropna()
                if len(valores_parecer) > 0:
                    info_geral += f"\nValores Aprovados (Parecer):\n{valores_parecer.describe().to_string()}\n"
            
            # Estatísticas por área
            if 'projeto_area' in df.columns:
                area_stats = df['projeto_area'].value_counts().head(10)
                info_geral += f"\nTop 10 Áreas de Projeto:\n{area_stats.to_string()}\n"
            
            # Estatísticas de progresso
            if 'status_atual_processo' in df.columns:
                status_stats = df['status_atual_processo'].value_counts()
                info_geral += f"\nStatus do Processo:\n{status_stats.to_string()}\n"
            
            # Amostra dos dados (primeiras linhas)
            amostra = df.head(5).to_string(max_cols=8)
            
            dados_formatados = f"""
{info_geral}

AMOSTRA DOS DADOS (primeiras 5 linhas, primeiras 8 colunas):
{amostra}

ANÁLISE SOLICITADA:
Por favor, analise estes dados considerando o contexto da Lei do Bem e forneça insights sobre padrões, inconsistências e oportunidades de otimização do processo de análise de projetos de P&D.
"""
            
            return dados_formatados
            
        except Exception as e:
            logger.error(f"Erro ao preparar dados para LLM: {e}")
            return None
    
    def executar_analise_llm(self, dados_contexto):
        """Executa a análise usando o LLM"""
        try:
            # Mensagens para o LLM
            messages = [
                SystemMessage(content=self.prompt_template),
                HumanMessage(content=dados_contexto)
            ]
            
            logger.info("Enviando dados para análise com DeepSeek...")
            
            # Executar análise
            response = self.llm(messages)
            
            logger.info("Análise concluída com sucesso")
            return response.content
            
        except Exception as e:
            logger.error(f"Erro ao executar análise LLM: {e}")
            return None
    
    def salvar_analise(self, analise_texto):
        """Salva a análise em arquivo Markdown na raiz do projeto"""
        try:
            # Nome do arquivo fixo conforme solicitado
            nome_arquivo = "Análise Completa - Projetos Lei do Bem.md"
            
            # Cabeçalho com informações da análise
            cabecalho = f"""# Análise Completa - Projetos Lei do Bem

**Data da Análise:** {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}  
**Modelo:** DeepSeek Chat  
**Gerado por:** Sistema de Análise Automatizada  

---

"""
            
            # Conteúdo completo
            conteudo_completo = cabecalho + analise_texto
            
            # Salvar arquivo
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_completo)
            
            logger.info(f"Análise salva em: {nome_arquivo}")
            print(f"\n✅ Análise salva em: {nome_arquivo}")
            
            return nome_arquivo
            
        except Exception as e:
            logger.error(f"Erro ao salvar análise: {e}")
            return None
    
    def executar_analise_completa(self, max_rows=50, salvar=True):
        """Executa o fluxo completo de análise"""
        try:
            print("🚀 Iniciando análise completa dos projetos da Lei do Bem...")
            
            # 1. Conectar ao banco
            if not self.conectar_banco():
                return "Erro: Não foi possível conectar ao banco de dados"
            
            # 2. Configurar LLM
            if not self.configurar_llm():
                return "Erro: Não foi possível configurar o LLM"
            
            # 3. Carregar dados
            print(f"📊 Carregando dados (máximo {max_rows} registros)...")
            df = self.carregar_dados(max_rows)
            if df is None:
                return "Erro: Não foi possível carregar os dados"
            
            # 4. Preparar dados para LLM
            print("🔄 Preparando dados para análise...")
            dados_contexto = self.preparar_dados_para_llm(df)
            if dados_contexto is None:
                return "Erro: Não foi possível preparar os dados"
            
            # 5. Executar análise
            print("🤖 Executando análise com IA...")
            analise = self.executar_analise_llm(dados_contexto)
            if analise is None:
                return "Erro: Não foi possível executar a análise"
            
            # 6. Salvar resultados
            if salvar:
                print("💾 Salvando análise...")
                arquivo_salvo = self.salvar_analise(analise)
                if arquivo_salvo:
                    print(f"✅ Análise completa salva em: {arquivo_salvo}")
            
            return analise
            
        except Exception as e:
            logger.error(f"Erro na análise completa: {e}")
            return f"Erro: {e}"

def main():
    """Função principal"""
    try:
        # Inicializar analisador
        analisador = AnalisadorLeiDoBemLangChain()
        
        # Executar análise
        resultado = analisador.executar_analise_completa(
            max_rows=100,  # Analisar 100 projetos
            salvar=True    # Salvar em arquivo
        )
        
        if "Erro:" not in resultado:
            print("\n" + "="*80)
            print("ANÁLISE CONCLUÍDA COM SUCESSO!")
            print("="*80)
            print("\nResumo dos próximos passos:")
            print("1. Verifique o arquivo 'Análise Completa - Projetos Lei do Bem.md'")
            print("2. Revise os insights e recomendações")
            print("3. Implemente as otimizações sugeridas")
        else:
            print(f"\n❌ {resultado}")
    
    except KeyboardInterrupt:
        print("\n⚠️ Análise interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
