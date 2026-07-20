# dbo.cmn_product_department_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.cmn_product_department_dim"]
    dbo_cmn_product_department_dim(["dbo.cmn_product_department_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.cmn_product_department_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[cmn_product_department_dim] AS     SELECT [cmn_department_code] COLLATE Latin1_General_CI_AS AS [cmn_department_code], [cmn_department] COLLATE Latin1_General_CI_AS AS [cmn_department]     FROM [dbo].[cmn_product_department_dim]
```

