# dbo.tmpwebvssalesaudit

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SalesAuditWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| SalesAuditTransactionDate | date | 3 | 1 |  |  |  |
| DynamicsShippedInvoiceDate | datetime2 | 8 | 1 |  |  |  |
| DynamicsShippedSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| IntegrationShippedDate | date | 3 | 1 |  |  |  |
| DynamicsShippedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| IntegrationSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| IntegrationWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKShippedOrder | varchar | 8000 | 1 |  |  |  |
| UKShippedDate | date | 3 | 1 |  |  |  |
| ExposedShippedOrder | varchar | 8000 | 1 |  |  |  |
| ExposedShippedDate | datetime2 | 8 | 1 |  |  |  |
| SalesAuditOrderNumber | varchar | 8000 | 1 |  |  |  |
