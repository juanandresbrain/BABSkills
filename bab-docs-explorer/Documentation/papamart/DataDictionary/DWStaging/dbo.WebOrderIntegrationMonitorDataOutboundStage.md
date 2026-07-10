# dbo.WebOrderIntegrationMonitorDataOutboundStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InvoiceDate | date | 3 | 1 |  |  |  |
| SalesOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| IntegrationShippedDate | date | 3 | 1 |  |  |  |
| WebOrderProcessingShippedStatusDate | date | 3 | 1 |  |  |  |
| WebOrderNumber | varchar | 30 | 1 |  |  |  |
| WebOrderProcessingShippedWebOrderNumber | varchar | 10 | 1 |  |  |  |
| WebOrderProcessingShippedSalesOrderNumber | nvarchar | 40 | 1 |  |  |  |
| DeckAPILogWebOrderNumber | varchar | 10 | 1 |  |  |  |
| DeckAPILogDate | date | 3 | 1 |  |  |  |
| DeckAPILogShippedSalesOrderNumber | nvarchar | 40 | 1 |  |  |  |
| SalesAuditWebOrderNumber | varchar | 10 | 1 |  |  |  |
| SalesAuditTransactionDate | date | 3 | 1 |  |  |  |
| SalesAuditSalesOrderNumber | nvarchar | 40 | 1 |  |  |  |
| IntegrationSalesOrderNumber | varchar | 20 | 1 |  |  |  |
| IntegrationWebOrderNumber | varchar | 10 | 1 |  |  |  |
