# dbo.franchiseetransactiongiftcard

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactiongiftcard"]
    dbo_franchiseetransactiongiftcard(["dbo.franchiseetransactiongiftcard"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactiongiftcard |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactiongiftcard] AS     SELECT [FranchiseeTransactionHeaderID], [FranchiseeTransactionGiftCardID], [Units], [GiftCardAmount], [Discount], [InsertDate], [BatchID] COLLATE Latin1_General_CI_AS AS [BatchID], [UpdateDate]     FROM [dbo].[franchiseetransactiongiftcard]
```

