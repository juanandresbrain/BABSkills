# azure.productchainonhandcost

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.productchainonhandcost"]
    dbo_azure_productchainonhandcost(["dbo.azure_productchainonhandcost"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_productchainonhandcost |

## View Code

```sql
; CREATE   VIEW azure.productchainonhandcost AS SELECT * FROM LH_Mart.dbo.azure_productchainonhandcost;
```

