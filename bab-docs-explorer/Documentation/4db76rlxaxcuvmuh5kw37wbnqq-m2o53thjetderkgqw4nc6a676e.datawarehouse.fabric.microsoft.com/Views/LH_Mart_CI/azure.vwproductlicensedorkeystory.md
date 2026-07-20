# azure.vwproductlicensedorkeystory

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.vwproductlicensedorkeystory"]
    dbo_azure_vwproductlicensedorkeystory(["dbo.azure_vwproductlicensedorkeystory"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_vwproductlicensedorkeystory |

## View Code

```sql
CREATE     VIEW [azure].[vwproductlicensedorkeystory] AS SELECT product_key, style_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [style_code], product_desc COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [product_desc], Licensed COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [Licensed], KeyStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [KeyStory] FROM LH_Mart.dbo.azure_vwproductlicensedorkeystory
```

