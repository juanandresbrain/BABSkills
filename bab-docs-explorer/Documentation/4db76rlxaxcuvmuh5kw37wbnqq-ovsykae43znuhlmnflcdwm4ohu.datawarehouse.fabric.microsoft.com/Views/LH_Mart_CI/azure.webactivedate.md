# azure.webactivedate

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.webactivedate"]
    dbo_azure_webactivedate(["dbo.azure_webactivedate"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_webactivedate |

## View Code

```sql
; CREATE   VIEW azure.webactivedate AS SELECT * FROM LH_Mart.dbo.azure_webactivedate;
```

