# dbo.vwloyaltystores

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwloyaltystores"]
    dbo_vwloyaltystores(["dbo.vwloyaltystores"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwloyaltystores |

## View Code

```sql
; CREATE   VIEW vwloyaltystores AS SELECT * FROM LH_Mart.dbo.vwloyaltystores;
```

