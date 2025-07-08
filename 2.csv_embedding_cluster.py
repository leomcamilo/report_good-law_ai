import pandas as pd
import numpy as np
import os
import nltk
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
    df_projetos_unico = pd.read_csv(arquivos_csv[0], sep=';')
    print(f"Dados carregados: {df_projetos_unico.shape[0]} projetos")
    
    return df_projetos_unico

def criar_embeddings(df):
    """Cria embeddings otimizados focando apenas no conteúdo técnico do projeto"""
    
    # Verificar se as colunas existem
    colunas_necessarias = ['empresa', 'projeto', 'projeto_multianual']
    colunas_faltantes = [col for col in colunas_necessarias if col not in df.columns]
    
    if colunas_faltantes:
        raise ValueError(f"Colunas faltantes no DataFrame: {colunas_faltantes}")
    
    # Baixar stopwords do NLTK se necessário
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Baixando stopwords do NLTK...")
        nltk.download('stopwords')
    
    # Carregar stopwords do NLTK
    stopwords_nltk = set(nltk.corpus.stopwords.words('portuguese'))
    
    # LISTA DE STOP WORDS CUSTOMIZADA PARA PROJETOS DE P&D
    stop_words_personalizadas = {
        # Stop words básicas em português
        'de', 'da', 'do', 'das', 'dos', 'a', 'o', 'as', 'os', 'e', 'ou', 'para', 'por', 'com', 'em', 'no', 'na', 'nos', 'nas',
        'um', 'uma', 'uns', 'umas', 'se', 'que', 'como', 'quando', 'onde', 'qual', 'quais', 'todo', 'toda', 'todos', 'todas',
        'esse', 'essa', 'esses', 'essas', 'este', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas',
        'seu', 'sua', 'seus', 'suas', 'meu', 'minha', 'meus', 'minhas', 'nosso', 'nossa', 'nossos', 'nossas',
        'muito', 'mais', 'menos', 'bem', 'já', 'ainda', 'também', 'apenas', 'sempre', 'nunca', 'sim', 'não',
        
        # Stop words específicas para contexto de P&D e Lei do Bem
        'projeto', 'projetos', 'empresa', 'desenvolvimento', 'pesquisa', 'inovação', 'tecnologia', 'tecnológico', 'tecnológica',
        'atividade', 'atividades', 'processo', 'processos', 'produto', 'produtos', 'sistema', 'sistemas',
        'método', 'métodos', 'técnica', 'técnicas', 'metodologia', 'metodologias', 'análise', 'estudo', 'estudos',
        'resultado', 'resultados', 'objetivo', 'objetivos', 'meta', 'metas', 'finalidade', 'propósito',
        'aplicação', 'aplicações', 'utilização', 'uso', 'implementação', 'execução', 'realização',
        'área', 'setor', 'segmento', 'campo', 'domínio', 'ramo', 'categoria', 'tipo', 'tipos',
        'forma', 'formas', 'modo', 'modos', 'maneira', 'maneiras', 'meio', 'meios', 'através', 'mediante',
        'sendo', 'tendo', 'fazendo', 'realizando', 'desenvolvendo', 'criando', 'produzindo', 'gerando',
        'assim', 'então', 'portanto', 'dessa', 'desta', 'nesta', 'nessa', 'neste', 'nesse',
        'partir', 'base', 'bases', 'fundamento', 'fundamentação', 'princípio', 'princípios',
        'elemento', 'elementos', 'componente', 'componentes', 'parte', 'partes', 'aspecto', 'aspectos',
        'característica', 'características', 'propriedade', 'propriedades', 'atributo', 'atributos',
        
        # Palavras muito genéricas do contexto empresarial
        'mercado', 'cliente', 'clientes', 'consumidor', 'consumidores', 'setor', 'indústria', 'industrial',
        'comercial', 'econômico', 'econômica', 'negócio', 'negócios', 'valor', 'custo', 'custos',
        'receita', 'lucro', 'investimento', 'recurso', 'recursos', 'capital', 'financeiro', 'financeira',
        
        # Conectivos e preposições comuns
        'sobre', 'sob', 'entre', 'durante', 'após', 'antes', 'depois', 'dentro', 'fora', 'acima', 'abaixo',
        'contra', 'sem', 'até', 'desde', 'perante', 'conforme', 'segundo', 'inclusive', 'exceto', 'salvo',
        
        # Artigos e pronomes adicionais
        'isto', 'isso', 'aquilo', 'algo', 'alguém', 'ninguém', 'nada', 'tudo', 'cada', 'outro', 'outra', 'outros', 'outras',
        'primeiro', 'primeira', 'último', 'última', 'único', 'única', 'mesmo', 'mesma', 'próprio', 'própria',
        
        # Palavras temporais genéricas
        'ano', 'anos', 'mês', 'meses', 'dia', 'dias', 'hora', 'horas', 'tempo', 'período', 'períodos',
        'momento', 'momentos', 'fase', 'fases', 'etapa', 'etapas', 'início', 'fim', 'final'
    }
    
    # Unir stopwords do NLTK com as personalizadas (sem duplicatas)
    stop_words_completas = stopwords_nltk.union(stop_words_personalizadas)
    
    print(f"📝 Stopwords NLTK: {len(stopwords_nltk)} palavras")
    print(f"📝 Stopwords personalizadas: {len(stop_words_personalizadas)} palavras")
    print(f"📝 Total de stop words (únicas): {len(stop_words_completas)} palavras")
    print(f"   Amostra: {list(sorted(stop_words_completas))[:20]}...")
    
    def remover_stop_words(texto):
        """Remove stop words do texto preservando contexto técnico"""
        if pd.isna(texto) or not texto:
            return ""
        
        # Converter para minúsculas e dividir em palavras
        palavras = str(texto).lower().split()
        
        # Filtrar stop words, mas manter palavras técnicas importantes
        palavras_filtradas = []
        for palavra in palavras:
            # Remover pontuação básica
            palavra_limpa = palavra.strip('.,!?;:()"\'[]{}')
            
            # Manter palavra se:
            # 1. Não é stop word
            # 2. Tem mais de 3 caracteres (palavras técnicas tendem a ser maiores)
            # 3. Contém números (códigos, versões, etc.)
            if (palavra_limpa not in stop_words_completas and 
                (len(palavra_limpa) > 3 or any(c.isdigit() for c in palavra_limpa))):
                palavras_filtradas.append(palavra_limpa)
        
        return ' '.join(palavras_filtradas)
    
    # ESTRATÉGIA: Focar apenas no conteúdo técnico do projeto
    def extrair_conteudo_tecnico(projeto_texto):
        """Extrai apenas o conteúdo técnico relevante SEM aplicar stop words ainda"""
        import re
        
        # Extrair descrição, elemento tecnológico, desafio tecnológico
        patterns = {
            'descricao': r'DESCRIÇÃO:\s*(.*?)\s*TIPO \(',
            'elemento_tech': r'ELEMENTO TECNOLÓGICO:\s*(.*?)\s*DESAFIO',
            'desafio_tech': r'DESAFIO TECNOLÓGICO:\s*(.*?)\s*METODOLOGIA',
            'metodologia': r'METODOLOGIA:\s*(.*?)\s*INFORMAÇÃO',
            'area': r'AREA:\s*(.*?)\s*PALAVRAS',
            'palavras_chave': r'PALAVRAS CHAVE:\s*(.*?)\s*NATUREZA'
        }
        
        conteudo = []
        for key, pattern in patterns.items():
            match = re.search(pattern, str(projeto_texto), re.DOTALL)
            if match:
                texto = match.group(1).strip()
                if texto and len(texto) > 10:  # Só incluir se tiver conteúdo significativo
                    conteudo.append(texto)
        
        return ' '.join(conteudo) if conteudo else str(projeto_texto)
    
    # Criar texto focado no conteúdo técnico (SEM stop words ainda)
    print("Extraindo conteúdo técnico dos projetos...")
    df['texto_tecnico_bruto'] = df['projeto'].apply(extrair_conteudo_tecnico)
    
    # AGORA aplicar limpeza de stop words 
    print("Aplicando remoção de stop words...")
    df['texto_tecnico'] = df['texto_tecnico_bruto'].apply(remover_stop_words)
    
    # Estatísticas da limpeza
    tamanho_medio_antes = df['texto_tecnico_bruto'].str.len().mean()
    tamanho_medio_depois = df['texto_tecnico'].str.len().mean()
    reducao_percentual = ((tamanho_medio_antes - tamanho_medio_depois) / tamanho_medio_antes) * 100
    
    print(f"📊 Estatísticas da limpeza:")
    print(f"   Tamanho médio antes: {tamanho_medio_antes:.0f} caracteres")
    print(f"   Tamanho médio depois: {tamanho_medio_depois:.0f} caracteres")
    print(f"   Redução: {reducao_percentual:.1f}%")
    
    # Mostrar exemplo de transformação
    print(f"\n🔍 Exemplo de transformação:")
    idx_exemplo = 0
    if len(df) > 0:
        print(f"   ANTES: {df['texto_tecnico_bruto'].iloc[idx_exemplo][:200]}...")
        print(f"   DEPOIS: {df['texto_tecnico'].iloc[idx_exemplo][:200]}...")
    
    # Carregar modelo de embeddings - SERAFIM (português especializado)
    print("Carregando modelo de embeddings...")
    model = SentenceTransformer("PORTULAN/serafim-335m-portuguese-pt-sentence-encoder-ir")
    
    # Gerar embeddings apenas do conteúdo técnico
    print("Gerando embeddings do conteúdo técnico...")
    embeddings = model.encode(df['texto_tecnico'].tolist(), show_progress_bar=True)
    
    print(f"Embeddings gerados: {embeddings.shape}")
    
    return df, embeddings

