# dbo.wms_dynamicsapilog__sqlsynccopy

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IntegrationName | varchar | 8000 | 1 |  |  |  |
| MergedJson | varchar | 8000 | 1 |  |  |  |
| ContentType | varchar | 8000 | 1 |  |  |  |
| ContentLength | decimal | 13 | 1 |  |  |  |
| HttpStatusCode | int | 4 | 1 |  |  |  |
| HttpResponseUrl | varchar | 8000 | 1 |  |  |  |
| HttpStatusCodeName | varchar | 8000 | 1 |  |  |  |
| ResponseBody | varchar | 8000 | 1 |  |  |  |
| ExceptionError | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| AptosDocumentNumber | varchar | 8000 | 1 |  |  |  |
| TPMShipmentNumber | varchar | 8000 | 1 |  |  |  |
| StoreShipmentNumber | varchar | 8000 | 1 |  |  |  |
| WebOrderNumber | varchar | 8000 | 1 |  |  |  |
| PO_OrderAccountNumber | varchar | 8000 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| MessageID | varchar | 8000 | 1 |  |  |  |
| CostcoOrderNumber | varchar | 8000 | 1 |  |  |  |
| TransferOrderNumber | varchar | 8000 | 1 |  |  |  |
