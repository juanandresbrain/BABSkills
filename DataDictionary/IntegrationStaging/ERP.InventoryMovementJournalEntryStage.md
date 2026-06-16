# ERP.InventoryMovementJournalEntryStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| productConfigurationId | varchar | 50 | 1 |  |  |  |
| inventoryStatusId | varchar | 50 | 1 |  |  |  |
| lineNumber | decimal | 9 | 1 |  |  |  |
| inventorySiteId | varchar | 50 | 1 |  |  |  |
| productSizeId | varchar | 50 | 1 |  |  |  |
| itemNumber | varchar | 50 | 1 |  |  |  |
| inventoryWarehouseId | varchar | 50 | 1 |  |  |  |
| itemSerialNumber | varchar | 50 | 1 |  |  |  |
| fixedCostCharges | decimal | 9 | 1 |  |  |  |
| inventoryQuantity | decimal | 9 | 1 |  |  |  |
| warehouseLocationId | varchar | 50 | 1 |  |  |  |
| unitCostQuantity | decimal | 9 | 1 |  |  |  |
| costAmount | decimal | 9 | 1 |  |  |  |
| transactionDate | datetimeoffset | 10 | 1 |  |  |  |
| itemBatchNumber | varchar | 50 | 1 |  |  |  |
| dataAreaId | varchar | 50 | 1 |  |  |  |
| unitCost | decimal | 9 | 1 |  |  |  |
| productColorId | varchar | 50 | 1 |  |  |  |
| catchWeightQuantity | decimal | 9 | 1 |  |  |  |
| journalNumber | varchar | 50 | 1 |  |  |  |
| licensePlateNumber | varchar | 50 | 1 |  |  |  |
| productStyleId | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spPFTGetOpenToByRollingCountsAndAttributes_ERP](../../StoredProcedures/IntegrationStaging/ERP.spPFTGetOpenToByRollingCountsAndAttributes_ERP.md)

