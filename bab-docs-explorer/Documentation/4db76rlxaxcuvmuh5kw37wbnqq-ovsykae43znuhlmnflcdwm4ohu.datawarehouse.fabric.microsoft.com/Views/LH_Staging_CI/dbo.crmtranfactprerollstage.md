# dbo.crmtranfactprerollstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmtranfactprerollstage"]
    dbo_crmtranfactprerollstage(["dbo.crmtranfactprerollstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmtranfactprerollstage |

## View Code

```sql
; CREATE   VIEW [dbo].[crmtranfactprerollstage] AS SELECT [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [LifetimeTransactionCount], [LifetimeRecencyCount], [LifetimeSalesTotal], [FirstTransactionDate], [LastTransDate], [FirstStoreConcept] COLLATE Latin1_General_CI_AS AS [FirstStoreConcept], [LastTransStore] COLLATE Latin1_General_CI_AS AS [LastTransStore] FROM [dbo].[crmtranfactprerollstage]
```

