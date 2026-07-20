# dbo.tmp_franchiseefilesimportselecttransactionmerchandiseinsert_au

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselecttransactionmerchandiseinsert_au"]
    dbo_tmp_franchiseefilesimportselecttransactionmerchandiseinsert_au(["dbo.tmp_franchiseefilesimportselecttransactionmerchandiseinsert_au"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselecttransactionmerchandiseinsert_au |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselecttransactionmerchandiseinsert_au] AS SELECT [FranchiseeTransactionHeaderID], [FranchiseeTransactionMerchandiseID], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [Style] COLLATE Latin1_General_CI_AS AS [Style], [Units], [Cost], [GrossSales], [Discount], [VAT], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [product_key], [UpdateDate], [OriginalDiscount] FROM [dbo].[tmp_franchiseefilesimportselecttransactionmerchandiseinsert_au]
```

