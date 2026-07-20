# dbo.franchiseetransactionmerchandiseimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionmerchandiseimport"]
    dbo_franchiseetransactionmerchandiseimport(["dbo.franchiseetransactionmerchandiseimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionmerchandiseimport |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionmerchandiseimport] AS SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [Style] COLLATE Latin1_General_CI_AS AS [Style], [Units], [Cost], [GrossSales], [Discount], [VAT], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [OriginalDiscount] FROM [dbo].[franchiseetransactionmerchandiseimport]
```

