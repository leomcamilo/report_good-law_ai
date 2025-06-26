# Análise de Projetos da Lei do Bem - DataFrame Pandas

Este projeto converte a consulta SQL dos projetos da Lei do Bem em um DataFrame pandas para análise e processamento de dados.

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

# Via pip (alternativa)
pip install uv
```

### 2. **Configurar o projeto:**

```bash
# Clonar/navegar para o diretório do projeto
cd /home/leomcamilo/projects/test_pgai

# Instalar dependências e criar ambiente virtual
uv sync

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

### 3. **Configurar ambiente:**

```bash
# Copiar arquivo de configuração
cp .env.example .env

# Editar com suas credenciais
nano .env
```

### 4. **Testar sistema:**

```bash
python test_sistema.py
```

## 📦 Gerenciamento de Dependências com uv

### Comandos Básicos do uv

```bash
# Instalar todas as dependências (primeira vez)
uv sync

# Adicionar nova dependência
uv add nome-do-pacote

# Adicionar dependência de desenvolvimento
uv add --dev nome-do-pacote

# Remover dependência
uv remove nome-do-pacote

# Atualizar dependências
uv sync --upgrade

# Mostrar dependências instaladas
uv pip list

# Ativar ambiente virtual
source .venv/bin/activate
```

### Estrutura do Projeto

```
test_pgai/
├── pyproject.toml          # Configuração e dependências
├── .env                    # Variáveis de ambiente
├── .venv/                  # Ambiente virtual (criado pelo uv)
├── analise_projetos.py     # Script principal
├── consulta_simples.py     # Script simples
├── analise_langchain_deepseek.py  # Análise com IA
├── test_sistema.py         # Testes
└── README.md              # Este arquivo
```

## 📊 Uso

### Opção 1: Script Completo (Recomendado)

Execute o script principal que inclui análises automáticas:

```bash
# Ativar ambiente (se não estiver ativo)
source .venv/bin/activate

# Executar análise
python analise_projetos.py
```

**Funcionalidades:**
- Carrega dados da consulta SQL consolidada
- Gera estatísticas e relatórios automáticos
- Salva dados em CSV e Excel
- Fornece insights sobre o processo da Lei do Bem

### Opção 2: Script Simples

Para uso rápido e direto:

```bash
python consulta_simples.py
```

**Funcionalidades:**
- Carrega apenas os dados em DataFrame
- Salva como CSV
- Ideal para uso interativo

### Opção 3: Uso Programático

```python
from analise_projetos import AnalisadorProjetosLeiDoBem

# Inicializar analisador
analisador = AnalisadorProjetosLeiDoBem()

# Conectar e carregar dados
analisador.conectar_banco()
df = analisador.carregar_dados()

# Usar o DataFrame
print(df.head())
print(df.info())

# Análises específicas
projetos_aprovados = df[df['do_resultado'] == 'RECOMENDADO']
print(f"Projetos recomendados: {len(projetos_aprovados)}")
```

## 📈 Estrutura dos Dados

O DataFrame resultante contém as seguintes categorias de colunas:

### 🏢 Identificação e Empresa
- `iddadoanaliseprojeto`, `projeto_numero`, `projeto_nome`
- `empresa_cnpj`, `empresa_razao_social`, `empresa_ano_base`

### 📝 Fase 1: Preenchimento
- `preen_tipo_organismo`, `preen_receita_liquida`
- `preen_total_funcionarios`, `preen_pesquisadores_exclusivos`

### 🔬 Dados Técnicos do Projeto
- `projeto_area`, `projeto_tipo_pesquisa`, `projeto_natureza`
- `projeto_elemento_tecnologico`, `projeto_metodologia`

### 🔍 Fase 2: Análise DO
- `do_resultado`, `do_valor_declarado`, `do_tipo_avaliacao`
- `do_justificativa_resumo`, `do_observacao_resumo`

### 📋 Fase 3: Parecer
- `parecer_resultado`, `parecer_valor_aprovado`, `parecer_valor_glosa`
- `parecer_projetos_aprovados`, `parecer_conclusao_resumo`

### ⚖️ Fase 4: Contestação
- `contestacao_solicita_reanalise`
- `contestacao_justificativa_resumo`, `contestacao_resposta_resumo`

### 📊 Indicadores de Progresso
- `passou_analise_do`, `passou_parecer`, `teve_contestacao`
- `status_atual_processo`

## 🔧 Exemplos de Análise

### Estatísticas Básicas
```python
# Distribuição por status
print(df['status_atual_processo'].value_counts())

# Valores por fase
print(df['do_valor_declarado'].describe())
print(df['parecer_valor_aprovado'].describe())
```

### Análises por Empresa
```python
# Projetos por empresa
empresas = df.groupby('empresa_razao_social').agg({
    'projeto_numero': 'count',
    'do_valor_declarado': 'sum',
    'parecer_valor_aprovado': 'sum'
}).sort_values('projeto_numero', ascending=False)

print(empresas.head(10))
```

### Análises por Área
```python
# Projetos por área
areas = df.groupby('projeto_area').size().sort_values(ascending=False)
print(areas.head(10))

# Taxa de aprovação por área
aprovacao_area = df.groupby('projeto_area').agg({
    'passou_parecer': 'mean',
    'teve_contestacao': 'mean'
})
print(aprovacao_area)
```

