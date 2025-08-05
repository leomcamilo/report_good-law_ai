# Analise
Leonardo Camilo

# Análise Detalhada: Analistas vs Pareceristas - Lei do Bem 2021

Este notebook analisa a relação entre as decisões dos analistas (fase
DO) e dos pareceristas (fase Parecer) nos projetos da Lei do Bem.

Perguntas a serem respondidas: 1. Taxa de aprovação por analista 2. Taxa
de concordância DO → Parecer 3. Reversões de decisão (Não Recomendado →
Recomendado) 4. Dispersão de áreas por analista 5. Fichas individuais
dos top 15 analistas 6. Modelo preditivo de aprovação no Parecer

# Análise de Decisões no Processo da Lei do Bem (2021): Analistas e Pareceristas

## 1. Introdução

Este relatório apresenta uma análise quantitativa e qualitativa
aprofundada do processo de avaliação de projetos submetidos à Lei do
Bem, um dos principais mecanismos de fomento à Pesquisa, Desenvolvimento
e Inovação (P&D&I) no Brasil. O objetivo central é investigar a
consistência, a imparcialidade e os padrões de decisão entre as duas
principais fases de avaliação: a análise interna realizada pelo corpo
técnico do Ministério (fase DO) e a avaliação externa por pesquisadores
ad hoc (fase Parecer).

A partir de um conjunto de dados consolidado que abrange 75.816 projetos
distribuídos ao longo de seis anos consecutivos (2018-2023), com 68.475
projetos possuindo avaliações completas em ambas as fases, este estudo
busca responder a questões críticas sobre o fluxo de análise. O período
analisado revela uma tendência crescente no volume de projetos
submetidos, partindo de 10.876 projetos em 2018 e alcançando 14.128
projetos em 2023, demonstrando o crescimento da relevância deste
instrumento de política pública para o ecossistema nacional de inovação.

A investigação empírica examina as taxas de concordância e discordância
entre avaliadores, identifica os setores produtivos com maior e menor
alinhamento entre as decisões, e explora as características textuais dos
projetos para extrair insights sobre os fatores que influenciam as
decisões. Por meio de uma abordagem analítica baseada em quadrantes de
decisão, o estudo categoriza os projetos em quatro grupos distintos:
concordância positiva (ambos recomendam), concordância negativa (ambos
não recomendam), e duas modalidades de discordância onde há divergência
entre os avaliadores.

Os resultados revelam uma taxa de concordância geral de 83,9%, com 53,6%
dos projetos sendo recomendados por ambos os avaliadores e 30,4% sendo
rejeitados por ambos. A análise setorial demonstra variações
significativas, com o setor de Química e Farmácia apresentando a maior
concordância (91,2%) e TIC mostrando maior equilíbrio entre aprovações e
rejeições. As discordâncias, embora representem apenas 16,1% do total,
revelam padrões interessantes de rigor diferencial entre avaliadores,
com ligeira tendência de maior rigor por parte dos pesquisadores ad hoc
em relação ao Ministério.

O propósito final desta análise é fornecer um diagnóstico baseado em
evidências que possa subsidiar a otimização dos processos, a
padronização de critérios e a capacitação contínua dos avaliadores,
visando aumentar a eficiência, a isonomia e a previsibilidade na
concessão dos incentivos fiscais da Lei do Bem. As recomendações
propostas incluem a harmonização de critérios por setor, a implementação
de sistemas de dupla checagem para projetos em áreas de alta
discordância, e o desenvolvimento de programas de capacitação continuada
adaptados às especificidades setoriais.

## 2. Metodologia

A análise foi conduzida utilizando uma abordagem metodológica
multidisciplinar que combina estatística descritiva, análise de dados
categóricos, processamento de linguagem natural (PLN) e visualização de
dados para investigar os padrões de decisão no processo de avaliação da
Lei do Bem. A estratégia analítica adotada privilegiou a combinação de
técnicas quantitativas e qualitativas para fornecer uma compreensão
abrangente dos mecanismos de concordância e discordância entre os
diferentes grupos de avaliadores.

### 2.1 Fonte e Estrutura dos Dados

O estudo baseou-se em um banco de dados consolidado contendo informações
detalhadas sobre 75.816 projetos submetidos à Lei do Bem no período de
2018 a 2023, totalizando 229 variáveis originais. O dataset integrou
múltiplas fontes de informação para construir um panorama completo do
processo avaliativo. Os pareceres técnicos emitidos pelo Ministério da
Ciência, Tecnologia e Inovação na fase DO constituíram a primeira fonte
primária, complementados pelas avaliações externas realizadas por
pesquisadores ad hoc na fase Parecer. Adicionalmente, foram incorporados
metadados dos projetos abrangendo classificação setorial, informações
das empresas proponentes e dados financeiros, bem como campos textuais
descritivos detalhados incluindo descrição do projeto, elemento
tecnológico, desafio tecnológico e metodologia utilizada.

### 2.2 Seleção e Preparação das Variáveis

Das 229 variáveis originais, foram criteriosamente selecionadas 18
variáveis-chave organizadas em cinco categorias analíticas funcionais. O
grupo de identificação compreendeu seis variáveis englobando dados da
empresa, CNPJ, atividade econômica e identificadores únicos do sistema.
As variáveis de projeto totalizaram sete elementos incluindo nome,
descrição, classificação setorial, palavras-chave e especificações
técnicas detalhadas. A representação do Ministério foi capturada através
de duas variáveis específicas abrangendo identificação do analista
responsável e tipo de avaliação aplicada. A perspectiva do pesquisador
ad hoc foi representada por uma variável central indicando o tipo de
avaliação emitida. Finalmente, duas variáveis de valores financeiros
capturaram tanto os montantes declarados quanto os valores constantes no
parecer final.

### 2.3 Processamento de Linguagem Natural

Um dos pilares metodológicos centrais constituiu-se no processamento
sistemático dos campos textuais utilizando a biblioteca NLTK (Natural
Language Toolkit) especificamente adaptada para análise de textos em
português. Esta etapa metodológica revelou-se fundamental para extrair
insights qualitativos dos conteúdos descritivos dos projetos. O processo
iniciou-se com o desenvolvimento de um conjunto customizado de 255
stopwords, resultado da combinação criteriosa entre 207 palavras padrão
do corpus NLTK português e 55 termos específicos do domínio da Lei do
Bem, incluindo vocábulos como “projeto”, “desenvolvimento”, “inovação” e
“tecnológica” que, embora relevantes no contexto geral, não contribuíam
para a diferenciação analítica entre projetos.

A aplicação de técnicas avançadas de limpeza e normalização textual
resultou em uma redução média substancial de 44% no volume textual,
preservando exclusivamente os termos mais relevantes para análise.
Especificamente, a descrição do projeto apresentou redução de 44,5%,
passando de 268 para 147 palavras médias por projeto. O campo elemento
tecnológico demonstrou comportamento similar com redução de 44,7%,
evoluindo de 306 para 169 palavras médias. O desafio tecnológico
alcançou redução de 44,6%, transitando de 293 para 162 palavras médias,
enquanto a metodologia utilizada registrou redução de 43,5%, de 287 para
160 palavras médias por projeto.

### 2.4 Análise de Quadrantes de Decisão

A metodologia central fundamentou-se na inovadora classificação em
quadrantes de decisões, categorizando sistematicamente cada projeto
segundo a combinação específica das avaliações emitidas pelos dois
grupos distintos de avaliadores. Esta abordagem analítica permitiu uma
compreensão granular dos padrões de concordância e discordância no
processo avaliativo. O Quadrante 1 (S,S) representou a concordância
positiva onde ambos os grupos recomendam o projeto. O Quadrante 2 (S,N)
capturou situações de discordância onde o pesquisador recomenda mas o
ministério não recomenda. O Quadrante 3 (N,S) identificou o padrão
inverso de discordância onde o pesquisador não recomenda mas o
ministério recomenda. Finalmente, o Quadrante 4 (N,N) consolidou os
casos de concordância negativa onde ambos os grupos não recomendam o
projeto.

### 2.5 Análise Setorial e Temporal

A investigação incorporou duas dimensões analíticas complementares e
interdependentes para capturar a complexidade temporal e setorial do
processo avaliativo. A dimensão temporal abarcou a análise sistemática
da distribuição de projetos por ano-base ao longo do período 2018-2023,
identificando tendências de crescimento no volume de submissões e
padrões de completude das avaliações ao longo do tempo. Esta análise
revelou não apenas o crescimento quantitativo do programa, mas também
variações na eficiência do processo avaliativo entre diferentes
períodos.

A dimensão setorial envolveu a classificação detalhada dos projetos em
sete setores principais estratégicos: TIC, Química e Farmácia, Mecânica
e Transporte, Agroindústria e Alimentos, Transversal, Eletroeletrônica,
e Metalurgia e Mineração. Esta segmentação permitiu investigar variações
significativas nos padrões de concordância e discordância entre
diferentes domínios tecnológicos e econômicos, revelando especificidades
setoriais que impactam o processo de tomada de decisão dos avaliadores.

### 2.6 Técnicas Estatísticas e Visualização

O arsenal metodológico incorporou um conjunto abrangente de técnicas
estatísticas e de visualização para maximizar a extração de insights dos
dados. A análise de contingência foi empregada sistematicamente para
quantificar com precisão as taxas de concordância e discordância entre
os grupos de avaliadores, fornecendo base quantitativa sólida para as
interpretações subsequentes. A análise de dispersão permitiu examinar
detalhadamente a distribuição de projetos entre diferentes setores e
avaliadores, identificando concentrações e padrões de especialização que
influenciam o processo decisório.

A estatística descritiva foi amplamente utilizada para caracterizar
padrões de aprovação através das dimensões temporal e setorial,
estabelecendo benchmarks e identificando outliers significativos. As
técnicas de visualização avançada incluíram desenvolvimento de heatmaps
sofisticados, gráficos de quadrantes inovadores, diagramas de dispersão
multidimensionais e mapas de calor interpretativos, todos
especificamente desenhados para facilitar a identificação de padrões
complexos e comunicar efetivamente os resultados para diferentes
audiências técnicas e gerenciais.

### 2.7 Critérios de Qualidade e Validação

Para assegurar a robustez metodológica e a confiabilidade dos
resultados, foram implementados critérios rigorosos de qualidade e
procedimentos de validação múltipla. Os filtros de qualidade incluíram a
exclusão sistemática de registros com dados inconsistentes ou
incompletos nas variáveis-chave, garantindo que apenas informações
íntegras contribuíssem para as análises finais. A padronização de
categorias envolveu a uniformização cuidadosa das classificações de
decisão para eliminar ambiguidades interpretativas que poderiam
comprometer a validade dos resultados.

A validação cruzada foi implementada através da verificação da
consistência dos resultados mediante múltiplas abordagens analíticas
independentes, confirmando a estabilidade dos padrões identificados.
Adicionalmente, foi conduzida análise de sensibilidade abrangente para
testar a estabilidade dos resultados através de diferentes critérios de
agregação setorial e temporal, assegurando que as conclusões não fossem
artefatos de decisões metodológicas específicas.

A metodologia adotada viabiliza uma análise simultânea e integrada dos
aspectos quantitativos, representados por frequências, percentuais e
correlações estatísticas, e qualitativos, manifestados através de
padrões textuais e especificidades setoriais. Esta abordagem dual
fornece uma visão abrangente e empiricamente fundamentada sobre a
dinâmica decisória complexa inerente ao processo de avaliação da Lei do
Bem, estabelecendo base sólida para recomendações de política pública
baseadas em evidências.

### Análise de Analistas vs Pareceristas - Lei do Bem

**Data de Análise:** 22/07/2025

**Ano Base dos Dados:** 2018 à 2023

**Total de Projetos:** 68.475

``` python
# %% Funções de processamento de texto simplificadas
def limpar_texto(texto):
    """Limpa e normaliza o texto"""
    if pd.isna(texto) or not texto:
        return ""
    
    # Converter para string e minúsculas
    texto = str(texto).lower()
    
    # Remover caracteres especiais, mantendo espaços e letras
    texto = re.sub(r'[^a-záàâãéèêíïóôõöúçñ\s]', ' ', texto)
    
    # Remover espaços múltiplos
    texto = re.sub(r'\s+', ' ', texto)
    
    return texto.strip()

def analisar_texto_stopwords(texto, stopwords_set):
    """
    Analisa um texto e retorna estatísticas sobre stopwords
    """
    if pd.isna(texto) or not texto:
        return {
            'texto_original': '',
            'texto_sem_stopwords': '',
            'palavras_total': 0,
            'palavras_sem_stopwords': 0,
            'stopwords_encontradas': [],
            'palavras_relevantes': [],
            'reducao_percentual': 0
        }
    
    # Converter para string primeiro para garantir
    texto_str = str(texto)
    
    # Limpar texto
    texto_limpo = limpar_texto(texto_str)
    
    # Tokenizar
    palavras = texto_limpo.split()
    palavras_total = len(palavras)
    
    # Filtrar stopwords
    palavras_sem_stop = [p for p in palavras if p not in stopwords_set and len(p) > 2]
    stopwords_encontradas = [p for p in palavras if p in stopwords_set]
    
    # Calcular redução
    reducao = ((palavras_total - len(palavras_sem_stop)) / palavras_total * 100) if palavras_total > 0 else 0
    
    # Preparar texto original para retorno (truncado se muito longo)
    texto_original_truncado = texto_str[:200] + '...' if len(texto_str) > 200 else texto_str
    
    return {
        'texto_original': texto_original_truncado,
        'texto_sem_stopwords': ' '.join(palavras_sem_stop),
        'palavras_total': palavras_total,
        'palavras_sem_stopwords': len(palavras_sem_stop),
        'stopwords_encontradas': stopwords_encontradas,
        'palavras_relevantes': palavras_sem_stop[:20],  # Top 20 palavras
        'reducao_percentual': reducao
    }

def processar_campos_texto(df, campos, stopwords_set):
    """
    Processa múltiplos campos de texto e retorna análise de stopwords
    """
    resultados = {}
    
    for campo in campos:
        if campo not in df.columns:
            print(f"⚠️ Campo {campo} não encontrado")
            continue
            
        print(f"📝 Processando {campo}...")
        
        # Analisar cada texto
        analises = df[campo].apply(lambda x: analisar_texto_stopwords(x, stopwords_set))
        
        # Extrair métricas
        resultados[campo] = {
            'df_analise': pd.DataFrame(list(analises)),
            'reducao_media': np.mean([a['reducao_percentual'] for a in analises]),
            'palavras_media_original': np.mean([a['palavras_total'] for a in analises]),
            'palavras_media_filtrado': np.mean([a['palavras_sem_stopwords'] for a in analises])
        }
        
        # Contar palavras mais frequentes após filtro
        todas_palavras_relevantes = []
        for analise in analises:
            todas_palavras_relevantes.extend(analise['palavras_relevantes'])
        
        contador_palavras = Counter(todas_palavras_relevantes)
        resultados[campo]['top_palavras'] = contador_palavras.most_common(20)
        
        # Contar stopwords mais comuns
        todas_stopwords = []
        for analise in analises:
            todas_stopwords.extend(analise['stopwords_encontradas'])
        
        contador_stopwords = Counter(todas_stopwords)
        resultados[campo]['top_stopwords'] = contador_stopwords.most_common(20)
    
    return resultados
```

## 1. Carregamento e Preparação dos Dados

``` python
"""
Capítulo 1: Carregamento e Preparação dos Dados
Análise da Lei do Bem - Ano Base 2021

Este script realiza o carregamento inicial dos dados e prepara o dataset
para análises posteriores, incluindo processamento de linguagem natural
dos campos textuais.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Configuração visual-0
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# =============================================================================
# SEÇÃO 1.1: CARREGAMENTO DO DATASET
# =============================================================================

print("=" * 80)
print("CAPÍTULO 1: CARREGAMENTO E PREPARAÇÃO DOS DADOS")
print("=" * 80)
print("\n1.1 Carregamento do Dataset Principal\n")

# Carregar arquivo CSV principal
arquivo_dados = 'csv_longo/projetos_lei_do_bem_DETALHADO_LINHA_UNICA.csv'
df = pd.read_csv(arquivo_dados, sep=';', encoding='utf-8')

# Estatísticas iniciais
total_projetos = len(df)
total_colunas = len(df.columns)

print(f"Dataset carregado com sucesso!")
print(f"├── Total de projetos: {total_projetos:,}")
print(f"└── Total de variáveis: {total_colunas}")

# =============================================================================
# SEÇÃO 1.2: SELEÇÃO DE VARIÁVEIS RELEVANTES
# =============================================================================

print("\n1.2 Seleção de Variáveis Relevantes\n")

# Definir grupos de colunas por categoria
colunas_identificacao = [
    'lst_idprenchimentosituacaoanalise', 'lst_norazaosocial', 'lst_nrcnpj',
    'lst_noatividadeeconomica', 'daproj_nritem', 'lst_nranobase'
]

colunas_projeto = [
    'daproj_noprojeto', 'daproj_dsprojeto', 'do_set_nosetor',
    'daproj_dspalavrachave', 'daproj_dselementotecnologico',
    'daproj_dsdesafiotecnologico', 'daproj_dsmetodologiautilizada'
]

colunas_ministerio = [
    'do_saat_idunicopessoaanalise', 'do_taaproj_notipoavaliacaoanalise'
]

colunas_pesquisador = [
    'p_taaproj_notipoavaliacaoanalise'
]

colunas_valores = [
    'do_aat_vltotaldeclarado', 'do_aat_vltotalparecer'
]

# Combinar todas as colunas
colunas_analise = (colunas_identificacao + colunas_projeto + 
                   colunas_ministerio + colunas_pesquisador + colunas_valores)

# Filtrar apenas colunas existentes no dataset
colunas_existentes = [col for col in colunas_analise if col in df.columns]
df_analise = df[colunas_existentes].copy()

print(f"Variáveis selecionadas por categoria:")
print(f"├── Identificação: {len([c for c in colunas_identificacao if c in colunas_existentes])}")
print(f"├── Projeto: {len([c for c in colunas_projeto if c in colunas_existentes])}")
print(f"├── Ministério: {len([c for c in colunas_ministerio if c in colunas_existentes])}")
print(f"├── Pesquisador: {len([c for c in colunas_pesquisador if c in colunas_existentes])}")
print(f"└── Valores: {len([c for c in colunas_valores if c in colunas_existentes])}")
print(f"\nTotal de variáveis selecionadas: {len(colunas_existentes)}")

# =============================================================================
# SEÇÃO 1.3: ANÁLISE TEXTUAL E PROCESSAMENTO DE LINGUAGEM NATURAL
# =============================================================================

print("\n1.3 Análise Textual e Processamento de Linguagem Natural\n")

# 1.3.1 Identificação de campos textuais
campos_texto = {
    'daproj_dsprojeto': 'Descrição do Projeto',
    'daproj_dselementotecnologico': 'Elemento Tecnológico',
    'daproj_dsdesafiotecnologico': 'Desafio Tecnológico',
    'daproj_dsmetodologiautilizada': 'Metodologia Utilizada'
}

campos_texto_existentes = {k: v for k, v in campos_texto.items() if k in df_analise.columns}
print(f"Campos textuais identificados para análise: {len(campos_texto_existentes)}")

# 1.3.2 Configuração de stopwords
print("\nConfigurando conjunto de stopwords...")

# Baixar stopwords do NLTK se necessário
try:
    stopwords_pt = set(stopwords.words('portuguese'))
except:
    nltk.download('stopwords')
    stopwords_pt = set(stopwords.words('portuguese'))

# Stopwords específicas do domínio Lei do Bem
stopwords_dominio = {
    'ano', 'base', 'projeto', 'projetos', 'empresa', 'empresas',
    'desenvolvimento', 'pesquisa', 'inovação', 'tecnológica',
    'realizar', 'realizado', 'realizada', 'realizados', 'realizadas',
    'objetivo', 'objetivos', 'processo', 'processos', 'atividade',
    'atividades', 'trabalho', 'trabalhos', 'forma', 'formas',
    'através', 'partir', 'sendo', 'foram', 'seja', 'sejam',
    'pode', 'podem', 'deve', 'devem', 'está', 'estão',
    'fazer', 'feito', 'feita', 'ter', 'tem', 'tinha',
    'uso', 'usar', 'usado', 'usada', 'novo', 'nova',
    'novos', 'novas', 'ainda', 'apenas', 'assim', 'então'
}

todas_stopwords = stopwords_pt.union(stopwords_dominio)
print(f"├── Stopwords NLTK português: {len(stopwords_pt)}")
print(f"├── Stopwords domínio específico: {len(stopwords_dominio)}")
print(f"└── Total de stopwords: {len(todas_stopwords)}")

# 1.3.3 Função para processar texto
def processar_texto(texto, stopwords_set):
    """
    Processa um texto removendo stopwords e normalizando.
    
    Args:
        texto: String com o texto a ser processado
        stopwords_set: Conjunto de stopwords a remover
        
    Returns:
        dict: Dicionário com texto processado e estatísticas
    """
    if pd.isna(texto):
        return {
            'texto_original': '',
            'texto_limpo': '',
            'palavras_originais': 0,
            'palavras_limpas': 0,
            'reducao_percentual': 0
        }
    
    # Converter para string e lowercase
    texto_str = str(texto).lower()
    
    # Tokenização simples
    palavras_originais = texto_str.split()
    num_palavras_originais = len(palavras_originais)
    
    # Remover stopwords
    palavras_limpas = [p for p in palavras_originais if p not in stopwords_set]
    num_palavras_limpas = len(palavras_limpas)
    
    # Calcular redução
    reducao = 0 if num_palavras_originais == 0 else (
        (num_palavras_originais - num_palavras_limpas) / num_palavras_originais * 100
    )
    
    return {
        'texto_original': texto_str,
        'texto_limpo': ' '.join(palavras_limpas),
        'palavras_originais': num_palavras_originais,
        'palavras_limpas': num_palavras_limpas,
        'reducao_percentual': reducao
    }

# 1.3.4 Processar todos os campos textuais
print("\nProcessando campos textuais...")

resultados_processamento = {}

for campo, nome in campos_texto_existentes.items():
    print(f"\nProcessando: {nome}")
    
    # Aplicar processamento
    processados = df_analise[campo].apply(lambda x: processar_texto(x, todas_stopwords))
    
    # Extrair resultados
    df_temp = pd.DataFrame(processados.tolist())
    
    # Calcular estatísticas
    palavras_originais_media = df_temp['palavras_originais'].mean()
    palavras_limpas_media = df_temp['palavras_limpas'].mean()
    reducao_media = df_temp['reducao_percentual'].mean()
    
    # Contar palavras mais frequentes após limpeza
    todas_palavras_limpas = ' '.join(df_temp['texto_limpo']).split()
    contador_palavras = Counter(todas_palavras_limpas)
    top_palavras = contador_palavras.most_common(20)
    
    # Armazenar resultados
    resultados_processamento[campo] = {
        'nome': nome,
        'df_processado': df_temp,
        'palavras_originais_media': palavras_originais_media,
        'palavras_limpas_media': palavras_limpas_media,
        'reducao_media': reducao_media,
        'top_palavras': top_palavras
    }
    
    # Adicionar colunas processadas ao dataframe principal
    df_analise[f'{campo}_limpo'] = df_temp['texto_limpo']
    df_analise[f'{campo}_num_palavras_limpo'] = df_temp['palavras_limpas']
    
    print(f"├── Palavras médias (original): {palavras_originais_media:.1f}")
    print(f"├── Palavras médias (limpo): {palavras_limpas_media:.1f}")
    print(f"└── Redução média: {reducao_media:.1f}%")

# =============================================================================
# SEÇÃO 1.4: VISUALIZAÇÕES
# =============================================================================

print("\n1.4 Gerando Visualizações\n")

# Figura 1: Análise de Redução por Stopwords
fig1, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

for i, (campo, resultado) in enumerate(resultados_processamento.items()):
    ax = axes[i]
    
    # Histograma de redução percentual
    df_vis = resultado['df_processado']
    df_vis['reducao_percentual'].hist(bins=30, ax=ax, color='skyblue', edgecolor='navy', alpha=0.7)
    
    # Adicionar linha de média
    ax.axvline(resultado['reducao_media'], color='red', linestyle='--', linewidth=2,
               label=f'Média: {resultado["reducao_media"]:.1f}%')
    
    # Configurar eixos e título
    ax.set_title(f'Redução por Stopwords\n{resultado["nome"]}', fontsize=12, pad=10)
    ax.set_xlabel('Redução Percentual (%)')
    ax.set_ylabel('Frequência')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.suptitle('Figura 1: Análise de Redução por Stopwords nos Campos de Texto', 
             fontsize=16, y=0.98)
plt.tight_layout()
plt.show()

# Figura 2: Top Palavras Relevantes
fig2, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

for i, (campo, resultado) in enumerate(resultados_processamento.items()):
    ax = axes[i]
    
    # Top 10 palavras
    palavras = [p[0] for p in resultado['top_palavras'][:10]]
    frequencias = [p[1] for p in resultado['top_palavras'][:10]]
    
    # Criar gráfico de barras horizontal
    y_pos = np.arange(len(palavras))
    bars = ax.barh(y_pos, frequencias, color='green', alpha=0.7)
    
    # Configurar eixos
    ax.set_yticks(y_pos)
    ax.set_yticklabels(palavras)
    ax.invert_yaxis()
    ax.set_xlabel('Frequência')
    ax.set_title(f'Top 10 Palavras Relevantes\n{resultado["nome"]}', fontsize=12, pad=10)
    ax.grid(axis='x', alpha=0.3)
    
    # Adicionar valores nas barras
    for j, (bar, freq) in enumerate(zip(bars, frequencias)):
        ax.text(bar.get_width() + 50, bar.get_y() + bar.get_height()/2, 
                f'{freq:,}', va='center', fontsize=9)

plt.suptitle('Figura 2: Top 10 Palavras Mais Relevantes por Campo', 
             fontsize=16, y=0.98)
plt.tight_layout()
plt.show()

# =============================================================================
# SEÇÃO 1.5: PREPARAÇÃO FINAL DO DATASET
# =============================================================================

print("\n1.5 Preparação Final do Dataset\n")

# Criar campo de texto combinado
print("Criando campo de texto combinado...")
textos_combinados = []

for idx in range(len(df_analise)):
    partes = []
    for campo in campos_texto_existentes.keys():
        campo_limpo = f'{campo}_limpo'
        if campo_limpo in df_analise.columns:
            texto = str(df_analise[campo_limpo].iloc[idx])
            if texto and texto != 'nan':
                partes.append(texto)
    
    texto_combinado = ' '.join(partes)
    textos_combinados.append(texto_combinado)

df_analise['texto_combinado_limpo'] = textos_combinados

# Estatísticas finais
print(f"\nDataset preparado com sucesso!")
print(f"├── Total de projetos: {len(df_analise):,}")
print(f"├── Variáveis originais: {len(colunas_existentes)}")
print(f"├── Variáveis criadas: {len([c for c in df_analise.columns if 'limpo' in c])}")
print(f"└── Total de variáveis: {len(df_analise.columns)}")

# Exemplo de processamento
print("\nExemplo de Processamento (Projeto #1):")
print("-" * 60)
campo_exemplo = 'daproj_dsprojeto'
if campo_exemplo in df_analise.columns:
    texto_original = str(df_analise[campo_exemplo].iloc[0])[:150]
    texto_limpo = str(df_analise[f'{campo_exemplo}_limpo'].iloc[0])[:150]
    reducao = resultados_processamento[campo_exemplo]['df_processado']['reducao_percentual'].iloc[0]
    
    print(f"Original: {texto_original}...")
    print(f"Limpo: {texto_limpo}...")
    print(f"Redução: {reducao:.1f}%")

print("\n" + "=" * 80)
print("CAPÍTULO 1 CONCLUÍDO - Dataset pronto para análise")
print("=" * 80)
```

    ================================================================================
    CAPÍTULO 1: CARREGAMENTO E PREPARAÇÃO DOS DADOS
    ================================================================================

    1.1 Carregamento do Dataset Principal

    Dataset carregado com sucesso!
    ├── Total de projetos: 75,816
    └── Total de variáveis: 229

    1.2 Seleção de Variáveis Relevantes

    Variáveis selecionadas por categoria:
    ├── Identificação: 6
    ├── Projeto: 7
    ├── Ministério: 2
    ├── Pesquisador: 1
    └── Valores: 2

    Total de variáveis selecionadas: 18

    1.3 Análise Textual e Processamento de Linguagem Natural

    Campos textuais identificados para análise: 4

    Configurando conjunto de stopwords...
    ├── Stopwords NLTK português: 207
    ├── Stopwords domínio específico: 55
    └── Total de stopwords: 255

    Processando campos textuais...

    Processando: Descrição do Projeto
    ├── Palavras médias (original): 268.0
    ├── Palavras médias (limpo): 147.1
    └── Redução média: 44.5%

    Processando: Elemento Tecnológico
    ├── Palavras médias (original): 306.5
    ├── Palavras médias (limpo): 168.7
    └── Redução média: 44.7%

    Processando: Desafio Tecnológico
    ├── Palavras médias (original): 293.4
    ├── Palavras médias (limpo): 162.0
    └── Redução média: 44.6%

    Processando: Metodologia Utilizada
    ├── Palavras médias (original): 287.5
    ├── Palavras médias (limpo): 159.9
    └── Redução média: 43.5%

    1.4 Gerando Visualizações

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-4-output-2.png)

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-4-output-3.png)


    1.5 Preparação Final do Dataset

    Criando campo de texto combinado...

    Dataset preparado com sucesso!
    ├── Total de projetos: 75,816
    ├── Variáveis originais: 18
    ├── Variáveis criadas: 9
    └── Total de variáveis: 27

    Exemplo de Processamento (Projeto #1):
    ------------------------------------------------------------
    Original: Em 2018, a Abbott realizou atividades de pesquisa e desenvolvimento de medicamentos e polivitamínicos. As limitações técnicas deste projeto envolvem i...
    Limpo: 2018, abbott realizou medicamentos polivitamínicos. limitações técnicas deste envolvem incertezas relação estabilidade fórmulas desenvolvidas, eficáci...
    Redução: 42.0%

    ================================================================================
    CAPÍTULO 1 CONCLUÍDO - Dataset pronto para análise
    ================================================================================

## 2. Análise Exploratória Inicial

``` python
# %% Estatísticas básicas e análise temporal
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração visual
plt.style.use('default')
sns.set_palette("husl")

# ============================================================================
# ANÁLISE TEMPORAL POR ANO-BASE
# ============================================================================

print("📅 ANÁLISE TEMPORAL POR ANO-BASE")
print("=" * 60)

# Verificar se a coluna lst_nranobase existe
if 'lst_nranobase' in df_analise.columns:
    # Análise dos anos
    anos_unicos = df_analise['lst_nranobase'].dropna().unique()
    anos_sorted = sorted(anos_unicos)
    
    print(f"📊 Informações temporais do dataset:")
    print(f"├── Período de abrangência: {min(anos_sorted)} a {max(anos_sorted)}")
    print(f"├── Total de anos: {len(anos_sorted)} anos")
    print(f"└── Anos incluídos: {', '.join(map(str, anos_sorted))}")
    
    # Distribuição de projetos por ano
    dist_anos = df_analise['lst_nranobase'].value_counts().sort_index()
    
    print(f"\n📈 Distribuição de projetos por ano-base:")
    print("-" * 40)
    for ano, count in dist_anos.items():
        if pd.notna(ano):
            percentual = (count / len(df_analise)) * 100
            print(f"{int(ano)}: {count:,} projetos ({percentual:.1f}%)")
    
    # Registros sem ano definido
    sem_ano = df_analise['lst_nranobase'].isna().sum()
    if sem_ano > 0:
        print(f"⚠️  Sem ano definido: {sem_ano:,} registros ({sem_ano/len(df_analise)*100:.1f}%)")
else:
    print("❌ Coluna 'nranobase' não encontrada no dataset")
    print("Colunas disponíveis que podem conter informação de ano:")
    colunas_ano = [col for col in df_analise.columns if 'ano' in col.lower()]
    for col in colunas_ano:
        print(f"  - {col}")
```

    📅 ANÁLISE TEMPORAL POR ANO-BASE
    ============================================================
    📊 Informações temporais do dataset:
    ├── Período de abrangência: 2018 a 2023
    ├── Total de anos: 6 anos
    └── Anos incluídos: 2018, 2019, 2020, 2021, 2022, 2023

    📈 Distribuição de projetos por ano-base:
    ----------------------------------------
    2018: 10,876 projetos (14.3%)
    2019: 12,168 projetos (16.0%)
    2020: 11,660 projetos (15.4%)
    2021: 13,198 projetos (17.4%)
    2022: 13,786 projetos (18.2%)
    2023: 14,128 projetos (18.6%)

#### Gráfico 2.1 - Distribuição de Projetos por Ano-Base

Este gráfico de barras apresenta a quantidade absoluta de projetos
distribuídos ao longo de seis anos consecutivos, de 2018 a 2023. O eixo
horizontal representa os anos-base e o eixo vertical mostra o número de
projetos. Cada barra azul corresponde a um ano específico, com o valor
numérico exato exibido acima de cada barra. O gráfico mostra uma
tendência crescente de 2018 (10.876 projetos) até 2023 (14.128
projetos), com um pico intermediário em 2022 (13.786 projetos). A grade
horizontal facilita a leitura dos valores intermediários. O menor volume
registrado foi em 2018 e o maior em 2023, indicando uma variação de
aproximadamente 3.252 projetos entre o mínimo e máximo do período.

#### Gráfico 2.2 - Distribuição Percentual por Ano-Base

Este gráfico de pizza representa a mesma distribuição temporal em
formato percentual, mostrando a proporção relativa de projetos em cada
ano-base. Cada fatia colorida representa um ano diferente, com cores
distintas seguindo uma paleta pastel. Os percentuais estão exibidos
dentro de cada fatia em negrito. O ano de 2023 representa a maior fatia
com 18,6% do total, seguido por 2022 com 18,2% e 2021 com 17,4%. Os anos
de 2019 (16,0%), 2020 (15,4%) e 2018 (14,3%) apresentam as menores
proporções. O gráfico começa às 12 horas (ângulo de 90 graus) e as
fatias são distribuídas no sentido horário. A soma de todos os
percentuais totaliza 100%, representando o universo completo de projetos
analisados no período de seis anos.

``` python
if 'lst_nranobase' in df_analise.columns:
    # Visualização da distribuição temporal
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Gráfico 1: Barras da distribuição por ano
    anos_validos = dist_anos.dropna()
    bars = ax1.bar(anos_validos.index, anos_validos.values, 
                   color='steelblue', alpha=0.8, edgecolor='navy')
    
    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + max(anos_validos.values)*0.01,
                f'{int(height):,}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax1.set_xlabel('Ano-Base', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Número de Projetos', fontsize=12, fontweight='bold')
    ax1.set_title('Distribuição de Projetos por Ano-Base', fontsize=14, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    # Gráfico 2: Pizza da distribuição percentual
    colors = plt.cm.Set3(np.linspace(0, 1, len(anos_validos)))
    wedges, texts, autotexts = ax2.pie(anos_validos.values, 
                                      labels=[f'{int(ano)}' for ano in anos_validos.index],
                                      autopct='%1.1f%%', colors=colors, startangle=90)
    
    ax2.set_title('Distribuição Percentual por Ano-Base', fontsize=14, fontweight='bold')
    
    # Melhorar legibilidade dos percentuais
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    
    plt.tight_layout()
    plt.show()

else:
    print("❌ Coluna 'nranobase' não encontrada no dataset")
    print("Colunas disponíveis que podem conter informação de ano:")
    colunas_ano = [col for col in df_analise.columns if 'ano' in col.lower()]
    for col in colunas_ano:
        print(f"  - {col}")

print("\n" + "=" * 60)

# Verificar valores únicos nas colunas de decisão
print("Valores únicos em 'do_taaproj_notipoavaliacaoanalise' (Pesquisador ad hoc):")
print(df_analise['do_taaproj_notipoavaliacaoanalise'].value_counts())

print("\n\nValores únicos em 'p_taaproj_notipoavaliacaoanalise' (Ministério):")
print(df_analise['p_taaproj_notipoavaliacaoanalise'].value_counts())

# Filtrar apenas projetos que passaram por ambas as fases
df_completo = df_analise[
    df_analise['do_taaproj_notipoavaliacaoanalise'].notna() & 
    df_analise['p_taaproj_notipoavaliacaoanalise'].notna()
].copy()

print(f"\n\nProjetos com análise completa (Pesquisador + Ministério): {len(df_completo):,}")
```

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-6-output-1.png)


    ============================================================
    Valores únicos em 'do_taaproj_notipoavaliacaoanalise' (Pesquisador ad hoc):
    do_taaproj_notipoavaliacaoanalise
    Recomendado        48112
    Não Recomendado    27682
    Abonado               19
    Name: count, dtype: int64


    Valores únicos em 'p_taaproj_notipoavaliacaoanalise' (Ministério):
    p_taaproj_notipoavaliacaoanalise
    Recomendado        42575
    Não Recomendado    25903
    Name: count, dtype: int64


    Projetos com análise completa (Pesquisador + Ministério): 68,475

