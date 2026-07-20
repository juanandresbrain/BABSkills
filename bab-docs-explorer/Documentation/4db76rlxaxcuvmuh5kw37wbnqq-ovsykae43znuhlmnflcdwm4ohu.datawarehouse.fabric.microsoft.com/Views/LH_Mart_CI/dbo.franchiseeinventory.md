# dbo.franchiseeinventory

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseeinventory"]
    dbo_franchiseeinventory(["dbo.franchiseeinventory"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseeinventory |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseeinventory] AS     SELECT [InventoryID] COLLATE Latin1_General_CI_AS AS [InventoryID], [InventoryLineNo], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [InventoryDate], [Style] COLLATE Latin1_General_CI_AS AS [Style], [OnHand], [Cost], [InsertDate], [BatchID] COLLATE Latin1_General_CI_AS AS [BatchID]     FROM [dbo].[franchiseeinventory]
```

