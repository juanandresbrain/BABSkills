# dbo.onpremview_azure_vwproducts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.onpremview_azure_vwproducts"]
    dbo_onpremview_azure_vwproducts(["dbo.onpremview_azure_vwproducts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.onpremview_azure_vwproducts |

## View Code

```sql
; CREATE   VIEW onpremview_azure_vwproducts AS SELECT * FROM LH_Mart.dbo.onpremview_azure_vwproducts;
```

