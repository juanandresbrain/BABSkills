# dbo.spdavetestproc

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spdavetestproc"]
    dbo_spGuestLoad_CRM_Bypass_Phys_Recleansing(["dbo.spGuestLoad_CRM_Bypass_Phys_Recleansing"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.spGuestLoad_CRM_Bypass_Phys_Recleansing |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spdavetestproc](@etl_log_id int, @etl_evnt_id int)
AS
BEGIN
-- SET NOCOUNT ON added to prevent extra result sets from
-- interfering with SELECT statements.
SET NOCOUNT ON

------select top 1 etl_log_id from dwstaging.dbo.load_rec_id_cntrl with (nolock)
--declare @etl_log_id int
--declare @etl_evnt_id int
--set @etl_log_id = 123
--set @etl_evnt_id = 123

exec dw.dbo.spGuestLoad_CRM_Bypass_Phys_Recleansing @etl_log_id, @etl_evnt_id

end

dbo,spGuestLoad_Build_GST_SUM_FACT,-- =============================================================================================================
-- Name: spGuestLoad_Build_GST_SUM_FACT
--
-- Description:	
--		Builds a guest's tkf facts.  this code can be used after a guest load run or the entire clnsd_gst_dim table 
--		can be trunc'd and then refreshed because this code looks for missing clnsd_gst_ids
--
-- Input:
--		@etl_log_id				int	
--			last guest load to touch this, used for logging.  if truncing the table, any int will do
--
--		@etl_evnt_id			int			
--			last guest load to touch this, used for logging.  if truncing the table, any int will do
--
-- Output: 
--		data will be loaded into dw.dbo.gst_sum_fact
--
-- Dependencies: 
--
-- EXAMPLE:
--		exec dw.dbo.spGuestLoad_Build_GST_SUM_FACT -1, -1
--
-- Revision History
--		Name:			Date:			Comments:
--		Dave Rice		7/19/2010		created
-- =============================================================================================================
CREATE PROCEDURE [dbo].[spGuestLoad_Build_GST_SUM_FACT](@etl_log_id int, @etl_evnt_id int)
AS
BEGIN
-- SET NOCOUNT ON added to prevent extra result sets from
-- interfering with SELECT statements.
SET NOCOUNT ON;

--exec dbo.usp_Build_GST_SUM_FACT 11, 22
--declare @etl_log_id int
--declare @etl_evnt_id int
--set @etl_log_id = 1
--set @etl_evnt_id = 1


-- get today's date_key
declare @date_key int
set @date_key = (select date_key from dw.dbo.date_dim where actual_date = cast(convert(varchar, getdate(), 101) as datetime))

-- look for any missing guests, typically these will come from the latest guestload run
IF (Object_ID('tempdb..#guests') IS NOT NULL) DROP TABLE #guests
select distinct b.clnsd_gst_id
into #guests
from tkf_clnsd_gst_brdg b with (nolock) 
	left join gst_sum_fact gsf with (nolock) 
	on gsf.clnsd_gst_id = b.clnsd_gst_id
where gsf.clnsd_gst_id is null
	and b.clnsd_gst_id >= 0


--IF (Object_ID('tempdb..#guests') IS NOT NULL) DROP TABLE #guests
--select top 10000 clnsd_gst_id
--into #guests
--from (
--	select distinct clnsd_gst_id
--	from (
--		select top 20000 clnsd_gst_id 
--		from tkf_clnsd_gst_brdg
--		where clnsd_gst_id >= 0
--		order by tkf_id desc
--	) d
--	) b
--
--create index ix_guests on #guests(clnsd_gst_id) with FILLFACTOR = 100



--CREATE TABLE [dbo].[#gsf](
--	[CLNSD_GST_ID] [int] NOT NULL,
--	[CLNSD_ADDR_ID] [int] NOT NULL,
--	[FRST_STR_VST_DT_ID] [int] NOT NULL,
--	[SCND_STR_VST_DT_ID] [int] NOT NULL,
--	[THRD_STR_VST_DT_ID] [int] NOT NULL,
--	[LAST_STR_VST_DT_ID] [int] NOT NULL,
--	[GST_SUM_FACT_UPDT_DT_ID] [int] NOT NULL,
--	[DY_INTVL_FRST_SCND_VST_CNT] [int] NULL,
--	[DY_INTVL_SCND_THRD_VST_CNT] [int] NULL,
--	[NEW_VS_RPT_CD] [char](1) NULL,
--	[TTL_VST_CNT] [int] NULL,
--	[MNTH_RCNCY_CNT] [int] NULL,
--	[MNTH_01_03_VST_CNT] [int] NULL,
--	[MNTH_04_06_VST_CNT] [int] NULL,
--	[MNTH_07_09_VST_CNT] [int] NULL,
--	[MNTH_10_12_VST_CNT] [int] NULL,
--	[MNTH_13_15_VST_CNT] [int] NULL,
--	[MNTH_16_18_VST_CNT] [int] NULL,
--	[MNTH_19_21_VST_CNT] [int] NULL,
--	[MNTH_22_24_VST_CNT] [int] NULL,
--	[MNTH_25_PLUS_VST_CNT] [int] NULL,
--	[TTL_ANML_CNT] [int] NULL,
--	[MNTH_01_03_ANML_CNT] [int] NULL,
--	[MNTH_04_06_ANML_CNT] [int] NULL,
--	[MNTH_07_09_ANML_CNT] [int] NULL,
--	[MNTH_10_12_ANML_CNT] [int] NULL,
--	[MNTH_13_15_ANML_CNT] [int] NULL,
--	[MNTH_16_18_ANML_CNT] [int] NULL,
--	[MNTH_19_21_ANML_CNT] [int] NULL,
--	[MNTH_22_24_ANML_CNT] [int] NULL,
--	[MNTH_25_PLUS_ANML_CNT] [int] NULL,
--	[TTL_SWIPE_CNT] [int] NULL,
--	[MNTH_01_03_SWIPES_CNT] [int] NULL,
--	[MNTH_04_06_SWIPES_CNT] [int] NULL,
--	[MNTH_07_09_SWIPES_CNT] [int] NULL,
--	[MNTH_10_12_SWIPES_CNT] [int] NULL,
--	[MNTH_13_15_SWIPES_CNT] [int] NULL,
--	[MNTH_16_18_SWIPES_CNT] [int] NULL,
--	[MNTH_19_21_SWIPES_CNT] [int] NULL,
--	[MNTH_22_24_SWIPES_CNT] [int] NULL,
--	[MNTH_25_PLUS_SWIPES_CNT] [int] NULL,
--	[CLNSD_GST_AGE_NBR] [varchar](20) NULL,
--	[GNDR_CD] [varchar](20) NULL,
--	[INS_DT] [datetime] NOT NULL,
--	[ETL_LOG_ID] [int] NOT NULL,
--	[ETL_EVNT_ID] [int] NOT NULL
--)
--CREATE TABLE [dbo].[#gsf_new](
--	[CLNSD_GST_ID] [int] NOT NULL,
--	[CLNSD_ADDR_ID] [int] NOT NULL,
--	[FRST_STR_VST_DT_ID] [int] NOT NULL,
--	[SCND_STR_VST_DT_ID] [int] NOT NULL,
--	[THRD_STR_VST_DT_ID] [int] NOT NULL,
--	[LAST_STR_VST_DT_ID] [int] NOT NULL,
--	[GST_SUM_FACT_UPDT_DT_ID] [int] NOT NULL,
--	[DY_INTVL_FRST_SCND_VST_CNT] [int] NULL,
--	[DY_INTVL_SCND_THRD_VST_CNT] [int] NULL,
--	[NEW_VS_RPT_CD] [char](1) NULL,
--	[TTL_VST_CNT] [int] NULL,
--	[MNTH_RCNCY_CNT] [int] NULL,
--	[MNTH_01_03_VST_CNT] [int] NULL,
--	[MNTH_04_06_VST_CNT] [int] NULL,
--	[MNTH_07_09_VST_CNT] [int] NULL,
--	[MNTH_10_12_VST_CNT] [int] NULL,
--	[MNTH_13_15_VST_CNT] [int] NULL,
--	[MNTH_16_18_VST_CNT] [int] NULL,
--	[MNTH_19_21_VST_CNT] [int] NULL,
--	[MNTH_22_24_VST_CNT] [int] NULL,
--	[MNTH_25_PLUS_VST_CNT] [int] NULL,
--	[TTL_ANML_CNT] [int] NULL,
--	[MNTH_01_03_ANML_CNT] [int] NULL,
--	[MNTH_04_06_ANML_CNT] [int] NULL,
--	[MNTH_07_09_ANML_CNT] [int] NULL,
--	[MNTH_10_12_ANML_CNT] [int] NULL,
--	[MNTH_13_15_ANML_CNT] [int] NULL,
--	[MNTH_16_18_ANML_CNT] [int] NULL,
--	[MNTH_19_21_ANML_CNT] [int] NULL,
--	[MNTH_22_24_ANML_CNT] [int] NULL,
--	[MNTH_25_PLUS_ANML_CNT] [int] NULL,
--	[TTL_SWIPE_CNT] [int] NULL,
--	[MNTH_01_03_SWIPES_CNT] [int] NULL,
--	[MNTH_04_06_SWIPES_CNT] [int] NULL,
--	[MNTH_07_09_SWIPES_CNT] [int] NULL,
--	[MNTH_10_12_SWIPES_CNT] [int] NULL,
--	[MNTH_13_15_SWIPES_CNT] [int] NULL,
--	[MNTH_16_18_SWIPES_CNT] [int] NULL,
--	[MNTH_19_21_SWIPES_CNT] [int] NULL,
--	[MNTH_22_24_SWIPES_CNT] [int] NULL,
--	[MNTH_25_PLUS_SWIPES_CNT] [int] NULL,
--	[CLNSD_GST_AGE_NBR] [varchar](20) NULL,
--	[GNDR_CD] [varchar](20) NULL,
--	[INS_DT] [datetime] NOT NULL,
--	[ETL_LOG_ID] [int] NOT NULL,
--	[ETL_EVNT_ID] [int] NOT NULL
--)
--
--truncate table #gsf
--truncate table #gsf_new
--
--INSERT INTO dw.dbo.gst_sum_fact (
--	CLNSD_GST_ID, CLNSD_ADDR_ID, 
--	FRST_STR_VST_DT_ID, SCND_STR_VST_DT_ID, THRD_STR_VST_DT_ID, 
--	last_STR_VST_DT_ID, 
--	GST_SUM_FACT_UPDT_DT_ID, 
--	DY_INTVL_FRST_SCND_VST_CNT, DY_INTVL_SCND_THRD_VST_CNT, 
--	MNTH_RCNCY_CNT, 
--	NEW_VS_RPT_CD, 
--	TTL_VST_CNT, 
--	MNTH_01_03_VST_CNT, MNTH_04_06_VST_CNT, MNTH_07_09_VST_CNT, MNTH_10_12_VST_CNT, MNTH_13_15_VST_CNT, MNTH_16_18_VST_CNT, MNTH_19_21_VST_CNT, MNTH_22_24_VST_CNT, MNTH_25_PLUS_VST_CNT, 
--	TTL_ANML_CNT, 
--	MNTH_01_03_ANML_CNT, MNTH_04_06_ANML_CNT, MNTH_07_09_ANML_CNT, MNTH_10_12_ANML_CNT, MNTH_13_15_ANML_CNT, MNTH_16_18_ANML_CNT, MNTH_19_21_ANML_CNT, MNTH_22_24_ANML_CNT, MNTH_25_PLUS_ANML_CNT, 
--	TTL_SWIPE_CNT, 
--	MNTH_01_03_SWIPES_CNT, MNTH_04_06_SWIPES_CNT, MNTH_07_09_SWIPES_CNT, MNTH_10_12_SWIPES_CNT, MNTH_13_15_SWIPES_CNT, MNTH_16_18_SWIPES_CNT, MNTH_19_21_SWIPES_CNT, MNTH_22_24_SWIPES_CNT, MNTH_25_PLUS_SWIPES_CNT, 
--	CLNSD_GST_AGE_NBR, GNDR_CD, INS_DT, ETL_LOG_ID,ETL_EVNT_ID)
--SELECT 
--	tkf.clnsd_gst_id, 
--	tkf.clnsd_addr_id, 
--	IsNull(vst_1.dt_id, -1) as frst_str_vst_dt_id, 
--	IsNull(vst_2.dt_id, -1) as scnd_str_vst_dt_id, 
--	IsNull(vst_3.dt_id, -1) as thrd_str_vst_dt_id, 
--	IsNull(visits.dt_id, -1) as last_str_vst_dt_id, 
--	@date_key as gst_sum_fact_upd_dt_id, 
--
--	CASE WHEN vst_2.dt_id IS NULL THEN 0 ELSE IsNull(vst_2.dt_id, 0) - IsNull(vst_1.dt_id, 0) END as dy_intrvl_frst_scnd_vst_cnt, 
--	CASE WHEN vst_3.dt_id IS NULL THEN 0 ELSE IsNull(vst_3.dt_id, 0) - IsNull(vst_2.dt_id, 0) END as dy_intrvl_scnd_thrd_vst_cnt, 
--
--	CASE 
--		WHEN visits.dt_id IS NULL THEN 0 
--		WHEN visits.dt_id = -1 THEN 999999
--		ELSE DateDiff(MM, visits.dt, getdate()) 
--	END as mnth_rcncy_cnt, 
--
--	CASE WHEN visits.cnt > 1 THEN 'R' ELSE 'F' END as new_vs_rpt_ind, 
--	
--	visits.cnt, 
--	visits.m_01_03_cnt, 
--	visits.m_04_06_cnt, 
--	visits.m_07_09_cnt,
--	visits.m_10_12_cnt,
--	visits.m_13_15_cnt,
--	visits.m_16_18_cnt,
--	visits.m_19_21_cnt,
--	visits.m_22_24_cnt,
--	visits.m_25_plus_cnt,
--
--	animals.cnt, 
--	animals.m_01_03_cnt, 
--	animals.m_04_06_cnt,
--	animals.m_07_09_cnt,
--	animals.m_10_12_cnt,
--	animals.m_13_15_cnt,
--	animals.m_16_18_cnt,
--	animals.m_19_21_cnt,
--	animals.m_22_24_cnt,
--	animals.m_25_plus_cnt,
--
--	swipes.cnt,
--	swipes.m_01_03_cnt,
--	swipes.m_04_06_cnt,
--	swipes.m_07_09_cnt,
--	swipes.m_10_12_cnt,
--	swipes.m_13_15_cnt,
--	swipes.m_16_18_cnt,
--	swipes.m_19_21_cnt,
--	swipes.m_22_24_cnt,
--	swipes.m_25_plus_cnt,
--
--	tkf.gst_age as clnsd_gst_age_nbr, 
--	tkf.gndr_cd as gndr_cd, 
--	getdate() as ins_dt, 
--	@etl_log_id as etl_log_id,
--	@etl_evnt_id as etl_evnt_id
--from
--	(
--	SELECT DISTINCT 
--		b.clnsd_gst_id, 
--		cgd.clnsd_addr_id, 
--		cast(((datediff(dy, cgd.brth_dt, getdate())/365.25)) as int) as gst_age, 
--		cgd.gndr_cd 
--	FROM #guests g
--		INNER JOIN dw.dbo.tkf_clnsd_gst_brdg b with (nolock)
--		on b.clnsd_gst_id = g.clnsd_gst_id
--		INNER JOIN dw.dbo.clnsd_gst_dim cgd with (nolock)
--		ON cgd.clnsd_gst_id = g.clnsd_gst_id 
--	WHERE b.clnsd_gst_id >= 0
--	) tkf
---- ******************************************************
----	INNER JOIN dw.dbo.date_dim dd with (nolock)
----	ON dd.actual_date = cast(convert(varchar, getdate(), 101) as datetime)
---- ******************************************************
--	LEFT OUTER JOIN (
--		SELECT DISTINCT 
--			b.clnsd_gst_id, 
--			dt_id, 
--			DENSE_RANK() OVER (PARTITION BY b.clnsd_gst_id ORDER BY dt_id) as rnk
--		FROM #guests g
--			INNER JOIN dw.dbo.tkf_clnsd_gst_brdg b with (nolock)
--			on b.clnsd_gst_id = g.clnsd_gst_id
--			INNER JOIN dw.dbo.trn_ksk_fact tkf with (nolock) 
--			ON tkf.tkf_id = b.tkf_id
--		WHERE dt_id > 0
--	) vst_1
--	ON tkf.clnsd_gst_id = vst_1.clnsd_gst_id 
--	AND vst_1.rnk = 1
---- ******************************************************
--	LEFT OUTER JOIN (
--		SELECT DISTINCT 
--			b.clnsd_gst_id, 
--			dt_id, 
--			DENSE_RANK() OVER (PARTITION BY b.clnsd_gst_id ORDER BY dt_id) as rnk
--			FROM #guests g
--				INNER JOIN dw.dbo.tkf_clnsd_gst_brdg b with (nolock)
--				on b.clnsd_gst_id = g.clnsd_gst_id
--				INNER JOIN dw.dbo.trn_ksk_fact tkf with (nolock) 
--				ON tkf.tkf_id = b.tkf_id
--		WHERE dt_id > 0
--	) vst_2
--	ON tkf.clnsd_gst_id = vst_2.clnsd_gst_id 
--	AND vst_2.rnk = 2
---- ******************************************************
--	LEFT OUTER JOIN (
--		SELECT DISTINCT 
--			b.clnsd_gst_id, 
--			dt_id, 
--			DENSE_RANK() OVER (PARTITION BY b.clnsd_gst_id ORDER BY dt_id) as rnk
--		FROM #guests g
--			INNER JOIN dw.dbo.tkf_clnsd_gst_brdg b with (nolock)
--			on b.clnsd_gst_id = g.clnsd_gst_id
--			INNER JOIN dw.dbo.trn_ksk_fact tkf with (nolock) 
--			ON tkf.tkf_id = b.tkf_id
--		WHERE dt_id > 0
--	) vst_3
--	ON tkf.clnsd_gst_id = vst_3.clnsd_gst_id 
--	AND vst_3.rnk = 3
---- ******************************************************
--	-- visits		distinct store, date per guest
--	LEFT OUTER JOIN (
--		SELECT 
--			d.clnsd_gst_id, 
--			MAX(d.dt_id) as dt_id, 
--			MAX(d.actual_date) as dt,
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 00 and 03 THEN 1 ELSE 0 END) as m_01_03_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 04 and 06 THEN 1 ELSE 0 END) as m_04_06_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 07 and 09 THEN 1 ELSE 0 END) as m_07_09_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 10 and 12 THEN 1 ELSE 0 END) as m_10_12_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 13 and 15 THEN 1 ELSE 0 END) as m_13_15_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 16 and 18 THEN 1 ELSE 0 END) as m_16_18_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 19 and 21 THEN 1 ELSE 0 END) as m_19_21_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 22 and 24 THEN 1 ELSE 0 END) as m_22_24_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) >= 25 THEN 1 ELSE 0 END) as m_25_plus_cnt,
--			count(*) cnt
--		from (
--			select distinct b.clnsd_gst_id, str_id, dt_id, actual_date
--			FROM #guests g
--				INNER JOIN dw.dbo.tkf_clnsd_gst_brdg b with (nolock)
--				on b.clnsd_gst_id = g.clnsd_gst_id
--				INNER JOIN dw.dbo.trn_ksk_fact tkf with (nolock) 
--				ON tkf.tkf_id = b.tkf_id
--				INNER JOIN dw.dbo.date_dim dd with (nolock)
--				ON tkf.dt_id = dd.date_key
--		) d
--		GROUP BY d.clnsd_gst_id
--	) visits
--	ON tkf.clnsd_gst_id = visits.clnsd_gst_id
---- ******************************************************
--	-- animal		distinct date, barcode
--	LEFT OUTER JOIN (
--		SELECT 
--			d.clnsd_gst_id, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 00 and 03 THEN 1 ELSE 0 END) as m_01_03_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 04 and 06 THEN 1 ELSE 0 END) as m_04_06_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 07 and 09 THEN 1 ELSE 0 END) as m_07_09_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 10 and 12 THEN 1 ELSE 0 END) as m_10_12_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 13 and 15 THEN 1 ELSE 0 END) as m_13_15_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 16 and 18 THEN 1 ELSE 0 END) as m_16_18_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 19 and 21 THEN 1 ELSE 0 END) as m_19_21_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) between 22 and 24 THEN 1 ELSE 0 END) as m_22_24_cnt, 
--			SUM(CASE WHEN DateDiff(MM, d.actual_date, getdate()) >= 25 THEN 1 ELSE 0 END) as m_25_plus_cnt,
--			count(*) cnt
--		from (
--			select distinct b.clnsd_gst_id, anml_barcd_nbr, actual_date
--			FROM #guests g
--				INNER JOIN dw.dbo.tkf_clnsd_gst_brdg b with (nolock)
--				on b.clnsd_gst_id = g.clnsd_gst_id
--				INNER JOIN dw.dbo.trn_ksk_fact tkf with (nolock) 
--				ON tkf.tkf_id = b.tkf_id
--				INNER JOIN dw.dbo.date_dim dd with (nolock)
--				ON tkf.dt_id = dd.date_key
--		) d
--		GROUP BY d.clnsd_gst_id
--	) animals
--	ON tkf.clnsd_gst_id = animals.clnsd_gst_id
---- ******************************************************
--	-- swipes		distinct tkf entries - basically, they can swipe the same barcode, or multiple barcodes for that day
--	LEFT OUTER JOIN (
--		SELECT 
--			b.clnsd_gst_id, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) between 00 and 03 THEN 1 ELSE 0 END) as m_01_03_cnt, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) between 04 and 06 THEN 1 ELSE 0 END) as m_04_06_cnt, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) between 07 and 09 THEN 1 ELSE 0 END) as m_07_09_cnt, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) between 10 and 12 THEN 1 ELSE 0 END) as m_10_12_cnt, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) between 13 and 15 THEN 1 ELSE 0 END) as m_13_15_cnt, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) between 16 and 18 THEN 1 ELSE 0 END) as m_16_18_cnt, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) between 19 and 21 THEN 1 ELSE 0 END) as m_19_21_cnt, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) between 22 and 24 THEN 1 ELSE 0 END) as m_22_24_cnt, 
--			SUM(CASE WHEN DateDiff(MM, dd.actual_date, getdate()) >= 25 THEN 1 ELSE 0 END) as m_25_plus_cnt,
--			count(*) cnt
--		FROM #guests g
--			INNER JOIN dw.dbo.tkf_clnsd_gst_brdg b with (nolock)
--			on b.clnsd_gst_id = g.clnsd_gst_id
--			INNER JOIN dw.dbo.trn_ksk_fact tkf with (nolock) 
--			ON tkf.tkf_id = b.tkf_id
--			INNER JOIN dw.dbo.date_dim dd with (nolock)
--			ON tkf.dt_id = dd.date_key
--		GROUP BY b.clnsd_gst_id
--	) swipes
--	ON tkf.clnsd_gst_id = swipes.clnsd_gst_id