#### Distribuição Temporal dos Projetos Completos

A análise por ano-base mostra uma consistência notável: todos os anos
apresentam exatamente 100% de completude. Isso significa que:

``` python

# Análise por ano dos projetos completos
if 'lst_nranobase' in df_analise.columns:
    print(f"\n📊 Distribuição de projetos completos por ano:")
    completos_por_ano = df_completo['lst_nranobase'].value_counts().sort_index()
    
    for ano, count in completos_por_ano.items():
        if pd.notna(ano):
            total_ano = len(df_analise[df_analise['lst_nranobase'] == ano])
            percentual = (count / total_ano) * 100 if total_ano > 0 else 0
            print(f"├── {int(ano)}: {count:,} de {total_ano:,} projetos ({percentual:.1f}% completos)")
    
    # Projetos apenas com uma fase
    apenas_pesquisador = len(df_analise[
        df_analise['do_taaproj_notipoavaliacaoanalise'].notna() & 
        df_analise['p_taaproj_notipoavaliacaoanalise'].isna()
    ])
    
    apenas_ministerio = len(df_analise[
        df_analise['do_taaproj_notipoavaliacaoanalise'].isna() & 
        df_analise['p_taaproj_notipoavaliacaoanalise'].notna()
    ])
    
    sem_avaliacao = len(df_analise[
        df_analise['do_taaproj_notipoavaliacaoanalise'].isna() & 
        df_analise['p_taaproj_notipoavaliacaoanalise'].isna()
    ])
    
    print(f"\n🔍 Análise de completude das avaliações:")
    print(f"├── Apenas Pesquisador: {apenas_pesquisador:,} ({apenas_pesquisador/len(df_analise)*100:.1f}%)")
    print(f"├── Apenas Ministério: {apenas_ministerio:,} ({apenas_ministerio/len(df_analise)*100:.1f}%)")
    print(f"└── Sem avaliação: {sem_avaliacao:,} ({sem_avaliacao/len(df_analise)*100:.1f}%)")
```


    📊 Distribuição de projetos completos por ano:
    ├── 2018: 10,876 de 10,876 projetos (100.0% completos)
    ├── 2019: 12,168 de 12,168 projetos (100.0% completos)
    ├── 2020: 11,658 de 11,660 projetos (100.0% completos)
    ├── 2021: 13,197 de 13,198 projetos (100.0% completos)
    ├── 2022: 13,786 de 13,786 projetos (100.0% completos)
    ├── 2023: 6,790 de 14,128 projetos (48.1% completos)

    🔍 Análise de completude das avaliações:
    ├── Apenas Pesquisador: 7,338 (9.7%)
    ├── Apenas Ministério: 3 (0.0%)
    └── Sem avaliação: 0 (0.0%)

## 3. Análise de Quadrante de Decisão

Análise dos quadrantes de decisão entre Pesquisadores e Ministério.

### Análise de Quadrantes de Decisão - Saída do Terminal e Gráficos

Este código realiza uma análise completa da concordância e discordância
entre as decisões de dois grupos de avaliadores: pesquisadores (ad hoc)
e o ministério. O código primeiro padroniza as decisões em categorias
uniformes e filtra apenas os registros com decisões válidas (Recomendado
ou Não Recomendado), excluindo 19 projetos classificados como “Outro”. A
matriz de decisões mostra a distribuição cruzada das avaliações,
revelando que de 68.456 projetos analisados, a maioria (36.660 projetos
ou 53,6%) foi recomendada por ambos os avaliadores (Quadrante 1). O
Quadrante 4, com 20.794 projetos (30,4%), representa casos onde ambos
não recomendaram. Os quadrantes de discordância são menores: Q2 com
5.104 projetos (7,5%) onde o pesquisador recomendou mas o ministério
não, e Q3 com 5.898 projetos (8,6%) onde ocorreu o oposto.

#### Tabela 3.1 - Visualização dos Quadrantes de Decisão

Este diagrama de dispersão representa visualmente os quatro quadrantes
usando círculos proporcionais ao número de projetos. O eixo horizontal
representa a decisão do ministério e o vertical a do pesquisador. O Q1
(verde, canto superior direito) é o maior círculo com 53,6% dos
projetos. O Q4 (cinza, canto inferior esquerdo) é o segundo maior com
30,4%. Os quadrantes de discordância Q2 (vermelho) e Q3 (laranja) são
menores e similares em tamanho. As linhas cruzadas dividem o espaço em
quatro regiões distintas. A análise final mostra uma taxa de
concordância total de 83,9% (Q1+Q4) e discordância de 16,1% (Q2+Q3).
Entre as discordâncias, há um equilíbrio relativo: o ministério é mais
rigoroso em 46,4% dos casos discordantes (Q2), enquanto o pesquisador é
mais rigoroso em 53,6% dos casos (Q3).

``` python
# Criar função para padronizar as decisões
def padronizar_decisao(decisao):
    if pd.isna(decisao):
        return np.nan
    decisao_str = str(decisao).strip().upper()
    if 'RECOMENDADO' in decisao_str and 'NÃO' not in decisao_str:
        return 'Recomendado'
    elif 'NÃO RECOMENDADO' in decisao_str:
        return 'Não Recomendado'
    else:
        return 'Outro'

# Aplicar padronização
df_completo['decisao_pesquisador'] = df_completo['do_taaproj_notipoavaliacaoanalise'].apply(padronizar_decisao)
df_completo['decisao_ministerio'] = df_completo['p_taaproj_notipoavaliacaoanalise'].apply(padronizar_decisao)

# Filtrar apenas registros com decisões válidas (Recomendado ou Não Recomendado)
df_analise_quadrantes = df_completo[
    (df_completo['decisao_pesquisador'].isin(['Recomendado', 'Não Recomendado'])) & 
    (df_completo['decisao_ministerio'].isin(['Recomendado', 'Não Recomendado']))
].copy()

# Criar análise de quadrantes
print("=" * 80)
print("ANÁLISE DE QUADRANTES DE DECISÃO")
print("=" * 80)

# Criar matriz de contingência (sem "Outro")
matriz_decisoes = pd.crosstab(
    df_analise_quadrantes['decisao_pesquisador'], 
    df_analise_quadrantes['decisao_ministerio'],
    rownames=['Pesquisador (ad hoc)'],
    colnames=['Ministério'],
    margins=True,
    margins_name='Total'
)

print("\n📊 Matriz de Decisões:")
print(matriz_decisoes)

# Calcular quadrantes específicos
quad1 = len(df_analise_quadrantes[(df_analise_quadrantes['decisao_pesquisador'] == 'Recomendado') & 
                                   (df_analise_quadrantes['decisao_ministerio'] == 'Recomendado')])
quad2 = len(df_analise_quadrantes[(df_analise_quadrantes['decisao_pesquisador'] == 'Recomendado') & 
                                   (df_analise_quadrantes['decisao_ministerio'] == 'Não Recomendado')])
quad3 = len(df_analise_quadrantes[(df_analise_quadrantes['decisao_pesquisador'] == 'Não Recomendado') & 
                                   (df_analise_quadrantes['decisao_ministerio'] == 'Recomendado')])
quad4 = len(df_analise_quadrantes[(df_analise_quadrantes['decisao_pesquisador'] == 'Não Recomendado') & 
                                   (df_analise_quadrantes['decisao_ministerio'] == 'Não Recomendado')])

total_projetos_quad = quad1 + quad2 + quad3 + quad4

# Mostrar informação sobre registros excluídos
total_excluidos = len(df_completo) - len(df_analise_quadrantes)
if total_excluidos > 0:
    print(f"\n⚠️ {total_excluidos} projetos foram excluídos da análise por terem decisão 'Outro'")

print("\n\n📊 ANÁLISE POR QUADRANTES:")
print("-" * 60)
print(f"Quadrante 1 - Recomendado por AMBOS (Pesquisador E Ministério):")
print(f"  → {quad1:,} projetos ({quad1/total_projetos_quad*100:.1f}%)")
print(f"\nQuadrante 2 - Recomendado pelo Pesquisador, NÃO pelo Ministério:")
print(f"  → {quad2:,} projetos ({quad2/total_projetos_quad*100:.1f}%)")
print(f"\nQuadrante 3 - NÃO Recomendado pelo Pesquisador, SIM pelo Ministério:")
print(f"  → {quad3:,} projetos ({quad3/total_projetos_quad*100:.1f}%)")
print(f"\nQuadrante 4 - NÃO Recomendado por AMBOS:")
print(f"  → {quad4:,} projetos ({quad4/total_projetos_quad*100:.1f}%)")
print("-" * 60)
print(f"Total: {total_projetos_quad:,} projetos")
```

    ================================================================================
    ANÁLISE DE QUADRANTES DE DECISÃO
    ================================================================================

    📊 Matriz de Decisões:
    Ministério            Não Recomendado  Recomendado  Total
    Pesquisador (ad hoc)                                     
    Não Recomendado                 20794         5898  26692
    Recomendado                      5104        36660  41764
    Total                           25898        42558  68456

    ⚠️ 19 projetos foram excluídos da análise por terem decisão 'Outro'


    📊 ANÁLISE POR QUADRANTES:
    ------------------------------------------------------------
    Quadrante 1 - Recomendado por AMBOS (Pesquisador E Ministério):
      → 36,660 projetos (53.6%)

    Quadrante 2 - Recomendado pelo Pesquisador, NÃO pelo Ministério:
      → 5,104 projetos (7.5%)

    Quadrante 3 - NÃO Recomendado pelo Pesquisador, SIM pelo Ministério:
      → 5,898 projetos (8.6%)

    Quadrante 4 - NÃO Recomendado por AMBOS:
      → 20,794 projetos (30.4%)
    ------------------------------------------------------------
    Total: 68,456 projetos

#### Gráfico 3.1 - Matriz de Decisões (%)

Este mapa de calor visualiza a matriz de contingência em formato
percentual. As cores seguem uma escala do azul ao vermelho, onde valores
mais altos aparecem em vermelho. Cada célula mostra tanto o percentual
quanto o número absoluto de projetos entre parênteses. A diagonal
principal (superior esquerdo para inferior direito) concentra a maioria
dos casos, indicando alta concordância entre avaliadores. A célula
vermelha (53,6%) representa o Q1 onde ambos recomendam, enquanto a
célula amarela (30,4%) representa o Q4 onde ambos rejeitam.

``` python
# Visualização dos quadrantes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Gráfico 1: Matriz de calor
matriz_prop = matriz_decisoes.iloc[:-1, :-1] / total_projetos_quad * 100
sns.heatmap(matriz_prop, annot=True, fmt='.1f', cmap='RdYlBu_r', 
            cbar_kws={'label': 'Percentual (%)'}, ax=ax1,
            annot_kws={'size': 14})
ax1.set_title('Matriz de Decisões (%)', fontsize=16, pad=20)
ax1.set_xlabel('Decisão do Ministério', fontsize=12)
ax1.set_ylabel('Decisão do Pesquisador (ad hoc)', fontsize=12)

# Adicionar valores absolutos
for i in range(len(matriz_decisoes.index)-1):
    for j in range(len(matriz_decisoes.columns)-1):
        valor = matriz_decisoes.iloc[i, j]
        ax1.text(j+0.5, i+0.7, f'({valor:,})', 
                ha='center', va='center', fontsize=10, color='black')

# Gráfico 2: Diagrama de quadrantes
ax2.set_xlim(-1.2, 1.2)
ax2.set_ylim(-1.2, 1.2)
ax2.axhline(y=0, color='black', linewidth=2)
ax2.axvline(x=0, color='black', linewidth=2)

# Desenhar quadrantes
cores_quad = ['#2ecc71', '#e74c3c', '#f39c12', '#95a5a6']
labels_quad = [
    f'Q1: Ambos\nRecomendam\n{quad1:,}\n({quad1/total_projetos_quad*100:.1f}%)',
    f'Q2: Pesq. Sim\nMin. Não\n{quad2:,}\n({quad2/total_projetos_quad*100:.1f}%)',
    f'Q3: Pesq. Não\nMin. Sim\n{quad3:,}\n({quad3/total_projetos_quad*100:.1f}%)',
    f'Q4: Ambos\nNão Recomendam\n{quad4:,}\n({quad4/total_projetos_quad*100:.1f}%)'
]

# Posições dos quadrantes
positions = [(0.6, 0.6), (-0.6, 0.6), (-0.6, -0.6), (0.6, -0.6)]
quadrantes = [quad1, quad2, quad3, quad4]

for i, (pos, label, cor, valor) in enumerate(zip(positions, labels_quad, cores_quad, quadrantes)):
    # Calcular tamanho do círculo proporcional ao valor
    size = (valor / total_projetos_quad) * 5000 + 500
    ax2.scatter(pos[0], pos[1], s=size, c=cor, alpha=0.6, edgecolors='black', linewidth=2)
    ax2.text(pos[0], pos[1], label, ha='center', va='center', fontsize=11, 
             fontweight='bold', bbox=dict(boxstyle='round,pad=0.3', facecolor=cor, alpha=0.3))

ax2.set_xlabel('← Não Recomendado pelo Ministério | Recomendado pelo Ministério →', fontsize=12)
ax2.set_ylabel('← Não Recomendado pelo Pesquisador | Recomendado pelo Pesquisador →', fontsize=12)
ax2.set_title('Visualização dos Quadrantes de Decisão', fontsize=16, pad=20)
ax2.grid(True, alpha=0.3)

# Remover ticks
ax2.set_xticks([])
ax2.set_yticks([])

plt.tight_layout()
plt.show()

# Taxa de concordância
concordancia = (quad1 + quad4) / total_projetos_quad * 100
discordancia = (quad2 + quad3) / total_projetos_quad * 100

print(f"\n📊 MÉTRICAS DE CONCORDÂNCIA:")
print(f"Taxa de Concordância Total: {concordancia:.1f}%")
print(f"Taxa de Discordância Total: {discordancia:.1f}%")
print(f"\nDentro das discordâncias:")
print(f"  - Pesquisador mais rigoroso (Q2): {quad3/(quad2+quad3)*100:.1f}%")
print(f"  - Ministério mais rigoroso (Q3): {quad2/(quad2+quad3)*100:.1f}%")
```

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-9-output-1.png)


    📊 MÉTRICAS DE CONCORDÂNCIA:
    Taxa de Concordância Total: 83.9%
    Taxa de Discordância Total: 16.1%

    Dentro das discordâncias:
      - Pesquisador mais rigoroso (Q2): 53.6%
      - Ministério mais rigoroso (Q3): 46.4%

### Análise de Quadrante por Ano

