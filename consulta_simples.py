#!/usr/bin/env python3
"""
Script Simples - Consulta Lei do Bem para DataFrame
==================================================

Script simplificado para carregar a consulta SQL em um DataFrame pandas.
"""

import pandas as pd
from sqlalchemy import create_engine

# Configurações do banco
DB_CONFIG = {
    'user': 'ia_budy',
    'password': 'ia_budy',
    'host': 'localhost',
    'port': 5432,
    'database': 'dbs_mctic2'
}

def carregar_dados():
    """Carrega os dados da consulta SQL em um DataFrame pandas."""
    
    # String de conexão
    connection_string = (
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    
    # Criar engine
    engine = create_engine(connection_string)
    
    # Query SQL (mesma do arquivo public.sql)
    query = """
    WITH base_projetos AS (
        SELECT 
            proj.iddadoanaliseprojeto,
            proj.idprenchimentosituacaoanalise,
            proj.nritem as projeto_numero,
            proj.noprojeto as projeto_nome,
            proj.dsprojeto as projeto_descricao,
            emp.nranobase as empresa_ano_base,
            emp.nrcnpj as empresa_cnpj,
            emp.norazaosocial as empresa_razao_social,
            preen.tporganismo as preen_tipo_organismo,
            preen.vlreceitaliquida as preen_receita_liquida,
            preen.nrtotalfuncionario as preen_total_funcionarios,
            preen.nrmediopesquisadordedicacaoexclusiva as preen_pesquisadores_exclusivos,
            preen.pcrecursoproprio as preen_percentual_recurso_proprio,
            proj.tppbpade as projeto_tipo_pesquisa,
            proj.dsareaprojeto as projeto_area,
            proj.dspalavrachave as projeto_palavras_chave,
            proj.tpnatureza as projeto_natureza,
            proj.dselementotecnologico as projeto_elemento_tecnologico,
            proj.dsdesafiotecnologico as projeto_desafio_tecnologico,
            proj.dsmetodologiautilizada as projeto_metodologia,
            proj.dsinicioatividade as projeto_inicio,
            proj.dsprevisaotermino as projeto_previsao_termino
        FROM tbdadoanaliseprojeto proj
        INNER JOIN tbdadoanalisepreenchimento preen 
            ON proj.idprenchimentosituacaoanalise = preen.idprenchimentosituacaoanalise
        INNER JOIN listaempresasporanobasesituacaoanalise emp 
            ON preen.idprenchimentosituacaoanalise = emp.idprenchimentosituacaoanalise
    ),
    marcos_do AS (
        SELECT 
            ma.idprenchimentosituacaoanalise,
            aom.iddadoanaliseprojeto,
            ma.idmarcoanalise as do_id_marco,
            ma.nrmarcoanalise as do_numero_marco,
            ma.dsobservacao as do_observacao,
            aom.dsjustificativapadrao as do_justificativa,
            aom.dsobservacaogeral as do_observacao_geral,
            aom.vltotaldeclarado as do_valor_declarado,
            ta.notipoavaliacaoanalise as do_tipo_avaliacao,
            CASE 
                WHEN ta.idtipoavaliacaoanalise = 1 THEN 'NÃO RECOMENDADO'
                WHEN ta.idtipoavaliacaoanalise = 2 THEN 'RECOMENDADO PARCIALMENTE' 
                WHEN ta.idtipoavaliacaoanalise = 3 THEN 'RECOMENDADO'
                ELSE 'AGUARDANDO ANÁLISE'
            END as do_resultado
        FROM tbmarcoanalise ma
        INNER JOIN tbanaliseobjetomarcoprojeto aom 
            ON ma.idmarcoanalise = aom.idmarcoanalise
        LEFT JOIN tbtipoavaliacaoanalise ta 
            ON aom.idtipoavaliacaoanalise = ta.idtipoavaliacaoanalise
        WHERE ma.cdtipomarcoanalise = 1
    ),
    marcos_parecer AS (
        SELECT 
            ma.idprenchimentosituacaoanalise,
            ma.idmarcoanalise as parecer_id_marco,
            ma.nrmarcoanalise as parecer_numero_marco,
            ma.dsobservacao as parecer_observacao,
            mdc.dsconclusao as parecer_conclusao,
            mdc.dsobservacaodo as parecer_observacao_do,
            mdc.vltotaldispendio as parecer_total_dispendio,
            mdc.vlaprovado as parecer_valor_aprovado,
            mdc.vlglosa as parecer_valor_glosa,
            mdc.nrtotalprojeto as parecer_total_projetos,
            mdc.nrtotalaprovado as parecer_projetos_aprovados,
            mdc.nrtotalreprovado as parecer_projetos_reprovados,
            rm.noresultadomarcoanalise as parecer_resultado
        FROM tbmarcoanalise ma
        LEFT JOIN tbmarcoanalisedadoconsolidado mdc 
            ON ma.idmarcoanalise = mdc.idmarcoanalise
        LEFT JOIN tbresultadomarcoanalise rm 
            ON ma.cdresultadomarcoanalise = rm.cdresultadomarcoanalise
        WHERE ma.cdtipomarcoanalise = 2
    ),
    marcos_contestacao AS (
        SELECT 
            ma.idprenchimentosituacaoanalise,
            ma.idmarcoanalise as contestacao_id_marco,
            ma.nrmarcoanalise as contestacao_numero_marco,
            apc.dsjustificativacontestacao as contestacao_justificativa,
            apc.dsjustificativapadrao as contestacao_resposta_padrao,
            apc.dsconsideracaoobservacaogeral as contestacao_consideracao,
            apc.dsobservacaogeralparecer as contestacao_obs_parecer,
            apc.dsrecursoadministrativo as contestacao_recurso_adm,
            apc.icsolicitacaoreanalise as contestacao_solicita_reanalise
        FROM tbmarcoanalise ma
        LEFT JOIN tbanaliseobjetomarcoprojetocontestacao apc 
            ON ma.idmarcoanalise = apc.idmarcoanalise
        WHERE ma.cdtipomarcoanalise = 3
    )
    SELECT 
        bp.iddadoanaliseprojeto,
        bp.idprenchimentosituacaoanalise,
        bp.projeto_numero,
        bp.projeto_nome,
        bp.empresa_ano_base,
        bp.empresa_cnpj,
        bp.empresa_razao_social,
        bp.preen_tipo_organismo,
        bp.preen_receita_liquida,
        bp.preen_total_funcionarios,
        bp.preen_pesquisadores_exclusivos,
        bp.preen_percentual_recurso_proprio,
        bp.projeto_tipo_pesquisa,
        bp.projeto_area,
        bp.projeto_natureza,
        bp.projeto_elemento_tecnologico,
        bp.projeto_desafio_tecnologico,
        bp.projeto_metodologia,
        bp.projeto_inicio,
        bp.projeto_previsao_termino,
        SUBSTRING(bp.projeto_descricao, 1, 200) as projeto_descricao_resumo,
        md.do_id_marco,
        md.do_numero_marco,
        md.do_resultado,
        md.do_valor_declarado,
        md.do_tipo_avaliacao,
        SUBSTRING(md.do_justificativa, 1, 200) as do_justificativa_resumo,
        SUBSTRING(md.do_observacao_geral, 1, 200) as do_observacao_resumo,
        mp.parecer_id_marco,
        mp.parecer_numero_marco,
        mp.parecer_resultado,
        mp.parecer_valor_aprovado,
        mp.parecer_valor_glosa,
        mp.parecer_projetos_aprovados,
        mp.parecer_projetos_reprovados,
        SUBSTRING(mp.parecer_conclusao, 1, 200) as parecer_conclusao_resumo,
        mc.contestacao_id_marco,
        mc.contestacao_numero_marco,
        mc.contestacao_solicita_reanalise,
        SUBSTRING(mc.contestacao_justificativa, 1, 200) as contestacao_justificativa_resumo,
        SUBSTRING(mc.contestacao_resposta_padrao, 1, 200) as contestacao_resposta_resumo,
        CASE WHEN md.do_id_marco IS NOT NULL THEN 1 ELSE 0 END as passou_analise_do,
        CASE WHEN mp.parecer_id_marco IS NOT NULL THEN 1 ELSE 0 END as passou_parecer,
        CASE WHEN mc.contestacao_id_marco IS NOT NULL THEN 1 ELSE 0 END as teve_contestacao,
        CASE 
            WHEN mc.contestacao_id_marco IS NOT NULL THEN 'CONTESTAÇÃO'
            WHEN mp.parecer_id_marco IS NOT NULL THEN 'PARECER CONCLUÍDO'
            WHEN md.do_id_marco IS NOT NULL THEN 'ANÁLISE DO CONCLUÍDA'
            ELSE 'PREENCHIMENTO'
        END as status_atual_processo
    FROM base_projetos bp
    LEFT JOIN marcos_do md 
        ON bp.idprenchimentosituacaoanalise = md.idprenchimentosituacaoanalise 
        AND bp.iddadoanaliseprojeto = md.iddadoanaliseprojeto
    LEFT JOIN marcos_parecer mp 
        ON bp.idprenchimentosituacaoanalise = mp.idprenchimentosituacaoanalise
    LEFT JOIN marcos_contestacao mc 
        ON bp.idprenchimentosituacaoanalise = mc.idprenchimentosituacaoanalise
    WHERE bp.empresa_ano_base = 2023
    ORDER BY bp.empresa_razao_social, bp.projeto_numero;
    """
    
    # Executar query e retornar DataFrame
    df = pd.read_sql_query(query, engine)
    return df

if __name__ == "__main__":
    print("Carregando dados da Lei do Bem...")
    df = carregar_dados()
    print(f"✅ {len(df)} projetos carregados")
    print(f"📊 Colunas disponíveis: {len(df.columns)}")
    print("\nPrimeiras 5 linhas:")
    print(df.head())
    
    # Salvar como CSV
    df.to_csv("projetos_lei_do_bem.csv", index=False)
    print("\n💾 Dados salvos em 'projetos_lei_do_bem.csv'")
