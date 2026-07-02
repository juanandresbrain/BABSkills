# WM.vwGiftCardInfo

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwGiftCardInfo"]
    WM_ProductCatalogMasterAttributes_Mirror(["WM.ProductCatalogMasterAttributes_Mirror"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ProductCatalogMasterAttributes_Mirror |

## View Code

```sql
CREATE VIEW [WM].[vwGiftCardInfo]
AS
SELECT        Style_Code, giftCardType
FROM            WM.ProductCatalogMasterAttributes_Mirror AS ProductCatalogMasterAttributes_1
WHERE        (giftCardType IS NOT NULL)
```

