# WEB.vwPOSpricebook

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwPOSpricebook"]
    web_PricebookFact(["web.PricebookFact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| web.PricebookFact |

## View Code

```sql
create view [WEB].[vwPOSpricebook]

as

select Catalog, Style_code, CurrentPrice, SalePrice
from web.PricebookFact
--order by Catalog desc, style_code
```

