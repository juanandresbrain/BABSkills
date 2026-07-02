# ComHub.StyleCodeCatalogNumber

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VendorCatalogNumberID | int | 4 | 0 | YES |  |  |
| MerchantSKU | varchar | 10 | 0 |  |  |  |
| VendorSKU | varchar | 10 | 0 |  |  |  |
| StyleCode | varchar | 10 | 1 |  |  |  |
| DefaultValue | numeric | 5 | 1 |  |  |  |
| StyleQtyPerVendorQty | int | 4 | 1 |  |  |  |
| isGiftCard | bit | 1 | 1 |  |  |  |
| CreatedBy | varchar | 255 | 0 |  |  |  |
| CreatedOn | datetime | 8 | 0 |  |  |  |
| UpdatedBy | varchar | 255 | 1 |  |  |  |
| UpdatedOn | datetime | 8 | 1 |  |  |  |

