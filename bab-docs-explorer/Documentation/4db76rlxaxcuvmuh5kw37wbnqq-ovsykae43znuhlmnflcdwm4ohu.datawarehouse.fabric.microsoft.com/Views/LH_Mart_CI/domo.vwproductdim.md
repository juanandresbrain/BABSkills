# domo.vwproductdim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["domo.vwproductdim"]
    dbo_domo_vwproductdim(["dbo.domo_vwproductdim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.domo_vwproductdim |

## View Code

```sql
CREATE   VIEW domo.vwproductdim AS SELECT * FROM LH_Mart.dbo.domo_vwproductdim;
```

