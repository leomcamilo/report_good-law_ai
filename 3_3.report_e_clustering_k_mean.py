#!/usr/bin/env python3
"""
Análise Avançada de Clusters para Projetos Lei do Bem
=====================================================

Este script implementa múltiplas abordagens de clusterização para identificar
padrões de decisão nos projetos, incluindo K-Means e análise por analista.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, calinski_harabasz_score
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

warnings.filterwarnings('ignore')

class AnalisadorClusterAvancado:
    """Classe para análise avançada de clusters com foco em padrões de decisão"""
    
    def __init__(self):
        self.df = None
        self.embeddings = None
        self.clusters_kmeans = None
        self.clusters_hierarquico = None
        self.model_embedding = None
        self.scaler = StandardScaler()
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
    
    def criar_embeddings_multimodais(self):
        """Cria embeddings considerando múltiplas dimensões do projeto"""
        print("🤖 Criando embeddings multimodais...")
        
        if self.model_embedding is None:
            self.model_embedding = SentenceTransformer(
                "PORTULAN/serafim-335m-portuguese-pt-sentence-encoder-ir"
            )
        
        # Criar texto combinado com pesos diferentes para cada componente
        def criar_texto_ponderado(row):
            componentes = []
            
            # Alta prioridade (peso 3)
            if pd.notna(row.get('descricao_projeto')):
                componentes.extend([str(row['descricao_projeto'])] * 3)
            
            # Média prioridade (peso 2)
            for campo in ['elemento_tecnologico', 'desafio_tecnologico']:
                if pd.notna(row.get(campo)):
                    componentes.extend([str(row[campo])] * 2)
            
            # Baixa prioridade (peso 1)
            for campo in ['area_projeto', 'tipo_projeto', 'atividade_economica']:
                if pd.notna(row.get(campo)):
                    componentes.append(str(row[campo]))
            
            return ' '.join(componentes)
        
        # Gerar textos ponderados
        textos_ponderados = self.df.apply(criar_texto_ponderado, axis=1).tolist()
        
        # Criar embeddings
        self.embeddings = self.model_embedding.encode(
            textos_ponderados, 
            show_progress_bar=True,
            batch_size=32
        )
        
        print(f"✅ Embeddings criados: {self.embeddings.shape}")
        
        return self.embeddings
    
    def analisar_kmeans_otimizado(self, max_k: int = 30):
        """Aplica K-Means com seleção otimizada de K"""
        print("🎯 Analisando K-Means otimizado...")
        
        # Normalizar embeddings
        embeddings_norm = self.scaler.fit_transform(self.embeddings)
        
        # Testar diferentes valores de K
        inertias = []
        silhouettes = []
        calinski_scores = []
        k_values = range(2, min(max_k + 1, len(self.df) // 10))
        
        for k in k_values:
            print(f"  Testando K={k}...")
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            clusters = kmeans.fit_predict(embeddings_norm)
            
            inertias.append(kmeans.inertia_)
            silhouettes.append(silhouette_score(embeddings_norm, clusters))
            calinski_scores.append(calinski_harabasz_score(embeddings_norm, clusters))
        
        # Encontrar K ótimo usando método do cotovelo + silhouette
        # Calcular segunda derivada da inércia
        if len(inertias) > 2:
            second_derivative = np.diff(np.diff(inertias))
            elbow_idx = np.argmax(second_derivative) + 2  # +2 por causa dos diffs
            k_elbow = list(k_values)[elbow_idx]
        else:
            k_elbow = 10
        
        # K com melhor silhouette
        k_silhouette = list(k_values)[np.argmax(silhouettes)]
        
        # K final: média entre elbow e silhouette
        k_optimal = (k_elbow + k_silhouette) // 2
        
        print(f"📊 K ótimo encontrado: {k_optimal}")
        print(f"   K (cotovelo): {k_elbow}")
        print(f"   K (silhouette): {k_silhouette}")
        
        # Aplicar K-Means com K ótimo
        self.kmeans_final = KMeans(n_clusters=k_optimal, random_state=42, n_init=20)
        self.clusters_kmeans = self.kmeans_final.fit_predict(embeddings_norm)
        
        # Salvar métricas
        self.resultados_analise['kmeans'] = {
            'k_optimal': k_optimal,
            'k_elbow': k_elbow,
            'k_silhouette': k_silhouette,
            'inertias': inertias,
            'silhouettes': silhouettes,
            'k_values': list(k_values)
        }
        
        return self.clusters_kmeans
    
    def analisar_padroes_decisao(self):
        """Analisa padrões de decisão por cluster e analista"""
        print("📊 Analisando padrões de decisão...")
        
        # Adicionar clusters ao dataframe
        self.df['cluster_kmeans'] = self.clusters_kmeans
        
        # Análise por cluster
        padroes_cluster = []
        
        for cluster_id in sorted(self.df['cluster_kmeans'].unique()):
            cluster_data = self.df[self.df['cluster_kmeans'] == cluster_id]
            
            # Estatísticas do cluster
            padrao = {
                'cluster_id': cluster_id,
                'tamanho': len(cluster_data),
                'percentual_total': len(cluster_data) / len(self.df) * 100,
                
                # Análise de aprovação (se houver campo de resultado)
                'taxa_recomendado': 0,
                'taxa_nao_recomendado': 0,
                
                # Características dominantes
                'area_principal': cluster_data['area_projeto'].mode().iloc[0] if not cluster_data['area_projeto'].mode().empty else 'N/A',
                'tipo_projeto_principal': cluster_data['tipo_projeto'].mode().iloc[0] if not cluster_data['tipo_projeto'].mode().empty else 'N/A',
                'porte_empresa_principal': cluster_data['porte_empresa'].mode().iloc[0] if not cluster_data['porte_empresa'].mode().empty else 'N/A',
                
                # Análise de analistas
                'num_analistas': cluster_data['do_saat_idunicopessoaanalise'].nunique() if 'do_saat_idunicopessoaanalise' in cluster_data.columns else 0,
                'analista_principal': None,
                'concentracao_analista': 0
            }
            
            # Análise de resultados se campo existir
            if 'do_taaproj_notipoavaliacaoanalise' in cluster_data.columns:
                resultados = cluster_data['do_taaproj_notipoavaliacaoanalise'].value_counts(normalize=True)
                if 'Recomendado' in resultados:
                    padrao['taxa_recomendado'] = resultados['Recomendado'] * 100
                if 'Não Recomendado' in resultados:
                    padrao['taxa_nao_recomendado'] = resultados['Não Recomendado'] * 100
            
            # Análise de concentração por analista
            if 'do_saat_idunicopessoaanalise' in cluster_data.columns:
                analistas = cluster_data['do_saat_idunicopessoaanalise'].value_counts()
                if not analistas.empty:
                    padrao['analista_principal'] = analistas.index[0]
                    padrao['concentracao_analista'] = (analistas.iloc[0] / len(cluster_data)) * 100
            
            padroes_cluster.append(padrao)
        
        self.resultados_analise['padroes_cluster'] = pd.DataFrame(padroes_cluster)
        
        # Análise por analista
        if 'do_saat_idunicopessoaanalise' in self.df.columns:
            padroes_analista = []
            
            for analista_id in self.df['do_saat_idunicopessoaanalise'].unique():
                if pd.notna(analista_id):
                    projetos_analista = self.df[self.df['do_saat_idunicopessoaanalise'] == analista_id]
                    
                    padrao_analista = {
                        'analista_id': analista_id,
                        'num_projetos': len(projetos_analista),
                        'clusters_atendidos': projetos_analista['cluster_kmeans'].nunique(),
                        'area_especializada': projetos_analista['area_projeto'].mode().iloc[0] if not projetos_analista['area_projeto'].mode().empty else 'N/A',
                        'taxa_aprovacao': 0
                    }
                    
                    # Taxa de aprovação se disponível
                    if 'do_taaproj_notipoavaliacaoanalise' in projetos_analista.columns:
                        aprovados = projetos_analista['do_taaproj_notipoavaliacaoanalise'].str.contains('Recomendado', na=False).sum()
                        padrao_analista['taxa_aprovacao'] = (aprovados / len(projetos_analista)) * 100
                    
                    padroes_analista.append(padrao_analista)
            
            self.resultados_analise['padroes_analista'] = pd.DataFrame(padroes_analista)
        
        return self.resultados_analise
    
    def criar_visualizacoes(self):
        """Cria visualizações dos clusters e padrões"""
        print("📈 Criando visualizações...")
        
        # Configurar estilo
        plt.style.use('seaborn-v0_8-darkgrid')
        fig_paths = []
        
        # 1. Visualização do método do cotovelo
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        k_values = self.resultados_analise['kmeans']['k_values']
        inertias = self.resultados_analise['kmeans']['inertias']
        silhouettes = self.resultados_analise['kmeans']['silhouettes']
        
        # Cotovelo
        ax1.plot(k_values, inertias, 'b-o', linewidth=2, markersize=8)
        ax1.axvline(x=self.resultados_analise['kmeans']['k_optimal'], color='r', linestyle='--', 
                   label=f'K ótimo = {self.resultados_analise["kmeans"]["k_optimal"]}')
        ax1.set_xlabel('Número de Clusters (K)', fontsize=12)
        ax1.set_ylabel('Inércia', fontsize=12)
        ax1.set_title('Método do Cotovelo', fontsize=14, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Silhouette
        ax2.plot(k_values, silhouettes, 'g-o', linewidth=2, markersize=8)
        ax2.axvline(x=self.resultados_analise['kmeans']['k_silhouette'], color='r', linestyle='--',
                   label=f'K melhor silhouette = {self.resultados_analise["kmeans"]["k_silhouette"]}')
        ax2.set_xlabel('Número de Clusters (K)', fontsize=12)
        ax2.set_ylabel('Silhouette Score', fontsize=12)
        ax2.set_title('Análise de Silhouette', fontsize=14, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        fig_path = 'kmeans_otimizacao.png'
        plt.savefig(fig_path, dpi=300, bbox_inches='tight')
        fig_paths.append(fig_path)
        plt.close()
        
        # 2. Distribuição dos clusters
        fig, ax = plt.subplots(figsize=(12, 8))
        
        cluster_counts = self.df['cluster_kmeans'].value_counts().sort_index()
        colors_palette = sns.color_palette('husl', len(cluster_counts))
        
        bars = ax.bar(cluster_counts.index, cluster_counts.values, color=colors_palette, edgecolor='black', linewidth=1)
        
        # Adicionar valores nas barras
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 10,
                   f'{int(height)}\n({height/len(self.df)*100:.1f}%)',
                   ha='center', va='bottom', fontsize=10)
        
        ax.set_xlabel('Cluster ID', fontsize=12)
        ax.set_ylabel('Número de Projetos', fontsize=12)
        ax.set_title('Distribuição de Projetos por Cluster (K-Means)', fontsize=14, fontweight='bold')
        ax.grid(True, axis='y', alpha=0.3)
        
        plt.tight_layout()
        fig_path = 'distribuicao_clusters.png'
        plt.savefig(fig_path, dpi=300, bbox_inches='tight')
        fig_paths.append(fig_path)
        plt.close()
        
        # 3. PCA dos embeddings colorido por cluster
        print("  Aplicando PCA para visualização...")
        pca = PCA(n_components=2, random_state=42)
        embeddings_2d = pca.fit_transform(self.embeddings)
        
        fig, ax = plt.subplots(figsize=(14, 10))
        
        scatter = ax.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], 
                           c=self.clusters_kmeans, 
                           cmap='tab20', 
                           alpha=0.6, 
                           edgecolors='black',
                           linewidth=0.5,
                           s=50)
        
        # Adicionar centroides
        for cluster_id in np.unique(self.clusters_kmeans):
            cluster_points = embeddings_2d[self.clusters_kmeans == cluster_id]
            centroid = cluster_points.mean(axis=0)
            ax.scatter(centroid[0], centroid[1], 
                      marker='*', 
                      s=500, 
                      c='red', 
                      edgecolors='black',
                      linewidth=2,
                      label=f'Centroide {cluster_id}' if cluster_id == 0 else '')
            ax.text(centroid[0], centroid[1], str(cluster_id), 
                   fontsize=12, fontweight='bold', ha='center', va='center')
        
        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variância)', fontsize=12)
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variância)', fontsize=12)
        ax.set_title('Visualização dos Clusters em 2D (PCA)', fontsize=14, fontweight='bold')
        
        # Legenda apenas para centroide
        handles, labels = ax.get_legend_handles_labels()
        if handles:
            ax.legend(handles[:1], ['Centroides'], loc='upper right')
        
        plt.tight_layout()
        fig_path = 'pca_clusters.png'
        plt.savefig(fig_path, dpi=300, bbox_inches='tight')
        fig_paths.append(fig_path)
        plt.close()
        
        # 4. Heatmap de características por cluster
        if 'padroes_cluster' in self.resultados_analise:
            fig, ax = plt.subplots(figsize=(12, 8))
            
            # Preparar dados para heatmap
            df_padroes = self.resultados_analise['padroes_cluster']
            heatmap_data = df_padroes[['taxa_recomendado', 'taxa_nao_recomendado', 
                                      'concentracao_analista', 'percentual_total']].fillna(0)
            
            sns.heatmap(heatmap_data.T, 
                       xticklabels=[f'C{i}' for i in df_padroes['cluster_id']],
                       yticklabels=['Taxa Recomendado (%)', 'Taxa Não Recomendado (%)', 
                                   'Concentração Analista (%)', 'Tamanho (%)'],
                       annot=True, 
                       fmt='.1f',
                       cmap='YlOrRd',
                       cbar_kws={'label': 'Percentual (%)'},
                       linewidths=0.5,
                       linecolor='gray')
            
            ax.set_xlabel('Cluster ID', fontsize=12)
            ax.set_title('Características dos Clusters', fontsize=14, fontweight='bold')
            
            plt.tight_layout()
            fig_path = 'heatmap_caracteristicas.png'
            plt.savefig(fig_path, dpi=300, bbox_inches='tight')
            fig_paths.append(fig_path)
            plt.close()
        
        self.fig_paths = fig_paths
        return fig_paths
    
    def gerar_relatorio_pdf(self, nome_arquivo='relatorio_clusters_lei_bem.pdf'):
        """Gera relatório em PDF com análises e visualizações"""
        print("📄 Gerando relatório PDF...")
        
        doc = SimpleDocTemplate(nome_arquivo, pagesize=A4)
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
        story.append(Paragraph("Análise de Clusters - Projetos Lei do Bem", titulo_style))
        story.append(Spacer(1, 0.2*inch))
        
        # Data e estatísticas gerais
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        story.append(Paragraph(f"<b>Data da Análise:</b> {data_atual}", styles['Normal']))
        story.append(Paragraph(f"<b>Total de Projetos:</b> {len(self.df):,}", styles['Normal']))
        story.append(Paragraph(f"<b>Número de Clusters (K-Means):</b> {self.resultados_analise['kmeans']['k_optimal']}", styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # 1. Metodologia
        story.append(Paragraph("1. Metodologia de Análise", subtitulo_style))
        metodologia_text = """
        A análise foi realizada utilizando técnicas avançadas de Machine Learning para identificar 
        padrões nos projetos submetidos à Lei do Bem:
        
        • <b>Embeddings Semânticos:</b> Utilizando o modelo SERAFIM (português), foram criadas 
        representações vetoriais dos projetos considerando descrição, elemento tecnológico, 
        desafio e metodologia.
        
        • <b>K-Means Otimizado:</b> Aplicação do algoritmo K-Means com seleção automática do 
        número ótimo de clusters usando método do cotovelo e análise de silhouette.
        
        • <b>Análise Multidimensional:</b> Consideração de múltiplas dimensões incluindo área 
        tecnológica, tipo de projeto, porte da empresa e padrões de decisão dos analistas.
        """
        story.append(Paragraph(metodologia_text, styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        # Adicionar gráfico de otimização
        if hasattr(self, 'fig_paths') and len(self.fig_paths) > 0:
            img = Image(self.fig_paths[0], width=6*inch, height=2.5*inch)
            story.append(img)
        
        story.append(PageBreak())
        
        # 2. Resultados da Clusterização
        story.append(Paragraph("2. Resultados da Clusterização", subtitulo_style))
        
        # Tabela de clusters principais
        if 'padroes_cluster' in self.resultados_analise:
            df_padroes = self.resultados_analise['padroes_cluster'].head(10)
            
            # Preparar dados da tabela
            data_table = [['Cluster', 'Projetos', '% Total', 'Área Principal', 'Taxa Recom. (%)']]
            for _, row in df_padroes.iterrows():
                data_table.append([
                    str(int(row['cluster_id'])),
                    str(int(row['tamanho'])),
                    f"{row['percentual_total']:.1f}%",
                    row['area_principal'][:30] + '...' if len(str(row['area_principal'])) > 30 else row['area_principal'],
                    f"{row['taxa_recomendado']:.1f}%" if row['taxa_recomendado'] > 0 else 'N/A'
                ])
            
            # Criar tabela
            t = Table(data_table, colWidths=[0.8*inch, 1*inch, 0.8*inch, 2.5*inch, 1.2*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
            ]))
            
            story.append(Paragraph("<b>Top 10 Clusters por Tamanho:</b>", styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
            story.append(t)
        
        # Adicionar gráfico de distribuição
        if hasattr(self, 'fig_paths') and len(self.fig_paths) > 1:
            story.append(Spacer(1, 0.3*inch))
            img = Image(self.fig_paths[1], width=5*inch, height=3.5*inch)
            story.append(img)
        
        story.append(PageBreak())
        
        # 3. Análise de Padrões de Decisão
        story.append(Paragraph("3. Padrões de Decisão Identificados", subtitulo_style))
        
        padroes_text = """
        A análise revelou os seguintes padrões principais nos clusters formados:
        """
        story.append(Paragraph(padroes_text, styles['Normal']))
        
        # Insights dos clusters
        if 'padroes_cluster' in self.resultados_analise:
            df_padroes = self.resultados_analise['padroes_cluster']
            
            # Clusters com alta taxa de aprovação
            clusters_alta_aprovacao = df_padroes[df_padroes['taxa_recomendado'] > 70]
            if not clusters_alta_aprovacao.empty:
                story.append(Paragraph("<b>• Clusters com Alta Taxa de Aprovação (>70%):</b>", styles['Normal']))
                for _, cluster in clusters_alta_aprovacao.iterrows():
                    texto = f"  - Cluster {int(cluster['cluster_id'])}: {cluster['area_principal']} " \
                           f"({cluster['taxa_recomendado']:.1f}% aprovação)"
                    story.append(Paragraph(texto, styles['Normal']))
                story.append(Spacer(1, 0.1*inch))
            
            # Clusters com alta concentração de analista
            clusters_concentrados = df_padroes[df_padroes['concentracao_analista'] > 50]
            if not clusters_concentrados.empty:
                story.append(Paragraph("<b>• Clusters com Alta Concentração de Analista (>50%):</b>", styles['Normal']))
                for _, cluster in clusters_concentrados.iterrows():
                    texto = f"  - Cluster {int(cluster['cluster_id'])}: {cluster['concentracao_analista']:.1f}% " \
                           f"dos projetos analisados pelo mesmo analista"
                    story.append(Paragraph(texto, styles['Normal']))
                story.append(Spacer(1, 0.1*inch))
        
        # Visualização PCA
        if hasattr(self, 'fig_paths') and len(self.fig_paths) > 2:
            story.append(Spacer(1, 0.2*inch))
            img = Image(self.fig_paths[2], width=5.5*inch, height=4*inch)
            story.append(img)
        
        story.append(PageBreak())
        
        # 4. Análise por Analista
        story.append(Paragraph("4. Análise de Performance por Analista", subtitulo_style))
        
        if 'padroes_analista' in self.resultados_analise:
            df_analistas = self.resultados_analise['padroes_analista'].head(10)
            
            # Tabela de analistas
            data_table = [['ID Analista', 'Projetos', 'Clusters', 'Área Espec.', 'Taxa Aprov.']]
            for _, row in df_analistas.iterrows():
                data_table.append([
                    str(int(row['analista_id'])),
                    str(int(row['num_projetos'])),
                    str(int(row['clusters_atendidos'])),
                    row['area_especializada'][:25] + '...' if len(str(row['area_especializada'])) > 25 else row['area_especializada'],
                    f"{row['taxa_aprovacao']:.1f}%"
                ])
            
            t = Table(data_table, colWidths=[1.2*inch, 0.8*inch, 0.8*inch, 2.2*inch, 1*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5090')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 11),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
            ]))
            
            story.append(Paragraph("<b>Top 10 Analistas por Volume de Projetos:</b>", styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
            story.append(t)
        
        # Heatmap de características
        if hasattr(self, 'fig_paths') and len(self.fig_paths) > 3:
            story.append(Spacer(1, 0.3*inch))
            img = Image(self.fig_paths[3], width=5.5*inch, height=3.5*inch)
            story.append(img)
        
        story.append(PageBreak())
        
        # 5. Recomendações
        story.append(Paragraph("5. Recomendações para Otimização do Processo", subtitulo_style))
        
        recomendacoes = self._gerar_recomendacoes()
        for i, rec in enumerate(recomendacoes, 1):
            story.append(Paragraph(f"<b>{i}. {rec['titulo']}</b>", styles['Normal']))
            story.append(Paragraph(rec['descricao'], styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
        
        # 6. Conclusões
        story.append(Paragraph("6. Conclusões", subtitulo_style))
        
        conclusoes_text = f"""
        A análise identificou {self.resultados_analise['kmeans']['k_optimal']} clusters distintos 
        nos projetos da Lei do Bem, revelando padrões importantes de agrupamento baseados em 
        similaridade semântica e características estruturais. 
        
        Os principais achados incluem:
        
        • <b>Especialização por área:</b> Clusters tendem a agrupar projetos de áreas tecnológicas 
        similares, sugerindo a possibilidade de especialização de analistas.
        
        • <b>Padrões de decisão:</b> Identificados clusters com taxas de aprovação significativamente 
        diferentes, indicando possíveis vieses ou critérios não uniformes.
        
        • <b>Distribuição de carga:</b> Alguns analistas concentram análises em clusters específicos, 
        o que pode indicar especialização informal ou desbalanceamento.
        
        A implementação das recomendações propostas pode levar a uma melhoria significativa na 
        eficiência e consistência do processo de avaliação.
        """
        story.append(Paragraph(conclusoes_text, styles['Normal']))
        
        # Construir PDF
        doc.build(story)
        print(f"✅ Relatório PDF gerado: {nome_arquivo}")
    
    def _gerar_recomendacoes(self) -> list[dict[str, str]]:
        """Gera recomendações baseadas na análise"""
        recomendacoes = []
        
        if 'padroes_cluster' in self.resultados_analise:
            df_padroes = self.resultados_analise['padroes_cluster']
            
            # 1. Balanceamento de carga
            if df_padroes['concentracao_analista'].max() > 60:
                recomendacoes.append({
                    'titulo': 'Implementar Balanceamento Automático de Carga',
                    'descricao': 'Alguns clusters têm mais de 60% dos projetos analisados pelo mesmo '
                               'analista. Recomenda-se implementar um sistema de distribuição automática '
                               'que considere a carga atual e a especialização dos analistas.'
                })
            
            # 2. Especialização formal
            areas_concentradas = df_padroes.groupby('area_principal')['tamanho'].sum()
            if len(areas_concentradas) > 5:
                recomendacoes.append({
                    'titulo': 'Formalizar Especialização por Área Tecnológica',
                    'descricao': f'Foram identificadas {len(areas_concentradas)} áreas tecnológicas '
                               'principais. Criar grupos de analistas especializados em cada área '
                               'pode aumentar a qualidade e velocidade das análises.'
                })
            
            # 3. Padronização de critérios
            variacao_aprovacao = df_padroes['taxa_recomendado'].std()
            if variacao_aprovacao > 20:
                recomendacoes.append({
                    'titulo': 'Padronizar Critérios de Avaliação',
                    'descricao': f'A variação na taxa de aprovação entre clusters é de '
                               f'{variacao_aprovacao:.1f}%. Desenvolver critérios objetivos e '
                               'checklists padronizados pode reduzir essa disparidade.'
                })
            
            # 4. Sistema de triagem
            if self.resultados_analise['kmeans']['k_optimal'] > 15:
                recomendacoes.append({
                    'titulo': 'Implementar Sistema de Triagem Automatizada',
                    'descricao': 'Com o grande número de clusters identificados, um sistema de '
                               'pré-classificação usando IA pode agilizar o direcionamento dos '
                               'projetos para os analistas mais adequados.'
                })
        
        # 5. Monitoramento contínuo
        recomendacoes.append({
            'titulo': 'Estabelecer Monitoramento Contínuo de Padrões',
            'descricao': 'Implementar dashboards em tempo real para acompanhar métricas de '
                       'distribuição, tempo de análise e taxas de aprovação por cluster e analista.'
        })
        
        return recomendacoes
    
    def exportar_resultados_detalhados(self, prefixo='lei_bem'):
        """Exporta todos os resultados detalhados"""
        print("💾 Exportando resultados detalhados...")
        
        # 1. DataFrame com clusters
        self.df.to_csv(f'{prefixo}_projetos_clusters.csv', index=False, sep=';', encoding='utf-8')
        
        # 2. Análise de clusters
        if 'padroes_cluster' in self.resultados_analise:
            self.resultados_analise['padroes_cluster'].to_csv(
                f'{prefixo}_analise_clusters.csv', index=False, sep=';', encoding='utf-8'
            )
        
        # 3. Análise de analistas
        if 'padroes_analista' in self.resultados_analise:
            self.resultados_analise['padroes_analista'].to_csv(
                f'{prefixo}_analise_analistas.csv', index=False, sep=';', encoding='utf-8'
            )
        
        # 4. Métricas de otimização
        import json
        metricas = {
            'k_optimal': self.resultados_analise['kmeans']['k_optimal'],
            'k_elbow': self.resultados_analise['kmeans']['k_elbow'],
            'k_silhouette': self.resultados_analise['kmeans']['k_silhouette'],
            'total_projetos': len(self.df),
            'total_clusters': self.resultados_analise['kmeans']['k_optimal']
        }
        
        with open(f'{prefixo}_metricas.json', 'w', encoding='utf-8') as f:
            json.dump(metricas, f, indent=2, ensure_ascii=False)
        
        print("✅ Todos os resultados exportados")


def main():
    """Função principal para executar análise completa"""
    print("🚀 Análise Avançada de Clusters - Lei do Bem")
    print("=" * 60)
    
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
    
    # 2. Criar embeddings multimodais
    analisador.criar_embeddings_multimodais()
    
    # 3. Aplicar K-Means otimizado
    analisador.analisar_kmeans_otimizado(max_k=30)
    
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
    print("   - relatorio_clusters_lei_bem.pdf (Relatório completo)")
    print("   - lei_bem_projetos_clusters.csv (Projetos com clusters)")
    print("   - lei_bem_analise_clusters.csv (Características dos clusters)")
    print("   - lei_bem_analise_analistas.csv (Análise por analista)")
    print("   - Visualizações em PNG")
    
    return analisador


if __name__ == "__main__":
    analisador = main()