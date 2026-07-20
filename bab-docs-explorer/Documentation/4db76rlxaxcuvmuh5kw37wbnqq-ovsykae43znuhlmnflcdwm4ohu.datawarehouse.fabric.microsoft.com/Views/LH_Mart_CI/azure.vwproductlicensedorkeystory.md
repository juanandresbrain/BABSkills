# azure.vwproductlicensedorkeystory

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
CREATE   VIEW azure.vwproductlicensedorkeystory AS SELECT * FROM LH_Mart.dbo.azure_vwproductlicensedorkeystory;
```