--select *
--from #gsf o
--	join #gsf_new n
--	on n.clnsd_gst_id = o.clnsd_gst_id
--where 
--o.CLNSD_ADDR_ID != n.CLNSD_ADDR_ID or 
--o.FRST_STR_VST_DT_ID != n.FRST_STR_VST_DT_ID or 
--o.SCND_STR_VST_DT_ID != n.SCND_STR_VST_DT_ID or 
--o.THRD_STR_VST_DT_ID != n.THRD_STR_VST_DT_ID or 
--o.last_STR_VST_DT_ID != n.last_STR_VST_DT_ID or 
--o.GST_SUM_FACT_UPDT_DT_ID != n.GST_SUM_FACT_UPDT_DT_ID or 
--o.DY_INTVL_FRST_SCND_VST_CNT != n.DY_INTVL_FRST_SCND_VST_CNT or 
--o.DY_INTVL_SCND_THRD_VST_CNT != n.DY_INTVL_SCND_THRD_VST_CNT or 
--o.MNTH_RCNCY_CNT != n.MNTH_RCNCY_CNT or 
--o.NEW_VS_RPT_CD != n.NEW_VS_RPT_CD or 
--o.TTL_VST_CNT != n.TTL_VST_CNT or 
--o.MNTH_01_03_VST_CNT != n.MNTH_01_03_VST_CNT or 
--o.MNTH_04_06_VST_CNT != n.MNTH_04_06_VST_CNT or 
--o.MNTH_07_09_VST_CNT != n.MNTH_07_09_VST_CNT or 
--o.MNTH_10_12_VST_CNT != n.MNTH_10_12_VST_CNT or 
--o.MNTH_13_15_VST_CNT != n.MNTH_13_15_VST_CNT or 
--o.MNTH_16_18_VST_CNT != n.MNTH_16_18_VST_CNT or 
--o.MNTH_19_21_VST_CNT != n.MNTH_19_21_VST_CNT or 
--o.MNTH_22_24_VST_CNT != n.MNTH_22_24_VST_CNT or 
--o.MNTH_25_PLUS_VST_CNT != n.MNTH_25_PLUS_VST_CNT or 
--o.TTL_ANML_CNT != n.TTL_ANML_CNT or 
--o.MNTH_01_03_ANML_CNT != n.MNTH_01_03_ANML_CNT or 
--o.MNTH_04_06_ANML_CNT != n.MNTH_04_06_ANML_CNT or 
--o.MNTH_07_09_ANML_CNT != n.MNTH_07_09_ANML_CNT or 
--o.MNTH_10_12_ANML_CNT != n.MNTH_10_12_ANML_CNT or 
--o.MNTH_13_15_ANML_CNT != n.MNTH_13_15_ANML_CNT or 
--o.MNTH_16_18_ANML_CNT != n.MNTH_16_18_ANML_CNT or 
--o.MNTH_19_21_ANML_CNT != n.MNTH_19_21_ANML_CNT or 
--o.MNTH_22_24_ANML_CNT != n.MNTH_22_24_ANML_CNT or 
--o.MNTH_25_PLUS_ANML_CNT != n.MNTH_25_PLUS_ANML_CNT or 
--o.TTL_SWIPE_CNT != n.TTL_SWIPE_CNT or 
--o.MNTH_01_03_SWIPES_CNT != n.MNTH_01_03_SWIPES_CNT or 
--o.MNTH_04_06_SWIPES_CNT != n.MNTH_04_06_SWIPES_CNT or 
--o.MNTH_07_09_SWIPES_CNT != n.MNTH_07_09_SWIPES_CNT or 
--o.MNTH_10_12_SWIPES_CNT != n.MNTH_10_12_SWIPES_CNT or 
--o.MNTH_13_15_SWIPES_CNT != n.MNTH_13_15_SWIPES_CNT or 
--o.MNTH_16_18_SWIPES_CNT != n.MNTH_16_18_SWIPES_CNT or 
--o.MNTH_19_21_SWIPES_CNT != n.MNTH_19_21_SWIPES_CNT or 
--o.MNTH_22_24_SWIPES_CNT != n.MNTH_22_24_SWIPES_CNT or 
--o.MNTH_25_PLUS_SWIPES_CNT != n.MNTH_25_PLUS_SWIPES_CNT or 
--o.CLNSD_GST_AGE_NBR != n.CLNSD_GST_AGE_NBR or 
--o.GNDR_CD != n.GNDR_CD 



