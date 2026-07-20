# dbo.franchiseeproductattribute

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseeproductattribute"]
    dbo_franchiseeproductattribute(["dbo.franchiseeproductattribute"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseeproductattribute |

## View Code

```sql
; CREATE   VIEW franchiseeproductattribute AS SELECT * FROM LH_Mart.dbo.franchiseeproductattribute;
```

