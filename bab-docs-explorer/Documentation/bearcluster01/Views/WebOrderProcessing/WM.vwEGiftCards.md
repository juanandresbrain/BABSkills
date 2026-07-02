# WM.vwEGiftCards

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwEGiftCards"]
    WM_ProductCatalogMasterAttributes_Mirror(["WM.ProductCatalogMasterAttributes_Mirror"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ProductCatalogMasterAttributes_Mirror |

## View Code

```sql
CREATE view [WM].[vwEGiftCards] 
as 

select
	ROW_NUMBER() over (order by BABWProductID) as ID,
	BABWProductID
	
from WM.ProductCatalogMasterAttributes_Mirror  
where giftCardType = 'EGC'
```

