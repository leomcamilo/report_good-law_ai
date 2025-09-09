--select A.do_resultado_analise, A.p_resultado_analise
--, sum(A.countsodoutorproj) as projsodoutor, sum(A.countdoutoremestreproj) as projdoutoresemestres, sum(A.countsomestreproj) as projsomestre, sum(A.countdoutorproj) as projdoutor, sum(A.countmestreproj) as projmestre,sum(A.countdoutoroumestreproj) as projdoutoroumestre 
--, sum(A.sumsodoutorproj) as quantsodoutor, sum(A.sumdoutoremestreproj) as quantdoutoresemestres, sum(A.sumsomestreproj) as quantsomestre, sum(A.sumdoutorproj) as quantdoutor, sum(A.summestreproj) as quantmestre,sum(A.sumdoutoroumestreproj) as quantdoutoroumestre 
--from (
--select A.do_resultado_analise, A.p_resultado_analise, count(*) from (

select lst.idprenchimentosituacaoanalise as id_empresa_ano
, lst.nranobase as ano_referencia
, do_setor.nosetor as setor
, lst.nrcnpj
, lst.norazaosocial, daproj.iddadoanaliseprojeto
, do_taaproj.notipoavaliacaoanalise as do_resultado_analise
, p_taaproj.notipoavaliacaoanalise as p_resultado_analise
, dapree.vlreceitaliquida 
, total.valortotalproj
, case when doutorquantparcial.quantdoutorproj > 0 and mestrequantparcial.quantmestreproj is null then 1 else 0 end as count_so_doutorproj
, case when doutorquantparcial.quantdoutorproj > 0 and mestrequantparcial.quantmestreproj > 0 then 1 else 0 end as count_doutor_e_mestreproj
, case when doutorquantparcial.quantdoutorproj is null and mestrequantparcial.quantmestreproj > 0 then 1 else 0 end as count_so_mestreproj
, case when doutorquantparcial.quantdoutorproj > 0 then 1 else 0 end as count_doutorproj
, case when mestrequantparcial.quantmestreproj > 0 then 1 else 0 end as count_mestreproj
, case when doutoroumestrequantparcial.quantdoutoroumestreproj > 0 then 1 else 0 end as count_doutor_ou_mestreproj
, case when doutorquantparcial.quantdoutorproj > 0 and mestrequantparcial.quantmestreproj is null then doutorquantparcial.quantdoutorproj else 0 end as quant_so_doutorproj
, case when doutorquantparcial.quantdoutorproj > 0 and mestrequantparcial.quantmestreproj > 0 then doutorquantparcial.quantdoutorproj + mestrequantparcial.quantmestreproj else 0 end as quant_doutor_e_mestreproj
, case when doutorquantparcial.quantdoutorproj is null and mestrequantparcial.quantmestreproj > 0 then mestrequantparcial.quantmestreproj else 0 end as quant_so_mestreproj
, doutorquantparcial.quantdoutorproj  as quant_doutorproj
, mestrequantparcial.quantmestreproj  as quant_mestreproj
, doutoroumestrequantparcial.quantdoutoroumestreproj as quant_doutor_ou_mestreproj
, ict.valorictproj 
, pessoalempresa.quantpessoalempresa
, coalesce(pessoalempresa.quantpessoalempresa/nullif(dapree.nrtotalfuncionario ,0),0) as percpessoalalocadoempresa
, case 	when dapree.vlreceitaliquida <= 360000 then 'Micro'
		when dapree.vlreceitaliquida <= 4800000 then 'Peq'
		when dapree.vlreceitaliquida <= 90000000 then 'Med_1'
		when dapree.vlreceitaliquida <= 300000000 then 'Med_2'
		else 'Grd'
 		end as porte
--select do_taaproj.notipoavaliacaoanalise, p_taaproj.notipoavaliacaoanalise, 
--
--select count(*)
from tbdadoanaliseprojeto daproj
left join tbdadoempresamarco dem on dem.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise 
left join tbdadoanalisepreenchimento dapree on dapree.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
left join listaempresasporanobasesituacaoanalise lst on lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
--
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valortotalproj 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		group by dapdisp.iddadoanaliseprojeto ) total on total.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valordoutorproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.tptitulacao = 'Doutor'
		group by dapdisp.iddadoanaliseprojeto ) doutor on doutor.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select doutorparcial.iddadoanaliseprojeto, sum(doutorparcial.quantdoutorparcial )	quantdoutorproj
		from (
		select daproj.iddadoanaliseprojeto, dapdisp.nrcnpjcpf, coalesce(doutorproj.valordoutorproj /nullif( doutorempresa.valordoutortotal,0),0) as quantdoutorparcial 
		from tbdadoanaliseprojeto daproj
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto
		left join (
			select dapdisp.iddadoanaliseprojeto, dapdisp.nrcnpjcpf, sum(dapdisp.vltotal ) valordoutorproj
			from tbdadoanaliseprojeto daproj
			left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto
			where dapdisp.tptitulacao = 'Doutor'
			group by dapdisp.iddadoanaliseprojeto, dapdisp.nrcnpjcpf ) doutorProj on doutorproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto and DoutorProj.nrcnpjcpf = dapdisp.nrcnpjcpf 
		left join (
			select daproj.idprenchimentosituacaoanalise , dapdisp.nrcnpjcpf , sum(dapdisp.vltotal) as valordoutortotal
			from tbdadoanaliseprojeto daproj 
			left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
			left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
			where dapdisp.tptitulacao = 'Doutor'
			group by daproj.idprenchimentosituacaoanalise, dapdisp.nrcnpjcpf ) doutorempresa on doutorempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise and doutorempresa.nrcnpjcpf = dapdisp.nrcnpjcpf
		where dapdisp.tptitulacao = 'Doutor' ) doutorparcial
		group by doutorparcial.iddadoanaliseprojeto ) doutorquantparcial on doutorquantparcial.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valormestreproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.tptitulacao ='Mestre'
		group by dapdisp.iddadoanaliseprojeto ) mestre on mestre.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select mestreparcial.iddadoanaliseprojeto, sum(mestreparcial.quantmestreparcial )	as quantmestreproj
		from (
		select daproj.iddadoanaliseprojeto, dapdisp.nrcnpjcpf, coalesce(mestreproj.valormestreproj / nullif(mestreempresa.valormestretotal,0),0) as quantmestreparcial 
		from tbdadoanaliseprojeto daproj
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto
		left join (
			select dapdisp.iddadoanaliseprojeto, dapdisp.nrcnpjcpf, sum(dapdisp.vltotal ) valormestreproj
			from tbdadoanaliseprojeto daproj
			left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto
			where dapdisp.tptitulacao ='Mestre'
			group by dapdisp.iddadoanaliseprojeto, dapdisp.nrcnpjcpf ) mestreProj on mestreproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto and mestreProj.nrcnpjcpf = dapdisp.nrcnpjcpf 
		left join (
			select daproj.idprenchimentosituacaoanalise , dapdisp.nrcnpjcpf , sum(dapdisp.vltotal) as valormestretotal
			from tbdadoanaliseprojeto daproj 
			left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
			left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
			where dapdisp.tptitulacao = 'Mestre'
			group by daproj.idprenchimentosituacaoanalise, dapdisp.nrcnpjcpf ) mestreempresa on mestreempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise and mestreempresa.nrcnpjcpf = dapdisp.nrcnpjcpf
		where dapdisp.tptitulacao = 'Mestre' ) mestreparcial
		group by mestreparcial.iddadoanaliseprojeto ) mestrequantparcial on mestrequantparcial.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valordoutoroumestreproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.tptitulacao in ('Doutor','Mestre')
		group by dapdisp.iddadoanaliseprojeto ) doutoroumestre on doutoroumestre.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select doutoroumestreparcial.iddadoanaliseprojeto, sum(doutoroumestreparcial.quantdoutoroumestreparcial )	as quantdoutoroumestreproj
		from (
		select daproj.iddadoanaliseprojeto, dapdisp.nrcnpjcpf, coalesce(doutoroumestreproj.valordoutoroumestreproj / nullif(doutoroumestreempresa.valordoutoroumestretotal,0),0) as quantdoutoroumestreparcial 
		from tbdadoanaliseprojeto daproj
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto
		left join (
			select dapdisp.iddadoanaliseprojeto, dapdisp.nrcnpjcpf, sum(dapdisp.vltotal ) valordoutoroumestreproj
			from tbdadoanaliseprojeto daproj
			left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto
			where dapdisp.tptitulacao in ('Doutor','Mestre')
			group by dapdisp.iddadoanaliseprojeto, dapdisp.nrcnpjcpf ) doutoroumestreProj on doutoroumestreproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto and doutoroumestreProj.nrcnpjcpf = dapdisp.nrcnpjcpf 
		left join (
			select daproj.idprenchimentosituacaoanalise , dapdisp.nrcnpjcpf , sum(dapdisp.vltotal) as valordoutoroumestretotal
			from tbdadoanaliseprojeto daproj 
			left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
			left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
			where dapdisp.tptitulacao in ('Doutor', 'Mestre')
			group by daproj.idprenchimentosituacaoanalise, dapdisp.nrcnpjcpf ) doutoroumestreempresa on doutoroumestreempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise and doutoroumestreempresa.nrcnpjcpf = dapdisp.nrcnpjcpf
		where dapdisp.tptitulacao in ('Doutor', 'Mestre') ) doutoroumestreparcial
		group by doutoroumestreparcial.iddadoanaliseprojeto ) doutoroumestrequantparcial on doutoroumestrequantparcial.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select dapdisp.iddadoanaliseprojeto, sum(dapdisp.vltotal ) as valorictproj
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.cddadoanaliseprojetotipodispendio in (1, 2 )
		group by dapdisp.iddadoanaliseprojeto ) ict on ict.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join (
		select daproj.idprenchimentosituacaoanalise , count(distinct dapdisp.nrcnpjcpf  ) as quantpessoalempresa 
		from tbdadoanaliseprojeto daproj 
		left join tbdadoanaliseprojetodispendio dapdisp on daproj.iddadoanaliseprojeto = dapdisp.iddadoanaliseprojeto 
		left join tbdadoanaliseprojetotipodispendio daptdisp on daptdisp.cddadoanaliseprojetotipodispendio = dapdisp.cddadoanaliseprojetotipodispendio
		where dapdisp.cddadoanaliseprojetotipodispendio = 9 
		group by daproj.idprenchimentosituacaoanalise  ) pessoalempresa on pessoalempresa.idprenchimentosituacaoanalise  = daproj.idprenchimentosituacaoanalise 
