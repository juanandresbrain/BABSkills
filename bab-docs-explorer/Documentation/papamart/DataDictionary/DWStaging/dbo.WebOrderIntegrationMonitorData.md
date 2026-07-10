# dbo.WebOrderIntegrationMonitorData

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ExposedOrderNumber | varchar | 10 | 1 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNetTotal | numeric | 9 | 1 |  |  |  |
| OrderImportDate | date | 3 | 1 |  |  |  |
| WebOrderNumber | varchar | 10 | 1 |  |  |  |
| WebOrderProcessingOrderNumber | varchar | 10 | 1 |  |  |  |
| CurrentStatus | varchar | 20 | 1 |  |  |  |
| NewOrderStatusDate | date | 3 | 1 |  |  |  |
| ShippedStatusDate | date | 3 | 1 |  |  |  |
| CurrentStatusDate | date | 3 | 1 |  |  |  |
| DynamicsAPILogDate | date | 3 | 1 |  |  |  |
| DynamicsAPILogWebOrderNumber | varchar | 30 | 1 |  |  |  |
| DynamicsAPILogSalesOrderNumber | varchar | 20 | 1 |  |  |  |
| DynamicsOrderCreationDateTime | date | 3 | 1 |  |  |  |
| DynamicsSalesOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| DynamicsShippedOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| DynamicsShippedDate | date | 3 | 1 |  |  |  |
