#!/usr/bin/env python3
"""
Análise Avançada de Clusters para Projetos Lei do Bem
=====================================================

Este script implementa clusterização por área tecnológica usando K-Means
para identificar padrões de decisão nos projetos dentro de cada área.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import re
from datetime import datetime
import warnings
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io
import os

warnings.filterwarnings('ignore')

class AnalisadorClusterAvancado:
    """Classe para análise avançada de clusters com foco em padrões de decisão por área"""
    
    def __init__(self):
        self.df = None
        self.embeddings = None
        self.embeddings_por_area = {}
        self.clusters_por_area = {}
        self.model_embedding = None
        self.resultados_analise = {}
        
    def carregar_dados(self, caminho_csv: str) -> pd.DataFrame:
        """Carrega os dados do CSV"""
        print("📂 Carregando dados...")
        self.df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8')
        print(f"✅ {len(self.df)} projetos carregados")
        
        # Extrair informações estruturadas
        self._extrair_campos_estruturados()
        
        return self.df
    
    def _extrair_campos_estruturados(self):
        """Extrai e renomeia campos estruturados das colunas do CSV."""
        print("🔍 Mapeando campos estruturados...")

        # Mapeamento de nomes de colunas do CSV para nomes de campos internos
        mapeamento_campos = {
            'daproj_noprojeto': 'nome_projeto',
            'daproj_dsprojeto': 'descricao_projeto',
            'daproj_tppbpade': 'tipo_projeto',
            'daproj_dsareaprojeto': 'area_projeto',
            'daproj_dselementotecnologico': 'elemento_tecnologico',
            'daproj_dsdesafiotecnologico': 'desafio_tecnologico',
            'daproj_dsmetodologiautilizada': 'metodologia',
            'daproj_dspalavrachave': 'palavra_chave',
            'lst_norazaosocial': 'razao_social',
            'lst_noatividadeeconomica': 'atividade_economica',
            'lst_notipoportepessoajuridica': 'porte_empresa'
        }

        # Renomear colunas para os nomes de campos esperados pelo resto do script
        colunas_para_renomear = {k: v for k, v in mapeamento_campos.items() if k in self.df.columns}
        self.df.rename(columns=colunas_para_renomear, inplace=True)

        # Verificar se as colunas renomeadas agora existem
        for campo_novo in mapeamento_campos.values():
            if campo_novo not in self.df.columns:
                print(f"⚠️ Campo esperado '{campo_novo}' não encontrado após o mapeamento.")

        # Campos numéricos e categóricos que já devem existir com o nome correto
        campos_relevantes = [
            'do_saat_idunicopessoaanalise',  # ID do analista
            'do_taaproj_notipoavaliacaoanalise',  # Resultado da avaliação
            'do_aat_vltotaldeclarado',  # Valor declarado
            'do_nd1_dsnotadimensao_invocao',  # Nota inovação
            'do_nd2_dsnotadimensao_resultado',  # Nota resultado
            'do_nd3_dsnotadimensao_final'  # Nota final
        ]

        # Verificar quais campos relevantes existem
        for campo in campos_relevantes:
            if campo not in self.df.columns:
                print(f"⚠️ Campo relevante '{campo}' não encontrado no CSV.")

        print("✅ Mapeamento de campos concluído.")
    
    def criar_embeddings_por_area(self):
        """Cria embeddings por área tecnológica"""
        print("🤖 Criando embeddings por área tecnológica...")
        
        if self.model_embedding is None:
            self.model_embedding = SentenceTransformer(
                "PORTULAN/serafim-335m-portuguese-pt-sentence-encoder-ir"
            )
        
        # Filtrar projetos sem área definida
        df_com_area = self.df[self.df['area_projeto'].notna()].copy()
        areas_unicas = df_com_area['area_projeto'].unique()
        
        print(f"📊 Encontradas {len(areas_unicas)} áreas tecnológicas:")
        for i, area in enumerate(sorted(areas_unicas), 1):
            count = len(df_com_area[df_com_area['area_projeto'] == area])
            print(f"   {i}. {area[:60]}... ({count} projetos)")
        
        # Criar embeddings para cada área
        def criar_texto_ponderado(row):
            componentes = []
            
            # Alta prioridade (peso 6)
            for campo in ['palavra_chave', 'razao_social']:
                if pd.notna(row.get(campo)):
                    componentes.extend([str(row[campo])] * 6)
            
            # Média prioridade (peso 5)
            for campo in ['atividade_economica', 'tipo_projeto']:
                if pd.notna(row.get(campo)):
                    componentes.extend([str(row[campo])] * 5)
            
            # Baixa prioridade (peso 1)
            for campo in ['descricao_projeto', 'desafio_tecnologico', 'elemento_tecnologico', 'metodologia']:
                if pd.notna(row.get(campo)):
                    componentes.append(str(row[campo]))
            
            return ' '.join(componentes)
        
        self.embeddings_por_area = {}
        self.dados_por_area = {}
        
        for area in areas_unicas:
            projetos_area = df_com_area[df_com_area['area_projeto'] == area].copy()
            
            if len(projetos_area) >= 2:  # Mínimo 2 projetos para clustering
                print(f"   Processando área: {area[:50]}... ({len(projetos_area)} projetos)")
                
                # Gerar textos ponderados para esta área
                textos_ponderados = projetos_area.apply(criar_texto_ponderado, axis=1).tolist()
                
                # Criar embeddings
                embeddings_area = self.model_embedding.encode(
                    textos_ponderados, 
                    show_progress_bar=False,
                    batch_size=32
                )
                
                self.embeddings_por_area[area] = embeddings_area
                self.dados_por_area[area] = projetos_area
            else:
                print(f"   ⚠️ Área '{area}' ignorada (apenas {len(projetos_area)} projetos)")
        
        print(f"✅ Embeddings criados para {len(self.embeddings_por_area)} áreas")
        return self.embeddings_por_area
    
    def analisar_kmeans_por_area(self, max_k: int = 20):
        """Aplica K-Means otimizado para cada área tecnológica"""
        print("🎯 Analisando K-Means por área tecnológica...")
        
        self.clusters_por_area = {}
        resultados_kmeans = {}
        
        for area, embeddings in self.embeddings_por_area.items():
            print(f"\n📊 Analisando área: {area[:50]}...")
            
            dados_area = self.dados_por_area[area]
            
            # Normalizar embeddings
            scaler = StandardScaler()
            embeddings_norm = scaler.fit_transform(embeddings)
            
            # Determinar range de K baseado no número de projetos
            num_projetos = len(dados_area)
            max_k_area = min(max_k, num_projetos // 2)  # Máximo metade dos projetos
            
            if max_k_area < 2:
                print(f"   ⚠️ Área com poucos projetos ({num_projetos}), usando K=1")
                clusters = np.zeros(num_projetos)
                k_optimal = 1
                best_silhouette = 0
                silhouettes = [0]
                k_values = [1]
            else:
                # Testar diferentes valores de K (a partir de 2)
                silhouettes = []
                k_values = list(range(2, max_k_area + 1))
                
                for k in k_values:
                    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
                    clusters_temp = kmeans.fit_predict(embeddings_norm)
                    silhouette = silhouette_score(embeddings_norm, clusters_temp)
                    silhouettes.append(silhouette)
                
                # K ótimo baseado no melhor silhouette score
                k_optimal = k_values[np.argmax(silhouettes)]
                best_silhouette = max(silhouettes)
                
                print(f"   📈 K ótimo: {k_optimal} (Silhouette: {best_silhouette:.4f})")
                
                # Aplicar K-Means com K ótimo
                kmeans_final = KMeans(n_clusters=k_optimal, random_state=42, n_init=20)
                clusters = kmeans_final.fit_predict(embeddings_norm)
            
            # Salvar resultados
            self.clusters_por_area[area] = clusters
            resultados_kmeans[area] = {
                'k_optimal': k_optimal,
                'best_silhouette': best_silhouette,
                'silhouettes': silhouettes,
                'k_values': k_values,
                'num_projetos': num_projetos,
                'scaler': scaler if max_k_area >= 2 else None
            }
            
            # Adicionar clusters aos dados da área
            dados_area_copy = dados_area.copy()
            dados_area_copy['cluster_kmeans'] = clusters
            dados_area_copy['area_tecnologica'] = area
            self.dados_por_area[area] = dados_area_copy
        
        self.resultados_analise['kmeans_por_area'] = resultados_kmeans
        
        # Consolidar todos os dados com clusters
        self._consolidar_dados_com_clusters()
        
        return self.clusters_por_area
    
    def _consolidar_dados_com_clusters(self):
        """Consolida todos os dados com clusters em um único DataFrame"""
        print("🔄 Consolidando dados com clusters...")
        
        # Concatenar todos os dataframes por área
        dfs_com_clusters = []
        for area, df_area in self.dados_por_area.items():
            # Criar ID único do cluster: area_clusterID
            df_area_copy = df_area.copy()
            df_area_copy['cluster_global'] = df_area_copy['cluster_kmeans'].apply(
                lambda x: f"{area[:20]}_{x}"
            )
            dfs_com_clusters.append(df_area_copy)
        
        if dfs_com_clusters:
            self.df_consolidado = pd.concat(dfs_com_clusters, ignore_index=True)
            print(f"✅ {len(self.df_consolidado)} projetos consolidados com clusters")
        else:
            print("⚠️ Nenhum dado consolidado disponível")
            self.df_consolidado = pd.DataFrame()
    
    def analisar_padroes_decisao(self):
        """Analisa padrões de decisão por área e cluster"""
        print("📊 Analisando padrões de decisão por área...")
        
        padroes_por_area = []
        padroes_cluster_detalhado = []
        
        for area, dados_area in self.dados_por_area.items():
            print(f"\n📈 Analisando área: {area[:40]}...")
            
            # Estatísticas gerais da área
            padrao_area = {
                'area_tecnologica': area,
                'total_projetos': len(dados_area),
                'num_clusters': dados_area['cluster_kmeans'].nunique(),
                'taxa_recomendado_area': 0,
                'num_analistas': 0,
                'analista_principal': None
            }
            
            # Análise de aprovação para a área
            if 'do_taaproj_notipoavaliacaoanalise' in dados_area.columns:
                resultados_validos = dados_area['do_taaproj_notipoavaliacaoanalise'].dropna()
                if len(resultados_validos) > 0:
                    recomendados = resultados_validos.apply(
                        lambda x: str(x).strip().lower() == 'recomendado'
                    ).sum()
                    padrao_area['taxa_recomendado_area'] = (recomendados / len(resultados_validos)) * 100
            
            # Análise de analistas na área
            if 'do_saat_idunicopessoaanalise' in dados_area.columns:
                analistas = dados_area['do_saat_idunicopessoaanalise'].value_counts()
                padrao_area['num_analistas'] = dados_area['do_saat_idunicopessoaanalise'].nunique()
                if not analistas.empty:
                    padrao_area['analista_principal'] = analistas.index[0]
            
            padroes_por_area.append(padrao_area)
            
            # Análise detalhada por cluster dentro da área
            for cluster_id in sorted(dados_area['cluster_kmeans'].unique()):
                cluster_data = dados_area[dados_area['cluster_kmeans'] == cluster_id]
                
                padrao_cluster = {
                    'area_tecnologica': area,
                    'cluster_id': cluster_id,
                    'cluster_global': f"{area[:20]}_{cluster_id}",
                    'tamanho': len(cluster_data),
                    'percentual_area': len(cluster_data) / len(dados_area) * 100,
                    'taxa_recomendado': 0,
                    'taxa_nao_recomendado': 0,
                    'tipo_projeto_principal': cluster_data['tipo_projeto'].mode().iloc[0] if not cluster_data['tipo_projeto'].mode().empty else 'N/A',
                    'porte_empresa_principal': cluster_data['porte_empresa'].mode().iloc[0] if not cluster_data['porte_empresa'].mode().empty else 'N/A',
                    'num_analistas_cluster': 0,
                    'concentracao_analista': 0
                }
                
                # Análise de aprovação do cluster
                if 'do_taaproj_notipoavaliacaoanalise' in cluster_data.columns:
                    resultados_validos = cluster_data['do_taaproj_notipoavaliacaoanalise'].dropna()
                    if len(resultados_validos) > 0:
                        recomendados = resultados_validos.apply(
                            lambda x: str(x).strip().lower() == 'recomendado'
                        ).sum()
                        nao_recomendados = resultados_validos.apply(
                            lambda x: 'não recomendado' in str(x).strip().lower()
                        ).sum()
                        
                        total_analisados = len(resultados_validos)
                        padrao_cluster['taxa_recomendado'] = (recomendados / total_analisados) * 100
                        padrao_cluster['taxa_nao_recomendado'] = (nao_recomendados / total_analisados) * 100
                
                # Análise de analistas do cluster
                if 'do_saat_idunicopessoaanalise' in cluster_data.columns:
                    analistas = cluster_data['do_saat_idunicopessoaanalise'].value_counts()
                    padrao_cluster['num_analistas_cluster'] = cluster_data['do_saat_idunicopessoaanalise'].nunique()
                    if not analistas.empty:
                        padrao_cluster['concentracao_analista'] = (analistas.iloc[0] / len(cluster_data)) * 100
                
                padroes_cluster_detalhado.append(padrao_cluster)
        
        # Salvar resultados
        self.resultados_analise['padroes_por_area'] = pd.DataFrame(padroes_por_area)
        self.resultados_analise['padroes_cluster_detalhado'] = pd.DataFrame(padroes_cluster_detalhado)
        
        # Análise de analistas consolidada
        self._analisar_analistas_consolidado()
        
        return self.resultados_analise
    
    def _analisar_analistas_consolidado(self):
        """Análise consolidada de analistas considerando todas as áreas"""
        print("👥 Analisando performance de analistas...")
        
        if hasattr(self, 'df_consolidado') and not self.df_consolidado.empty:
            padroes_analista = []
            
            for analista_id in self.df_consolidado['do_saat_idunicopessoaanalise'].unique():
                if pd.notna(analista_id):
                    projetos_analista = self.df_consolidado[self.df_consolidado['do_saat_idunicopessoaanalise'] == analista_id]
                    
                    padrao_analista = {
                        'analista_id': analista_id,
                        'num_projetos': len(projetos_analista),
                        'areas_atendidas': projetos_analista['area_tecnologica'].nunique(),
                        'clusters_atendidos': projetos_analista['cluster_global'].nunique(),
                        'area_especializada': projetos_analista['area_tecnologica'].mode().iloc[0] if not projetos_analista['area_tecnologica'].mode().empty else 'N/A',
                        'taxa_aprovacao': 0,
                        'total_analisados': 0,
                        'total_recomendados': 0
                    }
                    
                    # Taxa de aprovação
                    if 'do_taaproj_notipoavaliacaoanalise' in projetos_analista.columns:
                        resultados_validos = projetos_analista['do_taaproj_notipoavaliacaoanalise'].dropna()
                        
                        if len(resultados_validos) > 0:
                            recomendados = resultados_validos.apply(
                                lambda x: str(x).strip().lower() == 'recomendado'
                            ).sum()
                            
                            total_analisados = len(resultados_validos)
                            padrao_analista['total_analisados'] = total_analisados
                            padrao_analista['total_recomendados'] = recomendados
                            padrao_analista['taxa_aprovacao'] = (recomendados / total_analisados) * 100
                    
                    padroes_analista.append(padrao_analista)
            
            self.resultados_analise['padroes_analista'] = pd.DataFrame(padroes_analista)
            
            # Estatísticas
            df_analistas = self.resultados_analise['padroes_analista']
            print(f"   Taxa média de aprovação: {df_analistas['taxa_aprovacao'].mean():.1f}%")
            print(f"   Analistas especializados (1 área): {len(df_analistas[df_analistas['areas_atendidas'] == 1])}")
            print(f"   Analistas multidisciplinares (2+ áreas): {len(df_analistas[df_analistas['areas_atendidas'] > 1])}")
    
    def criar_visualizacoes(self):
        """Cria visualizações dos clusters por área"""
        print("📈 Criando visualizações por área...")
        
        # Criar pasta para imagens do relatório
        pasta_imagens = Path("imagens_relatorio")
        pasta_imagens.mkdir(exist_ok=True)
        
        plt.style.use('seaborn-v0_8-darkgrid')
        fig_paths = []
        
        # 1. Silhouette scores por área
        fig, ax = plt.subplots(figsize=(15, 8))
        
        areas_ordenadas = []
        k_otimos = []
        silhouettes = []
        
        for area, resultado in self.resultados_analise['kmeans_por_area'].items():
            areas_ordenadas.append(area[:25] + '...' if len(area) > 25 else area)
            k_otimos.append(resultado['k_optimal'])
            silhouettes.append(resultado['best_silhouette'])
        
        # Ordenar por silhouette score
        indices_ordenados = np.argsort(silhouettes)[::-1]
        areas_ordenadas = [areas_ordenadas[i] for i in indices_ordenados]
        k_otimos = [k_otimos[i] for i in indices_ordenados]
        silhouettes = [silhouettes[i] for i in indices_ordenados]
        
        colors = plt.cm.viridis(np.linspace(0, 1, len(areas_ordenadas)))
        bars = ax.barh(range(len(areas_ordenadas)), silhouettes, color=colors)
        
        # Adicionar valores nas barras
        for i, (bar, k, score) in enumerate(zip(bars, k_otimos, silhouettes)):
            width = bar.get_width()
            ax.text(width + 0.01, bar.get_y() + bar.get_height()/2,
                   f'K={k} ({score:.3f})',
                   ha='left', va='center', fontsize=9, fontweight='bold')
        
        ax.set_yticks(range(len(areas_ordenadas)))
        ax.set_yticklabels(areas_ordenadas, fontsize=10)
        ax.set_xlabel('Silhouette Score', fontsize=12)
        ax.set_title('K Ótimo e Silhouette Score por Área Tecnológica', fontsize=14, fontweight='bold')
        ax.grid(True, axis='x', alpha=0.3)
        
        plt.tight_layout()
        fig_path = pasta_imagens / 'silhouette_por_area.png'
        plt.savefig(fig_path, dpi=300, bbox_inches='tight')
        fig_paths.append(str(fig_path))
        plt.close()
        
        # 2. Distribuição de projetos por área
        if 'padroes_por_area' in self.resultados_analise:
            fig, ax = plt.subplots(figsize=(14, 8))
            
            df_areas = self.resultados_analise['padroes_por_area'].sort_values('total_projetos', ascending=True)
            
            colors = plt.cm.Set3(np.linspace(0, 1, len(df_areas)))
            bars = ax.barh(range(len(df_areas)), df_areas['total_projetos'], color=colors)
            
            # Adicionar valores nas barras
            for i, (bar, clusters) in enumerate(zip(bars, df_areas['num_clusters'])):
                width = bar.get_width()
                ax.text(width + 5, bar.get_y() + bar.get_height()/2,
                       f'{int(width)} projetos\n{clusters} clusters',
                       ha='left', va='center', fontsize=9)
            
            # Labels das áreas (truncadas)
            areas_truncadas = [area[:30] + '...' if len(area) > 30 else area 
                             for area in df_areas['area_tecnologica']]
            
            ax.set_yticks(range(len(df_areas)))
            ax.set_yticklabels(areas_truncadas, fontsize=10)
            ax.set_xlabel('Número de Projetos', fontsize=12)
            ax.set_title('Distribuição de Projetos e Clusters por Área Tecnológica', fontsize=14, fontweight='bold')
            ax.grid(True, axis='x', alpha=0.3)
            
            plt.tight_layout()
            fig_path = pasta_imagens / 'distribuicao_projetos_area.png'
            plt.savefig(fig_path, dpi=300, bbox_inches='tight')
            fig_paths.append(str(fig_path))
            plt.close()
        
        # 3. Heatmap de taxas de aprovação por área
        if 'padroes_por_area' in self.resultados_analise:
            fig, ax = plt.subplots(figsize=(12, 8))
            
            df_areas = self.resultados_analise['padroes_por_area']
            
            # Preparar dados para heatmap
            heatmap_data = df_areas[['taxa_recomendado_area', 'num_analistas', 'num_clusters']].fillna(0)
            
            # Normalizar para percentuais/escalas comparáveis
            heatmap_data_norm = heatmap_data.copy()
            heatmap_data_norm['num_analistas_norm'] = (heatmap_data_norm['num_analistas'] / heatmap_data_norm['num_analistas'].max()) * 100
            heatmap_data_norm['num_clusters_norm'] = (heatmap_data_norm['num_clusters'] / heatmap_data_norm['num_clusters'].max()) * 100
            
            heatmap_final = heatmap_data_norm[['taxa_recomendado_area', 'num_analistas_norm', 'num_clusters_norm']]
            
            # Truncar nomes das áreas para o heatmap
            areas_labels = [area[:25] + '...' if len(area) > 25 else area 
                           for area in df_areas['area_tecnologica']]
            
            sns.heatmap(heatmap_final.T, 
                       xticklabels=areas_labels,
                       yticklabels=['Taxa Aprovação (%)', 'Analistas (% max)', 'Clusters (% max)'],
                       annot=True, 
                       fmt='.1f',
                       cmap='RdYlBu_r',
                       cbar_kws={'label': 'Valor Normalizado (%)'},
                       linewidths=0.5)
            
            ax.set_xlabel('Área Tecnológica', fontsize=12)
            ax.set_title('Características por Área Tecnológica', fontsize=14, fontweight='bold')
            plt.xticks(rotation=45, ha='right')
            
            plt.tight_layout()
            fig_path = pasta_imagens / 'heatmap_areas.png'
            plt.savefig(fig_path, dpi=300, bbox_inches='tight')
            fig_paths.append(str(fig_path))
            plt.close()
        
        self.fig_paths = fig_paths
        return fig_paths
    
    def gerar_relatorio_pdf(self, nome_arquivo='2.relatorio_clusters_lei_bem_por_area.pdf'):
        """Gera relatório em PDF com análises por área"""
        print("📄 Gerando relatório PDF...")
        
        # Criar pasta de análises se não existir
        pasta_analises = Path("./Analises")
        pasta_analises.mkdir(exist_ok=True)
        
        # Caminho completo do arquivo PDF
        caminho_arquivo = pasta_analises / nome_arquivo
        
        doc = SimpleDocTemplate(str(caminho_arquivo), pagesize=A4)
        story = []
        styles = getSampleStyleSheet()
        
        # Estilos customizados
        titulo_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1f4788'),
            spaceAfter=30,
            alignment=1  # Centro
        )
        
        subtitulo_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#2e5090'),
            spaceBefore=20,
            spaceAfter=15
        )
        
        # Título
        story.append(Paragraph("Análise de Clusters por Área Tecnológica - Lei do Bem", titulo_style))
        story.append(Spacer(1, 0.2*inch))
        
        # Data e estatísticas gerais
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        total_projetos = sum([resultado['num_projetos'] for resultado in self.resultados_analise['kmeans_por_area'].values()])
        total_areas = len(self.resultados_analise['kmeans_por_area'])
        
        story.append(Paragraph(f"<b>Data da Análise:</b> {data_atual}", styles['Normal']))
        story.append(Paragraph(f"<b>Total de Projetos Analisados:</b> {total_projetos:,}", styles['Normal']))
        story.append(Paragraph(f"<b>Total de Áreas Tecnológicas:</b> {total_areas}", styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # 1. Metodologia
        story.append(Paragraph("1. Metodologia de Análise por Área", subtitulo_style))
        metodologia_text = """
        A análise foi reformulada para considerar as especificidades de cada área tecnológica:
        
        • <b>Segmentação por Área:</b> Os projetos foram divididos por área tecnológica antes 
        da aplicação do clustering, reconhecendo que cada área tem características únicas.
        
        • <b>K-Means Otimizado por Área:</b> Para cada área, foi aplicado K-Means com K variando 
        de 2 a 20, selecionando o K ótimo baseado no Silhouette Score.
        
        • <b>Embeddings Especializados:</b> Utilizando modelo SERAFIM (português), foram criadas 
        representações vetoriais considerando o contexto específico de cada área.
        
        • <b>Análise Multidimensional:</b> Padrões de decisão, distribuição de analistas e 
        características dos projetos foram analisados dentro do contexto de cada área.
        """
        story.append(Paragraph(metodologia_text, styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        # Adicionar gráfico de silhouette
        if hasattr(self, 'fig_paths') and len(self.fig_paths) > 0:
            img = Image(self.fig_paths[0], width=6*inch, height=3*inch)
            story.append(img)
        
        story.append(PageBreak())
        
        # 2. Resultados por Área
        story.append(Paragraph("2. Resultados da Clusterização por Área", subtitulo_style))
        
        # Tabela resumo das áreas
        if 'padroes_por_area' in self.resultados_analise:
            df_areas = self.resultados_analise['padroes_por_area'].sort_values('total_projetos', ascending=False).head(10)
            
            data_table = [['Área Tecnológica', 'Projetos', 'Clusters', 'Taxa Aprov.', 'Analistas']]
            for _, row in df_areas.iterrows():
                area_truncada = row['area_tecnologica'][:40] + '...' if len(row['area_tecnologica']) > 40 else row['area_tecnologica']
                data_table.append([
                    area_truncada,
                    str(int(row['total_projetos'])),
                    str(int(row['num_clusters'])),
                    f"{row['taxa_recomendado_area']:.1f}%" if row['taxa_recomendado_area'] > 0 else 'N/A',
                    str(int(row['num_analistas']))
                ])
            
            t = Table(data_table, colWidths=[2.5*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
            ]))
            
            story.append(Paragraph("<b>Top 10 Áreas por Volume de Projetos:</b>", styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
            story.append(t)
        
        # Adicionar gráfico de distribuição
        if hasattr(self, 'fig_paths') and len(self.fig_paths) > 1:
            story.append(Spacer(1, 0.3*inch))
            img = Image(self.fig_paths[1], width=5.5*inch, height=3.5*inch)
            story.append(img)
        
        story.append(PageBreak())
        
        # 3. Análise de Padrões
        story.append(Paragraph("3. Padrões Identificados por Área", subtitulo_style))
        
        # Insights baseados nos dados
        insights_text = """
        A segmentação por área tecnológica revelou padrões específicos:
        """
        story.append(Paragraph(insights_text, styles['Normal']))
        
        if 'padroes_por_area' in self.resultados_analise:
            df_areas = self.resultados_analise['padroes_por_area']
            
            # Áreas com alta taxa de aprovação
            areas_alta_aprovacao = df_areas[df_areas['taxa_recomendado_area'] > 80]
            if not areas_alta_aprovacao.empty:
                story.append(Paragraph("<b>• Áreas com Alta Taxa de Aprovação (>80%):</b>", styles['Normal']))
                for _, area in areas_alta_aprovacao.iterrows():
                    texto = f"  - {area['area_tecnologica'][:50]}... " \
                           f"({area['taxa_recomendado_area']:.1f}% aprovação, {area['total_projetos']} projetos)"
                    story.append(Paragraph(texto, styles['Normal']))
                story.append(Spacer(1, 0.1*inch))
            
            # Áreas com muitos clusters
            areas_complexas = df_areas[df_areas['num_clusters'] >= 5]
            if not areas_complexas.empty:
                story.append(Paragraph("<b>• Áreas com Alta Diversidade (≥5 clusters):</b>", styles['Normal']))
                for _, area in areas_complexas.iterrows():
                    texto = f"  - {area['area_tecnologica'][:50]}... " \
                           f"({area['num_clusters']} clusters, {area['total_projetos']} projetos)"
                    story.append(Paragraph(texto, styles['Normal']))
                story.append(Spacer(1, 0.1*inch))
        
        # Heatmap
        if hasattr(self, 'fig_paths') and len(self.fig_paths) > 2:
            story.append(Spacer(1, 0.2*inch))
            img = Image(self.fig_paths[2], width=5.5*inch, height=3.5*inch)
            story.append(img)
        
        story.append(PageBreak())
        
        # 4. Análise de Analistas
        story.append(Paragraph("4. Especialização de Analistas por Área", subtitulo_style))
        
        if 'padroes_analista' in self.resultados_analise:
            df_analistas = self.resultados_analise['padroes_analista'].sort_values('num_projetos', ascending=False).head(10)
            
            data_table = [['ID Analista', 'Projetos', 'Áreas', 'Clusters', 'Especialização']]
            for _, row in df_analistas.iterrows():
                especializacao = row['area_especializada'][:30] + '...' if len(str(row['area_especializada'])) > 30 else row['area_especializada']
                data_table.append([
                    str(int(row['analista_id'])),
                    str(int(row['num_projetos'])),
                    str(int(row['areas_atendidas'])),
                    str(int(row['clusters_atendidos'])),
                    especializacao
                ])
            
            t = Table(data_table, colWidths=[1*inch, 0.8*inch, 0.8*inch, 0.8*inch, 2.3*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
            ]))
            
            story.append(Paragraph("<b>Top 10 Analistas por Volume:</b>", styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
            story.append(t)
        
        story.append(PageBreak())
        
        # 5. Recomendações
        story.append(Paragraph("5. Recomendações Específicas por Área", subtitulo_style))
        
        recomendacoes = self._gerar_recomendacoes_por_area()
        for i, rec in enumerate(recomendacoes, 1):
            story.append(Paragraph(f"<b>{i}. {rec['titulo']}</b>", styles['Normal']))
            story.append(Paragraph(rec['descricao'], styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
        
        # Construir PDF
        doc.build(story)
        print(f"✅ Relatório PDF gerado: {caminho_arquivo}")
    
    def _gerar_recomendacoes_por_area(self) -> list[dict[str, str]]:
        """Gera recomendações específicas baseadas na análise por área"""
        recomendacoes = []
        
        if 'padroes_por_area' in self.resultados_analise:
            df_areas = self.resultados_analise['padroes_por_area']
            
            # 1. Especialização por área
            areas_grandes = df_areas[df_areas['total_projetos'] >= 50]
            if not areas_grandes.empty:
                recomendacoes.append({
                    'titulo': 'Criar Grupos de Especialistas por Área Tecnológica',
                    'descricao': f'Identificadas {len(areas_grandes)} áreas com volume significativo '
                               f'(≥50 projetos). Formar equipes especializadas para cada área pode '
                               'aumentar a qualidade e velocidade das análises.'
                })
            
            # 2. Padronização em áreas complexas
            areas_complexas = df_areas[df_areas['num_clusters'] >= 5]
            if not areas_complexas.empty:
                recomendacoes.append({
                    'titulo': 'Desenvolver Critérios Específicos para Áreas Complexas',
                    'descricao': f'{len(areas_complexas)} áreas apresentam alta diversidade interna '
                               f'(≥5 clusters). Criar critérios de avaliação específicos para cada '
                               'subgrupo pode reduzir inconsistências.'
                })
            
            # 3. Revisão de áreas com baixa aprovação
            areas_baixa_aprovacao = df_areas[df_areas['taxa_recomendado_area'] < 60]
            if not areas_baixa_aprovacao.empty:
                recomendacoes.append({
                    'titulo': 'Revisar Critérios para Áreas com Baixa Aprovação',
                    'descricao': f'{len(areas_baixa_aprovacao)} áreas apresentam taxa de aprovação '
                               'abaixo de 60%. Investigar se os critérios são adequados ou se há '
                               'necessidade de capacitação específica.'
                })
            
            # 4. Otimização de recursos
            total_areas = len(df_areas)
            if total_areas > 20:
                recomendacoes.append({
                    'titulo': 'Implementar Sistema de Triagem Inteligente',
                    'descricao': f'Com {total_areas} áreas tecnológicas identificadas, um sistema de '
                               'IA para pré-classificação e direcionamento automático pode otimizar '
                               'significativamente o fluxo de trabalho.'
                })
        
        # 5. Monitoramento contínuo por área
        recomendacoes.append({
            'titulo': 'Estabelecer KPIs Específicos por Área',
            'descricao': 'Criar dashboards com métricas específicas para cada área tecnológica, '
                       'incluindo tempo médio de análise, taxa de aprovação e distribuição de carga '
                       'entre analistas especializados.'
        })
        
        return recomendacoes
    
    def exportar_resultados_detalhados(self, prefixo='2.lei_bem'):
        """Exporta todos os resultados detalhados"""
        print("💾 Exportando resultados detalhados...")
        
        # Criar pasta de análises se não existir
        pasta_analises = Path("./Analises")
        pasta_analises.mkdir(exist_ok=True)
        
        # 1. DataFrame consolidado com clusters
        if hasattr(self, 'df_consolidado') and not self.df_consolidado.empty:
            self.df_consolidado.to_csv(pasta_analises / f'{prefixo}_projetos_clusters_por_area.csv', 
                                     index=False, sep=';', encoding='utf-8')
        
        # 2. Análise por área
        if 'padroes_por_area' in self.resultados_analise:
            self.resultados_analise['padroes_por_area'].to_csv(
                pasta_analises / f'{prefixo}_analise_areas.csv', index=False, sep=';', encoding='utf-8'
            )
        
        # 3. Análise detalhada de clusters
        if 'padroes_cluster_detalhado' in self.resultados_analise:
            self.resultados_analise['padroes_cluster_detalhado'].to_csv(
                pasta_analises / f'{prefixo}_analise_clusters_por_area.csv', index=False, sep=';', encoding='utf-8'
            )
        
        # 4. Análise de analistas
        if 'padroes_analista' in self.resultados_analise:
            self.resultados_analise['padroes_analista'].to_csv(
                pasta_analises / f'{prefixo}_analise_analistas_por_area.csv', index=False, sep=';', encoding='utf-8'
            )
        
        # 5. Métricas por área
        import json
        metricas_areas = {}
        for area, resultado in self.resultados_analise['kmeans_por_area'].items():
            metricas_areas[area] = {
                'k_optimal': int(resultado['k_optimal']),
                'best_silhouette': float(resultado['best_silhouette']),
                'num_projetos': int(resultado['num_projetos'])
            }
        
        with open(pasta_analises / f'{prefixo}_metricas_areas.json', 'w', encoding='utf-8') as f:
            json.dump(metricas_areas, f, indent=2, ensure_ascii=False)
        
        print("✅ Todos os resultados exportados")


def main():
    """Função principal para executar análise completa por área"""
    print("🚀 Análise Avançada de Clusters por Área Tecnológica - Lei do Bem")
    print("=" * 70)
    
    # Inicializar analisador
    analisador = AnalisadorClusterAvancado()
    
    # Encontrar arquivo CSV
    pasta_tabelas = Path("csv_longo")
    arquivos_csv = list(pasta_tabelas.glob("*.csv"))
    
    if not arquivos_csv:
        print("❌ Nenhum arquivo CSV encontrado")
        return
    
    print(f"📁 Usando arquivo: {arquivos_csv[0].name}")
    
    # Pipeline de análise
    # 1. Carregar dados
    analisador.carregar_dados(str(arquivos_csv[0]))
    
    # 2. Criar embeddings por área
    analisador.criar_embeddings_por_area()
    
    # 3. Aplicar K-Means por área (K entre 2-20, usando Silhouette)
    analisador.analisar_kmeans_por_area(max_k=20)
    
    # 4. Analisar padrões de decisão
    analisador.analisar_padroes_decisao()
    
    # 5. Criar visualizações
    analisador.criar_visualizacoes()
    
    # 6. Gerar relatório PDF
    analisador.gerar_relatorio_pdf()
    
    # 7. Exportar resultados detalhados
    analisador.exportar_resultados_detalhados()
    
    print("\n✅ Análise completa!")
    print("📊 Arquivos gerados:")
    print("   - ./Analises/relatorio_clusters_lei_bem_por_area.pdf (Relatório completo)")
    print("   - ./Analises/lei_bem_projetos_clusters_por_area.csv (Projetos com clusters)")
    print("   - ./Analises/lei_bem_analise_areas.csv (Análise por área)")
    print("   - ./Analises/lei_bem_analise_clusters_por_area.csv (Características dos clusters)")
    print("   - ./Analises/lei_bem_analise_analistas_por_area.csv (Análise por analista)")
    print("   - ./Analises/lei_bem_metricas_areas.json (Métricas por área)")
    print("   - imagens_relatorio/ (Pasta com visualizações)")
    
    return analisador


if __name__ == "__main__":
    analisador = main()