-- *********************************************************************************************************************
-- *********************************************************************************************************************
-- *********************************************************************************************************************
-- *********************************************************************************************************************
-- *********************************************************************************************************************

IF (Object_ID('tempdb..#tkf') IS NOT NULL) DROP TABLE #tkf
-- do not do distincts, we need all of them for the swipes
select 
	cgd.clnsd_gst_id
	, cgd.gndr_cd
	--, cast(((datediff(dy, cgd.brth_dt, getdate())/365.25)) as int) as gst_age
	, dbo.fnComputeDecimalAge(cgd.brth_dt, getdate()) AS gst_age
	, cgd.clnsd_addr_id
	, tkf.str_id
	, tkf.dt_id
	, dd.actual_date
	, anml_barcd_nbr
into #tkf
FROM #guests g
	INNER JOIN dw.dbo.tkf_clnsd_gst_brdg b with (nolock)
	on b.clnsd_gst_id = g.clnsd_gst_id
	INNER JOIN dw.dbo.clnsd_gst_dim cgd with (nolock)
	ON cgd.clnsd_gst_id = g.clnsd_gst_id 
	INNER JOIN dw.dbo.trn_ksk_fact tkf with (nolock) 
	ON tkf.tkf_id = b.tkf_id
	INNER JOIN dw.dbo.date_dim dd with (nolock)
	ON tkf.dt_id = dd.date_key
