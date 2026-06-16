# WMS.tmpInboundShipmentLoad3PL_Error

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InboundShipmentCreate | varchar | -1 | 1 |  |  |  |
| AptosShipmentNumber | varchar | 50 | 1 |  |  |  |
| BatchID | nvarchar | 76 | 1 |  |  |  |
| Company | varchar | 4 | 1 |  |  |  |
| TransferOrderNumber | varchar | 20 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| ErrorMessage | nvarchar | 4096 | 1 |  |  |  |
| HttpStatusCode | smallint | 2 | 1 |  |  |  |
| HttpStatusCodeName | nvarchar | 510 | 1 |  |  |  |
| ResponseBodyError | nvarchar | -1 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |

