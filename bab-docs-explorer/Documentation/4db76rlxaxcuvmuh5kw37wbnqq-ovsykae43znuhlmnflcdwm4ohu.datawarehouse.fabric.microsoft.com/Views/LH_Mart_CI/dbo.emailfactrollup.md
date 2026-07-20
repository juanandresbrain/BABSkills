# dbo.emailfactrollup

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailfactrollup"]
    dbo_emailfactrollup(["dbo.emailfactrollup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailfactrollup |

## View Code

```sql
; CREATE   VIEW [dbo].[emailfactrollup] AS     SELECT [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [LastSendDate], [LastClickDate], [LastOpenDate], [LastBounceDate], [LastUnSubscribeDate]     FROM [dbo].[emailfactrollup]
```

