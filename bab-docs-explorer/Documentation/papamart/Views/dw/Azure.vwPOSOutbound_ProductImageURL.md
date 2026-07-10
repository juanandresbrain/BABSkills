# Azure.vwPOSOutbound_ProductImageURL

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_ProductImageURL"]
    POS_vwPOSProductImageURL(["POS.vwPOSProductImageURL"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| POS.vwPOSProductImageURL |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_ProductImageURL] AS


 -- select * FROM [stl-ssis-p-01].[IntegrationStaging].[POS].[ProductImageURL]
  
  select * FROM [stl-ssis-p-01].[IntegrationStaging].[POS].vwPOSProductImageURL
```

