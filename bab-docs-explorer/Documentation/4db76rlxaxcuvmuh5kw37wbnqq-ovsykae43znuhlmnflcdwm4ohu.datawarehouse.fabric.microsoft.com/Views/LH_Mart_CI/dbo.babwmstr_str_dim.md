# dbo.babwmstr_str_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.babwmstr_str_dim"]
    dbo_babwmstr_str_dim(["dbo.babwmstr_str_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.babwmstr_str_dim |

## View Code

```sql
; CREATE   VIEW babwmstr_str_dim AS SELECT * FROM LH_Mart.dbo.babwmstr_str_dim;
```

