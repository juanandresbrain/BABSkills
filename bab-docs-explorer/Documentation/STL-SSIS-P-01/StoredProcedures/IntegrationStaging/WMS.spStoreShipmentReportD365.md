# WMS.spStoreShipmentReportD365

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spStoreShipmentReportD365"]
    WMS_ShippedNotReceived_StoreReportStage(["WMS.ShippedNotReceived_StoreReportStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ShippedNotReceived_StoreReportStage |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spStoreShipmentReportD365]
@DateDiff integer, @StoreNumber varchar(50)

WITH RECOMPILE 

as 

set nocount on 


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
FROM [WMS].[ShippedNotReceived_StoreReportStage]
where  1=1
and DATEDIFF(dd, [ShipDate], getdate()) <= @DateDiff
and [ToWarehouse] = @storeNumber
```

