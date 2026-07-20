# dbo.vwdw_merchandise_product_dimension

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_merchandise_product_dimension"]
    dbo_vwdw_product_dim_v3(["dbo.vwdw_product_dim_v3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwdw_product_dim_v3 |

## View Code

```sql
create view dbo.vwdw_merchandise_product_dimension
as
select * from  [dbo].[vwdw_product_dim_v3]
```

