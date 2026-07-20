# dbo.tmp_franchiseefilesimportselectpurchaseorderinsert_za

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselectpurchaseorderinsert_za"]
    dbo_tmp_franchiseefilesimportselectpurchaseorderinsert_za(["dbo.tmp_franchiseefilesimportselectpurchaseorderinsert_za"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselectpurchaseorderinsert_za |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselectpurchaseorderinsert_za] AS SELECT [PurchaseOrderID] COLLATE Latin1_General_CI_AS AS [PurchaseOrderID], [PurchaseOrderLineID], [WarehouseID] COLLATE Latin1_General_CI_AS AS [WarehouseID], [Style] COLLATE Latin1_General_CI_AS AS [Style], [Units], [LinePrice], [DueDate], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee] FROM [dbo].[tmp_franchiseefilesimportselectpurchaseorderinsert_za]
```

