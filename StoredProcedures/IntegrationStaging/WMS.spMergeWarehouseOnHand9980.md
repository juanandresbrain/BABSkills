# WMS.spMergeWarehouseOnHand9980

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMergeWarehouseOnHand9980"]
    WMS_WarehouseOnHand9980(["WMS.WarehouseOnHand9980"]) --> SP
    wms_WarehouseOnHand9980Stage(["wms.WarehouseOnHand9980Stage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.WarehouseOnHand9980 |
| wms.WarehouseOnHand9980Stage |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMergeWarehouseOnHand9980] 

as 
--=================================================================================================
--	Dan Tweedie	2019-11-11	Created proc to merge staged inventory data captured from Dynamics WMS
--	Tim Callahan 2020-11-09 Created proc to handly 9980 only 
--	Tim Callahan 2020-11-16 Updated proc with new field names as d365 entity field name changed
--=================================================================================================

set nocount on

merge into WMS.WarehouseOnHand9980 as target 
using wms.WarehouseOnHand9980Stage as source
on 
	(
		target.DataAreaID=source.DataAreaID
		and
		target.InventLocationId=source.InventLocationID
		and
		target.InventSiteID=source.InventSiteID
		and 
		target.ItemId=source.ItemId
		and
		target.InventStatusId=source.InventStatusId
	)
when matched 
and 
	(
	isnull	(target.Arrived,0) <> isnull (source.Arrived,0)
or	isnull	(target.AvailNoWork,0) <>	isnull(source.AvailNoWork,0)
or	isnull	(target.InventStatusId,'x')	<>	isnull(source.InventStatusId,0)
or	isnull	(target.OnOrder,0)<> isnull(source.OnOrder,0)
or	isnull	(target.Ordered,0)<> isnull(source.Ordered,0)
or	isnull	(target.PhysicalInvent,0)<>	isnull(source.PhysicalInvent,0)
or	isnull	(target.Picked,0)<>	isnull(source.Picked,0)
or	isnull	(target.ReservOrdered,0) <>	isnull(source.ReservOrdered,0)
or	isnull	(target.ReservedNoLocation,0) <> isnull(source.ReservedNoLocation,0)

	)
then update
	set
		target.Arrived=source.Arrived,
		target.AvailNoWork=source.AvailNoWork,
		target.InventStatusId=source.InventStatusId,
		target.OnOrder=source.OnOrder,
		target.Ordered =source.Ordered ,
		target.PhysicalInvent=source.PhysicalInvent,
		target.Picked=source.Picked,
		target.ReservOrdered=source.ReservOrdered,
		target.ReservedNoLocation=source.ReservedNoLocation,
		target.UpdateDate=getdate()

when not matched by target
then insert 
	(
		Arrived, 
		AvailNoWork, 
		dataAreaId, 
		InventLocationId, 
		InventSiteId, 
		InventStatusId, 
		ItemId, 
		OnOrder, 
		Ordered, 
		PhysicalInvent, 
		Picked, 
		ReservedNoLocation, 
		ReservOrdered,		
		InsertDate

	)
values
		(
		source.Arrived, 
		source.AvailNoWork, 
		source.dataAreaId, 
		source.InventLocationId, 
		source.InventSiteId, 
		source.InventStatusId, 
		source.ItemId, 
		source.OnOrder, 
		source.Ordered, 
		source.PhysicalInvent, 
		source.Picked, 
		source.ReservedNoLocation, 
		source.ReservOrdered, 		
		getdate()

	)
when not matched by source
then update
	set
		target.Arrived=0,
		target.AvailNoWork=0,
		target.InventStatusId=0,
		target.OnOrder=0,
		target.Ordered=0,
		target.PhysicalInvent=0,
		target.Picked=0,
		target.ReservedNoLocation=0,
		target.ReservOrdered=0,		
		target.UpdateDate=getdate()
;



WMS,spMergeWholesaleOnOrder,create proc WMS.spMergeWholesaleOnOrder 

as 

set nocount on

merge into WMS.WholesaleOnOrder as target 
using WMS.WholesaleOnOrderStage as source
	on target.PurchaseOrderNumber=source.PurchaseOrderNumber
	and target.LineNumber=source.LineNumber
when matched and
	isnull(target.PurchaseOrderLineStatus,'x')<>isnull(source.PurchaseOrderLineStatus,'x')
	or
	isnull(target.ItemNumber,'x')<>isnull(source.ItemNumber,'x')
	or
	isnull(target.RemainPurchPhysical,0)<>isnull(source.RemainPurchPhysical,0)
	or
	isnull(target.OrderedPurchaseQuantity,0)<>isnull(source.OrderedPurchaseQuantity,0)
then update
	set 
		target.PurchaseOrderLineStatus=source.PurchaseOrderLineStatus,
		target.ItemNumber=source.ItemNumber,
		target.RemainPurchPhysical=source.RemainPurchPhysical,
		target.OrderedPurchaseQuantity=source.OrderedPurchaseQuantity,
		target.UpdateDate=getdate()
when not matched by target
then insert 
	(
		PurchaseOrderLineStatus,
		ItemNumber,
		RemainPurchPhysical,
		OrderedPurchaseQuantity,
		InsertDate
	)
	values
	(
		source.PurchaseOrderLineStatus,
		source.ItemNumber,
		source.RemainPurchPhysical,
		source.OrderedPurchaseQuantity,
		getdate()
	)
;
```

