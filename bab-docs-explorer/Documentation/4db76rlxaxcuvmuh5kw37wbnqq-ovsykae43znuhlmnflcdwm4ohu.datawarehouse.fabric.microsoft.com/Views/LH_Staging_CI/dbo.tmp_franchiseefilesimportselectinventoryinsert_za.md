# dbo.tmp_franchiseefilesimportselectinventoryinsert_za

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselectinventoryinsert_za"]
    dbo_tmp_franchiseefilesimportselectinventoryinsert_za(["dbo.tmp_franchiseefilesimportselectinventoryinsert_za"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselectinventoryinsert_za |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselectinventoryinsert_za] AS SELECT [InventoryID] COLLATE Latin1_General_CI_AS AS [InventoryID], [InventoryLineNo], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [InventoryDate], [Style] COLLATE Latin1_General_CI_AS AS [Style], [OnHand], [Cost], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee] FROM [dbo].[tmp_franchiseefilesimportselectinventoryinsert_za]
```

