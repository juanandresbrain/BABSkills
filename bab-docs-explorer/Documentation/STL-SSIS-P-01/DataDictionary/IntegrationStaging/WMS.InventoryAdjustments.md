# WMS.InventoryAdjustments

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| itemNumber | nvarchar | 200 | 1 |  |  |  |
| warehouse | nvarchar | 200 | 1 |  |  |  |
| adjustedQuantity | int | 4 | 1 |  |  |  |
| reasonCode | nvarchar | 200 | 1 |  |  |  |
| journalType | nvarchar | 200 | 1 |  |  |  |
| EnqueuedTimeUTC | nvarchar | 8000 | 1 |  |  |  |
| MessageId | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| TransmittedToAptos | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeInventoryAdjustments](../../StoredProcedures/IntegrationStaging/WMS.spMergeInventoryAdjustments.md)
- [IntegrationStaging: WMS.spPrintInventoryAdjustments](../../StoredProcedures/IntegrationStaging/WMS.spPrintInventoryAdjustments.md)
- [IntegrationStaging: WMS.spSelectInventoryAdjustments](../../StoredProcedures/IntegrationStaging/WMS.spSelectInventoryAdjustments.md)

