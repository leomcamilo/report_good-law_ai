# Análise e Clusterização de Projetos da Lei do Bem

Este projeto extrai, processa e analisa dados de projetos da Lei do Bem. Ele opera em um pipeline de dois estágios para primeiro consolidar os dados de um banco de dados e, em seguida, aplicar técnicas de Machine Learning para agrupar projetos similares.

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
├── pyproject.toml          # Configuração e dependências
├── .venv/                  # Ambiente virtual (criado pelo uv)
├── analise_projetos.py     # Etapa 1: Extração de dados do DB
├── criar_resumo.py         # Etapa 2: Clusterização com ML
├── tabelas_csv_xlsx/       # Diretório para os dados extraídos
└── README.md               # Este arquivo
```

## 📊 Fluxo de Trabalho e Uso

O processo é dividido em duas etapas principais, que devem ser executadas em ordem.

### Etapa 1: Extrair Dados do Banco de Dados

O script `analise_projetos.py` conecta ao PostgreSQL, executa uma consulta consolidada e salva os dados brutos em um arquivo CSV.

```bash
# Ativar ambiente (se não estiver ativo)
source .venv/bin/activate

# Executar o script de extração
python analise_projetos.py
```

Isso criará um arquivo CSV dentro da pasta `tabelas_csv_xlsx/`, que será usado na próxima etapa.

### Etapa 2: Clusterizar Projetos com Machine Learning

O script `criar_resumo.py` lê o arquivo CSV gerado, aplica um modelo de linguagem para entender o conteúdo dos projetos e os agrupa por similaridade.

```bash
# Executar o script de clusterização
python criar_resumo.py
```

## 🤖 Pipeline de Machine Learning

A clusterização realizada pelo `criar_resumo.py` segue os seguintes passos:

1.  **Criação de Embeddings**: Textos de cada projeto são convertidos em vetores numéricos (embeddings) usando o modelo `neuralmind/bert-base-portuguese-cased`.
2.  **Redução de Dimensionalidade**: O `UMAP` é usado para reduzir a complexidade dos vetores, otimizando a performance do clustering.
3.  **Clusterização**: O `HDBSCAN` é aplicado para agrupar os projetos em clusters com base na proximidade de seus vetores.

## 📁 Arquivos de Saída

Ao final do processo, os seguintes arquivos serão gerados:

-   **Da Etapa 1:**
    -   `tabelas_csv_xlsx/projetos_lei_do_bem_2023_TODAS_AS_EMPRESAS.csv`: Dados brutos extraídos do banco de dados.
-   **Da Etapa 2:**
    -   `projetos_com_clusters.csv`: Arquivo final com uma coluna adicional `cluster` que identifica o grupo de cada projeto.
    -   `embeddings_reduced.npy`: Arquivo NumPy com os vetores de embeddings de dimensionalidade reduzida.

## 🆘 Troubleshooting

### Erro de Conexão com Banco
```
psycopg2.OperationalError: could not connect to server
```
**Solução**: Verifique se o serviço do PostgreSQL está ativo e se as credenciais no script `analise_projetos.py` estão corretas.

### Erro de `ParserError` em `criar_resumo.py`
```
pandas.errors.ParserError: Error tokenizing data.
```
**Solução**: Verifique se o separador no `pd.read_csv()` em `criar_resumo.py` (ex: `sep=';'`) corresponde ao separador usado para salvar o arquivo em `analise_projetos.py`.

### Problemas com `uv`

```bash
# Recriar ambiente virtual do zero
rm -rf .venv
uv sync

# Limpar cache do uv
uv clean
```

## 🔄 Desenvolvimento

### Adicionando Novas Dependências

```bash
# Ativar ambiente
source .venv/bin/activate

# Adicionar nova dependência
uv add matplotlib

# Sincronizar após mudanças manuais no pyproject.toml
uv sync
```
