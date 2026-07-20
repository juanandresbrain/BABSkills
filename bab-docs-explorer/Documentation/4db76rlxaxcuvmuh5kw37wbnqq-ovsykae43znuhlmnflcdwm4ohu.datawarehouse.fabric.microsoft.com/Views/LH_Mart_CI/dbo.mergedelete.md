# dbo.mergedelete

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.mergedelete"]
    dbo_mergedelete(["dbo.mergedelete"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.mergedelete |

## View Code

```sql
; CREATE   VIEW mergedelete AS SELECT * FROM LH_Mart.dbo.mergedelete;
```