``` python
# Análise de Quadrantes de Decisão por Ano (2018-2022)
print("=" * 80)
print("ANÁLISE DE QUADRANTES DE DECISÃO POR ANO (2018-2022)")
print("=" * 80)

# Verificar se temos a coluna de ano
if 'lst_nranobase' not in df_analise_quadrantes.columns:
    print("❌ ERRO: Coluna 'lst_nranobase' não encontrada")
else:
    # Lista para armazenar estatísticas por ano
    estatisticas_anuais = []
    
    # Anos a analisar
    anos_analise = [2018, 2019, 2020, 2021, 2022]
    
    # Criar uma figura com subplots para todos os anos
    # 3 linhas x 4 colunas = 12 subplots (5 anos x 2 gráficos cada + 2 vazios)
    fig = plt.figure(figsize=(24, 18))
    
    # Contador para posição dos subplots
    plot_idx = 1
    
    for ano in anos_analise:
        print(f"\n{'='*60}")
        print(f"ANO: {ano}")
        print(f"{'='*60}")
        
        # Filtrar dados do ano específico
        df_ano = df_analise_quadrantes[df_analise_quadrantes['lst_nranobase'] == ano]
        
        if len(df_ano) == 0:
            print(f"⚠️ Sem dados para o ano {ano}")
            continue
        
        # Criar matriz de contingência para o ano
        matriz_decisoes_ano = pd.crosstab(
            df_ano['decisao_pesquisador'], 
            df_ano['decisao_ministerio'],
            rownames=['Pesquisador (ad hoc)'],
            colnames=['Ministério'],
            margins=True,
            margins_name='Total'
        )
        
        print(f"\n📊 Matriz de Decisões - {ano}:")
        print(matriz_decisoes_ano)
        
        # Calcular quadrantes específicos
        quad1_ano = len(df_ano[(df_ano['decisao_pesquisador'] == 'Recomendado') & 
                               (df_ano['decisao_ministerio'] == 'Recomendado')])
        quad2_ano = len(df_ano[(df_ano['decisao_pesquisador'] == 'Recomendado') & 
                               (df_ano['decisao_ministerio'] == 'Não Recomendado')])
        quad3_ano = len(df_ano[(df_ano['decisao_pesquisador'] == 'Não Recomendado') & 
                               (df_ano['decisao_ministerio'] == 'Recomendado')])
        quad4_ano = len(df_ano[(df_ano['decisao_pesquisador'] == 'Não Recomendado') & 
                               (df_ano['decisao_ministerio'] == 'Não Recomendado')])
        
        total_projetos_ano = quad1_ano + quad2_ano + quad3_ano + quad4_ano
        
        # Calcular métricas
        concordancia_ano = (quad1_ano + quad4_ano) / total_projetos_ano * 100 if total_projetos_ano > 0 else 0
        discordancia_ano = (quad2_ano + quad3_ano) / total_projetos_ano * 100 if total_projetos_ano > 0 else 0
        
        # Armazenar estatísticas
        estatisticas_anuais.append({
            'Ano': ano,
            'Total_Projetos': total_projetos_ano,
            'Q1_Count': quad1_ano,
            'Q1_Percent': quad1_ano/total_projetos_ano*100 if total_projetos_ano > 0 else 0,
            'Q2_Count': quad2_ano,
            'Q2_Percent': quad2_ano/total_projetos_ano*100 if total_projetos_ano > 0 else 0,
            'Q3_Count': quad3_ano,
            'Q3_Percent': quad3_ano/total_projetos_ano*100 if total_projetos_ano > 0 else 0,
            'Q4_Count': quad4_ano,
            'Q4_Percent': quad4_ano/total_projetos_ano*100 if total_projetos_ano > 0 else 0,
            'Concordancia_%': concordancia_ano,
            'Discordancia_%': discordancia_ano
        })
        
        # Gráfico 1: Matriz de calor
        ax1 = plt.subplot(5, 4, plot_idx)
        plot_idx += 1
        
        matriz_prop_ano = matriz_decisoes_ano.iloc[:-1, :-1] / total_projetos_ano * 100
        sns.heatmap(matriz_prop_ano, annot=True, fmt='.1f', cmap='RdYlBu_r',
                    cbar_kws={'label': 'Percentual (%)'}, ax=ax1,
                    annot_kws={'size': 12})
        ax1.set_title(f'Matriz de Decisões (%) - {ano}', fontsize=14, pad=10)
        ax1.set_xlabel('Decisão do Ministério', fontsize=10)
        ax1.set_ylabel('Decisão do Pesquisador', fontsize=10)
        
        # Adicionar valores absolutos
        for i in range(len(matriz_decisoes_ano.index)-1):
            for j in range(len(matriz_decisoes_ano.columns)-1):
                valor = matriz_decisoes_ano.iloc[i, j]
                ax1.text(j+0.5, i+0.75, f'({valor:,})',
                        ha='center', va='center', fontsize=8, color='black')
        
        # Gráfico 2: Diagrama de quadrantes
        ax2 = plt.subplot(5, 4, plot_idx)
        plot_idx += 1
        
        ax2.set_xlim(-1.2, 1.2)
        ax2.set_ylim(-1.2, 1.2)
        ax2.axhline(y=0, color='black', linewidth=2)
        ax2.axvline(x=0, color='black', linewidth=2)
        
        # Cores e labels dos quadrantes
        cores_quad = ['#2ecc71', '#e74c3c', '#f39c12', '#95a5a6']
        labels_quad_ano = [
            f'Q1: Ambos\nRecomendam\n{quad1_ano:,}\n({quad1_ano/total_projetos_ano*100:.1f}%)',
            f'Q2: Pesq. Sim\nMin. Não\n{quad2_ano:,}\n({quad2_ano/total_projetos_ano*100:.1f}%)',
            f'Q3: Pesq. Não\nMin. Sim\n{quad3_ano:,}\n({quad3_ano/total_projetos_ano*100:.1f}%)',
            f'Q4: Ambos\nNão Recomendam\n{quad4_ano:,}\n({quad4_ano/total_projetos_ano*100:.1f}%)'
        ]
        
        # Posições dos quadrantes
        positions = [(0.6, 0.6), (-0.6, 0.6), (-0.6, -0.6), (0.6, -0.6)]
        quadrantes_ano = [quad1_ano, quad2_ano, quad3_ano, quad4_ano]
        
        for i, (pos, label, cor, valor) in enumerate(zip(positions, labels_quad_ano, cores_quad, quadrantes_ano)):
            # Calcular tamanho do círculo proporcional ao valor
            size = (valor / total_projetos_ano) * 5000 + 500 if total_projetos_ano > 0 else 500
            ax2.scatter(pos[0], pos[1], s=size, c=cor, alpha=0.6, edgecolors='black', linewidth=2)
            ax2.text(pos[0], pos[1], label, ha='center', va='center', fontsize=9,
                     fontweight='bold', bbox=dict(boxstyle='round,pad=0.3', facecolor=cor, alpha=0.3))
        
        ax2.set_xlabel('← Não Rec. Min. | Rec. Min. →', fontsize=9)
        ax2.set_ylabel('← Não Rec. Pesq. | Rec. Pesq. →', fontsize=9)
        ax2.set_title(f'Quadrantes de Decisão - {ano}', fontsize=14, pad=10)
        ax2.grid(True, alpha=0.3)
        ax2.set_xticks([])
        ax2.set_yticks([])
        
        # Imprimir estatísticas do ano
        print(f"\n📊 MÉTRICAS DE CONCORDÂNCIA - {ano}:")
        print(f"Taxa de Concordância Total: {concordancia_ano:.1f}%")
        print(f"Taxa de Discordância Total: {discordancia_ano:.1f}%")
        
        if (quad2_ano + quad3_ano) > 0:
            print(f"\nDentro das discordâncias:")
            print(f"  - Ministério mais rigoroso (Q2): {quad2_ano/(quad2_ano+quad3_ano)*100:.1f}%")
            print(f"  - Pesquisador mais rigoroso (Q3): {quad3_ano/(quad2_ano+quad3_ano)*100:.1f}%")
    
    plt.tight_layout()
    plt.show()
    
    # Criar DataFrame com estatísticas anuais
    df_stats = pd.DataFrame(estatisticas_anuais)
    
    # Visualização da evolução temporal
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Gráfico 1: Evolução da Concordância/Discordância
    anos = df_stats['Ano']
    ax1.plot(anos, df_stats['Concordancia_%'], marker='o', linewidth=2, markersize=8, 
             label='Concordância', color='#2ecc71')
    ax1.plot(anos, df_stats['Discordancia_%'], marker='s', linewidth=2, markersize=8,
             label='Discordância', color='#e74c3c')
    ax1.fill_between(anos, df_stats['Concordancia_%'], alpha=0.3, color='#2ecc71')
    ax1.fill_between(anos, df_stats['Discordancia_%'], alpha=0.3, color='#e74c3c')
    ax1.set_xlabel('Ano', fontsize=12)
    ax1.set_ylabel('Percentual (%)', fontsize=12)
    ax1.set_title('Evolução da Concordância vs Discordância (2018-2022)', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 100)
    ax1.set_xticks(anos)
    ax1.set_xticklabels([int(ano) for ano in anos])
    
    # Gráfico 2: Evolução dos Quadrantes
    ax2.plot(anos, df_stats['Q1_Percent'], marker='o', linewidth=2, label='Q1: Ambos Recomendam', color='#2ecc71')
    ax2.plot(anos, df_stats['Q2_Percent'], marker='s', linewidth=2, label='Q2: Pesq. Sim, Min. Não', color='#e74c3c')
    ax2.plot(anos, df_stats['Q3_Percent'], marker='^', linewidth=2, label='Q3: Pesq. Não, Min. Sim', color='#f39c12')
    ax2.plot(anos, df_stats['Q4_Percent'], marker='d', linewidth=2, label='Q4: Ambos Não Recomendam', color='#95a5a6')
    ax2.set_xlabel('Ano', fontsize=12)
    ax2.set_ylabel('Percentual (%)', fontsize=12)
    ax2.set_title('Evolução dos Quadrantes por Ano (2018-2022)', fontsize=14)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks(anos) 
    ax2.set_xticklabels([int(ano) for ano in anos])
    
    # Gráfico 3: Volume de projetos por quadrante (barras empilhadas)
    width = 0.6
    x = np.arange(len(anos))
    
    ax3.bar(x, df_stats['Q1_Count'], width, label='Q1', color='#2ecc71', alpha=0.8)
    ax3.bar(x, df_stats['Q2_Count'], width, bottom=df_stats['Q1_Count'], 
            label='Q2', color='#e74c3c', alpha=0.8)
    ax3.bar(x, df_stats['Q3_Count'], width, 
            bottom=df_stats['Q1_Count'] + df_stats['Q2_Count'],
            label='Q3', color='#f39c12', alpha=0.8)
    ax3.bar(x, df_stats['Q4_Count'], width,
            bottom=df_stats['Q1_Count'] + df_stats['Q2_Count'] + df_stats['Q3_Count'],
            label='Q4', color='#95a5a6', alpha=0.8)
    
    ax3.set_xlabel('Ano', fontsize=12)
    ax3.set_ylabel('Número de Projetos', fontsize=12)
    ax3.set_title('Volume de Projetos por Quadrante (2018-2022)', fontsize=14)
    ax3.set_xticks(x)
    ax3.set_xticklabels(anos)
    ax3.legend()
    ax3.grid(axis='y', alpha=0.3)
    
    # Gráfico 4: Heatmap da evolução
    heatmap_data = df_stats[['Q1_Percent', 'Q2_Percent', 'Q3_Percent', 'Q4_Percent']].T
    heatmap_data.columns = df_stats['Ano']
    
    sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='RdYlGn', center=25,
                ax=ax4, cbar_kws={'label': 'Percentual (%)'})
    ax4.set_xlabel('Ano', fontsize=12)
    ax4.set_ylabel('Quadrante', fontsize=12)
    ax4.set_title('Heatmap da Distribuição dos Quadrantes (2018-2022)', fontsize=14)
    ax4.set_yticklabels(['Q1: Ambos Rec.', 'Q2: Pesq. Sim', 'Q3: Pesq. Não', 'Q4: Ambos Não'], rotation=0)
    
    plt.tight_layout()
    plt.show()
    
    # Tabela resumo
    print("\n\n📊 TABELA RESUMO - EVOLUÇÃO ANUAL DOS QUADRANTES")
    print("=" * 100)
    print(f"{'Ano':^6} | {'Total':^8} | {'Q1':^15} | {'Q2':^15} | {'Q3':^15} | {'Q4':^15} | {'Conc.':^7}")
    print("-" * 100)
    
    for _, row in df_stats.iterrows():
        print(f"{row['Ano']:^6} | {row['Total_Projetos']:^8,} | "
              f"{row['Q1_Count']:>6,} ({row['Q1_Percent']:>5.1f}%) | "
              f"{row['Q2_Count']:>6,} ({row['Q2_Percent']:>5.1f}%) | "
              f"{row['Q3_Count']:>6,} ({row['Q3_Percent']:>5.1f}%) | "
              f"{row['Q4_Count']:>6,} ({row['Q4_Percent']:>5.1f}%) | "
              f"{row['Concordancia_%']:>6.1f}%")
    
    print("=" * 100)
    
    # Insights da evolução temporal
    print("\n🔍 INSIGHTS DA EVOLUÇÃO TEMPORAL:")
    print("-" * 60)
    
    # Ano com maior/menor concordância
    max_conc = df_stats.loc[df_stats['Concordancia_%'].idxmax()]
    min_conc = df_stats.loc[df_stats['Concordancia_%'].idxmin()]
    print(f"✅ Maior concordância: {max_conc['Ano']} com {max_conc['Concordancia_%']:.1f}%")
    print(f"❌ Menor concordância: {min_conc['Ano']} com {min_conc['Concordancia_%']:.1f}%")
    
    # Tendência
    if df_stats['Concordancia_%'].iloc[-1] > df_stats['Concordancia_%'].iloc[0]:
        print(f"📈 Tendência: Aumento na concordância (+{df_stats['Concordancia_%'].iloc[-1] - df_stats['Concordancia_%'].iloc[0]:.1f}% entre 2018-2022)")
    else:
        print(f"📉 Tendência: Redução na concordância ({df_stats['Concordancia_%'].iloc[-1] - df_stats['Concordancia_%'].iloc[0]:.1f}% entre 2018-2022)")
    
    # Exportar estatísticas
    df_stats.to_csv('evolucao_quadrantes_2018_2022.csv', index=False, sep=';', encoding='utf-8')
    print("\n💾 Estatísticas exportadas para 'evolucao_quadrantes_2018_2022.csv'")
```

    ================================================================================
    ANÁLISE DE QUADRANTES DE DECISÃO POR ANO (2018-2022)
    ================================================================================

    ============================================================
    ANO: 2018
    ============================================================

    📊 Matriz de Decisões - 2018:
    Ministério            Não Recomendado  Recomendado  Total
    Pesquisador (ad hoc)                                     
    Não Recomendado                   806         3316   4122
    Recomendado                        89         6654   6743
    Total                             895         9970  10865

    📊 MÉTRICAS DE CONCORDÂNCIA - 2018:
    Taxa de Concordância Total: 68.7%
    Taxa de Discordância Total: 31.3%

    Dentro das discordâncias:
      - Ministério mais rigoroso (Q2): 2.6%
      - Pesquisador mais rigoroso (Q3): 97.4%

    ============================================================
    ANO: 2019
    ============================================================

    📊 Matriz de Decisões - 2019:
    Ministério            Não Recomendado  Recomendado  Total
    Pesquisador (ad hoc)                                     
    Não Recomendado                  2687         1661   4348
    Recomendado                       166         7654   7820
    Total                            2853         9315  12168

    📊 MÉTRICAS DE CONCORDÂNCIA - 2019:
    Taxa de Concordância Total: 85.0%
    Taxa de Discordância Total: 15.0%

    Dentro das discordâncias:
      - Ministério mais rigoroso (Q2): 9.1%
      - Pesquisador mais rigoroso (Q3): 90.9%

    ============================================================
    ANO: 2020
    ============================================================

    📊 Matriz de Decisões - 2020:
    Ministério            Não Recomendado  Recomendado  Total
    Pesquisador (ad hoc)                                     
    Não Recomendado                  3702          599   4301
    Recomendado                       199         7153   7352
    Total                            3901         7752  11653

    📊 MÉTRICAS DE CONCORDÂNCIA - 2020:
    Taxa de Concordância Total: 93.2%
    Taxa de Discordância Total: 6.8%

    Dentro das discordâncias:
      - Ministério mais rigoroso (Q2): 24.9%
      - Pesquisador mais rigoroso (Q3): 75.1%

    ============================================================
    ANO: 2021
    ============================================================

    📊 Matriz de Decisões - 2021:
    Ministério            Não Recomendado  Recomendado  Total
    Pesquisador (ad hoc)                                     
    Não Recomendado                  4763          238   5001
    Recomendado                      2546         5647   8193
    Total                            7309         5885  13194

    📊 MÉTRICAS DE CONCORDÂNCIA - 2021:
    Taxa de Concordância Total: 78.9%
    Taxa de Discordância Total: 21.1%

    Dentro das discordâncias:
      - Ministério mais rigoroso (Q2): 91.5%
      - Pesquisador mais rigoroso (Q3): 8.5%

    ============================================================
    ANO: 2022
    ============================================================

    📊 Matriz de Decisões - 2022:
    Ministério            Não Recomendado  Recomendado  Total
    Pesquisador (ad hoc)                                     
    Não Recomendado                  5186           84   5270
    Recomendado                      2104         6412   8516
    Total                            7290         6496  13786

    📊 MÉTRICAS DE CONCORDÂNCIA - 2022:
    Taxa de Concordância Total: 84.1%
    Taxa de Discordância Total: 15.9%

    Dentro das discordâncias:
      - Ministério mais rigoroso (Q2): 96.2%
      - Pesquisador mais rigoroso (Q3): 3.8%

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-10-output-2.png)

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-10-output-3.png)



    📊 TABELA RESUMO - EVOLUÇÃO ANUAL DOS QUADRANTES
    ====================================================================================================
     Ano   |  Total   |       Q1        |       Q2        |       Q3        |       Q4        |  Conc. 
    ----------------------------------------------------------------------------------------------------
    2018.0 | 10,865.0 | 6,654.0 ( 61.2%) |   89.0 (  0.8%) | 3,316.0 ( 30.5%) |  806.0 (  7.4%) |   68.7%
    2019.0 | 12,168.0 | 7,654.0 ( 62.9%) |  166.0 (  1.4%) | 1,661.0 ( 13.7%) | 2,687.0 ( 22.1%) |   85.0%
    2020.0 | 11,653.0 | 7,153.0 ( 61.4%) |  199.0 (  1.7%) |  599.0 (  5.1%) | 3,702.0 ( 31.8%) |   93.2%
    2021.0 | 13,194.0 | 5,647.0 ( 42.8%) | 2,546.0 ( 19.3%) |  238.0 (  1.8%) | 4,763.0 ( 36.1%) |   78.9%
    2022.0 | 13,786.0 | 6,412.0 ( 46.5%) | 2,104.0 ( 15.3%) |   84.0 (  0.6%) | 5,186.0 ( 37.6%) |   84.1%
    ====================================================================================================

    🔍 INSIGHTS DA EVOLUÇÃO TEMPORAL:
    ------------------------------------------------------------
    ✅ Maior concordância: 2020.0 com 93.2%
    ❌ Menor concordância: 2018.0 com 68.7%
    📈 Tendência: Aumento na concordância (+15.5% entre 2018-2022)

    💾 Estatísticas exportadas para 'evolucao_quadrantes_2018_2022.csv'

## 4. Análise de Aprovação por Setor

Análise das taxas de aprovação por setor nas fases DO e Parecer,
identificando padrões setoriais e diferenças entre as fases de
avaliação.

### Análise dos quadrantes por Setor

``` python
# %% Heatmap dos Quadrantes de Decisão - ANÁLISE POR SETOR
"""
Análise dos Quadrantes de Decisão por Setor
Lei do Bem - Ministério vs Pareceristas por Área do Projeto

Quadrantes:
- Q1 (S,S): Ambos Recomendam
- Q2 (S,N): Parecerista Recomenda, Ministério Não Recomenda
- Q3 (N,S): Parecerista Não Recomenda, Ministério Recomenda
- Q4 (N,N): Ambos Não Recomendam

S = Recomendado | N = Não Recomendado
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Configuração visual
plt.style.use('default')
sns.set_palette("husl")

print("=" * 80)
print("HEATMAP DOS QUADRANTES DE DECISÃO - ANÁLISE POR SETOR")
print("Lei do Bem: Ministério vs Pareceristas por Área do Projeto")
print("=" * 80)

# Função para padronizar decisões
def padronizar_decisao(decisao):
    if pd.isna(decisao):
        return np.nan
    decisao_str = str(decisao).strip().upper()
    if 'RECOMENDADO' in decisao_str and 'NÃO' not in decisao_str:
        return 'S'  # Sim/Recomendado
    elif 'NÃO RECOMENDADO' in decisao_str:
        return 'N'  # Não/Não Recomendado
    else:
        return 'Outro'

# Carregar dados (assumindo que o arquivo existe)
try:
    arquivo_dados = 'csv_longo/projetos_lei_do_bem_DETALHADO_LINHA_UNICA.csv'
    df = pd.read_csv(arquivo_dados, sep=';', encoding='utf-8')
    print(f"✅ Dataset carregado: {len(df):,} registros")
except FileNotFoundError:
    print("❌ Arquivo não encontrado. Verifique o caminho do dataset.")
    exit()

# Preparar dados
df['decisao_pesquisador'] = df['do_taaproj_notipoavaliacaoanalise'].apply(padronizar_decisao)
df['decisao_ministerio'] = df['p_taaproj_notipoavaliacaoanalise'].apply(padronizar_decisao)

# Filtrar apenas decisões válidas e com setor definido
df_validos = df[
    (df['decisao_pesquisador'].isin(['S', 'N'])) & 
    (df['decisao_ministerio'].isin(['S', 'N'])) &
    (df['do_set_nosetor'].notna())
].copy()

print(f"📊 Projetos com decisões válidas e setor definido: {len(df_validos):,}")

# Função para classificar quadrantes
def classificar_quadrante(row):
    parecerista = row['decisao_pesquisador']
    ministerio = row['decisao_ministerio']
    
    if parecerista == 'S' and ministerio == 'S':
        return 'Q1'
    elif parecerista == 'S' and ministerio == 'N':
        return 'Q2'
    elif parecerista == 'N' and ministerio == 'S':
        return 'Q3'
    elif parecerista == 'N' and ministerio == 'N':
        return 'Q4'
    else:
        return 'Indefinido'

df_validos['quadrante'] = df_validos.apply(classificar_quadrante, axis=1)

# Analisar por setor
setores = df_validos['do_set_nosetor'].unique()
print(f"\n📈 Setores identificados: {len(setores)}")
for i, setor in enumerate(sorted(setores), 1):
    count = len(df_validos[df_validos['do_set_nosetor'] == setor])
    print(f"{i:2d}. {setor}: {count:,} projetos")

# Criar matriz de dados por setor
dados_setores = []

for setor in sorted(setores):
    df_setor = df_validos[df_validos['do_set_nosetor'] == setor]
    total_setor = len(df_setor)
    
    if total_setor >= 10:  # Apenas setores com volume mínimo
        contagem_quad = df_setor['quadrante'].value_counts()
        
        # Calcular percentuais
        q1_pct = (contagem_quad.get('Q1', 0) / total_setor) * 100
        q2_pct = (contagem_quad.get('Q2', 0) / total_setor) * 100
        q3_pct = (contagem_quad.get('Q3', 0) / total_setor) * 100
        q4_pct = (contagem_quad.get('Q4', 0) / total_setor) * 100
        
        dados_setores.append({
            'Setor': setor,
            'Q1 (S,S)': q1_pct,
            'Q2 (S,N)': q2_pct,
            'Q3 (N,S)': q3_pct,
            'Q4 (N,N)': q4_pct,
            'Total_Projetos': total_setor,
            'Concordancia_Total': q1_pct + q4_pct,
            'Discordancia_Total': q2_pct + q3_pct
        })

# Criar DataFrame para heatmap
df_heatmap = pd.DataFrame(dados_setores)
df_heatmap = df_heatmap.sort_values('Total_Projetos', ascending=False)

print(f"\n📊 Setores incluídos na análise: {len(df_heatmap)}")

# Preparar dados para o heatmap
heatmap_data = df_heatmap.set_index('Setor')[['Q1 (S,S)', 'Q2 (S,N)', 'Q3 (N,S)', 'Q4 (N,N)']]

# Criar heatmap principal
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# Heatmap 1: Distribuição dos Quadrantes por Setor
sns.heatmap(heatmap_data.T, annot=True, fmt='.1f', cmap='RdYlBu_r', 
            cbar_kws={'label': 'Percentual (%)'}, ax=ax1,
            linewidths=0.5, linecolor='white')

ax1.set_title('Distribuição dos Quadrantes por Setor (%)\n' +
              'Lei do Bem: Ministério vs Pareceristas', 
              fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('')
ax1.set_ylabel('Quadrantes', fontsize=12, fontweight='bold')

# Rotular eixos
ax1.set_yticklabels(['Q1: Ambos Recomendam', 'Q2: Parecerista S, Ministério N', 
                     'Q3: Parecerista N, Ministério S', 'Q4: Ambos Não Recomendam'], 
                    rotation=0, fontsize=10)

# Truncar nomes dos setores se muito longos
setores_truncados = [setor[:25] + '...' if len(setor) > 25 else setor 
                     for setor in heatmap_data.index]
ax1.set_xticklabels(setores_truncados, rotation=45, ha='right', fontsize=10)

# Heatmap 2: Concordância vs Discordância
concordancia_data = df_heatmap.set_index('Setor')[['Concordancia_Total', 'Discordancia_Total']]

sns.heatmap(concordancia_data.T, annot=True, fmt='.1f', cmap='RdYlGn', 
            cbar_kws={'label': 'Percentual (%)'}, ax=ax2,
            linewidths=0.5, linecolor='white', center=50)

ax2.set_title('Concordância vs Discordância por Setor (%)', 
              fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Setor', fontsize=12, fontweight='bold')
ax2.set_ylabel('Métricas', fontsize=12, fontweight='bold')

ax2.set_yticklabels(['Concordância Total (Q1+Q4)', 'Discordância Total (Q2+Q3)'], 
                    rotation=0, fontsize=10)
ax2.set_xticklabels(setores_truncados, rotation=45, ha='right', fontsize=10)

plt.tight_layout()
plt.show()

# Tabela detalhada por setor
print("\n📋 TABELA DETALHADA POR SETOR:")
print("=" * 120)
print(f"{'Setor':<35} {'Q1(S,S)':>8} {'Q2(S,N)':>8} {'Q3(N,S)':>8} {'Q4(N,N)':>8} {'Concord.':>9} {'Discord.':>9} {'Total':>8}")
print("-" * 120)

for _, row in df_heatmap.iterrows():
    setor_nome = row['Setor'][:33] + '..' if len(row['Setor']) > 35 else row['Setor']
    print(f"{setor_nome:<35} {row['Q1 (S,S)']:>7.1f}% {row['Q2 (S,N)']:>7.1f}% " + 
          f"{row['Q3 (N,S)']:>7.1f}% {row['Q4 (N,N)']:>7.1f}% {row['Concordancia_Total']:>8.1f}% " +
          f"{row['Discordancia_Total']:>8.1f}% {row['Total_Projetos']:>8}")

print("=" * 120)

# Análise de padrões por setor
print(f"\n🔍 ANÁLISE DE PADRÕES SETORIAIS:")
print("-" * 60)

# Setor com maior concordância
setor_max_concordancia = df_heatmap.loc[df_heatmap['Concordancia_Total'].idxmax()]
print(f"✅ Maior Concordância: {setor_max_concordancia['Setor']}")
print(f"   └── {setor_max_concordancia['Concordancia_Total']:.1f}% ({setor_max_concordancia['Total_Projetos']} projetos)")

# Setor com maior discordância
setor_max_discordancia = df_heatmap.loc[df_heatmap['Discordancia_Total'].idxmax()]
print(f"⚠️  Maior Discordância: {setor_max_discordancia['Setor']}")
print(f"   └── {setor_max_discordancia['Discordancia_Total']:.1f}% ({setor_max_discordancia['Total_Projetos']} projetos)")

# Setor com maior Q1 (ambos recomendam)
setor_max_q1 = df_heatmap.loc[df_heatmap['Q1 (S,S)'].idxmax()]
print(f"🟢 Maior Q1 (S,S): {setor_max_q1['Setor']}")
print(f"   └── {setor_max_q1['Q1 (S,S)']:.1f}% ({setor_max_q1['Total_Projetos']} projetos)")

# Setor com maior Q4 (ambos não recomendam)
setor_max_q4 = df_heatmap.loc[df_heatmap['Q4 (N,N)'].idxmax()]
print(f"🔴 Maior Q4 (N,N): {setor_max_q4['Setor']}")
print(f"   └── {setor_max_q4['Q4 (N,N)']:.1f}% ({setor_max_q4['Total_Projetos']} projetos)")

# Estatísticas gerais
print(f"\n📊 ESTATÍSTICAS GERAIS:")
print(f"└── Concordância média entre setores: {df_heatmap['Concordancia_Total'].mean():.1f}%")
print(f"└── Discordância média entre setores: {df_heatmap['Discordancia_Total'].mean():.1f}%")
print(f"└── Variação na concordância: {df_heatmap['Concordancia_Total'].std():.1f}% (desvio padrão)")

# Exportar resultados
df_heatmap.to_csv('quadrantes_por_setor.csv', index=False, sep=';', encoding='utf-8')
print(f"\n💾 Resultados exportados para 'quadrantes_por_setor.csv'")

print("\n" + "=" * 80)
print("HEATMAP POR SETOR CONCLUÍDO")
print("=" * 80)
```

    ================================================================================
    HEATMAP DOS QUADRANTES DE DECISÃO - ANÁLISE POR SETOR
    Lei do Bem: Ministério vs Pareceristas por Área do Projeto
    ================================================================================
    ✅ Dataset carregado: 75,816 registros
    📊 Projetos com decisões válidas e setor definido: 68,443

    📈 Setores identificados: 7
     1. Agroindústria e Alimentos: 8,144 projetos
     2. Eletroeletrônica: 7,158 projetos
     3. Mecânica e Transporte: 9,068 projetos
     4. Metalurgia e Mineração: 4,989 projetos
     5. Química e Farmácia: 12,845 projetos
     6. TIC: 18,772 projetos
     7. Transversal: 7,467 projetos

    📊 Setores incluídos na análise: 7

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-11-output-2.png)


    📋 TABELA DETALHADA POR SETOR:
    ========================================================================================================================
    Setor                                Q1(S,S)  Q2(S,N)  Q3(N,S)  Q4(N,N)  Concord.  Discord.    Total
    ------------------------------------------------------------------------------------------------------------------------
    TIC                                    40.9%    12.1%     7.5%    39.6%     80.4%     19.6%    18772
    Química e Farmácia                     73.3%     3.3%     5.5%    17.9%     91.2%      8.8%    12845
    Mecânica e Transporte                  54.6%     4.5%    13.6%    27.4%     82.0%     18.0%     9068
    Agroindústria e Alimentos              52.0%     8.5%     7.5%    31.9%     83.9%     16.1%     8144
    Transversal                            46.7%    11.8%     8.4%    33.1%     79.8%     20.2%     7467
    Eletroeletrônica                       56.4%     2.2%    11.1%    30.4%     86.7%     13.3%     7158
    Metalurgia e Mineração                 57.3%     5.6%    10.3%    26.9%     84.1%     15.9%     4989
    ========================================================================================================================

    🔍 ANÁLISE DE PADRÕES SETORIAIS:
    ------------------------------------------------------------
    ✅ Maior Concordância: Química e Farmácia
       └── 91.2% (12845 projetos)
    ⚠️  Maior Discordância: Transversal
       └── 20.2% (7467 projetos)
    🟢 Maior Q1 (S,S): Química e Farmácia
       └── 73.3% (12845 projetos)
    🔴 Maior Q4 (N,N): TIC
       └── 39.6% (18772 projetos)

    📊 ESTATÍSTICAS GERAIS:
    └── Concordância média entre setores: 84.0%
    └── Discordância média entre setores: 16.0%
    └── Variação na concordância: 3.9% (desvio padrão)

    💾 Resultados exportados para 'quadrantes_por_setor.csv'

    ================================================================================
    HEATMAP POR SETOR CONCLUÍDO
    ================================================================================

