# dbo.tmpemailwebrev1b

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpemailwebrev1b"]
    dbo_tmpemailwebrev1b(["dbo.tmpemailwebrev1b"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpemailwebrev1b |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpemailwebrev1b] AS SELECT [OpenDate], [emailAddress] COLLATE Latin1_General_CI_AS AS [emailAddress], [rev] FROM [dbo].[tmpemailwebrev1b]
```

