# dbo.tmpemailwebrev3

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpemailwebrev3"]
    dbo_tmpemailwebrev3(["dbo.tmpemailwebrev3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpemailwebrev3 |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpemailwebrev3] AS SELECT [OpenDate], [emailAddress] COLLATE Latin1_General_CI_AS AS [emailAddress], [rev] FROM [dbo].[tmpemailwebrev3]
```

