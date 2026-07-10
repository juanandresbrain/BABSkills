# dbo.spEmail_ET_Download_Process

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmail_ET_Download_Process"]
    dbo_ET_Bounce(["dbo.ET_Bounce"]) --> SP
    dbo_ET_Clicks(["dbo.ET_Clicks"]) --> SP
    dbo_ET_Conversions(["dbo.ET_Conversions"]) --> SP
    dbo_ET_Opens(["dbo.ET_Opens"]) --> SP
    dbo_ET_SendJobs(["dbo.ET_SendJobs"]) --> SP
    dbo_ET_Sent(["dbo.ET_Sent"]) --> SP
    dbo_ET_Surveys(["dbo.ET_Surveys"]) --> SP
    dbo_ET_Unsubs(["dbo.ET_Unsubs"]) --> SP
    audit_spEmail_Insert_ET_LoadLog(["audit.spEmail_Insert_ET_LoadLog"]) --> SP
    dbo_tmp_edin_bounce_import(["dbo.tmp_edin_bounce_import"]) --> SP
    dbo_tmp_edin_clicks_import(["dbo.tmp_edin_clicks_import"]) --> SP
    dbo_tmp_edin_conversions_import(["dbo.tmp_edin_conversions_import"]) --> SP
    dbo_tmp_edin_opens_import(["dbo.tmp_edin_opens_import"]) --> SP
    dbo_tmp_edin_sendjobs_import(["dbo.tmp_edin_sendjobs_import"]) --> SP
    dbo_tmp_edin_sent_import(["dbo.tmp_edin_sent_import"]) --> SP
    dbo_tmp_edin_surveys_import(["dbo.tmp_edin_surveys_import"]) --> SP
    dbo_tmp_edin_unsubs_import(["dbo.tmp_edin_unsubs_import"]) --> SP
    dbo_xp_cmdshell(["dbo.xp_cmdshell"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ET_Bounce |
| dbo.ET_Clicks |
| dbo.ET_Conversions |
| dbo.ET_Opens |
| dbo.ET_SendJobs |
| dbo.ET_Sent |
| dbo.ET_Surveys |
| dbo.ET_Unsubs |
| audit.spEmail_Insert_ET_LoadLog |
| dbo.tmp_edin_bounce_import |
| dbo.tmp_edin_clicks_import |
| dbo.tmp_edin_conversions_import |
| dbo.tmp_edin_opens_import |
| dbo.tmp_edin_sendjobs_import |
| dbo.tmp_edin_sent_import |
| dbo.tmp_edin_surveys_import |
| dbo.tmp_edin_unsubs_import |
| dbo.xp_cmdshell |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmail_ET_Download_Process]
	@Path VARCHAR(100),
	@zipfilename VARCHAR(50)
as

/*
--Test
exec dw.dbo.spEmail_ET_Download_Process '\\papamart\responsys\ExactTarget\Download\','Test.zip'
*/

declare @filename VARCHAR(1000)
DECLARE @cmd VARCHAR(800) -- stores the dynamically created DOS command
declare @RowCnt int
declare @load_id int

IF (Object_ID('tempdb.dbo.#FilesToProcess') IS NOT NULL) DROP TABLE #FilesToProcess
CREATE TABLE #FilesToProcess
(
FilesToProcess VARCHAR(7000)
)

-- Build the command that will list out all of the files in a directory
SELECT @cmd = 'dir ' + @Path + '*.csv /B'

  -- Run the dir command and put the results into a temp table
INSERT INTO #FilesToProcess
EXEC master.dbo.xp_cmdshell @cmd

-- Delete null row
  DELETE
  FROM #FilesToProcess
  WHERE FilesToProcess is null
 
--select * from #FilesToProcess

--BOUNCE files import
select top 1 @filename = FilesToProcess
from #FilesToProcess
where FilesToProcess like 'Bounce%.csv'

/*
--Manual run for bounce file
declare @load_id int
declare @path varchar(100)
declare @filename varchar(50)
declare @zipfilename varchar(50)
declare @cmd VARCHAR(800)

select @path = '\\papamart\responsys\ExactTarget\Download\'
select @filename = 'Bounces.csv'
select @zipfilename = 'BABW_Tracking_20140424.zip'


exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output
	--declare @load_id int
	--exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog 'TestZipFile', 'TestFileName', @load_id output
	--select @load_id
	
	truncate table dw.dbo.tmp_edin_bounce_import
	
	SELECT @cmd = 'bcp dw.dbo.tmp_edin_bounce_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.ESPStaging.dbo.ET_Bounce
	select 
		*,
		@load_id,
		null
	from dw.dbo.tmp_edin_bounce_import
*/


SET @RowCnt = @@ROWCOUNT
while @RowCnt <> 0
begin
	exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output
	--declare @load_id int
	--exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog 'TestZipFile', 'TestFileName', @load_id output
	--select @load_id
	
	truncate table dw.dbo.tmp_edin_bounce_import
	
	SELECT @cmd = 'bcp dw.dbo.tmp_edin_bounce_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.ESPStaging.dbo.ET_Bounce
	select 
		*,
		@load_id,
		null
	from dw.dbo.tmp_edin_bounce_import
	
	delete from #FilesToProcess
	where FilesToProcess = @filename
	
	select @cmd = 'del ' + @path + @filename + ' /Q /F'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	select top 1 @filename = FilesToProcess
	from #FilesToProcess
	where FilesToProcess like 'Bounce%.csv'
	
	SET @RowCnt = @@ROWCOUNT
end

--select * from dw.dbo.tmp_edin_bounce_import


--UNSUBS files import
select top 1 @filename = FilesToProcess
from #FilesToProcess
where FilesToProcess like 'Unsubs%.csv'

SET @RowCnt = @@ROWCOUNT
while @RowCnt <> 0
begin
	exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output
	
	truncate table dw.dbo.tmp_edin_unsubs_import
	
	SELECT @cmd = 'bcp dw.dbo.tmp_edin_unsubs_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.espstaging.dbo.ET_Unsubs
	select
		*,
		@load_id,
		null
	from dw.dbo.tmp_edin_unsubs_import
	
	delete from #FilesToProcess
	where FilesToProcess = @filename
	
	select @cmd = 'del ' + @path + @filename + ' /Q /F'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	select top 1 @filename = FilesToProcess
	from #FilesToProcess
	where FilesToProcess like 'Unsubs%.csv'
	
	SET @RowCnt = @@ROWCOUNT
end

--select * from dw.dbo.tmp_edin_unsubs_import

--OPENS files import
select top 1 @filename = FilesToProcess
from #FilesToProcess
where FilesToProcess like 'Opens%.csv'

SET @RowCnt = @@ROWCOUNT
while @RowCnt <> 0
begin
	exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output
	
	truncate table dw.dbo.tmp_edin_opens_import

	SELECT @cmd = 'bcp dw.dbo.tmp_edin_opens_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.espstaging.dbo.ET_Opens
	select
		*,
		@load_id
	from dw.dbo.tmp_edin_opens_import
	
	delete from #FilesToProcess
	where FilesToProcess = @filename
	
	select @cmd = 'del ' + @path + @filename + ' /Q /F'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	select top 1 @filename = FilesToProcess
	from #FilesToProcess
	where FilesToProcess like 'Opens%.csv'
	
	SET @RowCnt = @@ROWCOUNT
end

--select * from dw.dbo.tmp_edin_opens_import

--CLICKS files import
select top 1 @filename = FilesToProcess
from #FilesToProcess
where FilesToProcess like 'Clicks%.csv'

SET @RowCnt = @@ROWCOUNT
while @RowCnt <> 0
begin
	exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output
	
	truncate table dw.dbo.tmp_edin_clicks_import

	SELECT @cmd = 'bcp dw.dbo.tmp_edin_clicks_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.espstaging.dbo.ET_Clicks
	select
		*,
		@load_id
	from dw.dbo.tmp_edin_clicks_import
	
	delete from #FilesToProcess
	where FilesToProcess = @filename
	
	select @cmd = 'del ' + @path + @filename + ' /Q /F'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	select top 1 @filename = FilesToProcess
	from #FilesToProcess
	where FilesToProcess like 'Clicks%.csv'
	
	SET @RowCnt = @@ROWCOUNT
end

--select * from dw.dbo.tmp_edin_clicks_import

--SENDJOBS files import
select top 1 @filename = FilesToProcess
from #FilesToProcess
where FilesToProcess like 'SendJobs%.csv'

SET @RowCnt = @@ROWCOUNT
while @RowCnt <> 0
begin
	exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output

	truncate table dw.dbo.tmp_edin_sendjobs_import

	SELECT @cmd = 'bcp dw.dbo.tmp_edin_sendjobs_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.espstaging.dbo.ET_SendJobs
	select 
		*,
		@load_id
	from dw.dbo.tmp_edin_sendjobs_import
	
	delete from #FilesToProcess
	where FilesToProcess = @filename
	
	select @cmd = 'del ' + @path + @filename + ' /Q /F'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	select top 1 @filename = FilesToProcess
	from #FilesToProcess
	where FilesToProcess like 'SendJobs%.csv'
	
	SET @RowCnt = @@ROWCOUNT
end

--select * from dw.dbo.tmp_edin_sendjobs_import

--SENT files import
select top 1 @filename = FilesToProcess
from #FilesToProcess
where FilesToProcess like 'Sent%.csv'

SET @RowCnt = @@ROWCOUNT
while @RowCnt <> 0
begin
	exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output

	truncate table dw.dbo.tmp_edin_sent_import

	SELECT @cmd = 'bcp dw.dbo.tmp_edin_sent_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.espstaging.dbo.ET_Sent
	select
		*,
		@load_id
	from dw.dbo.tmp_edin_sent_import
	
	delete from #FilesToProcess
	where FilesToProcess = @filename
	
	select @cmd = 'del ' + @path + @filename + ' /Q /F'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	select top 1 @filename = FilesToProcess
	from #FilesToProcess
	where FilesToProcess like 'Sent%.csv'
	
	SET @RowCnt = @@ROWCOUNT
end

--select * from dw.dbo.tmp_edin_sent_import

--CONVERSIONS files import
select top 1 @filename = FilesToProcess
from #FilesToProcess
where FilesToProcess like 'Conversions%.csv'

SET @RowCnt = @@ROWCOUNT
while @RowCnt <> 0
begin
	exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output

	truncate table dw.dbo.tmp_edin_conversions_import

	SELECT @cmd = 'bcp dw.dbo.tmp_edin_conversions_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.espstaging.dbo.ET_Conversions
	select
		*,
		@load_id
	from dw.dbo.tmp_edin_conversions_import
	
	delete from #FilesToProcess
	where FilesToProcess = @filename
	
	select @cmd = 'del ' + @path + @filename + ' /Q /F'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	select top 1 @filename = FilesToProcess
	from #FilesToProcess
	where FilesToProcess like 'Conversions%.csv'
	
	SET @RowCnt = @@ROWCOUNT
end

--select * from dw.dbo.tmp_edin_conversions_import

--SURVEYS files import
select top 1 @filename = FilesToProcess
from #FilesToProcess
where FilesToProcess like 'Surveys%.csv'

SET @RowCnt = @@ROWCOUNT
while @RowCnt <> 0
begin
	exec kodiak.espstaging.audit.spEmail_Insert_ET_LoadLog @zipfilename, @filename, @load_id output

	truncate table dw.dbo.tmp_edin_surveys_import

	SELECT @cmd = 'bcp dw.dbo.tmp_edin_surveys_import in "' + @path + @filename + '" -t, -c -F 2 -T'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	insert into kodiak.espstaging.dbo.ET_Surveys
	select
		*,
		@load_id
	from dw.dbo.tmp_edin_surveys_import
	
	delete from #FilesToProcess
	where FilesToProcess = @filename
	
	select @cmd = 'del ' + @path + @filename + ' /Q /F'
	--select @cmd
	EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
	
	select top 1 @filename = FilesToProcess
	from #FilesToProcess
	where FilesToProcess like 'Surveys%.csv'
	
	SET @RowCnt = @@ROWCOUNT
end

--select * from dw.dbo.tmp_edin_surveys_import


dbo,spMetricsBuild_history,--Text
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--02/12/2007	only reloads specific metric_dim_keys


/****** Object:  Stored Procedure dbo.spMetricsBuild    Script Date: 3/23/2005 ******/

--EXEC spMetricsBuild_new '12/29/2002','1/25/2003'
-- select min(actual_date), max(actual_date) from date_dim where fiscal_year=2003 and fiscal_period = 1

CREATE PROCEDURE [dbo].[spMetricsBuild_history]
	/* ===== ARGUMENTS ===== */
	@StartDate 	datetime = NULL, 
	@EndDate 	datetime = NULL,
	@bDebugFl	bit = 0		-- Debug Flag

AS

SET NOCOUNT ON

/* ===== DECLARATIONS ===== */
DECLARE 
	@iRowCnt	INT		-- Used to save @@rowcount
	,@iErrNbr	INT		-- Used to save @@error
	,@iRtnCd	INT		-- Return code of procedure
	,@dStartDt	DATETIME	-- Time this procedure started
	,@dStopDt	DATETIME	-- Time this procedure ended
	,@SQLi 		VARCHAR(8000)
	,@sDateKeyList	VARCHAR(8000) 
	,@curDay 	char(2)
	,@curMon 	char(2)
	,@curYr 	char(4)
	,@curDate 	datetime
	,@wkCurTY 	int

--	,@StartDate	datetime
--	,@EndDate 	datetime
--	,@bDebugFl	bit

--SET @StartDate = NULL
--SET @EndDate = NULL
--SET @bDebugFl = 0

/* ===== INITIALIZE VARIABLES ===== */
SELECT @iRtnCd	= 0	


/* ============================================================================= */
/* ================================  BEGIN  ==================================== */
/* ============================================================================= */



SET @curDay = datepart(dd,getdate())
SET @curMon = datepart(mm,getdate())
SET @curYr = datepart(yy,getdate())


SET @curDate = cast((@curMon+'/'+@curDay+'/'+@curYr) as Datetime)

--SELECT @StartDate ='11/21/2003'
--SELECT @EndDate ='12/4/2003'
IF @StartDate is NULL
BEGIN
	SELECT @StartDate = dateadd(dd, -14,@curDate)  
	SELECT @EndDate =  dateadd(dd, -1,@curDate) 
END
--select @StartDate,@EndDate


/* ----- DEBUG */
IF @bDebugFl = 1

BEGIN
	PRINT 'KEY INDICATORS ROLLUP'
	PRINT ' '
	PRINT @@SERVERNAME + '/' + DB_Name()
	PRINT 'Procedure Name: ' + Object_Name(@@PROCID)
	PRINT 'Parmameter @StartDate: ' + cast(@StartDate as varchar)
	PRINT 'Parmameter @EndDate: ' + cast(@EndDate as varchar)
	PRINT ' '
END
/***************************************************************/
/*********************  DELETE PAST WEEK **********************/
/***************************************************************/


delete --dbo.metric_facts
from dbo.metric_facts 
where date_key IN (select date_key from dbo.date_dim 
	--WHERE actual_date BETWEEN '11/26/2003' AND '12/1/2003 23:59')				
	where actual_date BETWEEN @StartDate AND @EndDate)
