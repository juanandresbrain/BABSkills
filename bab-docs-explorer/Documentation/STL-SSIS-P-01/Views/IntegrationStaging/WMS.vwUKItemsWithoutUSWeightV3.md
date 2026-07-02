# WMS.vwUKItemsWithoutUSWeightV3

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwUKItemsWithoutUSWeightV3"]
    azure_vwMerchOnOrder(["azure.vwMerchOnOrder"]) --> VIEW
    azure_vwProducts(["azure.vwProducts"]) --> VIEW
    dbo_ClipperInventoryTC(["dbo.ClipperInventoryTC"]) --> VIEW
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_store_dim(["dbo.store_dim"]) --> VIEW
    erp_PurchaseOrderLines(["erp.PurchaseOrderLines"]) --> VIEW
    Reporting_UKItemCostUom(["Reporting.UKItemCostUom"]) --> VIEW
    wms_ItemMaster(["wms.ItemMaster"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| azure.vwMerchOnOrder |
| azure.vwProducts |
| dbo.ClipperInventoryTC |
| dbo.date_dim |
| dbo.store_dim |
| erp.PurchaseOrderLines |
| Reporting.UKItemCostUom |
| wms.ItemMaster |

## View Code

```sql
CREATE view [WMS].[vwUKItemsWithoutUSWeightV3]

as

with 
ItemsOnPO as
	(
		select DISTINCT 
			ItemID as ProductNumber,
			max(InsertDate) CreateDate
		from erp.PurchaseOrderLines
		where left(ItemID,1) in ('4','5','6')
		group by ItemID
		UNION
		select distinct p.Style,
			cast(max(dd.actual_date) as date) as CreateDate
		from papamart.dw.azure.vwMerchOnOrder o
		join papamart.dw.azure.vwProducts p on o.style_id=p.ProductKey
		join papamart.dw.dbo.date_dim dd on cast(o.DateKey as date)=cast(dd.actual_date as date)
		join papamart.dw.dbo.store_dim sd on o.Location_id=sd.store_key
		where sd.store_id = '2970'
		group by p.Style
	),
MaxPO as
	(
		select ProductNumber, max(CreateDate) CreateDate
		from ItemsOnPO 
		group by ProductNumber
	)


select u.ProductNumber, 
u.ProductDescription, 
im.NecessaryProductionWorkingTimeSchedulingPropertyId as ItemType, 
'Missing UOM Conversion to WMEA' as Issue
from Reporting.[UKItemCostUom] u 
join wms.ItemMaster im on u.ProductNumber=im.ProductNumber
		and im.Entity = '2110'	
where u.WeightKg is null
and (u.ProductNumber in (select distinct style_code from bedrockdb02.me_01.dbo.ClipperInventoryTC where booked> 0 or available > 0 or allocated > 0 )
	or u.ProductNumber in (select distinct ProductNumber from ItemsOnPO ) 
)
union all 
select u.ProductNumber, 
u.ProductDescription, 
im.NecessaryProductionWorkingTimeSchedulingPropertyId as ItemType, 
'Zero Cost' as Issue
from Reporting.[UKItemCostUom] u 
join wms.ItemMaster im on u.ProductNumber=im.ProductNumber
		and im.Entity = '2110'	
where U.UnitCost = 0
and (u.ProductNumber in (select distinct style_code from bedrockdb02.me_01.dbo.ClipperInventoryTC where booked> 0 or available > 0 or allocated > 0 )
	--or u.ProductNumber in (select distinct ProductNumber from ItemsOnPO ) -- Removed OnOrder per Santiago's request on 1/5/2021 as OnOrder items that have  never been received will not have cost
)

UNION ALL 
select u.ProductNumber, 
u.ProductDescription, 
im.NecessaryProductionWorkingTimeSchedulingPropertyId as ItemType, 
'Zero Weight' as Issue
from Reporting.[UKItemCostUom] u 
join wms.ItemMaster im on u.ProductNumber=im.ProductNumber
		and im.Entity = '2110'	
where ((u.WEIGHTKG IS NOT NULL and u.WeightKg = '0') or (u.WeightKG is null) )
and (u.ProductNumber in (select distinct style_code from bedrockdb02.me_01.dbo.ClipperInventoryTC where booked> 0 or available > 0 or allocated > 0 )
	or u.ProductNumber in (select distinct ProductNumber from ItemsOnPO ) 
)
```

