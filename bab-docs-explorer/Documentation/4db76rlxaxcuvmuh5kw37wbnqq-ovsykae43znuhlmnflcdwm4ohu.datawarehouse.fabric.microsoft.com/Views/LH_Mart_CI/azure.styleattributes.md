# azure.styleattributes

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.styleattributes"]
    dbo_azure_styleattributes(["dbo.azure_styleattributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_styleattributes |

## View Code

```sql
; CREATE   VIEW azure.styleattributes AS SELECT * FROM LH_Mart.dbo.azure_styleattributes;
```