and metric_dim_key in (33,34,35,45,46,47,53,54,55,68,69,70,100,101,102,103,104,105)						


--log------------------------------------------------------------
UPDATE dbo.ld_monitor
SET status = 'complete', process_date = getdate()
WHERE step = 8
-----------------------------------------------------------------

/***************************************************************/
/********************* TRANSACTION ROLLUP  *********************/
/***************************************************************/

IF (Object_ID('work_tmptransrollup') IS NOT NULL) DROP TABLE work_tmptransrollup
SELECT   t.transaction_id
	,t.store_key
	,t.date_key
	,t.register_no
	,t.party_y_n
	,ttd.transaction_type
--	,t.UGA
 	,t.Merchandise_UGA
	,t.Coupon_Amt
	,t.Coupon_Units
	,t.Discounts
-- 	,t.Paid_Outs
	,t.Gift_Card_Sold
	,t.Bear_Buck_Tender
	,t.Gift_Card_Tender
	,t.Tax_Tender
	,t.Cash_Tender
	,t.Check_Tender
	,t.Other_Tender
	,t.Amex_Tender
	,t.Discover_Tender
	,t.MasterCard_Tender
	,t.Visa_Tender
	,t.BuyStuff_Tender
	,t.Reward_Cert_Tender
	,t.Shipping
	,t.Other_Fee
	,t.Donations
	,t.Cub_Cash
	,t.GiftCardDiscounts
	,t.Party_Deposit_Merch
	,t.StuffingAndSupplies