--ANALISE DO
left join tbmarcoanalise do_ma on do_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanalisedo = do_ma.idmarcoanalise
left join tbanaliseat do_aat on do_aat.idmarcoanalise = do_ma.idmarcoanalise and do_aat.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbsituacaoanaliseat do_saat on do_saat.idanaliseat = do_aat.idanaliseat and do_saat.icativo 
left join tbsetor do_setor on do_setor.idsetor = do_saat.idsetor
left join tbanaliseobjetomarcoprojeto do_aomproj on do_aomproj.idmarcoanalise = do_ma.idmarcoanalise and do_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto
left join tbtipoavaliacaoanalise do_taaproj on do_taaproj.idtipoavaliacaoanalise = do_aomproj.idtipoavaliacaoanalise
-- ANALISE PARECER
left join tbmarcoanalise p_ma on p_ma.idprenchimentosituacaoanalise = daproj.idprenchimentosituacaoanalise and dem.idmarcoanaliseparecer = p_ma.idmarcoanalise
left join tbanaliseobjetomarcoprojeto p_aomproj on p_aomproj.idmarcoanalise = p_ma.idmarcoanalise and p_aomproj.iddadoanaliseprojeto = daproj.iddadoanaliseprojeto 
left join tbtipoavaliacaoanalise p_taaproj on p_taaproj.idtipoavaliacaoanalise = p_aomproj.idtipoavaliacaoanalise;

--)A
--group by A.do_resultado_analise, A.p_resultado_analise 