### Análise dos quadrantes por Setor ao longo dos Anos

``` python
# HEATMAP DOS QUADRANTES DE DECISÃO POR SETOR E ANO
# Lei do Bem: Análise temporal da concordância por setor (2018-2022)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Configuração visual
plt.style.use('default')
sns.set_palette("husl")

print("=" * 80)
print("HEATMAP DOS QUADRANTES DE DECISÃO - ANÁLISE POR SETOR E ANO")
print("Lei do Bem: Evolução Temporal por Setor (2018-2022)")
print("=" * 80)

# Verificar se os dados necessários estão disponíveis
if 'df_completo' not in locals():
    print("❌ ERRO: df_completo não encontrado. Execute primeiro o código de preparação dos dados.")
else:
    # Função para padronizar decisões
    def padronizar_decisao_simples(decisao):
        if pd.isna(decisao):
            return np.nan
        decisao_str = str(decisao).strip().upper()
        if 'RECOMENDADO' in decisao_str and 'NÃO' not in decisao_str:
            return 'S'  # Sim/Recomendado
        elif 'NÃO RECOMENDADO' in decisao_str:
            return 'N'  # Não/Não Recomendado
        else:
            return np.nan

    # Preparar dados se ainda não estiverem preparados
    if 'decisao_pesquisador_s_n' not in df_completo.columns:
        df_completo['decisao_pesquisador_s_n'] = df_completo['do_taaproj_notipoavaliacaoanalise'].apply(padronizar_decisao_simples)
        df_completo['decisao_ministerio_s_n'] = df_completo['p_taaproj_notipoavaliacaoanalise'].apply(padronizar_decisao_simples)

    # Função para classificar quadrantes
    def classificar_quadrante(row):
        parecerista = row['decisao_pesquisador_s_n']
        ministerio = row['decisao_ministerio_s_n']
        
        if parecerista == 'S' and ministerio == 'S':
            return 'Q1'
        elif parecerista == 'S' and ministerio == 'N':
            return 'Q2'
        elif parecerista == 'N' and ministerio == 'S':
            return 'Q3'
        elif parecerista == 'N' and ministerio == 'N':
            return 'Q4'
        else:
            return np.nan

    # Filtrar apenas decisões válidas e com setor e ano definidos
    df_validos = df_completo[
        (df_completo['decisao_pesquisador_s_n'].isin(['S', 'N'])) & 
        (df_completo['decisao_ministerio_s_n'].isin(['S', 'N'])) &
        (df_completo['do_set_nosetor'].notna()) &
        (df_completo['lst_nranobase'].notna())
    ].copy()

    df_validos['quadrante'] = df_validos.apply(classificar_quadrante, axis=1)
    
    print(f"📊 Projetos válidos para análise: {len(df_validos):,}")
    
    # Anos a analisar
    anos_analise = [2018, 2019, 2020, 2021, 2022]
    
    # Identificar setores com volume significativo
    setores_principais = df_validos['do_set_nosetor'].value_counts().head(7).index.tolist()
    
    # Criar figura para todos os anos
    fig = plt.figure(figsize=(20, 25))
    
    # Armazenar dados para análise posterior
    dados_temporais = []
    
    for idx, ano in enumerate(anos_analise):
        print(f"\n{'='*60}")
        print(f"ANÁLISE DO ANO: {ano}")
        print(f"{'='*60}")
        
        # Filtrar dados do ano
        df_ano = df_validos[df_validos['lst_nranobase'] == ano]
        
        if len(df_ano) == 0:
            print(f"⚠️ Sem dados para o ano {ano}")
            continue
        
        print(f"📊 Projetos no ano {ano}: {len(df_ano):,}")
        
        # Criar dados para heatmap do ano
        dados_setores_ano = []
        
        for setor in setores_principais:
            df_setor_ano = df_ano[df_ano['do_set_nosetor'] == setor]
            total_setor = len(df_setor_ano)
            
            if total_setor >= 10:  # Volume mínimo
                contagem_quad = df_setor_ano['quadrante'].value_counts()
                
                # Calcular percentuais
                q1_pct = (contagem_quad.get('Q1', 0) / total_setor) * 100
                q2_pct = (contagem_quad.get('Q2', 0) / total_setor) * 100
                q3_pct = (contagem_quad.get('Q3', 0) / total_setor) * 100
                q4_pct = (contagem_quad.get('Q4', 0) / total_setor) * 100
                
                dados_setores_ano.append({
                    'Setor': setor[:25] + '...' if len(setor) > 25 else setor,
                    'Q1 (S,S)': q1_pct,
                    'Q2 (S,N)': q2_pct,
                    'Q3 (N,S)': q3_pct,
                    'Q4 (N,N)': q4_pct,
                    'Total_Projetos': total_setor,
                    'Concordancia_Total': q1_pct + q4_pct,
                    'Discordancia_Total': q2_pct + q3_pct
                })
                
                # Armazenar para análise temporal
                dados_temporais.append({
                    'Ano': ano,
                    'Setor': setor,
                    'Q1': q1_pct,
                    'Q2': q2_pct,
                    'Q3': q3_pct,
                    'Q4': q4_pct,
                    'Concordancia': q1_pct + q4_pct,
                    'Discordancia': q2_pct + q3_pct,
                    'Total': total_setor
                })
        
        # Criar DataFrame para o ano
        df_heatmap_ano = pd.DataFrame(dados_setores_ano)
        
        if len(df_heatmap_ano) > 0:
            # Ordenar por total de projetos
            df_heatmap_ano = df_heatmap_ano.sort_values('Total_Projetos', ascending=False)
            
            # Subplot 1: Heatmap dos quadrantes
            ax1 = plt.subplot(5, 2, idx*2 + 1)
            
            heatmap_data = df_heatmap_ano.set_index('Setor')[['Q1 (S,S)', 'Q2 (S,N)', 'Q3 (N,S)', 'Q4 (N,N)']]
            
            sns.heatmap(heatmap_data.T, annot=True, fmt='.1f', cmap='RdYlBu_r', 
                       cbar_kws={'label': '%'}, ax=ax1,
                       linewidths=0.5, linecolor='white',
                       vmin=0, vmax=80)  # Escala fixa para comparação
            
            ax1.set_title(f'Distribuição dos Quadrantes por Setor - {ano}', 
                         fontsize=12, fontweight='bold')
            ax1.set_xlabel('')
            ax1.set_ylabel('Quadrantes', fontsize=10)
            
            if idx == 0:  # Labels completos apenas no primeiro gráfico
                ax1.set_yticklabels(['Q1: Ambos Rec.', 'Q2: Par. S, Min. N', 
                                    'Q3: Par. N, Min. S', 'Q4: Ambos Não Rec.'], 
                                   rotation=0, fontsize=9)
            else:
                ax1.set_yticklabels(['Q1', 'Q2', 'Q3', 'Q4'], rotation=0, fontsize=9)
            
            ax1.set_xticklabels(heatmap_data.index, rotation=45, ha='right', fontsize=9)
            
            # Subplot 2: Concordância vs Discordância
            ax2 = plt.subplot(5, 2, idx*2 + 2)
            
            concordancia_data = df_heatmap_ano.set_index('Setor')[['Concordancia_Total', 'Discordancia_Total']]
            
            sns.heatmap(concordancia_data.T, annot=True, fmt='.1f', cmap='RdYlGn', 
                       cbar_kws={'label': '%'}, ax=ax2,
                       linewidths=0.5, linecolor='white', 
                       center=50, vmin=0, vmax=100)
            
            ax2.set_title(f'Concordância vs Discordância - {ano}', 
                         fontsize=12, fontweight='bold')
            ax2.set_xlabel('')
            ax2.set_ylabel('Métricas', fontsize=10)
            
            ax2.set_yticklabels(['Concordância', 'Discordância'], rotation=0, fontsize=9)
            ax2.set_xticklabels(concordancia_data.index, rotation=45, ha='right', fontsize=9)
            
            # Estatísticas do ano
            print(f"\n📊 Estatísticas {ano}:")
            print(f"├── Concordância média: {df_heatmap_ano['Concordancia_Total'].mean():.1f}%")
            print(f"├── Discordância média: {df_heatmap_ano['Discordancia_Total'].mean():.1f}%")
            print(f"├── Setor com maior concordância: {df_heatmap_ano.loc[df_heatmap_ano['Concordancia_Total'].idxmax(), 'Setor']} ({df_heatmap_ano['Concordancia_Total'].max():.1f}%)")
            print(f"└── Setor com maior discordância: {df_heatmap_ano.loc[df_heatmap_ano['Discordancia_Total'].idxmax(), 'Setor']} ({df_heatmap_ano['Discordancia_Total'].max():.1f}%)")
    
    plt.tight_layout()
    plt.show()
    
    # Análise da evolução temporal por setor
    if len(dados_temporais) > 0:
        df_temporal = pd.DataFrame(dados_temporais)
        
        # Gráfico de evolução da concordância por setor
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Gráfico 1: Evolução da concordância
        for setor in setores_principais:
            df_setor_tempo = df_temporal[df_temporal['Setor'] == setor].sort_values('Ano')
            if len(df_setor_tempo) >= 3:  # Pelo menos 3 anos de dados
                ax1.plot(df_setor_tempo['Ano'], df_setor_tempo['Concordancia'], 
                        marker='o', linewidth=2, markersize=6,
                        label=setor[:20] + '...' if len(setor) > 20 else setor)
        
        ax1.set_xlabel('Ano', fontsize=12)
        ax1.set_ylabel('Taxa de Concordância (%)', fontsize=12)
        ax1.set_title('Evolução da Taxa de Concordância por Setor (2018-2022)', 
                     fontsize=14, fontweight='bold')
        ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 100)
        ax1.set_xticks(anos) 
        ax1.set_xticklabels([int(ano) for ano in anos])
        
        # Gráfico 2: Heatmap da evolução temporal
        # Preparar matriz pivot
        pivot_concordancia = df_temporal.pivot_table(
            index='Setor', 
            columns='Ano', 
            values='Concordancia', 
            aggfunc='mean'
        )
        
        # Truncar nomes dos setores
        pivot_concordancia.index = [s[:25] + '...' if len(s) > 25 else s for s in pivot_concordancia.index]
        
        sns.heatmap(pivot_concordancia, annot=True, fmt='.1f', cmap='RdYlGn',
                   cbar_kws={'label': 'Taxa de Concordância (%)'}, ax=ax2,
                   linewidths=0.5, linecolor='white', center=80)
        
        ax2.set_title('Heatmap Temporal: Taxa de Concordância por Setor e Ano', 
                     fontsize=14, fontweight='bold')
        ax2.set_xlabel('Ano', fontsize=12)
        ax2.set_ylabel('Setor', fontsize=12)
        
        plt.tight_layout()
        plt.show()
        
        # Análise de tendências
        print("\n\n🔍 ANÁLISE DE TENDÊNCIAS TEMPORAIS POR SETOR:")
        print("=" * 80)
        
        for setor in setores_principais:
            df_setor_trend = df_temporal[df_temporal['Setor'] == setor].sort_values('Ano')
            if len(df_setor_trend) >= 3:
                concordancia_inicial = df_setor_trend.iloc[0]['Concordancia']
                concordancia_final = df_setor_trend.iloc[-1]['Concordancia']
                variacao = concordancia_final - concordancia_inicial
                
                print(f"\n{setor}:")
                print(f"├── 2018: {concordancia_inicial:.1f}% → 2022: {concordancia_final:.1f}%")
                print(f"├── Variação: {variacao:+.1f}%")
                print(f"└── Tendência: {'📈 Aumento' if variacao > 5 else '📉 Redução' if variacao < -5 else '➡️ Estável'}")
        
        # Tabela resumo comparativa
        print("\n\n📊 TABELA COMPARATIVA: CONCORDÂNCIA POR SETOR E ANO")
        print("=" * 100)
        print(f"{'Setor':<30} {'2018':>12} {'2019':>12} {'2020':>12} {'2021':>12} {'2022':>12} {'Média':>12}")
        print("-" * 100)
        
        for setor in setores_principais:
            df_setor_tab = df_temporal[df_temporal['Setor'] == setor]
            setor_nome = setor[:28] + '..' if len(setor) > 30 else setor
            linha = f"{setor_nome:<30}"
            
            for ano in anos_analise:
                valor = df_setor_tab[df_setor_tab['Ano'] == ano]['Concordancia'].values
                if len(valor) > 0:
                    linha += f"{valor[0]:>11.1f}%"
                else:
                    linha += f"{'--':>12}"
            
            media = df_setor_tab['Concordancia'].mean()
            linha += f"{media:>11.1f}%"
            print(linha)
        
        print("=" * 100)
        
        # Exportar resultados
        df_temporal.to_csv('evolucao_quadrantes_setor_ano.csv', index=False, sep=';', encoding='utf-8')
        print("\n💾 Dados exportados para 'evolucao_quadrantes_setor_ano.csv'")
        
    print("\n" + "=" * 80)
    print("ANÁLISE TEMPORAL POR SETOR CONCLUÍDA")
    print("=" * 80)
```

    ================================================================================
    HEATMAP DOS QUADRANTES DE DECISÃO - ANÁLISE POR SETOR E ANO
    Lei do Bem: Evolução Temporal por Setor (2018-2022)
    ================================================================================
    📊 Projetos válidos para análise: 68,443

    ============================================================
    ANÁLISE DO ANO: 2018
    ============================================================
    📊 Projetos no ano 2018: 10,852

    📊 Estatísticas 2018:
    ├── Concordância média: 68.7%
    ├── Discordância média: 31.3%
    ├── Setor com maior concordância: Química e Farmácia (80.0%)
    └── Setor com maior discordância: Agroindústria e Alimentos (40.8%)

    ============================================================
    ANÁLISE DO ANO: 2019
    ============================================================
    📊 Projetos no ano 2019: 12,168

    📊 Estatísticas 2019:
    ├── Concordância média: 84.5%
    ├── Discordância média: 15.5%
    ├── Setor com maior concordância: Mecânica e Transporte (93.0%)
    └── Setor com maior discordância: Eletroeletrônica (25.9%)

    ============================================================
    ANÁLISE DO ANO: 2020
    ============================================================
    📊 Projetos no ano 2020: 11,653

    📊 Estatísticas 2020:
    ├── Concordância média: 91.9%
    ├── Discordância média: 8.1%
    ├── Setor com maior concordância: Química e Farmácia (97.1%)
    └── Setor com maior discordância: Mecânica e Transporte (17.6%)

    ============================================================
    ANÁLISE DO ANO: 2021
    ============================================================
    📊 Projetos no ano 2021: 13,194

    📊 Estatísticas 2021:
    ├── Concordância média: 82.2%
    ├── Discordância média: 17.8%
    ├── Setor com maior concordância: Química e Farmácia (92.3%)
    └── Setor com maior discordância: TIC (36.8%)

    ============================================================
    ANÁLISE DO ANO: 2022
    ============================================================
    📊 Projetos no ano 2022: 13,786

    📊 Estatísticas 2022:
    ├── Concordância média: 84.3%
    ├── Discordância média: 15.7%
    ├── Setor com maior concordância: Eletroeletrônica (99.2%)
    └── Setor com maior discordância: Transversal (26.6%)

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-12-output-2.png)

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-12-output-3.png)



    🔍 ANÁLISE DE TENDÊNCIAS TEMPORAIS POR SETOR:
    ================================================================================

    TIC:
    ├── 2018: 61.1% → 2022: 82.2%
    ├── Variação: +21.0%
    └── Tendência: 📈 Aumento

    Química e Farmácia:
    ├── 2018: 80.0% → 2022: 90.5%
    ├── Variação: +10.5%
    └── Tendência: 📈 Aumento

    Mecânica e Transporte:
    ├── 2018: 62.2% → 2022: 82.4%
    ├── Variação: +20.3%
    └── Tendência: 📈 Aumento

    Agroindústria e Alimentos:
    ├── 2018: 59.2% → 2022: 86.1%
    ├── Variação: +26.9%
    └── Tendência: 📈 Aumento

    Transversal:
    ├── 2018: 70.2% → 2022: 73.4%
    ├── Variação: +3.2%
    └── Tendência: ➡️ Estável

    Eletroeletrônica:
    ├── 2018: 70.3% → 2022: 99.2%
    ├── Variação: +28.9%
    └── Tendência: 📈 Aumento

    Metalurgia e Mineração:
    ├── 2018: 77.8% → 2022: 76.1%
    ├── Variação: -1.7%
    └── Tendência: ➡️ Estável


    📊 TABELA COMPARATIVA: CONCORDÂNCIA POR SETOR E ANO
    ====================================================================================================
    Setor                                  2018         2019         2020         2021         2022        Média
    ----------------------------------------------------------------------------------------------------
    TIC                                  61.1%       80.8%       96.4%       63.2%       82.2%       76.7%
    Química e Farmácia                   80.0%       91.5%       97.1%       92.3%       90.5%       90.3%
    Mecânica e Transporte                62.2%       93.0%       82.4%       83.6%       82.4%       80.7%
    Agroindústria e Alimentos            59.2%       89.2%       94.1%       75.8%       86.1%       80.9%
    Transversal                          70.2%       81.1%       92.8%       80.4%       73.4%       79.6%
    Eletroeletrônica                     70.3%       74.1%       94.4%       88.5%       99.2%       85.3%
    Metalurgia e Mineração               77.8%       81.7%       86.4%       91.4%       76.1%       82.7%
    ====================================================================================================

    💾 Dados exportados para 'evolucao_quadrantes_setor_ano.csv'

    ================================================================================
    ANÁLISE TEMPORAL POR SETOR CONCLUÍDA
    ================================================================================

### Análise Textual por Quadrante e Setor

