# WMS.StoreShipmentExportException

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JSON_F52E2B61-18A1-11d1-B105-00805F49916B | nvarchar | -1 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| ErrorMessage | nvarchar | 4096 | 1 |  |  |  |
| HttpStatusCode | smallint | 2 | 1 |  |  |  |
| HttpStatusCodeName | nvarchar | 510 | 1 |  |  |  |
| ResponseBodyError | nvarchar | -1 | 1 |  |  |  |

