# WMS.vwNonWarehouseOnHand

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwNonWarehouseOnHand"]
    WMS_NonWarehouseOnHand(["WMS.NonWarehouseOnHand"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.NonWarehouseOnHand |

## View Code

```sql
CREATE VIEW [WMS].[vwNonWarehouseOnHand] as 
SELECT
  i.InventLocationId AS InventLocationId,
  i.dataAreaId AS dataAreaId,
  i.ItemId AS StyleCode,
  CAST(SUM(i.ReservedNoLocation + i.AvailNoWork + i.Picked) AS BIGINT) AS Qty
  --,  COUNT_BIG(*) AS Row_Count
FROM WMS.NonWarehouseOnHand i
WHERE 1=1
and TRY_CAST(i.InventLocationId AS INT) IS NOT NULL
--and ISNUMERIC(i.InventLocationId) = 1
--and left(i.InventLocationId_Short,1) in ('1', '2')
--and i.dataAreaId in (1100, 1700, 2110) -- We only stage these entities anyway 
and i.InventLocationId not in ('9980', '9960', '9970') -- We Already exclude these in AX Connector 
and i.InventLocationId LIKE '[12]%'  -- faster than LEFT(...,1)
and i.ItemId LIKE '[0-9]%'  

GROUP BY
  i.InventLocationId,
  i.dataAreaId,
  i.ItemId;


WMS,vwNonWhsePhysicalInventory,create view WMS.vwNonWhsePhysicalInventory

as 

with
InventoryLocations as
	(
		select d.InventLocationId
		from WMS.NonWarehouseOnHand d
		where d.dataAreaId in (1100, 1700, 2110)
		and d.InventLocationId not in ('9980', '9960', '9970')
		and isnumeric(d.InventLocationId)=1
		and left(InventLocationId,1) in ('1', '2')
		group by d.InventLocationId
	),
LocationCodes as
	(
		select i.InventLocationId, w.LocationCode
		from InventoryLocations i
		join ERP.vwWarehouseIDToLocationCode w on i.InventLocationId=w.WarehouseId
		group by i.InventLocationId, w.LocationCode
	)
select 
	lc.LocationCode,
	cast(i.ItemId as varchar(6)) as StyleCode,
	cast(sum (i.ReservedNoLocation + i.AvailNoWork + i.Picked) as bigint) as Qty, 
	getdate() as LoadDate
from WMS.NonWarehouseOnHand i with (nolock)
join LocationCodes lc on i.InventLocationID=lc.InventLocationID
where 1=1
and isnumeric(left(i.ItemId,1)) = 1
group by 
	i.InventLocationId,
	i.ItemId,
	lc.LocationCode
```

