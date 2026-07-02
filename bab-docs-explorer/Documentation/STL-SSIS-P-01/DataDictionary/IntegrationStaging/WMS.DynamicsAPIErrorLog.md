# WMS.DynamicsAPIErrorLog

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IntegrationName | nvarchar | 200 | 1 |  |  |  |
| MergedJson | nvarchar | -1 | 1 |  |  |  |
| ContentType | nvarchar | 510 | 1 |  |  |  |
| ContentLength | numeric | 13 | 1 |  |  |  |
| HttpStatusCode | smallint | 2 | 1 |  |  |  |
| HttpResponseUrl | nvarchar | 4168 | 1 |  |  |  |
| HttpStatusCodeName | nvarchar | 510 | 1 |  |  |  |
| ResponseBody | nvarchar | -1 | 1 |  |  |  |
| ExceptionError | nvarchar | -1 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| AptosDocumentNumber | varchar | 20 | 1 |  |  |  |
| TPMShipmentNumber | nvarchar | 40 | 1 |  |  |  |
| StoreShipmentNumber | varchar | 20 | 1 |  |  |  |
| WebOrderNumber | nvarchar | 20 | 1 |  |  |  |
| PO_OrderAccountNumber | nvarchar | 20 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |

