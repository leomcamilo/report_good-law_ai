#!/usr/bin/env python3
"""
Análise de Clusters - Lei do Bem
===============================

Este script analisa os clusters criados pelo embedding_cluster.py,
extraindo informações específicas dos projetos para análise.
"""

import pandas as pd
import numpy as np
import re
from pathlib import Path


def extrair_nome_projeto(texto_projeto):
    """
    Extrai o nome do projeto da coluna 'projeto'.
    Busca o texto entre 'NOME: ' e ' DESCRIÇÃO: '
    """
    if pd.isna(texto_projeto):
        return None
    
    # Padrão regex para capturar o nome entre NOME: e DESCRIÇÃO:
    padrao = r'NOME:\s*(.*?)\s*DESCRIÇÃO:'
    match = re.search(padrao, str(texto_projeto))
    
    if match:
        return match.group(1).strip()
    return None


def extrair_descricao_projeto(texto_projeto):
    """
    Extrai a descrição do projeto da coluna 'projeto'.
    Busca o texto entre 'DESCRIÇÃO: ' e 'TIPO (PA ou DE): '
    """
    if pd.isna(texto_projeto):
        return None
    
    # Padrão regex para capturar a descrição entre DESCRIÇÃO: e TIPO (PA ou DE):
    padrao = r'DESCRIÇÃO:\s*(.*?)\s*TIPO \(PA ou DE\):'
    match = re.search(padrao, str(texto_projeto), re.DOTALL)
    
    if match:
        return match.group(1).strip()
    return None


def extrair_razao_social_empresa(texto_empresa):
    """
    Extrai a razão social da empresa da coluna 'empresa'.
    Busca o texto entre 'RAZÃO SOCIAL :' e ' ATIVIDADE ECONOMICA :'
    """
    if pd.isna(texto_empresa):
        return None
    
    # Padrão regex para capturar a razão social entre RAZÃO SOCIAL : e ATIVIDADE ECONOMICA :
    padrao = r'RAZÃO SOCIAL\s*:\s*(.*?)\s*ATIVIDADE ECONOMICA\s*:'
    match = re.search(padrao, str(texto_empresa))
    
    if match:
        return match.group(1).strip()
    return None


def analisar_distribuicao_clusters(df_clusters):
    """
    Analisa a distribuição dos clusters e retorna estatísticas básicas.
    """
    print("=" * 60)
    print("ANÁLISE DE DISTRIBUIÇÃO DOS CLUSTERS")
    print("=" * 60)
    
    # Estatísticas gerais
    total_projetos = len(df_clusters)
    total_clusters = df_clusters['cluster'].nunique()
    projetos_sem_cluster = len(df_clusters[df_clusters['cluster'] == -1])
    
    print(f"📊 Total de projetos: {total_projetos:,}")
    print(f"🎯 Total de clusters: {total_clusters}")
    print(f"❌ Projetos sem cluster (ruído): {projetos_sem_cluster:,}")
    print(f"✅ Taxa de clusterização: {((total_projetos - projetos_sem_cluster) / total_projetos * 100):.1f}%")
    
    # Top 10 clusters por tamanho
    print(f"\n📈 TOP 10 CLUSTERS POR TAMANHO:")
    cluster_sizes = df_clusters['cluster'].value_counts().head(10)
    for cluster_id, size in cluster_sizes.items():
        if cluster_id != -1:  # Ignorar ruído na lista top
            print(f"   Cluster {cluster_id}: {size:,} projetos")
    
    # Empresas mais frequentes
    print(f"\n🏢 TOP 10 EMPRESAS COM MAIS PROJETOS:")
    empresa_counts = df_clusters['razaosocial_empresa'].value_counts().head(10)
    for empresa, count in empresa_counts.items():
        print(f"   {empresa}: {count:,} projetos")
    
    return {
        'total_projetos': total_projetos,
        'total_clusters': total_clusters,
        'projetos_sem_cluster': projetos_sem_cluster,
        'taxa_clusterizacao': ((total_projetos - projetos_sem_cluster) / total_projetos * 100)
    }


def main():
    """Função principal para análise dos clusters."""
    
    print("🚀 Iniciando Análise de Clusters - Lei do Bem")
    print("=" * 60)
    
    # 1. Carregar dados dos clusters
    try:
        print("📂 Carregando arquivo projetos_com_clusters_final.csv...")
        df_original = pd.read_csv('projetos_com_clusters_final.csv', sep = ';', encoding='utf-8')
        print(f"✅ Dados carregados: {len(df_original):,} projetos")
        
        # Verificar se as colunas necessárias existem
        colunas_necessarias = ['empresa', 'projeto', 'cluster']
        colunas_faltantes = [col for col in colunas_necessarias if col not in df_original.columns]
        
        if colunas_faltantes:
            raise ValueError(f"Colunas faltantes: {colunas_faltantes}")
            
    except FileNotFoundError:
        print("❌ Arquivo 'projetos_com_clusters.csv' não encontrado!")
        print("   Execute primeiro o script 'embedding_cluster.py'")
        return
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        return
    
    # 2. Extrair informações específicas
    print("\n🔍 Extraindo informações dos projetos...")
    
    # Criar DataFrame com as 4 colunas especificadas
    df_clusters = pd.DataFrame()
    
    # Extrair nome do projeto
    print("   - Extraindo nomes dos projetos...")
    df_clusters['nome_projeto'] = df_original['projeto'].apply(extrair_nome_projeto)
    
    # Extrair descrição do projeto
    print("   - Extraindo descrições dos projetos...")
    df_clusters['descricao_projeto'] = df_original['projeto'].apply(extrair_descricao_projeto)
    
    # Extrair razão social da empresa
    print("   - Extraindo razões sociais das empresas...")
    df_clusters['razaosocial_empresa'] = df_original['empresa'].apply(extrair_razao_social_empresa)
    
    # Adicionar cluster
    df_clusters['cluster'] = df_original['cluster']
    
    # 3. Limpar dados e verificar qualidade da extração
    print("\n🧹 Verificando qualidade da extração...")
    
    # Contar valores nulos por coluna
    nulos_por_coluna = df_clusters.isnull().sum()
    print("   Valores nulos encontrados:")
    for coluna, nulos in nulos_por_coluna.items():
        print(f"   - {coluna}: {nulos:,} ({nulos/len(df_clusters)*100:.1f}%)")
    
    # Remover linhas onde todas as extrações falharam
    df_clusters_limpo = df_clusters.dropna(subset=['nome_projeto', 'descricao_projeto', 'razaosocial_empresa'], how='all')
    
    if len(df_clusters_limpo) < len(df_clusters):
        removidos = len(df_clusters) - len(df_clusters_limpo)
        print(f"   ⚠️  Removidos {removidos:,} projetos com falha na extração")
    
    # 4. Análise estatística dos clusters
    stats = analisar_distribuicao_clusters(df_clusters_limpo)
    
    # 5. Salvar resultado
    print(f"\n💾 Salvando arquivo clusters_projetos.csv...")
    try:
        df_clusters_limpo.to_csv('clusters_projetos.csv', index=False, encoding='utf-8', sep=';')
        print(f"✅ Arquivo salvo com sucesso!")
        print(f"   - Linhas: {len(df_clusters_limpo):,}")
        print(f"   - Colunas: {len(df_clusters_limpo.columns)}")
        
        # Mostrar amostra dos dados
        print(f"\n📋 AMOSTRA DOS DADOS EXTRAÍDOS:")
        print("-" * 60)
        for i, row in df_clusters_limpo.head(3).iterrows():
            print(f"Projeto {i+1}:")
            print(f"  Nome: {row['nome_projeto'][:80]}...")
            print(f"  Empresa: {row['razaosocial_empresa']}")
            print(f"  Cluster: {row['cluster']}")
            print()
        
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")
        return
    
    print("🎉 Análise concluída com sucesso!")
    
    return df_clusters_limpo


if __name__ == "__main__":
    df_resultado = main()