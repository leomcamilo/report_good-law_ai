select 
  lst.nranobase as lst_nranobase
, lst.nrcnpj as lst_nrcnpj
, lst.norazaosocial as lst_norazaosocial
, lst.idprenchimentosituacaoanalise as lst_idprenchimentosituacaoanalise
, lst.noatividadeeconomica as lst_noatividadeeconomica
, lst.cdatividadeeconomicaibge as lst_cdatividadeeconomicaibge
, lst.notipoportepessoajuridica as lst_notipoportepessoajuridica
, dem.idprenchimentosituacaoanalise as dem_idprenchimentosituacaoanalise
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
, dapree.idprenchimentosituacaoanalise as dapree_idprenchimentosituacaoanalise
, dapree.tporganismo as dapree_tporganismo
, dapree.tpsituacaoempresa as dapree_tpsituacaoempresa
, dapree.icbeneficiofiscal as dapree_icbeneficiofiscal
, dapree.tporigemcapital as dapree_tporigemcapital
, dapree.tprelacaogrupo as dapree_tprelacaogrupo
, dapree.vlreceitaliquida as dapree_vlreceitaliquida
, dapree.nrtotalfuncionario as dapree_nrtotalfuncionario
, dapree.icprejuizofiscal as dapree_icprejuizofiscal
, dapree.tpapuracaoirpjcsll as dapree_tpapuracaoirpjcsll
, dapree.dsmotivoususfruir as dapree_dsmotivoususfruir
, dapree.icpossuipatenteregistro as dapree_icpossuipatenteregistro
, dapree.pcrecursoproprio as dapree_pcrecursoproprio
, dapree.iccontratadodedicacaoexclusivaanobase as dapree_iccontratadodedicacaoexclusivaanobase
, dapree.nrmediopesquisadordedicacaoexclusiva as dapree_nrmediopesquisadordedicacaoexclusiva
, dapree.noarquivomemoriacalculo as dapree_noarquivomemoriacalculo
, dapree.dsreferenciaarquivo as dapree_dsreferenciaarquivo
, dapree.icaumentopesquisadoranoanterior as dapree_icaumentopesquisadoranoanterior
, dapree.nrmediopesquisadordedicacaoexclusivaanoanterior as dapree_nrmediopesquisadordedicacaoexclusivaanoanterior
, dapree.noarquivomemoriacalculoanoanterior as dapree_noarquivomemoriacalculoanoanterior
, dapree.dsreferenciaarquivoanoanterior as dapree_dsreferenciaarquivoanoanterior
, dapree.icpossuiprogramarh as dapree_icpossuiprogramarh
, dapree.dsprogramaformacao as dapree_dsprogramaformacao
, dapree.vlincentivodeducaolucroliquido as dapree_vlincentivodeducaolucroliquido
, dapree.vldadeducao60 as dapree_vldadeducao60
, dapree.vldaincremento20 as dapree_vldaincremento20
, dapree.vldaincremento10 as dapree_vldaincremento10
, dapree.vldapatente20 as dapree_vldapatente20
, dapree.vldaict as dapree_vldaict
, dapree.vlreducaoipinacional as dapree_vlreducaoipinacional
, dapree.vlreducaoipiimportado as dapree_vlreducaoipiimportado
, dapree.vlincentivoreducaoaliquotair as dapree_vlincentivoreducaoaliquotair
, dapree.vldepreciacaointegral as dapree_vldepreciacaointegral
, dapree.vldepreciacaodeducaosaldo as dapree_vldepreciacaodeducaosaldo
, dapree.vlamortizacaobens as dapree_vlamortizacaobens
, dapree.vlamortizacaosaldobens as dapree_vlamortizacaosaldobens
, dapree.dsoutrasinformacoes as dapree_dsoutrasinformacoes
, dapree.icdispendioict as dapree_icdispendioict
, dapree.icprejuizofiscalalterado as dapree_icprejuizofiscalalterado
, dapree.icaumentomediopesquisadordedicaoexclusivaalterado as dapree_icaumentomediopesquisadordedicaoexclusivaalterado
, dapree.idunicopessoafezalteracao as dapree_idunicopessoafezalteracao
, dapree.idmomentopessoafezalteracao as dapree_idmomentopessoafezalteracao
, dapree.dtmodificacaoregistro as dapree_dtmodificacaoregistro
, dapree.icempresapodealterartipolucroreal as dapree_icempresapodealterartipolucroreal
, dapree.tpapuracaoirpjcslloriginal as dapree_tpapuracaoirpjcslloriginal
, daffin.iddadoanalisefontefinanciamento as daffin_iddadoanalisefontefinanciamento
, daffin.idprenchimentosituacaoanalise as daffin_idprenchimentosituacaoanalise
, daffin.idagrupadorresposta as daffin_idagrupadorresposta
, daffin.nritem as daffin_nritem
, daffin.pcfinanciamento as daffin_pcfinanciamento
, daffin.dsfontefinanciamento as daffin_dsfontefinanciamento
, psa.idprenchimentosituacaoanalise as psa_idprenchimentosituacaoanalise
, psa.idpreenchimentoformulario as psa_idpreenchimentoformulario
, psa.idtiposituacaoanalise as psa_idtiposituacaoanalise
, psa.dscaminhoarquivoanalise as psa_dscaminhoarquivoanalise
, psa.icativo as psa_icativo
, psa.idpreenchimentoformpd as psa_idpreenchimentoformpd
, psa.idempresaformpd as psa_idempresaformpd
, psa.nranobase as psa_nranobase
, psa.dtpreenchimento as psa_dtpreenchimento
, do_ma.idmarcoanalise as do_ma_idmarcoanalise
, do_ma.idprenchimentosituacaoanalise as do_ma_idprenchimentosituacaoanalise
, do_ma.cdtipomarcoanalise as do_ma_cdtipomarcoanalise
, do_ma.idhistoricosituacaoanalise as do_ma_idhistoricosituacaoanalise
, do_ma.nrmarcoanalise as do_ma_nrmarcoanalise
, do_ma.dsobservacao as do_ma_dsobservacao
, do_ma.dscaminhoarquivoanalise as do_ma_dscaminhoarquivoanalise
, do_ma.cdresultadomarcoanalise as do_ma_cdresultadomarcoanalise
, do_ma.idmarcoanalisebase as do_ma_idmarcoanalisebase
, do_ma.cdsituacaoprocessamentoassinatura as do_ma_cdsituacaoprocessamentoassinatura
, do_rma.cdresultadomarcoanalise as do_rma_cdresultadomarcoanalise
, do_rma.noresultadomarcoanalise as do_rma_noresultadomarcoanalise
, do_tma.cdtipomarcoanalise as do_tma_cdtipomarcoanalise
, do_tma.notipomarcoanalise as do_tma_notipomarcoanalise
, do_hsa.idhistoricosituacaoanalise as do_hsa_idhistoricosituacaoanalise
, do_hsa.idprenchimentosituacaoanalise as do_hsa_idprenchimentosituacaoanalise
, do_hsa.cdtiposituacaomarco as do_hsa_cdtiposituacaomarco
, do_hsa.dtiniciosituacaoanalise as do_hsa_dtiniciosituacaoanalise
, do_hsa.dtfimsituacao as do_hsa_dtfimsituacao
, do_hsa.icativo as do_hsa_icativo
, do_hsa.idtask as do_hsa_idtask
, do_hsa.idmomentopessoa as do_hsa_idmomentopessoa
, do_hsa.idunicopessoa as do_hsa_idunicopessoa
, do_hsa.idmarcoanalise as do_hsa_idmarcoanalise
, do_tsm.cdtiposituacaomarco as do_tsm_cdtiposituacaomarco
, do_tsm.notiposituacaomarco as do_tsm_notiposituacaomarco
, do_tsm.dstiposituacaomarco as do_tsm_dstiposituacaomarco
, do_madc.idmarcoanalise as do_madc_idmarcoanalise
, do_madc.nrcnpj as do_madc_nrcnpj
, do_madc.norazaosocial as do_madc_norazaosocial
, do_madc.dsconclusao as do_madc_dsconclusao
, do_madc.dsobservacaodo as do_madc_dsobservacaodo
, do_madc.dsobservacaobens as do_madc_dsobservacaobens
, do_madc.vltotaldispendio as do_madc_vltotaldispendio
, do_madc.vlaprovado as do_madc_vlaprovado
, do_madc.vlglosa as do_madc_vlglosa
, do_madc.nrtotalprojeto as do_madc_nrtotalprojeto
, do_madc.nrtotalaprovado as do_madc_nrtotalaprovado
, do_madc.nrtotalreprovado as do_madc_nrtotalreprovado
, do_madc.nranobase as do_madc_nranobase
, do_madc.dsobservacaoaocoordenador as do_madc_dsobservacaoaocoordenador
, do_madc.dsinformacaocomplementar as do_madc_dsinformacaocomplementar
, do_madc.dsconsideracaorecomendacao as do_madc_dsconsideracaorecomendacao
, do_madc.dssolicitaalteracao as do_madc_dssolicitaalteracao
, do_madc.dsobservacoesfinaiscontestacao as do_madc_dsobservacoesfinaiscontestacao
, do_madc.dsobservacoesfinaisrecursoadministrativo as do_madc_dsobservacoesfinaisrecursoadministrativo
, do_madc.dsjustificativaincentivosrecursoadm as do_madc_dsjustificativaincentivosrecursoadm
--
,do_a_pree.do_aompree_dsjustificativapadrao
,do_a_pree.do_aompree_vlindicadoanalise
,do_a_pree.do_aompree_vlglosa
,do_a_pree.do_taompree_dstipoanaliseobjetomarcopreenchimento
,do_a_pree.do_taapree_notipoavaliacaoanalise
,do_a_pree.do_japree_nojustificativaanalise
,do_a_pree.do_japree_notitulojustificativaanalise
,do_a_pree.do_japree_nocorpojustificativaanalise
,do_a_pree.do_japree_norodapejustificativaanalise
,do_a_pree.do_japree_notitulojustificativagrupoobjetoanaliseindividual
,do_a_pree.do_tjapree_notipojustificativaanalise
--
, p_ma.idmarcoanalise as p_ma_idmarcoanalise
, p_ma.idprenchimentosituacaoanalise as p_ma_idprenchimentosituacaoanalise
, p_ma.cdtipomarcoanalise as p_ma_cdtipomarcoanalise
, p_ma.idhistoricosituacaoanalise as p_ma_idhistoricosituacaoanalise
, p_ma.nrmarcoanalise as p_ma_nrmarcoanalise
, p_ma.dsobservacao as p_ma_dsobservacao
, p_ma.dscaminhoarquivoanalise as p_ma_dscaminhoarquivoanalise
, p_ma.cdresultadomarcoanalise as p_ma_cdresultadomarcoanalise
, p_ma.idmarcoanalisebase as p_ma_idmarcoanalisebase
, p_ma.cdsituacaoprocessamentoassinatura as p_ma_cdsituacaoprocessamentoassinatura
, p_rma.cdresultadomarcoanalise as p_rma_cdresultadomarcoanalise
, p_rma.noresultadomarcoanalise as p_rma_noresultadomarcoanalise
, p_tma.cdtipomarcoanalise as p_tma_cdtipomarcoanalise
, p_tma.notipomarcoanalise as p_tma_notipomarcoanalise
, p_hsa.idhistoricosituacaoanalise as p_hsa_idhistoricosituacaoanalise
, p_hsa.idprenchimentosituacaoanalise as p_hsa_idprenchimentosituacaoanalise
, p_hsa.cdtiposituacaomarco as p_hsa_cdtiposituacaomarco
, p_hsa.dtiniciosituacaoanalise as p_hsa_dtiniciosituacaoanalise
, p_hsa.dtfimsituacao as p_hsa_dtfimsituacao
, p_hsa.icativo as p_hsa_icativo
, p_hsa.idtask as p_hsa_idtask
, p_hsa.idmomentopessoa as p_hsa_idmomentopessoa
, p_hsa.idunicopessoa as p_hsa_idunicopessoa
, p_hsa.idmarcoanalise as p_hsa_idmarcoanalise
, p_tsm.cdtiposituacaomarco as p_tsm_cdtiposituacaomarco
, p_tsm.notiposituacaomarco as p_tsm_notiposituacaomarco
, p_tsm.dstiposituacaomarco as p_tsm_dstiposituacaomarco
, p_madc.idmarcoanalise as p_madc_idmarcoanalise
, p_madc.nrcnpj as p_madc_nrcnpj
, p_madc.norazaosocial as p_madc_norazaosocial
, p_madc.dsconclusao as p_madc_dsconclusao
, p_madc.dsobservacaodo as p_madc_dsobservacaodo
, p_madc.dsobservacaobens as p_madc_dsobservacaobens
, p_madc.vltotaldispendio as p_madc_vltotaldispendio
, p_madc.vlaprovado as p_madc_vlaprovado
, p_madc.vlglosa as p_madc_vlglosa
, p_madc.nrtotalprojeto as p_madc_nrtotalprojeto
, p_madc.nrtotalaprovado as p_madc_nrtotalaprovado
, p_madc.nrtotalreprovado as p_madc_nrtotalreprovado
, p_madc.nranobase as p_madc_nranobase
, p_madc.dsobservacaoaocoordenador as p_madc_dsobservacaoaocoordenador
, p_madc.dsinformacaocomplementar as p_madc_dsinformacaocomplementar
, p_madc.dsconsideracaorecomendacao as p_madc_dsconsideracaorecomendacao
, p_madc.dssolicitaalteracao as p_madc_dssolicitaalteracao
, p_madc.dsobservacoesfinaiscontestacao as p_madc_dsobservacoesfinaiscontestacao
, p_madc.dsobservacoesfinaisrecursoadministrativo as p_madc_dsobservacoesfinaisrecursoadministrativo
, p_madc.dsjustificativaincentivosrecursoadm as p_madc_dsjustificativaincentivosrecursoadm
--
,p_a_pree.p_aompree_dsjustificativapadrao
,p_a_pree.p_aompree_vlindicadoanalise
,p_a_pree.p_aompree_vlglosa
,p_a_pree.p_taompree_dstipoanaliseobjetomarcopreenchimento
,p_a_pree.p_taapree_notipoavaliacaoanalise
,p_a_pree.p_japree_nojustificativaanalise
,p_a_pree.p_japree_notitulojustificativaanalise
,p_a_pree.p_japree_nocorpojustificativaanalise
,p_a_pree.p_japree_norodapejustificativaanalise
,p_a_pree.p_japree_notitulojustificativagrupoobjetoanaliseindividual
,p_a_pree.p_tjapree_notipojustificativaanalise
--
, do_c_ma.idmarcoanalise as do_c_ma_idmarcoanalise
, do_c_ma.idprenchimentosituacaoanalise as do_c_ma_idprenchimentosituacaoanalise
, do_c_ma.cdtipomarcoanalise as do_c_ma_cdtipomarcoanalise
, do_c_ma.idhistoricosituacaoanalise as do_c_ma_idhistoricosituacaoanalise
, do_c_ma.nrmarcoanalise as do_c_ma_nrmarcoanalise
, do_c_ma.dsobservacao as do_c_ma_dsobservacao
, do_c_ma.dscaminhoarquivoanalise as do_c_ma_dscaminhoarquivoanalise
, do_c_ma.cdresultadomarcoanalise as do_c_ma_cdresultadomarcoanalise
, do_c_ma.idmarcoanalisebase as do_c_ma_idmarcoanalisebase
, do_c_ma.cdsituacaoprocessamentoassinatura as do_c_ma_cdsituacaoprocessamentoassinatura
, do_c_rma.cdresultadomarcoanalise as do_c_rma_cdresultadomarcoanalise
, do_c_rma.noresultadomarcoanalise as do_c_rma_noresultadomarcoanalise
, do_c_tma.cdtipomarcoanalise as do_c_tma_cdtipomarcoanalise
, do_c_tma.notipomarcoanalise as do_c_tma_notipomarcoanalise
, do_c_hsa.idhistoricosituacaoanalise as do_c_hsa_idhistoricosituacaoanalise
, do_c_hsa.idprenchimentosituacaoanalise as do_c_hsa_idprenchimentosituacaoanalise
, do_c_hsa.cdtiposituacaomarco as do_c_hsa_cdtiposituacaomarco
, do_c_hsa.dtiniciosituacaoanalise as do_c_hsa_dtiniciosituacaoanalise
, do_c_hsa.dtfimsituacao as do_c_hsa_dtfimsituacao
, do_c_hsa.icativo as do_c_hsa_icativo
, do_c_hsa.idtask as do_c_hsa_idtask
, do_c_hsa.idmomentopessoa as do_c_hsa_idmomentopessoa
, do_c_hsa.idunicopessoa as do_c_hsa_idunicopessoa
, do_c_hsa.idmarcoanalise as do_c_hsa_idmarcoanalise
, do_c_tsm.cdtiposituacaomarco as do_c_tsm_cdtiposituacaomarco
, do_c_tsm.notiposituacaomarco as do_c_tsm_notiposituacaomarco
, do_c_tsm.dstiposituacaomarco as do_c_tsm_dstiposituacaomarco
, do_c_madc.idmarcoanalise as do_c_madc_idmarcoanalise
, do_c_madc.nrcnpj as do_c_madc_nrcnpj
, do_c_madc.norazaosocial as do_c_madc_norazaosocial
, do_c_madc.dsconclusao as do_c_madc_dsconclusao
, do_c_madc.dsobservacaodo as do_c_madc_dsobservacaodo
, do_c_madc.dsobservacaobens as do_c_madc_dsobservacaobens
, do_c_madc.vltotaldispendio as do_c_madc_vltotaldispendio
, do_c_madc.vlaprovado as do_c_madc_vlaprovado
, do_c_madc.vlglosa as do_c_madc_vlglosa
, do_c_madc.nrtotalprojeto as do_c_madc_nrtotalprojeto
, do_c_madc.nrtotalaprovado as do_c_madc_nrtotalaprovado
, do_c_madc.nrtotalreprovado as do_c_madc_nrtotalreprovado
, do_c_madc.nranobase as do_c_madc_nranobase
, do_c_madc.dsobservacaoaocoordenador as do_c_madc_dsobservacaoaocoordenador
, do_c_madc.dsinformacaocomplementar as do_c_madc_dsinformacaocomplementar
, do_c_madc.dsconsideracaorecomendacao as do_c_madc_dsconsideracaorecomendacao
, do_c_madc.dssolicitaalteracao as do_c_madc_dssolicitaalteracao
, do_c_madc.dsobservacoesfinaiscontestacao as do_c_madc_dsobservacoesfinaiscontestacao
, do_c_madc.dsobservacoesfinaisrecursoadministrativo as do_c_madc_dsobservacoesfinaisrecursoadministrativo
, do_c_madc.dsjustificativaincentivosrecursoadm as do_c_madc_dsjustificativaincentivosrecursoadm
--, do_c_aompreec.idanaliseobjetomarcopreenchimentocontestacao as do_c_aompreec_idanaliseobjetomarcopreenchimentocontestacao
--, do_c_aompreec.vlcontestacao as do_c_aompreec_vlcontestacao
--, do_c_aompreec.dsjustificativacontestacao as do_c_aompreec_dsjustificativacontestacao
--, do_c_aompreec.dsjustificativaparecer as do_c_aompreec_dsjustificativaparecer
--, do_c_aompreec.vlindicadoanaliseparecer as do_c_aompreec_vlindicadoanaliseparecer
--, do_c_aompreec.vlglosaparecer as do_c_aompreec_vlglosaparecer
--, do_c_aompreec.vlanalisecontestacao as do_c_aompreec_vlanalisecontestacao
--, do_c_aompreec.dsjustificativaanalisecontestacao as do_c_aompreec_dsjustificativaanalisecontestacao
--, do_c_aompreec.vlrecursoadministrativo as do_c_aompreec_vlrecursoadministrativo
--, do_c_aompreec.dsjustificativarecursoadministrativo as do_c_aompreec_dsjustificativarecursoadministrativo
--
,do_c_a_pree.do_c_aompree_dsjustificativapadrao
,do_c_a_pree.do_c_aompree_vlindicadoanalise
,do_c_a_pree.do_c_aompree_vlglosa
,do_c_a_pree.do_c_taompree_dstipoanaliseobjetomarcopreenchimento
,do_c_a_pree.do_c_taapree_notipoavaliacaoanalise
,do_c_a_pree.do_c_japree_nojustificativaanalise
,do_c_a_pree.do_c_japree_notitulojustificativaanalise
,do_c_a_pree.do_c_japree_nocorpojustificativaanalise
,do_c_a_pree.do_c_japree_norodapejustificativaanalise
,do_c_a_pree.do_c_japree_notitulojustificativagrupoobjetoanaliseindividual
,do_c_a_pree.do_c_tjapree_notipojustificativaanalise
--
,do_c_a_pree.do_c_aompreec_vlcontestacao
,do_c_a_pree.do_c_aompreec_dsjustificativacontestacao
,do_c_a_pree.do_c_aompreec_dsjustificativaparecer
,do_c_a_pree.do_c_aompreec_vlindicadoanaliseparecer
,do_c_a_pree.do_c_aompreec_vlglosaparecer
,do_c_a_pree.do_c_aompreec_vlanalisecontestacao
,do_c_a_pree.do_c_aompreec_notipojustificativaanalisecontestacao
,do_c_a_pree.do_c_aompreec_vlrecursoadministrativo
,do_c_a_pree.do_c_aompreec_dsjustificativarecursoadministrativo
--
, do_c_lotema.idlotemarcoanalise as do_c_lotema_idlotemarcoanalise
, do_c_lotema.idlote as do_c_lotema_idlote
, do_c_lotema.idmarcoanalise as do_c_lotema_idmarcoanalise
, do_c_lotema.icvisualizou as do_c_lotema_icvisualizou
, do_c_lotema.idlotenovo as do_c_lotema_idlotenovo
, do_c_lotema.idhistoricopessoaaceite as do_c_lotema_idhistoricopessoaaceite
, do_c_lotema.idunicopessoaaceite as do_c_lotema_idunicopessoaaceite
, do_c_lotema.dtaceite as do_c_lotema_dtaceite
, do_c_lotema.icemailenviado as do_c_lotema_icemailenviado
, do_c_tlote.cdtipolote as do_c_tlote_cdtipolote
, do_c_tlote.notipolote as do_c_tlote_notipolote
, do_c_lote.idlote as do_c_lote_idlote
, do_c_lote.cdtipolote as do_c_lote_cdtipolote
, do_c_lote.dtpublicacao as do_c_lote_dtpublicacao
, do_c_lote.dtloteinicio as do_c_lote_dtloteinicio
, do_c_lote.dtlotefim as do_c_lote_dtlotefim
, do_c_lote.iclotefinalizado as do_c_lote_iclotefinalizado
, do_c_lote.nranobase as do_c_lote_nranobase
, do_c_lote.nrdiasaguardandoaceite as do_c_lote_nrdiasaguardandoaceite
, do_c_lote.nrdiasduracaolote as do_c_lote_nrdiasduracaolote
, do_c_lote.dsobservacoes as do_c_lote_dsobservacoes
, do_c_lote.nrlote as do_c_lote_nrlote
, p_c_ma.idmarcoanalise as p_c_ma_idmarcoanalise
, p_c_ma.idprenchimentosituacaoanalise as p_c_ma_idprenchimentosituacaoanalise
, p_c_ma.cdtipomarcoanalise as p_c_ma_cdtipomarcoanalise
, p_c_ma.idhistoricosituacaoanalise as p_c_ma_idhistoricosituacaoanalise
, p_c_ma.nrmarcoanalise as p_c_ma_nrmarcoanalise
, p_c_ma.dsobservacao as p_c_ma_dsobservacao
, p_c_ma.dscaminhoarquivoanalise as p_c_ma_dscaminhoarquivoanalise
, p_c_ma.cdresultadomarcoanalise as p_c_ma_cdresultadomarcoanalise
, p_c_ma.idmarcoanalisebase as p_c_ma_idmarcoanalisebase
, p_c_ma.cdsituacaoprocessamentoassinatura as p_c_ma_cdsituacaoprocessamentoassinatura
, p_c_rma.cdresultadomarcoanalise as p_c_rma_cdresultadomarcoanalise
, p_c_rma.noresultadomarcoanalise as p_c_rma_noresultadomarcoanalise
, p_c_tma.cdtipomarcoanalise as p_c_tma_cdtipomarcoanalise
, p_c_tma.notipomarcoanalise as p_c_tma_notipomarcoanalise
, p_c_hsa.idhistoricosituacaoanalise as p_c_hsa_idhistoricosituacaoanalise
, p_c_hsa.idprenchimentosituacaoanalise as p_c_hsa_idprenchimentosituacaoanalise
, p_c_hsa.cdtiposituacaomarco as p_c_hsa_cdtiposituacaomarco
, p_c_hsa.dtiniciosituacaoanalise as p_c_hsa_dtiniciosituacaoanalise
, p_c_hsa.dtfimsituacao as p_c_hsa_dtfimsituacao
, p_c_hsa.icativo as p_c_hsa_icativo
, p_c_hsa.idtask as p_c_hsa_idtask
, p_c_hsa.idmomentopessoa as p_c_hsa_idmomentopessoa
, p_c_hsa.idunicopessoa as p_c_hsa_idunicopessoa
, p_c_hsa.idmarcoanalise as p_c_hsa_idmarcoanalise
, p_c_tsm.cdtiposituacaomarco as p_c_tsm_cdtiposituacaomarco
, p_c_tsm.notiposituacaomarco as p_c_tsm_notiposituacaomarco
, p_c_tsm.dstiposituacaomarco as p_c_tsm_dstiposituacaomarco
, p_c_madc.idmarcoanalise as p_c_madc_idmarcoanalise
, p_c_madc.nrcnpj as p_c_madc_nrcnpj
, p_c_madc.norazaosocial as p_c_madc_norazaosocial
, p_c_madc.dsconclusao as p_c_madc_dsconclusao
, p_c_madc.dsobservacaodo as p_c_madc_dsobservacaodo
, p_c_madc.dsobservacaobens as p_c_madc_dsobservacaobens
, p_c_madc.vltotaldispendio as p_c_madc_vltotaldispendio
, p_c_madc.vlaprovado as p_c_madc_vlaprovado
, p_c_madc.vlglosa as p_c_madc_vlglosa
, p_c_madc.nrtotalprojeto as p_c_madc_nrtotalprojeto
, p_c_madc.nrtotalaprovado as p_c_madc_nrtotalaprovado
, p_c_madc.nrtotalreprovado as p_c_madc_nrtotalreprovado
, p_c_madc.nranobase as p_c_madc_nranobase
, p_c_madc.dsobservacaoaocoordenador as p_c_madc_dsobservacaoaocoordenador
, p_c_madc.dsinformacaocomplementar as p_c_madc_dsinformacaocomplementar
, p_c_madc.dsconsideracaorecomendacao as p_c_madc_dsconsideracaorecomendacao
, p_c_madc.dssolicitaalteracao as p_c_madc_dssolicitaalteracao
, p_c_madc.dsobservacoesfinaiscontestacao as p_c_madc_dsobservacoesfinaiscontestacao
, p_c_madc.dsobservacoesfinaisrecursoadministrativo as p_c_madc_dsobservacoesfinaisrecursoadministrativo
, p_c_madc.dsjustificativaincentivosrecursoadm as p_c_madc_dsjustificativaincentivosrecursoadm
--
,p_c_a_pree.p_c_aompree_dsjustificativapadrao
,p_c_a_pree.p_c_aompree_vlindicadoanalise
,p_c_a_pree.p_c_aompree_vlglosa
,p_c_a_pree.p_c_taompree_dstipoanaliseobjetomarcopreenchimento
,p_c_a_pree.p_c_taapree_notipoavaliacaoanalise
,p_c_a_pree.p_c_japree_nojustificativaanalise
,p_c_a_pree.p_c_japree_notitulojustificativaanalise
,p_c_a_pree.p_c_japree_nocorpojustificativaanalise
,p_c_a_pree.p_c_japree_norodapejustificativaanalise
,p_c_a_pree.p_c_japree_notitulojustificativagrupoobjetoanaliseindividual
,p_c_a_pree.p_c_tjapree_notipojustificativaanalise
--
,p_c_a_pree.p_c_aompreec_vlcontestacao
,p_c_a_pree.p_c_aompreec_dsjustificativacontestacao
,p_c_a_pree.p_c_aompreec_dsjustificativaparecer
,p_c_a_pree.p_c_aompreec_vlindicadoanaliseparecer
,p_c_a_pree.p_c_aompreec_vlglosaparecer
,p_c_a_pree.p_c_aompreec_vlanalisecontestacao
,p_c_a_pree.p_c_aompreec_notipojustificativaanalisecontestacao
,p_c_a_pree.p_c_aompreec_vlrecursoadministrativo
,p_c_a_pree.p_c_aompreec_dsjustificativarecursoadministrativo
--
--, p_c_aompreec.idanaliseobjetomarcopreenchimentocontestacao as p_c_aompreec_idanaliseobjetomarcopreenchimentocontestacao
--, p_c_aompreec.vlcontestacao as p_c_aompreec_vlcontestacao
--, p_c_aompreec.dsjustificativacontestacao as p_c_aompreec_dsjustificativacontestacao
--, p_c_aompreec.dsjustificativaparecer as p_c_aompreec_dsjustificativaparecer
--, p_c_aompreec.vlindicadoanaliseparecer as p_c_aompreec_vlindicadoanaliseparecer
--, p_c_aompreec.vlglosaparecer as p_c_aompreec_vlglosaparecer
--, p_c_aompreec.vlanalisecontestacao as p_c_aompreec_vlanalisecontestacao
--, p_c_aompreec.dsjustificativaanalisecontestacao as p_c_aompreec_dsjustificativaanalisecontestacao
--, p_c_aompreec.vlrecursoadministrativo as p_c_aompreec_vlrecursoadministrativo
--, p_c_aompreec.dsjustificativarecursoadministrativo as p_c_aompreec_dsjustificativarecursoadministrativo
, p_c_lotema.idlotemarcoanalise as p_c_lotema_idlotemarcoanalise
, p_c_lotema.idlote as p_c_lotema_idlote
, p_c_lotema.idmarcoanalise as p_c_lotema_idmarcoanalise
, p_c_lotema.icvisualizou as p_c_lotema_icvisualizou
, p_c_lotema.idlotenovo as p_c_lotema_idlotenovo
, p_c_lotema.idhistoricopessoaaceite as p_c_lotema_idhistoricopessoaaceite
, p_c_lotema.idunicopessoaaceite as p_c_lotema_idunicopessoaaceite
, p_c_lotema.dtaceite as p_c_lotema_dtaceite
, p_c_lotema.icemailenviado as p_c_lotema_icemailenviado
, p_c_tlote.cdtipolote as p_c_tlote_cdtipolote
, p_c_tlote.notipolote as p_c_tlote_notipolote
, p_c_lote.idlote as p_c_lote_idlote
, p_c_lote.cdtipolote as p_c_lote_cdtipolote
, p_c_lote.dtpublicacao as p_c_lote_dtpublicacao
, p_c_lote.dtloteinicio as p_c_lote_dtloteinicio
, p_c_lote.dtlotefim as p_c_lote_dtlotefim
, p_c_lote.iclotefinalizado as p_c_lote_iclotefinalizado
, p_c_lote.nranobase as p_c_lote_nranobase
, p_c_lote.nrdiasaguardandoaceite as p_c_lote_nrdiasaguardandoaceite
, p_c_lote.nrdiasduracaolote as p_c_lote_nrdiasduracaolote
, p_c_lote.dsobservacoes as p_c_lote_dsobservacoes
, p_c_lote.nrlote as p_c_lote_nrlote
, ra_ma.idmarcoanalise as ra_ma_idmarcoanalise
, ra_ma.idprenchimentosituacaoanalise as ra_ma_idprenchimentosituacaoanalise
, ra_ma.cdtipomarcoanalise as ra_ma_cdtipomarcoanalise
, ra_ma.idhistoricosituacaoanalise as ra_ma_idhistoricosituacaoanalise
, ra_ma.nrmarcoanalise as ra_ma_nrmarcoanalise
, ra_ma.dsobservacao as ra_ma_dsobservacao
, ra_ma.dscaminhoarquivoanalise as ra_ma_dscaminhoarquivoanalise
, ra_ma.cdresultadomarcoanalise as ra_ma_cdresultadomarcoanalise
, ra_ma.idmarcoanalisebase as ra_ma_idmarcoanalisebase
, ra_ma.cdsituacaoprocessamentoassinatura as ra_ma_cdsituacaoprocessamentoassinatura
, ra_rma.cdresultadomarcoanalise as ra_rma_cdresultadomarcoanalise
, ra_rma.noresultadomarcoanalise as ra_rma_noresultadomarcoanalise
, ra_tma.cdtipomarcoanalise as ra_tma_cdtipomarcoanalise
, ra_tma.notipomarcoanalise as ra_tma_notipomarcoanalise
, ra_hsa.idhistoricosituacaoanalise as ra_hsa_idhistoricosituacaoanalise
, ra_hsa.idprenchimentosituacaoanalise as ra_hsa_idprenchimentosituacaoanalise
, ra_hsa.cdtiposituacaomarco as ra_hsa_cdtiposituacaomarco
, ra_hsa.dtiniciosituacaoanalise as ra_hsa_dtiniciosituacaoanalise
, ra_hsa.dtfimsituacao as ra_hsa_dtfimsituacao
, ra_hsa.icativo as ra_hsa_icativo
, ra_hsa.idtask as ra_hsa_idtask
, ra_hsa.idmomentopessoa as ra_hsa_idmomentopessoa
, ra_hsa.idunicopessoa as ra_hsa_idunicopessoa
, ra_hsa.idmarcoanalise as ra_hsa_idmarcoanalise
, ra_tsm.cdtiposituacaomarco as ra_tsm_cdtiposituacaomarco
, ra_tsm.notiposituacaomarco as ra_tsm_notiposituacaomarco
, ra_tsm.dstiposituacaomarco as ra_tsm_dstiposituacaomarco
, ra_madc.idmarcoanalise as ra_madc_idmarcoanalise
, ra_madc.nrcnpj as ra_madc_nrcnpj
, ra_madc.norazaosocial as ra_madc_norazaosocial
, ra_madc.dsconclusao as ra_madc_dsconclusao
, ra_madc.dsobservacaodo as ra_madc_dsobservacaodo
, ra_madc.dsobservacaobens as ra_madc_dsobservacaobens
, ra_madc.vltotaldispendio as ra_madc_vltotaldispendio
, ra_madc.vlaprovado as ra_madc_vlaprovado
, ra_madc.vlglosa as ra_madc_vlglosa
, ra_madc.nrtotalprojeto as ra_madc_nrtotalprojeto
, ra_madc.nrtotalaprovado as ra_madc_nrtotalaprovado
, ra_madc.nrtotalreprovado as ra_madc_nrtotalreprovado
, ra_madc.nranobase as ra_madc_nranobase
, ra_madc.dsobservacaoaocoordenador as ra_madc_dsobservacaoaocoordenador
, ra_madc.dsinformacaocomplementar as ra_madc_dsinformacaocomplementar
, ra_madc.dsconsideracaorecomendacao as ra_madc_dsconsideracaorecomendacao
, ra_madc.dssolicitaalteracao as ra_madc_dssolicitaalteracao
, ra_madc.dsobservacoesfinaiscontestacao as ra_madc_dsobservacoesfinaiscontestacao
, ra_madc.dsobservacoesfinaisrecursoadministrativo as ra_madc_dsobservacoesfinaisrecursoadministrativo
, ra_madc.dsjustificativaincentivosrecursoadm as ra_madc_dsjustificativaincentivosrecursoadm
--, ra_aompreec.idanaliseobjetomarcopreenchimentocontestacao as ra_aompreec_idanaliseobjetomarcopreenchimentocontestacao
--, ra_aompreec.vlcontestacao as ra_aompreec_vlcontestacao
--, ra_aompreec.dsjustificativacontestacao as ra_aompreec_dsjustificativacontestacao
--, ra_aompreec.dsjustificativaparecer as ra_aompreec_dsjustificativaparecer
--, ra_aompreec.vlindicadoanaliseparecer as ra_aompreec_vlindicadoanaliseparecer
--, ra_aompreec.vlglosaparecer as ra_aompreec_vlglosaparecer
--, ra_aompreec.vlanalisecontestacao as ra_aompreec_vlanalisecontestacao
--, ra_aompreec.dsjustificativaanalisecontestacao as ra_aompreec_dsjustificativaanalisecontestacao
--, ra_aompreec.vlrecursoadministrativo as ra_aompreec_vlrecursoadministrativo
--, ra_aompreec.dsjustificativarecursoadministrativo as ra_aompreec_dsjustificativarecursoadministrativo
--
,ra_a_pree.ra_aompree_dsjustificativapadrao
,ra_a_pree.ra_aompree_vlindicadoanalise
,ra_a_pree.ra_aompree_vlglosa
,ra_a_pree.ra_taompree_dstipoanaliseobjetomarcopreenchimento
,ra_a_pree.ra_taapree_notipoavaliacaoanalise
,ra_a_pree.ra_japree_nojustificativaanalise
,ra_a_pree.ra_japree_notitulojustificativaanalise
,ra_a_pree.ra_japree_nocorpojustificativaanalise
,ra_a_pree.ra_japree_norodapejustificativaanalise
,ra_a_pree.ra_japree_notitulojustificativagrupoobjetoanaliseindividual
,ra_a_pree.ra_tjapree_notipojustificativaanalise
--
,ra_a_pree.ra_aompreec_vlcontestacao
,ra_a_pree.ra_aompreec_dsjustificativacontestacao
,ra_a_pree.ra_aompreec_dsjustificativaparecer
,ra_a_pree.ra_aompreec_vlindicadoanaliseparecer
,ra_a_pree.ra_aompreec_vlglosaparecer
,ra_a_pree.ra_aompreec_vlanalisecontestacao
,ra_a_pree.ra_aompreec_notipojustificativaanalisecontestacao
,ra_a_pree.ra_aompreec_vlrecursoadministrativo
,ra_a_pree.ra_aompreec_dsjustificativarecursoadministrativo
--
, ra_lotema.idlotemarcoanalise as ra_lotema_idlotemarcoanalise
, ra_lotema.idlote as ra_lotema_idlote
, ra_lotema.idmarcoanalise as ra_lotema_idmarcoanalise
, ra_lotema.icvisualizou as ra_lotema_icvisualizou
, ra_lotema.idlotenovo as ra_lotema_idlotenovo
, ra_lotema.idhistoricopessoaaceite as ra_lotema_idhistoricopessoaaceite
, ra_lotema.idunicopessoaaceite as ra_lotema_idunicopessoaaceite
, ra_lotema.dtaceite as ra_lotema_dtaceite
, ra_lotema.icemailenviado as ra_lotema_icemailenviado
, ra_tlote.cdtipolote as ra_tlote_cdtipolote
, ra_tlote.notipolote as ra_tlote_notipolote
, ra_lote.idlote as ra_lote_idlote
, ra_lote.cdtipolote as ra_lote_cdtipolote
, ra_lote.dtpublicacao as ra_lote_dtpublicacao
, ra_lote.dtloteinicio as ra_lote_dtloteinicio
, ra_lote.dtlotefim as ra_lote_dtlotefim
, ra_lote.iclotefinalizado as ra_lote_iclotefinalizado
, ra_lote.nranobase as ra_lote_nranobase
, ra_lote.nrdiasaguardandoaceite as ra_lote_nrdiasaguardandoaceite
, ra_lote.nrdiasduracaolote as ra_lote_nrdiasduracaolote
, ra_lote.dsobservacoes as ra_lote_dsobservacoes
, ra_lote.nrlote as ra_lote_nrlote
from tbdadoempresamarco dem
left join listaempresasporanobasesituacaoanalise lst on lst.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise 
left join tbdadoanalisepreenchimento dapree on dapree.idprenchimentosituacaoanalise = dem.idprenchimentosituacaoanalise
left join tbdadoanalisefontefinanciamento daffin on daffin.idprenchimentosituacaoanalise = dapree.idprenchimentosituacaoanalise 
left join tbprenchimentosituacaoanalise psa on psa.idprenchimentosituacaoanalise = dapree.idprenchimentosituacaoanalise 
--left join tbinconsistenciarh incrh on incrh.idprenchimentosituacaoanalise = dapree.idprenchimentosituacaoanalise 
--
--DO
--
left join tbmarcoanalise do_ma on do_ma.idmarcoanalise = dem.idmarcoanalisedo
left join tbhistoricosituacaoanalise do_hsa on do_hsa.idhistoricosituacaoanalise  = do_ma.idhistoricosituacaoanalise  
--
left join tbresultadomarcoanalise do_rma on do_rma.cdresultadomarcoanalise = do_ma.cdresultadomarcoanalise 
left join tbtipomarcoanalise do_tma on do_tma.cdtipomarcoanalise = do_ma.cdtipomarcoanalise 
left join tbmarcoanalisedadoconsolidado do_madc on do_madc.idmarcoanalise = do_ma.idmarcoanalise 
left join tbtiposituacaomarco do_tsm on do_tsm.cdtiposituacaomarco = do_hsa.cdtiposituacaomarco 
--
left join( 
	select do_aompree.idmarcoanalise
		, STRING_AGG( do_aompree.dsjustificativapadrao , CHR(10)) as do_aompree_dsjustificativapadrao
		, SUM(do_aompree.vlindicadoanalise) as do_aompree_vlindicadoanalise
		, SUM(do_aompree.vlglosa) as do_aompree_vlglosa
		, STRING_AGG(do_taompree.dstipoanaliseobjetomarcopreenchimento , CHR(10)) as do_taompree_dstipoanaliseobjetomarcopreenchimento
		, STRING_AGG(do_taapree.notipoavaliacaoanalise , CHR(10)) as do_taapree_notipoavaliacaoanalise
		, STRING_AGG(do_japree.nojustificativaanalise , CHR(10)) as do_japree_nojustificativaanalise
		, STRING_AGG(do_japree.notitulojustificativaanalise , CHR(10)) as do_japree_notitulojustificativaanalise
		, STRING_AGG(do_japree.nocorpojustificativaanalise , CHR(10)) as do_japree_nocorpojustificativaanalise
		, STRING_AGG(do_japree.norodapejustificativaanalise , CHR(10)) as do_japree_norodapejustificativaanalise
		, STRING_AGG(do_japree.notitulojustificativagrupoobjetoanaliseindividual , CHR(10)) as do_japree_notitulojustificativagrupoobjetoanaliseindividual
		, STRING_AGG(do_tjapree.notipojustificativaanalise , CHR(10)) as do_tjapree_notipojustificativaanalise
	from tbanaliseobjetomarcopreenchimento do_aompree
	left join tbtipoanaliseobjetomarcopreenchimento do_taompree on do_taompree.cdtipoanaliseobjetomarcopreenchimento = do_aompree.cdtipoanaliseobjetomarcopreenchimento 
	left join tbtipoavaliacaoanalise do_taapree on do_taapree.idtipoavaliacaoanalise = do_aompree.idtipoavaliacaoanalise
	left join tbjustificativaanalise do_japree on do_japree.idjustificativaanalise = do_aompree.idjustificativaanalise
	left join tbtipojustificativaanalise do_tjapree on do_tjapree.cdtipojustificativaanalise = do_japree.cdtipojustificativaanalise
	group by do_aompree.idmarcoanalise) do_a_pree on do_a_pree.idmarcoanalise = do_ma.idmarcoanalise