WHERE dt_id > 0

create index ix_tkf on #tkf (clnsd_gst_id)

INSERT INTO dw.dbo.gst_sum_fact (
	CLNSD_GST_ID
	, CLNSD_ADDR_ID
	, FRST_STR_VST_DT_ID
	, SCND_STR_VST_DT_ID
	, THRD_STR_VST_DT_ID
	, last_STR_VST_DT_ID
	, GST_SUM_FACT_UPDT_DT_ID
	, DY_INTVL_FRST_SCND_VST_CNT
	, DY_INTVL_SCND_THRD_VST_CNT
	, MNTH_RCNCY_CNT
	, NEW_VS_RPT_CD
	, TTL_VST_CNT
	, MNTH_01_03_VST_CNT
	, MNTH_04_06_VST_CNT
	, MNTH_07_09_VST_CNT
	, MNTH_10_12_VST_CNT
	, MNTH_13_15_VST_CNT
	, MNTH_16_18_VST_CNT
	, MNTH_19_21_VST_CNT
	, MNTH_22_24_VST_CNT
	, MNTH_25_PLUS_VST_CNT
	, TTL_ANML_CNT
	, MNTH_01_03_ANML_CNT
	, MNTH_04_06_ANML_CNT
	, MNTH_07_09_ANML_CNT
	, MNTH_10_12_ANML_CNT
	, MNTH_13_15_ANML_CNT
	, MNTH_16_18_ANML_CNT
	, MNTH_19_21_ANML_CNT
	, MNTH_22_24_ANML_CNT
	, MNTH_25_PLUS_ANML_CNT
	, TTL_SWIPE_CNT
	, MNTH_01_03_SWIPES_CNT
	, MNTH_04_06_SWIPES_CNT
	, MNTH_07_09_SWIPES_CNT
	, MNTH_10_12_SWIPES_CNT
	, MNTH_13_15_SWIPES_CNT
	, MNTH_16_18_SWIPES_CNT
	, MNTH_19_21_SWIPES_CNT
	, MNTH_22_24_SWIPES_CNT
	, MNTH_25_PLUS_SWIPES_CNT
	, CLNSD_GST_AGE_NBR
	, GNDR_CD
	, INS_DT
	, ETL_LOG_ID,ETL_EVNT_ID)
