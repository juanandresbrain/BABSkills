# WMS.vwModeOfDeliveryWeb

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwModeOfDeliveryWeb"]
    WMS_ModeOfDeliveryWeb(["WMS.ModeOfDeliveryWeb"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ModeOfDeliveryWeb |

## View Code

```sql
CREATE VIEW [WMS].[vwModeOfDeliveryWeb]
AS
SELECT ISNULL(ROW_NUMBER() OVER(ORDER BY [SHIP_VIA]), -1) AS ModeOfDeliveryWeb
      ,[SHIP_VIA]
      ,[SHIP_VIA_DESC]
      ,[ModeOfDelivery]
      ,[CarrierCode]
      ,[CarrierService]
  FROM [IntegrationStaging].[WMS].[ModeOfDeliveryWeb]
```

