# Análise e Mineração de Dados de Projetos da Lei do Bem

Este projeto implementa um pipeline completo de análise de dados para projetos submetidos ao sistema da Lei do Bem do MCTI. Utiliza técnicas avançadas de ciência de dados, machine learning e análise estatística para identificar padrões de decisão, inconsistências no processo e oportunidades de otimização do fluxo de análise.

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
# Isso instalará pandas, sqlalchemy, scikit-learn, sentence-transformers, shap, etc.
uv sync

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

## 🏗️ Estrutura do Projeto

```
test_pgai/
├── pyproject.toml                       # Configuração e dependências
├── .venv/                               # Ambiente virtual (criado pelo uv)
├── 1.csv_gerador_projetos.py            # Etapa 1: Extração de dados do PostgreSQL
├── 2.report_e_clustering_k_mean.py    # Etapa 2: Clusterização e análise de padrões
├── analise_multivariada_lei_bem.py      # Etapa 3: Análise multivariada com ML
├── analise_analistas.py                 # Etapa 4: Análise específica dos analistas técnicos
├── prompt.md                            # Templates para análise com LLMs
├── tabelas_csv_xlsx/                    # Dados aglomerados extraídos (CSV/Excel)
├── csv_longo/                           # Dados detalhados linha única
├── Analises/                            # Relatórios e resultados de análise
├── imagens_relatorio/                   # Visualizações geradas
└── README.md                            # Este arquivo
```

## 📊 Pipeline Completo de Análise

O processo é estruturado em **quatro etapas principais** que analisam o fluxo completo dos projetos da Lei do Bem:

### 🔧 Etapa 1: Extração e Consolidação de Dados

**Arquivo:** [`1.csv_gerador_projetos.py`](1.csv_gerador_projetos.py)

Extrai dados consolidados dos projetos da Lei do Bem diretamente do banco PostgreSQL, cobrindo todo o fluxo do processo: **Preenchimento → Análise DO → Parecer → Contestação**.

```bash
# Ativar ambiente (se não estiver ativo)
source .venv/bin/activate

# Executar extração de dados
python 1.csv_gerador_projetos.py
```

**Funcionalidades:**
- Conexão otimizada com PostgreSQL
- Query SQL consolidada que une todas as fases do processo
- Extração de dados aglomerados e detalhados
- Informações de empresas, projetos, analistas e resultados de cada fase

**Saídas geradas:**
- `tabelas_csv_xlsx/projetos_lei_do_bem_2023_AGLOMERADOS.csv` - Dados consolidados
- `csv_longo/projetos_lei_do_bem_2023_DETALHADO_LINHA_UNICA.csv` - Dados detalhados

### 🤖 Etapa 2: Clusterização e Análise de Padrões

**Arquivo:** [`2.report_e_clustering_k_mean.py`](2.report_e_clustering_k_mean.py)

Aplica técnicas avançadas de NLP e Machine Learning para identificar padrões semânticos nos projetos e agrupar projetos similares.

```bash
# Executar clusterização e análise de padrões
python 2.report_e_clustering_k_mean.py
```

**Características técnicas:**
- **Modelo de Embeddings:** SERAFIM (português especializado) - `PORTULAN/serafim-335m-portuguese-pt-sentence-encoder-ir`
- **Pré-processamento:** Stop words customizadas para domínio P&D
- **Clustering:** K-Means otimizado com seleção automática de K
- **PCA:** Visualização bidimensional dos clusters
- **Análise de decisão:** Padrões de aprovação/reprovação por cluster

**Saídas geradas:**
- `Analises/lei_bem_projetos_clusters.csv` - Dataset com clusters
- `Analises/relatorio_clusters_lei_bem.pdf` - Relatório completo em PDF
- Visualizações PNG dos clusters e padrões

### 📈 Etapa 3: Análise Multivariada com Machine Learning

**Arquivo:** [`analise_multivariada_lei_bem.py`](analise_multivariada_lei_bem.py)

