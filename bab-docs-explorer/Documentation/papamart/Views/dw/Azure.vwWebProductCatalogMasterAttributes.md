# Azure.vwWebProductCatalogMasterAttributes

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWebProductCatalogMasterAttributes"]
    Azure_WebProductCatalogMasterAttributes(["Azure.WebProductCatalogMasterAttributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.WebProductCatalogMasterAttributes |

## View Code

```sql
CREATE view [Azure].[vwWebProductCatalogMasterAttributes]

as

select *
from Azure.WebProductCatalogMasterAttributes
where product_key is not null
```

