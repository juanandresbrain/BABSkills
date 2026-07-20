# dbo.tmpranktwo

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpranktwo"]
    dbo_tmpranktwo(["dbo.tmpranktwo"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpranktwo |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpranktwo] AS SELECT [LifetimeVisitSequence], [keyStory] COLLATE Latin1_General_CI_AS AS [keyStory], [isFreshCustomer], [KeyRankPerSequenceNewVOldCustomers], [KeyRankPerSequenceGlobal] FROM [dbo].[tmpranktwo]
```

