select daproj.nritem 
, lst.norazaosocial
,dem.idprenchimentosituacaoanalise as dem_idprenchimentosituacaoanalise
, dem.idmarcoanalisedo as dem_idmarcoanalisedo
, dem.nrmarcoanalisedo as dem_nrmarcoanalisedo
, dem.dtmarcoanalisedo as dem_dtmarcoanalisedo
, dem.idmarcoanaliseparecer as dem_idmarcoanaliseparecer
, dem.nrmarcoanaliseparecer as dem_nrmarcoanaliseparecer
, dem.dtmarcoanaliseparecer as dem_dtmarcoanaliseparecer
, dem.idmarcoanalisecontestacao as dem_idmarcoanalisecontestacao
, dem.nrmarcoanalisecontestacao as dem_nrmarcoanalisecontestacao
, dem.dtmarcoanalisecontestacao as dem_dtmarcoanalisecontestacao
, dem.idmarcoanalisedocontestacao as dem_idmarcoanalisedocontestacao
, dem.nrmarcoanalisedocontestacao as dem_nrmarcoanalisedocontestacao
, dem.dtmarcoanalisedocontestacao as dem_dtmarcoanalisedocontestacao
, dem.idmarcoanaliseparecercontestacao as dem_idmarcoanaliseparecercontestacao
, dem.dtmarcoanaliseparecercontestacao as dem_dtmarcoanaliseparecercontestacao
, dem.nrmarcoanaliseparecercontestacao as dem_nrmarcoanaliseparecercontestacao
, dem.idmarcoanaliserecurso as dem_idmarcoanaliserecurso
, dem.dtmarcoanaliserecurso as dem_dtmarcoanaliserecurso
, dem.nrmarcoanaliserecurso as dem_nrmarcoanaliserecurso
, dem.idmarcoanaliseparecerrecurso as dem_idmarcoanaliseparecerrecurso
, dem.nrmarcoanaliseparecerrecurso as dem_nrmarcoanaliseparecerrecurso
, dem.dtmarcoanaliseparecerrecurso as dem_dtmarcoanaliseparecerrecurso
, dem.nrmarcoanalisecontestacaocodigoautencidade as dem_nrmarcoanalisecontestacaocodigoautencidade
, dem.nrmarcoanaliserecursocodigoautencidade as dem_nrmarcoanaliserecursocodigoautencidade
, daproj.iddadoanaliseprojeto as daproj_iddadoanaliseprojeto
, daproj.idprenchimentosituacaoanalise as daproj_idprenchimentosituacaoanalise
, daproj.idagrupadorresposta as daproj_idagrupadorresposta
, daproj.nritem as daproj_nritem
, daproj.noprojeto as daproj_noprojeto
, daproj.dsprojeto as daproj_dsprojeto
, daproj.tppbpade as daproj_tppbpade
, daproj.dsareaprojeto as daproj_dsareaprojeto
, daproj.dspalavrachave as daproj_dspalavrachave
, daproj.tpnatureza as daproj_tpnatureza
, daproj.dselementotecnologico as daproj_dselementotecnologico
, daproj.dsdesafiotecnologico as daproj_dsdesafiotecnologico
, daproj.dsmetodologiautilizada as daproj_dsmetodologiautilizada
, daproj.icciclomaior as daproj_icciclomaior
, daproj.dsinicioatividade as daproj_dsinicioatividade
, daproj.dsprevisaotermino as daproj_dsprevisaotermino
, daproj.dsinformacaocomplementar as daproj_dsinformacaocomplementar
, daproj.dsresultadoeconomico as daproj_dsresultadoeconomico
, daproj.dsresultadoinovacao as daproj_dsresultadoinovacao
, daproj.dsrecursoshumanos as daproj_dsrecursoshumanos
, daproj.dsrecursosmateriais as daproj_dsrecursosmateriais
, daproj.dsatividadepdicontinuadaanobase as daproj_dsatividadepdicontinuadaanobase
, daproj.idprojetoformpd as daproj_idprojetoformpd
, dapdisp.iddadoanaliseprojetodispendio as dapdisp_iddadoanaliseprojetodispendio
, dapdisp.iddadoanaliseprojeto as dapdisp_iddadoanaliseprojeto
, dapdisp.idagrupadorrespostapai as dapdisp_idagrupadorrespostapai
, dapdisp.idagrupadorresposta as dapdisp_idagrupadorresposta
, dapdisp.nritem as dapdisp_nritem
, dapdisp.tpsituacao as dapdisp_tpsituacao
, dapdisp.nrcnpjcpf as dapdisp_nrcnpjcpf
, dapdisp.nodispendio as dapdisp_nodispendio
, dapdisp.vltotal as dapdisp_vltotal
, dapdisp.dscaracterizarservico as dapdisp_dscaracterizarservico
, dapdisp.tptitulacao as dapdisp_tptitulacao
, dapdisp.vlhoras as dapdisp_vlhoras
, dapdisp.tpdedicacao as dapdisp_tpdedicacao
, dapdisp.dsmaterial as dapdisp_dsmaterial
, dapdisp.dsatividaderealizada as dapdisp_dsatividaderealizada
, dapdisp.dsfuncaorh as dapdisp_dsfuncaorh
--, daptdisp.nodadoanaliseprojetotipodispendio as daptdisp_nodadoanaliseprojetotipodispendio
--, daptdisp.notipodispendio as daptdisp_notipodispendio
--, daptdisp.nogrupotipodispendio as daptdisp_nogrupotipodispendio
--
, do_ma.idprenchimentosituacaoanalise
, do_ma.idmarcoanalise as do_ma_idmarcoanalise
, do_tma.notipomarcoanalise as do_tma_notipomarcoanalise
, do_dispendio.valordispendio as do_dispendio_valordispendio
, do_dispendio.valoranalisedispendio as do_dispendio_valoranalisedispendio
, do_dispendio.valorglosadispendio as do_dispendio_valorglosadispendio
, do_dispendio.totaldispendio as do_dispendio_totaldispendio
, do_taaproj.notipoavaliacaoanalise as do_taaproj_notipoavaliacaoanalis
, do_aomdisp.idmarcoanalise as do_aomdisp_idmarcoanalise
, do_aomdisp.icanalisetotal as do_aomdisp_icanalisetotal
, do_aomdisp.icjustificativapadraoalterada as do_aomdisp_icjustificativapadraoalterada
, do_aomdisp.dsjustificativapadrao as do_aomdisp_dsjustificativapadrao
, daproj.nritem
, do_aomdisp.vlindicadoanalise as do_aomdisp_vlindicadoanalise
, do_aomdisp.vlglosa as do_aomdisp_vlglosa
, do_aomdisp.icreanalisado as do_aomdisp_icreanalisado
, do_aomdisp.iddadoanaliseprojetodispendio as do_aomdisp_iddadoanaliseprojetodispendio
, do_aomdisp.icmantemresposta as do_aomdisp_icmantemresposta
, do_aomdisp.vlindicadoanalisedo as do_aomdisp_vlindicadoanalisedo
, do_aomdisp.dsjustificativapadraodo as do_aomdisp_dsjustificativapadraodo
, do_a_disp.idanaliseobjetomarcodispendio as do_aomdispj_idanaliseobjetomarcodispendio  
, daproj.nritem
, do_a_disp.do_jadisp_nojustificativaanalise
, do_a_disp.do_jadisp_notitulojustificativaanalise
, do_a_disp.do_jadisp_nocorpojustificativaanalise
, do_a_disp.do_jadisp_norodapejustificativaanalise
, do_a_disp.do_jadisp_notitulojustificativagrupoobjetoanaliseindividual
, do_a_disp.do_tjadisp_notipojustificativaanalise
, do_taadisp.notipoavaliacaoanalise as do_taadisp_notipoavaliacaoanalise
--
, p_ma.idprenchimentosituacaoanalise
, p_ma.idmarcoanalise as p_ma_idmarcoanalise
, p_tma.notipomarcoanalise as p_tma_notipomarcoanalise
, p_dispendio.valordispendio as p_dispendio_valordispendio
, p_dispendio.valoranalisedispendio as p_dispendio_valoranalisedispendio
, p_dispendio.valorglosadispendio as p_dispendio_valorglosadispendio
, p_dispendio.totaldispendio as p_dispendio_totaldispendio
, p_taaproj.notipoavaliacaoanalise as p_taaproj_notipoavaliacaoanalis
, p_aomdisp.idmarcoanalise as p_aomdisp_idmarcoanalise
, p_aomdisp.icanalisetotal as p_aomdisp_icanalisetotal
, p_aomdisp.icjustificativapadraoalterada as p_aomdisp_icjustificativapadraoalterada
, p_aomdisp.dsjustificativapadrao as p_aomdisp_dsjustificativapadrao
, daproj.nritem
, p_aomdisp.vlindicadoanalise as p_aomdisp_vlindicadoanalise
, p_aomdisp.vlglosa as p_aomdisp_vlglosa
, p_aomdisp.icreanalisado as p_aomdisp_icreanalisado
, p_aomdisp.iddadoanaliseprojetodispendio as p_aomdisp_iddadoanaliseprojetodispendio
, p_aomdisp.icmantemresposta as p_aomdisp_icmantemresposta
, p_aomdisp.vlindicadoanalisedo as p_aomdisp_vlindicadoanalisedo
, p_aomdisp.dsjustificativapadraodo as p_aomdisp_dsjustificativapadraodo
, p_a_disp.idanaliseobjetomarcodispendio as p_aomdispj_idanaliseobjetomarcodispendio  
, daproj.nritem
, p_a_disp.p_jadisp_nojustificativaanalise
, p_a_disp.p_jadisp_notitulojustificativaanalise
, p_a_disp.p_jadisp_nocorpojustificativaanalise
, p_a_disp.p_jadisp_norodapejustificativaanalise
, p_a_disp.p_jadisp_notitulojustificativagrupoobjetoanaliseindividual
, p_a_disp.p_tjadisp_notipojustificativaanalise
, p_taadisp.notipoavaliacaoanalise as p_taadisp_notipoavaliacaoanalise
--
, do_c_ma.idprenchimentosituacaoanalise
, do_c_ma.idmarcoanalise as do_c_ma_idmarcoanalise
, do_c_tma.notipomarcoanalise as do_c_tma_notipomarcoanalise
, do_c_dispendio.valordispendio as do_c_dispendio_valordispendio
, do_c_dispendio.valoranalisedispendio as do_c_dispendio_valoranalisedispendio
, do_c_dispendio.valorglosadispendio as do_c_dispendio_valorglosadispendio
, do_c_dispendio.totaldispendio as do_c_dispendio_totaldispendio
, do_c_taaproj.notipoavaliacaoanalise as do_c_taaproj_notipoavaliacaoanalis
, do_c_aomdisp.idmarcoanalise as do_c_aomdisp_idmarcoanalise
, do_c_aomdisp.icanalisetotal as do_c_aomdisp_icanalisetotal
, do_c_aomdisp.icjustificativapadraoalterada as do_c_aomdisp_icjustificativapadraoalterada
, do_c_aomdisp.dsjustificativapadrao as do_c_aomdisp_dsjustificativapadrao
, daproj.nritem
, do_c_aomdisp.vlindicadoanalise as do_c_aomdisp_vlindicadoanalise
, do_c_aomdisp.vlglosa as do_c_aomdisp_vlglosa
, do_c_aomdisp.icreanalisado as do_c_aomdisp_icreanalisado
, do_c_aomdisp.iddadoanaliseprojetodispendio as do_c_aomdisp_iddadoanaliseprojetodispendio
, do_c_aomdisp.icmantemresposta as do_c_aomdisp_icmantemresposta
, do_c_aomdisp.vlindicadoanalisedo as do_c_aomdisp_vlindicadoanalisedo
, do_c_aomdisp.dsjustificativapadraodo as do_c_aomdisp_dsjustificativapadraodo
, do_c_a_disp.idanaliseobjetomarcodispendio as do_c_aomdispj_idanaliseobjetomarcodispendio  
, daproj.nritem
, do_c_a_disp.do_c_jadisp_nojustificativaanalise
, do_c_a_disp.do_c_jadisp_notitulojustificativaanalise
, do_c_a_disp.do_c_jadisp_nocorpojustificativaanalise
, do_c_a_disp.do_c_jadisp_norodapejustificativaanalise
, do_c_a_disp.do_c_jadisp_notitulojustificativagrupoobjetoanaliseindividual
, do_c_a_disp.do_c_tjadisp_notipojustificativaanalise
--
,do_c_aomdispc.vlcontestacao as do_c_aomdispc_vlcontestacao
,do_c_aomdispc.dsjustificativacontestacao as do_c_aomdispc_dsjustificativacontestacao
,do_c_aomdispc.dsjustificativaparecer as do_c_aomdispc_dsjustificativaparecer
,do_c_aomdispc.vlindicadoanaliseparecer as do_c_aomdispc_vlindicadoanaliseparecer
,do_c_aomdispc.vlglosaparecer as do_c_aomdispc_vlglosaparecer
,do_c_aomdispc.icitemretificado as do_c_aomdispc_icitemretificado
,do_c_aomdispc.vlanalisecontestacao as do_c_aomdispc_vlanalisecontestacao
,do_c_aomdispc.dsjustificativaanalisecontestacao as do_c_aomdispc_dsjustificativaanalisecontestacao
,do_c_aomdispc.vlrecursoadministrativo as do_c_aomdispc_vlrecursoadministrativo
,do_c_aomdispc.dsjustificativarecursoadministrativo as do_c_aomdispc_dsjustificativarecursoadministrativo
, do_c_taadisp.notipoavaliacaoanalise as do_c_taadisp_notipoavaliacaoanalise
--
, p_c_ma.idprenchimentosituacaoanalise
, p_c_ma.idmarcoanalise as p_c_ma_idmarcoanalise
, p_c_tma.notipomarcoanalise as p_c_tma_notipomarcoanalise
, p_c_dispendio.valordispendio as p_c_dispendio_valordispendio
, p_c_dispendio.valoranalisedispendio as p_c_dispendio_valoranalisedispendio
, p_c_dispendio.valorglosadispendio as p_c_dispendio_valorglosadispendio
, p_c_dispendio.totaldispendio as p_c_dispendio_totaldispendio
, p_c_taaproj.notipoavaliacaoanalise as p_c_taaproj_notipoavaliacaoanalis
, p_c_aomdisp.idmarcoanalise as p_c_aomdisp_idmarcoanalise
, p_c_aomdisp.icanalisetotal as p_c_aomdisp_icanalisetotal
, p_c_aomdisp.icjustificativapadraoalterada as p_c_aomdisp_icjustificativapadraoalterada
, p_c_aomdisp.dsjustificativapadrao as p_c_aomdisp_dsjustificativapadrao
, daproj.nritem
, p_c_aomdisp.vlindicadoanalise as p_c_aomdisp_vlindicadoanalise
, p_c_aomdisp.vlglosa as p_c_aomdisp_vlglosa
, p_c_aomdisp.icreanalisado as p_c_aomdisp_icreanalisado
, p_c_aomdisp.iddadoanaliseprojetodispendio as p_c_aomdisp_iddadoanaliseprojetodispendio
, p_c_aomdisp.icmantemresposta as p_c_aomdisp_icmantemresposta
, p_c_aomdisp.vlindicadoanalisedo as p_c_aomdisp_vlindicadoanalisedo
, p_c_aomdisp.dsjustificativapadraodo as p_c_aomdisp_dsjustificativapadraodo
, p_c_a_disp.idanaliseobjetomarcodispendio as p_c_aomdispj_idanaliseobjetomarcodispendio  
, daproj.nritem
, p_c_a_disp.p_c_jadisp_nojustificativaanalise
, p_c_a_disp.p_c_jadisp_notitulojustificativaanalise
, p_c_a_disp.p_c_jadisp_nocorpojustificativaanalise
, p_c_a_disp.p_c_jadisp_norodapejustificativaanalise
, p_c_a_disp.p_c_jadisp_notitulojustificativagrupoobjetoanaliseindividual
, p_c_a_disp.p_c_tjadisp_notipojustificativaanalise
--
,p_c_aomdispc.vlcontestacao as p_c_aomdispc_vlcontestacao
,p_c_aomdispc.dsjustificativacontestacao as p_c_aomdispc_dsjustificativacontestacao
,p_c_aomdispc.dsjustificativaparecer as p_c_aomdispc_dsjustificativaparecer
,p_c_aomdispc.vlindicadoanaliseparecer as p_c_aomdispc_vlindicadoanaliseparecer
,p_c_aomdispc.vlglosaparecer as p_c_aomdispc_vlglosaparecer
,p_c_aomdispc.icitemretificado as p_c_aomdispc_icitemretificado
,p_c_aomdispc.vlanalisecontestacao as p_c_aomdispc_vlanalisecontestacao
,p_c_aomdispc.dsjustificativaanalisecontestacao as p_c_aomdispc_dsjustificativaanalisecontestacao
,p_c_aomdispc.vlrecursoadministrativo as p_c_aomdispc_vlrecursoadministrativo
,p_c_aomdispc.dsjustificativarecursoadministrativo as p_c_aomdispc_dsjustificativarecursoadministrativo
, p_c_taadisp.notipoavaliacaoanalise as p_c_taadisp_notipoavaliacaoanalise
--
, ra_ma.idprenchimentosituacaoanalise
, ra_ma.idmarcoanalise as ra_ma_idmarcoanalise
, ra_tma.notipomarcoanalise as ra_tma_notipomarcoanalise
, ra_dispendio.valordispendio as ra_dispendio_valordispendio
, ra_dispendio.valoranalisedispendio as ra_dispendio_valoranalisedispendio
, ra_dispendio.valorglosadispendio as ra_dispendio_valorglosadispendio
, ra_dispendio.totaldispendio as ra_dispendio_totaldispendio
, ra_taaproj.notipoavaliacaoanalise as ra_taaproj_notipoavaliacaoanalis
, ra_aomdisp.idmarcoanalise as ra_aomdisp_idmarcoanalise
, ra_aomdisp.icanalisetotal as ra_aomdisp_icanalisetotal
, ra_aomdisp.icjustificativapadraoalterada as ra_aomdisp_icjustificativapadraoalterada
, ra_aomdisp.dsjustificativapadrao as ra_aomdisp_dsjustificativapadrao
, daproj.nritem
, ra_aomdisp.vlindicadoanalise as ra_aomdisp_vlindicadoanalise
, ra_aomdisp.vlglosa as ra_aomdisp_vlglosa
, ra_aomdisp.icreanalisado as ra_aomdisp_icreanalisado
, ra_aomdisp.iddadoanaliseprojetodispendio as ra_aomdisp_iddadoanaliseprojetodispendio
, ra_aomdisp.icmantemresposta as ra_aomdisp_icmantemresposta
, ra_aomdisp.vlindicadoanalisedo as ra_aomdisp_vlindicadoanalisedo
, ra_aomdisp.dsjustificativapadraodo as ra_aomdisp_dsjustificativapadraodo
, ra_a_disp.idanaliseobjetomarcodispendio as ra_aomdispj_idanaliseobjetomarcodispendio  
, daproj.nritem
, ra_a_disp.ra_jadisp_nojustificativaanalise
, ra_a_disp.ra_jadisp_notitulojustificativaanalise
, ra_a_disp.ra_jadisp_nocorpojustificativaanalise
, ra_a_disp.ra_jadisp_norodapejustificativaanalise
, ra_a_disp.ra_jadisp_notitulojustificativagrupoobjetoanaliseindividual
, ra_a_disp.ra_tjadisp_notipojustificativaanalise
--
,ra_aomdispc.vlcontestacao as ra_aomdispc_vlcontestacao
,ra_aomdispc.dsjustificativacontestacao as ra_aomdispc_dsjustificativacontestacao
,ra_aomdispc.dsjustificativaparecer as ra_aomdispc_dsjustificativaparecer
,ra_aomdispc.vlindicadoanaliseparecer as ra_aomdispc_vlindicadoanaliseparecer
,ra_aomdispc.vlglosaparecer as ra_aomdispc_vlglosaparecer
,ra_aomdispc.icitemretificado as ra_aomdispc_icitemretificado
,ra_aomdispc.vlanalisecontestacao as ra_aomdispc_vlanalisecontestacao
,ra_aomdispc.dsjustificativaanalisecontestacao as ra_aomdispc_dsjustificativaanalisecontestacao
,ra_aomdispc.vlrecursoadministrativo as ra_aomdispc_vlrecursoadministrativo
,ra_aomdispc.dsjustificativarecursoadministrativo as ra_aomdispc_dsjustificativarecursoadministrativo
, ra_taadisp.notipoavaliacaoanalise as ra_taadisp_notipoavaliacaoanalise
--
-- DO
--
--select count (*)
from tbdadoempresamarco dem
left join tbmarcoanalise do_ma on do_ma.idmarcoanalise = dem.idmarcoanalisedo 
left join tbdadoanaliseprojeto daproj on daproj.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
left join tbanaliseobjetomarcoprojeto do_aomproj on do_aomproj.idmarcoanalise = do_ma.idmarcoanalise and do_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise do_taaproj on do_taaproj.idtipoavaliacaoanalise = do_aomproj.idtipoavaliacaoanalise
left join tbdadoanaliseprojetodispendio dapdisp on dapdisp.iddadoanaliseprojeto = do_aomproj.iddadoanaliseprojeto 
left join tbanaliseobjetomarcodispendio do_aomdisp on do_aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio and do_aomdisp.idmarcoanalise = do_ma.idmarcoanalise 
left join tbtipoavaliacaoanalise do_taadisp on do_taadisp.idtipoavaliacaoanalise = do_aomdisp.idtipoavaliacaoanalise
left join listaempresasporanobasesituacaoanalise lst on lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
left join tbtipomarcoanalise do_tma on do_tma.cdtipomarcoanalise  = do_ma.cdtipomarcoanalise 
--
left join ( 
    select idprenchimentosituacaoanalise
    , idmarcoanalise
    , apd.iddadoanaliseprojetodispendio
    , sum(apd.vltotal) as valordispendio
    , sum(amd.vlindicadoanalise::decimal) as valoranalisedispendio
    , sum(amd.vlglosa::decimal) as valorglosadispendio
    , count(1) as totaldispendio
    from tbdadoanaliseprojeto apj
    join tbdadoanaliseprojetodispendio apd on apd.iddadoanaliseprojeto = apj.iddadoanaliseprojeto
    left join tbanaliseobjetomarcodispendio amd 
        on amd.iddadoanaliseprojetodispendio = apd.iddadoanaliseprojetodispendio
    group by idprenchimentosituacaoanalise, idmarcoanalise, apd.iddadoanaliseprojetodispendio
) do_dispendio
on do_dispendio.idprenchimentosituacaoanalise = do_ma.idprenchimentosituacaoanalise
and do_dispendio.idmarcoanalise = do_ma.idmarcoanalise
and do_dispendio.iddadoanaliseprojetodispendio = do_aomdisp.iddadoanaliseprojetodispendio
--
left join( 
	select 	do_aomdispj.idanaliseobjetomarcodispendio
			,STRING_AGG(do_jadisp.nojustificativaanalise,CHR(10)) as do_jadisp_nojustificativaanalise
			,STRING_AGG(do_jadisp.notitulojustificativaanalise,CHR(10)) as do_jadisp_notitulojustificativaanalise
			,STRING_AGG(do_jadisp.nocorpojustificativaanalise,CHR(10)) as do_jadisp_nocorpojustificativaanalise
			,STRING_AGG(do_jadisp.norodapejustificativaanalise,CHR(10)) as do_jadisp_norodapejustificativaanalise
			,STRING_AGG(do_jadisp.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as do_jadisp_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(do_tjadisp.notipojustificativaanalise,CHR(10)) as do_tjadisp_notipojustificativaanalise
			,SUM(coalesce(do_aomdispj.idanaliseobjetomarcodispendiojustificativa) ) as do_aomdispj_idanaliseobjetomarcodispendiojustificativa
		from tbanaliseobjetomarcodispendiojustificativa do_aomdispj
		left join tbjustificativaanalise do_jadisp on do_jadisp.idjustificativaanalise = do_aomdispj.idjustificativaanalise
		left join tbtipojustificativaanalise do_tjadisp on do_tjadisp.cdtipojustificativaanalise = do_jadisp.cdtipojustificativaanalise
		group by do_aomdispj.idanaliseobjetomarcodispendio ) do_a_disp on do_a_disp.idanaliseobjetomarcodispendio = do_aomdisp.idanaliseobjetomarcodispendio 
--
-- PARECER
--
left join tbmarcoanalise p_ma on p_ma.idmarcoanalise = dem.idmarcoanaliseparecer
left join tbanaliseobjetomarcoprojeto p_aomproj on p_aomproj.idmarcoanalise = p_ma.idmarcoanalise and p_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise p_taaproj on p_taaproj.idtipoavaliacaoanalise = p_aomproj.idtipoavaliacaoanalise
left join tbanaliseobjetomarcodispendio p_aomdisp on p_aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio and p_aomdisp.idmarcoanalise = p_ma.idmarcoanalise 
left join tbtipoavaliacaoanalise p_taadisp on p_taadisp.idtipoavaliacaoanalise = p_aomdisp.idtipoavaliacaoanalise
left join tbtipomarcoanalise p_tma on p_tma.cdtipomarcoanalise  = p_ma.cdtipomarcoanalise 
--
left join ( 
    select idprenchimentosituacaoanalise
    , idmarcoanalise
    , apd.iddadoanaliseprojetodispendio
    , sum(apd.vltotal) as valordispendio
    , sum(amd.vlindicadoanalise::decimal) as valoranalisedispendio
    , sum(amd.vlglosa::decimal) as valorglosadispendio
    , count(1) as totaldispendio
    from tbdadoanaliseprojeto apj
    join tbdadoanaliseprojetodispendio apd on apd.iddadoanaliseprojeto = apj.iddadoanaliseprojeto
    left join tbanaliseobjetomarcodispendio amd 
        on amd.iddadoanaliseprojetodispendio = apd.iddadoanaliseprojetodispendio
    group by idprenchimentosituacaoanalise, idmarcoanalise, apd.iddadoanaliseprojetodispendio
) p_dispendio
on p_dispendio.idprenchimentosituacaoanalise = p_ma.idprenchimentosituacaoanalise
and p_dispendio.idmarcoanalise = p_ma.idmarcoanalise
and p_dispendio.iddadoanaliseprojetodispendio = p_aomdisp.iddadoanaliseprojetodispendio
--
left join( 
	select 	p_aomdispj.idanaliseobjetomarcodispendio
			,STRING_AGG(p_jadisp.nojustificativaanalise,CHR(10)) as p_jadisp_nojustificativaanalise
			,STRING_AGG(p_jadisp.notitulojustificativaanalise,CHR(10)) as p_jadisp_notitulojustificativaanalise
			,STRING_AGG(p_jadisp.nocorpojustificativaanalise,CHR(10)) as p_jadisp_nocorpojustificativaanalise
			,STRING_AGG(p_jadisp.norodapejustificativaanalise,CHR(10)) as p_jadisp_norodapejustificativaanalise
			,STRING_AGG(p_jadisp.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as p_jadisp_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(p_tjadisp.notipojustificativaanalise,CHR(10)) as p_tjadisp_notipojustificativaanalise
			,SUM(coalesce(p_aomdispj.idanaliseobjetomarcodispendiojustificativa) ) as p_aomdispj_idanaliseobjetomarcodispendiojustificativa
		from tbanaliseobjetomarcodispendiojustificativa p_aomdispj
		left join tbjustificativaanalise p_jadisp on p_jadisp.idjustificativaanalise = p_aomdispj.idjustificativaanalise
		left join tbtipojustificativaanalise p_tjadisp on p_tjadisp.cdtipojustificativaanalise = p_jadisp.cdtipojustificativaanalise
		group by p_aomdispj.idanaliseobjetomarcodispendio ) p_a_disp on p_a_disp.idanaliseobjetomarcodispendio = p_aomdisp.idanaliseobjetomarcodispendio 
--
-- DO_CONTESTACAO
--
left join tbmarcoanalise do_c_ma on do_c_ma.idmarcoanalise = dem.idmarcoanalisedocontestacao 
left join tbanaliseobjetomarcoprojeto do_c_aomproj on do_c_aomproj.idmarcoanalise = do_c_ma.idmarcoanalise and do_c_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise do_c_taaproj on do_c_taaproj.idtipoavaliacaoanalise = do_c_aomproj.idtipoavaliacaoanalise
left join tbanaliseobjetomarcodispendio do_c_aomdisp on do_c_aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio and do_c_aomdisp.idmarcoanalise = do_c_ma.idmarcoanalise
left join tbtipoavaliacaoanalise do_c_taadisp on do_c_taadisp.idtipoavaliacaoanalise = do_c_aomdisp.idtipoavaliacaoanalise
left join tbtipomarcoanalise do_c_tma on do_c_tma.cdtipomarcoanalise  = do_c_ma.cdtipomarcoanalise 
left join tbanaliseobjetomarcodispendiocontestacao do_c_aomdispc on do_c_aomdispc.idanaliseobjetomarcodispendiocontestacao = do_c_aomdisp.idanaliseobjetomarcodispendio
--
left join ( 
    select idprenchimentosituacaoanalise
    , idmarcoanalise
    , apd.iddadoanaliseprojetodispendio
    , sum(apd.vltotal) as valordispendio
    , sum(amd.vlindicadoanalise::decimal) as valoranalisedispendio
    , sum(amd.vlglosa::decimal) as valorglosadispendio
    , count(1) as totaldispendio
    from tbdadoanaliseprojeto apj
    join tbdadoanaliseprojetodispendio apd on apd.iddadoanaliseprojeto = apj.iddadoanaliseprojeto
    left join tbanaliseobjetomarcodispendio amd 
        on amd.iddadoanaliseprojetodispendio = apd.iddadoanaliseprojetodispendio
    group by idprenchimentosituacaoanalise, idmarcoanalise, apd.iddadoanaliseprojetodispendio
) do_c_dispendio
on do_c_dispendio.idprenchimentosituacaoanalise = do_c_ma.idprenchimentosituacaoanalise
and do_c_dispendio.idmarcoanalise = do_c_ma.idmarcoanalise
and do_c_dispendio.iddadoanaliseprojetodispendio = do_c_aomdisp.iddadoanaliseprojetodispendio
--
left join( 
	select 	do_c_aomdispj.idanaliseobjetomarcodispendio
			,STRING_AGG(do_c_jadisp.nojustificativaanalise,CHR(10)) as do_c_jadisp_nojustificativaanalise
			,STRING_AGG(do_c_jadisp.notitulojustificativaanalise,CHR(10)) as do_c_jadisp_notitulojustificativaanalise
			,STRING_AGG(do_c_jadisp.nocorpojustificativaanalise,CHR(10)) as do_c_jadisp_nocorpojustificativaanalise
			,STRING_AGG(do_c_jadisp.norodapejustificativaanalise,CHR(10)) as do_c_jadisp_norodapejustificativaanalise
			,STRING_AGG(do_c_jadisp.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as do_c_jadisp_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(do_c_tjadisp.notipojustificativaanalise,CHR(10)) as do_c_tjadisp_notipojustificativaanalise
			,SUM(coalesce(do_c_aomdispj.idanaliseobjetomarcodispendiojustificativa) ) as do_c_aomdispj_idanaliseobjetomarcodispendiojustificativa
		from tbanaliseobjetomarcodispendiojustificativa do_c_aomdispj
		left join tbjustificativaanalise do_c_jadisp on do_c_jadisp.idjustificativaanalise = do_c_aomdispj.idjustificativaanalise
		left join tbtipojustificativaanalise do_c_tjadisp on do_c_tjadisp.cdtipojustificativaanalise = do_c_jadisp.cdtipojustificativaanalise
		group by do_c_aomdispj.idanaliseobjetomarcodispendio ) do_c_a_disp on do_c_a_disp.idanaliseobjetomarcodispendio = do_c_aomdisp.idanaliseobjetomarcodispendio 
--
-- PARECER_CONTESTACAO
--
left join tbmarcoanalise p_c_ma on p_c_ma.idmarcoanalise = dem.idmarcoanaliseparecercontestacao 
left join tbanaliseobjetomarcoprojeto p_c_aomproj on p_c_aomproj.idmarcoanalise = p_c_ma.idmarcoanalise and p_c_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise p_c_taaproj on p_c_taaproj.idtipoavaliacaoanalise = p_c_aomproj.idtipoavaliacaoanalise
left join tbanaliseobjetomarcodispendio p_c_aomdisp on p_c_aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio and p_c_aomdisp.idmarcoanalise = p_c_ma.idmarcoanalise 
left join tbtipoavaliacaoanalise p_c_taadisp on p_c_taadisp.idtipoavaliacaoanalise = p_c_aomdisp.idtipoavaliacaoanalise
left join tbtipomarcoanalise p_c_tma on p_c_tma.cdtipomarcoanalise  = p_c_ma.cdtipomarcoanalise 
left join tbanaliseobjetomarcodispendiocontestacao p_c_aomdispc on p_c_aomdispc.idanaliseobjetomarcodispendiocontestacao = p_c_aomdisp.idanaliseobjetomarcodispendio
--
left join ( 
    select idprenchimentosituacaoanalise
    , idmarcoanalise
    , apd.iddadoanaliseprojetodispendio
    , sum(apd.vltotal) as valordispendio
    , sum(amd.vlindicadoanalise::decimal) as valoranalisedispendio
    , sum(amd.vlglosa::decimal) as valorglosadispendio
    , count(1) as totaldispendio
    from tbdadoanaliseprojeto apj
    join tbdadoanaliseprojetodispendio apd on apd.iddadoanaliseprojeto = apj.iddadoanaliseprojeto
    left join tbanaliseobjetomarcodispendio amd 
        on amd.iddadoanaliseprojetodispendio = apd.iddadoanaliseprojetodispendio
    group by idprenchimentosituacaoanalise, idmarcoanalise, apd.iddadoanaliseprojetodispendio
) p_c_dispendio
on p_c_dispendio.idprenchimentosituacaoanalise = p_c_ma.idprenchimentosituacaoanalise
and p_c_dispendio.idmarcoanalise = p_c_ma.idmarcoanalise
and p_c_dispendio.iddadoanaliseprojetodispendio = p_c_aomdisp.iddadoanaliseprojetodispendio
--
left join( 
	select 	p_c_aomdispj.idanaliseobjetomarcodispendio
			,STRING_AGG(p_c_jadisp.nojustificativaanalise,CHR(10)) as p_c_jadisp_nojustificativaanalise
			,STRING_AGG(p_c_jadisp.notitulojustificativaanalise,CHR(10)) as p_c_jadisp_notitulojustificativaanalise
			,STRING_AGG(p_c_jadisp.nocorpojustificativaanalise,CHR(10)) as p_c_jadisp_nocorpojustificativaanalise
			,STRING_AGG(p_c_jadisp.norodapejustificativaanalise,CHR(10)) as p_c_jadisp_norodapejustificativaanalise
			,STRING_AGG(p_c_jadisp.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as p_c_jadisp_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(p_c_tjadisp.notipojustificativaanalise,CHR(10)) as p_c_tjadisp_notipojustificativaanalise
			,SUM(coalesce(p_c_aomdispj.idanaliseobjetomarcodispendiojustificativa) ) as p_c_aomdispj_idanaliseobjetomarcodispendiojustificativa
		from tbanaliseobjetomarcodispendiojustificativa p_c_aomdispj
		left join tbjustificativaanalise p_c_jadisp on p_c_jadisp.idjustificativaanalise = p_c_aomdispj.idjustificativaanalise
		left join tbtipojustificativaanalise p_c_tjadisp on p_c_tjadisp.cdtipojustificativaanalise = p_c_jadisp.cdtipojustificativaanalise
		group by p_c_aomdispj.idanaliseobjetomarcodispendio ) p_c_a_disp on p_c_a_disp.idanaliseobjetomarcodispendio = p_c_aomdisp.idanaliseobjetomarcodispendio
--
-- RECURSO_ADMINISTRATIVO
--
left join tbmarcoanalise ra_ma on ra_ma.idmarcoanalise = dem.idmarcoanaliseparecerrecurso
left join tbanaliseobjetomarcoprojeto ra_aomproj on ra_aomproj.idmarcoanalise = ra_ma.idmarcoanalise and ra_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise ra_taaproj on ra_taaproj.idtipoavaliacaoanalise = ra_aomproj.idtipoavaliacaoanalise
left join tbanaliseobjetomarcodispendio ra_aomdisp on ra_aomdisp.iddadoanaliseprojetodispendio = dapdisp.iddadoanaliseprojetodispendio and ra_aomdisp.idmarcoanalise = ra_ma.idmarcoanalise 
left join tbtipoavaliacaoanalise ra_taadisp on ra_taadisp.idtipoavaliacaoanalise = ra_aomdisp.idtipoavaliacaoanalise
left join tbtipomarcoanalise ra_tma on ra_tma.cdtipomarcoanalise  = ra_ma.cdtipomarcoanalise
left join tbanaliseobjetomarcodispendiocontestacao ra_aomdispc on ra_aomdispc.idanaliseobjetomarcodispendiocontestacao = ra_aomdisp.idanaliseobjetomarcodispendio
--
left join ( 
    select idprenchimentosituacaoanalise
    , idmarcoanalise
    , apd.iddadoanaliseprojetodispendio
    , sum(apd.vltotal) as valordispendio
    , sum(amd.vlindicadoanalise::decimal) as valoranalisedispendio
    , sum(amd.vlglosa::decimal) as valorglosadispendio
    , count(1) as totaldispendio
    from tbdadoanaliseprojeto apj
    join tbdadoanaliseprojetodispendio apd on apd.iddadoanaliseprojeto = apj.iddadoanaliseprojeto
    left join tbanaliseobjetomarcodispendio amd 
        on amd.iddadoanaliseprojetodispendio = apd.iddadoanaliseprojetodispendio
    group by idprenchimentosituacaoanalise, idmarcoanalise, apd.iddadoanaliseprojetodispendio
) ra_dispendio
on ra_dispendio.idprenchimentosituacaoanalise = ra_ma.idprenchimentosituacaoanalise
and ra_dispendio.idmarcoanalise = ra_ma.idmarcoanalise
and ra_dispendio.iddadoanaliseprojetodispendio = ra_aomdisp.iddadoanaliseprojetodispendio
--
left join( 
	select 	ra_aomdispj.idanaliseobjetomarcodispendio
			,STRING_AGG(ra_jadisp.nojustificativaanalise,CHR(10)) as ra_jadisp_nojustificativaanalise
			,STRING_AGG(ra_jadisp.notitulojustificativaanalise,CHR(10)) as ra_jadisp_notitulojustificativaanalise
			,STRING_AGG(ra_jadisp.nocorpojustificativaanalise,CHR(10)) as ra_jadisp_nocorpojustificativaanalise
			,STRING_AGG(ra_jadisp.norodapejustificativaanalise,CHR(10)) as ra_jadisp_norodapejustificativaanalise
			,STRING_AGG(ra_jadisp.notitulojustificativagrupoobjetoanaliseindividual,CHR(10)) as ra_jadisp_notitulojustificativagrupoobjetoanaliseindividual
			,STRING_AGG(ra_tjadisp.notipojustificativaanalise,CHR(10)) as ra_tjadisp_notipojustificativaanalise
			,SUM(coalesce(ra_aomdispj.idanaliseobjetomarcodispendiojustificativa) ) as ra_aomdispj_idanaliseobjetomarcodispendiojustificativa
		from tbanaliseobjetomarcodispendiojustificativa ra_aomdispj
		left join tbjustificativaanalise ra_jadisp on ra_jadisp.idjustificativaanalise = ra_aomdispj.idjustificativaanalise
		left join tbtipojustificativaanalise ra_tjadisp on ra_tjadisp.cdtipojustificativaanalise = ra_jadisp.cdtipojustificativaanalise
		group by ra_aomdispj.idanaliseobjetomarcodispendio ) ra_a_disp on ra_a_disp.idanaliseobjetomarcodispendio = ra_aomdisp.idanaliseobjetomarcodispendio
where dem.idprenchimentosituacaoanalise in 
	(select distinct t3.idprenchimentosituacaoanalise
from tbanaliseobjetomarcodispendiocontestacao t 
left join tbmarcoanalisedadoconsolidado t2 on t2.idmarcoanalise = t.idmarcoanalise
left join tbmarcoanalise t3 on t3.idmarcoanalise = t.idmarcoanalise
left join vwprojetosporpreenchimento v1 on v1.idprenchimentosituacaoanalise = t3.idprenchimentosituacaoanalise	
where t.dsjustificativaanalisecontestacao is not null
and t.dsjustificativacontestacao is not null
and t.dsjustificativaparecer is not null
and t.dsjustificativarecursoadministrativo is not null
and v1.nprojs = 10
and t2.nranobase = 2019)
order by dem.idprenchimentosituacaoanalise, daproj.nritem 