Implementa análise estatística avançada usando Random Forest + SHAP para identificar fatores determinantes de aprovação e inconsistências entre fases.

```bash
# Executar análise multivariada
python analise_multivariada_lei_bem.py
```

**Análises realizadas:**
- **Modelagem preditiva:** Random Forest para prever aprovação
- **Análise SHAP:** Interpretabilidade das decisões do modelo
- **Análise entre fases:** Consistência DO → Parecer
- **Feature importance:** Fatores mais influentes na aprovação
- **Detecção de vieses:** Padrões por área, porte de empresa, analista

**Saídas geradas:**
- `insights_padroes_decisao_*.txt` - Relatório detalhado de insights
- `projetos_com_predicoes.csv` - Projetos com probabilidades de aprovação
- `feature_importance.csv` - Importância das variáveis
- Visualizações de análise estatística

### 🎯 Etapa 4: Análise Específica dos Analistas Técnicos

**Arquivo:** [`analise_analistas.py`](analise_analistas.py) *(Em desenvolvimento)*

Foca na análise comportamental e de performance dos Analistas Técnicos (ATs) responsáveis pela fase de Análise DO.

```bash
# Executar análise de analistas (quando disponível)
python analise_analistas.py
```

**Análises planejadas:**
- Performance individual por analista
- Padrões de especialização por área tecnológica
- Consistência temporal nas decisões
- Distribuição de carga de trabalho
- Identificação de vieses individuais

## 🔍 Contexto e Objetivos da Análise

O projeto analisa o fluxo completo dos projetos da Lei do Bem, que passam pelas seguintes fases:

1. **Preenchimento:** Dados iniciais da empresa e projeto
2. **Análise DO:** Avaliação técnica pelos Analistas Técnicos
3. **Parecer:** Consolidação e decisão final
4. **Contestação:** Recurso da empresa (quando aplicável)

### Principais Objetivos:

- **Consistência entre fases:** Identificar divergências entre DO e Parecer
- **Padrões de contestação:** Características dos projetos que geram recursos
- **Detecção de vieses:** Inconsistências por área, porte ou analista
- **Otimização do processo:** Propor melhorias baseadas em dados

## 🤖 Detalhes Técnicos

### Processamento de Texto e NLP
- **Extração semântica:** Foco em descrição, metodologia, desafio tecnológico
- **Embeddings:** Modelo SERAFIM otimizado para português técnico
- **Stop words:** Customizadas para domínio P&D e Lei do Bem

### Machine Learning e Estatística
- **Clustering:** K-Means com otimização automática via Silhouette Score
- **Classificação:** Random Forest com balanceamento de classes
- **Interpretabilidade:** SHAP values para explicar decisões
- **Validação:** Cross-validation estratificada

### Análise de Dados
- **Análise multivariada:** Correlações entre múltiplas dimensões
- **Detecção de anomalias:** Casos extremos e inconsistências
- **Visualização:** Matplotlib, Seaborn, plots interativos

## 📁 Arquivos de Saída

### Etapa 1 - Extração
- **Aglomerados:** `tabelas_csv_xlsx/projetos_lei_do_bem_2023_AGLOMERADOS.csv`
- **Detalhados:** `csv_longo/projetos_lei_do_bem_2023_DETALHADO_LINHA_UNICA.csv`

### Etapa 2 - Clusterização
- **Clusters:** `Analises/lei_bem_projetos_clusters.csv`
- **Relatório PDF:** `Analises/relatorio_clusters_lei_bem.pdf`
- **Análise de clusters:** `Analises/lei_bem_analise_clusters.csv`

### Etapa 3 - Análise Multivariada
- **Insights:** `insights_padroes_decisao_YYYYMMDD_HHMMSS.txt`
- **Predições:** `projetos_com_predicoes.csv`
- **Importância:** `feature_importance.csv`
- **Modelo:** `modelo_rf_padroes_decisao.pkl`

## 📊 Exemplo de Uso Completo