SELECT 
	tkf.clnsd_gst_id, 
	tkf.clnsd_addr_id, 
	IsNull(vst_1.dt_id, -1) as frst_str_vst_dt_id, 
	IsNull(vst_2.dt_id, -1) as scnd_str_vst_dt_id, 
	IsNull(vst_3.dt_id, -1) as thrd_str_vst_dt_id, 
	IsNull(visits.dt_id, -1) as last_str_vst_dt_id, 
	@date_key as gst_sum_fact_upd_dt_id, 

	CASE WHEN vst_2.dt_id IS NULL THEN 0 ELSE IsNull(vst_2.dt_id, 0) - IsNull(vst_1.dt_id, 0) END as dy_intrvl_frst_scnd_vst_cnt, 
	CASE WHEN vst_3.dt_id IS NULL THEN 0 ELSE IsNull(vst_3.dt_id, 0) - IsNull(vst_2.dt_id, 0) END as dy_intrvl_scnd_thrd_vst_cnt, 

	CASE 
		WHEN visits.dt_id IS NULL THEN 0 
		WHEN visits.dt_id = -1 THEN 999999
		ELSE DateDiff(MM, visits.dt, getdate()) 
	END as mnth_rcncy_cnt, 

	CASE WHEN visits.cnt > 1 THEN 'R' ELSE 'F' END as new_vs_rpt_ind, 
	
	visits.cnt, 
	visits.m_01_03_cnt, 
	visits.m_04_06_cnt, 
	visits.m_07_09_cnt,
	visits.m_10_12_cnt,
	visits.m_13_15_cnt,
	visits.m_16_18_cnt,
	visits.m_19_21_cnt,
	visits.m_22_24_cnt,
	visits.m_25_plus_cnt,

	animals.cnt, 
	animals.m_01_03_cnt, 
	animals.m_04_06_cnt,
	animals.m_07_09_cnt,
	animals.m_10_12_cnt,
	animals.m_13_15_cnt,
	animals.m_16_18_cnt,
	animals.m_19_21_cnt,
	animals.m_22_24_cnt,
	animals.m_25_plus_cnt,

	swipes.cnt,
	swipes.m_01_03_cnt,
	swipes.m_04_06_cnt,
	swipes.m_07_09_cnt,
	swipes.m_10_12_cnt,
	swipes.m_13_15_cnt,
	swipes.m_16_18_cnt,
	swipes.m_19_21_cnt,
	swipes.m_22_24_cnt,
	swipes.m_25_plus_cnt,

	tkf.gst_age as clnsd_gst_age_nbr, 
	tkf.gndr_cd as gndr_cd, 
	getdate() as ins_dt, 
	@etl_log_id as etl_log_id,
	@etl_evnt_id as etl_evnt_id