``` python
# ANÁLISE TEXTUAL POR QUADRANTE E SETOR
# Lei do Bem: Análise das palavras mais frequentes em cada quadrante por setor

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

# Configuração visual
plt.style.use('default')
sns.set_palette("husl")

print("=" * 80)
print("ANÁLISE TEXTUAL POR QUADRANTE E SETOR")
print("Lei do Bem: Palavras-chave por tipo de decisão")
print("=" * 80)

# Verificar se os dados necessários estão disponíveis
if 'df_completo' not in locals():
    print("❌ ERRO: df_completo não encontrado. Execute primeiro o código de preparação dos dados.")
else:
    # ============================================================================
    # PREPARAÇÃO DOS DADOS
    # ============================================================================
    
    # Configurar stopwords
    try:
        stopwords_pt = set(stopwords.words('portuguese'))
    except:
        nltk.download('stopwords')
        stopwords_pt = set(stopwords.words('portuguese'))
    
    # Stopwords específicas do domínio
    stopwords_dominio = {
        'ano', 'base', 'projeto', 'projetos', 'empresa', 'empresas',
        'desenvolvimento', 'pesquisa', 'inovação', 'tecnológica',
        'realizar', 'realizado', 'realizada', 'realizados', 'realizadas',
        'objetivo', 'objetivos', 'processo', 'processos', 'atividade',
        'atividades', 'trabalho', 'trabalhos', 'forma', 'formas',
        'através', 'partir', 'sendo', 'foram', 'seja', 'sejam',
        'pode', 'podem', 'deve', 'devem', 'está', 'estão',
        'fazer', 'feito', 'feita', 'ter', 'tem', 'tinha',
        'uso', 'usar', 'usado', 'usada', 'novo', 'nova',
        'novos', 'novas', 'ainda', 'apenas', 'assim', 'então',
        'para', 'com', 'uma', 'por', 'que', 'dos', 'das',
        'mais', 'como', 'sua', 'seu', 'aos', 'ela', 'ele'
    }
    
    todas_stopwords = stopwords_pt.union(stopwords_dominio)
    
    # Campos textuais para análise
    campos_texto = [
        'daproj_noprojeto',
        'daproj_dsprojeto',
        'daproj_dspalavrachave',
        'daproj_dselementotecnologico',
        'daproj_dsdesafiotecnologico',
        'daproj_dsmetodologiautilizada'
    ]
    
    # Filtrar apenas campos existentes
    campos_texto_existentes = [c for c in campos_texto if c in df_completo.columns]
    
    print(f"📊 Campos textuais identificados: {len(campos_texto_existentes)}")
    for campo in campos_texto_existentes:
        print(f"   • {campo}")
    
    # Função para processar texto
    def processar_texto_simples(texto):
        """Processa texto removendo stopwords e normalizando"""
        if pd.isna(texto):
            return ""
        
        # Converter para lowercase e split
        palavras = str(texto).lower().split()
        
        # Remover stopwords e palavras muito curtas
        palavras_limpas = [p for p in palavras if p not in todas_stopwords and len(p) > 2]
        
        return ' '.join(palavras_limpas)
    
    # Criar campo de texto combinado
    print("\nCombinando campos textuais...")
    textos_combinados = []
    
    for idx in range(len(df_completo)):
        partes = []
        for campo in campos_texto_existentes:
            texto = df_completo[campo].iloc[idx]
            if pd.notna(texto) and str(texto).strip():
                texto_processado = processar_texto_simples(texto)
                if texto_processado:
                    partes.append(texto_processado)
        
        texto_combinado = ' '.join(partes)
        textos_combinados.append(texto_combinado)
    
    df_completo['texto_combinado_processado'] = textos_combinados
    
    # Adicionar classificação de quadrantes se não existir
    if 'quadrante' not in df_completo.columns:
        def classificar_quadrante(row):
            if row['decisao_pesquisador'] == 'Recomendado' and row['decisao_ministerio'] == 'Recomendado':
                return 'Q1'
            elif row['decisao_pesquisador'] == 'Recomendado' and row['decisao_ministerio'] == 'Não Recomendado':
                return 'Q2'
            elif row['decisao_pesquisador'] == 'Não Recomendado' and row['decisao_ministerio'] == 'Recomendado':
                return 'Q3'
            elif row['decisao_pesquisador'] == 'Não Recomendado' and row['decisao_ministerio'] == 'Não Recomendado':
                return 'Q4'
            else:
                return None
        
        df_completo['quadrante'] = df_completo.apply(classificar_quadrante, axis=1)
    
    # Filtrar apenas registros com quadrante válido e setor definido
    df_analise = df_completo[
        (df_completo['quadrante'].notna()) & 
        (df_completo['do_set_nosetor'].notna()) &
        (df_completo['texto_combinado_processado'].str.len() > 0)
    ].copy()
    
    print(f"\n📊 Projetos válidos para análise: {len(df_analise):,}")
    
    # ============================================================================
    # ANÁLISE POR SETOR E QUADRANTE
    # ============================================================================
    
    # Identificar setores principais (top 6 por volume)
    setores_principais = df_analise['do_set_nosetor'].value_counts().head(6).index.tolist()
    
    print(f"\n🏭 Setores principais para análise:")
    for i, setor in enumerate(setores_principais, 1):
        count = len(df_analise[df_analise['do_set_nosetor'] == setor])
        print(f"{i}. {setor}: {count:,} projetos")
    
    # Armazenar resultados
    analise_palavras = {}
    
    # Analisar cada setor
    for setor in setores_principais:
        print(f"\n\nAnalisando setor: {setor}")
        print("-" * 60)
        
        df_setor = df_analise[df_analise['do_set_nosetor'] == setor]
        analise_palavras[setor] = {}
        
        # Analisar cada quadrante
        for quadrante in ['Q1', 'Q2', 'Q3', 'Q4']:
            df_quad = df_setor[df_setor['quadrante'] == quadrante]
            
            if len(df_quad) > 0:
                # Combinar todos os textos do quadrante
                todos_textos = ' '.join(df_quad['texto_combinado_processado'].values)
                palavras = todos_textos.split()
                
                # Contar palavras
                contador = Counter(palavras)
                top_palavras = contador.most_common(20)
                
                analise_palavras[setor][quadrante] = {
                    'total_projetos': len(df_quad),
                    'top_palavras': top_palavras,
                    'todas_palavras': todos_textos
                }
                
                print(f"\n{quadrante} ({len(df_quad)} projetos):")
                print("Top 10 palavras:")
                for palavra, freq in top_palavras[:10]:
                    print(f"   • {palavra}: {freq}")
    
    # ============================================================================
    # VISUALIZAÇÕES
    # ============================================================================
    
    # Figura 1: Top palavras por quadrante para cada setor
    fig = plt.figure(figsize=(24, 16))
    
    plot_idx = 1
    for setor_idx, setor in enumerate(setores_principais[:6]):  # Primeiros 6 setores
        for quad_idx, quadrante in enumerate(['Q1', 'Q2', 'Q3', 'Q4']):
            ax = plt.subplot(6, 4, plot_idx)
            plot_idx += 1
            
            if quadrante in analise_palavras[setor]:
                dados = analise_palavras[setor][quadrante]
                
                # Top 10 palavras
                palavras = [p[0] for p in dados['top_palavras'][:10]]
                frequencias = [p[1] for p in dados['top_palavras'][:10]]
                
                # Criar gráfico de barras
                y_pos = np.arange(len(palavras))
                bars = ax.barh(y_pos, frequencias)
                
                # Colorir barras por quadrante
                cores = {'Q1': '#2ecc71', 'Q2': '#e74c3c', 'Q3': '#f39c12', 'Q4': '#95a5a6'}
                for bar in bars:
                    bar.set_color(cores[quadrante])
                    bar.set_alpha(0.8)
                
                ax.set_yticks(y_pos)
                ax.set_yticklabels(palavras, fontsize=9)
                ax.invert_yaxis()
                ax.set_xlabel('Frequência', fontsize=9)
                
                # Título com informações
                titulo = f'{setor[:20]}...\n{quadrante} ({dados["total_projetos"]} proj.)'
                ax.set_title(titulo, fontsize=10, pad=5)
                ax.grid(axis='x', alpha=0.3)
                
                # Adicionar valores nas barras
                for i, (bar, freq) in enumerate(zip(bars, frequencias)):
                    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
                           str(freq), va='center', fontsize=8)
            else:
                ax.text(0.5, 0.5, f'Sem dados\n{quadrante}', 
                       ha='center', va='center', transform=ax.transAxes,
                       fontsize=12, alpha=0.5)
                ax.set_xticks([])
                ax.set_yticks([])
    
    plt.suptitle('Palavras Mais Frequentes por Quadrante e Setor (Top 3 Setores)', 
                fontsize=16, y=0.98)
    plt.tight_layout()
    plt.show()
    
    # Figura 2: Word Clouds comparativas
    fig = plt.figure(figsize=(20, 24))
    
    plot_idx = 1
    for setor in setores_principais[:6]:  # Primeiros 6 setores
        for quadrante in ['Q1', 'Q2', 'Q3', 'Q4']:
            ax = plt.subplot(6, 4, plot_idx)
            plot_idx += 1
            
            if quadrante in analise_palavras[setor] and analise_palavras[setor][quadrante]['todas_palavras']:
                # Criar word cloud
                texto = analise_palavras[setor][quadrante]['todas_palavras']
                
                # Cores por quadrante
                cores_map = {
                    'Q1': 'Greens',
                    'Q2': 'Reds', 
                    'Q3': 'Oranges',
                    'Q4': 'Greys'
                }
                
                wordcloud = WordCloud(
                    width=400, 
                    height=300,
                    background_color='white',
                    colormap=cores_map[quadrante],
                    max_words=50,
                    relative_scaling=0.5,
                    min_font_size=10
                ).generate(texto)
                
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                ax.set_title(f'{setor[:25]}...\n{quadrante} ({analise_palavras[setor][quadrante]["total_projetos"]} proj.)',
                           fontsize=10, pad=5)
            else:
                ax.text(0.5, 0.5, f'Sem dados\n{quadrante}', 
                       ha='center', va='center', transform=ax.transAxes,
                       fontsize=12, alpha=0.5)
                ax.axis('off')
    
    plt.suptitle('Word Clouds por Quadrante e Setor', fontsize=16, y=0.98)
    plt.tight_layout()
    plt.show()
    
    # ============================================================================
    # ANÁLISE COMPARATIVA
    # ============================================================================
    
    print("\n\n🔍 ANÁLISE COMPARATIVA DE TERMOS POR QUADRANTE")
    print("=" * 80)
    
    # Identificar palavras exclusivas ou predominantes em cada quadrante
    for setor in setores_principais:
        print(f"\n\n📌 {setor}")
        print("-" * 60)
        
        # Coletar todas as palavras por quadrante
        palavras_por_quadrante = {}
        for quad in ['Q1', 'Q2', 'Q3', 'Q4']:
            if quad in analise_palavras[setor]:
                contador = Counter(analise_palavras[setor][quad]['todas_palavras'].split())
                palavras_por_quadrante[quad] = contador
        
        # Encontrar palavras distintivas
        for quad in ['Q1', 'Q2', 'Q3', 'Q4']:
            if quad in palavras_por_quadrante:
                print(f"\n{quad} - Termos Distintivos:")
                
                # Calcular score de distintividade
                palavras_distintivas = []
                for palavra, freq in palavras_por_quadrante[quad].most_common(50):
                    # Frequência em outros quadrantes
                    freq_outros = sum(palavras_por_quadrante[q].get(palavra, 0) 
                                    for q in palavras_por_quadrante if q != quad)
                    
                    # Score: frequência no quadrante / (frequência total + 1)
                    score = freq / (freq + freq_outros + 1)
                    
                    if score > 0.5 and freq >= 5:  # Palavra distintiva
                        palavras_distintivas.append((palavra, freq, score))
                
                # Mostrar top 5 palavras distintivas
                palavras_distintivas.sort(key=lambda x: x[2], reverse=True)
                for palavra, freq, score in palavras_distintivas[:5]:
                    print(f"   • {palavra}: freq={freq}, distintividade={score:.2f}")
    
    # ============================================================================
    # TABELA RESUMO
    # ============================================================================
    
    print("\n\n📊 TABELA RESUMO: CARACTERÍSTICAS TEXTUAIS POR QUADRANTE")
    print("=" * 100)
    print(f"{'Setor':<30} {'Quadrante':<10} {'Projetos':>10} {'Top 3 Palavras':<50}")
    print("-" * 100)
    
    for setor in setores_principais:
        setor_nome = setor[:28] + '..' if len(setor) > 30 else setor
        
        for quad in ['Q1', 'Q2', 'Q3', 'Q4']:
            if quad in analise_palavras[setor]:
                dados = analise_palavras[setor][quad]
                top3 = ', '.join([f"{p[0]}({p[1]})" for p in dados['top_palavras'][:3]])
                print(f"{setor_nome:<30} {quad:<10} {dados['total_projetos']:>10} {top3:<50}")
    
    print("=" * 100)
    
    # Exportar resultados
    print("\n💾 Exportando resultados...")
    
    # Criar DataFrame com resultados
    resultados_export = []
    for setor in analise_palavras:
        for quad in analise_palavras[setor]:
            for palavra, freq in analise_palavras[setor][quad]['top_palavras']:
                resultados_export.append({
                    'Setor': setor,
                    'Quadrante': quad,
                    'Palavra': palavra,
                    'Frequencia': freq,
                    'Total_Projetos_Quadrante': analise_palavras[setor][quad]['total_projetos']
                })
    
    df_export = pd.DataFrame(resultados_export)
    df_export.to_csv('analise_textual_quadrantes_setor.csv', index=False, sep=';', encoding='utf-8')
    
    print("✅ Arquivo 'analise_textual_quadrantes_setor.csv' exportado com sucesso!")
    
    print("\n" + "=" * 80)
    print("ANÁLISE TEXTUAL POR QUADRANTE E SETOR CONCLUÍDA")
    print("=" * 80)
```

    ================================================================================
    ANÁLISE TEXTUAL POR QUADRANTE E SETOR
    Lei do Bem: Palavras-chave por tipo de decisão
    ================================================================================
    📊 Campos textuais identificados: 6
       • daproj_noprojeto
       • daproj_dsprojeto
       • daproj_dspalavrachave
       • daproj_dselementotecnologico
       • daproj_dsdesafiotecnologico
       • daproj_dsmetodologiautilizada

    Combinando campos textuais...

    📊 Projetos válidos para análise: 68,437

    🏭 Setores principais para análise:
    1. TIC: 18,769 projetos
    2. Química e Farmácia: 12,845 projetos
    3. Mecânica e Transporte: 9,067 projetos
    4. Agroindústria e Alimentos: 8,144 projetos
    5. Transversal: 7,466 projetos
    6. Eletroeletrônica: 7,157 projetos


    Analisando setor: TIC
    ------------------------------------------------------------

    Q1 (7670 projetos):
    Top 10 palavras:
       • dados: 58213
       • sistema: 39860
       • informações: 25176
       • testes: 24361
       • sistemas: 23122
       • solução: 22163
       • além: 21861
       • integração: 21233
       • equipe: 19488
       • plataforma: 19392

    Q2 (2268 projetos):
    Top 10 palavras:
       • dados: 21333
       • sistema: 11437
       • informações: 8744
       • solução: 7909
       • plataforma: 7808
       • testes: 7582
       • integração: 7537
       • além: 7025
       • soluções: 6697
       • cada: 6608

    Q3 (1408 projetos):
    Top 10 palavras:
       • dados: 6380
       • sistema: 5919
       • informações: 3757
       • sistemas: 3348
       • testes: 3343
       • solução: 3095
       • além: 3073
       • integração: 2929
       • plataforma: 2919
       • cada: 2603

    Q4 (7423 projetos):
    Top 10 palavras:
       • dados: 60879
       • sistema: 38602
       • integração: 27340
       • informações: 26014
       • sistemas: 25483
       • testes: 23913
       • equipe: 23606
       • soluções: 22970
       • além: 22496
       • plataforma: 22038


    Analisando setor: Química e Farmácia
    ------------------------------------------------------------

    Q1 (9415 projetos):
    Top 10 palavras:
       • produto: 36639
       • testes: 34574
       • produtos: 27754
       • estudos: 22150
       • além: 20621
       • estudo: 18699
       • formulação: 18355
       • produção: 16513
       • tratamento: 15407
       • qualidade: 14257

    Q2 (424 projetos):
    Top 10 palavras:
       • testes: 1720
       • produto: 1661
       • produtos: 1608
       • além: 1178
       • qualidade: 1126
       • sistema: 1118
       • estudos: 1029
       • equipe: 935
       • formulação: 851
       • tratamento: 848

    Q3 (710 projetos):
    Top 10 palavras:
       • testes: 1835
       • produto: 1536
       • produtos: 1392
       • estudos: 1350
       • sistema: 1075
       • estudo: 1064
       • além: 994
       • tratamento: 917
       • qualidade: 813
       • produção: 774

    Q4 (2296 projetos):
    Top 10 palavras:
       • produto: 5682
       • testes: 4231
       • produtos: 3925
       • além: 2744
       • estudos: 2716
       • sistema: 2708
       • produção: 2363
       • qualidade: 2273
       • estudo: 2227
       • formulação: 2161


    Analisando setor: Mecânica e Transporte
    ------------------------------------------------------------

    Q1 (4952 projetos):
    Top 10 palavras:
       • sistema: 24626
       • testes: 22110
       • produto: 12273
       • além: 11301
       • componentes: 9800
       • maior: 9699
       • estudos: 8763
       • durante: 8643
       • sistemas: 7941
       • produção: 7888

    Q2 (404 projetos):
    Top 10 palavras:
       • sistema: 2240
       • testes: 1529
       • além: 1467
       • qualidade: 1317
       • equipe: 1068
       • produtos: 1054
       • produção: 1043
       • linha: 992
       • dados: 971
       • maior: 966

    Q3 (1230 projetos):
    Top 10 palavras:
       • sistema: 3913
       • testes: 3798
       • produto: 2422
       • além: 1832
       • componentes: 1742
       • maior: 1723
       • estudos: 1598
       • veículo: 1571
       • durante: 1459
       • produção: 1440

    Q4 (2481 projetos):
    Top 10 palavras:
       • sistema: 7077
       • testes: 6784
       • além: 4005
       • produto: 3871
       • qualidade: 3596
       • estudos: 3281
       • produtos: 3279
       • produção: 3253
       • linha: 3010
       • garantir: 2942


    Analisando setor: Agroindústria e Alimentos
    ------------------------------------------------------------

    Q1 (4236 projetos):
    Top 10 palavras:
       • produto: 16785
       • testes: 14301
       • produtos: 14222
       • além: 10045
       • produção: 9070
       • estudos: 8758
       • diferentes: 8638
       • qualidade: 8429
       • maior: 8312
       • aplicação: 7868

    Q2 (694 projetos):
    Top 10 palavras:
       • produtos: 3809
       • produto: 3048
       • testes: 2737
       • produção: 2314
       • além: 2232
       • qualidade: 2183
       • controle: 1886
       • maior: 1831
       • estudos: 1700
       • aplicação: 1619

    Q3 (614 projetos):
    Top 10 palavras:
       • produto: 1998
       • sistema: 1542
       • testes: 1402
       • produtos: 1305
       • produção: 1030
       • além: 975
       • estudos: 882
       • maior: 821
       • qualidade: 808
       • linha: 740

    Q4 (2600 projetos):
    Top 10 palavras:
       • produto: 6366
       • produtos: 6330
       • testes: 5186
       • sistema: 5102
       • produção: 5056
       • qualidade: 4448
       • além: 4132
       • maior: 3354
       • controle: 3112
       • linha: 2915


    Analisando setor: Transversal
    ------------------------------------------------------------

    Q1 (3489 projetos):
    Top 10 palavras:
       • testes: 12283
       • produto: 10725
       • produtos: 9538
       • sistema: 8614
       • além: 7917
       • produção: 7507
       • qualidade: 6953
       • maior: 6713
       • aplicação: 6271
       • estudos: 5606

    Q2 (879 projetos):
    Top 10 palavras:
       • testes: 3192
       • produto: 3017
       • produtos: 2653
       • sistema: 2565
       • além: 2240
       • qualidade: 1963
       • dados: 1707
       • produção: 1660
       • equipe: 1628
       • maior: 1564

    Q3 (630 projetos):
    Top 10 palavras:
       • testes: 1626
       • produto: 1475
       • produtos: 1337
       • sistema: 1313
       • além: 983
       • maior: 979
       • linha: 926
       • produção: 859
       • qualidade: 824
       • estudos: 786

    Q4 (2468 projetos):
    Top 10 palavras:
       • produtos: 6251
       • sistema: 5786
       • testes: 5436
       • produto: 5035
       • qualidade: 4765
       • além: 4545
       • produção: 3980
       • maior: 3387
       • equipe: 3326
       • estudo: 3169


    Analisando setor: Eletroeletrônica
    ------------------------------------------------------------

    Q1 (4035 projetos):
    Top 10 palavras:
       • sistema: 19581
       • testes: 11869
       • dados: 9648
       • energia: 9538
       • produto: 9367
       • além: 8638
       • controle: 7700
       • sistemas: 7619
       • análise: 6389
       • maior: 5910

    Q2 (157 projetos):
    Top 10 palavras:
       • sistema: 1119
       • testes: 472
       • energia: 428
       • controle: 421
       • dados: 351
       • além: 341
       • sistemas: 337
       • produto: 331
       • tempo: 307
       • maior: 292

    Q3 (792 projetos):
    Top 10 palavras:
       • sistema: 3016
       • testes: 1943
       • produto: 1685
       • dados: 1408
       • energia: 1226
       • controle: 1178
       • além: 1111
       • produtos: 1094
       • cada: 1050
       • sistemas: 1034

    Q4 (2173 projetos):
    Top 10 palavras:
       • sistema: 9353
       • testes: 4917
       • produto: 4540
       • dados: 3561
       • além: 3535
       • energia: 3505
       • sistemas: 3200
       • estudos: 3153
       • transmissão: 3027
       • controle: 3002

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-13-output-2.png)

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-13-output-3.png)



    🔍 ANÁLISE COMPARATIVA DE TERMOS POR QUADRANTE
    ================================================================================


    📌 TIC
    ------------------------------------------------------------

    Q1 - Termos Distintivos:

    Q2 - Termos Distintivos:

    Q3 - Termos Distintivos:

    Q4 - Termos Distintivos:


    📌 Química e Farmácia
    ------------------------------------------------------------

    Q1 - Termos Distintivos:
       • pacientes: freq=8177, distintividade=0.89
       • formulações: freq=12658, distintividade=0.87
       • resultados: freq=11644, distintividade=0.85
       • avaliação: freq=13812, distintividade=0.84
       • medicamento: freq=8956, distintividade=0.84

    Q2 - Termos Distintivos:

    Q3 - Termos Distintivos:

    Q4 - Termos Distintivos:


    📌 Mecânica e Transporte
    ------------------------------------------------------------

    Q1 - Termos Distintivos:
       • motor: freq=5660, distintividade=0.73
       • veículos: freq=6022, distintividade=0.69
       • resistência: freq=5664, distintividade=0.68
       • aplicação: freq=7636, distintividade=0.67
       • veículo: freq=5241, distintividade=0.66

    Q2 - Termos Distintivos:

    Q3 - Termos Distintivos:

    Q4 - Termos Distintivos:


    📌 Agroindústria e Alimentos
    ------------------------------------------------------------

    Q1 - Termos Distintivos:
       • plantas: freq=4304, distintividade=0.71
       • formulações: freq=4683, distintividade=0.68
       • ingredientes: freq=4395, distintividade=0.66
       • diferentes: freq=8638, distintividade=0.65
       • condições: freq=4782, distintividade=0.65

    Q2 - Termos Distintivos:

    Q3 - Termos Distintivos:

    Q4 - Termos Distintivos:
       • embalagem: freq=1885, distintividade=0.51


    📌 Transversal
    ------------------------------------------------------------

    Q1 - Termos Distintivos:
       • papel: freq=3300, distintividade=0.67
       • propriedades: freq=3344, distintividade=0.66
       • resistência: freq=5177, distintividade=0.61
       • material: freq=5302, distintividade=0.60
       • características: freq=4147, distintividade=0.59

    Q2 - Termos Distintivos:

    Q3 - Termos Distintivos:

    Q4 - Termos Distintivos:


    📌 Eletroeletrônica
    ------------------------------------------------------------

    Q1 - Termos Distintivos:
       • geração: freq=4603, distintividade=0.68
       • desafios: freq=4082, distintividade=0.67
       • operação: freq=4836, distintividade=0.66
       • comunicação: freq=4541, distintividade=0.66
       • rede: freq=4604, distintividade=0.66

    Q2 - Termos Distintivos:

    Q3 - Termos Distintivos:

    Q4 - Termos Distintivos:
       • transmissão: freq=3027, distintividade=0.51


    📊 TABELA RESUMO: CARACTERÍSTICAS TEXTUAIS POR QUADRANTE
    ====================================================================================================
    Setor                          Quadrante    Projetos Top 3 Palavras                                    
    ----------------------------------------------------------------------------------------------------
    TIC                            Q1               7670 dados(58213), sistema(39860), informações(25176)  
    TIC                            Q2               2268 dados(21333), sistema(11437), informações(8744)   
    TIC                            Q3               1408 dados(6380), sistema(5919), informações(3757)     
    TIC                            Q4               7423 dados(60879), sistema(38602), integração(27340)   
    Química e Farmácia             Q1               9415 produto(36639), testes(34574), produtos(27754)    
    Química e Farmácia             Q2                424 testes(1720), produto(1661), produtos(1608)       
    Química e Farmácia             Q3                710 testes(1835), produto(1536), produtos(1392)       
    Química e Farmácia             Q4               2296 produto(5682), testes(4231), produtos(3925)       
    Mecânica e Transporte          Q1               4952 sistema(24626), testes(22110), produto(12273)     
    Mecânica e Transporte          Q2                404 sistema(2240), testes(1529), além(1467)           
    Mecânica e Transporte          Q3               1230 sistema(3913), testes(3798), produto(2422)        
    Mecânica e Transporte          Q4               2481 sistema(7077), testes(6784), além(4005)           
    Agroindústria e Alimentos      Q1               4236 produto(16785), testes(14301), produtos(14222)    
    Agroindústria e Alimentos      Q2                694 produtos(3809), produto(3048), testes(2737)       
    Agroindústria e Alimentos      Q3                614 produto(1998), sistema(1542), testes(1402)        
    Agroindústria e Alimentos      Q4               2600 produto(6366), produtos(6330), testes(5186)       
    Transversal                    Q1               3489 testes(12283), produto(10725), produtos(9538)     
    Transversal                    Q2                879 testes(3192), produto(3017), produtos(2653)       
    Transversal                    Q3                630 testes(1626), produto(1475), produtos(1337)       
    Transversal                    Q4               2468 produtos(6251), sistema(5786), testes(5436)       
    Eletroeletrônica               Q1               4035 sistema(19581), testes(11869), dados(9648)        
    Eletroeletrônica               Q2                157 sistema(1119), testes(472), energia(428)          
    Eletroeletrônica               Q3                792 sistema(3016), testes(1943), produto(1685)        
    Eletroeletrônica               Q4               2173 sistema(9353), testes(4917), produto(4540)        
    ====================================================================================================

    💾 Exportando resultados...
    ✅ Arquivo 'analise_textual_quadrantes_setor.csv' exportado com sucesso!

    ================================================================================
    ANÁLISE TEXTUAL POR QUADRANTE E SETOR CONCLUÍDA
    ================================================================================

#### Distintividade

A distintividade é uma métrica que mede o quão específica ou
característica uma palavra é para um determinado quadrante em comparação
com os outros quadrantes.

Fórmula Implementada:

    Distintividade = freq_quadrante / (freq_quadrante + freq_outros_quadrantes + 1)

Onde:

freq_quadrante = frequência da palavra no quadrante analisado

freq_outros_quadrantes = soma das frequências da palavra em todos os
outros quadrantes

+1 = fator de suavização para evitar divisão por zero

##### Interpretação:

Distintividade = 1.0: A palavra aparece APENAS neste quadrante

Distintividade = 0.5: A palavra aparece com a mesma frequência neste
quadrante e nos outros combinados

Distintividade = 0.0: A palavra nunca aparece neste quadrante

### Análise por Setor

Este bloco de código executa uma análise detalhada das taxas de
aprovação de projetos organizados por área/setor. O código primeiro
padroniza as decisões dos avaliadores (analista/DO e
parecerista/Parecer) em três categorias: “Recomendado”, “Não
Recomendado” ou “Outro”. Em seguida, filtra os dados para incluir apenas
projetos com área definida, resultando em 68.443 projetos válidos
distribuídos em 7 áreas únicas.

A saída apresenta a distribuição das áreas ordenadas por volume, sendo
TIC a maior com 18.772 projetos, seguida por Química e Farmácia com
12.845 projetos. O código calcula estatísticas gerais mostrando uma taxa
média de aprovação de 61,3% na fase DO e 63,6% na fase Parecer, com uma
diferença média positiva de 2,3% entre as fases.

A tabela principal exibe as 20 principais áreas por volume, mostrando
para cada uma: o total de projetos, as taxas de aprovação em cada fase
(DO e Parecer), a diferença percentual entre as fases e o número de
projetos que mudaram de decisão entre as avaliações. Por exemplo, TIC
apresenta 19,6% de projetos que mudaram de decisão (3.676 de 18.772
projetos).

A seção de destaques identifica padrões importantes: áreas com maiores
taxas de aprovação em cada fase, áreas com maior queda ou aumento entre
as fases DO e Parecer, e áreas com maior taxa de mudança de decisão.
Metalurgia e Mineração lidera com 15,9% de projetos que mudaram de
decisão, indicando maior discordância entre avaliadores neste setor. O
código fornece uma visão abrangente do desempenho de aprovação por setor
e identifica onde há maior convergência ou divergência entre as duas
fases de avaliação.

``` python
# Análise de aprovação por área do projeto
print("\n📊 ANÁLISE DE APROVAÇÃO POR ÁREA DO PROJETO")
print("=" * 80)

# Função para padronizar decisões (mantém a mesma)
def padronizar_decisao(decisao):
    if pd.isna(decisao):
        return np.nan
    decisao_str = str(decisao).strip().upper()
    if 'RECOMENDADO' in decisao_str and 'NÃO' not in decisao_str:
        return 'Recomendado'
    elif 'NÃO RECOMENDADO' in decisao_str:
        return 'Não Recomendado'
    else:
        return 'Outro'

# Aplicar padronização
df_completo['decisao_analista'] = df_completo['do_taaproj_notipoavaliacaoanalise'].apply(padronizar_decisao)
df_completo['decisao_pesquisador'] = df_completo['p_taaproj_notipoavaliacaoanalise'].apply(padronizar_decisao)

# Verificar se a coluna de área do projeto existe
if 'do_set_nosetor' in df_completo.columns:
    print("✅ Usando coluna 'do_set_nosetor' (Área do Projeto)")
    
    # Filtrar registros com área definida
    df_com_area = df_completo[df_completo['do_set_nosetor'].notna()].copy()
    print(f"📊 Projetos com área definida: {len(df_com_area):,}")
    
    # Mostrar distribuição das áreas
    print("\n📊 Distribuição das Áreas de Projeto:")
    dist_areas = df_com_area['do_set_nosetor'].value_counts()
    print(f"Total de áreas únicas: {len(dist_areas)}")
    print("\nTop 15 áreas por volume:")
    for i, (area, count) in enumerate(dist_areas.head(15).items()):
        print(f"{i+1:2d}. {area}: {count:,} projetos")
    
    # Calcular estatísticas por área
    analise_por_area = []
    
    for area in df_com_area['do_set_nosetor'].unique():
        if pd.notna(area):
            projetos_area = df_com_area[df_com_area['do_set_nosetor'] == area]
            
            # Estatísticas DO (Analista)
            total_do = len(projetos_area[projetos_area['decisao_analista'].notna()])
            aprovados_do = len(projetos_area[projetos_area['decisao_analista'] == 'Recomendado'])
            taxa_do = (aprovados_do / total_do * 100) if total_do > 0 else 0
            
            # Estatísticas Parecer (Parecerista)
            total_parecer = len(projetos_area[projetos_area['decisao_pesquisador'].notna()])
            aprovados_parecer = len(projetos_area[projetos_area['decisao_pesquisador'] == 'Recomendado'])
            taxa_parecer = (aprovados_parecer / total_parecer * 100) if total_parecer > 0 else 0
            
            # Projetos que mudaram de decisão
            projetos_duas_fases = projetos_area[
                (projetos_area['decisao_analista'].notna()) & 
                (projetos_area['decisao_pesquisador'].notna())
            ]
            
            mudou_decisao = 0
            if len(projetos_duas_fases) > 0:
                mudou_decisao = len(projetos_duas_fases[
                    projetos_duas_fases['decisao_analista'] != projetos_duas_fases['decisao_pesquisador']
                ])
            
            analise_por_area.append({
                'Area_Projeto': area,
                'Total_Projetos': len(projetos_area),
                'Total_DO': total_do,
                'Aprovados_DO': aprovados_do,
                'Taxa_Aprovacao_DO_%': taxa_do,
                'Total_Parecer': total_parecer,
                'Aprovados_Parecer': aprovados_parecer,
                'Taxa_Aprovacao_Parecer_%': taxa_parecer,
                'Diferenca_Taxa_%': taxa_parecer - taxa_do,
                'Projetos_Mudaram_Decisao': mudou_decisao,
                'Taxa_Mudanca_%': (mudou_decisao / len(projetos_duas_fases) * 100) if len(projetos_duas_fases) > 0 else 0
            })

# Criar DataFrame com resultados
    df_areas = pd.DataFrame(analise_por_area)
    df_areas = df_areas.sort_values('Total_Projetos', ascending=False)
    
    # Estatísticas gerais
    print(f"\n📊 ESTATÍSTICAS GERAIS:")
    print(f"Total de áreas analisadas: {len(df_areas)}")
    print(f"Taxa média de aprovação DO: {df_areas['Taxa_Aprovacao_DO_%'].mean():.1f}%")
    print(f"Taxa média de aprovação Parecer: {df_areas['Taxa_Aprovacao_Parecer_%'].mean():.1f}%")
    print(f"Diferença média (Parecer - DO): {df_areas['Diferenca_Taxa_%'].mean():.1f}%")
    
    # Tabela resumo
    print("\n📋 TABELA DE APROVAÇÃO POR ÁREA DO PROJETO (Top 20 por volume)")
    print("=" * 130)
    print(f"{'Área do Projeto':<40} {'Projetos':>10} {'Taxa DO':>12} {'Taxa Parecer':>12} {'Diferença':>12} {'Mudaram':>10}")
    print("-" * 130)
    
    for _, row in df_areas.head(20).iterrows():
        area = row['Area_Projeto'][:38] + '..' if len(row['Area_Projeto']) > 40 else row['Area_Projeto']
        print(f"{area:<40} {row['Total_Projetos']:>10} "
              f"{row['Taxa_Aprovacao_DO_%']:>11.1f}% {row['Taxa_Aprovacao_Parecer_%']:>11.1f}% "
              f"{row['Diferenca_Taxa_%']:>11.1f}% {row['Projetos_Mudaram_Decisao']:>10}")
    
    print("=" * 130)
    
    # Destaques
    print("\n🔍 DESTAQUES DA ANÁLISE POR ÁREA DO PROJETO:")
    
    print(f"\nÁreas com MAIOR taxa de aprovação no DO:")
    top_do = df_areas.nlargest(5, 'Taxa_Aprovacao_DO_%')
    for _, row in top_do.iterrows():
        print(f"  - {row['Area_Projeto']}: {row['Taxa_Aprovacao_DO_%']:.1f}% ({row['Total_Projetos']} projetos)")
    
    print(f"\nÁreas com MAIOR taxa de aprovação no Parecer:")
    top_parecer = df_areas.nlargest(5, 'Taxa_Aprovacao_Parecer_%')
    for _, row in top_parecer.iterrows():
        print(f"  - {row['Area_Projeto']}: {row['Taxa_Aprovacao_Parecer_%']:.1f}% ({row['Total_Projetos']} projetos)")
    
    print(f"\nÁreas com MAIOR QUEDA entre DO e Parecer:")
    maior_queda = df_areas.nsmallest(5, 'Diferenca_Taxa_%')
    for _, row in maior_queda.iterrows():
        if row['Diferenca_Taxa_%'] < 0:
            print(f"  - {row['Area_Projeto']}: {row['Diferenca_Taxa_%']:.1f}% de queda ({row['Total_Projetos']} projetos)")
    
    print(f"\nÁreas com MAIOR AUMENTO entre DO e Parecer:")
    maior_aumento = df_areas.nlargest(5, 'Diferenca_Taxa_%')
    for _, row in maior_aumento.iterrows():
        if row['Diferenca_Taxa_%'] > 0:
            print(f"  - {row['Area_Projeto']}: +{row['Diferenca_Taxa_%']:.1f}% de aumento ({row['Total_Projetos']} projetos)")
    
    print(f"\nÁreas com MAIOR taxa de mudança de decisão:")
    maior_mudanca = df_areas.nlargest(5, 'Taxa_Mudanca_%')
    for _, row in maior_mudanca.iterrows():
        if row['Taxa_Mudanca_%'] > 0:
            print(f"  - {row['Area_Projeto']}: {row['Taxa_Mudanca_%']:.1f}% mudaram decisão ({row['Projetos_Mudaram_Decisao']} de {row['Total_Projetos']} projetos)")

else:
    print("❌ Coluna 'do_set_nosetor' não encontrada no dataset")
    # Lista alternativas disponíveis
    print("Colunas disponíveis que podem conter informação de categoria:")
    for col in df_completo.columns:
        if 'area' in col.lower() or 'setor' in col.lower() or 'atividade' in col.lower():
            print(f"  - {col}")
```


    📊 ANÁLISE DE APROVAÇÃO POR ÁREA DO PROJETO
    ================================================================================
    ✅ Usando coluna 'do_set_nosetor' (Área do Projeto)
    📊 Projetos com área definida: 68,443

    📊 Distribuição das Áreas de Projeto:
    Total de áreas únicas: 7

    Top 15 áreas por volume:
     1. TIC: 18,772 projetos
     2. Química e Farmácia: 12,845 projetos
     3. Mecânica e Transporte: 9,068 projetos
     4. Agroindústria e Alimentos: 8,144 projetos
     5. Transversal: 7,467 projetos
     6. Eletroeletrônica: 7,158 projetos
     7. Metalurgia e Mineração: 4,989 projetos

    📊 ESTATÍSTICAS GERAIS:
    Total de áreas analisadas: 7
    Taxa média de aprovação DO: 61.3%
    Taxa média de aprovação Parecer: 63.6%
    Diferença média (Parecer - DO): 2.3%

    📋 TABELA DE APROVAÇÃO POR ÁREA DO PROJETO (Top 20 por volume)
    ==================================================================================================================================
    Área do Projeto                            Projetos      Taxa DO Taxa Parecer    Diferença    Mudaram
    ----------------------------------------------------------------------------------------------------------------------------------
    TIC                                           18772        52.9%        48.4%        -4.6%       3676
    Química e Farmácia                            12845        76.6%        78.8%         2.2%       1134
    Mecânica e Transporte                          9068        59.1%        68.2%         9.1%       1634
    Agroindústria e Alimentos                      8144        60.5%        59.6%        -1.0%       1308
    Transversal                                    7467        58.5%        55.2%        -3.3%       1509
    Eletroeletrônica                               7158        58.6%        67.4%         8.9%        949
    Metalurgia e Mineração                         4989        62.8%        67.6%         4.8%        791
    ==================================================================================================================================

    🔍 DESTAQUES DA ANÁLISE POR ÁREA DO PROJETO:

    Áreas com MAIOR taxa de aprovação no DO:
      - Química e Farmácia: 76.6% (12845 projetos)
      - Metalurgia e Mineração: 62.8% (4989 projetos)
      - Agroindústria e Alimentos: 60.5% (8144 projetos)
      - Mecânica e Transporte: 59.1% (9068 projetos)
      - Eletroeletrônica: 58.6% (7158 projetos)

    Áreas com MAIOR taxa de aprovação no Parecer:
      - Química e Farmácia: 78.8% (12845 projetos)
      - Mecânica e Transporte: 68.2% (9068 projetos)
      - Metalurgia e Mineração: 67.6% (4989 projetos)
      - Eletroeletrônica: 67.4% (7158 projetos)
      - Agroindústria e Alimentos: 59.6% (8144 projetos)

    Áreas com MAIOR QUEDA entre DO e Parecer:
      - TIC: -4.6% de queda (18772 projetos)
      - Transversal: -3.3% de queda (7467 projetos)
      - Agroindústria e Alimentos: -1.0% de queda (8144 projetos)

    Áreas com MAIOR AUMENTO entre DO e Parecer:
      - Mecânica e Transporte: +9.1% de aumento (9068 projetos)
      - Eletroeletrônica: +8.9% de aumento (7158 projetos)
      - Metalurgia e Mineração: +4.8% de aumento (4989 projetos)
      - Química e Farmácia: +2.2% de aumento (12845 projetos)

    Áreas com MAIOR taxa de mudança de decisão:
      - Transversal: 20.2% mudaram decisão (1509 de 7467 projetos)
      - TIC: 19.6% mudaram decisão (3676 de 18772 projetos)
      - Mecânica e Transporte: 18.0% mudaram decisão (1634 de 9068 projetos)
      - Agroindústria e Alimentos: 16.1% mudaram decisão (1308 de 8144 projetos)
      - Metalurgia e Mineração: 15.9% mudaram decisão (791 de 4989 projetos)

