# azure.pchealthchecks

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.pchealthchecks"]
    dbo_azure_pchealthchecks(["dbo.azure_pchealthchecks"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_pchealthchecks |

## View Code

```sql
;
CREATE   VIEW azure.pchealthchecks AS SELECT * FROM LH_Mart.dbo.azure_pchealthchecks;
```