-- 	,t.Merch_Units	
	,t.Units
	,t.Donation_Only
	,t.Gift_Card_Only
	,t.Party_Dep_Only
	,t.Paid_Outs
	,t.Net_Sale
	,t.GAAP_Sale
	,t.Receipt_Ttl
	,(isnull(t.Net_Sale,0) - isnull(Shipping,0)) as ttlHoney

INTO work_tmptransrollup 	
FROM dbo.transaction_summary_facts t
JOIN dbo.store_dim s ON s.store_key = t.store_key
JOIN dbo.date_dim d ON d.date_key = t.date_key
LEFT JOIN dbo.transaction_type_dim ttd ON t.transaction_type_key = ttd.transaction_key
	
WHERE d.actual_date  BETWEEN @StartDate AND @EndDate 
--WHERE d.actual_date BETWEEN '12/8/2005' AND '12/8/2005 23:59'
--AND s.store_id = 3
--AND (t.transaction_line_seq >=0)
--AND (t.product_key <> -18)


	

/* ===== CREATE  INDEX ON TRANS ROLLUP TABLE ===== */

CREATE  CLUSTERED INDEX IX_TMPTrans on work_tmptransrollup (store_key, date_key)
CREATE  INDEX IX_TMPTrans_tranID on work_tmptransrollup (transaction_id, register_no)
--select * from work_tmptransrollup where giftcardonly_y_n = 1

