# dbo.integrationstaging_wms_shipconfirmdbschenker

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | int | 4 | 1 |  |  |  |
| itemId | varchar | 8000 | 1 |  |  |  |
| itemName | varchar | 8000 | 1 |  |  |  |
| countryOfOrigin | varchar | 8000 | 1 |  |  |  |
| harmonizedCode | varchar | 8000 | 1 |  |  |  |
| quantity | decimal | 9 | 1 |  |  |  |
| unitPrice | decimal | 9 | 1 |  |  |  |
| netSalesPrice | decimal | 9 | 1 |  |  |  |
| loadNumber | varchar | 8000 | 1 |  |  |  |
| warehouse | varchar | 8000 | 1 |  |  |  |
| ShipToCountry | varchar | 8000 | 1 |  |  |  |
| _upstream.EnqueuedTimeUTC | varchar | 8000 | 1 |  |  |  |
| _upstream.MessageId | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| SentToHA | datetime2 | 8 | 1 |  |  |  |
