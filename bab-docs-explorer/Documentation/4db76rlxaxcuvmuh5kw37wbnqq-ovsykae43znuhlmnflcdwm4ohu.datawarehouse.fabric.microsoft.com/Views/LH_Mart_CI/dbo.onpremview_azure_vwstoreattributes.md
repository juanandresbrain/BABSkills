# dbo.onpremview_azure_vwstoreattributes

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.onpremview_azure_vwstoreattributes"]
    dbo_onpremview_azure_vwstoreattributes(["dbo.onpremview_azure_vwstoreattributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.onpremview_azure_vwstoreattributes |

## View Code

```sql
; CREATE   VIEW onpremview_azure_vwstoreattributes AS SELECT * FROM LH_Mart.dbo.onpremview_azure_vwstoreattributes;
```

