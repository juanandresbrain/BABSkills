# POS.StoreInventoryForEnterpriseInventoryStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 1 |  |  |  |
| StoreNumber | varchar | 4 | 1 |  |  |  |
| StyleCode | varchar | 6 | 1 |  |  |  |
| StoreInventory | int | 4 | 1 |  |  |  |
| Country | varchar | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: POS.spMergeStoreInventoryForEnterpriseInventory](../../StoredProcedures/IntegrationStaging/POS.spMergeStoreInventoryForEnterpriseInventory.md)

