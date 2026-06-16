# WMS.InventorySyncStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| warehouse | nvarchar | 200 | 1 |  |  |  |
| itemNumber | nvarchar | 200 | 1 |  |  |  |
| inventoryStatus | nvarchar | 200 | 1 |  |  |  |
| physicalInventory | int | 4 | 1 |  |  |  |
| physicalReserved | int | 4 | 1 |  |  |  |
| availablePhysical | int | 4 | 1 |  |  |  |
| availPhysExactDimensions | int | 4 | 1 |  |  |  |
| orderedInTotal | int | 4 | 1 |  |  |  |
| onOrder | int | 4 | 1 |  |  |  |
| orderedReserved | int | 4 | 1 |  |  |  |
| availableReservation | int | 4 | 1 |  |  |  |
| totalAvailable | int | 4 | 1 |  |  |  |
| MessageDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeInventorySync](../../StoredProcedures/IntegrationStaging/WMS.spMergeInventorySync.md)

