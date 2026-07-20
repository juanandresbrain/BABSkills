# dbo.tmpliccode

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpliccode"]
    dbo_tmpliccode(["dbo.tmpliccode"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpliccode |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpliccode] AS     SELECT [KeyStory] COLLATE Latin1_General_CI_AS AS [KeyStory], [licenseCode] COLLATE Latin1_General_CI_AS AS [licenseCode]     FROM [dbo].[tmpliccode]
```

