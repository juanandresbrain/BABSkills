# dbo.franchiseeinventoryerror

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseeinventoryerror"]
    dbo_franchiseeinventoryerror(["dbo.franchiseeinventoryerror"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseeinventoryerror |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseeinventoryerror]
AS
    SELECT [InventoryID] COLLATE Latin1_General_CI_AS AS [InventoryID], [InventoryLineNo], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [InventoryDate] COLLATE Latin1_General_CI_AS AS [InventoryDate], [Style] COLLATE Latin1_General_CI_AS AS [Style], [OnHand] COLLATE Latin1_General_CI_AS AS [OnHand], [Cost] COLLATE Latin1_General_CI_AS AS [Cost], [InsertDate] COLLATE Latin1_General_CI_AS AS [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [ErrorDesc] COLLATE Latin1_General_CI_AS AS [ErrorDesc], [ErrorSource] COLLATE Latin1_General_CI_AS AS [ErrorSource]
    FROM LH_Staging.[dbo].[franchiseeinventoryerror]
```

