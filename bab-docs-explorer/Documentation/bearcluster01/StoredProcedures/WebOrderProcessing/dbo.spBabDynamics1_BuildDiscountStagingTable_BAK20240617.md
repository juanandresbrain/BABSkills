# dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617"]
    dbo_DynamicsDiscountLineStage(["dbo.DynamicsDiscountLineStage"]) --> SP
    dbo_DynamicsDiscountSumStage(["dbo.DynamicsDiscountSumStage"]) --> SP
    dbo_WebDemandOrderItemZ(["dbo.WebDemandOrderItemZ"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DynamicsDiscountLineStage |
| dbo.DynamicsDiscountSumStage |
| dbo.WebDemandOrderItemZ |

## Stored Procedure Code

```sql
---- =====================================================================================================
---- Name: spBabDynamics1_BuildDiscountStagingTable
---- Revision History
----		Name:			Date:			Comments:
----		Tim Callahan	06/13/2024		Initial Release

---- =====================================================================================================
CREATE PROCEDURE [dbo].[spBabDynamics1_BuildDiscountStagingTable_BAK20240617]

@DaysBack int

as


-- Truncate STaging Tables 
truncate table DynamicsDiscountLineStage
truncate table DynamicsDiscountSumStage 
;

-- Variable Section for Manual Execution 
--Declare @DaysBack int
--set @Daysback = 3
;

IF OBJECT_ID(N'tempdb..#MaxOrderLine') IS NOT NULL
DROP TABLE #MaxOrderLine
; 

select 
i.OrderNumber, 
i.OrderLineNumber, 
max (LastUpdateDateUTC) as MaxLineUtc
,max(InsertDate) as MaxInsertDate
into #MaxOrderLine
from WebDemandOrderItemZ i (nolock) 
where 1=1
and cast (i.LastUpdateDateUTC as date)  > = getdate()-@Daysback
--and i.OrderNumber = @OrderNumber
group by
i.OrderNumber, 
i.OrderLineNumber


--  Build DiscountLinePrep Temp Table 
IF OBJECT_ID(N'tempdb..#DiscountLinePrep') IS NOT NULL
DROP TABLE #DiscountLinePrep
; 

--Capture Transaction Level Discounts 
--Our Deck data does not have multiple lines for each discount 
select 
case
	when i.SiteCode = 'UK' and i.WarehouseCode is null 
		then concat('2013','-','002','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber) 
	when i.SiteCode = 'UK' and isnull(i.WarehouseCode,'0000') = '2013'
		then concat(i.WarehouseCode,'-','002','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber) 
	when i.SiteCode = 'UK' and isnull(i.WarehouseCode,'0000') <> '2013'
		then concat(i.WarehouseCode,'-','052','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber) 			
	when i.SiteCode = 'US'
		then concat('1',right(i.WarehouseCode,3),'-','052','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber) 
	else null 
end	as TransactionKey
,i.OrderDiscount  as Amount 
,i.OrderDiscount  as DiscountCost
,'Manual' as DiscountOriginType
, case 
	when i.SiteCode = 'UK' and i.WarehouseCode is not null 
		then concat(i.WarehouseCode,'INT') 
	when i.SiteCode = 'UK' and i.WarehouseCode is null 
		then concat('2013','INT') 
	when i.SiteCode = 'US'
		then concat ('1',right(i.WarehouseCode,3),'INT')
	else null 
end as RetailTerminalId
,case
	when i.SiteCode = 'UK' and i.WarehouseCode is null 
		then concat('2013','-','002','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber,'_1') 
	when i.SiteCode = 'UK' and isnull(i.WarehouseCode,'0000') = '2013'
		then concat(i.WarehouseCode,'-','002','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber,'_1') 
	when i.SiteCode = 'UK'and isnull(i.WarehouseCode,'0000') <> '2013'
		then concat(i.WarehouseCode,'-','052','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber,'_1') 		
	when i.SiteCode = 'US'
		then concat('1',right(i.WarehouseCode,3),'-','052','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber,'_1') 
	else null 
end	as RetailTransactionId
,'LookupRequired' as BABIntRetailOperatingUnitNumber
,null as Percentage
, case 
	when i.SiteCode = 'UK' and i.WarehouseCode is not null 
		then i.WarehouseCode
	when i.SiteCode = 'UK' and i.WarehouseCode is null 
		then '2013'
	when i.SiteCode = 'US'
		then concat ('1',right(i.WarehouseCode,3))
	else null 
end as RetailStoreId
,i.OrderLineNumber as SaleLineNum
,'None' as CustomerDiscountType
,null as BABIntRetailProcessed
,'TotalDiscountAmount' as ManualDiscountType 
,case 
	when i.GiftCardNumber is not null
		then 'GiftCardDis'
	when i.GiftCardNumber is null 
		then 'MerchDis'
		else null 
	end as PeriodicDiscountOfferId
,case
	when i.SiteCode = 'UK'
		then '2110'
	when i.SiteCode = 'US'
		then '1100'	
	end as Entity
, I.LastUpdateDateUTC as CreateTime
--, null as Barcode 
, i.OrderNumber as Barcode 
into #DiscountLinePrep
from WebDemandOrderItemZ i (nolock) 
join #MaxOrderLine mol on mol.OrderNumber = i.OrderNumber
	and mol.OrderLineNumber = i.OrderLineNumber
	and mol.MaxLineUtc = i.LastUpdateDateUTC
	and mol.MaxInsertDate = i.InsertDate
where 1=1
and 
(
	i.SiteCode = 'US' and i.WarehouseCode is not null and isnull(i.WarehouseCode,'0000') not in ('0013') -- Exclude US WebStore E Gift Cards  and  US Webstore 
		and i.ItemStatus in ('Delivered','Picked Up','Return','Store Shipped')  -- Statuses to Include as of 6/14/2024 Per Comments from  Dan Tweedie
	or 
	i.SiteCode = 'UK' 
		and i.ItemStatus in ('Store Shipped','Return','Shipped','Picked Up','Gift Card Processed','Donation Processed','Gift Card Devalued') -- Statuses to Include as of 6/14/2024 Per Comments from  Dan Tweedie
) 
and cast (i.LastUpdateDateUTC as date)  > = getdate()-@Daysback
--and i.OrderNumber = @OrderNumber
and i.OrderDiscount <> 0.00 -- Header Level Transactions
union 
--Capture Line Level Discounts 
--Our Deck data does not have multiple lines for each discount 
select 
case
	when i.SiteCode = 'UK' and i.WarehouseCode is null 
		then concat('2013','-','002','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber) 
	when i.SiteCode = 'UK' and isnull(i.WarehouseCode,'0000') = '2013'
		then concat(i.WarehouseCode,'-','002','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber) 
	when i.SiteCode = 'UK'and isnull(i.WarehouseCode,'0000') <> '2013'
		then concat(i.WarehouseCode,'-','052','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber) 		
	when i.SiteCode = 'US'
		then concat('1',right(i.WarehouseCode,3),'-','052','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber) 
	else null 
end	as TransactionKey
,i.ItemDiscount  as Amount 
,i.ItemDiscount  as DiscountCost
,'Periodic' as DiscountOriginType
, case 
	when i.SiteCode = 'UK' and i.WarehouseCode is not null 
		then concat(i.WarehouseCode,'INT') 
	when i.SiteCode = 'UK' and i.WarehouseCode is null 
		then concat('2013','INT') 
	when i.SiteCode = 'US'
		then concat ('1',right(i.WarehouseCode,3),'INT')
	else null 
end as RetailTerminalId
,case
	when i.SiteCode = 'UK' and i.WarehouseCode is null 
		then concat('2013','-','002','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber,'_1') 
	when i.SiteCode = 'UK' and isnull(i.WarehouseCode,'0000') = '2013'
		then concat(i.WarehouseCode,'-','002','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber,'_1') 
	when i.SiteCode = 'UK'and isnull(i.WarehouseCode,'0000') <> '2013'
		then concat(i.WarehouseCode,'-','052','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber,'_1') 		
	when i.SiteCode = 'US'
		then concat('1',right(i.WarehouseCode,3),'-','052','-',convert (varchar,i.LastUpdateDateUTC,112),'-',i.OrderNumber,'_1') 
	else null 
end	as RetailTransactionId
,'LookupRequired' as BABIntRetailOperatingUnitNumber
,null as Percentage
, case 
	when i.SiteCode = 'UK' and i.WarehouseCode is not null 
		then i.WarehouseCode
	when i.SiteCode = 'UK' and i.WarehouseCode is null 
		then '2013'
	when i.SiteCode = 'US'
		then concat ('1',right(i.WarehouseCode,3))
	else null 
end as RetailStoreId
,i.OrderLineNumber as SaleLineNum
,'None' as CustomerDiscountType
,null as BABIntRetailProcessed
,'None' as ManualDiscountType 
,case 
	when i.GiftCardNumber is not null
		then 'GiftCardDis'
	when i.GiftCardNumber is null 
		then 'MerchDis'
		else null 
	end as PeriodicDiscountOfferId
,case
	when i.SiteCode = 'UK'
		then '2110'
	when i.SiteCode = 'US'
		then '1100'	
	end as Entity
, I.LastUpdateDateUTC as CreateTime
--, null as Barcode 
, i.OrderNumber as Barcode
from WebDemandOrderItemZ i (nolock) 
join #MaxOrderLine mol on mol.OrderNumber = i.OrderNumber
	and mol.OrderLineNumber = i.OrderLineNumber
	and mol.MaxLineUtc = i.LastUpdateDateUTC
	and mol.MaxInsertDate = i.InsertDate
where 1=1
and 
(
	i.SiteCode = 'US' and i.WarehouseCode is not null and isnull(i.WarehouseCode,'0000') not in ('0013') -- Exclude US WebStore E Gift Cards  and  US Webstore 
		and i.ItemStatus in ('Delivered','Picked Up','Return','Store Shipped')  -- Statuses to Include as of 6/14/2024 Per Comments from  Dan Tweedie
	or 
	i.SiteCode = 'UK' 
		and i.ItemStatus in ('Store Shipped','Return','Shipped','Picked Up','Gift Card Processed','Donation Processed','Gift Card Devalued') -- Statuses to Include as of 6/14/2024 Per Comments from  Dan Tweedie
) 
and cast (i.LastUpdateDateUTC as date)  > = getdate()-@Daysback
--and i.OrderNumber = @OrderNumber
and i.ItemDiscount <> 0.00 -- Line Level Transactions



-- DiscountLineBase 
IF OBJECT_ID(N'tempdb..#DiscountLineBase ') IS NOT NULL
DROP TABLE #DiscountLineBase
; 
select 
p.TransactionKey, 
p.Amount, 
p.DiscountCost, 
p.DiscountOriginType, 
p.RetailTerminalId, 
p.RetailTransactionId, 
p.BABIntRetailOperatingUnitNumber, 
ROW_NUMBER() OVER(
    PARTITION BY p.RetailTransactionId, p.SaleLineNum
    ORDER BY p.SaleLineNum
) as LineNum,
p.Percentage, 
p.RetailStoreId, 
p.SaleLineNum, 
p.CustomerDiscountType, 
p.BABIntRetailProcessed, 
p.ManualDiscountType, 
p.PeriodicDiscountOfferId, 
ROW_NUMBER() OVER(
    PARTITION BY p.RetailTransactionId
    ORDER BY p.SaleLineNum
) as BabRetailDiscountTransUniqueLineNum,
p.Entity, 
p.CreateTime, 
p.Barcode
into #DiscountLineBase
from #DiscountLinePrep p
where 1=1
--order by p.RetailTransactionId, p.SaleLineNum

-- Build Staging Table dynamicsdiscountlinestage
Insert into DynamicsDiscountLineStage
select 
dlb.TransactionKey, 
dlb.Amount, 
dlb.DiscountCost, 
dlb.DiscountOriginType, 
dlb.RetailTerminalId, 
dlb.RetailTransactionId, 
dlb.BABIntRetailOperatingUnitNumber, 
dlb.LineNum, 
dlb.Percentage, 
dlb.RetailStoreId, 
dlb.SaleLineNum, 
dlb.CustomerDiscountType, 
dlb.BABIntRetailProcessed, 
dlb.ManualDiscountType, 
dlb.PeriodicDiscountOfferId, 
dlb.BabRetailDiscountTransUniqueLineNum, 
dlb.Entity, 
dlb.CreateTime, 
dlb.Barcode
from #DiscountLineBase dlb 
group by 
dlb.TransactionKey, 
dlb.Amount, 
dlb.DiscountCost, 
dlb.DiscountOriginType, 
dlb.RetailTerminalId, 
dlb.RetailTransactionId, 
dlb.BABIntRetailOperatingUnitNumber, 
dlb.LineNum, 
dlb.Percentage, 
dlb.RetailStoreId, 
dlb.SaleLineNum, 
dlb.CustomerDiscountType, 
dlb.BABIntRetailProcessed, 
dlb.ManualDiscountType, 
dlb.PeriodicDiscountOfferId, 
dlb.BabRetailDiscountTransUniqueLineNum, 
dlb.Entity, 
dlb.CreateTime, 
dlb.Barcode


-- Build Discount Sum Tables 

--  Build dynamicsheaderdiscountssummed Temp Table 
IF OBJECT_ID(N'tempdb..#DynamicsHeaderDiscountSum') IS NOT NULL
DROP TABLE #DynamicsHeaderDiscountSum
; 

select
s.TransactionKey,
sum(s.amount) AS SumHeaderDiscounts,
s.RetailtransactionId,
s.Entity
into #DynamicsHeaderDiscountSum
FROM dynamicsdiscountlinestage s
WHERE 1 = 1 
AND s.discountorigintype = 'Manual'
GROUP BY 
s.TransactionKey,
s.RetailtransactionId,
s.Entity;

-- Build line dynamicslinediscountssum Table 
IF OBJECT_ID(N'tempdb..#DynamicsLineDiscountSum') IS NOT NULL
DROP TABLE #DynamicsLineDiscountSum
; 

select
s.TransactionKey,
sum(s.amount) AS SumlineDiscounts,
s.RetailtransactionId,
s.Entity
into #DynamicsLineDiscountSum
FROM dynamicsdiscountlinestage s
WHERE 1 = 1 
AND s.discountorigintype = 'Periodic'
GROUP BY 
s.TransactionKey,
s.RetailtransactionId,
s.Entity;


insert into DynamicsDiscountSumStage
select
dsl.RetailTransactionId,
isnull(h.sumheaderdiscounts,0.00)+isnull(l.sumlinediscounts,0.00) as DiscAmount,
isnull(h.sumheaderdiscounts,0.00) as TotalDiscAmount
--, l.sumlinediscounts
from dynamicsdiscountlinestage dsl
left join #DynamicsHeaderDiscountSum h  on h.RetailTransactionId = dsl.RetailTransactionId
left join #DynamicsLineDiscountSum l on l.RetailTransactionId = dsl.RetailTransactionId
where 1=1
group by 
dsl.RetailTransactionId,
isnull(h.sumheaderdiscounts,0.00)+isnull(l.sumlinediscounts,0.00) ,
h.sumheaderdiscounts
--, l.sumlinediscounts



-- Testing Only 
-- Review Staged Tables 
/*

select *
from DynamicsDiscountLineStage ds
where 1=1
--and RetailStoreId is NULL
order by ds.entity, ds.RetailTransactionId


select *
from DynamicsDiscountSumStage ds
where 1=1
order by ds.RetailTransactionId

*/
```

