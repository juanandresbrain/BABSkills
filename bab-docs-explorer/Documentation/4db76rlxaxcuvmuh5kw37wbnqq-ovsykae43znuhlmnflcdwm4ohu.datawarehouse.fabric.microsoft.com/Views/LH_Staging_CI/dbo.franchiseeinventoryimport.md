# dbo.franchiseeinventoryimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseeinventoryimport"]
    dbo_franchiseeinventoryimport(["dbo.franchiseeinventoryimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseeinventoryimport |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseeinventoryimport] AS SELECT [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [InventoryDate], [Style] COLLATE Latin1_General_CI_AS AS [Style], [OnHand], [Cost], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee] FROM [dbo].[franchiseeinventoryimport]
```

