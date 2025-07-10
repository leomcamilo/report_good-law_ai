#!/usr/bin/env python3
"""
Clusterização Multi-Dimensional para Análise de Decisões Lei do Bem
==================================================================

Este script implementa uma abordagem multi-dimensional para clusterização
que combina aspectos técnicos, empresariais e de processo para detectar
padrões de decisão nos projetos da Lei do Bem.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sentence_transformers import SentenceTransformer
import umap
import hdbscan
from pathlib import Path
import re
import nltk
from typing import Dict, List, Tuple, Optional
import seaborn as sns
import matplotlib.pyplot as plt

class ClusterizadorMultiDimensional:
    """
    Clusterizador avançado para análise de padrões de decisão
    em projetos da Lei do Bem.
    """
    
    def __init__(self):
        self.model_embedding = None
        self.scalers = {}
        self.encoders = {}
        self.cluster_results = {}
        
    def carregar_dados(self, caminho_csv: str) -> pd.DataFrame:
        """Carrega e preprocessa os dados."""
        df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8')
        print(f"📊 Dados carregados: {len(df)} projetos")
        return df
    
    def extrair_features_empresariais(self, df: pd.DataFrame) -> pd.DataFrame:
        """Extrai features relacionadas às características empresariais."""
        print("🏢 Extraindo features empresariais...")
        
        # Extrair informações da coluna 'empresa'
        df['cnpj'] = df['empresa'].str.extract(r'CNPJ:\s*([0-9./]+)')
        df['razao_social'] = df['empresa'].str.extract(r'RAZÃO SOCIAL\s*:\s*(.*?)\s*ATIVIDADE')
        df['atividade_economica'] = df['empresa'].str.extract(r'ATIVIDADE ECONOMICA\s*:\s*(.*?)\s*Cd ATIV')
        df['codigo_cnae'] = df['empresa'].str.extract(r'Cd ATIV\.ECONOMICA IBGE\s*:\s*(.*?)\s*PORTE')
        
        return df
    
    def extrair_features_projeto(self, df: pd.DataFrame) -> pd.DataFrame:
        """Extrai features específicas dos projetos."""
        print("🔬 Extraindo features dos projetos...")
        
        # Extrair informações da coluna 'projeto'
        df['numero_projeto'] = df['projeto'].str.extract(r'NÚMERO:\s*(\d+)')
        df['nome_projeto'] = df['projeto'].str.extract(r'NOME:\s*(.*?)\s*DESCRIÇÃO:')
        df['descricao_projeto'] = df['projeto'].str.extract(r'DESCRIÇÃO:\s*(.*?)\s*TIPO \(')
        df['tipo_projeto'] = df['projeto'].str.extract(r'TIPO \(PA ou DE\):\s*(.*?)\s*AREA:')
        df['area_projeto'] = df['projeto'].str.extract(r'AREA:\s*(.*?)\s*PALAVRAS')
        df['palavras_chave'] = df['projeto'].str.extract(r'PALAVRAS CHAVE:\s*(.*?)\s*NATUREZA:')
        df['natureza'] = df['projeto'].str.extract(r'NATUREZA:\s*(.*?)\s*ELEMENTO')
        df['elemento_tecnologico'] = df['projeto'].str.extract(r'ELEMENTO TECNOLÓGICO:\s*(.*?)\s*DESAFIO')
        df['desafio_tecnologico'] = df['projeto'].str.extract(r'DESAFIO TECNOLÓGICO:\s*(.*?)\s*METODOLOGIA')
        df['metodologia'] = df['projeto'].str.extract(r'METODOLOGIA:\s*(.*?)\s*INFORMAÇÃO')
        
        # Criar features numéricas dos textos
        df['tamanho_descricao'] = df['descricao_projeto'].str.len().fillna(0)
        df['tamanho_elemento_tech'] = df['elemento_tecnologico'].str.len().fillna(0)
        df['tamanho_desafio'] = df['desafio_tecnologico'].str.len().fillna(0)
        df['tamanho_metodologia'] = df['metodologia'].str.len().fillna(0)
        
        # Normalizar tipo de projeto
        df['tipo_projeto_cod'] = df['tipo_projeto'].map({'PA': 1, 'DE': 2}).fillna(1)
        
        return df
    
    def criar_embeddings_contextuais(self, df: pd.DataFrame) -> np.ndarray:
        """Cria embeddings considerando contexto empresarial + projeto."""
        print("🤖 Criando embeddings contextuais...")
        
        if self.model_embedding is None:
            self.model_embedding = SentenceTransformer(
                "PORTULAN/serafim-335m-portuguese-pt-sentence-encoder-ir"
            )
        
        # Criar texto contextual combinado
        def criar_contexto_completo(row):
            contexto_partes = []
            
            # Contexto empresarial
            if pd.notna(row.get('atividade_economica')):
                contexto_partes.append(f"Setor: {row['atividade_economica']}")
            
            # Contexto do projeto
            if pd.notna(row.get('tipo_projeto')):
                contexto_partes.append(f"Tipo: {row['tipo_projeto']}")
            if pd.notna(row.get('area_projeto')):
                contexto_partes.append(f"Área: {row['area_projeto']}")
            if pd.notna(row.get('natureza')):
                contexto_partes.append(f"Natureza: {row['natureza']}")
            
            # Conteúdo técnico principal
            conteudo_tecnico = []
            for col in ['descricao_projeto', 'elemento_tecnologico', 'desafio_tecnologico']:
                if pd.notna(row.get(col)) and len(str(row[col])) > 10:
                    conteudo_tecnico.append(str(row[col]))
            
            # Combinar tudo
            contexto_final = " | ".join(contexto_partes) + " || " + " ".join(conteudo_tecnico)
            return contexto_final
        
        # Criar contexto completo (sem limpeza adicional, pois já foi feita)
        df['contexto_completo'] = df.apply(criar_contexto_completo, axis=1)
        
        # Gerar embeddings
        embeddings = self.model_embedding.encode(
            df['contexto_completo'].tolist(), 
            show_progress_bar=True
        )
        
        print(f"✅ Embeddings gerados: {embeddings.shape}")
        return embeddings
    
    def criar_features_numericas(self, df: pd.DataFrame) -> np.ndarray:
        """Cria matriz de features numéricas."""
        print("🔢 Criando features numéricas...")
        
        # Features numéricas diretas
        features_numericas = [
            'tipo_projeto_cod',
            'tamanho_descricao', 'tamanho_elemento_tech', 'tamanho_desafio'
        ]
        
        # Features categóricas para encoding
        features_categoricas = ['atividade_economica', 'area_projeto', 'natureza']
        
        # Matriz final
        X_num = df[features_numericas].fillna(0).values
        
        # Encoding de categóricas
        X_cat_list = []
        for col in features_categoricas:
            if col not in self.encoders:
                self.encoders[col] = LabelEncoder()
                encoded = self.encoders[col].fit_transform(df[col].fillna('UNKNOWN'))
            else:
                encoded = self.encoders[col].transform(df[col].fillna('UNKNOWN'))
            X_cat_list.append(encoded.reshape(-1, 1))
        
        if X_cat_list:
            X_cat = np.hstack(X_cat_list)
            X_final = np.hstack([X_num, X_cat])
        else:
            X_final = X_num
        
        # Normalizar
        if 'features_numericas' not in self.scalers:
            self.scalers['features_numericas'] = StandardScaler()
            X_scaled = self.scalers['features_numericas'].fit_transform(X_final)
        else:
            X_scaled = self.scalers['features_numericas'].transform(X_final)
        
        print(f"✅ Features numéricas: {X_scaled.shape}")
        return X_scaled
    
    def cluster_hibrido(self, 
                       embeddings: np.ndarray, 
                       features_numericas: np.ndarray,
                       peso_semantico: float = 0.7,
                       peso_estrutural: float = 0.3) -> Dict[str, np.ndarray]:
        """
        Aplica clusterização híbrida combinando embeddings semânticos
        e features estruturais.
        """
        print("🎯 Aplicando clusterização híbrida...")
        
        # Normalizar embeddings para mesmo range das features
        embeddings_norm = StandardScaler().fit_transform(embeddings)
        
        # Combinar representações com pesos
        X_combinado = np.hstack([
            embeddings_norm * peso_semantico,
            features_numericas * peso_estrutural
        ])
        
        # Redução de dimensionalidade
        print("📉 Aplicando UMAP para redução dimensional...")
        umap_reducer = umap.UMAP(
            n_components=50,
            metric='cosine',
            min_dist=0.1,
            n_neighbors=15,
            random_state=42
        )
        X_reduced = umap_reducer.fit_transform(X_combinado)
        
        # Múltiplas abordagens de clustering
        resultados = {}
        
        # 1. HDBSCAN - Detecta clusters de densidade
        print("🔍 HDBSCAN clustering...")
        hdbscan_clusterer = hdbscan.HDBSCAN(
            min_cluster_size=20,
            min_samples=10,
            metric='euclidean'
        )
        clusters_hdbscan = hdbscan_clusterer.fit_predict(X_reduced)
        resultados['hdbscan'] = clusters_hdbscan
        
        # 2. Aglomerativo - Para comparação
        print("🔗 Clustering aglomerativo...")
        agg_clusterer = AgglomerativeClustering(
            n_clusters=None,
            distance_threshold=0.6,
            linkage='average'
        )
        clusters_agg = agg_clusterer.fit_predict(X_reduced)
        resultados['aglomerativo'] = clusters_agg
        
        # 3. Clustering por área + semântica
        print("📊 Clustering estratificado por área...")
        clusters_estratificado = self._cluster_por_area(X_reduced, features_numericas)
        resultados['estratificado'] = clusters_estratificado
        
        # Avaliar qualidade dos clusters
        for nome, clusters in resultados.items():
            if len(set(clusters)) > 1:
                silhouette = silhouette_score(X_reduced, clusters)
                n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
                cobertura = (clusters != -1).sum() / len(clusters) * 100
                print(f"   {nome}: {n_clusters} clusters, Silhouette: {silhouette:.3f}, Cobertura: {cobertura:.1f}%")
        
        return resultados
    
    def _cluster_por_area(self, X_reduced: np.ndarray, features_num: np.ndarray) -> np.ndarray:
        """Clustering estratificado considerando área do projeto."""
        # Esta seria uma implementação específica que considera
        # clustering dentro de cada área tecnológica
        # Por simplicidade, retorno clustering padrão
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters=25, random_state=42)
        return kmeans.fit_predict(X_reduced)
    
    def analisar_caracteristicas_clusters(self, 
                                        df: pd.DataFrame, 
                                        clusters: np.ndarray,
                                        nome_metodo: str) -> pd.DataFrame:
        """Analisa as características de cada cluster."""
        print(f"📊 Analisando características dos clusters ({nome_metodo})...")
        
        df_analise = df.copy()
        df_analise['cluster'] = clusters
        
        # Análise por cluster
        analise_clusters = []
        
        for cluster_id in sorted(df_analise['cluster'].unique()):
            if cluster_id == -1:  # Pular ruído
                continue
                
            cluster_data = df_analise[df_analise['cluster'] == cluster_id]
            
            analise = {
                'cluster_id': cluster_id,
                'num_projetos': len(cluster_data),
                'percentual': len(cluster_data) / len(df_analise) * 100,
                
                # Características empresariais dominantes
                'setor_principal': cluster_data['atividade_economica'].mode().iloc[0] if not cluster_data['atividade_economica'].mode().empty else 'N/A',
                
                # Características dos projetos
                'tipo_projeto_principal': cluster_data['tipo_projeto'].mode().iloc[0] if not cluster_data['tipo_projeto'].mode().empty else 'N/A',
                'area_principal': cluster_data['area_projeto'].mode().iloc[0] if not cluster_data['area_projeto'].mode().empty else 'N/A',
                
                # Métricas de tamanho
                'tamanho_descricao_medio': cluster_data['tamanho_descricao'].mean(),
                'tamanho_elemento_tech_medio': cluster_data['tamanho_elemento_tech'].mean(),
                'tamanho_desafio_medio': cluster_data['tamanho_desafio'].mean(),
                
                # Empresas representativas
                'empresas_exemplo': cluster_data['razao_social'].value_counts().head(3).index.tolist()
            }
            
            analise_clusters.append(analise)
        
        df_clusters_analise = pd.DataFrame(analise_clusters)
        return df_clusters_analise
    
    def sugerir_criterios_divisao(self, analise_clusters: pd.DataFrame) -> List[str]:
        """Sugere critérios para divisão dos projetos baseado nos clusters."""
        print("💡 Sugerindo critérios de divisão...")
        
        criterios = []
        
        # Analisar dominância por setor
        setores = analise_clusters['setor_principal'].value_counts()
        if len(setores) >= 3:
            criterios.append(f"DIVISÃO POR SETOR: {len(setores)} setores identificados - {', '.join(setores.index[:3])}")
        
        # Analisar por tipo de projeto
        tipos = analise_clusters['tipo_projeto_principal'].value_counts()
        if len(tipos) >= 2:
            criterios.append(f"DIVISÃO POR TIPO: PA vs DE - {tipos.to_dict()}")
        
        # Analisar por tamanho de descrição (proxy para complexidade)
        tamanho_alto = analise_clusters[analise_clusters['tamanho_descricao_medio'] > analise_clusters['tamanho_descricao_medio'].quantile(0.75)]
        if len(tamanho_alto) > 0:
            criterios.append(f"DIVISÃO POR DETALHAMENTO: {len(tamanho_alto)} clusters com descrições muito detalhadas")
        
        # Analisar por área do projeto
        areas = analise_clusters['area_principal'].value_counts()
        if len(areas) >= 3:
            criterios.append(f"DIVISÃO POR ÁREA TECNOLÓGICA: {len(areas)} áreas principais - {', '.join(areas.index[:3])}")
        
        return criterios

def main():
    """Função principal com exemplo de uso."""
    print("🚀 Clusterização Multi-Dimensional - Lei do Bem")
    print("=" * 60)
    
    # Inicializar clusterizador
    cluster_analyzer = ClusterizadorMultiDimensional()
    
    # Buscar arquivo CSV
    pasta_tabelas = Path("tabelas_csv_xlsx")
    arquivos_csv = list(pasta_tabelas.glob("*.csv"))
    
    if not arquivos_csv:
        print("❌ Nenhum arquivo CSV encontrado na pasta tabelas_csv_xlsx")
        return
    
    # Carregar dados
    df = cluster_analyzer.carregar_dados(arquivos_csv[0])
    
    # Extrair features
    df = cluster_analyzer.extrair_features_empresariais(df)
    df = cluster_analyzer.extrair_features_projeto(df)
    
    # Criar representações
    embeddings = cluster_analyzer.criar_embeddings_contextuais(df)
    features_num = cluster_analyzer.criar_features_numericas(df)
    
    # Aplicar clustering híbrido
    resultados_cluster = cluster_analyzer.cluster_hibrido(embeddings, features_num)
    
    # Analisar melhor resultado (baseado em silhouette score)
    melhor_metodo = 'aglomerativo'  # ou escolher baseado em métricas
    clusters_finais = resultados_cluster[melhor_metodo]
    
    # Analisar características
    analise = cluster_analyzer.analisar_caracteristicas_clusters(
        df, clusters_finais, melhor_metodo
    )
    
    # Exibir resultados
    print("\n📋 TOP 10 CLUSTERS:")
    print(analise.head(10).to_string(index=False))
    
    # Sugerir critérios
    criterios = cluster_analyzer.sugerir_criterios_divisao(analise)
    print("\n💡 CRITÉRIOS SUGERIDOS PARA DIVISÃO:")
    for i, criterio in enumerate(criterios, 1):
        print(f"{i}. {criterio}")
    
    # Salvar resultados
    df['cluster_final'] = clusters_finais
    df.to_csv('projetos_clusters_melhorados.csv', index=False, sep=';')
    analise.to_csv('analise_clusters_caracteristicas.csv', index=False, sep=';')
    
    print(f"\n✅ Análise concluída!")
    print(f"📁 Resultados salvos em:")
    print(f"   - projetos_clusters_melhorados.csv")
    print(f"   - analise_clusters_caracteristicas.csv")

if __name__ == "__main__":
    main()