--
--PARECER
--
left join tbmarcoanalise p_ma on p_ma.idmarcoanalise = dem.idmarcoanaliseparecer
left join tbhistoricosituacaoanalise p_hsa on p_hsa.idhistoricosituacaoanalise  = p_ma.idhistoricosituacaoanalise  
--
left join tbresultadomarcoanalise p_rma on p_rma.cdresultadomarcoanalise = p_ma.cdresultadomarcoanalise 
left join tbtipomarcoanalise p_tma on p_tma.cdtipomarcoanalise = p_ma.cdtipomarcoanalise 
left join tbmarcoanalisedadoconsolidado p_madc on p_madc.idmarcoanalise = p_ma.idmarcoanalise 
left join tbtiposituacaomarco p_tsm on p_tsm.cdtiposituacaomarco = p_hsa.cdtiposituacaomarco 
--
left join( 
	select p_aompree.idmarcoanalise
		, STRING_AGG( p_aompree.dsjustificativapadrao , CHR(10)) as p_aompree_dsjustificativapadrao
		, SUM(p_aompree.vlindicadoanalise) as p_aompree_vlindicadoanalise
		, SUM(p_aompree.vlglosa) as p_aompree_vlglosa
		, STRING_AGG(p_taompree.dstipoanaliseobjetomarcopreenchimento , CHR(10)) as p_taompree_dstipoanaliseobjetomarcopreenchimento
		, STRING_AGG(p_taapree.notipoavaliacaoanalise , CHR(10)) as p_taapree_notipoavaliacaoanalise
		, STRING_AGG(p_japree.nojustificativaanalise , CHR(10)) as p_japree_nojustificativaanalise
		, STRING_AGG(p_japree.notitulojustificativaanalise , CHR(10)) as p_japree_notitulojustificativaanalise
		, STRING_AGG(p_japree.nocorpojustificativaanalise , CHR(10)) as p_japree_nocorpojustificativaanalise
		, STRING_AGG(p_japree.norodapejustificativaanalise , CHR(10)) as p_japree_norodapejustificativaanalise
		, STRING_AGG(p_japree.notitulojustificativagrupoobjetoanaliseindividual , CHR(10)) as p_japree_notitulojustificativagrupoobjetoanaliseindividual
		, STRING_AGG(p_tjapree.notipojustificativaanalise , CHR(10)) as p_tjapree_notipojustificativaanalise
	from tbanaliseobjetomarcopreenchimento p_aompree
	left join tbtipoanaliseobjetomarcopreenchimento p_taompree on p_taompree.cdtipoanaliseobjetomarcopreenchimento = p_aompree.cdtipoanaliseobjetomarcopreenchimento 
	left join tbtipoavaliacaoanalise p_taapree on p_taapree.idtipoavaliacaoanalise = p_aompree.idtipoavaliacaoanalise
	left join tbjustificativaanalise p_japree on p_japree.idjustificativaanalise = p_aompree.idjustificativaanalise
	left join tbtipojustificativaanalise p_tjapree on p_tjapree.cdtipojustificativaanalise = p_japree.cdtipojustificativaanalise
	group by p_aompree.idmarcoanalise) p_a_pree on p_a_pree.idmarcoanalise = p_ma.idmarcoanalise