--log------------------------------------------------------------
UPDATE dbo.ld_monitor
SET status = 'complete', process_date = getdate()
WHERE step = 9
-----------------------------------------------------------------

/***************************************************************/
/********************** UNITS BY DEPT **************************/
/***************************************************************/


IF (Object_ID('tempdb.dbo.#tmpunits') IS NOT NULL) DROP TABLE dbo.#tmpunits
SELECT  a.transaction_id,
		a.store_key,
		a.date_key,
		a.register_num,
		/*UNIT COUNTS*/
		sum(isnull(CASE WHEN right(a.department_code,2) = 25 OR right(a.subclass_code,2) = 25
				THEN a.units END,0)) as ttlanimals,	
--		sum(isnull(CASE WHEN a.department IN ('Animals','Dolls','Unstuffed')
--				 OR (a.department = 'Sports Licensing' AND a.subclass = 'Skins')
--				THEN a.units END,0)) as ttlanimals,		
		sum(isnull(CASE WHEN (right(a.department_code,2)  IN (10,15,20,05,30,35,12) and right(subclass_code,2) <> 25) and a.line_object = 100
				THEN a.units END,0)) as ttlnonanimals,		
--		sum(isnull(CASE WHEN a.department IN ('Sports Licensing','Clothes','Clothing','Sounds','Accessories','Footwear','Prestuffed','Human') 
--				AND a.subclass <> 'Skins'
--				THEN a.units END,0)) as ttlnonanimals,
		sum(isnull(CASE WHEN right(department_code,2) NOT IN (25,10,15,20,05,30,35,12) or department_code is null  
				THEN a.units END,0)) as ttlotherunits,
--		sum(isnull(CASE WHEN a.department NOT IN ('Animals','Dolls','Unstuffed','Sports Licensing','Clothes','Clothing','Sounds','Accessories','Footwear','Prestuffed','Human')
--				THEN a.units END,0)) as ttlotherunits,
		sum(isnull(CASE WHEN right(a.department_code,2) = 05 THEN a.units END,0)) as ttlaccessories,
--		sum(isnull(CASE WHEN a.department = 'Accessories' THEN a.units END,0)) as ttlaccessories,
		sum(isnull(CASE WHEN right(a.department_code,2) = 15 THEN a.units END,0)) as ttlshoes,	
--		sum(isnull(CASE WHEN a.department = 'Footwear' THEN a.units END,0)) as ttlshoes,
		sum(isnull(CASE WHEN right(a.department_code,2) = 20 THEN a.units END,0)) as ttlsounds,	
--		sum(isnull(CASE WHEN a.department = 'Sounds' THEN a.units END,0)) as ttlsounds,
		sum(isnull(CASE WHEN a.line_object = 100 THEN a.units END,0)) as ttlunits,
		sum(isnull(CASE WHEN a.line_object IN (294,400,401,402,403,404,410,1625)
				THEN a.units END ,0)) as ttlGiftCardUnits,

		/*UNIT NET AMOUNTS*/
		sum(isnull(CASE WHEN right(a.department_code,2) = 25 OR right(a.subclass_code,2) = 25
				THEN a.unit_net_amount END,0)) as ttlanimalUGA,
