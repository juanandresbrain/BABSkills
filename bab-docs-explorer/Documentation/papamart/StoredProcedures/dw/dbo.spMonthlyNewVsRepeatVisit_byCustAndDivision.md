# dbo.spMonthlyNewVsRepeatVisit_byCustAndDivision

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMonthlyNewVsRepeatVisit_byCustAndDivision"]
    date_dim(["date_dim"]) --> SP
    product_dim(["product_dim"]) --> SP
    store_dim(["store_dim"]) --> SP
    dbo_tdf_rpt(["dbo.tdf_rpt"]) --> SP
    dbo_transaction_detail_facts(["dbo.transaction_detail_facts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| product_dim |
| store_dim |
| dbo.tdf_rpt |
| dbo.transaction_detail_facts |

## Stored Procedure Code

```sql
/******************************************************************************
**
**	Name:		spMonthlyNewVsRepeatVisit_byCustAndDivision
**
**	Description: 	Display new and repeat visits, by month, by store
**
**	Parameters:
**		@FromDate	- Date to start with
**		@ToDate		- Date to end with
**		@GroupByMonthFl	- Group by month, instead of by store, by month
**		@bDebugFl	- Debug flag. Prints intermediate results.
**
** 	Returns:	@iRtnCd {0=Success; non-zero=Failure}
**
**	Examples:	spMonthlyNewVsRepeatVisit_byCustAndDivision @FromDate='2002-01-31 00:00:00', @ToDate='2002-12-31 23:59:59', @GroupByMonthFl=1
			spMonthlyNewVsRepeatVisit_byCustAndDivision @FromDate='2002-10-01 00:00:00', @ToDate='2002-12-31 23:59:59', @bDebugFl=1

**	History:	12/05/2002	PaulK		DEVELOP
**			 4/24/2003	davidr	switched output over to fiscal year and fiscal month
**	       		10/16/2003	cecec	modified to run on Papamart/DW
			01/13/2004  	danm   modified to run at the customer level
******************************************************************************/
CREATE
PROCEDURE dbo.spMonthlyNewVsRepeatVisit_byCustAndDivision
	/* ===== ARGUMENTS ===== */
	@FromDate 		DATETIME	= NULL,
	@ToDate 		DATETIME	= NULL,
	@GroupByStoreFl		BIT		= 0
AS

SET NOCOUNT ON
SET QUOTED_IDENTIFIER OFF
	
	


/* ============================================================================= */
/* ================================  BEGIN  ==================================== */
/* ============================================================================= */

/************************************************************/
-- Prep...build new TDF table with only kiosk data
/***********************************************************
if exists (select * from sysobjects where id = object_id('dbo.tdf_rpt') and sysstat & 0xf = 3)
	drop table dbo.tdf_rpt

select store_key, date_key, purpose_key, sender_household_key, sender_customer_key, sender_address_key, recipient_household_key, recipient_customer_key, recipient_address_key, transaction_line_seq
into tdf_rpt
from transaction_detail_facts
where transaction_line_seq <0
--50 min
ALTER  clustered index idxC_NU_date_key on tdf_rpt(date_key)
--6 min
*/



/* ===== GET VISIT INFO FROM Transaction Detail Facts TABLE FOR ALL stores in DATE range ===== */
IF (Object_ID('tempdb..#TMPKiosk') IS NOT NULL) DROP TABLE #TMPKiosk
--gift senders
SELECT --DISTINCT 
	dd.actual_date,
	sd.store_id,
	tdf.sender_customer_key as hhkey,
	tdf.product_key,
	0 as FirstVisit,
	0 as RepeatVisit
INTO #TMPKiosk
--FROM dbo.transaction_detail_facts tdf
FROM dbo.transaction_detail_facts tdf
JOIN store_dim sd ON tdf.store_key = sd.store_key
JOIN date_dim dd ON tdf.date_key = dd.date_key
JOIN product_dim p ON tdf.product_key = p.product_key 
WHERE dd.actual_date BETWEEN '2/28/2005' AND '3/31/2005 23:59' --BETWEEN @FromDate AND @ToDate --
and sender_customer_key <> 0
and transaction_line_seq < 0
and p.division = 'dolls'
--and sd.store_id = 54

UNION
--self recipients
SELECT --DISTINCT 
	dd.actual_date,
	sd.store_id,
--	tdf.recipient_household_key as hhkey,
	tdf.sender_customer_key as hhkey,
	tdf.product_key,
	0 as FirstVisit,
	0 as RepeatVisit
--FROM dbo.transaction_detail_facts tdf
FROM dbo.transaction_detail_facts tdf
JOIN store_dim sd ON tdf.store_key = sd.store_key
JOIN date_dim dd ON tdf.date_key = dd.date_key
JOIN product_dim p ON tdf.product_key = p.product_key 
WHERE dd.actual_date BETWEEN '2/28/2005' AND '3/31/2005 23:59' --BETWEEN @FromDate AND @ToDate --
AND tdf.purpose_key = 1 
and recipient_customer_key <> 0
and transaction_line_seq < 0
and p.division = 'dolls'

--(347375 row(s) affected) in 17 sec
--select count(*) from #TMPKiosk
--select * from purpose_dim
--and sd.store_id = 54



CREATE INDEX IX_hhkey ON #TMPKiosk (hhkey)


/* ===== GET ALL VISITS FOR SELECTED HHs ===== */

IF (Object_ID('tempdb..#TMPAllVisits') IS NOT NULL) DROP TABLE #TMPAllVisits
SELECT distinct a.actual_date, hhkey
INTO	#TMPAllVisits
from(
SELECT --DISTINCT	
	dd.actual_date,
	tdf.sender_customer_key as hhkey
	--tdf.sender_household_key as hhkey		
--FROM dbo.transaction_detail_facts tdf (nolock) 
FROM dbo.tdf_rpt tdf (nolock)
	JOIN date_dim dd ON tdf.date_key = dd.date_key		
WHERE tdf.transaction_line_seq = -1
and tdf.sender_customer_key in (select hhkey from #TMPKiosk where hhkey >0)
 
UNION 
SELECT --DISTINCT	
	dd.actual_date,
	tdf.recipient_customer_key as hhkey
	--tdf.recipient_household_key as hhkey		
--FROM dbo.transaction_detail_facts tdf (nolock)
FROM dbo.tdf_rpt tdf (nolock)
	JOIN date_dim dd ON tdf.date_key = dd.date_key		
WHERE tdf.purpose_key = 1 and tdf.transaction_line_seq = -1
and tdf.recipient_customer_key in (select hhkey from #TMPKiosk where hhkey >0)
) a



CREATE   INDEX IX_Visit_hhkey ON #TMPAllVisits (hhkey)

/* ===== COMPUTE FIRST VISIT ===== */
IF (Object_ID('tempdb..#TMPFirstVisit') IS NOT NULL) DROP TABLE #TMPFirstVisit
SELECT		Min(actual_date)	'FirstVisit',
		hhkey
INTO		#TMPFirstVisit
FROM		#TMPAllVisits
GROUP BY 	hhkey





/* ===== MARK FIRST VISIT ===== */

UPDATE		#TMPKiosk
SET		FirstVisit = 1
FROM		#TMPKiosk
JOIN		#TMPFirstVisit V
	ON	V.hhkey = #TMPKiosk.hhkey 
WHERE		V.FirstVisit = #TMPKiosk.actual_date  --  BETWEEN  @FromDate AND @ToDate



/* ===== MARK REPEAT VISIT ===== */
UPDATE		#TMPKiosk
SET		RepeatVisit = 1
WHERE		FirstVisit = 0


--select left(Date,11) Date, Left(Address,25) Address, Left(sCity,16) City, Left(sState,2) state, left(Zipcode,5) zipcode, Left(sLastName,12) lastname, FirstVisit First, RepeatVisit Repeat from #tmpkiosk K
--join tbluniqueaddress U on U.sAddress = K.Address and U.sZipcode = K.zipcode
--order by FirstVisit DESC, Date, Address, Zipcode

/* ===== OUTPUT GROUPING ===== */
IF @GroupByStoreFl = 0
	/* ----- GROUP BY STORE ----- */
	SELECT		dd.Fiscal_Year		'Year',
			dd.Fiscal_Period	'Month',
			dd.Fiscal_Week		'Week',				
			tk.store_id,
			Sum(tk.FirstVisit)	'SumFirstVisit',
			Sum(tk.RepeatVisit)	'SumRepeatVisit'
	FROM		#TMPKiosk tk
			JOIN Date_dim dd
			ON dd.actual_Date = tk.actual_date
	GROUP BY	dd.Fiscal_Year,
			dd.Fiscal_Period,
			dd.Fiscal_Week,
			tk.store_id
	ORDER BY	dd.Fiscal_Year,
			dd.Fiscal_Period,
			dd.Fiscal_Week,
			tk.store_id

ELSE
	/* ----- GROUP BY MONTH ----- */
	SELECT		dd.Fiscal_Year		'Year',
			dd.Fiscal_Period	'Month',
			dd.Fiscal_Week		'Week',				
			Sum(tk.FirstVisit)	'SumFirstVisit',
			Sum(tk.RepeatVisit)	'SumRepeatVisit'
	FROM		#TMPKiosk tk
			JOIN Date_dim dd
			ON dd.actual_Date = tk.actual_date
	GROUP BY	dd.Fiscal_Year,
			dd.Fiscal_Period,
			dd.Fiscal_Week
	ORDER BY	dd.Fiscal_Year,
			dd.Fiscal_Period,
			dd.Fiscal_Week




SET NOCOUNT OFF
SET QUOTED_IDENTIFIER ON
/* ============================================================================= */
/* =================================  END  ===================================== */
/* ============================================================================= */
```

