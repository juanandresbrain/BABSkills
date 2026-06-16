# WMS.spStoreShipmentReportTotalsD365

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spStoreShipmentReportTotalsD365"]
    WMS_ShippedNotReceived_StoreReportStage(["WMS.ShippedNotReceived_StoreReportStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ShippedNotReceived_StoreReportStage |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spStoreShipmentReportTotalsD365]
@DateDiff integer, @storeNumber varchar(50)

as 
set nocount on

;
with totals1 as
(
select ToWarehouse, sum(ItemQty) as 'ItemTotal',
count(distinct(LicensePlate)) as 'CartonTotal'
from [WMS].[ShippedNotReceived_StoreReportStage] 
where ToWarehouse = @storeNumber
and datediff(dd, ShipDate, getdate()) <= @DateDiff
group by ToWarehouse
),
totals2 as
(
select ToWarehouse, count(distinct(LicensePlate)) as 'MiscCartonTotal'
from [WMS].[ShippedNotReceived_StoreReportStage] 
where isMiscCarton = 1
and ToWarehouse = @storeNumber
and datediff(dd, ShipDate, getdate()) <= @DateDiff
group by ToWarehouse
)
select t1.ItemTotal, t1.CartonTotal, t2.MiscCartonTotal 
from totals1 t1 
join totals2 t2 on t1.ToWarehouse = t2.ToWarehouse
```