from
	(
	SELECT DISTINCT 
		clnsd_gst_id, 
		clnsd_addr_id, 
		gst_age, 
		gndr_cd 
	FROM #tkf
	) tkf
-- ******************************************************
--	INNER JOIN dw.dbo.date_dim dd with (nolock)
--	ON dd.actual_date = cast(convert(varchar, getdate(), 101) as datetime)
-- ******************************************************
	LEFT OUTER JOIN (
		SELECT DISTINCT 
			clnsd_gst_id, 
			dt_id, 
			DENSE_RANK() OVER (PARTITION BY clnsd_gst_id ORDER BY dt_id) as rnk
		FROM #tkf
	) vst_1
	ON tkf.clnsd_gst_id = vst_1.clnsd_gst_id 
	AND vst_1.rnk = 1
-- ******************************************************
	LEFT OUTER JOIN (
		SELECT DISTINCT 
			clnsd_gst_id, 
			dt_id, 
			DENSE_RANK() OVER (PARTITION BY clnsd_gst_id ORDER BY dt_id) as rnk
			FROM #tkf
	) vst_2
	ON tkf.clnsd_gst_id = vst_2.clnsd_gst_id 
	AND vst_2.rnk = 2
-- ******************************************************
	LEFT OUTER JOIN (
		SELECT DISTINCT 
			clnsd_gst_id, 
			dt_id, 
			DENSE_RANK() OVER (PARTITION BY clnsd_gst_id ORDER BY dt_id) as rnk
		FROM #tkf
	) vst_3
	ON tkf.clnsd_gst_id = vst_3.clnsd_gst_id 
	AND vst_3.rnk = 3
