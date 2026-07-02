# WM.vwDonationInfo

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwDonationInfo"]
    WM_ProductCatalogMasterAttributes_Mirror(["WM.ProductCatalogMasterAttributes_Mirror"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ProductCatalogMasterAttributes_Mirror |

## View Code

```sql
CREATE VIEW [WM].[vwDonationInfo]
AS
SELECT        Style_Code, ClassName
FROM            WM.ProductCatalogMasterAttributes_Mirror AS ProductCatalogMasterAttributes_1
WHERE        (ClassName IN ('Donations', 'UK-Donations')) AND (Style_Code NOT IN ('057700'))
```

