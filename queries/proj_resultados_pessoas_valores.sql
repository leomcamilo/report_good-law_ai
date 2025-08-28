select lst.idprenchimentosituacaoanalise as id_empresa_ano
, lst.nranobase as ano_referencia
--
-- Projeto - caracterização
--
, do_setor.nosetor as setor
, daproj.tpnatureza as natureza
, daproj.tppbpade as tipo_pesquisa
, concat('CNPJ: '::text , lst.nrcnpj::text ,' RAZÃO SOCIAL :'::text , lst.norazaosocial::text, ' ATIVIDADE ECONOMICA :'::text, lst.noatividadeeconomica::text,' Cd ATIV.ECONOMICA IBGE :'::text, lst.cdatividadeeconomicaibge::text, ' PORTE '::text, lst.notipoportepessoajuridica::text, ' ID EMPRESA/ANO :'::text, lst.idprenchimentosituacaoanalise) as Empresa
, concat('NÚMERO: '::text, daproj.nritem::text ,' ID ÚNICO: '::text, daproj.iddadoanaliseprojeto::text ,' NOME: '::text, daproj.noprojeto::text ,' DESCRIÇÂO: '::text, daproj.dsprojeto::text ,' AREA: '::text, daproj.dsareaprojeto::text ,' PALAVRAS CHAVE: '::text, daproj.dspalavrachave::text ,' ELEMENTO TECNOLÓGICO: '::text, daproj.dselementotecnologico::text ,' DESAFIO TECNOLÓGICO: '::text, daproj.dsdesafiotecnologico::text ,' METODOLOGIA: '::text, daproj.dsmetodologiautilizada::text ,' INFORMAÇÃO COMPLEMENTAR: '::text, daproj.dsinformacaocomplementar::text  ) as projeto
, concat('CICLO MAIOR QUE 1 ANO: '::text, daproj.icciclomaior::text , ' ATIVIDADE PDI CONTINUADA ANO ANTERIOR :'::text, daproj.dsatividadepdicontinuadaanobase::text) as projeto_multianual
, concat('ECONOMICO: '::text, daproj.dsresultadoeconomico::text ,' INOVACAO: '::text, daproj.dsresultadoinovacao::text ) as projeto_resultados
--
, dapdisp.cddadoanaliseprojetotipodispendio as cd_dispendio
, dapdisp.tptitulacao as titulacao
, dapdisp.vlhoras as horas
, dapdisp.vltotal as valor
, coalesce( dapdisp.vltotal/ nullif(dapdisp.vlhoras,0),0) as hh
--
-- Titulacao, Despesas
--
,total.valortotalproj
,doutor.valordoutorproj
,doutor.quantdoutorproj
,mestre.valormestreproj
,mestre.quantmestreproj
,rh.valorrhproj
,rh.quantrhproj
,ict.valorictproj 
,universidades.valoruniversidadesproj 
,servterceiros.valorservterceirosproj 
,coalesce(servterceiros.valorservterceirosproj/nullif(total.valortotalproj,0),0) as percservterceirosproj
,pessoalempresa.quantpessoalempresa
,coalesce(pessoalempresa.quantpessoalempresa/nullif(dapree.nrtotalfuncionario ,0),0) as percpessoalalocadoempresa
,doutorempresa.quantdoutorempresa
,mestreempresa.quantmestreempresa 
,totalempresa.valortotalempresa 
,servterceirosempresa.valorserterceirosempresa 
,coalesce(servterceirosempresa.valorserterceirosempresa/nullif(totalempresa.valortotalempresa,0),0) as percservterceirosempresa
,bensequipempresa.valorbensequipempresa 
,coalesce(bensequipempresa.valorbensequipempresa/nullif(totalempresa.valortotalempresa,0),0) as percbensequipempresa
--
-- DO analise
--
, do_comite.nocomite as do_comite
, do_saat.idunicopessoaanalise as do_id_at
, do_nd1.dsnotadimensao as do_relevancia_invocao
, do_nd2.dsnotadimensao as do_relevancia_resultado
, do_nd3.dsnotadimensao as do_relevancia_final
, concat( do_aomproj.dsobservacaogeral::text,' / ' ,do_aomproj.dsobservacaopadrao::text) as do_observacao
, do_aomproj.dsjustificativapadrao as do_justificativa_livre
, concat(do_a_proj.do_japroj_nojustificativaanalise::text,' / '::text, do_a_proj.do_japroj_notitulojustificativaanalise::text,' / '::text, do_a_proj.do_japroj_nocorpojustificativaanalise::text,' / '::text, do_a_proj.do_japroj_norodapejustificativaanalise::text,' / '::text, do_a_proj.do_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as do_justificativa_padronizada
, do_a_proj.do_tjaproj_notipojustificativaanalise as do_tipo_justificativa
, do_taaproj.notipoavaliacaoanalise as do_resultado_analise
, do_aomproj.vltotaldeclarado as do_valor_projeto
, do_disp_vl.do_disp_vlglosa as do_disp_vlglosa
, do_disp_vl.do_disp_vlindicadoanalise as do_disp_vlindicadoanalise
--
-- Parecer
--
, p_hsa.idunicopessoa as p_id_analista_mcti
, concat( p_aomproj.dsobservacaogeral::text,' / ' ,p_aomproj.dsobservacaopadrao::text) as p_observacao
, p_aomproj.dsjustificativapadrao as p_justificativa_livre
, concat(p_a_proj.p_japroj_nojustificativaanalise::text,' / '::text, p_a_proj.p_japroj_notitulojustificativaanalise::text,' / '::text, p_a_proj.p_japroj_nocorpojustificativaanalise::text,' / '::text, p_a_proj.p_japroj_norodapejustificativaanalise::text,' / '::text, p_a_proj.p_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as p_justificativa_padronizada
, p_a_proj.p_tjaproj_notipojustificativaanalise as p_tipo_justificativa
, p_taaproj.notipoavaliacaoanalise as p_resultado_analise
, p_aomproj.vltotaldeclarado as p_valor_projeto
, p_disp_vl.p_disp_vlglosa as p_disp_vlglosa
, p_disp_vl.p_disp_vlindicadoanalise as p_disp_vlindicadoanalise
--
-- DO contestacao
--
, do_c_aomprojc.dsjustificativacontestacao as empresa_do_contestacao
, do_c_comite.nocomite as do_c_comite
, do_c_saat.idunicopessoaanalise as do_c_id_at
, do_c_nd1.dsnotadimensao as do_c_relevancia_invocao
, do_c_nd2.dsnotadimensao as do_c_relevancia_resultado
, do_c_nd3.dsnotadimensao as do_c_relevancia_final
, concat( do_c_aomproj.dsobservacaogeral::text,' / ' ,do_c_aomproj.dsobservacaopadrao::text) as do_c_observacao
, do_c_aomproj.dsjustificativapadrao as do_c_justificativa_livre
, concat(do_c_a_proj.do_c_japroj_nojustificativaanalise::text,' / '::text, do_c_a_proj.do_c_japroj_notitulojustificativaanalise::text,' / '::text, do_c_a_proj.do_c_japroj_nocorpojustificativaanalise::text,' / '::text, do_c_a_proj.do_c_japroj_norodapejustificativaanalise::text,' / '::text, do_c_a_proj.do_c_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as do_c_justificativa_padronizada
, do_c_a_proj.do_c_tjaproj_notipojustificativaanalise as do_c_tipo_justificativa
, do_c_taaproj.notipoavaliacaoanalise as do_c_resultado_analise
, do_c_aomproj.vltotaldeclarado as do_c_valor_projeto
, do_c_disp_vl.do_c_disp_vlglosa as do_c_disp_vlglosa
, do_c_disp_vl.do_c_disp_vlindicadoanalise as do_c_disp_vlindicadoanalise
--
-- Parecer contestacao
--
, p_c_aomprojc.dsjustificativacontestacao as empresa_parecer_contestacao
, p_c_hsa.idunicopessoa as p_c_id_analista_mcti
, concat( p_c_aomproj.dsobservacaogeral::text,' / ' ,p_c_aomproj.dsobservacaopadrao::text) as p_c_observacao
, p_c_aomproj.dsjustificativapadrao as p_c_justificativa_livre
, concat(p_c_a_proj.p_c_japroj_nojustificativaanalise::text,' / '::text, p_c_a_proj.p_c_japroj_notitulojustificativaanalise::text,' / '::text, p_c_a_proj.p_c_japroj_nocorpojustificativaanalise::text,' / '::text, p_c_a_proj.p_c_japroj_norodapejustificativaanalise::text,' / '::text, p_c_a_proj.p_c_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as p_c_justificativa_padronizada
, p_c_a_proj.p_c_tjaproj_notipojustificativaanalise as p_c_tipo_justificativa
, p_c_taaproj.notipoavaliacaoanalise as p_c_resultado_analise
, p_c_aomproj.vltotaldeclarado as p_c_valor_projeto
, p_c_disp_vl.p_c_disp_vlglosa as p_c_disp_vlglosa
, p_c_disp_vl.p_c_disp_vlindicadoanalise as p_c_disp_vlindicadoanalise
--
-- Recurso Administrativo
--
, ra_aomprojc.dsrecursoadministrativo as empresa_recurso_administrativo
, ra_hsa.idunicopessoa as ra_id_analista_mcti
, concat( ra_aomproj.dsobservacaogeral::text,' / ' ,ra_aomproj.dsobservacaopadrao::text) as ra_observacao
, ra_aomproj.dsjustificativapadrao as ra_justificativa_livre
, concat(ra_a_proj.ra_japroj_nojustificativaanalise::text,' / '::text, ra_a_proj.ra_japroj_notitulojustificativaanalise::text,' / '::text, ra_a_proj.ra_japroj_nocorpojustificativaanalise::text,' / '::text, ra_a_proj.ra_japroj_norodapejustificativaanalise::text,' / '::text, ra_a_proj.ra_japroj_notitulojustificativagrupoobjetoanaliseindividual::text) as ra_justificativa_padronizada
, ra_a_proj.ra_tjaproj_notipojustificativaanalise as ra_tipo_justificativa
, ra_taaproj.notipoavaliacaoanalise as ra_resultado_analise
, ra_aomproj.vltotaldeclarado as ra_valor_projeto
, ra_disp_vl.ra_disp_vlglosa as ra_disp_vlglosa
, ra_disp_vl.ra_disp_vlindicadoanalise as ra_disp_vlindicadoanalise
--
--select count(*)
from tbdadoanaliseprojeto daproj
left join tbdadoempresamarco dem on dem.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise 
left join tbdadoanalisepreenchimento dapree on dapree.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
left join listaempresasporanobasesituacaoanalise lst on lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
--
left join tbdadoanaliseprojetodispendio dapdisp on dapdisp.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
--
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valortotalproj 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		group by dapdisp.iddadoanaliseprojeto ) total on total.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valordoutorproj , count(dapdisp.nrcnpjcpf  ) as quantdoutorproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.tptitulacao = 'Doutor'
		group by dapdisp.iddadoanaliseprojeto ) doutor on doutor.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valormestreproj , count(dapdisp.nrcnpjcpf  ) as quantmestreproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.tptitulacao in ('Doutor', 'Mestre')
		group by dapdisp.iddadoanaliseprojeto ) mestre on mestre.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valorrhproj , count(dapdisp.nrcnpjcpf  ) as quantrhproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.cddadoanaliseprojetotipodispendio = 9
		group by dapdisp.iddadoanaliseprojeto ) rh on rh.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valorictproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.cddadoanaliseprojetotipodispendio = 2 
		group by dapdisp.iddadoanaliseprojeto ) ict on ict.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valoruniversidadesproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.cddadoanaliseprojetotipodispendio = 1 
		group by dapdisp.iddadoanaliseprojeto ) universidades on universidades.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valorservterceirosproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.cddadoanaliseprojetotipodispendio in  ( 7, 8, 10)
		group by dapdisp.iddadoanaliseprojeto ) servterceiros on servterceiros.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select daproj.idprenchimentosituacaoanalise , count(distinct dapdisp.nrcnpjcpf  ) as quantpessoalempresa 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.cddadoanaliseprojetotipodispendio = 9 
		group by daproj.idprenchimentosituacaoanalise  ) pessoalempresa on pessoalempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise 
