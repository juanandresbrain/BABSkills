# dbo.emaileventfact

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emaileventfact"]
    dbo_emaileventfact(["dbo.emaileventfact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emaileventfact |

## View Code

```sql
; CREATE   VIEW [dbo].[emaileventfact] AS     SELECT [ClientID], [SendID], [Subject] COLLATE Latin1_General_CI_AS AS [Subject], [EmailName] COLLATE Latin1_General_CI_AS AS [EmailName], [EventDate], [InsertDate], [UpdateDate]     FROM [dbo].[emaileventfact]
```