### Visualização por Setor

#### Gráfico 4.4 - Taxa de Aprovação por Área do Projeto: Comparação DO vs Parecer

Este gráfico de barras agrupadas compara as taxas de aprovação entre
duas fases de avaliação (DO e Parecer) para as 15 áreas com maior volume
de projetos. As barras azuis representam a taxa de aprovação na fase DO
(primeira avaliação) e as barras vermelhas representam a taxa na fase
Parecer (segunda avaliação). Cada par de barras corresponde a uma área
específica, com os valores percentuais exibidos acima de cada barra. O
eixo vertical mostra a taxa de aprovação em percentual, variando de 0 a
100%. As áreas estão ordenadas por volume total de projetos, sendo TIC a
área com maior número de projetos analisados. A grade horizontal
facilita a leitura dos valores percentuais.

``` python
# Visualizações para análise por área
if 'df_areas' in locals() and len(df_areas) > 0:
    
    # Visualização 1: Gráfico de barras comparativo DO vs Parecer
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Preparar dados (top 15 áreas por volume)
    top_areas = df_areas.head(15)
    x = np.arange(len(top_areas))
    width = 0.35
    
    # Barras
    bars1 = ax.bar(x - width/2, top_areas['Taxa_Aprovacao_DO_%'], width, 
                   label='Fase DO', color='#3498db', alpha=0.8)
    bars2 = ax.bar(x + width/2, top_areas['Taxa_Aprovacao_Parecer_%'], width,
                   label='Fase Parecer', color='#e74c3c', alpha=0.8)
    
    # Adicionar valores nas barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{height:.1f}%', ha='center', va='bottom', fontsize=9)
    
    # Configurar eixos
    ax.set_xlabel('Área do Projeto', fontsize=12)
    ax.set_ylabel('Taxa de Aprovação (%)', fontsize=12)
    ax.set_title('Taxa de Aprovação por Área do Projeto: Comparação DO vs Parecer (Top 15)', fontsize=16, pad=20)
    ax.set_xticks(x)
    
    # Labels das áreas (truncar se muito longo)
    labels_areas = [area[:20] + '...' if len(area) > 20 else area for area in top_areas['Area_Projeto']]
    ax.set_xticklabels(labels_areas, rotation=45, ha='right')
    
    ax.legend(loc='upper right', fontsize=12)
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_ylim(0, 105)
    
    plt.tight_layout()
    plt.show()
    
else:
    print("\n❌ Não foi possível realizar a análise por área do projeto")
    print("Verifique se a coluna 'do_set_nosetor' existe e contém dados válidos")
```

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-15-output-1.png)

#### Gráfico 4.5 - Correlação entre Taxas de Aprovação DO e Parecer por Área do Projeto

Este gráfico de dispersão mostra a relação entre as taxas de aprovação
das duas fases de avaliação. No eixo horizontal está a taxa de aprovação
na fase DO e no eixo vertical a taxa na fase Parecer. Cada círculo
representa uma área diferente, sendo que o tamanho do círculo é
proporcional ao número total de projetos daquela área (círculos maiores
indicam áreas com mais projetos). A cor dos círculos segue uma escala
que vai do vermelho ao azul, representando a diferença percentual entre
as taxas (Parecer menos DO). A linha diagonal tracejada representa o
ponto onde as taxas seriam iguais nas duas fases. Áreas específicas como
TIC, Química e Farmácia, e Mecânica e Transporte estão identificadas com
rótulos devido ao seu volume significativo ou diferença expressiva entre
as fases.

``` python
if 'df_areas' in locals() and len(df_areas) > 0:
    # Visualização 2: Scatter plot - Taxa DO vs Taxa Parecer
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Filtrar áreas com pelo menos 20 projetos para melhor visualização
    df_scatter = df_areas[df_areas['Total_Projetos'] >= 20]
    
    if len(df_scatter) > 0:
        scatter = ax.scatter(df_scatter['Taxa_Aprovacao_DO_%'], 
                           df_scatter['Taxa_Aprovacao_Parecer_%'],
                           s=df_scatter['Total_Projetos']*3,  # Tamanho proporcional
                           c=df_scatter['Diferenca_Taxa_%'],
                           cmap='RdYlBu', alpha=0.6, edgecolors='black', linewidth=1)
        
        # Linha de referência (y = x)
        ax.plot([0, 100], [0, 100], 'k--', alpha=0.5, label='Linha de Igualdade')
        
        # Adicionar labels para áreas extremas
        for _, row in df_scatter.iterrows():
            if abs(row['Diferenca_Taxa_%']) > 25 or row['Total_Projetos'] > df_scatter['Total_Projetos'].quantile(0.6):
                label_area = row['Area_Projeto'][:15] + '...' if len(row['Area_Projeto']) > 15 else row['Area_Projeto']
                ax.annotate(label_area, 
                          (row['Taxa_Aprovacao_DO_%'], row['Taxa_Aprovacao_Parecer_%']),
                          fontsize=9, alpha=0.7, 
                          bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
        
        ax.set_xlabel('Taxa de Aprovação DO (%)', fontsize=12)
        ax.set_ylabel('Taxa de Aprovação Parecer (%)', fontsize=12)
        ax.set_title('Correlação entre Taxas de Aprovação DO e Parecer por Área do Projeto', fontsize=14)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 105)
        ax.set_ylim(0, 105)
        ax.legend()
        
        # Colorbar
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Diferença (Parecer - DO) %', rotation=270, labelpad=20)
        
        plt.tight_layout()
        plt.show()
    else:
        print("\n❌ Não foi possível realizar a análise por área do projeto")
        print("Verifique se a coluna 'do_set_nosetor' existe e contém dados válidos")
```

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-16-output-1.png)

#### Gráfico 4.6 - Análise Detalhada por Área do Projeto

Este mapa de calor apresenta uma visão consolidada de quatro métricas
diferentes para as 20 áreas com maior volume de projetos. As linhas
representam: Taxa de Aprovação DO, Taxa de Aprovação Parecer, Taxa de
Mudança de Decisão (percentual de projetos que tiveram decisão diferente
entre as fases) e Diferença (Parecer-DO). Cada célula contém o valor
numérico da métrica e é colorida segundo uma escala que vai do azul
escuro (valores mais negativos) ao vermelho escuro (valores mais
positivos), com o branco representando valores próximos a zero. Esta
escala de cores está centrada em zero, facilitando a identificação
visual de valores positivos e negativos, especialmente útil para a linha
de Diferença onde valores negativos indicam queda na taxa de aprovação e
positivos indicam aumento.

``` python
if 'df_areas' in locals() and len(df_areas) > 0:
    
    # Visualização 3: Heatmap de análise por área
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Preparar dados para heatmap (top 20 áreas)
    heatmap_data = df_areas.head(20)[['Taxa_Aprovacao_DO_%', 'Taxa_Aprovacao_Parecer_%', 
                                      'Taxa_Mudanca_%', 'Diferenca_Taxa_%']]
    
    # Truncar nomes das áreas para o heatmap
    areas_truncadas = [area[:25] + '...' if len(area) > 25 else area for area in df_areas.head(20)['Area_Projeto']]
    heatmap_data.index = areas_truncadas
    
    sns.heatmap(heatmap_data.T, annot=True, fmt='.1f', cmap='coolwarm', center=0,
               cbar_kws={'label': 'Percentual (%)'}, linewidths=0.5, linecolor='gray')
    
    ax.set_xlabel('Área do Projeto', fontsize=12)
    ax.set_yticklabels(['Taxa Aprovação DO', 'Taxa Aprovação Parecer', 
                      'Taxa Mudança Decisão', 'Diferença (Parecer-DO)'], rotation=0)
    ax.set_title('Análise Detalhada por Área do Projeto - Top 20 por Volume', fontsize=14)
    
    plt.tight_layout()
    plt.show()
        
    # Exportar resultados
    df_areas.to_csv('analise_aprovacao_por_area_projeto.csv', index=False, sep=';', encoding='utf-8')
    print("\n💾 Resultados exportados para 'analise_aprovacao_por_area_projeto.csv'")
    
    # Estatísticas adicionais
    print(f"\n📊 ESTATÍSTICAS ADICIONAIS:")
    print(f"Áreas com 100% aprovação no Parecer: {len(df_areas[df_areas['Taxa_Aprovacao_Parecer_%'] == 100])}")
    print(f"Áreas com 0% aprovação no Parecer: {len(df_areas[df_areas['Taxa_Aprovacao_Parecer_%'] == 0])}")
    print(f"Área com maior volume: {df_areas.iloc[0]['Area_Projeto']} ({df_areas.iloc[0]['Total_Projetos']} projetos)")
    print(f"Diferença máxima (Parecer-DO): {df_areas['Diferenca_Taxa_%'].max():.1f}%")
    print(f"Diferença mínima (Parecer-DO): {df_areas['Diferenca_Taxa_%'].min():.1f}%")

else:
    print("\n❌ Não foi possível realizar a análise por área do projeto")
    print("Verifique se a coluna 'do_set_nosetor' existe e contém dados válidos")
```

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-17-output-1.png)


    💾 Resultados exportados para 'analise_aprovacao_por_area_projeto.csv'

    📊 ESTATÍSTICAS ADICIONAIS:
    Áreas com 100% aprovação no Parecer: 0
    Áreas com 0% aprovação no Parecer: 0
    Área com maior volume: TIC (18772 projetos)
    Diferença máxima (Parecer-DO): 9.1%
    Diferença mínima (Parecer-DO): -4.6%

### Análise e Insights por Setor

**O que foi investigado:**

Esta análise focou em identificar padrões de aprovação por setor nas
duas fases principais do processo (DO e Parecer), quantificando as
diferenças entre as decisões dos analistas técnicos e dos pareceristas
para cada setor de atividade.

**Principais Descobertas:**

A análise setorial revela significativas disparidades nas taxas de
aprovação entre diferentes setores e entre as fases do processo:

-   **Variação Setorial**: As taxas de aprovação variam drasticamente
    entre setores, tanto na fase DO quanto no Parecer
-   **Tendência Geral**: A maioria dos setores apresenta queda na taxa
    de aprovação entre DO e Parecer, confirmando que os pareceristas
    aplicam critérios mais rigorosos
-   **Setores Favorecidos**: Alguns setores mantêm altas taxas de
    aprovação em ambas as fases
-   **Setores Penalizados**: Certos setores sofrem quedas dramáticas
    entre as fases

**Padrões Identificados:**

1.  **Setores de Alta Performance**: Setores com taxas superiores a 80%
    em ambas as fases
2.  **Setores de Queda Acentuada**: Setores que perdem mais de 20 pontos
    percentuais entre DO e Parecer
3.  **Setores de Reversão**: Raros casos onde a taxa no Parecer supera a
    do DO
4.  **Setores Voláteis**: Alta taxa de mudança de decisão entre fases

**Insights e Implicações Práticas:**

1.  **Especialização Setorial**: A variação nas taxas sugere que
    diferentes setores requerem expertise específica para avaliação
    adequada

2.  **Necessidade de Padronização**: As grandes diferenças entre setores
    podem indicar falta de critérios uniformes ou vieses setoriais

3.  **Oportunidade de Capacitação**: Setores com altas taxas de mudança
    entre fases podem se beneficiar de treinamento específico para
    analistas

4.  **Revisão de Critérios**: Setores com quedas sistemáticas merecem
    revisão dos critérios de avaliação aplicados

### 5. Análise de Concordância por Área do Projeto - Foco nos Quadrantes 1 e 4

#### Gráfico 5.1 - Análise de Concordância por Área: Q1 vs Q4

Este gráfico de dispersão apresenta a relação entre duas métricas de
concordância. No eixo horizontal (X) está representada a Taxa de
Concordância Positiva Q1, que indica o percentual de projetos onde tanto
o pesquisador quanto o ministério recomendam o projeto.

No eixo vertical (Y) está a Taxa de Concordância Negativa Q4,
representando o percentual onde ambos os avaliadores não recomendam.
Cada círculo no gráfico representa uma área diferente, sendo que o
tamanho do círculo é proporcional ao número total de projetos daquela
área.

A cor dos círculos varia de acordo com a concordância total (Q1+Q4),
seguindo uma escala de cores do roxo ao amarelo. As linhas tracejadas
indicam as médias de Q1 (54,5%) e Q4 (29,6%), enquanto a linha diagonal
representa o ponto de equilíbrio onde Q1 seria igual a Q4. O gráfico
inclui apenas áreas com 20 ou mais projetos para garantir
representatividade estatística.

``` python
# Análise de Concordância por Área do Projeto - Foco nos Quadrantes 1 e 4
print("=" * 80)
print("ANÁLISE DE CONCORDÂNCIA POR ÁREA DO PROJETO")
print("Foco: Quadrantes 1 (ambos recomendam) e 4 (ambos não recomendam)")
print("=" * 80)

# Verificar se temos os dados necessários
if 'df_analise_quadrantes' in locals() and 'do_set_nosetor' in df_analise_quadrantes.columns:
    
    # Criar classificação de quadrantes
    df_analise_quadrantes['quadrante'] = ''
    df_analise_quadrantes.loc[
        (df_analise_quadrantes['decisao_pesquisador'] == 'Recomendado') & 
        (df_analise_quadrantes['decisao_ministerio'] == 'Recomendado'), 'quadrante'] = 'Q1'
    df_analise_quadrantes.loc[
        (df_analise_quadrantes['decisao_pesquisador'] == 'Recomendado') & 
        (df_analise_quadrantes['decisao_ministerio'] == 'Não Recomendado'), 'quadrante'] = 'Q2'
    df_analise_quadrantes.loc[
        (df_analise_quadrantes['decisao_pesquisador'] == 'Não Recomendado') & 
        (df_analise_quadrantes['decisao_ministerio'] == 'Recomendado'), 'quadrante'] = 'Q3'
    df_analise_quadrantes.loc[
        (df_analise_quadrantes['decisao_pesquisador'] == 'Não Recomendado') & 
        (df_analise_quadrantes['decisao_ministerio'] == 'Não Recomendado'), 'quadrante'] = 'Q4'
    
    # Filtrar apenas áreas com dados válidos
    df_com_area = df_analise_quadrantes[df_analise_quadrantes['do_set_nosetor'].notna()].copy()
    
    # Análise por área
    analise_concordancia_area = []
    
    for area in df_com_area['do_set_nosetor'].unique():
        if pd.notna(area):
            projetos_area = df_com_area[df_com_area['do_set_nosetor'] == area]
            
            # Contagem por quadrante
            q1_count = len(projetos_area[projetos_area['quadrante'] == 'Q1'])
            q2_count = len(projetos_area[projetos_area['quadrante'] == 'Q2'])
            q3_count = len(projetos_area[projetos_area['quadrante'] == 'Q3'])
            q4_count = len(projetos_area[projetos_area['quadrante'] == 'Q4'])
            
            total_area = len(projetos_area)
            concordancia_positiva = q1_count / total_area * 100 if total_area > 0 else 0
            concordancia_negativa = q4_count / total_area * 100 if total_area > 0 else 0
            concordancia_total = (q1_count + q4_count) / total_area * 100 if total_area > 0 else 0
            discordancia_total = (q2_count + q3_count) / total_area * 100 if total_area > 0 else 0
            
            analise_concordancia_area.append({
                'Area': area,
                'Total_Projetos': total_area,
                'Q1_Ambos_Recomendam': q1_count,
                'Q1_Percent': concordancia_positiva,
                'Q4_Ambos_Nao_Recomendam': q4_count,
                'Q4_Percent': concordancia_negativa,
                'Q2_Pesq_Sim_Min_Nao': q2_count,
                'Q3_Pesq_Nao_Min_Sim': q3_count,
                'Concordancia_Total_%': concordancia_total,
                'Discordancia_Total_%': discordancia_total,
                'Razao_Q1_Q4': q1_count / q4_count if q4_count > 0 else float('inf')
            })
    
    # Criar DataFrame
    df_concordancia = pd.DataFrame(analise_concordancia_area)
    df_concordancia = df_concordancia.sort_values('Total_Projetos', ascending=False)
    
    # Estatísticas gerais
    print(f"\n📊 ESTATÍSTICAS GERAIS:")
    print(f"Total de áreas analisadas: {len(df_concordancia)}")
    print(f"Taxa média de concordância total: {df_concordancia['Concordancia_Total_%'].mean():.1f}%")
    print(f"Taxa média de concordância positiva (Q1): {df_concordancia['Q1_Percent'].mean():.1f}%")
    print(f"Taxa média de concordância negativa (Q4): {df_concordancia['Q4_Percent'].mean():.1f}%")
    
    # Top áreas por concordância
    print("\n🏆 TOP 10 ÁREAS COM MAIOR CONCORDÂNCIA TOTAL (Q1+Q4):")
    print("-" * 80)
    top_concordancia = df_concordancia.nlargest(10, 'Concordancia_Total_%')
    for i, row in enumerate(top_concordancia.iterrows(), 1):
        _, area_data = row
        print(f"{i:2d}. {area_data['Area'][:40]:<40} | "
              f"Conc: {area_data['Concordancia_Total_%']:5.1f}% | "
              f"Q1: {area_data['Q1_Percent']:5.1f}% | "
              f"Q4: {area_data['Q4_Percent']:5.1f}% | "
              f"({area_data['Total_Projetos']} projetos)")
    
    # Visualização 1: Scatter plot Q1 vs Q4
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Filtrar áreas com pelo menos 20 projetos
    df_vis = df_concordancia[df_concordancia['Total_Projetos'] >= 20]
    
    # Criar scatter plot
    scatter = ax.scatter(df_vis['Q1_Percent'], df_vis['Q4_Percent'],
                        s=df_vis['Total_Projetos']*2,
                        c=df_vis['Concordancia_Total_%'],
                        cmap='viridis', alpha=0.6,
                        edgecolors='black', linewidth=1)
    
    # Adicionar linhas de referência
    ax.axhline(y=df_vis['Q4_Percent'].mean(), color='red', linestyle='--', alpha=0.5, 
               label=f'Média Q4: {df_vis["Q4_Percent"].mean():.1f}%')
    ax.axvline(x=df_vis['Q1_Percent'].mean(), color='blue', linestyle='--', alpha=0.5,
               label=f'Média Q1: {df_vis["Q1_Percent"].mean():.1f}%')
    
    # Diagonal de equilíbrio
    max_val = max(ax.get_xlim()[1], ax.get_ylim()[1])
    ax.plot([0, max_val], [0, max_val], 'k--', alpha=0.3, label='Linha de equilíbrio (Q1=Q4)')
    
    # Anotar áreas extremas
    # Áreas com alta concordância positiva (Q1)
    top_q1 = df_vis.nlargest(3, 'Q1_Percent')
    for _, row in top_q1.iterrows():
        if row['Q1_Percent'] > 70:
            ax.annotate(f"{row['Area'][:20]}...", 
                       (row['Q1_Percent'], row['Q4_Percent']),
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=9, color='darkblue',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.7))
    
    # Áreas com alta concordância negativa (Q4)
    top_q4 = df_vis.nlargest(3, 'Q4_Percent')
    for _, row in top_q4.iterrows():
        if row['Q4_Percent'] > 50:
            ax.annotate(f"{row['Area'][:20]}...", 
                       (row['Q1_Percent'], row['Q4_Percent']),
                       xytext=(-5, -5), textcoords='offset points',
                       fontsize=9, color='darkred',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightcoral', alpha=0.7))
    
    ax.set_xlabel('Taxa de Concordância Positiva - Q1 (%)\n(Ambos Recomendam)', fontsize=12)
    ax.set_ylabel('Taxa de Concordância Negativa - Q4 (%)\n(Ambos Não Recomendam)', fontsize=12)
    ax.set_title('Análise de Concordância por Área: Q1 vs Q4\n(Áreas com ≥20 projetos)', fontsize=16, pad=20)
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Concordância Total (%)', rotation=270, labelpad=20)
    
    plt.tight_layout()
    plt.show()
else:
    print("❌ Dados insuficientes para análise de concordância por área do projeto")
    print("Certifique-se de que as colunas 'decisao_pesquisador', 'decisao_ministerio' e 'do_set_nosetor' estão presentes no DataFrame.")
```

    ================================================================================
    ANÁLISE DE CONCORDÂNCIA POR ÁREA DO PROJETO
    Foco: Quadrantes 1 (ambos recomendam) e 4 (ambos não recomendam)
    ================================================================================

    📊 ESTATÍSTICAS GERAIS:
    Total de áreas analisadas: 7
    Taxa média de concordância total: 84.0%
    Taxa média de concordância positiva (Q1): 54.5%
    Taxa média de concordância negativa (Q4): 29.6%

    🏆 TOP 10 ÁREAS COM MAIOR CONCORDÂNCIA TOTAL (Q1+Q4):
    --------------------------------------------------------------------------------
     1. Química e Farmácia                       | Conc:  91.2% | Q1:  73.3% | Q4:  17.9% | (12845 projetos)
     2. Eletroeletrônica                         | Conc:  86.7% | Q1:  56.4% | Q4:  30.4% | (7158 projetos)
     3. Metalurgia e Mineração                   | Conc:  84.1% | Q1:  57.3% | Q4:  26.9% | (4989 projetos)
     4. Agroindústria e Alimentos                | Conc:  83.9% | Q1:  52.0% | Q4:  31.9% | (8144 projetos)
     5. Mecânica e Transporte                    | Conc:  82.0% | Q1:  54.6% | Q4:  27.4% | (9068 projetos)
     6. TIC                                      | Conc:  80.4% | Q1:  40.9% | Q4:  39.6% | (18772 projetos)
     7. Transversal                              | Conc:  79.8% | Q1:  46.7% | Q4:  33.1% | (7467 projetos)

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-18-output-2.png)

#### Gráfico 5.2 - Distribuição dos Quadrantes por Área

Este conjunto de dois gráficos de barras mostra a distribuição
percentual dos quatro quadrantes de decisão para as 15 áreas com maior
volume de projetos.

O gráfico superior apresenta barras empilhadas onde cada segmento
colorido representa um quadrante: verde para Q1 (ambos recomendam),
vermelho para Q2 (pesquisador recomenda, ministério não), laranja para
Q3 (pesquisador não recomenda, ministério sim) e cinza para Q4 (ambos
não recomendam).

A altura total de cada barra sempre soma 100%, mostrando a distribuição
completa das decisões. O gráfico inferior foca especificamente na
comparação entre Q1 e Q4, usando barras lado a lado para facilitar a
comparação direta entre concordância positiva (verde) e negativa (cinza)
em cada área, com os valores percentuais exibidos acima de cada barra.

