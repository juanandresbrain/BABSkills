# dbo.spRptParam_StoreSelectStateProvince

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRptParam_StoreSelectStateProvince"]
    dbo_vwStore_dimBO6(["dbo.vwStore_dimBO6"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwStore_dimBO6 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRptParam_StoreSelectStateProvince]

AS
/*
	2015-04-15	Kevin Shyr	Created
*/
BEGIN
	SET NOCOUNT ON;

	SELECT DISTINCT vsdbo.state_province
	FROM dbo.vwStore_dimBO6 vsdbo
	WHERE ISNULL(vsdbo.state_province, '') <> ''
	ORDER BY vsdbo.state_province

END
dbo,spGuestLoad_Pull_Raw_Kiosk_Addresses,-- =============================================================================================================
-- Name: spGuestLoad_Pull_Raw_Kiosk_Addresses
--
-- Description:	
--		Take the staged kiosk addresses and merge them with the raw_addr_dim to see if we have matches
--
-- Input:
--		@etl_log_id			int	
--			Current load to process
--
-- Output: 
--		data will be loaded into dw.dbo.GuestLoad_Pull_Raw_Kiosk_Addresses 
--
-- Dependencies: 
--
-- EXAMPLE:
--		exec dw.dbo.spGuestLoad_Pull_Raw_Kiosk_Addresses 1
--
-- Revision History
--		Name:			Date:			Comments:
--		Dave Rice		7/19/2010		created
--		Dave Rice		12/28/2010		null now means yes, but it's a little more complicated, if blank, then use the email_stat_cd
--										party data, we need the cleansed addresses for cleansed guests, but we don't want to make them opted in,
--										so i'm making them unknown, parties shouldn't be valid options now
-- =============================================================================================================

CREATE PROCEDURE [dbo].[spGuestLoad_Pull_Raw_Kiosk_Addresses](@etl_log_id int)
AS
BEGIN
-- SET NOCOUNT ON added to prevent extra result sets from
-- interfering with SELECT statements.
SET NOCOUNT ON;

----exec dbo.[spGuestLoad_Pull_Raw_Kiosk_Addresses] 13882
--select top 1 etl_log_id from dwstaging.dbo.load_rec_id_cntrl with (nolock)
--declare @etl_log_id int
--set @etl_log_id = 42601

IF (Object_ID('tempdb..#staging_kiosk') IS NOT NULL) DROP TABLE #staging_kiosk
select distinct 
	addr_chksum,
	KSK_REGIS_STG_ID,
	isnull(SNDR_SND_MAIL_CD, '') SNDR_SND_MAIL_CD, 

	-- if the mail code is blank then use the email stat code
	case 
		when SNDR_SND_MAIL_CD is null or SNDR_SND_MAIL_CD = '' then
		case
			when PRTY_TRN_CD in ('true','yes','1') then 'U'
			when SNDR_SND_EMAIL_CD in ('KEEP') then 'Y'
			when SNDR_SND_EMAIL_CD in ('Y', 'YES', 'T', 'TRUE', '1', '') or SNDR_SND_EMAIL_CD is null then 'Y'
			when SNDR_SND_EMAIL_CD in ('N', 'NO', 'F', 'FALSE', '0') then 'N'
			else 'U'
		end		
		else
		case 
			when PRTY_TRN_CD in ('true','yes','1') then 'U'
			when SNDR_SND_MAIL_CD in ('KEEP') then 'Y'
			when SNDR_SND_MAIL_CD IN ('Y', 'YES', 'T', 'TRUE', '1', '') or SNDR_SND_MAIL_CD is null then 'Y'
			when SNDR_SND_MAIL_CD IN ('N', 'NO', 'F', 'FALSE', '0') then 'N'
			else 'U' 
		end 
	end DRVD_MAIL_STAT_CD,
--	cast(convert(varchar, isnull(TRN_START_DT, @null_date), 101) as datetime) MAIL_OPT_IN_DT,

	isnull(dw.dbo.fnRemoveASCIIChar(SNDR_ADDR_LN_1_TXT, 0),'')	SNDR_ADDR_LN_1_TXT, 
	isnull(dw.dbo.fnRemoveASCIIChar(SNDR_ADDR_LN_2_TXT, 0),'')	SNDR_ADDR_LN_2_TXT,
	isnull(dw.dbo.fnRemoveASCIIChar(SNDR_APT_UNIT_NBR, 0),'')	SNDR_APT_UNIT_NBR, 
	isnull(dw.dbo.fnRemoveASCIIChar(SNDR_CTY_NM, 0),'')	SNDR_CTY_NM, 
	isnull(dw.dbo.fnRemoveASCIIChar(SNDR_PSTL_CD, 0),'')	SNDR_PSTL_CD, 
	isnull(dw.dbo.fnRemoveASCIIChar(SNDR_ST_PRVNC_TXT, 0),'')	SNDR_ST_PRVNC_TXT, 
	isnull(dw.dbo.fnRemoveASCIIChar(SNDR_CNTRY_TXT, 0),'')	SNDR_CNTRY_TXT,
	cast(''	as varchar(1)) CRM_SND_MAIL_CD,
	cast(''	as varchar(1)) CRM_MAIL_OPT_IN_CD,
	case 
		when st.statename is not null and st.US_BABW = 'Y' then 'US'
		when st.statename is not null and st.US_BABW = 'N' then 'CA'
		when st2.abrev is not null and len(s.SNDR_PSTL_CD) = 5 and st2.US_BABW = 'Y' then 'US'
		when st2.abrev is not null and st2.US_BABW = 'N' then 'CA'
 		when kcm.sCountry is not null then '' + kcm.sCountry
-- 		when kcm2.sCountry is not null then '' + kcm.sCountry
		when uk.postcode is not null then 'GB'
		when sd.country is not null then case when sd.country = 'UK' then 'GB' else sd.country end
		else 'US'
	end DRVD_CNTRY_ABBRV
into #staging_kiosk
--select *
from dwStaging.dbo.KSK_REGIS_STG s
	left join dw.dbo.tblKioskCountryMapping kcm with (nolock)
	on kcm.sKioskCountry = s.SNDR_CNTRY_TXT
	left join dw.dbo.tblstates st with (nolock)
	on st.statename = rtrim(s.SNDR_ST_PRVNC_TXT)
	left join dw.dbo.tblstates st2 with (nolock)
	on st2.abrev = s.SNDR_ST_PRVNC_TXT 
	left join dw.dbo.tblUKPostalCodes_new uk with (nolock)
	on uk.postcodecompressed = replace(s.SNDR_PSTL_CD, ' ','')
	left join dw.dbo.store_dim sd with (nolock)
	on sd.store_id = s.str_nbr
where s.[etl_log_id] = @etl_log_id
create index ix_tmp_addr_chksum on #staging_kiosk(addr_chksum)

-- strip out the distinct chksums
IF (Object_ID('tempdb..#addr_chksum') IS NOT NULL) DROP TABLE #addr_chksum
select distinct addr_chksum
into #addr_chksum
from #staging_kiosk
create index ix_tmp_addr_chksum on #addr_chksum(addr_chksum)

IF (Object_ID('tempdb..#rad') IS NOT NULL) DROP TABLE #rad
select rad.raw_addr_id,
	rad.addr_chksum,
	isnull(rad.addr_ln_1_txt,'') addr_ln_1_txt,
	isnull(rad.addr_ln_2_txt, '') addr_ln_2_txt,
	isnull(rad.apt_unit_nbr, '') apt_unit_nbr,
	isnull(rad.cty_nm, '') cty_nm,
	isnull(rad.st_prvnc_txt, '') st_prvnc_txt,
	isnull(rad.pstl_cd,'') pstl_cd,
	isnull(rad.cntry_txt,'') cntry_txt,
	isnull(rad.drvd_mail_stat_cd, '') drvd_mail_stat_cd,
	isnull(rad.ksk_sndr_snd_mail_cd, '') ksk_sndr_snd_mail_cd,
--	isnull(rad.mail_opt_in_dt, @null_date) mail_opt_in_dt,
	isnull(rad.drvd_cntry_abbrv, '') drvd_cntry_abbrv,
	-- crm data so these better be null
	isnull(rad.crm_snd_mail_cd, '') crm_snd_mail_cd,
	isnull(rad.crm_mail_opt_in_cd, '') crm_mail_opt_in_cd
into #rad
from #addr_chksum a
	join dw.dbo.raw_addr_dim rad with (nolock)
	on rad.addr_chksum = a.addr_chksum
create index ix_rad_addr_chksum on #rad(addr_chksum)

truncate table GuestLoad_Pull_Raw_Kiosk_Addresses

insert into GuestLoad_Pull_Raw_Kiosk_Addresses (
	KSK_REGIS_STG_ID,
	SNDR_SND_MAIL_CD, DRVD_MAIL_STAT_CD, --MAIL_OPT_IN_DT,
	SNDR_ADDR_LN_1_TXT, SNDR_ADDR_LN_2_TXT, SNDR_APT_UNIT_NBR, SNDR_CTY_NM, SNDR_PSTL_CD, SNDR_ST_PRVNC_TXT, SNDR_CNTRY_TXT,
	DRVD_CNTRY_ABBRV,
	addr_chksum,
	raw_addr_id)
select
	distinct s.KSK_REGIS_STG_ID,
	s.SNDR_SND_MAIL_CD, s.DRVD_MAIL_STAT_CD, --s.MAIL_OPT_IN_DT, 
	s.SNDR_ADDR_LN_1_TXT, s.SNDR_ADDR_LN_2_TXT, s.SNDR_APT_UNIT_NBR, s.SNDR_CTY_NM, s.SNDR_PSTL_CD, s.SNDR_ST_PRVNC_TXT, s.SNDR_CNTRY_TXT,
	s.DRVD_CNTRY_ABBRV,
	s.addr_chksum,
	r.raw_addr_id
from #staging_kiosk s
	left join #rad r with (nolock)
	on r.addr_chksum = s.addr_chksum
	and r.addr_ln_1_txt = s.sndr_addr_ln_1_txt
	and r.addr_ln_2_txt = s.sndr_addr_ln_2_txt
	and r.apt_unit_nbr = s.sndr_apt_unit_nbr
	and r.cty_nm = s.sndr_cty_nm
	and r.st_prvnc_txt = s.sndr_st_prvnc_txt
	and r.pstl_cd = s.sndr_pstl_cd
	and r.cntry_txt = s.sndr_cntry_txt
	and r.DRVD_MAIL_STAT_CD = s.DRVD_MAIL_STAT_CD
--	and r.MAIL_OPT_IN_DT = s.MAIL_OPT_IN_DT
	and r.DRVD_CNTRY_ABBRV = s.DRVD_CNTRY_ABBRV

	and r.ksk_sndr_snd_mail_cd = s.SNDR_SND_MAIL_CD
	and r.crm_snd_mail_cd = s.CRM_SND_MAIL_CD
	and r.crm_mail_opt_in_cd = s.CRM_MAIL_OPT_IN_CD
END
```

