# dbo.spGiftCard_Activations

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGiftCard_Activations"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE PROC spGiftCard_Activations
AS


DECLARE @cnt int
DECLARE @select varchar(5000)
DECLARE @filename  varchar(100)
Declare @char_seperator varchar(12)


set nocount on
declare @StartDate varchar(15)          
declare @StopDate varchar(15)           

SET @StartDate = CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
SET @StopDate  = CONVERT(char,GETDATE(),101) 

SET @select ='
SET ANSI_WARNINGS OFF
SET NOCOUNT ON
	select storeid, item_num, filecount
	from (
		select storeid,
			item_num,
			count(*) FileCount 
		from (
			select case when store_id = 0 then 990 else store_id end storeid, 
	 		    case when store_id = 13 and store13_item_num is not null then store13_item_num 
			        else item_num 
			    end item_num
			from dw..giftcard_header gch 
				join dw..giftcard_detail gcd 
				on gcd.fileid = gch.fileid 
				join dw..store_dim s  
				on s.store_key = gcd.store_key 
				join dw..GiftCard_PromotionCode_To_ItemNum p 
				on p.promotion_code = gcd.promotion_code 
			where internal_request_code in (18, 28) 
				and escheatable_transaction = '+char(39)+'Y'+char(39) + '
				and gcd.promotion_code <> 0 
				and gch.fileid in ( 
					select fileid 
					from dw..giftcard_header h 
					where period_start_date >= '+char(39)+@StartDate+char(39)+' and period_start_date < '+char(39)+@StopDate+char(39) + '
				)
			) d
		group by storeid, item_num 
	
		union
	
		select case when store_id = 0 then 2990 else store_id end storeid, 
			item_num, 
			count(*) FileCount 
		from dw..giftcard_header_international gch 
			join dw..giftcard_detail_international gcd 
			on gcd.fileid = gch.fileid 
			join dw..store_dim s  
			on s.store_key = gcd.store_key 
			join dw..GiftCard_PromotionCode_To_ItemNum p 
			on p.promotion_code = gcd.promotion_code 
		where internal_request_code in (18, 28) 
			and escheatable_transaction = '+char(39)+'Y'+char(39) + '
			and gcd.promotion_code <> 0 
			and gch.fileid in ( 
				select fileid 
				from dw..giftcard_header_international h 
				where period_start_date >= '+char(39)+@StartDate+char(39)+' and period_start_date < '+char(39)+@StopDate+char(39) + '
					and groupcode =''UK''
			)
		group by case when store_id = 0 then 2990 else store_id end, item_num 
	) d
	order by storeid, item_num 
'

--print @select
-- 	order by case when store_id = 0 then 2990 else store_id end, item_num 


SET @filename='GiftCardReport'+replace(convert(varchar(12),getdate(),102),'.','')+'.csv'
SET @char_seperator =char(9)
-- 
exec msdb.dbo.sp_send_dbmail @recipients = 'databears@buildabear.com',
--@copy_recipients='databears@buildabear.com',
   				   @body = 'The attached list of GiftCard Activations.',
   				   @subject = 'GiftCard_Activations',
   				   @query =@select,
                      @attach_query_result_as_file = 'TRUE',
                      @query_result_separator =  @char_seperator ,
    	               @query_attachment_filename =  @filename 
                       
                       


dbo,spMetricsBuild_KioskOnly,--Text
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--02/12/2007	corrected transaction bucket logic


/****** Object:  Stored Procedure dbo.spMetricsBuild    Script Date: 3/23/2005 ******/

--EXEC spMetricsBuild '12/29/2002','1/25/2003'
-- select min(actual_date), max(actual_date) from date_dim where fiscal_year=2003 and fiscal_period = 1

CREATE PROCEDURE [dbo].[spMetricsBuild_KioskOnly]
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
and metric_dim_key in (select metric_dim_key from metric_dim 
						where source = 'KIOSK'
						)


/***************************************************************/
/************************ REGISTRATIONS ************************/
/***************************************************************/

-- IF (Object_ID('tempdb..work_tmpRegRollup') IS NOT NULL) DROP TABLE work_tmpRegRollup
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
-- into work_tmpRegRollup
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


