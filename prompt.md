# Prompt Adaptado para Análise de Dados Lei do Bem - Base Consolidada

## System Prompt
Você é um analista de dados altamente qualificado, especializado em identificar padrões, tendências e correlações em grandes conjuntos de dados do sistema da Lei do Bem do MCTI. Sua função é processar informações de projetos de P&D e extrair insights valiosos que possam otimizar processos de tomada de decisão e identificar inconsistências no fluxo de análise. Suas análises devem ser objetivas, rigorosas e apresentadas de forma clara e estruturada, utilizando terminologia analítica apropriada. Você é incentivado a pensar de forma crítica e a propor novas perspectivas de análise, mesmo que os dados iniciais não as revelem diretamente.

## User Prompt

Por favor, analise a tabela de dados consolidada de projetos da "Lei do Bem" que lhe fornecerei a seguir. Meu objetivo é entender os padrões de decisão existentes ao longo do fluxo completo do processo (Preenchimento → Análise DO → Parecer → Contestação) e identificar novas correlações que possam otimizar futuras avaliações e detectar inconsistências no sistema.

A estrutura da tabela é a seguinte, no formato CSV, com cada linha representando um projeto que passou pelo fluxo completo de análise:

### Identificação e Empresa
- `iddadoanaliseprojeto`: ID único do projeto
- `projeto_numero`: Número sequencial do projeto na empresa
- `projeto_nome`: Nome/título do projeto
- `empresa_cnpj`: CNPJ da empresa proponente
- `empresa_razao_social`: Razão social da empresa
- `empresa_ano_base`: Ano base da análise

### Fase 1: Preenchimento (Dados Iniciais)
- `preen_tipo_organismo`: Tipo de organismo (Privado/Público/Misto)
- `preen_receita_liquida`: Receita líquida da empresa
- `preen_total_funcionarios`: Total de funcionários
- `preen_pesquisadores_exclusivos`: Número médio de pesquisadores dedicação exclusiva
- `preen_percentual_recurso_proprio`: Percentual de recursos próprios

### Dados Técnicos do Projeto
- `projeto_tipo_pesquisa`: Tipo (PB - Pesquisa Básica, PA - Pesquisa Aplicada, DE - Desenvolvimento Experimental)
- `projeto_area`: Área do projeto
- `projeto_natureza`: Natureza (Produto/Processo)
- `projeto_elemento_tecnologico`: Elemento tecnológico inovador
- `projeto_desafio_tecnologico`: Desafio tecnológico a ser superado
- `projeto_metodologia`: Metodologia utilizada
- `projeto_inicio`: Data de início das atividades
- `projeto_previsao_termino`: Previsão de término

### Fase 2: Análise DO (Apoio Técnico)
- `do_id_marco`: ID do marco de análise DO
- `do_numero_marco`: Número do marco DO
- `do_resultado`: Resultado da análise (NÃO RECOMENDADO/RECOMENDADO PARCIALMENTE/RECOMENDADO)
- `do_valor_declarado`: Valor declarado na análise DO
- `do_tipo_avaliacao`: Tipo de avaliação aplicada
- `do_justificativa_resumo`: Resumo da justificativa da decisão DO
- `do_observacao_resumo`: Resumo das observações do analista DO

### Fase 3: Parecer (Consolidação)
- `parecer_id_marco`: ID do marco de parecer
- `parecer_numero_marco`: Número do marco parecer
- `parecer_resultado`: Resultado final (Recomendada/Recomendada com Incentivos Adicionais/Recomendada com Glosas)
- `parecer_valor_aprovado`: Valor aprovado no parecer
- `parecer_valor_glosa`: Valor glosado (rejeitado)
- `parecer_projetos_aprovados`: Número de projetos aprovados na empresa
- `parecer_projetos_reprovados`: Número de projetos reprovados na empresa
- `parecer_conclusao_resumo`: Resumo da conclusão do parecer

### Fase 4: Contestação (se houver)
- `contestacao_id_marco`: ID do marco de contestação
- `contestacao_numero_marco`: Número do marco contestação
- `contestacao_solicita_reanalise`: Se solicita reanálise (true/false)
- `contestacao_justificativa_resumo`: Resumo da justificativa da empresa
- `contestacao_resposta_resumo`: Resumo da resposta à contestação

### Indicadores de Progresso
- `passou_analise_do`: Se passou pela análise DO (1/0)
- `passou_parecer`: Se passou pelo parecer (1/0)
- `teve_contestacao`: Se teve contestação (1/0)
- `status_atual_processo`: Status atual (PREENCHIMENTO/ANÁLISE DO CONCLUÍDA/PARECER CONCLUÍDO/CONTESTAÇÃO)

---
{}
---

Com base nos dados da tabela consolidada e em sua capacidade analítica especializada em sistemas da Lei do Bem:

1. **Analise a consistência entre as fases do processo.** Compare os resultados da Análise DO com os Pareceres finais. Identifique casos onde houve mudança de decisão entre fases e as possíveis razões baseadas nas justificativas. Calcule a taxa de concordância entre DO e Parecer.

2. **Identifique padrões de contestação e suas características.** Analise quais tipos de projetos, áreas tecnológicas ou resultados de análise têm maior propensão a contestação. Examine se as contestações resultam em mudanças de decisão e quais argumentos são mais eficazes.

3. **Detecte possíveis inconsistências ou vieses no processo de avaliação.** Por exemplo, há diferenças sistemáticas de avaliação entre diferentes áreas tecnológicas? Projetos de empresas de determinado porte recebem tratamento diferenciado? Analise os valores declarados vs. aprovados para identificar padrões de glosas.

4. **Proponha no mínimo três (3) novos tipos de análises ou indicadores** que seriam relevantes para otimizar o processo da Lei do Bem, considerando fatores como:
   - Tempo de trâmite entre fases
   - Complexidade da linguagem técnica nas justificativas
   - Histórico de aprovação da empresa/setor
   - Correlação entre características da empresa (porte, setor) e taxa de aprovação
   - Indicadores de qualidade da documentação técnica
   - Padrões de comportamento dos avaliadores

Por favor, organize sua resposta em seções claras, como "Metodologia de Análise", "Descobertas sobre Consistência do Processo", "Padrões de Contestação", "Detecção de Inconsistências" e "Propostas de Otimização". Apresente tabelas, métricas e visualizações sempre que apropriado para facilitar a compreensão dos insights descobertos.