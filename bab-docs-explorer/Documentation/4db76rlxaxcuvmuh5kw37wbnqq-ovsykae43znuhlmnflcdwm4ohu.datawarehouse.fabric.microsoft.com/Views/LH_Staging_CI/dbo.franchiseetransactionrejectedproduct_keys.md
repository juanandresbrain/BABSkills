# dbo.franchiseetransactionrejectedproduct_keys

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionrejectedproduct_keys"]
    dbo_franchiseetransactionrejectedproduct_keys(["dbo.franchiseetransactionrejectedproduct_keys"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionrejectedproduct_keys |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionrejectedproduct_keys] AS SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [Style] COLLATE Latin1_General_CI_AS AS [Style], [Units], [Cost], [GrossSales], [Discount], [VAT] FROM [dbo].[franchiseetransactionrejectedproduct_keys]
```

