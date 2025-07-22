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

Esta análise aprofundada explora as decisões tomadas por analistas e
pareceristas no âmbito do programa Lei do Bem do MCTI, um dos principais
instrumentos de fomento à inovação no Brasil. O estudo se baseia em um
volume expressivo de dados, compreendendo 13.198 projetos analisados
durante o ano de 2021. O objetivo geral é identificar padrões,
inconsistências e insights nas avaliações, visando otimizar a
eficiência, a isonomia e a previsibilidade do processo de concessão de
incentivos fiscais para Pesquisa e Desenvolvimento (P&D).

## 2. Metodologia

A análise foi conduzida a partir de um banco de dados consolidado
contendo informações detalhadas sobre cada um dos 13.198 projetos do
ano-base de 2021. As fontes de dados incluem os pareceres técnicos
emitidos tanto pelo Ministério (fase DO) quanto pelos pesquisadores ad
hoc (fase Parecer), além de metadados dos projetos, como áreas de
conhecimento e informações textuais descritivas. As técnicas aplicadas
envolveram desde a estatística descritiva, para quantificar taxas de
aprovação e concordância, até a análise de dispersão para entender a
distribuição de projetos entre os representantes do Ministério. Um dos
pilares da metodologia foi o processamento de linguagem natural (PLN),
utilizado para extrair insights dos campos textuais. Para isso, a
biblioteca NLTK (Natural Language Toolkit) foi empregada para processar
os textos em português, aplicando a remoção de stopwords (palavras
comuns como “de”, “para”, “com”) para focar nos termos mais relevantes
de cada projeto. O conjunto de stopwords foi composto por 207 palavras
do NLTK e um conjunto customizado de 71 termos específicos do domínio da
Lei do Bem, totalizando 278 palavras removidas para garantir uma análise
mais limpa e focada. Além disso, foi desenvolvido um modelo de Machine
Learning para explorar a capacidade preditiva dos dados textuais em
relação à aprovação final dos projetos.

### Análise de Analistas vs Pareceristas - Lei do Bem 2021

**Data de Análise:** 22/07/2025

**Ano Base dos Dados:** 2018 à 2023

**Total de Projetos:** 13.198

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
    'lst_noatividadeeconomica', 'daproj_nritem'
]

colunas_projeto = [
    'daproj_noprojeto', 'daproj_dsprojeto', 'daproj_dsareaprojeto',
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

## 2. Análise Exploratória Inicial

``` python
# %% Estatísticas básicas
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

## Análise de Quadrante de Decisão

Análise dos quadrantes de decisão entre Pesquisadores e Ministério.

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