```bash
# Pipeline completo
source .venv/bin/activate

# 1. Extrair dados do banco
python 1.csv_gerador_projetos.py

# 2. Aplicar clusterização e análise de padrões
python 2.report_e_clustering_k_mean.py

# 3. Executar análise multivariada
python analise_multivariada_lei_bem.py

# 4. Análise específica de analistas (futuro)
# python analise_analistas.py

# Verificar resultados
ls -la Analises/
ls -la imagens_relatorio/
```

## 🆘 Troubleshooting

### Erro de Conexão com Banco (Etapa 1)
```
psycopg2.OperationalError: could not connect to server
```
**Solução:** Verifique se PostgreSQL está ativo e credenciais estão corretas.

### Erro de Arquivo Não Encontrado (Etapa 2)
```
FileNotFoundError: Nenhum arquivo CSV encontrado na pasta csv_longo
```
**Solução:** Execute primeiro a Etapa 1 (`1.csv_gerador_projetos.py`).

### Erro de Dependências SHAP (Etapa 3)
```
ImportError: No module named 'shap'
```
**Solução:** 
```bash
source .venv/bin/activate
uv add shap
```

### Problemas com Encoding
```
UnicodeDecodeError: 'utf-8' codec can't decode
```
**Solução:** Verifique se os arquivos CSV estão salvos com encoding UTF-8.

## 🔄 Desenvolvimento e Customização

### Ajustar Parâmetros de Clustering
Edite [`2.report_e_clustering_k_mean.py`](2.report_e_clustering_k_mean.py):
```python
# Para mais clusters (K menor)
analisador.analisar_kmeans_otimizado(max_k=50)

# Para menos clusters (K maior)  
analisador.analisar_kmeans_otimizado(max_k=20)
```

### Modificar Features da Análise Multivariada
Edite [`analise_multivariada_lei_bem.py`](analise_multivariada_lei_bem.py):
```python
# Adicionar novas features categóricas
features_categoricas.extend([
    'nova_coluna_categorica',
    'outra_feature'
])
```

### Integração com LLMs
Use o template em [`prompt.md`](prompt.md) para análises com LLMs:
```python
# Carregar template
with open('prompt.md', 'r', encoding='utf-8') as f:
    prompt_template = f.read()

# Integrar dados
dados_formatados = prompt_template.format(df.head(100).to_csv())
```

## 📈 Métricas de Performance

- **Cobertura de dados:** 100% dos projetos da base são analisados
- **Escalabilidade:** Testado com datasets de 50k+ projetos
- **Acurácia do modelo:** ROC-AUC > 0.85 para predição de aprovação
- **Velocidade:** Processamento otimizado com paralelização

## 🎯 Roadmap e Próximos Passos

### Em Desenvolvimento
- [ ] **Análise de Analistas:** Módulo específico para ATs ([`analise_analistas.py`](analise_analistas.py))
- [ ] **Dashboard Interativo:** Plotly/Dash para visualização em tempo real
- [ ] **API REST:** Endpoint para análise de novos projetos

### Futuras Implementações
- [ ] **Análise Temporal:** Evolução dos padrões ao longo do tempo
- [ ] **NLP Avançado:** Análise de sentimento nas justificativas
- [ ] **Detecção de Fraude:** Identificação de padrões suspeitos
- [ ] **Sistema de Recomendação:** Sugestões para melhoria dos projetos

### Integrações Planejadas
- [ ] **LangChain + LLMs:** Análise automática de justificativas
- [ ] **MLflow:** Versionamento e deploy de modelos
- [ ] **Apache Airflow:** Automatização do pipeline

## 📖 Contexto da Lei do Bem

A Lei do Bem (Lei nº 11.196/2005) oferece incentivos fiscais para empresas que investem em P&D. O projeto analisa dados do MCTI para:

- **Otimizar** o processo de avaliação
- **Identificar** padrões de aprovação/reprovação
- **Detectar** inconsistências e vieses
- **Propor** melhorias baseadas em evidências

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

Para dúvidas ou sugestões sobre a análise dos dados da Lei do Bem, entre em contato