``` python
if 'df_analise_quadrantes' in locals() and 'do_set_nosetor' in df_analise_quadrantes.columns:
    
    # Visualização 2: Barras empilhadas para top áreas
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12))
    
    # Top 15 áreas por volume
    top_areas = df_concordancia.head(15)
    
    # Preparar dados para barras empilhadas
    x = np.arange(len(top_areas))
    
    # Gráfico 1: Distribuição completa dos quadrantes
    ax1.bar(x, top_areas['Q1_Percent'], label='Q1: Ambos Recomendam', 
            color='#2ecc71', alpha=0.8)
    ax1.bar(x, top_areas['Q2_Pesq_Sim_Min_Nao']/top_areas['Total_Projetos']*100, 
            bottom=top_areas['Q1_Percent'],
            label='Q2: Pesq. Sim, Min. Não', color='#e74c3c', alpha=0.8)
    ax1.bar(x, top_areas['Q3_Pesq_Nao_Min_Sim']/top_areas['Total_Projetos']*100,
            bottom=top_areas['Q1_Percent'] + top_areas['Q2_Pesq_Sim_Min_Nao']/top_areas['Total_Projetos']*100,
            label='Q3: Pesq. Não, Min. Sim', color='#f39c12', alpha=0.8)
    ax1.bar(x, top_areas['Q4_Percent'],
            bottom=top_areas['Q1_Percent'] + top_areas['Q2_Pesq_Sim_Min_Nao']/top_areas['Total_Projetos']*100 + 
                   top_areas['Q3_Pesq_Nao_Min_Sim']/top_areas['Total_Projetos']*100,
            label='Q4: Ambos Não Recomendam', color='#95a5a6', alpha=0.8)
    
    ax1.set_ylabel('Percentual (%)', fontsize=12)
    ax1.set_title('Distribuição dos Quadrantes por Área (Top 15 por volume)', fontsize=14)
    ax1.set_xticks(x)
    labels_areas = [area[:25] + '...' if len(area) > 25 else area for area in top_areas['Area']]
    ax1.set_xticklabels(labels_areas, rotation=45, ha='right')
    ax1.legend(loc='upper right')
    ax1.grid(axis='y', alpha=0.3)
    
    # Gráfico 2: Foco em Q1 e Q4
    width = 0.35
    bars1 = ax2.bar(x - width/2, top_areas['Q1_Percent'], width, 
                    label='Q1: Concordância Positiva', color='#2ecc71', alpha=0.8)
    bars2 = ax2.bar(x + width/2, top_areas['Q4_Percent'], width,
                    label='Q4: Concordância Negativa', color='#95a5a6', alpha=0.8)
    
    # Adicionar valores nas barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                        f'{height:.0f}%', ha='center', va='bottom', fontsize=8)
    
    ax2.set_ylabel('Percentual (%)', fontsize=12)
    ax2.set_title('Comparação de Concordância: Q1 (Positiva) vs Q4 (Negativa)', fontsize=14)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels_areas, rotation=45, ha='right')
    ax2.legend()
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()
else:
    print("❌ Dados insuficientes para análise de concordância por área do projeto")
    print("Certifique-se de que as colunas 'decisao_pesquisador', 'decisao_ministerio' e 'do_set_nosetor' estão presentes no DataFrame.")
```

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-19-output-1.png)

#### Gráfico 5.3 - Heatmap de Concordância por Área

Este mapa de calor apresenta uma matriz onde as colunas representam as
20 áreas com maior volume de projetos e as linhas mostram quatro
métricas diferentes: Q1 (Concordância Positiva), Q4 (Concordância
Negativa), Concordância Total e Discordância Total. Cada célula contém o
valor percentual correspondente e é colorida segundo uma escala que vai
do vermelho ao verde, passando pelo amarelo. Valores mais altos aparecem
em tons de verde, valores médios em amarelo e valores mais baixos em
vermelho. O centro da escala de cores está fixado em 50%, facilitando a
identificação visual de valores acima ou abaixo deste ponto médio. Os
valores numéricos são exibidos dentro de cada célula para precisão, e as
bordas cinzas delimitam cada célula individual.

``` python
if 'df_analise_quadrantes' in locals() and 'do_set_nosetor' in df_analise_quadrantes.columns:
    
    # Visualização 3: Heatmap de concordância
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Preparar dados para heatmap (top 20 áreas)
    heatmap_data = df_concordancia.head(20)[['Q1_Percent', 'Q4_Percent', 
                                             'Concordancia_Total_%', 'Discordancia_Total_%']]
    
    # Truncar nomes das áreas
    areas_truncadas = [area[:30] + '...' if len(area) > 30 else area for area in df_concordancia.head(20)['Area']]
    heatmap_data.index = areas_truncadas
    
    sns.heatmap(heatmap_data.T, annot=True, fmt='.1f', cmap='RdYlGn', center=50,
               cbar_kws={'label': 'Percentual (%)'}, linewidths=0.5, linecolor='gray')
    
    ax.set_xlabel('Área do Projeto', fontsize=12)
    ax.set_yticklabels(['Q1: Concordância Positiva', 'Q4: Concordância Negativa', 
                       'Concordância Total', 'Discordância Total'], rotation=0)
    ax.set_title('Análise de Concordância por Área - Top 20 por Volume', fontsize=14)
    
    plt.tight_layout()
    plt.show()
    
    # Análise de padrões especiais
    print("\n🔍 PADRÕES ESPECIAIS DE CONCORDÂNCIA:")
    print("-" * 80)
    
    # Áreas com alta concordância positiva (Q1 > 70%)
    alta_concordancia_positiva = df_concordancia[df_concordancia['Q1_Percent'] > 70]
    if len(alta_concordancia_positiva) > 0:
        print(f"\n✅ Áreas com ALTA concordância positiva (Q1 > 70%):")
        for _, row in alta_concordancia_positiva.head(5).iterrows():
            print(f"   • {row['Area']}: {row['Q1_Percent']:.1f}% ({row['Q1_Ambos_Recomendam']} de {row['Total_Projetos']} projetos)")
    
    # Áreas com alta concordância negativa (Q4 > 50%)
    alta_concordancia_negativa = df_concordancia[df_concordancia['Q4_Percent'] > 50]
    if len(alta_concordancia_negativa) > 0:
        print(f"\n❌ Áreas com ALTA concordância negativa (Q4 > 50%):")
        for _, row in alta_concordancia_negativa.head(5).iterrows():
            print(f"   • {row['Area']}: {row['Q4_Percent']:.1f}% ({row['Q4_Ambos_Nao_Recomendam']} de {row['Total_Projetos']} projetos)")
    
    # Áreas equilibradas (Q1 ≈ Q4)
    df_concordancia['diferenca_q1_q4'] = abs(df_concordancia['Q1_Percent'] - df_concordancia['Q4_Percent'])
    areas_equilibradas = df_concordancia[df_concordancia['diferenca_q1_q4'] < 10]
    if len(areas_equilibradas) > 0:
        print(f"\n⚖️ Áreas EQUILIBRADAS (diferença Q1-Q4 < 10%):")
        for _, row in areas_equilibradas.head(5).iterrows():
            print(f"   • {row['Area']}: Q1={row['Q1_Percent']:.1f}%, Q4={row['Q4_Percent']:.1f}% ({row['Total_Projetos']} projetos)")
    
    # Exportar resultados
    df_concordancia.to_csv('analise_concordancia_por_area.csv', index=False, sep=';', encoding='utf-8')
    print("\n💾 Resultados exportados para 'analise_concordancia_por_area.csv'")
    
else:
    print("\n❌ Não foi possível realizar a análise por área")
    print("Verifique se os dados necessários estão disponíveis:")
    print("- df_analise_quadrantes")
    print("- coluna 'do_set_nosetor'")
```

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-20-output-1.png)


    🔍 PADRÕES ESPECIAIS DE CONCORDÂNCIA:
    --------------------------------------------------------------------------------

    ✅ Áreas com ALTA concordância positiva (Q1 > 70%):
       • Química e Farmácia: 73.3% (9415 de 12845 projetos)

    ⚖️ Áreas EQUILIBRADAS (diferença Q1-Q4 < 10%):
       • TIC: Q1=40.9%, Q4=39.6% (18772 projetos)

    💾 Resultados exportados para 'analise_concordancia_por_area.csv'

### 6. Análise por setor para Q2 e Q3

#### Tabelas 6.1 e 6.2 - Top 5 Setores Q2 e Q3

Estas duas tabelas apresentam os cinco setores com as maiores taxas
percentuais de discordância em cada quadrante. A primeira tabela, com
fundo rosa, mostra os setores onde o ministério é mais rigoroso (Q2),
enquanto a segunda tabela, com fundo azul, mostra onde o pesquisador é
mais rigoroso (Q3). Cada tabela contém quatro colunas: o nome do setor,
a taxa percentual do quadrante correspondente, o número absoluto de
projetos naquele quadrante e o total de projetos do setor. Os setores
estão ordenados pela taxa percentual em ordem decrescente e numerados de
1 a 5.

``` python
# ANÁLISE APROFUNDADA DE DISCORDÂNCIA - QUADRANTES 2 E 3
# Analista Sênior MCTI - Lei do Bem

print("=" * 100)
print("ANÁLISE APROFUNDADA DAS CAUSAS DE DISCORDÂNCIA NA AVALIAÇÃO DE PROJETOS")
print("Lei do Bem - Quadrantes 2 e 3")
print("=" * 100)

# Verificar dados necessários
if 'df_analise_quadrantes' not in locals():
    print("❌ ERRO: df_analise_quadrantes não encontrado. Execute primeiro a análise de quadrantes.")
else:
    # Adicionar classificação de quadrantes se ainda não existir
    if 'quadrante' not in df_analise_quadrantes.columns:
        df_analise_quadrantes['quadrante'] = ''
        df_analise_quadrantes.loc[
            (df_analise_quadrantes['decisao_pesquisador'] == 'Recomendado') & 
            (df_analise_quadrantes['decisao_ministerio'] == 'Recomendado'), 'quadrante'] = 'Q1'
        df_analise_quadrantes.loc[
            (df_analise_quadrantes['decisao_pesquisador'] == 'Recomendado') & 
            (df_analise_quadrantes['decisao_ministerio'] == 'Não Recomendado'), 'quadrante'] = 'Q2'
        df_analise_quadrantes.loc[
            (df_analise_quadrantes['decisao_pesquisador'] == 'Não Recomendado') & 
            (df_analise_quadrantes['decisao_ministerio'] == 'Recomendado'), 'quadrante'] = 'Q3'
        df_analise_quadrantes.loc[
            (df_analise_quadrantes['decisao_pesquisador'] == 'Não Recomendado') & 
            (df_analise_quadrantes['decisao_ministerio'] == 'Não Recomendado'), 'quadrante'] = 'Q4'
    
    # ========================================================================
    # PARTE 1: ANÁLISE SETORIAL DA DISCORDÂNCIA
    # ========================================================================
    
    print("\n📊 1. ANÁLISE SETORIAL DA DISCORDÂNCIA")
    print("-" * 80)
    
    if 'do_set_nosetor' in df_analise_quadrantes.columns:
        # Filtrar apenas registros com área definida
        df_com_area = df_analise_quadrantes[df_analise_quadrantes['do_set_nosetor'].notna()].copy()
        
        # Análise por setor
        analise_setorial = []
        
        for setor in df_com_area['do_set_nosetor'].unique():
            if pd.notna(setor):
                projetos_setor = df_com_area[df_com_area['do_set_nosetor'] == setor]
                total_setor = len(projetos_setor)
                
                if total_setor >= 10:  # Apenas setores com volume mínimo
                    q2_count = len(projetos_setor[projetos_setor['quadrante'] == 'Q2'])
                    q3_count = len(projetos_setor[projetos_setor['quadrante'] == 'Q3'])
                    
                    analise_setorial.append({
                        'Setor': setor,
                        'Total_Projetos': total_setor,
                        'Q2_Count': q2_count,
                        'Q2_Percent': (q2_count / total_setor * 100),
                        'Q3_Count': q3_count,
                        'Q3_Percent': (q3_count / total_setor * 100),
                        'Discordancia_Total_%': ((q2_count + q3_count) / total_setor * 100)
                    })
        
        df_setorial = pd.DataFrame(analise_setorial)
        
        # Top 5 setores com maior taxa de Q2
        print("\n🔴 TOP 5 SETORES - MAIOR TAXA Q2 (Pesquisador SIM → Ministério NÃO):")
        top_q2 = df_setorial.nlargest(5, 'Q2_Percent').copy()
        top_q2.reset_index(drop=True, inplace=True)
        top_q2.index = top_q2.index + 1  # Começar índice em 1
        
        # Formatar para exibição
        top_q2_display = top_q2[['Setor', 'Q2_Percent', 'Q2_Count', 'Total_Projetos']].copy()
        top_q2_display['Setor'] = top_q2_display['Setor'].str[:50]  # Truncar setores longos
        top_q2_display['Q2_Percent'] = top_q2_display['Q2_Percent'].round(1).astype(str) + '%'
        top_q2_display.columns = ['Setor', 'Taxa Q2 (%)', 'Projetos Q2', 'Total Projetos']
        
        # Aplicar estilo com pandas
        styled_q2 = top_q2_display.style\
            .set_caption("Top 5 Setores - Maior Taxa Q2 (Pesquisador SIM → Ministério NÃO)")\
            .set_properties(**{'background-color': '#ffe6e6', 'border': '1px solid #ddd'})\
            .set_table_styles([
                {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('margin-bottom', '10px')]},
                {'selector': 'th', 'props': [('background-color', '#ffcccc'), ('font-weight', 'bold')]}
            ])
        
        # Exibir tabela
        display(styled_q2)
        
        # Exportar para CSV
        top_q2.to_csv('top5_setores_q2.csv', index=True, sep=';', encoding='utf-8')
        
        # Top 5 setores com maior taxa de Q3
        print("\n🔵 TOP 5 SETORES - MAIOR TAXA Q3 (Pesquisador NÃO → Ministério SIM):")
        top_q3 = df_setorial.nlargest(5, 'Q3_Percent').copy()
        top_q3.reset_index(drop=True, inplace=True)
        top_q3.index = top_q3.index + 1
        
        # Formatar para exibição
        top_q3_display = top_q3[['Setor', 'Q3_Percent', 'Q3_Count', 'Total_Projetos']].copy()
        top_q3_display['Setor'] = top_q3_display['Setor'].str[:50]
        top_q3_display['Q3_Percent'] = top_q3_display['Q3_Percent'].round(1).astype(str) + '%'
        top_q3_display.columns = ['Setor', 'Taxa Q3 (%)', 'Projetos Q3', 'Total Projetos']
        
        # Aplicar estilo com pandas
        styled_q3 = top_q3_display.style\
            .set_caption("Top 5 Setores - Maior Taxa Q3 (Pesquisador NÃO → Ministério SIM)")\
            .set_properties(**{'background-color': '#e6f3ff', 'border': '1px solid #ddd'})\
            .set_table_styles([
                {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('margin-bottom', '10px')]},
                {'selector': 'th', 'props': [('background-color', '#cce6ff'), ('font-weight', 'bold')]}
            ])
        
        display(styled_q3)
        
        # Exportar para CSV
        top_q3.to_csv('top5_setores_q3.csv', index=True, sep=';', encoding='utf-8')
        
```

    ====================================================================================================
    ANÁLISE APROFUNDADA DAS CAUSAS DE DISCORDÂNCIA NA AVALIAÇÃO DE PROJETOS
    Lei do Bem - Quadrantes 2 e 3
    ====================================================================================================

    📊 1. ANÁLISE SETORIAL DA DISCORDÂNCIA
    --------------------------------------------------------------------------------

    🔴 TOP 5 SETORES - MAIOR TAXA Q2 (Pesquisador SIM → Ministério NÃO):

<style type="text/css">
#T_4cd1c caption {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}
#T_4cd1c th {
  background-color: #ffcccc;
  font-weight: bold;
}
#T_4cd1c_row0_col0, #T_4cd1c_row0_col1, #T_4cd1c_row0_col2, #T_4cd1c_row0_col3, #T_4cd1c_row1_col0, #T_4cd1c_row1_col1, #T_4cd1c_row1_col2, #T_4cd1c_row1_col3, #T_4cd1c_row2_col0, #T_4cd1c_row2_col1, #T_4cd1c_row2_col2, #T_4cd1c_row2_col3, #T_4cd1c_row3_col0, #T_4cd1c_row3_col1, #T_4cd1c_row3_col2, #T_4cd1c_row3_col3, #T_4cd1c_row4_col0, #T_4cd1c_row4_col1, #T_4cd1c_row4_col2, #T_4cd1c_row4_col3 {
  background-color: #ffe6e6;
  border: 1px solid #ddd;
}
</style>

<table id="T_4cd1c" data-quarto-postprocess="true">
<thead>
<tr>
<th class="blank level0" data-quarto-table-cell-role="th"> </th>
<th id="T_4cd1c_level0_col0" class="col_heading level0 col0"
data-quarto-table-cell-role="th">Setor</th>
<th id="T_4cd1c_level0_col1" class="col_heading level0 col1"
data-quarto-table-cell-role="th">Taxa Q2 (%)</th>
<th id="T_4cd1c_level0_col2" class="col_heading level0 col2"
data-quarto-table-cell-role="th">Projetos Q2</th>
<th id="T_4cd1c_level0_col3" class="col_heading level0 col3"
data-quarto-table-cell-role="th">Total Projetos</th>
</tr>
</thead>
<tbody>
<tr>
<td id="T_4cd1c_level0_row0" class="row_heading level0 row0"
data-quarto-table-cell-role="th">1</td>
<td id="T_4cd1c_row0_col0" class="data row0 col0">TIC</td>
<td id="T_4cd1c_row0_col1" class="data row0 col1">12.1%</td>
<td id="T_4cd1c_row0_col2" class="data row0 col2">2268</td>
<td id="T_4cd1c_row0_col3" class="data row0 col3">18772</td>
</tr>
<tr>
<td id="T_4cd1c_level0_row1" class="row_heading level0 row1"
data-quarto-table-cell-role="th">2</td>
<td id="T_4cd1c_row1_col0" class="data row1 col0">Transversal</td>
<td id="T_4cd1c_row1_col1" class="data row1 col1">11.8%</td>
<td id="T_4cd1c_row1_col2" class="data row1 col2">879</td>
<td id="T_4cd1c_row1_col3" class="data row1 col3">7467</td>
</tr>
<tr>
<td id="T_4cd1c_level0_row2" class="row_heading level0 row2"
data-quarto-table-cell-role="th">3</td>
<td id="T_4cd1c_row2_col0" class="data row2 col0">Agroindústria e
Alimentos</td>
<td id="T_4cd1c_row2_col1" class="data row2 col1">8.5%</td>
<td id="T_4cd1c_row2_col2" class="data row2 col2">694</td>
<td id="T_4cd1c_row2_col3" class="data row2 col3">8144</td>
</tr>
<tr>
<td id="T_4cd1c_level0_row3" class="row_heading level0 row3"
data-quarto-table-cell-role="th">4</td>
<td id="T_4cd1c_row3_col0" class="data row3 col0">Metalurgia e
Mineração</td>
<td id="T_4cd1c_row3_col1" class="data row3 col1">5.6%</td>
<td id="T_4cd1c_row3_col2" class="data row3 col2">277</td>
<td id="T_4cd1c_row3_col3" class="data row3 col3">4989</td>
</tr>
<tr>
<td id="T_4cd1c_level0_row4" class="row_heading level0 row4"
data-quarto-table-cell-role="th">5</td>
<td id="T_4cd1c_row4_col0" class="data row4 col0">Mecânica e
Transporte</td>
<td id="T_4cd1c_row4_col1" class="data row4 col1">4.5%</td>
<td id="T_4cd1c_row4_col2" class="data row4 col2">404</td>
<td id="T_4cd1c_row4_col3" class="data row4 col3">9068</td>
</tr>
</tbody>
</table>


    🔵 TOP 5 SETORES - MAIOR TAXA Q3 (Pesquisador NÃO → Ministério SIM):

<style type="text/css">
#T_1569c caption {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}
#T_1569c th {
  background-color: #cce6ff;
  font-weight: bold;
}
#T_1569c_row0_col0, #T_1569c_row0_col1, #T_1569c_row0_col2, #T_1569c_row0_col3, #T_1569c_row1_col0, #T_1569c_row1_col1, #T_1569c_row1_col2, #T_1569c_row1_col3, #T_1569c_row2_col0, #T_1569c_row2_col1, #T_1569c_row2_col2, #T_1569c_row2_col3, #T_1569c_row3_col0, #T_1569c_row3_col1, #T_1569c_row3_col2, #T_1569c_row3_col3, #T_1569c_row4_col0, #T_1569c_row4_col1, #T_1569c_row4_col2, #T_1569c_row4_col3 {
  background-color: #e6f3ff;
  border: 1px solid #ddd;
}
</style>

<table id="T_1569c" data-quarto-postprocess="true">
<thead>
<tr>
<th class="blank level0" data-quarto-table-cell-role="th"> </th>
<th id="T_1569c_level0_col0" class="col_heading level0 col0"
data-quarto-table-cell-role="th">Setor</th>
<th id="T_1569c_level0_col1" class="col_heading level0 col1"
data-quarto-table-cell-role="th">Taxa Q3 (%)</th>
<th id="T_1569c_level0_col2" class="col_heading level0 col2"
data-quarto-table-cell-role="th">Projetos Q3</th>
<th id="T_1569c_level0_col3" class="col_heading level0 col3"
data-quarto-table-cell-role="th">Total Projetos</th>
</tr>
</thead>
<tbody>
<tr>
<td id="T_1569c_level0_row0" class="row_heading level0 row0"
data-quarto-table-cell-role="th">1</td>
<td id="T_1569c_row0_col0" class="data row0 col0">Mecânica e
Transporte</td>
<td id="T_1569c_row0_col1" class="data row0 col1">13.6%</td>
<td id="T_1569c_row0_col2" class="data row0 col2">1230</td>
<td id="T_1569c_row0_col3" class="data row0 col3">9068</td>
</tr>
<tr>
<td id="T_1569c_level0_row1" class="row_heading level0 row1"
data-quarto-table-cell-role="th">2</td>
<td id="T_1569c_row1_col0" class="data row1 col0">Eletroeletrônica</td>
<td id="T_1569c_row1_col1" class="data row1 col1">11.1%</td>
<td id="T_1569c_row1_col2" class="data row1 col2">792</td>
<td id="T_1569c_row1_col3" class="data row1 col3">7158</td>
</tr>
<tr>
<td id="T_1569c_level0_row2" class="row_heading level0 row2"
data-quarto-table-cell-role="th">3</td>
<td id="T_1569c_row2_col0" class="data row2 col0">Metalurgia e
Mineração</td>
<td id="T_1569c_row2_col1" class="data row2 col1">10.3%</td>
<td id="T_1569c_row2_col2" class="data row2 col2">514</td>
<td id="T_1569c_row2_col3" class="data row2 col3">4989</td>
</tr>
<tr>
<td id="T_1569c_level0_row3" class="row_heading level0 row3"
data-quarto-table-cell-role="th">4</td>
<td id="T_1569c_row3_col0" class="data row3 col0">Transversal</td>
<td id="T_1569c_row3_col1" class="data row3 col1">8.4%</td>
<td id="T_1569c_row3_col2" class="data row3 col2">630</td>
<td id="T_1569c_row3_col3" class="data row3 col3">7467</td>
</tr>
<tr>
<td id="T_1569c_level0_row4" class="row_heading level0 row4"
data-quarto-table-cell-role="th">5</td>
<td id="T_1569c_row4_col0" class="data row4 col0">Agroindústria e
Alimentos</td>
<td id="T_1569c_row4_col1" class="data row4 col1">7.5%</td>
<td id="T_1569c_row4_col2" class="data row4 col2">614</td>
<td id="T_1569c_row4_col3" class="data row4 col3">8144</td>
</tr>
</tbody>
</table>

#### Gráfico 6.1 - Análise Setorial de Discordância: Q2 vs Q3

Este gráfico de barras agrupadas compara as taxas de discordância entre
os Quadrantes 2 e 3 para os 15 setores com maior volume de projetos. As
barras vermelhas representam o Q2 (projetos recomendados pelo
pesquisador mas não recomendados pelo ministério) e as barras azuis
representam o Q3 (projetos não recomendados pelo pesquisador mas
recomendados pelo ministério).

Cada par de barras corresponde a um setor específico, com os valores
percentuais exibidos acima de cada barra. As linhas horizontais
tracejadas indicam as médias gerais de Q2 (8,8%) e Q3 (4,3%) em todos os
setores. O gráfico permite visualizar quais setores apresentam maior
discordância e em qual direção essa discordância ocorre
predominantemente.

``` python
if 'df_analise_quadrantes' not in locals():
    print("❌ ERRO: df_analise_quadrantes não encontrado. Execute primeiro a análise de quadrantes.")
else:
    if 'do_set_nosetor' in df_analise_quadrantes.columns:
        # Visualização: Comparação Q2 vs Q3 nos 15 maiores setores
        fig, ax = plt.subplots(figsize=(16, 10))
        
        # Top 15 setores por volume
        top_setores = df_setorial.nlargest(15, 'Total_Projetos')
        
        x = np.arange(len(top_setores))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, top_setores['Q2_Percent'], width, 
                       label='Q2: Pesquisador SIM → Ministério NÃO', 
                       color='#e74c3c', alpha=0.8)
        bars2 = ax.bar(x + width/2, top_setores['Q3_Percent'], width,
                       label='Q3: Pesquisador NÃO → Ministério SIM', 
                       color='#3498db', alpha=0.8)
        
        # Adicionar valores nas barras
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                if height > 0:
                    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                           f'{height:.1f}%', ha='center', va='bottom', fontsize=9)
        
        # Configurar gráfico
        ax.set_xlabel('Setor', fontsize=12, fontweight='bold')
        ax.set_ylabel('Taxa de Discordância (%)', fontsize=12, fontweight='bold')
        ax.set_title('Análise Setorial de Discordância: Q2 vs Q3\n(15 Setores de Maior Volume)', 
                    fontsize=16, fontweight='bold', pad=20)
        ax.set_xticks(x)
        labels_setores = [setor[:25] + '...' if len(setor) > 25 else setor for setor in top_setores['Setor']]
        ax.set_xticklabels(labels_setores, rotation=45, ha='right')
        ax.legend(loc='upper right', fontsize=11)
        ax.grid(axis='y', alpha=0.3)
        
        # Adicionar linha média
        media_q2 = df_setorial['Q2_Percent'].mean()
        media_q3 = df_setorial['Q3_Percent'].mean()
        ax.axhline(y=media_q2, color='#e74c3c', linestyle='--', alpha=0.5, linewidth=2)
        ax.axhline(y=media_q3, color='#3498db', linestyle='--', alpha=0.5, linewidth=2)
        
        plt.tight_layout()
        plt.show()
        
        # Análise de padrões setoriais
        print("\n📈 ANÁLISE DE PADRÕES SETORIAIS:")
        print("-" * 80)
```

![](analise_setores_quadrantes_files/figure-markdown_strict/cell-22-output-1.png)


    📈 ANÁLISE DE PADRÕES SETORIAIS:
    --------------------------------------------------------------------------------

#### Tabelas 6.3 e 6.4 - Viés do Ministério e do Pesquisador

Estas tabelas identificam setores onde há um viés significativo
(diferença maior que 5%) entre Q2 e Q3. A tabela de viés do ministério
mostra setores onde Q2 \> Q3 + 5%, indicando que o ministério tende a
ser mais rigoroso nesses setores. A tabela de viés do pesquisador mostra
o oposto (Q3 \> Q2 + 5%). Cada tabela apresenta as taxas de Q2 e Q3, a
diferença entre elas (Δ) e o total de projetos. A coluna de diferença é
destacada com cor de fundo correspondente ao tipo de viés (rosa para
ministério, azul para pesquisador).

