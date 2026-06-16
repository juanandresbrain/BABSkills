# WMS.SalesOrderStatusUpdateWaved

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WaveId | varchar | 25 | 1 |  |  |  |
| ReleasedDateAndTime | datetime | 8 | 1 |  |  |  |
| Warehouse | varchar | 10 | 1 |  |  |  |
| ShipmentStatus | varchar | 20 | 1 |  |  |  |
| ContainerId | varchar | 20 | 0 | YES |  |  |
| MasterTrackingNumber | varchar | 30 | 1 |  |  |  |
| ItemId | varchar | 20 | 0 | YES |  |  |
| SalesPoolId | varchar | 20 | 1 |  |  |  |
| DeckSalesOrderReferenceNumber | varchar | 10 | 1 |  |  |  |
| OrderNum | varchar | 20 | 0 | YES |  |  |
| WorkId | varchar | 20 | 1 |  |  |  |
| ServiceBusSequence | bigint | 8 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: NOCDev.spGetWaveOrders](../../StoredProcedures/IntegrationStaging/NOCDev.spGetWaveOrders.md)
- [IntegrationStaging: WMS.spRetryReleasedOutOfOrderWaves](../../StoredProcedures/IntegrationStaging/WMS.spRetryReleasedOutOfOrderWaves.md)
- [IntegrationStaging: WMS.spUpdateReleaseDateAndTime](../../StoredProcedures/IntegrationStaging/WMS.spUpdateReleaseDateAndTime.md)

