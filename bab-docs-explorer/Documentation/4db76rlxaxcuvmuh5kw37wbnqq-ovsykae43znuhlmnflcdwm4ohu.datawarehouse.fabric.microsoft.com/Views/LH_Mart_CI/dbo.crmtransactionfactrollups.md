# dbo.crmtransactionfactrollups

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmtransactionfactrollups"]
    dbo_crmtransactionfactrollups(["dbo.crmtransactionfactrollups"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmtransactionfactrollups |

## View Code

```sql
; CREATE   VIEW [dbo].[crmtransactionfactrollups] AS     SELECT [TransactionID], [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [TransactionYear], [TransacionMonth], [TransactionDate], [StoreConcept] COLLATE Latin1_General_CI_AS AS [StoreConcept], [LifetimeVisitNumber], [KeyStory] COLLATE Latin1_General_CI_AS AS [KeyStory], [ConsumerGroup] COLLATE Latin1_General_CI_AS AS [ConsumerGroup], [Department] COLLATE Latin1_General_CI_AS AS [Department], [LicensedOrNot], [Units], [Sales], [InsertDate], [UpdateDate], [StoreNumber] COLLATE Latin1_General_CI_AS AS [StoreNumber], [Country] COLLATE Latin1_General_CI_AS AS [Country], [sku] COLLATE Latin1_General_CI_AS AS [sku]     FROM [dbo].[crmtransactionfactrollups]
```

