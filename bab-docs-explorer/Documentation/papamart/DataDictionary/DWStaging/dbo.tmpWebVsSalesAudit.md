# dbo.tmpWebVsSalesAudit

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SalesAuditWebOrderNumber | varchar | 10 | 1 |  |  |  |
| SalesAuditTransactionDate | date | 3 | 1 |  |  |  |
| DynamicsShippedInvoiceDate | datetime | 8 | 1 |  |  |  |
| DynamicsShippedSalesOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| IntegrationShippedDate | date | 3 | 1 |  |  |  |
| DynamicsShippedWebOrderNumber | varchar | 30 | 1 |  |  |  |
| IntegrationSalesOrderNumber | varchar | 20 | 1 |  |  |  |
| IntegrationWebOrderNumber | varchar | 10 | 1 |  |  |  |
| UKShippedOrder | varchar | 10 | 1 |  |  |  |
| UKShippedDate | date | 3 | 1 |  |  |  |
| ExposedShippedOrder | varchar | 10 | 1 |  |  |  |
| ExposedShippedDate | datetime | 8 | 1 |  |  |  |
| SalesAuditOrderNumber | varchar | 8 | 1 |  |  |  |