### Análise Temporal
```python
# Análise por data de início (se disponível)
if 'projeto_inicio' in df.columns:
    df['projeto_inicio'] = pd.to_datetime(df['projeto_inicio'])
    temporal = df.groupby(df['projeto_inicio'].dt.year).size()
    print(temporal)
```

## 📁 Arquivos de Saída

O script gera automaticamente:

- `projetos_lei_do_bem_2023.csv` - Dados em formato CSV
- `projetos_lei_do_bem_2023.xlsx` - Dados em formato Excel
- Relatório de estatísticas no console

## ⚠️ Observações Importantes

1. **Filtro de Ano**: A consulta está filtrada para ano base 2023
2. **Campos de Texto**: Limitados a 200 caracteres para otimização
3. **Valores Nulos**: Campos opcionais podem conter valores nulos
4. **Performance**: Para grandes volumes, considere usar `chunksize` no pandas

## 🆘 Troubleshooting

### Erro de Conexão
```
psycopg2.OperationalError: could not connect to server
```
**Solução**: Verificar se PostgreSQL está rodando e credenciais estão corretas.

### Erro de Permissão
```
permission denied for table
```
**Solução**: Verificar se usuário `ia_budy` tem permissões adequadas.

### Erro de Memória
```
MemoryError
```
**Solução**: Usar `chunksize` no `pd.read_sql_query()` para grandes datasets.

### Problemas com uv

```bash
# Recriar ambiente virtual
rm -rf .venv
uv sync

# Limpar cache do uv
uv clean

# Verificar versão
uv --version
```

## 📚 Recursos Adicionais

- [Documentação uv](https://docs.astral.sh/uv/)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 🤖 Análise com IA (LangChain + DeepSeek)

### Configuração da API

1. **Obter chave da API DeepSeek:**
   - Acesse: https://platform.deepseek.com/
   - Crie uma conta e obtenha sua API key

2. **Configurar a chave:**
   ```bash
   # Edite o arquivo .env
   nano .env
   
   # Substitua pela sua chave real:
   DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
   ```

### Scripts de Análise com IA

Certifique-se de que o ambiente virtual está ativo:

```bash
source .venv/bin/activate
```

#### Opção 1: Script Interativo (Recomendado)
```bash
python analise_simples.py
```

**Menu interativo com opções:**
- Análise Rápida (30 projetos)
- Análise Completa (100 projetos)  
- Análise Customizada
- Verificação de configuração

#### Opção 2: Script Completo
```bash
python analise_langchain_deepseek.py
```

**Funcionalidades:**
- Carregamento automático dos dados
- Análise avançada com IA
- Identificação de padrões e inconsistências
- Geração de relatório detalhado em Markdown
- Propostas de otimização do processo

### Análises Fornecidas pela IA

A IA analisa automaticamente:

1. **Consistência entre Fases**
   - Comparação DO vs Parecer
   - Taxa de concordância entre avaliadores
   - Mudanças de decisão e suas causas

2. **Padrões de Contestação**
   - Tipos de projetos mais contestados
   - Eficácia dos argumentos de contestação
   - Características das empresas que contestam

3. **Detecção de Inconsistências**
   - Vieses por área tecnológica
   - Tratamento diferenciado por porte da empresa
   - Padrões anômalos de aprovação/glosa

4. **Propostas de Otimização**
   - Novos indicadores de qualidade
   - Melhorias no fluxo do processo
   - Automatizações possíveis

### Exemplo de Uso Programático

```python
from analise_langchain_deepseek import AnalisadorLeiDoBemLangChain

# Inicializar analisador
analisador = AnalisadorLeiDoBemLangChain()

# Executar análise
analise = analisador.executar_analise_completa(
    max_rows=50,  # Número de projetos
    salvar=True   # Salvar em arquivo
)

# Exibir resultado
print(analise)
```

### Arquivos de Saída

- `analise_lei_do_bem_deepseek_YYYYMMDD_HHMMSS.md` - Relatório completo da IA
- `projetos_lei_do_bem_2023.csv` - Dados brutos
- `projetos_lei_do_bem_2023.xlsx` - Dados em Excel

---

## 🔄 Desenvolvimento

### Adicionando Novas Dependências

```bash
# Ativar ambiente
source .venv/bin/activate

# Adicionar nova dependência
uv add matplotlib seaborn

# Ou para desenvolvimento
uv add --dev pytest black flake8

# Sincronizar após mudanças
uv sync
```

### Fluxo de Trabalho Recomendado

1. **Desenvolvimento diário:**
   ```bash
   source .venv/bin/activate
   python seu_script.py
   ```

2. **Atualizações do projeto:**
   ```bash
   uv sync --upgrade
   ```

3. **Compartilhamento:**
   - Commitar apenas `pyproject.toml`
   - O `.venv/` está no `.gitignore`
   - Outros desenvolvedores usam `uv sync`

## 🔄 Próximos Passos

Após carregar os dados, você pode:

1. **Análise com IA** usando DeepSeek para insights avançados
2. **Criar visualizações** com matplotlib/seaborn (`uv add matplotlib seaborn`)
3. **Aplicar machine learning** para predições (`uv add scikit-learn`)
4. **Gerar relatórios automáticos** com templates (`uv add jinja2`)
5. **Integrar com BI tools** como Power BI
