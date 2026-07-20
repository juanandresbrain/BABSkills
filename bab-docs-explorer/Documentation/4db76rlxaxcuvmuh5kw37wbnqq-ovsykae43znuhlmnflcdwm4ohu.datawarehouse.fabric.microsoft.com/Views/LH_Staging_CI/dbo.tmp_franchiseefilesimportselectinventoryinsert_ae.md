# dbo.tmp_franchiseefilesimportselectinventoryinsert_ae

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselectinventoryinsert_ae"]
    dbo_tmp_franchiseefilesimportselectinventoryinsert_ae(["dbo.tmp_franchiseefilesimportselectinventoryinsert_ae"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselectinventoryinsert_ae |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselectinventoryinsert_ae] AS SELECT [InventoryID] COLLATE Latin1_General_CI_AS AS [InventoryID], [InventoryLineNo], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [InventoryDate], [Style] COLLATE Latin1_General_CI_AS AS [Style], [OnHand], [Cost], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee] FROM [dbo].[tmp_franchiseefilesimportselectinventoryinsert_ae]
```