IF (Object_ID('work_tmpRegRollup') IS NOT NULL) DROP TABLE work_tmpRegRollup
select 	tdf.store_key,
	tdf.date_key,
	count(distinct isnull(ad.animal_id,0)) as NumAnimalsReg,
	count(distinct
	CASE 	WHEN tdf.animal_key <> 0 AND cd.gender = 'M'
 		THEN ad.animal_id
		ELSE null
	END) as NumBoyReg,
	count(distinct
	CASE 	WHEN tdf.animal_key <> 0 AND cd.gender = 'F'
 		THEN ad.animal_id
		ELSE null
	END) as NumGirlReg,
	count(distinct
	CASE 	WHEN tdf.animal_key <> 0 AND tdf.purpose_key = 2
 		THEN ad.animal_id
		ELSE null
	END) as NumGiftReg,
	count(distinct
	CASE 	WHEN  tdf.animal_key <> 0 AND tdf.purpose_key = 1 
 		THEN ad.animal_id
		ELSE null
	END) as NumSelfReg,

	count(distinct
	CASE 	WHEN  tdf.purpose_key = 1 AND tdf.guest_type_key IN (1,2) 
 		THEN tdf.customer_key
		ELSE null
	END) as NumSelfRecipGuest,

	count(distinct
	CASE 	WHEN  tdf.purpose_key = 2 AND tdf.guest_type_key = 2 
 		THEN tdf.customer_key
		ELSE null
	END) as NumGiftGiverGuest,

	count(distinct
	CASE 	WHEN  tdf.purpose_key = 2 AND tdf.guest_type_key = 1 
 		THEN tdf.customer_key
		ELSE null
	END) as NumGiftRecipGuest,

	count(distinct
	CASE 	WHEN tdf.First_vs_Repeat = 'first'
 		THEN tdf.household_key --tdf.transaction_id
		ELSE null
	END) as NumNewVis,
	count(distinct
	CASE 	WHEN tdf.First_vs_Repeat = 'repeat'
 		THEN household_key --tdf.transaction_id
		ELSE null
	END) as NumRepeatVis
into work_tmpRegRollup

from dbo.transaction_kiosk_facts tdf
join dbo.animal_dim ad ON tdf.animal_key = ad.animal_key
join dbo.customer_dim cd ON tdf.customer_key = cd.customer_key
join dbo.date_dim d on tdf.date_key = d.date_key 
join dbo.store_dim s on tdf.store_key = s.store_key
WHERE d.actual_date BETWEEN @StartDate AND @EndDate   
--WHERE d.actual_date >= '11/11/2005' 
--AND s.store_id = 1
--WHERE d.fiscal_year = 2003 and d.fiscal_week = 46	
GROUP BY tdf.store_key,
	 tdf.date_key

--select * from work_tmpRegRollup


/* ===== CREATE  INDEX ON REG ROLLUP TABLE ===== */
CREATE  INDEX IX_TMPRegRoll on work_tmpRegRollup (store_key, date_key)

INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	92, --GiftRecipientGuests
	a.store_key,
	a.date_key,
	NumGiftRecipGuest 

from work_tmpRegRollup a


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	93, --SelfRecipientGuests
	a.store_key,
	a.date_key,
	NumSelfRecipGuest 

from work_tmpRegRollup a

INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	94, --GiftGiverGuests
	a.store_key,
	a.date_key,
	NumGiftGiverGuest 

from work_tmpRegRollup a

INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	23, --Girl Reg
	a.store_key,
	a.date_key,
	NumGirlReg 

from work_tmpRegRollup a



INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	24, --Boy Reg
	a.store_key,
	a.date_key,
	NumBoyReg

from work_tmpRegRollup a



INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	25, --Registrations
	a.store_key,
	a.date_key,
	NumAnimalsReg

from work_tmpRegRollup a




INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	28, --Self Reg
	a.store_key,
	a.date_key,
	NumSelfReg

from work_tmpRegRollup a


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	29, --Gift Reg
	a.store_key,
	a.date_key,
	NumGiftReg

from work_tmpRegRollup a

INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	91, --New Guests
	a.store_key,
	a.date_key,
	NumNewVis

from work_tmpRegRollup a


INSERT INTO [dbo].[metric_facts](metric_dim_key, [store_key], [date_key], [amount])
select 	22, --Gift Reg
	a.store_key,
	a.date_key,
	NumRepeatVis

from work_tmpRegRollup a




/*
/*************************************************
** Fill in the missing date_key blanks
** Added:  Dan M. 10/10/03
**************************************************/
---- get 26 months of date_keys
select * into #date_dim
from date_dim where actual_date >= dateadd(mm,-26,getdate()) and actual_date <= dateadd(mm,2,getdate())

---- populate a table with every combination
select date_key, store_key,metric_dim_key
into #metric_cross_join
from #date_dim dd
	cross join metric_dim mf 
	cross join store_dim sd 

---- insert the blanks
INSERT INTO dbo.metric_facts(metric_dim_key, store_key, date_key, amount)
select mc.metric_dim_key
	,mc.store_key
	,mc.date_key
	,0
 from #metric_cross_join mc
	left join metric_facts mf on mc.date_key = mf.date_key 
		and mc.store_key = mf.store_key
		and mc.metric_dim_key = mf.metric_dim_key
where mf.date_key is null

-- --log------------------------------------------------------------
-- INSERT INTO dw.dbo.ld_monitor(process_name, status, process_date)
-- VALUES('spMetricsBuild_GAAP', '17 of 17', getdate())
-- -----------------------------------------------------------------
--log------------------------------------------------------------
UPDATE dbo.ld_monitor
SET status = 'complete', process_date = getdate()
WHERE step = 13
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

*/


SET NOCOUNT OFF
Return(@iRtnCd)
```

