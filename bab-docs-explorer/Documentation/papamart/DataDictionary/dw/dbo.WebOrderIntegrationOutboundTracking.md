# dbo.WebOrderIntegrationOutboundTracking

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TrackingIdentifier | int | 4 | 0 | YES |  |  |
| ExposedShippedDate | date | 3 | 1 |  |  |  |
| ShippedFromCountry | varchar | 2 | 1 |  |  |  |
| ExposedShippedOrder | varchar | 10 | 1 |  |  |  |
| DynamicsShippedInvoiceDate | date | 3 | 1 |  |  |  |
| DynamicsShippedSalesOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| DynamicsShippedWebOrderNumber | varchar | 30 | 1 |  |  |  |
| IntegrationShippedDate | date | 3 | 1 |  |  |  |
| IntegrationSalesOrderNumber | varchar | 20 | 1 |  |  |  |
| IntegrationWebOrderNumber | varchar | 10 | 1 |  |  |  |
| UKShippedDate | date | 3 | 1 |  |  |  |
| UKShippedOrder | varchar | 10 | 1 |  |  |  |
| WebOrderProcessingShippedStatusDate | date | 3 | 1 |  |  |  |
| WebOrderProcessingShippedWebOrderNumber | varchar | 10 | 1 |  |  |  |
| DeckShipDate | date | 3 | 1 |  |  |  |
| DeckWebOrderNumber | varchar | 10 | 1 |  |  |  |
| SalesAuditWebOrderNumber | varchar | 10 | 1 |  |  |  |
| SalesAuditTransactionDate | date | 3 | 1 |  |  |  |
| DeckCurrentStatus | varchar | 50 | 1 |  |  |  |
| DeckCancelDate | date | 3 | 1 |  |  |  |
| SettledOrderNumber | varchar | 10 | 1 |  |  |  |
| SettlementDate | date | 3 | 1 |  |  |  |
| isSettled | int | 4 | 1 |  |  |  |
