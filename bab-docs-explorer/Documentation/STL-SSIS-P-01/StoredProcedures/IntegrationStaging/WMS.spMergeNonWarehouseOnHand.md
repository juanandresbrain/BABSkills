# WMS.spMergeNonWarehouseOnHand

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMergeNonWarehouseOnHand"]
    WMS_NonWarehouseOnHand(["WMS.NonWarehouseOnHand"]) --> SP
    wms_NonWarehouseOnHandStage(["wms.NonWarehouseOnHandStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.NonWarehouseOnHand |
| wms.NonWarehouseOnHandStage |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMergeNonWarehouseOnHand] 

as 
--=================================================================================================
--	Dan Tweedie	2019-11-11	Created proc to merge staged inventory data captured from Dynamics WMS
--	Tim Callahan 2020-11-09 Created proc to handly 9980 only 
--	Tim Callahan 2020-11-16 Updated proc with new field names as d365 entity field name changed
--=================================================================================================

set nocount on

merge into WMS.NonWarehouseOnHand as target 
--using wms.NonWarehouseOnHandStage as source
using  
(
select 
 Arrived
,AvailNoWork
,dataAreaId
,InventLocationId
,InventSiteId
,InventStatusId
,ItemId
,OnOrder
,Ordered
,PhysicalInvent
,Picked
,ReservedNoLocation
,ReservOrdered
from wms.NonWarehouseOnHandStage 
where 1=1
and TRY_CAST(InventLocationId AS INT) IS NOT NULL -- Excludes in transit -T warehouses no need to maintain that data
group by 
 Arrived
,AvailNoWork
,dataAreaId
,InventLocationId
,InventSiteId
,InventStatusId
,ItemId
,OnOrder
,Ordered
,PhysicalInvent
,Picked
,ReservedNoLocation
,ReservOrdered

) as source 
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
```

