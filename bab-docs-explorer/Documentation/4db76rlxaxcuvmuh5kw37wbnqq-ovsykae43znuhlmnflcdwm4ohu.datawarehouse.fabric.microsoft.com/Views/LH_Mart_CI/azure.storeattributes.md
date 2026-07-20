# azure.storeattributes

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.storeattributes"]
    dbo_azure_storeattributes(["dbo.azure_storeattributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_storeattributes |

## View Code

```sql
; CREATE   VIEW azure.storeattributes AS SELECT * FROM LH_Mart.dbo.azure_storeattributes;
```

