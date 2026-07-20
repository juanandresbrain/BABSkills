# azure.prodfactory

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.prodfactory"]
    dbo_azure_prodfactory(["dbo.azure_prodfactory"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_prodfactory |

## View Code

```sql
; CREATE   VIEW azure.prodfactory AS SELECT * FROM LH_Mart.dbo.azure_prodfactory;
```

