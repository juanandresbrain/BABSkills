# Azure.vwWebProductStorefrontCategoryMap

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWebProductStorefrontCategoryMap"]
    Azure_WebProductStorefrontCategoryMap(["Azure.WebProductStorefrontCategoryMap"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.WebProductStorefrontCategoryMap |

## View Code

```sql
create view Azure.vwWebProductStorefrontCategoryMap
as

select *
from Azure.WebProductStorefrontCategoryMap
```

