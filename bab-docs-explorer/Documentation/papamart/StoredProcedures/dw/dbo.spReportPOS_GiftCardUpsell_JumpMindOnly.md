# dbo.spReportPOS_GiftCardUpsell_JumpMindOnly

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spReportPOS_GiftCardUpsell_JumpMindOnly"]
    dbo_JMC_sls_retail_line_item(["dbo.JMC_sls_retail_line_item"]) --> SP
    dbo_JMC_sls_trans(["dbo.JMC_sls_trans"]) --> SP
    store_dim(["store_dim"]) --> SP
    vwUTAEmployee(["vwUTAEmployee"]) --> SP
    ERP_vwWarehouseIDToLocationCodeRetailInventory(["ERP.vwWarehouseIDToLocationCodeRetailInventory"]) --> SP
    ERP_vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated(["ERP.vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.JMC_sls_retail_line_item |
| dbo.JMC_sls_trans |
| store_dim |
| vwUTAEmployee |
| ERP.vwWarehouseIDToLocationCodeRetailInventory |
| ERP.vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated |

## Stored Procedure Code

```sql
-- =====================================================================================================
-- Name: spReportPOS_GiftCardUpsell
-- Revision History
--		Name:			Date:			Comments:
--		Tim Callahan	05/17/2023		Initial Release
--		Tim Callahan	05/25/2023		Received additional requirements from Annie S of Store Ops 
--		Tim Callahan	09/15/2023		Updated To Handle Multiple Store Countries for JumpMind Portion Of Sales
--										Solutioning Still needed for Historical Aptos POS Sales for UK\CA Stores 
--		Tim Callahan	10/19/2023		Changed Employee Lookup source 
--		Tim Callahan	11/16/2023		Added transaction threshold case statement to account for different countries. 
--		Tim Callahan	2024/09/12		Added Union to Store Lookup Temp table build to allow partner stores to use reporting 
-- =====================================================================================================
CREATE PROCEDURE [dbo].[spReportPOS_GiftCardUpsell_JumpMindOnly]

 @BeginDate date,
 @EndDate date ,
 @StoreNumber varchar (4),
 @USThreshold numeric (14,2),
 @UkThreshold  numeric (14,2)

 --@DynanmicsLocationCode varchar (4)
 --@DwLocationCode varchar (4)

 WITH RECOMPILE 

 as 

 -- Use This Section for testing 
--Declare @BeginDate date
--Declare @EndDate date 
--Declare @StoreNumber varchar (4)
--Declare @DynanmicsLocationCode varchar (4)
--Declare @DwLocationCode varchar (4)
--;

--set @BeginDate = '2022-05-08'
--set @EndDate = '2023-05-08'
--set @StoreNumber = '1105'
--;
Declare @DynanmicsLocationCode varchar (4)
Declare @DwLocationCode varchar (4)
;

IF OBJECT_ID(N'tempdb..#StoreLookup') IS NOT NULL
DROP TABLE #StoreLookup
select 
WarehouseId as DynanmicsLocationCode,
LocationCode as DwLocationCode, 
case when Entity = '1100' 
		then 'US'
	when Entity = '1700'
		then 'CA'
	when Entity = '2110'
		then 'UK'
	ELSE NULL 
	end as Country 
into #StoreLookup
from [stl-ssis-p-01].[IntegrationStaging].[ERP].[vwWarehouseIDToLocationCodeRetailInventory] -- Replaced View on 9/15/2023
where 1=1
--and Entity = '1100'
and WarehouseId = @StoreNumber
-- Added below on 2024-09-12
union 
select 
	v.WarehouseId as DynanmicsLocationCode,
	v.LocationCode as DwLocationCode, 
	sd.country
from [stl-ssis-p-01].[IntegrationStaging].[ERP].[vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated] v 
join store_dim sd on cast(v.LocationCode as int)=sd.store_id  --added 2023-10-06
where 1=1
and WarehouseId = @StoreNumber

set @DynanmicsLocationCode = (select DynanmicsLocationCode from #StoreLookup) 
set @DwLocationCode = (select DwLocationCode from #StoreLookup)
;



-- Total Trans Data 

IF OBJECT_ID(N'tempdb..#RawTransData') IS NOT NULL
DROP TABLE #RawTransData
--select 
--dd.actual_date as TransactionDate, 
----right('111'+cast(sd.store_id as varchar),4) as StoreNumber, 
--sl.DynanmicsLocationCode as StoreNumber,
----isnull(e.Emp_Name,cd.cashier_code) as AssociateNumber, -- Replaced on 11/21/2023
--isnull(e.Emp_Name,SUBSTRING(cd.cashier_code, CHARINDEX('_',cd.cashier_code)+1, 7)) as AssociateNumber, 
--isnull(e.Emp_Fullname,'AssocNameLookUpNotFound') as AssociateName,
--sum (tf.unit_net_amount+tf.tax_amount+abs(tf.upsell_discount_amount)) as SumTotal, -- Basically Goods sold after discount plus tax less any promo gc redeemed 
--cast (count (distinct tf.transaction_id) as float)  as TotalTrans, 
--sum (
--	case 
--		when tf.unit_net_amount >= 25.00 and sl.Country in ('US','CA')	then 1 
--		when tf.unit_net_amount >= 20.00 and sl.Country in ('UK')	then 1 
--		else 0 
--	end ) as TotalQualifyingTrans
--into #RawTransData 
--From Transaction_Facts tf (nolock)
--left join CRMTransactionFact ctf (nolock) on ctf.TransactionID=tf.transaction_id
--join store_dim sd (nolock) on sd.store_key=tf.store_key
--join vwPOSActiveJumpMindStores v on v.StoreID=sd.store_id
--join date_dim dd (nolock) on dd.date_key=tf.date_key
--left join Cashier_Dim cd (nolock) on cd.cashier_key=tf.cashier_key
----left join vwUTAEmployee e (nolock) on right('0000000'+cd.cashier_code,7)=e.Emp_Name -- Replaced on 11/21/2023
--left join vwUTAEmployee e (nolock) on right('0000000'+(SUBSTRING(cd.cashier_code, CHARINDEX('_',cd.cashier_code)+1, 7)),7)=e.Emp_Name
--	--and e.Calcgrp_ID in ('10005','10004')-- US hourly\salary	
--join #StoreLookup sl  on sl.DwLocationCode=sd.store_id
--where 1=1
----and sd.country = 'US' -- CA and UK may need to be handled differently for the employee lookup 
--and tf.isShipFromStore = 0 
--and tf.isPickupFromStore = 0 
--and dd.actual_date between @BeginDate and @EndDate
--and sd.store_id = @DwLocationCode
--and isnull(cd.cashier_code,'1')  not in ('13','1') -- This is In case a web\store (bopis, etc.) doesn't get flagged in DW as such due to a lookup failure against Web Order Processed -- Added 1 on 12/6/2023 per Linda this is "These are the records from when an endless aisle order is completed. "
--group by 
--dd.actual_date, 
----right('111'+cast(sd.store_id as varchar),4),
--sl.DynanmicsLocationCode,
----isnull(e.Emp_Name,cd.cashier_code),
--isnull(e.Emp_Name,SUBSTRING(cd.cashier_code, CHARINDEX('_',cd.cashier_code)+1, 7)) ,
--isnull(e.Emp_Fullname,'AssocNameLookUpNotFound')

--union 

select 
--h.business_date as TransactionDate, 
cast (h.create_time as date) as TransactionDate, -- Replaced 5/24/2023 due to Business Date could be wrong if store doesnt run EOD\SOD
h.business_unit_id as StoreNumber, 
--e.Emp_name as AssociateNumber,
isnull(e.Emp_name,h.username) as AssociateNumber,
isnull(e.Emp_Fullname,'AssocNameLookUpNotFound') as AssociateName,
sum (h.total) as SumTotal,
cast (count (distinct h.trans_nbr) as float)  as TotalTrans,
sum (
	case 
		--when h.subtotal >= 25.00 and left(h.business_unit_id,1) = 1 then 1 
		--when h.subtotal >= 20.00 and left(h.business_unit_id,1) = 2 then 1 
		when h.subtotal >= @USThreshold and left(h.business_unit_id,1) = 1 then 1 
		when h.subtotal >= @UkThreshold and left(h.business_unit_id,1) = 2 then 1 
		else 0 
	end ) as TotalQualifyingTrans
,h.device_id
into #RawTransData
from [dbo].[JMC_sls_trans] h (nolock) 
left join vwUTAEmployee e on h.username=e.Emp_Name	
	--and e.Calcgrp_ID in ('10005','10004')-- US hourly\salary	
where 1=1
and h.trans_type = 'SALE'
and h.trans_status = 'COMPLETED' -- Added 5/15/2023
and h.username <> 000
--and h.business_date between @BeginDate and @EndDate
and cast (h.create_time as date) between @BeginDate and @EndDate -- Replaced 5/24/2023 due to Business Date could be wrong if store doesnt run EOD\SOD
and h.business_unit_id = @DynanmicsLocationCode
group by 
--h.business_date, 
cast (h.create_time as date),
h.business_unit_id, 
--e.Emp_name , 
isnull(e.Emp_name,h.username),
isnull(e.Emp_Fullname,'AssocNameLookUpNotFound')
,h.device_id
--order by 1, 3

-- Found that there is at time as transaction date variance between the JM data and the AW\DW data , taking max value 
IF OBJECT_ID(N'tempdb..#RawTransData2') IS NOT NULL
DROP TABLE #RawTransData2
select
TransactionDate, 
StoreNumber, 
AssociateNumber, 
AssociateName, 
max (SumTotal) as SumTotal, 
max (TotalTrans) as TotalTrans, 
max (TotalQualifyingTrans) as TotalQualifyingTrans
,device_id
into #RawTransData2
from #RawTransData
group by 
TransactionDate, 
StoreNumber, 
AssociateNumber, 
AssociateName
,device_id

-- GC Upsell Trans Data 
IF OBJECT_ID(N'tempdb..#GcTransData') IS NOT NULL
DROP TABLE #GcTransData

--select 
--dd.actual_date as TransactionDate, 
----right('111'+cast(sd.store_id as varchar),4) as StoreNumber, 
--sl.DynanmicsLocationCode as StoreNumber,
--isnull(e.Emp_Name,cd.cashier_code) as AssociateNumber, 
--isnull(e.Emp_Fullname,'AssocNameLookUpNotFound') as AssociateName,
--cast (count (distinct tf.transaction_id) as float)  as TotalTransWithGcPromo
--into #GcTransData
--From Transaction_Facts tf (nolock)
--left join CRMTransactionFact ctf (nolock) on ctf.TransactionID=tf.transaction_id
--join store_dim sd (nolock) on sd.store_key=tf.store_key
--join vwPOSActiveJumpMindStores v on v.StoreID=sd.store_id
--join date_dim dd (nolock) on dd.date_key=tf.date_key
--left join Cashier_Dim cd (nolock) on cd.cashier_key=tf.cashier_key
--left join vwUTAEmployee e (nolock) on right('0000000'+cd.cashier_code,7)=e.Emp_Name
--	--and e.Calcgrp_ID in ('10005','10004')-- US hourly\salary	
--join #StoreLookup sl  on sl.DwLocationCode=sd.store_id
--where 1=1
----and sd.country = 'US' -- CA and UK will need to be handled differently for the employee lookup 
--and tf.isShipFromStore = 0 
--and tf.isPickupFromStore = 0 
--and tf.giftcard_units > 0 
--and abs(tf.giftcard_discount_amount / tf.giftcard_units) = 5
--and dd.actual_date between @BeginDate and @EndDate
--and sd.store_id = @DwLocationCode
--group by
--dd.actual_date, 
----right('111'+cast(sd.store_id as varchar),4),
--sl.DynanmicsLocationCode,
--isnull(e.Emp_Name,cd.cashier_code),
--isnull(e.Emp_Fullname,'AssocNameLookUpNotFound')
--union 
select
--h.business_date as TransactionDate, 
cast (h.create_time as date) as TransactionDate, -- Replaced 5/24/2023 due to Business Date could be wrong if store doesnt run EOD\SOD
h.business_unit_id as StoreNumber, 
--e.Emp_name as AssociateNumber,
isnull(e.Emp_name,h.username) as AssociateNumber, -- Replaced Above on 9/15/2023
isnull(e.Emp_Fullname,'AssocNameLookUpNotFound') as AssociateName,
cast (count (distinct h.trans_nbr) as float) as TotalTransWithGcPromo
, h.device_id
into #GcTransData
from [dbo].[JMC_sls_trans] h (nolock) 
join [dbo].[JMC_sls_retail_line_item] l (nolock) on h.device_id=l.device_id
												and h.trans_nbr=l.sequence_number
												and h.business_date = l.business_date
left join vwUTAEmployee e on h.username=e.Emp_Name
	--and e.Calcgrp_ID in ('10005','10004')-- US hourly\salary	

where 1=1
and h.trans_type = 'SALE'
and h.trans_status = 'COMPLETED'
and h.username <> 000
and l.voided = 0
and l.item_returned = 0
and l.item_id in ('083500','183500','483500') -- Gift Card Activation Styles 
and l.regular_unit_price = '10.000'
and l.discount_amount = '5.000'
--and h.business_date between @BeginDate and @EndDate
and cast (h.create_time as date) between @BeginDate and @EndDate -- Replaced 5/24/2023 due to Business Date could be wrong if store doesnt run EOD\SOD
and cast (l.create_time as date) between @BeginDate and @EndDate --  Added 8/10/2023
and h.business_unit_id = @DynanmicsLocationCode

group by 
--h.business_date, 
cast (h.create_time as date),-- Replaced 5/24/2023 due to Business Date could be wrong if store doesnt run EOD\SOD
h.business_unit_id, 
--e.Emp_Name, 
isnull(e.Emp_name,h.username), -- Replaced Above on 9/15/2023
isnull(e.Emp_Fullname,'AssocNameLookUpNotFound')
, h.device_id
--order by 1, 2, 3


 
IF OBJECT_ID(N'tempdb..#GcTransData2') IS NOT NULL
DROP TABLE #GcTransData2
select
TransactionDate, 
StoreNumber, 
AssociateNumber, 
AssociateName, 
device_id, 
max (TotalTransWithGcPromo) as TotalTransWithGcPromo
into #GcTransData2
from #GcTransData
group by 
TransactionDate, 
StoreNumber, 
AssociateNumber, 
AssociateName,
device_id





IF OBJECT_ID(N'tempdb..#Summary') IS NOT NULL
DROP TABLE #Summary
select
--r.TransactionDate, 
r.StoreNumber, 
r.AssociateNumber, 
r.AssociateName, 
sum (r.SumTotal) SumTotal,
sum (r.TotalTrans) as TotalTrans,
sum (r.TotalQualifyingTrans) as TotalQualifyingTrans,
sum (isnull(g.TotalTransWithGcPromo,0)) as TotalTransWithGcPromo
into #Summary
from #RawTransData2 r
left join #GcTransData2 G on r.TransactionDate=g.TransactionDate
	and r.StoreNumber=g.StoreNumber
	and r.AssociateName=g.AssociateName
	and r.AssociateNumber=g.AssociateNumber
	and r.device_id = g.device_id
group by 
r.StoreNumber, 
r.AssociateNumber, 
r.AssociateName


-- Final Output 
select
StoreNumber, 
isnull(AssociateNumber, 'NumberNotFound') as AssociateNumber,
AssociateName, 
SumTotal as TotalTransactionAmount , 
TotalTrans as TotalTransactionsNumber, 
TotalQualifyingTrans as TotalQualifyingTransactions,
TotalTransWithGcPromo as TotalTransactionsWithGcUpsell,
cast (isnull(TotalTransWithGcPromo,0)/TotalQualifyingTrans as numeric (5,2)) as PercentageTransactionsWithGcUpsell
from #Summary
where TotalQualifyingTrans > 0 
order by 8 desc, 2
--order by 2

dbo,spGuestLoad_Insert_BATCH_ADDR_STG,-- =============================================================================================================
-- Name: spGuestLoad_Insert_BATCH_ADDR_STG
--
-- Description:	
--		Loads up dirty addresses for the current Guest Load so that QAS can cleanse them
--
-- Input:
--		@etl_log_id				int	
--			last guest load to touch this, used for logging.
--
-- Output: 
--		data will be loaded into QASCleansing.dbo.BATCH_ADDR_STG
--
-- Dependencies: 
--
-- EXAMPLE:
--		exec crm.dbo.spGuestLoad_Insert_BATCH_ADDR_STG -1
--
-- Revision History
--		Name:			Date:			Comments:
--		Dave Rice		7/19/2010		created
--		Dan Tweedie		08/20/216		Altered proc to allow for bypass of QAS system. We now use dwstaging tables instead of QASCleansing.
-- =============================================================================================================

CREATE PROCEDURE [dbo].[spGuestLoad_Insert_BATCH_ADDR_STG](@etl_log_id int)
AS
BEGIN

SET NOCOUNT ON;


truncate table dwstaging.dbo.BATCH_ADDR_STG


insert into dwstaging.dbo.BATCH_ADDR_STG (
	stg_id, stg_dta_set_cd, 
	ADDR_LN_1_TXT, ADDR_LN_2_TXT, APT_UNIT_NBR, CTY_NM, ST_PRVNC_ABBRV, PSTL_CD, CNTRY_ABBRV, 
	INS_DT, ETL_LOG_ID, ETL_EVNT_ID
)
SELECT distinct
	c.raw_addr_id stg_id,
	c.stg_dta_set_cd,
	cast(case when isnumeric(rad.ADDR_LN_1_TXT) = 1 and len(rad.ADDR_LN_1_TXT) > 8 then null 
		when isnumeric(substring(rad.ADDR_LN_1_TXT, 1, charindex(' ', rad.ADDR_LN_1_TXT))) = 1 and charindex(' ', rad.ADDR_LN_1_TXT) > 9 then null
		else rad.ADDR_LN_1_TXT end as varchar(60)) ADDR_LN_1_TXT,
	cast(case when isnumeric(rad.ADDR_LN_2_TXT) = 1 and len(rad.ADDR_LN_2_TXT) > 8 then null 
		when isnumeric(substring(rad.ADDR_LN_2_TXT, 1, charindex(' ', rad.ADDR_LN_2_TXT))) = 1 and charindex(' ', rad.ADDR_LN_2_TXT) > 9 then null
		else rad.ADDR_LN_2_TXT end as varchar(60)) ADDR_LN_2_TXT,
	case when isnumeric(rad.APT_UNIT_NBR) = 1 and len(rad.APT_UNIT_NBR) > 8 then null else rad.APT_UNIT_NBR end APT_UNIT_NBR,
	rad.CTY_NM,
	left(case when rad.DRVD_CNTRY_ABBRV = 'US' then
		case when s1.statename is not null then cast(s1.abrev as varchar(2))
			when s2.abrev is not null then cast(s2.abrev as varchar(2))
			when uszc.zip is not null then uszc.st
			else rad.ST_PRVNC_TXT
		end
		else rad.ST_PRVNC_TXT
	end, 5) ST_PRVNC_ABBRV,
	cast(rad.PSTL_CD as varchar(10)) PSTL_CD, 
	case when rad.DRVD_CNTRY_ABBRV = 'US' then 'USA'
		when rad.DRVD_CNTRY_ABBRV = 'CA' then 'CAN'
		when rad.DRVD_CNTRY_ABBRV = 'GB' then 'GBR'
		when rad.DRVD_CNTRY_ABBRV = 'FR' then 'FRA'
		else 'USA'
	end CNTRY_ABBRV,
	getdate() INS_DT,
	c.ETL_LOG_ID,
	c.ETL_EVNT_ID
from dwstaging.dbo.LOAD_REC_ID_CNTRL c with (nolock)
	join dw.dbo.raw_addr_dim rad with (nolock)
	on rad.raw_addr_id = c.raw_addr_id
	left join dw.dbo.tblstates s1 with (nolock)
	on s1.statename = rad.ST_PRVNC_TXT
	left join dw.dbo.tblstates s2 with (nolock)
	on s2.abrev = rad.ST_PRVNC_TXT
	left join dw.dbo.tblUSZIPCurrent uszc with (nolock)
	on uszc.zip = substring(rad.pstl_cd, 1, 5)
where c.ETL_LOG_ID = @etl_log_id
	and rad.clnsd_addr_id is null
END
```

