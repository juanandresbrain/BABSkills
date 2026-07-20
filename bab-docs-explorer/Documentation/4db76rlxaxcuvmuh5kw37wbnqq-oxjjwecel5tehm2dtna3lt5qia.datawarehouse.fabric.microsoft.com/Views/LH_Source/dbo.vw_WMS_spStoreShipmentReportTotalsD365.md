# dbo.vw_WMS_spStoreShipmentReportTotalsD365

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_WMS_spStoreShipmentReportTotalsD365"]
    dbo_integrationstaging_wms_shippednotreceived_storereportstage(["dbo.integrationstaging_wms_shippednotreceived_storereportstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.integrationstaging_wms_shippednotreceived_storereportstage |

## View Code

```sql
CREATE view dbo.vw_WMS_spStoreShipmentReportTotalsD365
as 
with totals1 as
(
select ToWarehouse, sum(ItemQty) as 'ItemTotal',
count(distinct(LicensePlate)) as 'CartonTotal'
from [dbo].[integrationstaging_wms_shippednotreceived_storereportstage]
--where 
--ToWarehouse = @storeNumber
--and datediff(dd, ShipDate, getdate()) <= @DateDiff
group by ToWarehouse
),
totals2 as
(
select ToWarehouse, count(distinct(LicensePlate)) as 'MiscCartonTotal'
from [dbo].[integrationstaging_wms_shippednotreceived_storereportstage]
where isMiscCarton = 1
--and ToWarehouse = @storeNumber
--and datediff(dd, ShipDate, getdate()) <= @DateDiff
group by ToWarehouse
)
select isnull(t1.ItemTotal,0) as ItemTotal, isnull(t1.CartonTotal,0) as CartonTotal, isnull(t2.MiscCartonTotal,0) as MiscCartonTotal 
from totals1 t1 
left join totals2 t2 on t1.ToWarehouse = t2.ToWarehouse
```

