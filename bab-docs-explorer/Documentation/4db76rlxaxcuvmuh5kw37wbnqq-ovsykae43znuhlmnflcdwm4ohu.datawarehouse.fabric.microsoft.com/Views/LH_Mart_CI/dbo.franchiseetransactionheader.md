# dbo.franchiseetransactionheader

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionheader"]
    dbo_franchiseetransactionheader(["dbo.franchiseetransactionheader"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionheader |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionheader] AS     SELECT [FranchiseeTransactionHeaderID], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [TransactionDateTime], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [InsertDate], [BatchID] COLLATE Latin1_General_CI_AS AS [BatchID], [store_key], [date_key], [time_key], [UpdateDate]     FROM [dbo].[franchiseetransactionheader]
```

