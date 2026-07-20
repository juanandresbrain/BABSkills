# dbo.metric_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.metric_dim"]
    dbo_metric_dim(["dbo.metric_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.metric_dim |

## View Code

```sql
;

CREATE VIEW dbo.metric_dim AS SELECT metric_dim_key, name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS name, description COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS description, source COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS source FROM LH_Mart.dbo.metric_dim;
```

