# dbo.weborderintegrationoutboundtracking

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TrackingIdentifier | int | 4 | 1 |  |  |  |
| ExposedShippedDate | date | 3 | 1 |  |  |  |
| ShippedFromCountry | varchar | 8000 | 1 |  |  |  |
| ExposedShippedOrder | varchar | 8000 | 1 |  |  |  |
| DynamicsShippedInvoiceDate | date | 3 | 1 |  |  |  |
| DynamicsShippedSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsShippedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| IntegrationShippedDate | date | 3 | 1 |  |  |  |
| IntegrationSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| IntegrationWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKShippedDate | date | 3 | 1 |  |  |  |
| UKShippedOrder | varchar | 8000 | 1 |  |  |  |
| WebOrderProcessingShippedStatusDate | date | 3 | 1 |  |  |  |
| WebOrderProcessingShippedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| DeckShipDate | date | 3 | 1 |  |  |  |
| DeckWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| SalesAuditWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| SalesAuditTransactionDate | date | 3 | 1 |  |  |  |
| DeckCurrentStatus | varchar | 8000 | 1 |  |  |  |
| DeckCancelDate | date | 3 | 1 |  |  |  |
| SettledOrderNumber | varchar | 8000 | 1 |  |  |  |
| SettlementDate | date | 3 | 1 |  |  |  |
| isSettled | int | 4 | 1 |  |  |  |
