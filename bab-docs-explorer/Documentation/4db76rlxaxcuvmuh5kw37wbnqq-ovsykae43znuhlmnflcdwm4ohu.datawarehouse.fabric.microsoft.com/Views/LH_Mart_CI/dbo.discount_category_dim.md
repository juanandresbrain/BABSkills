# dbo.discount_category_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.discount_category_dim"]
    dbo_discount_category_dim(["dbo.discount_category_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.discount_category_dim |

## View Code

```sql
; CREATE   VIEW discount_category_dim AS SELECT * FROM LH_Mart.dbo.discount_category_dim;
```

