# azure.prodmstat

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.prodmstat"]
    dbo_azure_prodmstat(["dbo.azure_prodmstat"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_prodmstat |

## View Code

```sql
; CREATE   VIEW azure.prodmstat AS SELECT * FROM LH_Mart.dbo.azure_prodmstat;
```

