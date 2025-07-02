import pandas as pd
import numpy as np
import os
from sentence_transformers import SentenceTransformer
import umap
import hdbscan
from pathlib import Path

def carregar_dados_csv():
    """Carrega arquivo CSV da pasta tabelas_csv_xlsx"""
    pasta_tabelas = Path("tabelas_csv_xlsx")
    
    # Busca por arquivos CSV na pasta
    arquivos_csv = list(pasta_tabelas.glob("*.csv"))
    
    if not arquivos_csv:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado na pasta tabelas_csv_xlsx")
    
    if len(arquivos_csv) > 1:
        print(f"Múltiplos arquivos CSV encontrados. Usando: {arquivos_csv[0]}")
    
    # Carrega o primeiro arquivo CSV encontrado
    df_projetos_unico = pd.read_csv(arquivos_csv[0])
    print(f"Dados carregados: {df_projetos_unico.shape[0]} projetos")
    
    return df_projetos_unico

def criar_embeddings(df):
    """Cria embeddings baseado nas colunas empresa, projeto e projeto_multianual"""
    
    # Verificar se as colunas existem
    colunas_necessarias = ['empresa', 'projeto', 'projeto_multianual']
    colunas_faltantes = [col for col in colunas_necessarias if col not in df.columns]
    
    if colunas_faltantes:
        raise ValueError(f"Colunas faltantes no DataFrame: {colunas_faltantes}")
    
    # Concatenar as três colunas
    df['texto_concatenado'] = (
        df['empresa'].astype(str) + " " + 
        df['projeto'].astype(str) + " " + 
        df['projeto_multianual'].astype(str)
    )
    
    # Carregar modelo de embeddings em português
    print("Carregando modelo de embeddings...")
    model = SentenceTransformer('neuralmind/bert-base-portuguese-cased')
    
    # Gerar embeddings
    print("Gerando embeddings...")
    embeddings = model.encode(df['texto_concatenado'].tolist(), show_progress_bar=True)
    
    # Adicionar embeddings como coluna
    df['embeddings'] = list(embeddings)
    
    return df, embeddings

def fazer_clustering(embeddings, n_projetos):
    """Faz clustering usando UMAP + HDBSCAN"""
    
    print("Reduzindo dimensionalidade com UMAP...")
    # UMAP para reduzir dimensionalidade
    reducer = umap.UMAP(
        n_components=100,      # mais dimensões = mais informação preservada
        n_neighbors=30,        # para dataset grande, mais vizinhos
        min_dist=0.0,         # permitir pontos bem próximos
        metric='cosine',
        random_state=42,
        verbose=True
    )
    
    embeddings_reduced = reducer.fit_transform(embeddings)
    
    print("Fazendo clustering com HDBSCAN...")
    # Ajustar parâmetros baseado no número de projetos
    # Para 70k projetos, queremos entre 100-400 clusters
    min_cluster_size = max(50, n_projetos // 1000)  # Ajuste dinâmico
    
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster_size,    # clusters maiores para dataset grande
        min_samples=10,
        metric='euclidean',
        cluster_selection_method='leaf'  # pega folhas da árvore
    )
    
    clusters = clusterer.fit_predict(embeddings_reduced)
    
    # Estatísticas do clustering
    n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
    n_noise = list(clusters).count(-1)
    
    print(f"Número de clusters: {n_clusters}")
    print(f"Pontos de ruído: {n_noise}")
    print(f"Porcentagem clusterizada: {((n_projetos - n_noise) / n_projetos) * 100:.2f}%")
    
    return clusters, embeddings_reduced

def main():
    """Função principal"""
    try:
        # 1. Carregar dados
        print("1. Carregando dados CSV...")
        df_projetos_unico = carregar_dados_csv()
        
        # 2. Criar embeddings
        print("2. Criando embeddings...")
        df_projetos_unico, embeddings = criar_embeddings(df_projetos_unico)
        
        # 3. Fazer clustering
        print("3. Fazendo clustering...")
        clusters, embeddings_reduced = fazer_clustering(embeddings, len(df_projetos_unico))
        
        # 4. Adicionar clusters ao dataframe
        df_projetos_unico['cluster'] = clusters
        
        # 5. Salvar resultado
        print("4. Salvando resultado...")
        df_projetos_unico.to_csv('projetos_com_clusters.csv', index=False)
        
        # Salvar embeddings reduzidos separadamente (opcional)
        np.save('embeddings_reduced.npy', embeddings_reduced)
        
        print("Processo concluído com sucesso!")
        print(f"Arquivo salvo: projetos_com_clusters.csv")
        
        # Mostrar estatísticas finais
        cluster_stats = df_projetos_unico['cluster'].value_counts().sort_index()
        print(f"\nEstatísticas dos clusters:")
        print(f"Total de clusters: {len(cluster_stats[cluster_stats.index != -1])}")
        print(f"Projetos não clusterizados (ruído): {cluster_stats.get(-1, 0)}")
        
    except Exception as e:
        print(f"Erro durante execução: {str(e)}")
        raise

if __name__ == "__main__":
    main()