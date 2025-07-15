#!/usr/bin/env python3
"""
Análise Multivariada de Padrões de Decisão - Lei do Bem
=======================================================

Este script implementa análise multivariada usando Random Forest + SHAP
para identificar padrões de aprovação/reprovação em projetos da Lei do Bem.

Considera duas fases de análise:
- DO (do_taaproj_notipoavaliacaoanalise): Primeira fase
- Parecer (p_taaproj_notipoavaliacaoanalise): Segunda fase

Dependências necessárias:
pip install pandas numpy scikit-learn shap matplotlib seaborn joblib
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.inspection import permutation_importance
import shap
import warnings
from datetime import datetime
import joblib
# Configurar matplotlib para não exibir janelas
import matplotlib
matplotlib.use('Agg')

warnings.filterwarnings('ignore')

class AnalisadorPadroesDecisao:
    """
    Classe para análise multivariada de padrões de decisão em projetos Lei do Bem
    """
    
    def __init__(self):
        self.df = None
        self.df_processado = None
        self.model = None
        self.encoders = {}
        self.scaler = StandardScaler()
        self.feature_names = []
        self.resultados = {}
        
    def carregar_dados(self, caminho_csv='lei_bem_projetos_clusters.csv'):
        """Carrega e preprocessa os dados do CSV"""
        print("📂 Carregando dados...")
        self.df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8')
        print(f"✅ {len(self.df)} projetos carregados")
        
        # Verificar colunas essenciais
        colunas_necessarias = [
            'lst_nrcnpj', 'lst_norazaosocial', 'lst_noatividadeeconomica',
            'lst_notipoportepessoajuridica', 'daproj_tppbpade', 'daproj_dsareaprojeto',
            'daproj_tpnatureza', 'do_saat_idunicopessoaanalise', 
            'do_taaproj_notipoavaliacaoanalise',  # Campo correto para resultado DO
            'p_taaproj_notipoavaliacaoanalise',   # Campo para resultado Parecer
            'cluster_kmeans'
        ]
        
        colunas_faltantes = [col for col in colunas_necessarias if col not in self.df.columns]
        if colunas_faltantes:
            print(f"⚠️ Colunas faltantes: {colunas_faltantes}")
            print("Tentando mapear colunas similares...")
            self._mapear_colunas_similares()
        
        # Log de colunas de resultado encontradas
        print("\n📊 Colunas de resultado encontradas:")
        if 'do_taaproj_notipoavaliacaoanalise' in self.df.columns:
            print("✅ do_taaproj_notipoavaliacaoanalise (Fase DO)")
        if 'p_taaproj_notipoavaliacaoanalise' in self.df.columns:
            print("✅ p_taaproj_notipoavaliacaoanalise (Fase Parecer)")
        
        return self.df
    
    def _mapear_colunas_similares(self):
        """Mapeia colunas com nomes similares se não encontrar exatas"""
        # Mapeamento de possíveis variações de nomes
        mapeamentos = {
            'lst_nrcnpj': ['nrcnpj', 'cnpj', 'lst_cnpj'],
            'lst_norazaosocial': ['norazaosocial', 'razao_social', 'razaosocial_empresa'],
            'lst_noatividadeeconomica': ['atividade_economica', 'noatividadeeconomica'],
            'lst_notipoportepessoajuridica': ['porte_empresa', 'notipoportepessoajuridica'],
            'daproj_tppbpade': ['tipo_projeto', 'tppbpade'],
            'daproj_dsareaprojeto': ['area_projeto', 'dsareaprojeto'],
            'daproj_tpnatureza': ['natureza', 'tpnatureza'],
            'do_saat_idunicopessoaanalise': ['id_analista', 'idunicopessoaanalise'],
            'do_taaproj_notipoavaliacaoanalise': ['resultado_do', 'notipoavaliacaoanalise_do', 'tipo_avaliacao_do'],
            'p_taaproj_notipoavaliacaoanalise': ['resultado_parecer', 'notipoavaliacaoanalise_parecer', 'tipo_avaliacao_parecer']
        }
        
        for col_esperada, alternativas in mapeamentos.items():
            if col_esperada not in self.df.columns:
                for alt in alternativas:
                    if alt in self.df.columns:
                        self.df[col_esperada] = self.df[alt]
                        print(f"✅ Mapeado: {alt} → {col_esperada}")
                        break
    
    def preparar_features(self):
        """Prepara features para análise multivariada incluindo análise de duas fases"""
        print("\n🔧 Preparando features...")
        
        # Criar target binário (aprovado/não aprovado)
        self._criar_variavel_alvo()
        
        # Selecionar features relevantes
        features_categoricas = [
            'lst_noatividadeeconomica',
            'lst_notipoportepessoajuridica', 
            'daproj_tppbpade',
            'daproj_dsareaprojeto',
            'daproj_tpnatureza',
            'cluster_kmeans'
        ]
        
        features_numericas = []
        
        # Features relacionadas às fases
        if 'mudou_decisao' in self.df.columns:
            features_numericas.append('mudou_decisao')
        
        # Feature especial: analista
        if 'do_saat_idunicopessoaanalise' in self.df.columns:
            # Criar feature de frequência do analista
            freq_analista = self.df['do_saat_idunicopessoaanalise'].value_counts()
            self.df['freq_analista'] = self.df['do_saat_idunicopessoaanalise'].map(freq_analista)
            features_numericas.append('freq_analista')
            
            # Taxa de aprovação histórica do analista (apenas fase DO)
            if 'aprovado_do' in self.df.columns:
                taxa_aprovacao_analista = self.df[self.df['aprovado_do'] != -1].groupby('do_saat_idunicopessoaanalise')['aprovado_do'].mean()
                self.df['taxa_aprovacao_analista'] = self.df['do_saat_idunicopessoaanalise'].map(taxa_aprovacao_analista)
                features_numericas.append('taxa_aprovacao_analista')
            
            # Top 10 analistas como categórica
            top_analistas = freq_analista.head(10).index
            self.df['analista_top10'] = self.df['do_saat_idunicopessoaanalise'].apply(
                lambda x: str(x) if x in top_analistas else 'Outros'
            )
            features_categoricas.append('analista_top10')
        
        # Processar features categóricas
        df_encoded = pd.DataFrame()
        
        for col in features_categoricas:
            if col in self.df.columns:
                # Label encoding
                if col not in self.encoders:
                    self.encoders[col] = LabelEncoder()
                    encoded = self.encoders[col].fit_transform(self.df[col].fillna('MISSING'))
                else:
                    encoded = self.encoders[col].transform(self.df[col].fillna('MISSING'))
                
                df_encoded[f'{col}_encoded'] = encoded
                
                # One-hot encoding para as mais importantes
                if col in ['daproj_dsareaprojeto', 'lst_notipoportepessoajuridica', 'daproj_tppbpade']:
                    # Criar dummies para top categorias
                    top_cats = self.df[col].value_counts().head(5).index
                    for cat in top_cats:
                        df_encoded[f'{col}_{cat}'] = (self.df[col] == cat).astype(int)
        
        # Adicionar features numéricas
        for col in features_numericas:
            if col in self.df.columns:
                df_encoded[col] = self.df[col].fillna(0)
        
        # Adicionar interações importantes
        if 'cluster_kmeans' in self.df.columns and 'analista_top10' in features_categoricas:
            # Interação cluster × analista
            for cluster in self.df['cluster_kmeans'].unique()[:5]:  # Top 5 clusters
                df_encoded[f'cluster_{cluster}_analista'] = (
                    (self.df['cluster_kmeans'] == cluster) & 
                    (self.df['analista_top10'] != 'Outros')
                ).astype(int)
        
        # Interação área × mudança de decisão
        if 'mudou_decisao' in self.df.columns and 'daproj_dsareaprojeto' in self.df.columns:
            top_areas_mudanca = self.df[self.df['mudou_decisao'] == 1]['daproj_dsareaprojeto'].value_counts().head(3).index
            for area in top_areas_mudanca:
                df_encoded[f'area_{area}_mudou'] = (
                    (self.df['daproj_dsareaprojeto'] == area) & 
                    (self.df['mudou_decisao'] == 1)
                ).astype(int)
        
        self.df_processado = df_encoded
        self.feature_names = list(df_encoded.columns)
        
        print(f"✅ {len(self.feature_names)} features criadas")
        return df_encoded
    
    def _criar_variavel_alvo(self):
        """Cria variável alvo binária de aprovação com análise de duas fases"""
        # Mapear resultados para binário
        mapa_aprovacao = {
            'Recomendado': 1,
            'Não Recomendado': 0,
            'RECOMENDADO': 1,
            'NÃO RECOMENDADO': 0
        }
        
        # Primeira fase - DO
        if 'do_taaproj_notipoavaliacaoanalise' in self.df.columns:
            self.df['aprovado_do'] = self.df['do_taaproj_notipoavaliacaoanalise'].map(
                lambda x: mapa_aprovacao.get(str(x).strip(), 0) if pd.notna(x) else -1
            )
            print(f"📊 Distribuição Fase DO:")
            print(self.df['aprovado_do'].value_counts(normalize=True))
        else:
            print("⚠️ Campo do_taaproj_notipoavaliacaoanalise não encontrado")
            self.df['aprovado_do'] = -1
        
        # Segunda fase - Parecer
        if 'p_taaproj_notipoavaliacaoanalise' in self.df.columns:
            self.df['aprovado_parecer'] = self.df['p_taaproj_notipoavaliacaoanalise'].map(
                lambda x: mapa_aprovacao.get(str(x).strip(), 0) if pd.notna(x) else -1
            )
            print(f"\n📊 Distribuição Fase Parecer:")
            print(self.df['aprovado_parecer'].value_counts(normalize=True))
        else:
            print("⚠️ Campo p_taaproj_notipoavaliacaoanalise não encontrado")
            self.df['aprovado_parecer'] = -1
        
        # Criar variável alvo combinada (prioriza parecer se existir)
        self.df['aprovado'] = self.df.apply(
            lambda row: row['aprovado_parecer'] if row['aprovado_parecer'] != -1 
                       else row['aprovado_do'] if row['aprovado_do'] != -1 
                       else 0,
            axis=1
        )
        
        # Criar variável de mudança entre fases
        self.df['mudou_decisao'] = (
            (self.df['aprovado_do'] != -1) & 
            (self.df['aprovado_parecer'] != -1) & 
            (self.df['aprovado_do'] != self.df['aprovado_parecer'])
        ).astype(int)
        
        print(f"\n📊 Distribuição final (combinada):")
        print(self.df['aprovado'].value_counts(normalize=True))
        print(f"\n📊 Projetos que mudaram de decisão entre fases: {self.df['mudou_decisao'].sum()}")
    
    def treinar_modelo(self, test_size=0.2, random_state=42):
        """Treina modelo Random Forest com validação cruzada"""
        print("\n🤖 Treinando modelo Random Forest...")
        
        X = self.df_processado
        y = self.df['aprovado']
        
        # Split treino/teste estratificado
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
        
        # Modelo Random Forest otimizado
        self.model = RandomForestClassifier(
            n_estimators=200,
            max_depth=15,
            min_samples_split=20,
            min_samples_leaf=10,
            max_features='sqrt',
            class_weight='balanced',
            random_state=random_state,
            n_jobs=-1
        )
        
        # Treinar modelo
        self.model.fit(X_train, y_train)
        
        # Avaliação
        y_pred = self.model.predict(X_test)
        y_proba = self.model.predict_proba(X_test)[:, 1]
        
        print("\n📊 Métricas de Performance:")
        print(classification_report(y_test, y_pred))
        
        # ROC-AUC
        if len(np.unique(y_test)) > 1:
            auc_score = roc_auc_score(y_test, y_proba)
            print(f"ROC-AUC Score: {auc_score:.3f}")
            self.resultados['auc'] = auc_score
        
        # Validação cruzada
        cv_scores = cross_val_score(self.model, X, y, cv=5, scoring='roc_auc')
        print(f"Cross-validation AUC: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
        
        # Salvar resultados
        self.resultados['X_test'] = X_test
        self.resultados['y_test'] = y_test
        self.resultados['y_pred'] = y_pred
        self.resultados['y_proba'] = y_proba
        
        return self.model
    
    def analisar_importancia_features(self, top_n=20):
        """Analisa importância das features usando múltiplos métodos"""
        print("\n📈 Analisando importância das features...")
        
        # 1. Feature importance do Random Forest
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1][:top_n]
        
        plt.figure(figsize=(12, 8))
        plt.title('Top 20 Features Mais Importantes (Random Forest)')
        plt.bar(range(top_n), importances[indices])
        plt.xticks(range(top_n), [self.feature_names[i] for i in indices], rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('feature_importance_rf.png', dpi=300)
        plt.close()
        
        # 2. Permutation importance
        perm_importance = permutation_importance(
            self.model, 
            self.resultados['X_test'], 
            self.resultados['y_test'],
            n_repeats=10,
            random_state=42
        )
        
        perm_indices = np.argsort(perm_importance.importances_mean)[::-1][:top_n]
        
        plt.figure(figsize=(12, 8))
        plt.title('Top 20 Features - Permutation Importance')
        plt.boxplot([perm_importance.importances[i] for i in perm_indices], 
                   labels=[self.feature_names[i] for i in perm_indices])
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Diminuição na Acurácia')
        plt.tight_layout()
        plt.savefig('permutation_importance.png', dpi=300)
        plt.close()
        
        # Retornar top features
        top_features_rf = [(self.feature_names[i], importances[i]) for i in indices]
        top_features_perm = [(self.feature_names[i], perm_importance.importances_mean[i]) 
                            for i in perm_indices]
        
        self.resultados['top_features_rf'] = top_features_rf
        self.resultados['top_features_perm'] = top_features_perm
        
        return top_features_rf, top_features_perm
    
    def analise_shap(self, max_samples=1000):
        """Análise SHAP para interpretabilidade detalhada"""
        print("\n🔍 Executando análise SHAP...")
        
        # Limitar amostras para SHAP (computacionalmente intensivo)
        X_shap = self.resultados['X_test']
        if len(X_shap) > max_samples:
            idx = np.random.choice(len(X_shap), max_samples, replace=False)
            X_shap = X_shap.iloc[idx]
        
        # Criar explicador SHAP
        explainer = shap.TreeExplainer(self.model)
        shap_values = explainer.shap_values(X_shap)
        
        # Se binary classification, pegar valores da classe positiva
        if isinstance(shap_values, list):
            shap_values = shap_values[1]
        
        # Summary plot
        plt.figure(figsize=(12, 8))
        shap.summary_plot(shap_values, X_shap, feature_names=self.feature_names, 
                         show=False, max_display=20)
        plt.tight_layout()
        plt.savefig('shap_summary.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # Feature importance plot
        plt.figure(figsize=(10, 8))
        shap.summary_plot(shap_values, X_shap, feature_names=self.feature_names,
                         plot_type="bar", show=False, max_display=20)
        plt.tight_layout()
        plt.savefig('shap_importance.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # Salvar valores SHAP
        self.resultados['shap_values'] = shap_values
        self.resultados['X_shap'] = X_shap
        
        return shap_values
    
    def analisar_padroes_decisao(self):
        """Analisa padrões específicos de decisão incluindo análise entre fases"""
        print("\n🎯 Analisando padrões de decisão...")
        
        # Adicionar predições ao dataframe original
        self.df['probabilidade_aprovacao'] = self.model.predict_proba(self.df_processado)[:, 1]
        self.df['predicao'] = self.model.predict(self.df_processado)
        
        padroes = {}
        
        # 0. Análise de mudanças entre fases
        if 'aprovado_do' in self.df.columns and 'aprovado_parecer' in self.df.columns:
            # Matriz de transição DO → Parecer
            df_duas_fases = self.df[(self.df['aprovado_do'] != -1) & (self.df['aprovado_parecer'] != -1)]
            
            if len(df_duas_fases) > 0:
                matriz_transicao = pd.crosstab(
                    df_duas_fases['aprovado_do'].map({0: 'Não Recomendado', 1: 'Recomendado'}),
                    df_duas_fases['aprovado_parecer'].map({0: 'Não Recomendado', 1: 'Recomendado'}),
                    normalize='index'
                )
                
                padroes['matriz_transicao'] = matriz_transicao
                
                # Visualizar matriz de transição
                plt.figure(figsize=(8, 6))
                sns.heatmap(matriz_transicao, annot=True, fmt='.2%', cmap='Blues', 
                           cbar_kws={'label': 'Probabilidade'})
                plt.title('Matriz de Transição: DO → Parecer')
                plt.xlabel('Decisão no Parecer')
                plt.ylabel('Decisão no DO')
                plt.tight_layout()
                plt.savefig('matriz_transicao_fases.png', dpi=300)
                plt.close()
                
                # Análise de mudanças por área
                mudancas_por_area = df_duas_fases[df_duas_fases['mudou_decisao'] == 1].groupby('daproj_dsareaprojeto').size()
                total_por_area = df_duas_fases.groupby('daproj_dsareaprojeto').size()
                taxa_mudanca_area = (mudancas_por_area / total_por_area * 100).sort_values(ascending=False)
                
                padroes['taxa_mudanca_por_area'] = taxa_mudanca_area.head(10)
        
        # 1. Análise por área
        if 'daproj_dsareaprojeto' in self.df.columns:
            padroes['por_area'] = self.df.groupby('daproj_dsareaprojeto').agg({
                'aprovado': ['count', 'mean'],
                'aprovado_do': lambda x: (x == 1).mean() if 'aprovado_do' in self.df.columns else None,
                'aprovado_parecer': lambda x: (x == 1).mean() if 'aprovado_parecer' in self.df.columns else None,
                'probabilidade_aprovacao': 'mean',
                'predicao': 'mean'
            }).round(3)
            
            # Visualização
            top_areas = self.df['daproj_dsareaprojeto'].value_counts().head(10).index
            df_top_areas = self.df[self.df['daproj_dsareaprojeto'].isin(top_areas)]
            
            # Gráfico comparativo DO vs Parecer
            if 'aprovado_do' in self.df.columns and 'aprovado_parecer' in self.df.columns:
                fig, ax = plt.subplots(figsize=(12, 6))
                
                df_comp = df_top_areas.groupby('daproj_dsareaprojeto').agg({
                    'aprovado_do': lambda x: (x == 1).mean(),
                    'aprovado_parecer': lambda x: (x == 1).mean()
                }).sort_values('aprovado_do')
                
                x = np.arange(len(df_comp))
                width = 0.35
                
                ax.bar(x - width/2, df_comp['aprovado_do'], width, label='DO', alpha=0.8)
                ax.bar(x + width/2, df_comp['aprovado_parecer'], width, label='Parecer', alpha=0.8)
                
                ax.set_xlabel('Área')
                ax.set_ylabel('Taxa de Aprovação')
                ax.set_title('Taxa de Aprovação por Área: DO vs Parecer')
                ax.set_xticks(x)
                ax.set_xticklabels(df_comp.index, rotation=45, ha='right')
                ax.legend()
                
                plt.tight_layout()
                plt.savefig('aprovacao_por_area_fases.png', dpi=300)
                plt.close()
        
        # 2. Análise por analista
        if 'do_saat_idunicopessoaanalise' in self.df.columns:
            analistas_freq = self.df['do_saat_idunicopessoaanalise'].value_counts()
            analistas_top = analistas_freq[analistas_freq >= 10].index
            
            df_analistas = self.df[self.df['do_saat_idunicopessoaanalise'].isin(analistas_top)]
            padroes['por_analista'] = df_analistas.groupby('do_saat_idunicopessoaanalise').agg({
                'aprovado': ['count', 'mean'],
                'aprovado_do': lambda x: (x == 1).mean() if 'aprovado_do' in self.df.columns else None,
                'mudou_decisao': 'mean' if 'mudou_decisao' in self.df.columns else lambda x: 0,
                'probabilidade_aprovacao': 'mean'
            }).round(3)
            
            # Matriz analista × área
            if 'daproj_dsareaprojeto' in self.df.columns:
                top_areas_5 = self.df['daproj_dsareaprojeto'].value_counts().head(5).index
                df_matriz = self.df[
                    (self.df['do_saat_idunicopessoaanalise'].isin(analistas_top[:10])) &
                    (self.df['daproj_dsareaprojeto'].isin(top_areas_5))
                ]
                
                matriz_aprovacao = pd.crosstab(
                    df_matriz['do_saat_idunicopessoaanalise'],
                    df_matriz['daproj_dsareaprojeto'],
                    df_matriz['aprovado'],
                    aggfunc='mean'
                ).fillna(0)
                
                plt.figure(figsize=(10, 8))
                sns.heatmap(matriz_aprovacao, annot=True, fmt='.2f', cmap='RdYlGn', 
                           cbar_kws={'label': 'Taxa de Aprovação'})
                plt.title('Taxa de Aprovação: Analista × Área')
                plt.tight_layout()
                plt.savefig('matriz_analista_area.png', dpi=300)
                plt.close()
        
        # 3. Análise por cluster
        padroes['por_cluster'] = self.df.groupby('cluster_kmeans').agg({
            'aprovado': ['count', 'mean'],
            'mudou_decisao': 'mean' if 'mudou_decisao' in self.df.columns else lambda x: 0,
            'probabilidade_aprovacao': 'mean'
        }).round(3)
        
        # 4. Identificar casos extremos
        # Projetos com alta probabilidade mas reprovados
        falsos_positivos = self.df[
            (self.df['probabilidade_aprovacao'] > 0.8) & 
            (self.df['aprovado'] == 0)
        ]
        
        # Projetos com baixa probabilidade mas aprovados
        falsos_negativos = self.df[
            (self.df['probabilidade_aprovacao'] < 0.2) & 
            (self.df['aprovado'] == 1)
        ]
        
        # Projetos que mudaram de decisão
        if 'mudou_decisao' in self.df.columns:
            projetos_mudaram = self.df[self.df['mudou_decisao'] == 1]
            padroes['mudancas_decisao'] = {
                'total': len(projetos_mudaram),
                'de_aprovado_para_reprovado': len(projetos_mudaram[(projetos_mudaram['aprovado_do'] == 1) & (projetos_mudaram['aprovado_parecer'] == 0)]),
                'de_reprovado_para_aprovado': len(projetos_mudaram[(projetos_mudaram['aprovado_do'] == 0) & (projetos_mudaram['aprovado_parecer'] == 1)])
            }
        
        padroes['casos_extremos'] = {
            'falsos_positivos': len(falsos_positivos),
            'falsos_negativos': len(falsos_negativos),
            'fp_clusters': falsos_positivos['cluster_kmeans'].value_counts().head(),
            'fn_clusters': falsos_negativos['cluster_kmeans'].value_counts().head()
        }
        
        self.resultados['padroes'] = padroes
        return padroes
    
    def gerar_relatorio_insights(self):
        """Gera relatório com principais insights incluindo análise entre fases"""
        print("\n📝 Gerando relatório de insights...")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        with open(f'insights_padroes_decisao_{timestamp}.txt', 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("ANÁLISE DE PADRÕES DE DECISÃO - LEI DO BEM\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"Data da análise: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            f.write(f"Total de projetos analisados: {len(self.df):,}\n")
            f.write(f"Taxa geral de aprovação: {self.df['aprovado'].mean():.1%}\n")
            
            # Análise entre fases
            if 'mudou_decisao' in self.df.columns:
                f.write(f"\nANÁLISE ENTRE FASES (DO → PARECER):\n")
                f.write("-" * 50 + "\n")
                total_duas_fases = len(self.df[(self.df['aprovado_do'] != -1) & (self.df['aprovado_parecer'] != -1)])
                if total_duas_fases > 0:
                    f.write(f"Projetos com análise nas duas fases: {total_duas_fases:,}\n")
                    f.write(f"Projetos que mudaram de decisão: {self.df['mudou_decisao'].sum():,} ({self.df['mudou_decisao'].sum()/total_duas_fases:.1%})\n")
                    
                    if 'mudancas_decisao' in self.resultados['padroes']:
                        mudancas = self.resultados['padroes']['mudancas_decisao']
                        f.write(f"  - Aprovado DO → Reprovado Parecer: {mudancas['de_aprovado_para_reprovado']:,}\n")
                        f.write(f"  - Reprovado DO → Aprovado Parecer: {mudancas['de_reprovado_para_aprovado']:,}\n")
            
            # Top features
            f.write("\n\nTOP 10 FATORES MAIS IMPORTANTES PARA APROVAÇÃO:\n")
            f.write("-" * 50 + "\n")
            for i, (feat, imp) in enumerate(self.resultados['top_features_rf'][:10], 1):
                f.write(f"{i}. {feat}: {imp:.4f}\n")
            
            # Padrões por área
            if 'por_area' in self.resultados['padroes']:
                f.write("\n\nPADRÕES POR ÁREA TECNOLÓGICA:\n")
                f.write("-" * 50 + "\n")
                df_area = self.resultados['padroes']['por_area']
                df_area_sorted = df_area.sort_values(('aprovado', 'mean'), ascending=False)
                for area in df_area_sorted.head(10).index:
                    taxa = df_area_sorted.loc[area, ('aprovado', 'mean')]
                    count = df_area_sorted.loc[area, ('aprovado', 'count')]
                    f.write(f"{area}: {taxa:.1%} aprovação ({count} projetos)\n")
                
                # Áreas com maior mudança entre fases
                if 'taxa_mudanca_por_area' in self.resultados['padroes']:
                    f.write("\n\nÁREAS COM MAIOR TAXA DE MUDANÇA ENTRE FASES:\n")
                    f.write("-" * 50 + "\n")
                    for area, taxa in self.resultados['padroes']['taxa_mudanca_por_area'].items():
                        f.write(f"{area}: {taxa:.1f}% de mudança\n")
            
            # Análise por analista
            if 'por_analista' in self.resultados['padroes']:
                f.write("\n\nANÁLISE POR ANALISTA (TOP 10 POR VOLUME):\n")
                f.write("-" * 50 + "\n")
                df_analista = self.resultados['padroes']['por_analista']
                df_analista_sorted = df_analista.sort_values(('aprovado', 'count'), ascending=False)
                for analista in df_analista_sorted.head(10).index:
                    taxa = df_analista_sorted.loc[analista, ('aprovado', 'mean')]
                    count = df_analista_sorted.loc[analista, ('aprovado', 'count')]
                    taxa_mudanca = df_analista_sorted.loc[analista, ('mudou_decisao', 'mean')] if ('mudou_decisao', 'mean') in df_analista_sorted.columns else 0
                    f.write(f"Analista {analista}: {taxa:.1%} aprovação, {count} projetos")
                    if taxa_mudanca > 0:
                        f.write(f", {taxa_mudanca:.1%} mudança entre fases")
                    f.write("\n")
            
            # Insights específicos
            f.write("\n\nINSIGHTS PRINCIPAIS:\n")
            f.write("-" * 50 + "\n")
            
            # Identificar fatores críticos
            top_3_features = [feat for feat, _ in self.resultados['top_features_rf'][:3]]
            f.write(f"1. Os três fatores mais determinantes são: {', '.join(top_3_features)}\n")
            
            # Casos extremos
            casos = self.resultados['padroes']['casos_extremos']
            f.write(f"\n2. Casos que merecem atenção especial:\n")
            f.write(f"   - {casos['falsos_positivos']} projetos com alta probabilidade de aprovação mas reprovados\n")
            f.write(f"   - {casos['falsos_negativos']} projetos com baixa probabilidade mas aprovados\n")
            
            # Performance do modelo
            f.write(f"\n3. Performance do modelo:\n")
            f.write(f"   - AUC-ROC: {self.resultados.get('auc', 0):.3f}\n")
            f.write(f"   - Indica {self.resultados.get('auc', 0)*100:.1f}% de capacidade discriminativa\n")
            
            # Recomendações baseadas na análise
            f.write("\n\nRECOMENDAÇÕES:\n")
            f.write("-" * 50 + "\n")
            f.write("1. Revisar projetos que mudaram de decisão entre fases para identificar critérios inconsistentes\n")
            f.write("2. Padronizar critérios de avaliação entre analistas com taxas muito divergentes\n")
            f.write("3. Investigar áreas com alta taxa de mudança entre DO e Parecer\n")
            f.write("4. Criar checklist específico para clusters com baixa taxa de aprovação\n")
            
            f.write("\n" + "=" * 80)
        
        print(f"✅ Relatório salvo: insights_padroes_decisao_{timestamp}.txt")
    
    def salvar_resultados(self):
        """Salva todos os resultados da análise"""
        print("\n💾 Salvando resultados...")
        
        # Salvar modelo
        joblib.dump(self.model, 'modelo_rf_padroes_decisao.pkl')
        
        # Salvar encoders
        joblib.dump(self.encoders, 'encoders_padroes_decisao.pkl')
        
        # Salvar dataframe com predições
        self.df.to_csv('projetos_com_predicoes.csv', index=False, sep=';', encoding='utf-8')
        
        # Salvar métricas
        pd.DataFrame(self.resultados['top_features_rf'], 
                    columns=['feature', 'importance']).to_csv('feature_importance.csv', index=False)
        
        print("✅ Todos os resultados salvos!")


def main():
    """Função principal para executar análise completa"""
    print("🚀 Análise Multivariada de Padrões de Decisão - Lei do Bem")
    print("=" * 60)
    
    # Inicializar analisador
    analisador = AnalisadorPadroesDecisao()
    
    # 1. Carregar dados
    analisador.carregar_dados('lei_bem_projetos_clusters.csv')
    
    # 2. Preparar features
    analisador.preparar_features()
    
    # 3. Treinar modelo
    analisador.treinar_modelo()
    
    # 4. Analisar importância
    analisador.analisar_importancia_features()
    
    # 5. Análise SHAP
    analisador.analise_shap()
    
    # 6. Analisar padrões
    analisador.analisar_padroes_decisao()
    
    # 7. Gerar relatório
    analisador.gerar_relatorio_insights()
    
    # 8. Salvar resultados
    analisador.salvar_resultados()
    
    print("\n✅ Análise completa!")
    print("📊 Arquivos gerados:")
    print("   - insights_padroes_decisao_*.txt (relatório principal)")
    print("   - projetos_com_predicoes.csv (predições)")
    print("   - feature_importance.csv (importância das variáveis)")
    print("   - Visualizações PNG (gráficos)")
    print("   - modelo_rf_padroes_decisao.pkl (modelo treinado)")
    
    return analisador


if __name__ == "__main__":
    analisador = main()