--		sum(isnull(CASE WHEN a.department IN ('Animals','Dolls','Unstuffed')
--				 OR (a.department = 'Sports Licensing' AND a.subclass = 'Skins')
--				THEN a.unit_net_amount END,0)) as ttlanimalUGA,
		sum(isnull(CASE WHEN (right(a.department_code,2) IN (10,15,20,05,30,35,12) and right(subclass_code,2) <> 25) and a.line_object = 100
				THEN a.unit_net_amount END,0)) as ttlnonanimalUGA,
--		sum(isnull(CASE WHEN a.department IN ('Sports Licensing','Clothes','Clothing','Sounds','Accessories','Footwear','Prestuffed','Human') 
--				AND a.subclass <> 'Skins'
--				THEN a.unit_net_amount END,0)) as ttlnonanimalUGA,
		sum(isnull(CASE WHEN  right(a.department_code,2) = 15 
				THEN a.unit_net_amount END,0)) as ttlFootwearUGA,
--		sum(isnull(CASE WHEN a.department = 'Footwear' 
--				THEN a.unit_net_amount END,0)) as ttlFootwearUGA,
		sum(isnull(CASE WHEN right(a.department_code,2) = 05 
				THEN a.unit_net_amount END,0)) as ttlAccessoriesUGA,
--		sum(isnull(CASE WHEN a.department = 'Accessories' 
--				THEN a.unit_net_amount END,0)) as ttlAccessoriesUGA,
		sum(isnull(CASE WHEN right(a.department_code,2) = 20  
				THEN a.unit_net_amount END,0)) as ttlSoundsUGA,
--		sum(isnull(CASE WHEN a.department = 'Sounds' 
--				THEN a.unit_net_amount END,0)) as ttlSoundsUGA,

		sum(isnull(CASE WHEN right(a.department_code,2) = 10  
				THEN a.unit_net_amount END,0)) as ttlClothingUGA,
--		sum(isnull(CASE WHEN a.department IN ('Clothes','Clothing')
--				THEN a.unit_net_amount END,0)) as ttlClothingUGA

--		sum(isnull(CASE WHEN a.line_object IN (294,400,401,402,403,404,410,1625)
--				THEN a.unit_net_amount END ,0)) as ttlGiftCardUGA,
--		sum(isnull(CASE WHEN (a.department NOT IN ('Clothes','Clothing','Sounds','Accessories','Footwear') 
--				AND a.subclass <> 'Skins') 
		sum(isnull(CASE WHEN right(department_code,2) NOT IN (25,10,15,20,05,30,35,12) or department_code is null  
				THEN a.unit_net_amount END,0)) as ttlOtherUGA
--				AND a.line_object NOT IN (294,400,401,402,403,404,410,1625)
--				THEN a.unit_net_amount END,0)) as ttlOtherUGA

INTO dbo.#tmpunits	
FROM 
		(
		SELECT  t.transaction_id,
				t.store_key,
				t.date_key,
				t.register_num,
--				p.department,
				p.department_code,
--				p.subclass,
				p.subclass_code,
				lo.line_object,
				sum(isnull(t.units,0)) as units,
				sum(isnull(t.unit_gross_amount,0)) as unit_gross_amount,
--				sum(isnull(t.unit_disc_amount,0)) as unit_disc_amount,
				sum(isnull(CASE WHEN (t.unit_gross_amount > 0 AND t.unit_disc_amount > 0) 
							    THEN t.unit_gross_amount - t.unit_disc_amount
							    WHEN (t.unit_gross_amount > 0 AND t.unit_disc_amount < 0)
							    THEN t.unit_gross_amount - t.unit_disc_amount
							    WHEN (t.unit_gross_amount < 0 AND t.unit_disc_amount > 0)
							    THEN t.unit_gross_amount + t.unit_disc_amount
							    WHEN (t.unit_gross_amount < 0 AND t.unit_disc_amount < 0)	
							    THEN t.unit_gross_amount + t.unit_disc_amount
							    WHEN (t.unit_gross_amount = 0 AND t.unit_disc_amount < 0)
							    THEN t.unit_gross_amount + t.unit_disc_amount
							    WHEN (t.unit_gross_amount = 0 AND t.unit_disc_amount > 0)
							    THEN t.unit_gross_amount - t.unit_disc_amount
								WHEN (t.unit_disc_amount = 0)
							    THEN t.unit_gross_amount 
								ELSE t.unit_gross_amount
				END,0)) as unit_net_amount,
				p.TRAN_TYPE_NUM
			--into #edin_testing				
			FROM dbo.transaction_detail_facts t
			JOIN dbo.store_dim s ON s.store_key = t.store_key
			JOIN dbo.date_dim d ON d.date_key = t.date_key
			left JOIN dbo.vwProduct_Dim_with_TranType p ON p.product_key = t.product_key
			JOIN dbo.line_object_dim lo ON lo.line_object_key = t.line_object_key
		WHERE d.actual_date  BETWEEN @StartDate AND @EndDate
		--WHERE d.actual_date BETWEEN '12/4/2006' AND '12/10/2006 23:59'
		--AND s.store_id =186
			AND (t.transaction_line_seq >=0)
		GROUP BY t.transaction_id,
				 t.store_key,
				 t.date_key,
				 t.register_num,
				 p.department_code,
				 p.subclass_code,
				 lo.line_object,
				 p.TRAN_TYPE_NUM	
	) a


