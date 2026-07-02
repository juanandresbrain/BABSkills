# dbo.StoreInventoryStageForOMS

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 1 |  |  |  |
| GTIN | varchar | 20 | 1 |  |  |  |
| StyleCode | varchar | 6 | 1 |  |  |  |
| SKUDescription | varchar | 120 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |
| SellingGeography | varchar | 2 | 1 |  |  |  |
| BufferedQty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spSelectStoreInventoryPrepData](../../StoredProcedures/me_01/dbo.spSelectStoreInventoryPrepData.md)

