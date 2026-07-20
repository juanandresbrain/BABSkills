# dbo.tmpemailfactretrev1b

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpemailfactretrev1b"]
    dbo_tmpemailfactretrev1b(["dbo.tmpemailfactretrev1b"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpemailfactretrev1b |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpemailfactretrev1b] AS SELECT [OpenDate], [emailAddress] COLLATE Latin1_General_CI_AS AS [emailAddress], [rev] FROM [dbo].[tmpemailfactretrev1b]
```

