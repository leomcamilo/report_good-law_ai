# Análise e Clusterização de Projetos da Lei do Bem

Este projeto extrai, processa e analisa dados de projetos da Lei do Bem usando técnicas avançadas de Machine Learning. Ele opera em um pipeline de **três estágios** para consolidar dados de um banco PostgreSQL, aplicar clusterização semântica e extrair insights analíticos dos clusters formados.

## 📋 Pré-requisitos

- Python 3.9+
- PostgreSQL rodando localmente na porta 5432
- Banco de dados `dbs_mctic2` configurado
- Credenciais: usuário `ia_budy`, senha `ia_budy`
- [uv](https://docs.astral.sh/uv/) - Gerenciador de pacotes Python moderno

## 🚀 Instalação

### 1. **Instalar uv (se ainda não tiver):**

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. **Configurar o projeto:**

```bash
# Clonar/navegar para o diretório do projeto
cd /home/leomcamilo/projects/test_pgai

# Instalar dependências e criar ambiente virtual
# Isso instalará pandas, sqlalchemy, sentence-transformers, umap-learn, hdbscan, etc.
uv sync

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

## 🏗️ Estrutura do Projeto

```
test_pgai/
├── pyproject.toml                   # Configuração e dependências
├── .venv/                           # Ambiente virtual (criado pelo uv)
├── 1.csv_analise_projetos.py        # Etapa 1: Extração de dados do PostgreSQL
├── 2.csv_embedding_cluster.py       # Etapa 2: Clusterização com embeddings semânticos
├── 3.csv_analise_cluster.py         # Etapa 3: Análise e extração de insights
├── tabelas_csv_xlsx/                # Dados brutos extraídos (CSV/Excel)
├── json_outputs/                    # Saídas em formato JSON
└── README.md                        # Este arquivo
```

## 📊 Pipeline Completo de Análise

O processo é dividido em **três etapas** que devem ser executadas sequencialmente:

### 🔧 Etapa 1: Extração de Dados do Banco

**Arquivo:** `1.csv_analise_projetos.py`

Conecta ao PostgreSQL, executa consulta otimizada e exporta dados consolidados dos projetos da Lei do Bem de 2023.

```bash
# Ativar ambiente (se não estiver ativo)
source .venv/bin/activate

# Executar extração de dados
python 1.csv_analise_projetos.py
```

**Saídas geradas:**
- `tabelas_csv_xlsx/projetos_lei_do_bem_2023_TODAS_AS_EMPRESAS.csv`
- `tabelas_csv_xlsx/projetos_lei_do_bem_2023_TODAS_AS_EMPRESAS.xlsx`

### 🤖 Etapa 2: Clusterização com IA

**Arquivo:** `2.csv_embedding_cluster.py`

Aplica técnicas avançadas de NLP e Machine Learning para agrupar projetos similares semanticamente.

```bash
# Executar clusterização
python 2.csv_embedding_cluster.py
```

**Características técnicas:**
- **Modelo de Embeddings:** SERAFIM (português especializado) - `PORTULAN/serafim-335m-portuguese-pt-sentence-encoder-ir`
- **Pré-processamento:** Stop words customizadas (NLTK + domínio P&D)
- **Clustering:** Aglomerativo com threshold otimizado (0.58)
- **Extração:** Foco em conteúdo técnico (descrição, metodologia, desafio tecnológico)

**Saídas geradas:**
- `projetos_com_clusters_final.csv` - Dataset completo com clusters
- Estatísticas detalhadas de todos os clusters

### 📈 Etapa 3: Análise de Clusters

**Arquivo:** `3.csv_analise_cluster.py`

Extrai informações estruturadas dos clusters e gera análises estatísticas detalhadas.

```bash
# Executar análise de clusters
python 3.csv_analise_cluster.py
```

**Análises realizadas:**
- Extração de nomes e descrições dos projetos
- Identificação de razões sociais das empresas
- Distribuição por tamanho de cluster
- Top empresas por quantidade de projetos
- Estatísticas de qualidade da clusterização

**Saída gerada:**
- `clusters_projetos.csv` - Dados estruturados para análise

## 🤖 Detalhes Técnicos do Pipeline de ML

### Processamento de Texto
1. **Extração de Conteúdo Técnico**: Regex patterns para capturar descrição, metodologia, desafio tecnológico
2. **Limpeza com Stop Words**: União de NLTK (português) + palavras específicas do domínio P&D
3. **Preservação de Contexto**: Mantém termos técnicos, códigos e palavras > 3 caracteres

### Geração de Embeddings
- **Modelo:** SERAFIM-335M (especializado em português)
- **Dimensionalidade:** 768 dimensões por projeto
- **Foco:** Apenas conteúdo técnico relevante

### Clustering Aglomerativo
- **Algoritmo:** AgglomerativeClustering (scikit-learn)
- **Métrica:** Cosine similarity
- **Linkage:** Average (otimizado para embeddings semânticos)
- **Threshold:** 0.58 (otimizado para cobertura 100%)

## 📁 Arquivos de Saída Detalhados

### Etapa 1 - Extração
- **CSV:** `tabelas_csv_xlsx/projetos_lei_do_bem_2023_TODAS_AS_EMPRESAS.csv`
- **Excel:** `tabelas_csv_xlsx/projetos_lei_do_bem_2023_TODAS_AS_EMPRESAS.xlsx`
- **Conteúdo:** Dados brutos consolidados do PostgreSQL

### Etapa 2 - Clusterização
- **Principal:** `projetos_com_clusters_final.csv`
- **Colunas adicionais:** `texto_tecnico_bruto`, `texto_tecnico`, `cluster`
- **Estatísticas:** Distribuição completa de todos os clusters

### Etapa 3 - Análise
- **Resultado:** `clusters_projetos.csv`
- **Colunas:** `nome_projeto`, `descricao_projeto`, `razaosocial_empresa`, `cluster`
- **Formato:** Dados estruturados para análise e visualização

## 📊 Exemplo de Uso Completo

```bash
# Pipeline completo
source .venv/bin/activate

# 1. Extrair dados do banco
python 1.csv_analise_projetos.py

# 2. Aplicar clusterização
python 2.csv_embedding_cluster.py

# 3. Analisar resultados
python 3.csv_analise_cluster.py

# Verificar resultados
ls -la projetos_com_clusters_final.csv
ls -la clusters_projetos.csv
```

## 🆘 Troubleshooting

### Erro de Conexão com Banco (Etapa 1)
```
psycopg2.OperationalError: could not connect to server
```
**Solução**: Verifique se PostgreSQL está ativo e credenciais estão corretas.

### Erro de Arquivo Não Encontrado (Etapa 2)
```
FileNotFoundError: Nenhum arquivo CSV encontrado na pasta tabelas_csv_xlsx
```
**Solução**: Execute primeiro a Etapa 1 (`1.csv_analise_projetos.py`).

### Erro de Parser (Etapa 3)
```
FileNotFoundError: Arquivo 'projetos_com_clusters_final.csv' não encontrado
```
**Solução**: Execute primeiro a Etapa 2 (`2.csv_embedding_cluster.py`).

### Problemas com NLTK
```bash
# Download manual das stopwords
python -c "import nltk; nltk.download('stopwords')"
```

### Problemas com `uv`
```bash
# Recriar ambiente virtual
rm -rf .venv
uv sync

# Limpar cache do uv
uv clean
```

## 🔄 Desenvolvimento e Customização

### Ajustar Threshold de Clustering
Edite `2.csv_embedding_cluster.py`, linha com `threshold = 0.58`:
```python
# Para mais clusters (menor threshold)
threshold = 0.45

# Para menos clusters (maior threshold)  
threshold = 0.70
```

### Adicionar Novas Stop Words
Edite `stop_words_personalizadas` em `2.csv_embedding_cluster.py`:
```python
stop_words_personalizadas.update({
    'nova_palavra', 'outro_termo', 'palavra_especifica'
})
```

### Adicionando Dependências
```bash
source .venv/bin/activate
uv add matplotlib seaborn plotly  # Para visualizações
uv sync
```

## 📈 Métricas de Performance

- **Cobertura:** 100% dos projetos são clusterizados
- **Escalabilidade:** Testado com até 75k projetos
- **Qualidade:** Threshold otimizado para máxima separação semântica
- **Velocidade:** Processamento eficiente com embeddings pré-treinados

## 🎯 Próximos Passos

1. **Visualização:** Implementar dashboard interativo dos clusters
2. **API:** Criar endpoint para clusterização em tempo real
3. **Modelos:** Testar outros modelos de embedding português
4. **Análise:** Adicionar análise de tendências temporais
