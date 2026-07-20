# dbo.tmpemailretrev2a

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpemailretrev2a"]
    dbo_tmpemailretrev2a(["dbo.tmpemailretrev2a"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpemailretrev2a |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpemailretrev2a] AS SELECT [OpenDate], [emailAddress] COLLATE Latin1_General_CI_AS AS [emailAddress], [rev] FROM [dbo].[tmpemailretrev2a]
```