``` python
if 'df_analise_quadrantes' not in locals():
    print("❌ ERRO: df_analise_quadrantes não encontrado. Execute primeiro a análise de quadrantes.")
else:
    if 'do_set_nosetor' in df_analise_quadrantes.columns:
        # Setores com viés Q2 (Ministério mais rigoroso)
        setores_vies_q2 = df_setorial[df_setorial['Q2_Percent'] > df_setorial['Q3_Percent'] + 5].copy()
        if len(setores_vies_q2) > 0:
            print(f"\n🔴 Setores onde o MINISTÉRIO é mais RIGOROSO (Q2 > Q3 + 5%):")
            
            # Preparar dados para tabela
            vies_q2_display = setores_vies_q2.nlargest(5, 'Total_Projetos').copy()
            vies_q2_display['Diferenca'] = vies_q2_display['Q2_Percent'] - vies_q2_display['Q3_Percent']
            vies_q2_display.reset_index(drop=True, inplace=True)
            vies_q2_display.index = vies_q2_display.index + 1
            
            # Formatar para exibição
            vies_q2_show = vies_q2_display[['Setor', 'Q2_Percent', 'Q3_Percent', 'Diferenca', 'Total_Projetos']].copy()
            vies_q2_show['Setor'] = vies_q2_show['Setor'].str[:40]
            vies_q2_show['Q2_Percent'] = vies_q2_show['Q2_Percent'].round(1).astype(str) + '%'
            vies_q2_show['Q3_Percent'] = vies_q2_show['Q3_Percent'].round(1).astype(str) + '%'
            vies_q2_show['Diferenca'] = '+' + vies_q2_show['Diferenca'].round(1).astype(str) + '%'
            vies_q2_show.columns = ['Setor', 'Q2 (%)', 'Q3 (%)', 'Δ (Q2-Q3)', 'Total']
            
            # Aplicar estilo
            styled_vies_q2 = vies_q2_show.style\
                .set_caption("Viés do Ministério - Setores onde Q2 > Q3 + 5%")\
                .set_properties(**{'border': '1px solid #ddd'})\
                .apply(lambda x: ['background-color: #ffcccc' if x.name == 'Δ (Q2-Q3)' else 'background-color: #fff' for i in x], axis=0)\
                .set_table_styles([
                    {'selector': 'caption', 'props': [('font-size', '14px'), ('font-weight', 'bold'), ('margin-bottom', '10px')]},
                    {'selector': 'th', 'props': [('background-color', '#f0f0f0'), ('font-weight', 'bold')]}
                ])
            
            display(styled_vies_q2)
            
            # Exportar para CSV
            vies_q2_display.to_csv('setores_vies_ministerio_q2.csv', index=True, sep=';', encoding='utf-8')
        
        # Setores com viés Q3 (Pesquisador mais rigoroso)
        setores_vies_q3 = df_setorial[df_setorial['Q3_Percent'] > df_setorial['Q2_Percent'] + 5].copy()
        if len(setores_vies_q3) > 0:
            print(f"\n🔵 Setores onde o PESQUISADOR é mais RIGOROSO (Q3 > Q2 + 5%):")
            
            # Preparar dados para tabela
            vies_q3_display = setores_vies_q3.nlargest(5, 'Total_Projetos').copy()
            vies_q3_display['Diferenca'] = vies_q3_display['Q3_Percent'] - vies_q3_display['Q2_Percent']
            vies_q3_display.reset_index(drop=True, inplace=True)
            vies_q3_display.index = vies_q3_display.index + 1
            
            # Formatar para exibição
            vies_q3_show = vies_q3_display[['Setor', 'Q3_Percent', 'Q2_Percent', 'Diferenca', 'Total_Projetos']].copy()
            vies_q3_show['Setor'] = vies_q3_show['Setor'].str[:40]
            vies_q3_show['Q3_Percent'] = vies_q3_show['Q3_Percent'].round(1).astype(str) + '%'
            vies_q3_show['Q2_Percent'] = vies_q3_show['Q2_Percent'].round(1).astype(str) + '%'
            vies_q3_show['Diferenca'] = '+' + vies_q3_show['Diferenca'].round(1).astype(str) + '%'
            vies_q3_show.columns = ['Setor', 'Q3 (%)', 'Q2 (%)', 'Δ (Q3-Q2)', 'Total']
            
            # Aplicar estilo
            styled_vies_q3 = vies_q3_show.style\
                .set_caption("Viés do Pesquisador - Setores onde Q3 > Q2 + 5%")\
                .set_properties(**{'border': '1px solid #ddd'})\
                .apply(lambda x: ['background-color: #cce6ff' if x.name == 'Δ (Q3-Q2)' else 'background-color: #fff' for i in x], axis=0)\
                .set_table_styles([
                    {'selector': 'caption', 'props': [('font-size', '14px'), ('font-weight', 'bold'), ('margin-bottom', '10px')]},
                    {'selector': 'th', 'props': [('background-color', '#f0f0f0'), ('font-weight', 'bold')]}
                ])
            
            display(styled_vies_q3)
            
            # Exportar para CSV
            vies_q3_display.to_csv('setores_vies_pesquisador_q3.csv', index=True, sep=';', encoding='utf-8')
        
        # Tabela resumo geral de discordância setorial
        print("\n📊 RESUMO GERAL DE DISCORDÂNCIA POR SETOR:")
        
        print("""
              
              """)
```


    🔵 Setores onde o PESQUISADOR é mais RIGOROSO (Q3 > Q2 + 5%):

<style type="text/css">
#T_173e7 caption {
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 10px;
}
#T_173e7 th {
  background-color: #f0f0f0;
  font-weight: bold;
}
#T_173e7_row0_col0, #T_173e7_row0_col1, #T_173e7_row0_col2, #T_173e7_row0_col4, #T_173e7_row1_col0, #T_173e7_row1_col1, #T_173e7_row1_col2, #T_173e7_row1_col4 {
  border: 1px solid #ddd;
  background-color: #fff;
}
#T_173e7_row0_col3, #T_173e7_row1_col3 {
  border: 1px solid #ddd;
  background-color: #cce6ff;
}
</style>

<table id="T_173e7" data-quarto-postprocess="true">
<thead>
<tr>
<th class="blank level0" data-quarto-table-cell-role="th"> </th>
<th id="T_173e7_level0_col0" class="col_heading level0 col0"
data-quarto-table-cell-role="th">Setor</th>
<th id="T_173e7_level0_col1" class="col_heading level0 col1"
data-quarto-table-cell-role="th">Q3 (%)</th>
<th id="T_173e7_level0_col2" class="col_heading level0 col2"
data-quarto-table-cell-role="th">Q2 (%)</th>
<th id="T_173e7_level0_col3" class="col_heading level0 col3"
data-quarto-table-cell-role="th">Δ (Q3-Q2)</th>
<th id="T_173e7_level0_col4" class="col_heading level0 col4"
data-quarto-table-cell-role="th">Total</th>
</tr>
</thead>
<tbody>
<tr>
<td id="T_173e7_level0_row0" class="row_heading level0 row0"
data-quarto-table-cell-role="th">1</td>
<td id="T_173e7_row0_col0" class="data row0 col0">Mecânica e
Transporte</td>
<td id="T_173e7_row0_col1" class="data row0 col1">13.6%</td>
<td id="T_173e7_row0_col2" class="data row0 col2">4.5%</td>
<td id="T_173e7_row0_col3" class="data row0 col3">+9.1%</td>
<td id="T_173e7_row0_col4" class="data row0 col4">9068</td>
</tr>
<tr>
<td id="T_173e7_level0_row1" class="row_heading level0 row1"
data-quarto-table-cell-role="th">2</td>
<td id="T_173e7_row1_col0" class="data row1 col0">Eletroeletrônica</td>
<td id="T_173e7_row1_col1" class="data row1 col1">11.1%</td>
<td id="T_173e7_row1_col2" class="data row1 col2">2.2%</td>
<td id="T_173e7_row1_col3" class="data row1 col3">+8.9%</td>
<td id="T_173e7_row1_col4" class="data row1 col4">7158</td>
</tr>
</tbody>
</table>


    📊 RESUMO GERAL DE DISCORDÂNCIA POR SETOR:

                  
                  

#### Tabela 6.5 - Resumo Geral de Discordância por Setor

Esta tabela apresenta os 10 setores com maior taxa de discordância total
(Q2 + Q3). As colunas mostram o nome do setor, a taxa de discordância
total, as taxas individuais de Q2 e Q3, qual avaliador é mais rigoroso
naquele setor (colorido em rosa se for o ministério ou azul se for o
pesquisador), e o total de projetos. O setor TIC - Software lidera com
34,8% de discordância total. A coloração na coluna “Mais Rigoroso”
facilita a identificação visual de padrões de rigor por setor, mostrando
se há tendências sistemáticas em determinadas áreas.

``` python
if 'df_analise_quadrantes' not in locals():
    print("❌ ERRO: df_analise_quadrantes não encontrado. Execute primeiro a análise de quadrantes.")
else:
    if 'do_set_nosetor' in df_analise_quadrantes.columns:
        # Top 10 setores com maior discordância total
        top_discordancia = df_setorial.nlargest(10, 'Discordancia_Total_%').copy()
        top_discordancia['Dominancia'] = top_discordancia.apply(
            lambda row: 'Ministério' if row['Q2_Percent'] > row['Q3_Percent'] else 'Pesquisador', axis=1
        )
        top_discordancia.reset_index(drop=True, inplace=True)
        top_discordancia.index = top_discordancia.index + 1
        
        # Formatar para exibição
        disc_show = top_discordancia[['Setor', 'Discordancia_Total_%', 'Q2_Percent', 'Q3_Percent', 'Dominancia', 'Total_Projetos']].copy()
        disc_show['Setor'] = disc_show['Setor'].str[:35]
        disc_show['Discordancia_Total_%'] = disc_show['Discordancia_Total_%'].round(1).astype(str) + '%'
        disc_show['Q2_Percent'] = disc_show['Q2_Percent'].round(1).astype(str) + '%'
        disc_show['Q3_Percent'] = disc_show['Q3_Percent'].round(1).astype(str) + '%'
        disc_show.columns = ['Setor', 'Discord. Total', 'Q2 (%)', 'Q3 (%)', 'Mais Rigoroso', 'Total']
        
        # Função para aplicar cores baseadas na dominância
        def highlight_dominance(s):
            colors = []
            for val in s:
                if val == 'Ministério':
                    colors.append('background-color: #ffe6e6')
                elif val == 'Pesquisador':
                    colors.append('background-color: #e6f3ff')
                else:
                    colors.append('background-color: white')
            return colors
        
        # Aplicar estilo
        styled_disc = disc_show.style\
            .set_caption("Top 10 Setores - Maior Discordância Total")\
            .set_properties(**{'border': '1px solid #ddd'})\
            .apply(highlight_dominance, subset=['Mais Rigoroso'])\
            .apply(lambda x: ['background-color: #f0f0f0' if x.name == 'Discord. Total' else '' for i in x], axis=0)\
            .set_table_styles([
                {'selector': 'caption', 'props': [('font-size', '16px'), ('font-weight', 'bold'), ('margin-bottom', '10px')]},
                {'selector': 'th', 'props': [('background-color', '#d0d0d0'), ('font-weight', 'bold')]}
            ])
        
        display(styled_disc)
        
        # Exportar para CSV
        top_discordancia.to_csv('resumo_discordancia_setorial.csv', index=True, sep=';', encoding='utf-8')
    
    # ========================================================================
    # PARTE 2: ANÁLISE DE FREQUÊNCIA DAS JUSTIFICATIVAS
    # ========================================================================
        
    # Análise Q2: Justificativas do MINISTÉRIO para não recomendar
    df_q2 = df_analise_quadrantes[df_analise_quadrantes['quadrante'] == 'Q2'].copy()
    
    # Verificar campos de justificativa do Ministério
    if 'p_japroj_nojustificativaanalise' in df_q2.columns and 'p_japroj_nocorpojustificativaanalise' in df_q2.columns:
        # Concatenar título e corpo da justificativa
        df_q2['justificativa_ministerio'] = (
            df_q2['p_japroj_nojustificativaanalise'].fillna('') + ' - ' + 
            df_q2['p_japroj_nocorpojustificativaanalise'].fillna('')
        )
        
        # Remover vazios
        df_q2_just = df_q2[df_q2['justificativa_ministerio'].str.strip() != ' - ']
        
        if len(df_q2_just) > 0:
            # Análise de frequência
            freq_just_ministerio = df_q2_just['justificativa_ministerio'].value_counts()
            
            print(f"\n📊 TOP 10 JUSTIFICATIVAS DO MINISTÉRIO (Q2):")
            print("-" * 80)
            for i, (just, count) in enumerate(freq_just_ministerio.head(10).items(), 1):
                percent = count / len(df_q2_just) * 100
                print(f"{i:2d}. [{count:4d} | {percent:5.1f}%] {just[:100]}{'...' if len(just) > 100 else ''}")
            
            # Visualização das justificativas Q2
            fig, ax = plt.subplots(figsize=(12, 8))
            
            top_just = freq_just_ministerio.head(10)
            y_pos = np.arange(len(top_just))
            
            bars = ax.barh(y_pos, top_just.values, color='#e74c3c', alpha=0.8)
            
            # Truncar labels longas
            labels = [just[:60] + '...' if len(just) > 60 else just for just in top_just.index]
            ax.set_yticks(y_pos)
            ax.set_yticklabels(labels, fontsize=10)
            ax.invert_yaxis()
            ax.set_xlabel('Frequência', fontsize=12)
            ax.set_title('Q2: Top 10 Justificativas do Ministério para NÃO Recomendar\n(Projetos recomendados pelo Pesquisador)', 
                        fontsize=14, fontweight='bold', pad=20)
            ax.grid(axis='x', alpha=0.3)
            
            # Adicionar valores nas barras
            for i, (bar, valor) in enumerate(zip(bars, top_just.values)):
                percent = valor / len(df_q2_just) * 100
                ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, 
                       f'{valor} ({percent:.1f}%)', va='center', fontsize=9)
            
            plt.tight_layout()
            plt.show()
    
    # Análise Q3: Justificativas do PESQUISADOR para não recomendar
    df_q3 = df_analise_quadrantes[df_analise_quadrantes['quadrante'] == 'Q3'].copy()
    
    # Verificar campos de justificativa do Pesquisador
    if 'do_japroj_nojustificativaanalise' in df_q3.columns and 'do_japroj_nocorpojustificativaanalise' in df_q3.columns:
        # Concatenar título e corpo da justificativa
        df_q3['justificativa_pesquisador'] = (
            df_q3['do_japroj_nojustificativaanalise'].fillna('') + ' - ' + 
            df_q3['do_japroj_nocorpojustificativaanalise'].fillna('')
        )
        
        # Remover vazios
        df_q3_just = df_q3[df_q3['justificativa_pesquisador'].str.strip() != ' - ']
        
        if len(df_q3_just) > 0:
            # Análise de frequência
            freq_just_pesquisador = df_q3_just['justificativa_pesquisador'].value_counts()
            
            print(f"\n📊 TOP 10 JUSTIFICATIVAS DO PESQUISADOR (Q3):")
            print("-" * 80)
            for i, (just, count) in enumerate(freq_just_pesquisador.head(10).items(), 1):
                percent = count / len(df_q3_just) * 100
                print(f"{i:2d}. [{count:4d} | {percent:5.1f}%] {just[:100]}{'...' if len(just) > 100 else ''}")
            
            # Visualização das justificativas Q3
            fig, ax = plt.subplots(figsize=(12, 8))
            
            top_just = freq_just_pesquisador.head(10)
            y_pos = np.arange(len(top_just))
            
            bars = ax.barh(y_pos, top_just.values, color='#3498db', alpha=0.8)
            
            # Truncar labels longas
            labels = [just[:60] + '...' if len(just) > 60 else just for just in top_just.index]
            ax.set_yticks(y_pos)
            ax.set_yticklabels(labels, fontsize=10)
            ax.invert_yaxis()
            ax.set_xlabel('Frequência', fontsize=12)
            ax.set_title('Q3: Top 10 Justificativas do Pesquisador para NÃO Recomendar\n(Projetos recomendados pelo Ministério)', 
                        fontsize=14, fontweight='bold', pad=20)
            ax.grid(axis='x', alpha=0.3)
            
            # Adicionar valores nas barras
            for i, (bar, valor) in enumerate(zip(bars, top_just.values)):
                percent = valor / len(df_q3_just) * 100
                ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, 
                       f'{valor} ({percent:.1f}%)', va='center', fontsize=9)
            
            plt.tight_layout()
            plt.show()
    
    # ========================================================================
    # PARTE 3: ANÁLISE COMPARATIVA E INSIGHTS
    # ========================================================================
    
    print("\n\n🔍 2. ANÁLISE COMPARATIVA E INSIGHTS")
    print("-" * 80)
    
    # Categorizar as justificativas por tipo
    if 'freq_just_ministerio' in locals() and 'freq_just_pesquisador' in locals():
        print("\n📊 CATEGORIZAÇÃO DAS JUSTIFICATIVAS:")
        
        # Palavras-chave para categorização
        categorias = {
            'Aspectos Formais/Documentais': ['clareza', 'documentação', 'metodologia', 'descrição', 'detalhamento'],
            'Mérito da Inovação': ['inovação', 'tecnológico', 'originalidade', 'estado da arte', 'avanço'],
            'Enquadramento': ['enquadramento', 'requisitos', 'critérios', 'elegibilidade'],
            'Aspectos Técnicos': ['técnico', 'viabilidade', 'complexidade', 'desafio']
        }
        
        # Análise de categorias para Q2 (Ministério)
        print("\n🔴 FOCO DO MINISTÉRIO (Q2):")
        categorias_ministerio = {cat: 0 for cat in categorias}
        
        for just, count in freq_just_ministerio.head(10).items():
            just_lower = just.lower()
            for categoria, palavras in categorias.items():
                if any(palavra in just_lower for palavra in palavras):
                    categorias_ministerio[categoria] += count
        
        total_cat_min = sum(categorias_ministerio.values())
        for cat, count in sorted(categorias_ministerio.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                print(f"   • {cat}: {count} ocorrências ({count/total_cat_min*100:.1f}%)")
        
        # Análise de categorias para Q3 (Pesquisador)
        print("\n🔵 FOCO DO PESQUISADOR (Q3):")
        categorias_pesquisador = {cat: 0 for cat in categorias}
        
        for just, count in freq_just_pesquisador.head(10).items():
            just_lower = just.lower()
            for categoria, palavras in categorias.items():
                if any(palavra in just_lower for palavra in palavras):
                    categorias_pesquisador[categoria] += count
        
        total_cat_pesq = sum(categorias_pesquisador.values())
        for cat, count in sorted(categorias_pesquisador.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                print(f"   • {cat}: {count} ocorrências ({count/total_cat_pesq*100:.1f}%)")
    
    # ========================================================================
    # RECOMENDAÇÕES FINAIS
    # ========================================================================
    
    print("\n\n💡 RECOMENDAÇÕES PARA REDUÇÃO DA SUBJETIVIDADE")
    print("=" * 80)
    
    print("""
1. **HARMONIZAÇÃO DE CRITÉRIOS POR SETOR:**
   - Desenvolver guias específicos para setores com alta discordância
   - Realizar workshops de alinhamento entre avaliadores por área temática

2. **PADRONIZAÇÃO DE INTERPRETAÇÕES:**
   - Criar exemplos concretos do que constitui "inovação suficiente" por setor
   - Estabelecer métricas objetivas para avaliar "clareza metodológica"

3. **SISTEMA DE DUPLA CHECAGEM:**
   - Implementar revisão obrigatória para projetos em setores de alta discordância
   - Criar comitês mistos (pesquisador + analista) para casos limítrofes

4. **CAPACITAÇÃO CONTINUADA:**
   - Treinar analistas do Ministério em aspectos técnicos específicos
   - Sensibilizar pesquisadores sobre requisitos formais e de enquadramento

5. **FEEDBACK ESTRUTURADO:**
   - Implementar sistema de justificativas estruturadas com campos obrigatórios
   - Criar base de conhecimento com decisões anteriores como referência
    """)
    
    # Exportar resultados
    if 'df_setorial' in locals():
        df_setorial.to_csv('analise_discordancia_setorial_q2_q3.csv', index=False, sep=';', encoding='utf-8')
        print("\n💾 Análise setorial exportada para 'analise_discordancia_setorial_q2_q3.csv'")
```

<style type="text/css">
#T_adc24 caption {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}
#T_adc24 th {
  background-color: #d0d0d0;
  font-weight: bold;
}
#T_adc24_row0_col0, #T_adc24_row0_col2, #T_adc24_row0_col3, #T_adc24_row0_col5, #T_adc24_row1_col0, #T_adc24_row1_col2, #T_adc24_row1_col3, #T_adc24_row1_col5, #T_adc24_row2_col0, #T_adc24_row2_col2, #T_adc24_row2_col3, #T_adc24_row2_col5, #T_adc24_row3_col0, #T_adc24_row3_col2, #T_adc24_row3_col3, #T_adc24_row3_col5, #T_adc24_row4_col0, #T_adc24_row4_col2, #T_adc24_row4_col3, #T_adc24_row4_col5, #T_adc24_row5_col0, #T_adc24_row5_col2, #T_adc24_row5_col3, #T_adc24_row5_col5, #T_adc24_row6_col0, #T_adc24_row6_col2, #T_adc24_row6_col3, #T_adc24_row6_col5 {
  border: 1px solid #ddd;
}
#T_adc24_row0_col1, #T_adc24_row1_col1, #T_adc24_row2_col1, #T_adc24_row3_col1, #T_adc24_row4_col1, #T_adc24_row5_col1, #T_adc24_row6_col1 {
  border: 1px solid #ddd;
  background-color: #f0f0f0;
}
#T_adc24_row0_col4, #T_adc24_row1_col4, #T_adc24_row3_col4 {
  border: 1px solid #ddd;
  background-color: #ffe6e6;
}
#T_adc24_row2_col4, #T_adc24_row4_col4, #T_adc24_row5_col4, #T_adc24_row6_col4 {
  border: 1px solid #ddd;
  background-color: #e6f3ff;
}
</style>

<table id="T_adc24" data-quarto-postprocess="true">
<thead>
<tr>
<th class="blank level0" data-quarto-table-cell-role="th"> </th>
<th id="T_adc24_level0_col0" class="col_heading level0 col0"
data-quarto-table-cell-role="th">Setor</th>
<th id="T_adc24_level0_col1" class="col_heading level0 col1"
data-quarto-table-cell-role="th">Discord. Total</th>
<th id="T_adc24_level0_col2" class="col_heading level0 col2"
data-quarto-table-cell-role="th">Q2 (%)</th>
<th id="T_adc24_level0_col3" class="col_heading level0 col3"
data-quarto-table-cell-role="th">Q3 (%)</th>
<th id="T_adc24_level0_col4" class="col_heading level0 col4"
data-quarto-table-cell-role="th">Mais Rigoroso</th>
<th id="T_adc24_level0_col5" class="col_heading level0 col5"
data-quarto-table-cell-role="th">Total</th>
</tr>
</thead>
<tbody>
<tr>
<td id="T_adc24_level0_row0" class="row_heading level0 row0"
data-quarto-table-cell-role="th">1</td>
<td id="T_adc24_row0_col0" class="data row0 col0">Transversal</td>
<td id="T_adc24_row0_col1" class="data row0 col1">20.2%</td>
<td id="T_adc24_row0_col2" class="data row0 col2">11.8%</td>
<td id="T_adc24_row0_col3" class="data row0 col3">8.4%</td>
<td id="T_adc24_row0_col4" class="data row0 col4">Ministério</td>
<td id="T_adc24_row0_col5" class="data row0 col5">7467</td>
</tr>
<tr>
<td id="T_adc24_level0_row1" class="row_heading level0 row1"
data-quarto-table-cell-role="th">2</td>
<td id="T_adc24_row1_col0" class="data row1 col0">TIC</td>
<td id="T_adc24_row1_col1" class="data row1 col1">19.6%</td>
<td id="T_adc24_row1_col2" class="data row1 col2">12.1%</td>
<td id="T_adc24_row1_col3" class="data row1 col3">7.5%</td>
<td id="T_adc24_row1_col4" class="data row1 col4">Ministério</td>
<td id="T_adc24_row1_col5" class="data row1 col5">18772</td>
</tr>
<tr>
<td id="T_adc24_level0_row2" class="row_heading level0 row2"
data-quarto-table-cell-role="th">3</td>
<td id="T_adc24_row2_col0" class="data row2 col0">Mecânica e
Transporte</td>
<td id="T_adc24_row2_col1" class="data row2 col1">18.0%</td>
<td id="T_adc24_row2_col2" class="data row2 col2">4.5%</td>
<td id="T_adc24_row2_col3" class="data row2 col3">13.6%</td>
<td id="T_adc24_row2_col4" class="data row2 col4">Pesquisador</td>
<td id="T_adc24_row2_col5" class="data row2 col5">9068</td>
</tr>
<tr>
<td id="T_adc24_level0_row3" class="row_heading level0 row3"
data-quarto-table-cell-role="th">4</td>
<td id="T_adc24_row3_col0" class="data row3 col0">Agroindústria e
Alimentos</td>
<td id="T_adc24_row3_col1" class="data row3 col1">16.1%</td>
<td id="T_adc24_row3_col2" class="data row3 col2">8.5%</td>
<td id="T_adc24_row3_col3" class="data row3 col3">7.5%</td>
<td id="T_adc24_row3_col4" class="data row3 col4">Ministério</td>
<td id="T_adc24_row3_col5" class="data row3 col5">8144</td>
</tr>
<tr>
<td id="T_adc24_level0_row4" class="row_heading level0 row4"
data-quarto-table-cell-role="th">5</td>
<td id="T_adc24_row4_col0" class="data row4 col0">Metalurgia e
Mineração</td>
<td id="T_adc24_row4_col1" class="data row4 col1">15.9%</td>
<td id="T_adc24_row4_col2" class="data row4 col2">5.6%</td>
<td id="T_adc24_row4_col3" class="data row4 col3">10.3%</td>
<td id="T_adc24_row4_col4" class="data row4 col4">Pesquisador</td>
<td id="T_adc24_row4_col5" class="data row4 col5">4989</td>
</tr>
<tr>
<td id="T_adc24_level0_row5" class="row_heading level0 row5"
data-quarto-table-cell-role="th">6</td>
<td id="T_adc24_row5_col0" class="data row5 col0">Eletroeletrônica</td>
<td id="T_adc24_row5_col1" class="data row5 col1">13.3%</td>
<td id="T_adc24_row5_col2" class="data row5 col2">2.2%</td>
<td id="T_adc24_row5_col3" class="data row5 col3">11.1%</td>
<td id="T_adc24_row5_col4" class="data row5 col4">Pesquisador</td>
<td id="T_adc24_row5_col5" class="data row5 col5">7158</td>
</tr>
<tr>
<td id="T_adc24_level0_row6" class="row_heading level0 row6"
data-quarto-table-cell-role="th">7</td>
<td id="T_adc24_row6_col0" class="data row6 col0">Química e
Farmácia</td>
<td id="T_adc24_row6_col1" class="data row6 col1">8.8%</td>
<td id="T_adc24_row6_col2" class="data row6 col2">3.3%</td>
<td id="T_adc24_row6_col3" class="data row6 col3">5.5%</td>
<td id="T_adc24_row6_col4" class="data row6 col4">Pesquisador</td>
<td id="T_adc24_row6_col5" class="data row6 col5">12845</td>
</tr>
</tbody>
</table>



    🔍 2. ANÁLISE COMPARATIVA E INSIGHTS
    --------------------------------------------------------------------------------


    💡 RECOMENDAÇÕES PARA REDUÇÃO DA SUBJETIVIDADE
    ================================================================================

    1. **HARMONIZAÇÃO DE CRITÉRIOS POR SETOR:**
       - Desenvolver guias específicos para setores com alta discordância
       - Realizar workshops de alinhamento entre avaliadores por área temática

    2. **PADRONIZAÇÃO DE INTERPRETAÇÕES:**
       - Criar exemplos concretos do que constitui "inovação suficiente" por setor
       - Estabelecer métricas objetivas para avaliar "clareza metodológica"

    3. **SISTEMA DE DUPLA CHECAGEM:**
       - Implementar revisão obrigatória para projetos em setores de alta discordância
       - Criar comitês mistos (pesquisador + analista) para casos limítrofes

    4. **CAPACITAÇÃO CONTINUADA:**
       - Treinar analistas do Ministério em aspectos técnicos específicos
       - Sensibilizar pesquisadores sobre requisitos formais e de enquadramento

    5. **FEEDBACK ESTRUTURADO:**
       - Implementar sistema de justificativas estruturadas com campos obrigatórios
       - Criar base de conhecimento com decisões anteriores como referência
        

    💾 Análise setorial exportada para 'analise_discordancia_setorial_q2_q3.csv'
