# dbo.store_dim_backup

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.store_dim_backup"]
    dbo_store_dim_backup(["dbo.store_dim_backup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.store_dim_backup |

## View Code

```sql
; CREATE   VIEW store_dim_backup AS SELECT * FROM LH_Mart.dbo.store_dim_backup;
```

