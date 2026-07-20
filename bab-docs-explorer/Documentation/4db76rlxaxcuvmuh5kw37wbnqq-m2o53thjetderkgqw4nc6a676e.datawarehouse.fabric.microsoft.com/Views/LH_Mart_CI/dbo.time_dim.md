# dbo.time_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
CREATE VIEW dbo.time_dim AS SELECT time_key, hour, minute, daypart COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS daypart, half_hour_id, qtr_hour_id FROM LH_Mart.dbo.time_dim;
```

