# queries.snapshot_storecompdetail_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["queries.snapshot_storecompdetail_dim"]
    dbo_queries_snapshot_storecompdetail_dim(["dbo.queries_snapshot_storecompdetail_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.queries_snapshot_storecompdetail_dim |

## View Code

```sql
CREATE   VIEW queries.snapshot_storecompdetail_dim AS SELECT * FROM LH_Mart.dbo.queries_snapshot_storecompdetail_dim;
```