left join (
		select daproj.idprenchimentosituacaoanalise , count(distinct dapdisp.nrcnpjcpf  ) as quantdoutorempresa  
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.tptitulacao = 'Doutor'
		group by daproj.idprenchimentosituacaoanalise ) doutorempresa on doutorempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise
left join (
		select daproj.idprenchimentosituacaoanalise , count(distinct dapdisp.nrcnpjcpf  ) as quantmestreempresa 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.tptitulacao = 'Mestre'
		group by daproj.idprenchimentosituacaoanalise ) mestreempresa on mestreempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise
left join (
		select daproj.idprenchimentosituacaoanalise , sum(dapdisp.vltotal  ) as valorserterceirosempresa 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.cddadoanaliseprojetotipodispendio in  ( 7, 8, 10)
		group by daproj.idprenchimentosituacaoanalise ) servterceirosempresa on servterceirosempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise		
left join (
		select daproj.idprenchimentosituacaoanalise , sum(dapdisp.vltotal  ) as valortotalempresa 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		group by daproj.idprenchimentosituacaoanalise ) totalempresa on totalempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise		
left join (
		select daequip.idprenchimentosituacaoanalise , sum(daequip.vlbensintangiveisequipamento   ) as valorbensequipempresa 
		from tbdadoanalisebensintangiveisequipamento daequip 
		group by daequip.idprenchimentosituacaoanalise ) bensequipempresa on bensequipempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise
--
-- DO
--
left join tbmarcoanalise do_ma on do_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanalisedo = do_ma.idmarcoanalise
left join tbanaliseat do_aat on do_aat.idmarcoanalise = do_ma.idmarcoanalise and do_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbsituacaoanaliseat do_saat on do_saat.idanaliseat = do_aat.idanaliseat and do_saat.icativo 
left join tbsetor do_setor on do_setor.idsetor = do_saat.idsetor 
left join tbcomite do_comite on do_comite.idcomite = do_saat.idapoiotecnico 
left join tbavaliacaonotaprojeto do_anproj on do_anproj.idanaliseat = do_aat.idanaliseat
left join tbanaliseobjetomarcoprojeto do_aomproj on do_aomproj.idmarcoanalise = do_ma.idmarcoanalise and do_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join tbnotadimensao do_nd1 on do_nd1.cdnotadimensao = do_anproj.cdnotadimensaoinovacao 
left join tbnotadimensao do_nd2 on do_nd2.cdnotadimensao = do_anproj.cdnotadimensaoresultado  
left join tbnotadimensao do_nd3 on do_nd3.cdnotadimensao = do_anproj.cdnotafinal
left join tbtipoavaliacaoanalise do_taaproj on do_taaproj.idtipoavaliacaoanalise = do_aomproj.idtipoavaliacaoanalise
left join( 	
		select 	do_aomprojj.idanaliseobjetomarcoprojeto
			,STRING_AGG(do_japroj.nojustificativaanalise,' || ') as do_japroj_nojustificativaanalise
			,STRING_AGG(do_japroj.notitulojustificativaanalise,' || ') as do_japroj_notitulojustificativaanalise
			,STRING_AGG(do_japroj.nocorpojustificativaanalise,' || ') as do_japroj_nocorpojustificativaanalise
			,STRING_AGG(do_japroj.norodapejustificativaanalise,' || ') as do_japroj_norodapejustificativaanalise
			,STRING_AGG(do_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as do_japroj_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(do_tjaproj.notipojustificativaanalise,' || ') as do_tjaproj_notipojustificativaanalise
		from tbanaliseobjetomarcoprojetojustificativa do_aomprojj
		left join tbjustificativaanalise do_japroj on do_japroj.idjustificativaanalise = do_aomprojj.idjustificativaanalise
		left join tbtipojustificativaanalise do_tjaproj on do_tjaproj.cdtipojustificativaanalise = do_japroj.cdtipojustificativaanalise
		group by do_aomprojj.idanaliseobjetomarcoprojeto ) do_a_proj on do_a_proj.idanaliseobjetomarcoprojeto = do_aomproj.idanaliseobjetomarcoprojeto
left join (
		select aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto , sum(aomdisp.vlglosa::decimal ) as do_disp_vlglosa, sum(aomdisp.vlindicadoanalise::decimal  ) as do_disp_vlindicadoanalise 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbanaliseobjetomarcodispendio aomdisp on aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio 
		group by aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto 
		) do_disp_vl on do_disp_vl.iddadoanaliseprojeto  = daproj.iddadoanaliseprojeto and do_disp_vl.idmarcoanalise = do_ma.idmarcoanalise
--
--PARECER
--
left join tbmarcoanalise p_ma on p_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanaliseparecer = p_ma.idmarcoanalise
left join tbanaliseobjetomarcoprojeto p_aomproj on p_aomproj.idmarcoanalise = p_ma.idmarcoanalise and p_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise p_taaproj on p_taaproj.idtipoavaliacaoanalise = p_aomproj.idtipoavaliacaoanalise
left join( 	
		select 	p_aomprojj.idanaliseobjetomarcoprojeto
			,STRING_AGG(p_japroj.nojustificativaanalise,' || ') as p_japroj_nojustificativaanalise
			,STRING_AGG(p_japroj.notitulojustificativaanalise,' || ') as p_japroj_notitulojustificativaanalise
			,STRING_AGG(p_japroj.nocorpojustificativaanalise,' || ') as p_japroj_nocorpojustificativaanalise
			,STRING_AGG(p_japroj.norodapejustificativaanalise,' || ') as p_japroj_norodapejustificativaanalise
			,STRING_AGG(p_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as p_japroj_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(p_tjaproj.notipojustificativaanalise,' || ') as p_tjaproj_notipojustificativaanalise
		from tbanaliseobjetomarcoprojetojustificativa p_aomprojj
		left join tbjustificativaanalise p_japroj on p_japroj.idjustificativaanalise = p_aomprojj.idjustificativaanalise
		left join tbtipojustificativaanalise p_tjaproj on p_tjaproj.cdtipojustificativaanalise = p_japroj.cdtipojustificativaanalise
		group by p_aomprojj.idanaliseobjetomarcoprojeto ) p_a_proj on p_a_proj.idanaliseobjetomarcoprojeto = p_aomproj.idanaliseobjetomarcoprojeto		
left join(
		select hsa1.idhistoricosituacaoanalise, hsa1.idmarcoanalise, hsa1.idunicopessoa 
		from tbhistoricosituacaoanalise hsa1
		where hsa1.idhistoricosituacaoanalise in 
		(	select max(hsa2.idhistoricosituacaoanalise )
			from tbhistoricosituacaoanalise hsa2
			where hsa2.cdtiposituacaomarco = 2
			group by hsa2.idmarcoanalise )		
		) p_hsa on p_hsa.idmarcoanalise = p_ma.idmarcoanalise 
left join (
		select aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto , sum(aomdisp.vlglosa::decimal ) as p_disp_vlglosa, sum(aomdisp.vlindicadoanalise::decimal  ) as p_disp_vlindicadoanalise 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbanaliseobjetomarcodispendio aomdisp on aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio 
		group by aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto 
		) p_disp_vl on p_disp_vl.iddadoanaliseprojeto  = daproj.iddadoanaliseprojeto and p_disp_vl.idmarcoanalise = p_ma.idmarcoanalise
--
--DO CONTESTACAO
--
left join tbmarcoanalise do_c_ma on do_c_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanalisedocontestacao = do_c_ma.idmarcoanalise
left join tbanaliseat do_c_aat on do_c_aat.idmarcoanalise = do_c_ma.idmarcoanalise and do_c_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbsituacaoanaliseat do_c_saat on do_c_saat.idanaliseat = do_c_aat.idanaliseat and do_c_saat.icativo 
left join tbsetor do_c_setor on do_c_setor.idsetor = do_c_saat.idsetor 
left join tbcomite do_c_comite on do_c_comite.idcomite = do_c_saat.idapoiotecnico 
left join tbavaliacaonotaprojeto do_c_anproj on do_c_anproj.idanaliseat = do_c_aat.idanaliseat
left join tbanaliseobjetomarcoprojeto do_c_aomproj on do_c_aomproj.idmarcoanalise = do_c_ma.idmarcoanalise and do_c_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join tbnotadimensao do_c_nd1 on do_c_nd1.cdnotadimensao = do_c_anproj.cdnotadimensaoinovacao 
left join tbnotadimensao do_c_nd2 on do_c_nd2.cdnotadimensao = do_c_anproj.cdnotadimensaoresultado  
left join tbnotadimensao do_c_nd3 on do_c_nd3.cdnotadimensao = do_c_anproj.cdnotafinal
left join tbtipoavaliacaoanalise do_c_taaproj on do_c_taaproj.idtipoavaliacaoanalise = do_c_aomproj.idtipoavaliacaoanalise
left join tbanaliseobjetomarcoprojetocontestacao do_c_aomprojc on do_c_aomprojc.idmarcoanalise = do_c_aomproj.idmarcoanalise and do_c_aomprojc.idanaliseobjetomarcoprojetocontestacao = do_c_aomproj.idanaliseobjetomarcoprojeto
left join tbtipoavaliacaoanalise do_c_taaprojc on do_c_taaprojc.idtipoavaliacaoanalise = do_c_aomprojc.idtipoavaliacaoanalisecontestacao
left join( 	
		select 	do_c_aomprojj.idanaliseobjetomarcoprojeto
			,STRING_AGG(do_c_japroj.nojustificativaanalise,' || ') as do_c_japroj_nojustificativaanalise
			,STRING_AGG(do_c_japroj.notitulojustificativaanalise,' || ') as do_c_japroj_notitulojustificativaanalise
			,STRING_AGG(do_c_japroj.nocorpojustificativaanalise,' || ') as do_c_japroj_nocorpojustificativaanalise
			,STRING_AGG(do_c_japroj.norodapejustificativaanalise,' || ') as do_c_japroj_norodapejustificativaanalise
			,STRING_AGG(do_c_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as do_c_japroj_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(do_c_tjaproj.notipojustificativaanalise,' || ') as do_c_tjaproj_notipojustificativaanalise
		from tbanaliseobjetomarcoprojetojustificativa do_c_aomprojj
		left join tbjustificativaanalise do_c_japroj on do_c_japroj.idjustificativaanalise = do_c_aomprojj.idjustificativaanalise
		left join tbtipojustificativaanalise do_c_tjaproj on do_c_tjaproj.cdtipojustificativaanalise = do_c_japroj.cdtipojustificativaanalise
		group by do_c_aomprojj.idanaliseobjetomarcoprojeto ) do_c_a_proj on do_c_a_proj.idanaliseobjetomarcoprojeto = do_c_aomproj.idanaliseobjetomarcoprojeto
left join (
		select aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto , sum(aomdisp.vlglosa::decimal ) as do_c_disp_vlglosa, sum(aomdisp.vlindicadoanalise::decimal  ) as do_c_disp_vlindicadoanalise 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbanaliseobjetomarcodispendio aomdisp on aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio 
		group by aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto 
		) do_c_disp_vl on do_c_disp_vl.iddadoanaliseprojeto  = daproj.iddadoanaliseprojeto and do_c_disp_vl.idmarcoanalise = do_c_ma.idmarcoanalise
--
--PARECER CONTESTACAO
--
left join tbmarcoanalise p_c_ma on p_c_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanaliseparecercontestacao = p_c_ma.idmarcoanalise
left join tbanaliseobjetomarcoprojeto p_c_aomproj on p_c_aomproj.idmarcoanalise = p_c_ma.idmarcoanalise and p_c_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise p_c_taaproj on p_c_taaproj.idtipoavaliacaoanalise = p_c_aomproj.idtipoavaliacaoanalise
--
left join tbanaliseobjetomarcoprojetocontestacao p_c_aomprojc on p_c_aomprojc.idmarcoanalise = p_c_aomproj.idmarcoanalise and p_c_aomprojc.idanaliseobjetomarcoprojetocontestacao  = p_c_aomproj.idanaliseobjetomarcoprojeto
left join tbtipoavaliacaoanalise p_c_taaprojc on p_c_taaprojc.idtipoavaliacaoanalise = p_c_aomprojc.idtipoavaliacaoanalisecontestacao
left join( 	
		select 	p_c_aomprojj.idanaliseobjetomarcoprojeto
			,STRING_AGG(p_c_japroj.nojustificativaanalise,' || ') as p_c_japroj_nojustificativaanalise
			,STRING_AGG(p_c_japroj.notitulojustificativaanalise,' || ') as p_c_japroj_notitulojustificativaanalise
			,STRING_AGG(p_c_japroj.nocorpojustificativaanalise,' || ') as p_c_japroj_nocorpojustificativaanalise
			,STRING_AGG(p_c_japroj.norodapejustificativaanalise,' || ') as p_c_japroj_norodapejustificativaanalise
			,STRING_AGG(p_c_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as p_c_japroj_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(p_c_tjaproj.notipojustificativaanalise,' || ') as p_c_tjaproj_notipojustificativaanalise
		from tbanaliseobjetomarcoprojetojustificativa p_c_aomprojj
		left join tbjustificativaanalise p_c_japroj on p_c_japroj.idjustificativaanalise = p_c_aomprojj.idjustificativaanalise
		left join tbtipojustificativaanalise p_c_tjaproj on p_c_tjaproj.cdtipojustificativaanalise = p_c_japroj.cdtipojustificativaanalise
		group by p_c_aomprojj.idanaliseobjetomarcoprojeto ) p_c_a_proj on p_c_a_proj.idanaliseobjetomarcoprojeto = p_c_aomproj.idanaliseobjetomarcoprojeto		
left join(
		select hsa1.idhistoricosituacaoanalise, hsa1.idmarcoanalise, hsa1.idunicopessoa 
		from tbhistoricosituacaoanalise hsa1
		where hsa1.idhistoricosituacaoanalise in 
		(	select max(hsa2.idhistoricosituacaoanalise )
			from tbhistoricosituacaoanalise hsa2
			where hsa2.cdtiposituacaomarco = 15
			group by hsa2.idmarcoanalise )		
		) p_c_hsa on p_c_hsa.idmarcoanalise = p_c_ma.idmarcoanalise 
left join (
		select aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto , sum(aomdisp.vlglosa::decimal ) as p_c_disp_vlglosa, sum(aomdisp.vlindicadoanalise::decimal  ) as p_c_disp_vlindicadoanalise 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbanaliseobjetomarcodispendio aomdisp on aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio 
		group by aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto 
		) p_c_disp_vl on p_c_disp_vl.iddadoanaliseprojeto  = daproj.iddadoanaliseprojeto and p_c_disp_vl.idmarcoanalise = p_c_ma.idmarcoanalise
--
--RECURSO ADMINISTRATIVO
--
left join tbmarcoanalise ra_ma on ra_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanaliseparecercontestacao = ra_ma.idmarcoanalise
left join tbanaliseobjetomarcoprojeto ra_aomproj on ra_aomproj.idmarcoanalise = ra_ma.idmarcoanalise and ra_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise ra_taaproj on ra_taaproj.idtipoavaliacaoanalise = ra_aomproj.idtipoavaliacaoanalise
--
left join tbanaliseobjetomarcoprojetocontestacao ra_aomprojc on ra_aomprojc.idmarcoanalise = ra_aomproj.idmarcoanalise and ra_aomprojc.idanaliseobjetomarcoprojetocontestacao  = ra_aomproj.idanaliseobjetomarcoprojeto
left join tbtipoavaliacaoanalise ra_taaprojc on ra_taaprojc.idtipoavaliacaoanalise = ra_aomprojc.idtipoavaliacaoanalisecontestacao
left join( 	
		select 	ra_aomprojj.idanaliseobjetomarcoprojeto
			,STRING_AGG(ra_japroj.nojustificativaanalise,' || ') as ra_japroj_nojustificativaanalise
			,STRING_AGG(ra_japroj.notitulojustificativaanalise,' || ') as ra_japroj_notitulojustificativaanalise
			,STRING_AGG(ra_japroj.nocorpojustificativaanalise,' || ') as ra_japroj_nocorpojustificativaanalise
			,STRING_AGG(ra_japroj.norodapejustificativaanalise,' || ') as ra_japroj_norodapejustificativaanalise
			,STRING_AGG(ra_japroj.notitulojustificativagrupoobjetoanaliseindividual,' || ') as ra_japroj_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(ra_tjaproj.notipojustificativaanalise,' || ') as ra_tjaproj_notipojustificativaanalise
		from tbanaliseobjetomarcoprojetojustificativa ra_aomprojj
		left join tbjustificativaanalise ra_japroj on ra_japroj.idjustificativaanalise = ra_aomprojj.idjustificativaanalise
		left join tbtipojustificativaanalise ra_tjaproj on ra_tjaproj.cdtipojustificativaanalise = ra_japroj.cdtipojustificativaanalise
		group by ra_aomprojj.idanaliseobjetomarcoprojeto ) ra_a_proj on ra_a_proj.idanaliseobjetomarcoprojeto = ra_aomproj.idanaliseobjetomarcoprojeto		
left join(
		select hsa1.idhistoricosituacaoanalise, hsa1.idmarcoanalise, hsa1.idunicopessoa 
		from tbhistoricosituacaoanalise hsa1
		where hsa1.idhistoricosituacaoanalise in 
		(	select max(hsa2.idhistoricosituacaoanalise )
			from tbhistoricosituacaoanalise hsa2
			where hsa2.cdtiposituacaomarco = 36
			group by hsa2.idmarcoanalise )		
		) ra_hsa on ra_hsa.idmarcoanalise = ra_ma.idmarcoanalise 
left join (
		select aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto , sum(aomdisp.vlglosa::decimal ) as ra_disp_vlglosa, sum(aomdisp.vlindicadoanalise::decimal  ) as ra_disp_vlindicadoanalise 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbanaliseobjetomarcodispendio aomdisp on aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio 
		group by aomdisp.idmarcoanalise, daproj.iddadoanaliseprojeto 
		) ra_disp_vl on ra_disp_vl.iddadoanaliseprojeto  = daproj.iddadoanaliseprojeto and ra_disp_vl.idmarcoanalise = ra_ma.idmarcoanalise
where dem.idprenchimentosituacaoanalise = 753;

-- dapdisp.cddadoanaliseprojetotipodispendio = 9
-- --dapdisp.iddadoanaliseprojetodispendio = 1110862
-- --dem.idprenchimentosituacaoanalise = 753
-- and dapdisp.vlhoras > 2700
-- and lst.nranobase > 2020

-- where lst.nranobase = 2023
-- and daproj.dsatividadepdicontinuadaanobase is not null
