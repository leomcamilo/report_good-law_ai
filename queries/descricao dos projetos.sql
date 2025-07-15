-- Active: 1750170051954@@127.0.0.1@5432@dbs_mctic2@public

--
select 
lst.idprenchimentosituacaoanalise as id_empresa_ano
,lst.nranobase as ano_referencia
, concat('CNPJ: '::text , lst.nrcnpj::text ,' RAZÃO SOCIAL :'::text , lst.norazaosocial::text, ' ATIVIDADE ECONOMICA :'::text, lst.noatividadeeconomica::text,' Cd ATIV.ECONOMICA IBGE :'::text, lst.cdatividadeeconomicaibge::text, ' PORTE '::text, lst.notipoportepessoajuridica::text, ' ID EMPRESA/ANO :'::text, lst.idprenchimentosituacaoanalise) as Empresa
, concat('NÚMERO: '::text, daproj.nritem::text ,' ID ÚNICO: '::text, daproj.iddadoanaliseprojeto::text ,' NOME: '::text, daproj.noprojeto::text ,' DESCRIÇÃO: '::text, daproj.dsprojeto::text ,' TIPO (PA ou DE): '::text, daproj.tppbpade::text ,' AREA: '::text, daproj.dsareaprojeto::text ,' PALAVRAS CHAVE: '::text, daproj.dspalavrachave::text ,' NATUREZA: '::text, daproj.tpnatureza::text ,' ELEMENTO TECNOLÓGICO: '::text, daproj.dselementotecnologico::text ,' DESAFIO TECNOLÓGICO: '::text, daproj.dsdesafiotecnologico::text ,' METODOLOGIA: '::text, daproj.dsmetodologiautilizada::text ,' INFORMAÇÃO COMPLEMENTAR: '::text, daproj.dsinformacaocomplementar::text ,' RESULTADO ECONÔMICO: '::text, daproj.dsresultadoeconomico::text ,' RESULTADO INOVAÇÃO: '::text, daproj.dsresultadoinovacao::text ,' DESCRIÇÃO RH: '::text, daproj.dsrecursoshumanos::text ,' DESCRIÇÃO MATERIAIS: '::text, daproj.dsrecursosmateriais::text ,' SETOR PARA ANALISE DO PROJETO: '::text, do_set.nosetor::text) as projeto
, concat('CICLO MAIOR QUE 1 ANO: '::text, daproj.icciclomaior::text , ' ATIVIDADE PDI CONTINUADA ANO ANTERIOR :'::text, daproj.dsatividadepdicontinuadaanobase::text) as projeto_multianual
--
--,concat('NÚMERO: '::text, daproj.nritem::text ,'ID ÚNICO: '::text, daproj.iddadoanaliseprojeto::text ,'NOME: '::text, daproj.noprojeto::text ,'DESCRIÇÃO: '::text, daproj.dsprojeto::text ,'TIPO (PA ou DE): '::text, daproj.tppbpade::text ,'AREA: '::text, daproj.dsareaprojeto::text ,'PALAVRAS CHAVE: '::text, daproj.dspalavrachave::text ,'NATUREZA: '::text, daproj.tpnatureza::text ,'ELEMENTO TECNOLÓGICO: '::text, daproj.dselementotecnologico::text ,'DESAFIO TECNOLÓGICO: '::text, daproj.dsdesafiotecnologico::text ,'METODOLOGIA: '::text, daproj.dsmetodologiautilizada::text ,'CICLO MAIOR QUE 1 ANO: '::text, daproj.icciclomaior::text ,'daproj_dsinicioatividade: '::text, daproj.dsinicioatividade::text ,'daproj_dsprevisaotermino: '::text, daproj.dsprevisaotermino::text ,'INFORMAÇÃO COMPLEMENTAR: '::text, daproj.dsinformacaocomplementar::text ,'RESULTADO ECONÔMICO: '::text, daproj.dsresultadoeconomico::text ,'RESULTADO INOVAÇÃO: '::text, daproj.dsresultadoinovacao::text ,'DESCRIÇÃO RH: '::text, daproj.dsrecursoshumanos::text ,'DESCRIÇÃO MATERIAIS: '::text, daproj.dsrecursosmateriais::text ,'ATIVIDADE PDI CONTINUADA ANO ANTERIOR: '::text, daproj.dsatividadepdicontinuadaanobase::text ,'SETOR PARA ANALISE DO PROJETO: '::text, do_set.nosetor::text) as projeto
--
--
from tbdadoempresamarco dem
left join listaempresasporanobasesituacaoanalise lst on lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
left join tbdadoanaliseprojeto daproj on daproj.idprenchimentosituacaoanalise  = dem.idprenchimentosituacaoanalise
--
--DO
--
left join tbanaliseobjetomarcoprojeto do_aomproj on do_aomproj.idmarcoanalise = dem.idmarcoanalisedo and do_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbanaliseat do_aat on do_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto and do_aat.idmarcoanalise = dem.idmarcoanalisedo
left join tbsituacaoanaliseat do_saat on do_saat.idanaliseat = do_aat.idanaliseat and do_saat.icativo 
left join tbsetor do_set on do_set.idsetor = do_saat.idsetor
where (lst.norazaosocial ilike '%BANCO ITAU%' or  lst.norazaosocial ilike '%BANCO do brasil%' or  lst.norazaosocial ilike '%petrobras%') AND lst.nranobase = 2021
order by lst.idprenchimentosituacaoanalise, daproj.nritem;

--where --daproj.dsrecursoshumanos is not null
--daproj.icciclomaior is not null
--daproj.dsatividadepdicontinuadaanobase is not null

--concat text