--
--DO CONTESTACAO
--
left join tbmarcoanalise do_c_ma on do_c_ma.idmarcoanalise = dem.idmarcoanalisedocontestacao 
left join tbhistoricosituacaoanalise do_c_hsa on do_c_hsa.idhistoricosituacaoanalise  = do_c_ma.idhistoricosituacaoanalise  
--
left join tbresultadomarcoanalise do_c_rma on do_c_rma.cdresultadomarcoanalise = do_c_ma.cdresultadomarcoanalise 
left join tbtipomarcoanalise do_c_tma on do_c_tma.cdtipomarcoanalise = do_c_ma.cdtipomarcoanalise 
left join tbmarcoanalisedadoconsolidado do_c_madc on do_c_madc.idmarcoanalise = do_c_ma.idmarcoanalise 
left join tbtiposituacaomarco do_c_tsm on do_c_tsm.cdtiposituacaomarco = do_c_hsa.cdtiposituacaomarco 
--left join tbmarcoanalisedadoconsolidadoanexo do_c_madca on do_c_madca.idmarcoanalise = do_c_ma.idmarcoanalise 
--left join tbanaliseobjetomarcopreenchimentocontestacao do_c_aompreec on do_c_aompreec.idanaliseobjetomarcopreenchimentocontestacao = do_c_aompree.idanaliseobjetomarcopreenchimento
--
left join( 
	select do_c_aompree.idmarcoanalise
		, STRING_AGG( do_c_aompree.dsjustificativapadrao , CHR(10)) as do_c_aompree_dsjustificativapadrao
		, SUM(do_c_aompree.vlindicadoanalise) as do_c_aompree_vlindicadoanalise
		, SUM(do_c_aompree.vlglosa) as do_c_aompree_vlglosa
		, STRING_AGG(do_c_taompree.dstipoanaliseobjetomarcopreenchimento , CHR(10)) as do_c_taompree_dstipoanaliseobjetomarcopreenchimento
		, STRING_AGG(do_c_taapree.notipoavaliacaoanalise , CHR(10)) as do_c_taapree_notipoavaliacaoanalise
		, STRING_AGG(do_c_japree.nojustificativaanalise , CHR(10)) as do_c_japree_nojustificativaanalise
		, STRING_AGG(do_c_japree.notitulojustificativaanalise , CHR(10)) as do_c_japree_notitulojustificativaanalise
		, STRING_AGG(do_c_japree.nocorpojustificativaanalise , CHR(10)) as do_c_japree_nocorpojustificativaanalise
		, STRING_AGG(do_c_japree.norodapejustificativaanalise , CHR(10)) as do_c_japree_norodapejustificativaanalise
		, STRING_AGG(do_c_japree.notitulojustificativagrupoobjetoanaliseindividual , CHR(10)) as do_c_japree_notitulojustificativagrupoobjetoanaliseindividual
		, STRING_AGG(do_c_tjapree.notipojustificativaanalise , CHR(10)) as do_c_tjapree_notipojustificativaanalise
		--
		, SUM(do_c_aompreec.vlcontestacao) as do_c_aompreec_vlcontestacao
		, STRING_AGG(do_c_aompreec.dsjustificativacontestacao , CHR(10)) as do_c_aompreec_dsjustificativacontestacao
		, STRING_AGG(do_c_aompreec.dsjustificativaparecer , CHR(10)) as do_c_aompreec_dsjustificativaparecer
		, SUM(do_c_aompreec.vlindicadoanaliseparecer) as do_c_aompreec_vlindicadoanaliseparecer
		, SUM(do_c_aompreec.vlglosaparecer) as do_c_aompreec_vlglosaparecer
		, SUM(do_c_aompreec.vlanalisecontestacao) as do_c_aompreec_vlanalisecontestacao
		, STRING_AGG(do_c_aompreec.dsjustificativaanalisecontestacao , CHR(10)) as do_c_aompreec_notipojustificativaanalisecontestacao
		, SUM(do_c_aompreec.vlrecursoadministrativo) as do_c_aompreec_vlrecursoadministrativo
		, STRING_AGG(do_c_aompreec.dsjustificativarecursoadministrativo , CHR(10)) as do_c_aompreec_dsjustificativarecursoadministrativo
	from tbanaliseobjetomarcopreenchimento do_c_aompree
	left join tbtipoanaliseobjetomarcopreenchimento do_c_taompree on do_c_taompree.cdtipoanaliseobjetomarcopreenchimento = do_c_aompree.cdtipoanaliseobjetomarcopreenchimento 
	left join tbtipoavaliacaoanalise do_c_taapree on do_c_taapree.idtipoavaliacaoanalise = do_c_aompree.idtipoavaliacaoanalise
	left join tbjustificativaanalise do_c_japree on do_c_japree.idjustificativaanalise = do_c_aompree.idjustificativaanalise
	left join tbtipojustificativaanalise do_c_tjapree on do_c_tjapree.cdtipojustificativaanalise = do_c_japree.cdtipojustificativaanalise
	left join tbanaliseobjetomarcopreenchimentocontestacao do_c_aompreec on do_c_aompreec.idanaliseobjetomarcopreenchimentocontestacao = do_c_aompree.idanaliseobjetomarcopreenchimento
	group by do_c_aompree.idmarcoanalise) do_c_a_pree on do_c_a_pree.idmarcoanalise = do_c_ma.idmarcoanalise
