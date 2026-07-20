# azure.productsbrf

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.productsbrf"]
    dbo_azure_productsbrf(["dbo.azure_productsbrf"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_productsbrf |

## View Code

```sql
; CREATE   VIEW azure.productsbrf AS SELECT * FROM LH_Mart.dbo.azure_productsbrf;
```

