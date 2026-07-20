# dbo.franchiseetransactionmerchandise

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionmerchandise"]
    dbo_franchiseetransactionmerchandise(["dbo.franchiseetransactionmerchandise"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionmerchandise |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionmerchandise] AS     SELECT [FranchiseeTransactionHeaderID], [FranchiseeTransactionMerchandiseID], [Style] COLLATE Latin1_General_CI_AS AS [Style], [Units], [Cost], [GrossSales], [Discount], [VAT], [InsertDate], [BatchID] COLLATE Latin1_General_CI_AS AS [BatchID], [product_key], [updateDate], [OriginalDiscount]     FROM [dbo].[franchiseetransactionmerchandise]
```