-- ******************************************************
	-- visits		distinct store, date per guest
	LEFT OUTER JOIN (
		SELECT 
			clnsd_gst_id, 
			MAX(dt_id) as dt_id, 
			MAX(actual_date) as dt,
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 00 and 03 THEN 1 ELSE 0 END) as m_01_03_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 04 and 06 THEN 1 ELSE 0 END) as m_04_06_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 07 and 09 THEN 1 ELSE 0 END) as m_07_09_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 10 and 12 THEN 1 ELSE 0 END) as m_10_12_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 13 and 15 THEN 1 ELSE 0 END) as m_13_15_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 16 and 18 THEN 1 ELSE 0 END) as m_16_18_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 19 and 21 THEN 1 ELSE 0 END) as m_19_21_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 22 and 24 THEN 1 ELSE 0 END) as m_22_24_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) >= 25 THEN 1 ELSE 0 END) as m_25_plus_cnt,
			count(*) cnt
		from (
			select distinct clnsd_gst_id, str_id, dt_id, actual_date
			FROM #tkf
		) d
		GROUP BY clnsd_gst_id
	) visits
	ON tkf.clnsd_gst_id = visits.clnsd_gst_id
-- ******************************************************
	-- animal		distinct date, barcode
	LEFT OUTER JOIN (
		SELECT 
			clnsd_gst_id, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 00 and 03 THEN 1 ELSE 0 END) as m_01_03_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 04 and 06 THEN 1 ELSE 0 END) as m_04_06_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 07 and 09 THEN 1 ELSE 0 END) as m_07_09_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 10 and 12 THEN 1 ELSE 0 END) as m_10_12_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 13 and 15 THEN 1 ELSE 0 END) as m_13_15_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 16 and 18 THEN 1 ELSE 0 END) as m_16_18_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 19 and 21 THEN 1 ELSE 0 END) as m_19_21_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 22 and 24 THEN 1 ELSE 0 END) as m_22_24_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) >= 25 THEN 1 ELSE 0 END) as m_25_plus_cnt,
			count(*) cnt
		from (
			select distinct clnsd_gst_id, anml_barcd_nbr, actual_date
			FROM #tkf
		) d
		GROUP BY clnsd_gst_id
	) animals
	ON tkf.clnsd_gst_id = animals.clnsd_gst_id
