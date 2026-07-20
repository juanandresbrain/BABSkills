# dbo.tmpgavlkey

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpgavlkey"]
    dbo_tmpgavlkey(["dbo.tmpgavlkey"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpgavlkey |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpgavlkey] AS SELECT [recID] FROM [dbo].[tmpgavlkey]
```

