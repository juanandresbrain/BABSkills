# dbo.weborderintegrationoutboundtrackingstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ExposedShippedDate | date | 3 | 1 |  |  |  |
| ShippedFromCountry | varchar | 8000 | 1 |  |  |  |
| ExposedShippedOrder | varchar | 8000 | 1 |  |  |  |
| DynamicsShippedInvoiceDate | datetime2 | 8 | 1 |  |  |  |
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
| ESWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| ESinSATransactionDate | datetime2 | 8 | 1 |  |  |  |
| DeckCurrentStatus | varchar | 8000 | 1 |  |  |  |
| DeckCancelDate | date | 3 | 1 |  |  |  |
| SettledOrderNumber | varchar | 8000 | 1 |  |  |  |
| SettlementDate | date | 3 | 1 |  |  |  |
| isSettled | int | 4 | 1 |  |  |  |
