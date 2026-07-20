# azure.prodlicense

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.prodlicense"]
    dbo_azure_prodlicense(["dbo.azure_prodlicense"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_prodlicense |

## View Code

```sql
; CREATE   VIEW azure.prodlicense AS SELECT * FROM LH_Mart.dbo.azure_prodlicense;
```

