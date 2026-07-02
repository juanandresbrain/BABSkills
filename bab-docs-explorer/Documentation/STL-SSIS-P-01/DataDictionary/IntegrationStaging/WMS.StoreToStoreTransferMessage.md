# WMS.StoreToStoreTransferMessage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransferOrderNumber | varchar | 20 | 1 |  |  |  |
| Entity | varchar | 10 | 1 |  |  |  |
| FromWarehouse | varchar | 5 | 1 |  |  |  |
| ToWarehouse | varchar | 5 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| WorkLookupComplete | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeStoreToStoreTransferLicensePlate](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreToStoreTransferLicensePlate.md)
- [IntegrationStaging: WMS.spMergeStoreToStoreTransferMessage](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreToStoreTransferMessage.md)