-- ******************************************************
	-- swipes		distinct tkf entries - basically, they can swipe the same barcode, or multiple barcodes for that day
	LEFT OUTER JOIN (
		SELECT 
			clnsd_gst_id, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 00 and 03 THEN 1 ELSE 0 END) as m_01_03_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 04 and 06 THEN 1 ELSE 0 END) as m_04_06_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 07 and 09 THEN 1 ELSE 0 END) as m_07_09_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 10 and 12 THEN 1 ELSE 0 END) as m_10_12_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 13 and 15 THEN 1 ELSE 0 END) as m_13_15_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 16 and 18 THEN 1 ELSE 0 END) as m_16_18_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 19 and 21 THEN 1 ELSE 0 END) as m_19_21_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) between 22 and 24 THEN 1 ELSE 0 END) as m_22_24_cnt, 
			SUM(CASE WHEN DateDiff(MM, actual_date, getdate()) >= 25 THEN 1 ELSE 0 END) as m_25_plus_cnt,
			count(*) cnt
		FROM #tkf
		GROUP BY clnsd_gst_id
	) swipes
	ON tkf.clnsd_gst_id = swipes.clnsd_gst_id

END
 
dbo,dt_verstamp006,/*
**	This procedure returns the version number of the stored
**    procedures used by legacy versions of the Microsoft
**	Visual Database Tools.  Version is 7.0.00.
*/
create procedure dbo.dt_verstamp006
as
	select 7000
```

