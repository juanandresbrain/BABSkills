# dbo.tmpemailretrev3

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpemailretrev3"]
    dbo_tmpemailretrev3(["dbo.tmpemailretrev3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpemailretrev3 |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpemailretrev3] AS SELECT [OpenDate], [emailAddress] COLLATE Latin1_General_CI_AS AS [emailAddress], [rev] FROM [dbo].[tmpemailretrev3]
```

