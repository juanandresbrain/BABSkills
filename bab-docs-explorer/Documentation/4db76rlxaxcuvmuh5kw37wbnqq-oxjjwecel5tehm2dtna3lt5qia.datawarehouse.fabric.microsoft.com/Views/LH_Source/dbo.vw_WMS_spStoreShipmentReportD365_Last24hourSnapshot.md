# dbo.vw_WMS_spStoreShipmentReportD365_Last24hourSnapshot

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_WMS_spStoreShipmentReportD365_Last24hourSnapshot"]
    dbo_integrationstaging_wms_shippednotreceived_storereportstage(["dbo.integrationstaging_wms_shippednotreceived_storereportstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.integrationstaging_wms_shippednotreceived_storereportstage |

## View Code

```sql
CREATE view dbo.vw_WMS_spStoreShipmentReportD365_Last24hourSnapshot
--@DateDiff integer, @StoreNumber varchar(50)
as

SELECT [OrderNumber]
      ,[LicensePlate]
      ,[ItemNumber]
      ,[Name]
      ,[FromWarehouse]
      ,[ToWarehouse]
      ,[ProductHierarchy]
      ,[ShipDate]
      ,[ItemQty]
      ,[CartonQty]
	  ,[isMiscCarton]
      ,[MiscCartonDetails]
	  ,[ShipConfirmUTCDateTime]
FROM [dbo].[integrationstaging_wms_shippednotreceived_storereportstage]
where  1=1 and DATEDIFF(hh, ShipConfirmUTCDateTime, getdate()) <= 32
```

