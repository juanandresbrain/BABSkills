# dbo.tmpcrmtransactions

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpcrmtransactions"]
    dbo_tmpcrmtransactions(["dbo.tmpcrmtransactions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpcrmtransactions |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpcrmtransactions] AS SELECT [TransactionID], [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [TransactionYear], [TransacionMonth], [TransactionDate], [StoreConcept] COLLATE Latin1_General_CI_AS AS [StoreConcept], [LifetimeVisitNumber], [KeyStory] COLLATE Latin1_General_CI_AS AS [KeyStory], [ConsumerGroup] COLLATE Latin1_General_CI_AS AS [ConsumerGroup], [Department] COLLATE Latin1_General_CI_AS AS [Department], [LicensedOrNot], [Units], [Sales], [Country] COLLATE Latin1_General_CI_AS AS [Country], [StoreNumber] COLLATE Latin1_General_CI_AS AS [StoreNumber], [sku] COLLATE Latin1_General_CI_AS AS [sku], [ProductKey] FROM [dbo].[tmpcrmtransactions]
```

