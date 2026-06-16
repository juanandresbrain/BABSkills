# WMS.StoreToStoreTransferMessageStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransferOrderNumber | varchar | 20 | 1 |  |  |  |
| Entity | varchar | 10 | 1 |  |  |  |
| FromWarehouse | varchar | 5 | 1 |  |  |  |
| ToWarehouse | varchar | 5 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeStoreToStoreTransferMessage](../../StoredProcedures/IntegrationStaging/WMS.spMergeStoreToStoreTransferMessage.md)

