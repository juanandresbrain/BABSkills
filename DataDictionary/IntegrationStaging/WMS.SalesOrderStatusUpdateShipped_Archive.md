# WMS.SalesOrderStatusUpdateShipped_Archive

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WaveId | varchar | 25 | 1 |  |  |  |
| ModeOfDelivery | varchar | 20 | 1 |  |  |  |
| ShipConfirmDateTime | datetime | 8 | 1 |  |  |  |
| Warehouse | varchar | 10 | 1 |  |  |  |
| ShipmentId | varchar | 20 | 0 |  |  |  |
| ShipmentStatus | varchar | 20 | 1 |  |  |  |
| ContainerId | varchar | 20 | 0 |  |  |  |
| MasterTrackingNumber | varchar | 30 | 1 |  |  |  |
| ItemId | varchar | 20 | 0 |  |  |  |
| SalesPoolId | varchar | 20 | 1 |  |  |  |
| OrderNum | varchar | 20 | 0 |  |  |  |
| DeckSalesOrderReferenceNumber | varchar | 10 | 1 |  |  |  |
| ShippedQty | int | 4 | 1 |  |  |  |

