# dbo.AVAIL_980_SUPPLY_V2

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.AVAIL_980_SUPPLY_V2"]
    dbo_AVAIL_980_SUPPLY(["dbo.AVAIL_980_SUPPLY"]) --> VIEW
    ERP_vwAvailableSupplies(["ERP.vwAvailableSupplies"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.AVAIL_980_SUPPLY |
| ERP.vwAvailableSupplies |

## View Code

```sql
CREATE VIEW [dbo].[AVAIL_980_SUPPLY_V2]
AS
SELECT *
FROM 
(
	SELECT style FROM 
	[WMDB01].[WMPROD].[dbo].[AVAIL_980_SUPPLY]
	EXCEPT
	SELECT ItemNumber AS style
	FROM [STL-SSIS-P-01].IntegrationStaging.ERP.vwAvailableSupplies
	WHERE InventoryWarehouseId IN ('9980')-- AND AvailableOnHandQuantity > 0
) AS innerQry
UNION
SELECT ItemNumber AS style
FROM [STL-SSIS-P-01].IntegrationStaging.ERP.vwAvailableSupplies
WHERE InventoryWarehouseId IN ('9980') AND AvailableOnHandQuantity > 0
```

