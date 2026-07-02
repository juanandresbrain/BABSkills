# WMS.SalesOrderStatusUpdateWaved_Duplicates

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WaveId | varchar | 25 | 1 |  |  |  |
| ReleasedDateAndTime | datetime | 8 | 1 |  |  |  |
| Warehouse | varchar | 10 | 1 |  |  |  |
| ShipmentStatus | varchar | 20 | 1 |  |  |  |
| ContainerId | varchar | 20 | 0 |  |  |  |
| MasterTrackingNumber | varchar | 30 | 1 |  |  |  |
| ItemId | varchar | 20 | 0 |  |  |  |
| SalesPoolId | varchar | 20 | 1 |  |  |  |
| DeckSalesOrderReferenceNumber | varchar | 10 | 1 |  |  |  |
| OrderNum | varchar | 20 | 0 |  |  |  |
| WorkId | varchar | 20 | 1 |  |  |  |
| ServiceBusSequence | bigint | 8 | 1 |  |  |  |

