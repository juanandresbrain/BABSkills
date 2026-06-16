# WMS.StoreToStoreTransferLicensePlate

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | varchar | 10 | 1 |  |  |  |
| TransferOrderNumber | varchar | 20 | 1 |  |  |  |
| FromWarehouse | varchar | 10 | 1 |  |  |  |
| ToWarehouse | varchar | 10 | 1 |  |  |  |
| LicensePlateNumber | nvarchar | 8000 | 1 |  |  |  |
| EmailAddress | varchar | 30 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| EmailedDate | datetime | 8 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeStoreToStoreTransferLicensePlate](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreToStoreTransferLicensePlate.md)

