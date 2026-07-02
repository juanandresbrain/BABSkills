# WM.vwOMSStyleCodeGTINLookup

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwOMSStyleCodeGTINLookup"]
    WEB_ProductCatalogMasterAttributes(["WEB.ProductCatalogMasterAttributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.ProductCatalogMasterAttributes |

## View Code

```sql
CREATE VIEW [WM].[vwOMSStyleCodeGTINLookup]
AS
SELECT        ISNULL(ROW_NUMBER() OVER(ORDER BY Style_Code), -1) AS ID, Style_Code, UPC AS GTIN
FROM            WEB.ProductCatalogMasterAttributes
--WHERE        (OnlineFlag = 1)
```

