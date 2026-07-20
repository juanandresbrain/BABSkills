# dbo.emailfactrollupstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailfactrollupstage"]
    dbo_emailfactrollupstage(["dbo.emailfactrollupstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailfactrollupstage |

## View Code

```sql
; CREATE   VIEW [dbo].[emailfactrollupstage] AS SELECT [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [LastSendDate], [LastClickDate], [LastOpenDate], [LastBounceDate], [LastUnSubscribeDate] FROM [dbo].[emailfactrollupstage]
```

