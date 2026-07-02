# WMS.SalesOrderStatusUpdateShipped

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WaveId | varchar | 25 | 1 |  |  |  |
| ModeOfDelivery | varchar | 20 | 1 |  |  |  |
| ShipConfirmDateTime | datetime | 8 | 1 |  |  |  |
| Warehouse | varchar | 10 | 1 |  |  |  |
| ShipmentId | varchar | 20 | 0 | YES |  |  |
| ShipmentStatus | varchar | 20 | 1 |  |  |  |
| ContainerId | varchar | 20 | 0 | YES |  |  |
| MasterTrackingNumber | varchar | 30 | 1 |  |  |  |
| ItemId | varchar | 20 | 0 | YES |  |  |
| SalesPoolId | varchar | 20 | 1 |  |  |  |
| OrderNum | varchar | 20 | 0 | YES |  |  |
| DeckSalesOrderReferenceNumber | varchar | 10 | 1 |  |  |  |
| ShippedQty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spReportBearhouseWebStoreInvoiceUpdate](../../StoredProcedures/IntegrationStaging/WMS.spReportBearhouseWebStoreInvoiceUpdate.md)
- [IntegrationStaging: WMS.spReportWebOrderMakeup](../../StoredProcedures/IntegrationStaging/WMS.spReportWebOrderMakeup.md)

