# dbo.franchiseepurchaseorderimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseepurchaseorderimport"]
    dbo_franchiseepurchaseorderimport(["dbo.franchiseepurchaseorderimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseepurchaseorderimport |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseepurchaseorderimport]
AS
    SELECT [PurchaseOrderID] COLLATE Latin1_General_CI_AS AS [PurchaseOrderID], [WarehouseID] COLLATE Latin1_General_CI_AS AS [WarehouseID], [Style] COLLATE Latin1_General_CI_AS AS [Style], [Units], [LinePrice], [DueDate], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee]
    FROM LH_Staging.[dbo].[franchiseepurchaseorderimport]
```

