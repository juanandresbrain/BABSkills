# dbo.time_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.time_dim"]
    dbo_time_dim(["dbo.time_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.time_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[time_dim] AS     SELECT [time_key], [hour], [minute], [daypart] COLLATE Latin1_General_CI_AS AS [daypart], [half_hour_id], [qtr_hour_id]     FROM [dbo].[time_dim]
```

