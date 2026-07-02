# WMS.ShipmentConfirmAptosHeaderStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _JSON | nvarchar | -1 | 1 |  |  |  |
| _RowIndex | int | 4 | 1 |  |  |  |
| aptosShipmentId | nvarchar | 200 | 1 |  |  |  |
| modeOfDelivery | nvarchar | 200 | 1 |  |  |  |
| shipConfirmDateTime | nvarchar | 200 | 1 |  |  |  |
| warehouse | nvarchar | 200 | 1 |  |  |  |
| _upstream.EnqueuedTimeUTC | nvarchar | 8000 | 1 |  |  |  |
| _upstream.ExpiresAtUTC | nvarchar | 8000 | 1 |  |  |  |
| _upstream.Label | nvarchar | 8000 | 1 |  |  |  |
| _upstream.Message | nvarchar | 8000 | 1 |  |  |  |
| _upstream.MessageId | nvarchar | 8000 | 1 |  |  |  |
| _upstream.Sequence | bigint | 8 | 1 |  |  |  |
| _upstream.Size | bigint | 8 | 1 |  |  |  |

