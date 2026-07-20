# dbo.test_store_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.test_store_dim"]
    dbo_test_store_dim(["dbo.test_store_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.test_store_dim |

## View Code

```sql
; CREATE   VIEW test_store_dim AS SELECT * FROM LH_Mart.dbo.test_store_dim;
```