left join tblotemarcoanalise do_c_lotema on do_c_lotema.idmarcoanalise = do_c_ma.idmarcoanalise 
left join tblote do_c_lote on do_c_lote.idlote = do_c_lotema.idlote 
left join tbtipolote do_c_tlote on do_c_tlote.cdtipolote = do_c_lote.cdtipolote
--
--PARECER CONTESTACAO
--
left join tbmarcoanalise p_c_ma on p_c_ma.idmarcoanalise = dem.idmarcoanaliseparecercontestacao 
left join tbhistoricosituacaoanalise p_c_hsa on p_c_hsa.idhistoricosituacaoanalise  = p_c_ma.idhistoricosituacaoanalise  
--
left join tbresultadomarcoanalise p_c_rma on p_c_rma.cdresultadomarcoanalise = p_c_ma.cdresultadomarcoanalise 
left join tbtipomarcoanalise p_c_tma on p_c_tma.cdtipomarcoanalise = p_c_ma.cdtipomarcoanalise 
left join tbmarcoanalisedadoconsolidado p_c_madc on p_c_madc.idmarcoanalise = p_c_ma.idmarcoanalise 
left join tbtiposituacaomarco p_c_tsm on p_c_tsm.cdtiposituacaomarco = p_c_hsa.cdtiposituacaomarco 
--
left join( 
	select p_c_aompree.idmarcoanalise
		, STRING_AGG( p_c_aompree.dsjustificativapadrao , CHR(10)) as p_c_aompree_dsjustificativapadrao
		, SUM(p_c_aompree.vlindicadoanalise) as p_c_aompree_vlindicadoanalise
		, SUM(p_c_aompree.vlglosa) as p_c_aompree_vlglosa
		, STRING_AGG(p_c_taompree.dstipoanaliseobjetomarcopreenchimento , CHR(10)) as p_c_taompree_dstipoanaliseobjetomarcopreenchimento
		, STRING_AGG(p_c_taapree.notipoavaliacaoanalise , CHR(10)) as p_c_taapree_notipoavaliacaoanalise
		, STRING_AGG(p_c_japree.nojustificativaanalise , CHR(10)) as p_c_japree_nojustificativaanalise
		, STRING_AGG(p_c_japree.notitulojustificativaanalise , CHR(10)) as p_c_japree_notitulojustificativaanalise
		, STRING_AGG(p_c_japree.nocorpojustificativaanalise , CHR(10)) as p_c_japree_nocorpojustificativaanalise
		, STRING_AGG(p_c_japree.norodapejustificativaanalise , CHR(10)) as p_c_japree_norodapejustificativaanalise
		, STRING_AGG(p_c_japree.notitulojustificativagrupoobjetoanaliseindividual , CHR(10)) as p_c_japree_notitulojustificativagrupoobjetoanaliseindividual
		, STRING_AGG(p_c_tjapree.notipojustificativaanalise , CHR(10)) as p_c_tjapree_notipojustificativaanalise
		--
		, SUM(p_c_aompreec.vlcontestacao) as p_c_aompreec_vlcontestacao
		, STRING_AGG(p_c_aompreec.dsjustificativacontestacao , CHR(10)) as p_c_aompreec_dsjustificativacontestacao
		, STRING_AGG(p_c_aompreec.dsjustificativaparecer , CHR(10)) as p_c_aompreec_dsjustificativaparecer
		, SUM(p_c_aompreec.vlindicadoanaliseparecer) as p_c_aompreec_vlindicadoanaliseparecer
		, SUM(p_c_aompreec.vlglosaparecer) as p_c_aompreec_vlglosaparecer
		, SUM(p_c_aompreec.vlanalisecontestacao) as p_c_aompreec_vlanalisecontestacao
		, STRING_AGG(p_c_aompreec.dsjustificativaanalisecontestacao , CHR(10)) as p_c_aompreec_notipojustificativaanalisecontestacao
		, SUM(p_c_aompreec.vlrecursoadministrativo) as p_c_aompreec_vlrecursoadministrativo
		, STRING_AGG(p_c_aompreec.dsjustificativarecursoadministrativo , CHR(10)) as p_c_aompreec_dsjustificativarecursoadministrativo
	from tbanaliseobjetomarcopreenchimento p_c_aompree
	left join tbtipoanaliseobjetomarcopreenchimento p_c_taompree on p_c_taompree.cdtipoanaliseobjetomarcopreenchimento = p_c_aompree.cdtipoanaliseobjetomarcopreenchimento 
	left join tbtipoavaliacaoanalise p_c_taapree on p_c_taapree.idtipoavaliacaoanalise = p_c_aompree.idtipoavaliacaoanalise
	left join tbjustificativaanalise p_c_japree on p_c_japree.idjustificativaanalise = p_c_aompree.idjustificativaanalise
	left join tbtipojustificativaanalise p_c_tjapree on p_c_tjapree.cdtipojustificativaanalise = p_c_japree.cdtipojustificativaanalise
	left join tbanaliseobjetomarcopreenchimentocontestacao p_c_aompreec on p_c_aompreec.idanaliseobjetomarcopreenchimentocontestacao = p_c_aompree.idanaliseobjetomarcopreenchimento
	group by p_c_aompree.idmarcoanalise) p_c_a_pree on p_c_a_pree.idmarcoanalise = p_c_ma.idmarcoanalise
