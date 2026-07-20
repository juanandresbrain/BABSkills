# dbo.integrationstaging_wms_inboundshipmentload

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShipDate | date | 3 | 1 |  |  |  |
| ExpectedReceiptDate | date | 3 | 1 |  |  |  |
| DeliveryTerms | varchar | 8000 | 1 |  |  |  |
| ItemNumber | varchar | 8000 | 1 |  |  |  |
| TransferQuantity | int | 4 | 1 |  |  |  |
| UOM | varchar | 8000 | 1 |  |  |  |
| BABAptosDistroNumber | varchar | 8000 | 1 |  |  |  |
| InventoryStatus | varchar | 8000 | 1 |  |  |  |
| LicensePlate | varchar | 8000 | 1 |  |  |  |
| ContainerID | varchar | 8000 | 1 |  |  |  |
| 3PLDocumentNumber | varchar | 8000 | 1 |  |  |  |
| OrderCreateSource | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| FromWarehouse | varchar | 8000 | 1 |  |  |  |
| ToWarehouse | varchar | 8000 | 1 |  |  |  |
| AptosShipmentNumber | varchar | 8000 | 1 |  |  |  |
| ModeOfDelivery | varchar | 8000 | 1 |  |  |  |
| OrderId | varchar | 8000 | 1 |  |  |  |
| BABAptosDistroLineNumber | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| SentDate | datetime2 | 8 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| ParentLicensePlate | varchar | 8000 | 1 |  |  |  |