GROUP BY a.transaction_id,
		 a.store_key,
		 a.date_key,
		 a.register_num

-- add sum_type column
IF (Object_ID('work_tmpunits') IS NOT NULL) DROP TABLE work_tmpunits
select u.*, sum_type
into work_tmpunits
from #tmpunits u
join 
(
select transaction_id, sum(tran_type_num) as sum_type from
(
SELECT  transaction_id,
		TRAN_TYPE_NUM
FROM dbo.transaction_detail_facts t
			JOIN dbo.store_dim s ON s.store_key = t.store_key
			JOIN dbo.date_dim d ON d.date_key = t.date_key
left JOIN dbo.vwProduct_Dim_with_TranType p ON p.product_key = t.product_key

		WHERE d.actual_date  BETWEEN @StartDate AND @EndDate
		--WHERE d.actual_date BETWEEN '12/4/2006' AND '12/10/2006 23:59'
		--AND s.store_id =186
		GROUP BY t.transaction_id, p.TRAN_TYPE_NUM
) d
group by transaction_id
) a
on u.transaction_id = a.transaction_id


--select * from dbo.work_tmpunits where transaction_id = 39809256 order by transaction_id


IF (Object_ID('work_tmpTypeSummary') IS NOT NULL) DROP TABLE work_tmpTypeSummary
SELECT  transaction_id,
	store_key,
	date_key,
	register_num,	
	case when sum_type = 1 then 1 else 0 end barebear,
	case when sum_type in (0,2,6) then 1 else 0 end plusonly,
	case when sum_type in (3,7) then 1 else 0 end bearplus,
	case when sum_type = 4 then 1 else 0 end otheronly,
	case when sum_type = 5 then 1 else 0 end bearwithother
into dbo.work_tmpTypeSummary
FROM dbo.work_tmpunits p	
--group by 	
--	transaction_id,
--	store_key,
--	date_key,
--	register_num


--select * from work_tmpTypeSummary ts



--select  sum(barebear) as barebear,
--		sum(bearwithother) as bearwithother,
--		sum(bearplus) as bearplus,
--		sum(plusonly) as plusonly,
--		sum(otheronly) as otheronly,
--		s.store_id,
--		month(d.actual_date) as dmonth,
--		year(d.actual_date) as dyear 
-- 
--from work_tmpTypeSummary ts
--JOIN dbo.store_dim s ON s.store_key = ts.store_key
--JOIN dbo.date_dim d ON d.date_key = ts.date_key
--GROUP BY s.store_id,month(d.actual_date) ,
--		year(d.actual_date)  


