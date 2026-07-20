# azure.franchiseetspa

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.franchiseetspa"]
    dbo_azure_franchiseetspa(["dbo.azure_franchiseetspa"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_franchiseetspa |

## View Code

```sql
CREATE   VIEW azure.franchiseetspa AS SELECT * FROM LH_Mart.dbo.azure_franchiseetspa;
```

