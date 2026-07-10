# dbo.spReportPOS_GAAP_Sales

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spReportPOS_GAAP_Sales"]
    dbo_JMC_sls_retail_line_item(["dbo.JMC_sls_retail_line_item"]) --> SP
    dbo_JMC_sls_trans(["dbo.JMC_sls_trans"]) --> SP
    pos_ProductCatalogMasterAttributesStage(["pos.ProductCatalogMasterAttributesStage"]) --> SP
    store_dim(["store_dim"]) --> SP
    ERP_vwWarehouseIDToLocationCodeRetailInventory(["ERP.vwWarehouseIDToLocationCodeRetailInventory"]) --> SP
    ERP_vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated(["ERP.vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.JMC_sls_retail_line_item |
| dbo.JMC_sls_trans |
| pos.ProductCatalogMasterAttributesStage |
| store_dim |
| ERP.vwWarehouseIDToLocationCodeRetailInventory |
| ERP.vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated |

## Stored Procedure Code

```sql
---- =====================================================================================================
---- Name: spReportPOS_GAAP_Sales
---- Revision History
----		Name:			Date:			Comments:
----		Tim Callahan	06/01/2023		Initial Release
----		Tim Callahan	09/15/2023		Updated To Handle Multiple Store Countries for JumpMind Portion Of Sales
----		Dan Tweedie		2023-10-06		Added join to store_dim to get country so UK and IE are broken out, subtract tax from UK/IE for sales due to complaints from UK ops, experimenting
----		Tim Callahan	2023/10/13		Changed NetSales source field as the JM field actual_price did not multiple by qty, need to used the extended field 
----		Tim Callahan	2024/07/15		Overhualed proc to use temp tables as well as had to stage device id to ensure transaction count was correct 
----		Tim Callahan	2024/09/12		Added Union to Store Lookup Temp table build to allow partner stores to use reporting 
---- =====================================================================================================
CREATE PROCEDURE [dbo].[spReportPOS_GAAP_Sales]

 @BeginDate date,
 @EndDate date ,
 @StoreNumber varchar (4)

--@DynanmicsLocationCode varchar (4)
--@DwLocationCode varchar (4)

as 

-- Use This Section for testing 
--Declare @BeginDate date
--Declare @EndDate date 
--Declare @StoreNumber varchar (4)
--Declare @DynanmicsLocationCode varchar (4)
--Declare @DwLocationCode varchar (4)
--;
-- End Testing Parameters 

--set @BeginDate = '2024-06-02'
--set @EndDate = '2024-06-27'
--set @StoreNumber = '1119'
--;
----end of Testing Section

Declare @DynanmicsLocationCode varchar (4)
Declare @DwLocationCode varchar (4)
;

IF OBJECT_ID(N'tempdb..#StoreLookup') IS NOT NULL
DROP TABLE #StoreLookup
select 
	v.WarehouseId as DynanmicsLocationCode,
	v.LocationCode as DwLocationCode, 
	sd.country
	--case when Entity = '1100' 
	--		then 'US'
	--	when Entity = '1700'
	--		then 'CA'
	--	when Entity = '2110'
	--		then 'UK'
	--	ELSE NULL 
	--	end as Country 
into #StoreLookup
from [stl-ssis-p-01].[IntegrationStaging].[ERP].[vwWarehouseIDToLocationCodeRetailInventory] v -- changed view source on 9/15/2023
join store_dim sd on cast(v.LocationCode as int)=sd.store_id  --added 2023-10-06
where 1=1
--and Entity = '1100' -- Removed Condition on 9/15/2023
and WarehouseId = @StoreNumber
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

-- Style Data
IF OBJECT_ID(N'tempdb..#StyleLookup') IS NOT NULL
DROP TABLE #StyleLookup
select a.ProductNumber, a.ProductDescription, a.Department, a.DepartmentCode, a.ProductSellingGeography, a.ItemType
into #StyleLookup
from [stl-ssis-p-01].IntegrationStaging.pos.ProductCatalogMasterAttributesStage a 
join #StoreLookup sl on sl.Country=a.ProductSellingGeography -- Added Join on 9/15/2023
group by a.ProductNumber, a.ProductDescription, a.Department, a.DepartmentCode, a.ProductSellingGeography, a.ItemType

;



IF OBJECT_ID(N'tempdb..#RawData') IS NOT NULL
DROP TABLE #RawData
select 
cast (h.create_time as date) as TransactionDate, -- Replaced h.last_update_time with h.create_time for all in raw data table 
h.trans_nbr, 
datepart( hh, h.create_time) as TransactionHour, 
datepart( mi, h.create_time) as TransactionMinute, 
h.business_unit_id as StoreNumber,
s.Department
--,case when s.ProductSellingGeography in ('UK','IE') 
--	then sum(l.actual_unit_price-l.tax_amount) 
--		else sum(l.actual_unit_price) 
--	end as NetSales -- Replaced on 10/13/2023
,case when s.ProductSellingGeography in ('UK','IE') 
	then sum(l.extended_discounted_amount-l.tax_amount) 
		else sum(l.extended_discounted_amount) 
	end as NetSales -- Replaced above on 10/13/2023 as this wasn't considering multiple of the same sku
, sum (l.quantity) as UnitsSold
,h.device_id
into #RawData
from [dbo].[JMC_sls_trans] h (nolock) 
join [dbo].[JMC_sls_retail_line_item] l (nolock) on h.device_id=l.device_id
												and h.trans_nbr=l.sequence_number
												and h.business_date = l.business_date -- Added 7/2/2024
join #StyleLookup s on s.productnumber=l.item_id
where 1=1
--and h.trans_type = 'SALE'
and h.trans_status = 'COMPLETED'
and h.username <> 000
and l.voided = 0
--and l.item_returned = 0
and l.item_type in ('STOCK')
and s.DepartmentCode not in ('R-B-D-47')

and l.line_item_type ='STORE_SALE'

--and cast (h.last_update_time as date) = cast (getdate () as date) -- Will be replaced by parameters 
--and h.business_unit_id = '1105'-- Will be replaced by parameters 
and cast (h.create_time as date) between @BeginDate and @EndDate
and cast (l.create_time as date) between @BeginDate and @EndDate -- Added on 8/10/2023 -- Replaced l.last_update_time  with  l.create_time
and h.business_unit_id = @DynanmicsLocationCode
group by 
cast (h.create_time as date),
h.trans_nbr, 
datepart( hh, h.create_time), 
datepart( mi, h.create_time), 
h.business_unit_id,
s.Department,
s.ProductSellingGeography
,h.device_id




IF OBJECT_ID(N'tempdb..#TransactionCountPerHour') IS NOT NULL
DROP TABLE #TransactionCountPerHour
select TransactionHour, 
count (distinct Trans_Nbr) as TransactionCountPerHour
,r.Device_id 
,r.TransactionDate
--,r.TransactionDate
into #TransactionCountPerHour
from #RawData r
group by TransactionHour
,Device_id 
,r.TransactionDate


IF OBJECT_ID(N'tempdb..#NetSalesPerHour') IS NOT NULL
DROP TABLE #NetSalesPerHour
select TransactionHour, 
sum (NetSales) as NetSalesPerHour
,device_id
,TransactionDate
into #NetSalesPerHour
from #RawData
group by TransactionHour
,device_id
,TransactionDate

IF OBJECT_ID(N'tempdb..#UnitsPerHour') IS NOT NULL
DROP TABLE #UnitsPerHour
select TransactionHour, 
cast (sum (UnitsSold) as Int)  as UnitSoldPerHour
,device_id 
,TransactionDate
into #UnitsPerHour
from #RawData
group by TransactionHour
,device_id 
,TransactionDate


IF OBJECT_ID(N'tempdb..#UnitsPerHourByDepartment') IS NOT NULL
DROP TABLE #UnitsPerHourByDepartment
select 
TransactionHour, 
Department,
cast (sum (UnitsSold) as Int)  as UnitSoldPerHour, 
count (distinct Trans_Nbr) as CountTransWithKeyDepartment
,device_id
,TransactionDate
into #UnitsPerHourByDepartment
from #RawData
where Department in ('Footwear','Stuffers')
group by 
TransactionHour, 
Department
,device_id
,TransactionDate


IF OBJECT_ID(N'tempdb..#UnitsPerHourSkins') IS NOT NULL
DROP TABLE #UnitsPerHourSkins
select 
TransactionHour, 
Department,
cast (sum (UnitsSold) as Int)  as UnitSoldPerHour, 
count (distinct Trans_Nbr) as CountTransWithKeyDepartment
,device_id
,TransactionDate
into #UnitsPerHourSkins
from #RawData
where Department in ('Unstuffed')
group by 
TransactionHour, 
Department
,device_id
,TransactionDate


IF OBJECT_ID(N'tempdb..#Summary1') IS NOT NULL
DROP TABLE #Summary1 
select 
n.TransactionHour
,t.TransactionCountPerHour
,u.UnitSoldPerHour
,n.NetSalesPerHour
--,cast (n.NetSalesPerHour/t.TransactionCountPerHour as numeric (14,2)) as DPT
--,cast (cast (u.UnitSoldPerHour as float) /cast (t.TransactionCountPerHour as float) as numeric (14,2)) as UPT
,uphs.UnitSoldPerHour as SkinsPerHour 
,uphd.UnitSoldPerHour as ShoesPerHour 
,uphds.UnitSoldPerHour as StuffersPerHour
--,cast (cast (uphd.UnitSoldPerHour as float) /cast (uphs.UnitSoldPerHour as float) as numeric (5,2)) as ShoesPct
--,cast (cast (uphds.UnitSoldPerHour as float) /cast (uphs.UnitSoldPerHour as float) as numeric (5,2)) as StuffersPct
, n.device_id
,n.TransactionDate
into #Summary1
from #NetSalesPerHour  N
join #TransactionCountPerHour T on t.TransactionHour=n.TransactionHour and t.device_id = n.device_id and t.TransactionDate = n.TransactionDate
join #UnitsPerHour u on u.TransactionHour=n.TransactionHour and u.device_id = n.device_id and u.TransactionDate = n.TransactionDate
left join #UnitsPerHourskins uphs on uphs.TransactionHour=n.TransactionHour and uphs.device_id = n.device_id and uphs.TransactionDate = n.TransactionDate
left join #UnitsPerHourByDepartment uphd on uphd.TransactionHour=n.TransactionHour and uphd.device_id = n.device_id and uphd.TransactionDate  = n.TransactionDate
								and uphd.Department = 'Footwear'
left join #UnitsPerHourByDepartment uphds on uphds.TransactionHour=n.TransactionHour and uphds.device_id = n.device_id and uphds.TransactionDate = n.TransactionDate
								and uphds.Department = 'Stuffers'

group by 
n.TransactionHour
,n.NetSalesPerHour 
,t.TransactionCountPerHour
,u.UnitSoldPerHour
--,cast (n.NetSalesPerHour/t.TransactionCountPerHour as numeric (14,2)) as DPT
--,cast (cast (u.UnitSoldPerHour as float) /cast (t.TransactionCountPerHour as float) as numeric (14,2)) as UPT
,uphs.UnitSoldPerHour 
,uphd.UnitSoldPerHour 
,uphds.UnitSoldPerHour
,n.device_id
,n.TransactionDate


IF OBJECT_ID(N'tempdb..#Summary2') IS NOT NULL
DROP TABLE #Summary2

select 
s.TransactionHour
,sum (isnull(s.NetSalesPerHour,0.00)) as NetSalesPerHour
,sum (isnull(s.TransactionCountPerHour,0.00)) as TransactionCountPerHour
,sum (isnull(s.UnitSoldPerHour,0)) as UnitsSoldPerHour
,sum (isnull(s.SkinsPerHour,0)) as SkinsPerHour
,sum (isnull(s.ShoesPerHour,0)) as ShoesPerHour
,sum (isnull(s.StuffersPerHour,0)) as StuffersPerHour
into #Summary2
from #Summary1 s
group by s.TransactionHour


IF OBJECT_ID(N'tempdb..#Summary3') IS NOT NULL
DROP TABLE #Summary3
select 
s.*
,cast (s.NetSalesPerHour/s.TransactionCountPerHour as numeric (14,2)) as DPT
,cast (cast (s.UnitsSoldPerHour as float) /cast (s.TransactionCountPerHour as float) as numeric (14,2)) as UPT
,case when s.SkinsPerHour = 0 
		then 0 
	else 
		cast (cast (s.ShoesPerHour as float) /cast (s.SkinsPerHour as float) as numeric (5,2)) 
	end as ShoesPct
,case when s.SkinsPerHour = 0 
		then 0
	else cast (cast (s.StuffersPerHour as float) /cast (s.SkinsPerHour as float) as numeric (5,2)) 
	end as StuffersPct
into #Summary3
from #Summary2 s




 ----Original Final Output 
select 
s.TransactionHour, 
format (dateadd(hh,s.TransactionHour, '00:00'),'h tt') as TransactionHourConverted,
s.NetSalesPerHour, 
s.TransactionCountPerHour, 
--s.UnitSoldPerHour, 
s.UnitsSoldPerHour as UnitSoldPerHour,
s.DPT, 
s.UPT, 
isnull(s.SkinsPerHour,0) as SkinsPerHour, 
s.ShoesPerHour, 
s.StuffersPerHour, 
s.ShoesPct as ShoesPctRaw, 
case when s.ShoesPct >= 1 
		then 1--00
	when s.ShoesPct is null 
		then 0
	else s.ShoesPct--*100 
	end as ShoesPercentage, 
s.StuffersPct as StufferPctRaw,
case when s.StuffersPct >= 1 
		then 1--00
	when s.StuffersPct is null 
		then 0
	else s.StuffersPct--*100
	end as StufferPercentage
from #Summary3 s
order by 1
```

