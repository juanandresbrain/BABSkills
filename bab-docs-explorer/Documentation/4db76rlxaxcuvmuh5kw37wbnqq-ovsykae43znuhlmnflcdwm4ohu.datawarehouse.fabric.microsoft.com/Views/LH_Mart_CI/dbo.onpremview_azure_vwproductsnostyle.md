# dbo.onpremview_azure_vwproductsnostyle

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.onpremview_azure_vwproductsnostyle"]
    dbo_onpremview_azure_vwproductsnostyle(["dbo.onpremview_azure_vwproductsnostyle"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.onpremview_azure_vwproductsnostyle |

## View Code

```sql
; CREATE   VIEW onpremview_azure_vwproductsnostyle AS SELECT * FROM LH_Mart.dbo.onpremview_azure_vwproductsnostyle;
```