def fazer_clustering(embeddings, n_projetos):
    """
    Aplica clustering aglomerativo otimizado para projetos da Lei do Bem.
    Escalável para até 75k projetos.
    """
    
    print("=== APLICANDO CLUSTERING AGLOMERATIVO ===")
    print(f"📊 Processando {n_projetos:,} projetos")
    
    # Threshold otimizado baseado na análise anterior
    threshold = 0.58
    
    from sklearn.cluster import AgglomerativeClustering
    
    print(f"🎯 Usando threshold: {threshold}")
    print("⚙️  Configuração: linkage='average', metric='cosine'")
    
    # Clustering aglomerativo otimizado
    clusterer = AgglomerativeClustering(
        n_clusters=None,           # Deixa threshold decidir o número
        distance_threshold=threshold,    # Threshold otimizado
        linkage='average',         # Melhor para embeddings semânticos
        metric='cosine'           # Ideal para SentenceTransformers
    )
    
    print("🔄 Executando clustering...")
    clusters = clusterer.fit_predict(embeddings)
    
    # Estatísticas dos resultados
    n_clusters = len(set(clusters))
    cobertura = 100.0  # Aglomerativo sempre cobre 100%
    
    print(f"✅ Clustering concluído!")
    print(f"   📈 Cobertura: {cobertura}%")
    print(f"   🎯 Número de clusters: {n_clusters}")
    
    # Estatísticas adicionais por cluster
    cluster_sizes = {}
    for cluster_id in set(clusters):
        size = list(clusters).count(cluster_id)
        cluster_sizes[cluster_id] = size
    
    # Ordenar clusters por tamanho
    sorted_clusters = sorted(cluster_sizes.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\n📋 TOP 10 CLUSTERS POR TAMANHO:")
    for i, (cluster_id, size) in enumerate(sorted_clusters[:10]):
        percentage = (size / n_projetos) * 100
        print(f"   Cluster {cluster_id}: {size:,} projetos ({percentage:.1f}%)")
    
    # Estatísticas de distribuição
    avg_size = n_projetos / n_clusters
    print(f"\n📊 ESTATÍSTICAS DE DISTRIBUIÇÃO:")
    print(f"   Tamanho médio por cluster: {avg_size:.1f} projetos")
    print(f"   Maior cluster: {max(cluster_sizes.values()):,} projetos")
    print(f"   Menor cluster: {min(cluster_sizes.values()):,} projetos")
    
    return clusters

def main():
    """Função principal otimizada"""
    try:
        # 1. Carregar dados
        print("1. Carregando dados CSV...")
        df_projetos_unico = carregar_dados_csv()
        
        # 2. Criar embeddings otimizados
        print("2. Criando embeddings otimizados...")
        df_projetos_unico, embeddings = criar_embeddings(df_projetos_unico)
        
        # 3. Fazer clustering
        print("3. Fazendo clustering aglomerativo...")
        clusters = fazer_clustering(embeddings, len(df_projetos_unico))
        
        # 4. Adicionar clusters ao dataframe
        df_projetos_unico['cluster'] = clusters
        
        # 5. Salvar resultado
        print("4. Salvando resultado...")
        nome_arquivo = 'projetos_com_clusters_final.csv'
        df_projetos_unico.to_csv(nome_arquivo, index=False, sep=';')
        
        print(f"\n✅ Processo concluído com sucesso!")
        print(f"📁 Arquivo salvo: {nome_arquivo}")
        
        # Estatísticas finais
        cluster_stats = df_projetos_unico['cluster'].value_counts().sort_index()
        n_clusters_final = len(cluster_stats)
        
        print(f"\n📊 ESTATÍSTICAS FINAIS:")
        print(f"   Total de projetos: {len(df_projetos_unico):,}")
        print(f"   Projetos clusterizados: {len(df_projetos_unico):,}")
        print(f"   Taxa de cobertura: 100.0%")
        print(f"   Número de clusters: {n_clusters_final}")
        
        print("🎯 META ATINGIDA: Cobertura de 100%!")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {str(e)}")
        raise

if __name__ == "__main__":
    main()