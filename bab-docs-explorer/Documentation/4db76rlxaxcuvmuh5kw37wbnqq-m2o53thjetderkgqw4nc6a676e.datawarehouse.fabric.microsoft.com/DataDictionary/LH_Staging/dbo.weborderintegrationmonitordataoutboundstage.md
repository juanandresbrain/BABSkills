# dbo.weborderintegrationmonitordataoutboundstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InvoiceDate | date | 3 | 1 |  |  |  |
| SalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| IntegrationShippedDate | date | 3 | 1 |  |  |  |
| WebOrderProcessingShippedStatusDate | date | 3 | 1 |  |  |  |
| WebOrderNumber | varchar | 8000 | 1 |  |  |  |
| WebOrderProcessingShippedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| WebOrderProcessingShippedSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| DeckAPILogWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| DeckAPILogDate | date | 3 | 1 |  |  |  |
| DeckAPILogShippedSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| SalesAuditWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| SalesAuditTransactionDate | date | 3 | 1 |  |  |  |
| SalesAuditSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| IntegrationSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| IntegrationWebOrderNumber | varchar | 8000 | 1 |  |  |  |
