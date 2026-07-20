# domo.vwma_warehousedim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["domo.vwma_warehousedim"]
    dbo_domo_vwma_warehousedim(["dbo.domo_vwma_warehousedim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.domo_vwma_warehousedim |

## View Code

```sql
; CREATE   VIEW domo.vwma_warehousedim AS SELECT * FROM LH_Mart.dbo.domo_vwma_warehousedim;
```

