# dbo.emailbouncestage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailbouncestage"]
    dbo_emailbouncestage(["dbo.emailbouncestage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailbouncestage |

## View Code

```sql
; CREATE   VIEW [dbo].[emailbouncestage] AS SELECT [ClientID], [SendID], [SubscriberKey] COLLATE Latin1_General_CI_AS AS [SubscriberKey], [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [BounceDate] FROM [dbo].[emailbouncestage]
```

