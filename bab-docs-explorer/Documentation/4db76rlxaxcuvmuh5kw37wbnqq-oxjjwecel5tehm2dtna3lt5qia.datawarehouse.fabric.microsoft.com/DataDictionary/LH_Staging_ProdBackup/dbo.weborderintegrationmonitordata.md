# dbo.weborderintegrationmonitordata

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ExposedOrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNetTotal | decimal | 9 | 1 |  |  |  |
| OrderImportDate | date | 3 | 1 |  |  |  |
| WebOrderNumber | varchar | 8000 | 1 |  |  |  |
| WebOrderProcessingOrderNumber | varchar | 8000 | 1 |  |  |  |
| CurrentStatus | varchar | 8000 | 1 |  |  |  |
| NewOrderStatusDate | date | 3 | 1 |  |  |  |
| ShippedStatusDate | date | 3 | 1 |  |  |  |
| CurrentStatusDate | date | 3 | 1 |  |  |  |
| DynamicsAPILogDate | date | 3 | 1 |  |  |  |
| DynamicsAPILogWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsAPILogSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsOrderCreationDateTime | date | 3 | 1 |  |  |  |
| DynamicsSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsShippedOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsShippedDate | date | 3 | 1 |  |  |  |