--
--left join tbmarcoanalisedadoconsolidadoanexo p_c_madca on p_c_madca.idmarcoanalise = p_c_ma.idmarcoanalise 
--left join tbanaliseobjetomarcopreenchimentocontestacao p_c_aompreec on p_c_aompreec.idanaliseobjetomarcopreenchimentocontestacao = p_c_aompree.idanaliseobjetomarcopreenchimento
left join tblotemarcoanalise p_c_lotema on p_c_lotema.idmarcoanalise = p_c_ma.idmarcoanalise 
left join tblote p_c_lote on p_c_lote.idlote = p_c_lotema.idlote 
left join tbtipolote p_c_tlote on p_c_tlote.cdtipolote = p_c_lote.cdtipolote
--
--RECURSO ADMINISTRATIVO
--
left join tbmarcoanalise ra_ma on ra_ma.idmarcoanalise = dem.idmarcoanaliseparecerrecurso 
left join tbhistoricosituacaoanalise ra_hsa on ra_hsa.idhistoricosituacaoanalise  = ra_ma.idhistoricosituacaoanalise  
--
left join tbresultadomarcoanalise ra_rma on ra_rma.cdresultadomarcoanalise = ra_ma.cdresultadomarcoanalise 
left join tbtipomarcoanalise ra_tma on ra_tma.cdtipomarcoanalise = ra_ma.cdtipomarcoanalise 
left join tbmarcoanalisedadoconsolidado ra_madc on ra_madc.idmarcoanalise = ra_ma.idmarcoanalise 
left join tbtiposituacaomarco ra_tsm on ra_tsm.cdtiposituacaomarco = ra_hsa.cdtiposituacaomarco 
--
left join( 
	select ra_aompree.idmarcoanalise
		, STRING_AGG( ra_aompree.dsjustificativapadrao , CHR(10)) as ra_aompree_dsjustificativapadrao
		, SUM(ra_aompree.vlindicadoanalise) as ra_aompree_vlindicadoanalise
		, SUM(ra_aompree.vlglosa) as ra_aompree_vlglosa
		, STRING_AGG(ra_taompree.dstipoanaliseobjetomarcopreenchimento , CHR(10)) as ra_taompree_dstipoanaliseobjetomarcopreenchimento
		, STRING_AGG(ra_taapree.notipoavaliacaoanalise , CHR(10)) as ra_taapree_notipoavaliacaoanalise
		, STRING_AGG(ra_japree.nojustificativaanalise , CHR(10)) as ra_japree_nojustificativaanalise
		, STRING_AGG(ra_japree.notitulojustificativaanalise , CHR(10)) as ra_japree_notitulojustificativaanalise
		, STRING_AGG(ra_japree.nocorpojustificativaanalise , CHR(10)) as ra_japree_nocorpojustificativaanalise
		, STRING_AGG(ra_japree.norodapejustificativaanalise , CHR(10)) as ra_japree_norodapejustificativaanalise
		, STRING_AGG(ra_japree.notitulojustificativagrupoobjetoanaliseindividual , CHR(10)) as ra_japree_notitulojustificativagrupoobjetoanaliseindividual
		, STRING_AGG(ra_tjapree.notipojustificativaanalise , CHR(10)) as ra_tjapree_notipojustificativaanalise
		--
		, SUM(ra_aompreec.vlcontestacao) as ra_aompreec_vlcontestacao
		, STRING_AGG(ra_aompreec.dsjustificativacontestacao , CHR(10)) as ra_aompreec_dsjustificativacontestacao
		, STRING_AGG(ra_aompreec.dsjustificativaparecer , CHR(10)) as ra_aompreec_dsjustificativaparecer
		, SUM(ra_aompreec.vlindicadoanaliseparecer) as ra_aompreec_vlindicadoanaliseparecer
		, SUM(ra_aompreec.vlglosaparecer) as ra_aompreec_vlglosaparecer
		, SUM(ra_aompreec.vlanalisecontestacao) as ra_aompreec_vlanalisecontestacao
		, STRING_AGG(ra_aompreec.dsjustificativaanalisecontestacao , CHR(10)) as ra_aompreec_notipojustificativaanalisecontestacao
		, SUM(ra_aompreec.vlrecursoadministrativo) as ra_aompreec_vlrecursoadministrativo
		, STRING_AGG(ra_aompreec.dsjustificativarecursoadministrativo , CHR(10)) as ra_aompreec_dsjustificativarecursoadministrativo
		--
	from tbanaliseobjetomarcopreenchimento ra_aompree
	left join tbtipoanaliseobjetomarcopreenchimento ra_taompree on ra_taompree.cdtipoanaliseobjetomarcopreenchimento = ra_aompree.cdtipoanaliseobjetomarcopreenchimento 
	left join tbtipoavaliacaoanalise ra_taapree on ra_taapree.idtipoavaliacaoanalise = ra_aompree.idtipoavaliacaoanalise
	left join tbjustificativaanalise ra_japree on ra_japree.idjustificativaanalise = ra_aompree.idjustificativaanalise
	left join tbtipojustificativaanalise ra_tjapree on ra_tjapree.cdtipojustificativaanalise = ra_japree.cdtipojustificativaanalise
	left join tbanaliseobjetomarcopreenchimentocontestacao ra_aompreec on ra_aompreec.idanaliseobjetomarcopreenchimentocontestacao = ra_aompree.idanaliseobjetomarcopreenchimento
	group by ra_aompree.idmarcoanalise) ra_a_pree on ra_a_pree.idmarcoanalise = ra_ma.idmarcoanalise
--
--left join tbmarcoanalisedadoconsolidadoanexo ra_madca on ra_madca.idmarcoanalise = ra_ma.idmarcoanalise 
--left join tbanaliseobjetomarcopreenchimentocontestacao ra_aompreec on ra_aompreec.idanaliseobjetomarcopreenchimentocontestacao = ra_aompree.idanaliseobjetomarcopreenchimento
left join tblotemarcoanalise ra_lotema on ra_lotema.idmarcoanalise = ra_ma.idmarcoanalise 
left join tblote ra_lote on ra_lote.idlote = ra_lotema.idlote 
left join tbtipolote ra_tlote on ra_tlote.cdtipolote = ra_lote.cdtipolote


where lst.nranobase = 2022