----select distinct department,class,subclass from dbo.product_dim order by department
--IF (Object_ID('tempdb.dbo.work_tmpunits') IS NOT NULL) DROP TABLE dbo.work_tmpunits
--
--/** Cece modified on 1/5/05 to include discounts **/
--/*
--sum(isnull(CASE WHEN t.unit_gross_amount >= 0 AND lo.line_object IN (101,294,400,401,402,403,404,410) --including heart donation line obj 
--				THEN (t.unit_disc_amount*-1)
--				WHEN t.unit_gross_amount < 0  AND lo.line_object IN (101,294,400,401,402,403,404,410)
--				THEN t.unit_disc_amount END ,0)) as ttlGiftCardDiscount,
--*/
--
--
--	SELECT  t.transaction_id,
--		t.store_key,
--		t.date_key,
--		t.register_num,
-- 		sum(isnull(CASE WHEN p.department IN ('Dolls','Unstuffed')
--				 OR (p.department = 'Sports Licensing' AND p.subclass = 'Skins')
--				THEN t.units 	END,0)) as ttlanimals,
--		sum(isnull(CASE WHEN p.department IN ('Dolls','Unstuffed')
--				 OR (p.department = 'Sports Licensing' AND p.subclass = 'Skins') 
--				 THEN t.unit_gross_amount 
--				 END,0)) as ttlanimaluga,
--
-- 		--modified 9/14/05 to catch exceptions with returned animals overrung
----		sum(isnull(CASE WHEN p.department IN ('Dolls','Unstuffed')
----				 OR (p.department = 'Sports Licensing' AND p.subclass = 'Skins') 
----				 AND (t.unit_gross_amount < 0 AND t.unit_disc_amount > 0)
----				THEN t.unit_gross_amount + t.unit_disc_amount
----				WHEN p.department IN ('Dolls','Unstuffed')
----				 OR (p.department = 'Sports Licensing' AND p.subclass = 'Skins') 
----				 AND (t.unit_gross_amount > 0 AND t.unit_disc_amount < 0)
----				THEN t.unit_gross_amount  
----				END,0)) as ttlanimaluga,
----		sum(isnull(CASE WHEN right(p.department_code,2) = 25 THEN t.units END,0)) as ttlanimals,
----		sum(isnull(CASE WHEN right(p.department_code,2) = 25 THEN t.unit_gross_amount END,0)) as ttlanimaluga,
--
---- 		sum(isnull(CASE WHEN p.department = 'Unstuffed' AND t.unit_gross_amount < 15 THEN t.units END,0)) as animals_lt15,
---- 		sum(isnull(CASE WHEN p.department = 'Unstuffed' AND t.unit_gross_amount >= 15 AND t.unit_gross_amount < 20 THEN t.units END,0)) as animals_gte15_lt20,
---- 		sum(isnull(CASE WHEN p.department = 'Unstuffed' AND t.unit_gross_amount >= 20 THEN t.units END,0)) as animals_gte20,
--		sum(isnull(CASE WHEN p.department IN ('Sports Licensing','Clothes','Sounds','Accessories','Footwear','Prestuffed','Human') 
--				AND p.subclass <> 'Skins'
--				THEN t.units END,0)) as ttlnonanimals,
--		sum(isnull(CASE WHEN p.department IN ('Sports Licensing','Clothes','Sounds','Accessories','Footwear','Prestuffed','Human') 
--				AND p.subclass <> 'Skins'
--				THEN t.unit_gross_amount END,0)) as ttlnonanimaluga,
--		sum(isnull(CASE WHEN p.department = 'Accessories' THEN t.units END,0)) as ttlaccessories,
--		sum(isnull(CASE WHEN p.department = 'Footwear' THEN t.units END,0)) as ttlshoes,	
--		sum(isnull(CASE WHEN p.department = 'Sounds' THEN t.units END,0)) as ttlsounds,
--		--units = coupons, bear bucks redeemed OR sold, gift cards redeemed OR sold, - basically just merchandise
--
----		sum(isnull(CASE WHEN p.product_key > 0 
----				AND p.department NOT IN ('Supplies','BABW Gift Cards') 
----				AND p.department <> '' AND p.department is not null 
----				THEN t.units END,0)) as ttlunits,
--		sum(isnull(CASE WHEN lo.line_object = 100 
--				THEN t.units END,0)) as ttlunits,
--		
--		sum(isnull(CASE WHEN lo.line_object IN (294,400,401,402,403,404,410,1625)
--				THEN t.units END ,0)) as ttlGiftCardUnits	
--		
----		sum(isnull(CASE WHEN p.product_key = -6 
----				THEN t.units END,0)) as ttlGiftCardUnits
--	
--	INTO dbo.work_tmpunits	
--	FROM dbo.transaction_detail_facts t
--	JOIN dbo.store_dim s ON s.store_key = t.store_key
--	JOIN dbo.date_dim d ON d.date_key = t.date_key
--	JOIN dbo.product_dim p ON p.product_key = t.product_key
--	JOIN dbo.line_object_dim lo ON lo.line_object_key = t.line_object_key
--	WHERE d.actual_date  BETWEEN @StartDate AND @EndDate
--	--WHERE d.actual_date BETWEEN '5/8/2005' AND '5/8/2005 23:59'
--	--AND s.store_id =186
--	AND (t.transaction_line_seq >=0)
--	
--
--	GROUP BY t.transaction_id,
--	 t.store_key,
--	 t.date_key,
--	 t.register_num
	

/* ===== CREATE  INDEX ON UNITS BY DEPT TABLE ===== */
CREATE  INDEX IX_TMPUnits on work_tmpunits (store_key, date_key)

--select * from work_tmpunits where transaction_id = 27411280


--log------------------------------------------------------------
UPDATE dbo.ld_monitor
SET status = 'complete', process_date = getdate()
WHERE step = 10
-----------------------------------------------------------------

/**************************************************************/
/**************************************************************/
/******** ===== INSERT TOTALS INTO METRICS TABLE ===== ********/

/**************************************************************/
/**************************************************************/


--select  sum(barebear) as barebear,
--		sum(bearwithother) as bearwithother,
--		sum(bearplus) as bearplus,
--		sum(plusonly) as plusonly,
--		sum(otheronly) as otheronly,
--		s.store_id,
--		month(d.actual_date) as dmonth,
--		year(d.actual_date) as dyear 
-- 
--from work_tmpTypeSummary ts



INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	33, --Bare Bear Transactions
	a.store_key,
	a.date_key,
	sum(barebear)

from work_tmpTypeSummary a
group by a.store_key,
	 a.date_key

INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	34, --Bear Plus
	a.store_key,
	a.date_key,
	sum(bearplus)

from work_tmpTypeSummary a
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	35, --Plus Only
	a.store_key,
	a.date_key,
	sum(plusonly)

from work_tmpTypeSummary a
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	100, --Bear with Other
	a.store_key,
	a.date_key,
	sum(bearwithother)

from work_tmpTypeSummary a
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	101, --Other Only 
	a.store_key,
	a.date_key,
	sum(otheronly)

from work_tmpTypeSummary a
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	45, --Bare Bear Sales
	a.store_key,
	a.date_key,
	sum(isnull(Net_Sale,0))

FROM work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.barebear = 1
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	46, --Bear Plus Sales
	a.store_key,
	a.date_key,
	sum(isnull(Net_Sale,0))

FROM work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.bearplus = 1
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	47, -- Plus Only Sales
	a.store_key,
	a.date_key,
	sum(isnull(Net_Sale,0))

FROM work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.plusonly = 1
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	103, -- BearWithOtherSales
	a.store_key,
	a.date_key,
	sum(isnull(Net_Sale,0))

