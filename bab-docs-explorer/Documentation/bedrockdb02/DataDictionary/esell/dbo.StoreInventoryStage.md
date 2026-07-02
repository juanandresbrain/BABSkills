# dbo.StoreInventoryStage

**Database:** esell  
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

- [esell: dbo.spSelectEnterpriseSellingStoreInventory](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventory.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711.md)

