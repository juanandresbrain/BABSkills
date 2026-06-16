# WMS.InventorySync3PLArchiveStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 8 | 1 |  |  |  |
| DynWhseID | nvarchar | 8 | 1 |  |  |  |
| LocationCode | varchar | 4 | 1 |  |  |  |
| ItemNumber | varchar | 6 | 1 |  |  |  |
| InventoryMultiple | int | 4 | 1 |  |  |  |
| DynQty | int | 4 | 1 |  |  |  |
| WhseQty | int | 4 | 1 |  |  |  |
| InventoryDate | date | 3 | 1 |  |  |  |
| VarianceQty | bigint | 8 | 1 |  |  |  |