FROM work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.bearwithother = 1
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	105, -- OtherOnlySales
	a.store_key,
	a.date_key,
	sum(isnull(Net_Sale,0))

FROM work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.otheronly = 1
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	53, --Bare Bear 
	a.store_key,
	a.date_key,
	sum(isnull(Units,0)) 

from work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.barebear = 1
group by a.store_key,
	 a.date_key

INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	54, --Bear Plus Units
	a.store_key,
	a.date_key,
	sum(isnull(Units,0))

from work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.bearplus = 1
group by a.store_key,
	 a.date_key

INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	55, -- Plus Only Units
	a.store_key,
	a.date_key,
	sum(isnull(Units,0))

from work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.plusonly = 1
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	102, -- BearWithOtherTransUnits
	a.store_key,
	a.date_key,
	sum(isnull(Units,0))

from work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.bearwithother = 1
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	104, -- OtherOnlyUnits
	a.store_key,
	a.date_key,
	sum(isnull(Units,0))

from work_tmptransrollup a
JOIN work_tmpTypeSummary b ON a.transaction_id = b.transaction_id
where b.otheronly = 1
group by a.store_key,
	 a.date_key



INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	68, --GAAP Bare Bear Sales
	a.store_key,
	a.date_key,
	sum(isnull(GAAP_Sale,0))

FROM work_tmptransrollup a
where transaction_type = 'Bare Bear'
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	69, --GAAP Bear Plus Sales
	a.store_key,
	a.date_key,
	sum(isnull(GAAP_Sale,0))

FROM work_tmptransrollup a
where transaction_type = 'Bear Plus'
group by a.store_key,
	 a.date_key


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	70, -- GAAP Plus Only Sales
	a.store_key,
	a.date_key,
	sum(isnull(GAAP_Sale,0))

FROM work_tmptransrollup a
where transaction_type = 'Plus Only'
group by a.store_key,
	 a.date_key



-- --log------------------------------------------------------------
-- INSERT INTO dw.dbo.ld_monitor(process_name, status, process_date)
-- VALUES('spMetricsBuild_GAAP', '16 of 17', getdate())
-- -----------------------------------------------------------------
--log------------------------------------------------------------
UPDATE dbo.ld_monitor
SET status = 'complete', process_date = getdate()
WHERE step = 11
-----------------------------------------------------------------


/***************************************************************/
/************************ REGISTRATIONS ************************/
/***************************************************************/

-- IF (Object_ID('tempdb..#tmpRegRollup') IS NOT NULL) DROP TABLE #tmpRegRollup
-- select 	tdf.store_key,
-- 
-- 	tdf.date_key,
-- 	count(distinct
-- 	CASE 	WHEN tdf.transaction_line_seq < 0 
--  		THEN ad.animal_id
-- 		ELSE null
-- 	END) as NumAnimalsReg,
-- 	count(distinct
-- 	CASE 	WHEN tdf.transaction_line_seq < 0 AND tdf.animal_key <> 0 AND cd.gender = 'M'
--  		THEN ad.animal_id
-- 		ELSE null
-- 	END) as NumBoyReg,
-- 	count(distinct
-- 	CASE 	WHEN tdf.transaction_line_seq < 0 AND tdf.animal_key <> 0 AND cd.gender = 'F'
--  		THEN ad.animal_id
-- 		ELSE null
-- 	END) as NumGirlReg,
-- 	count(distinct
-- 	CASE 	WHEN tdf.transaction_line_seq < 0 AND tdf.animal_key <> 0 AND tdf.purpose_key = 2
--  		THEN ad.animal_id
-- 		ELSE null
-- 	END) as NumGiftReg,
-- 	count(distinct
-- 	CASE 	WHEN tdf.transaction_line_seq < 0 AND tdf.animal_key <> 0 AND tdf.purpose_key = 1 
--  		THEN ad.animal_id
-- 		ELSE null
-- 	END) as NumSelfReg
-- into #tmpRegRollup
-- 
-- from dbo.transaction_detail_facts tdf
-- join dbo.animal_dim ad ON tdf.animal_key = ad.animal_key
-- left join dbo.customer_dim cd ON ad.Reference_ID = cd.customer_num
-- join dbo.date_dim d on tdf.date_key = d.date_key 
-- join dbo.store_dim s on tdf.store_key = s.store_key
-- WHERE d.actual_date BETWEEN @StartDate AND @EndDate   
-- --WHERE d.actual_date >= '12/11/2003' 
-- AND tdf.transaction_line_seq < 0
-- --AND s.store_id = 1
-- --WHERE d.fiscal_year = 2003 and d.fiscal_week = 46	

-- GROUP BY tdf.store_key,
-- 	 tdf.date_key

--log------------------------------------------------------------
UPDATE dbo.ld_monitor
SET status = 'complete', process_date = getdate()
WHERE step = 12
-----------------------------------------------------------------

---- rebuild the indexes on metric_facts
--DBCC DBREINDEX (metric_facts, '', 80)

/**************************************************/
-- 3/9/05 DanM--now called separately in DTS package; 
-- /*==========================================================================
-- == Call the procedure for "Jacks Facts"
-- =================================================================*/
-- DECLARE @RC int

-- 
-- EXEC @RC = dw.dbo.spTransactionSummaryBuild @StartDate, @EndDate
-- /*==========================================================================*/




SET NOCOUNT OFF
Return(@iRtnCd)
```

