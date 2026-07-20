# dbo.integrationstaging_wms_shipconfirmdbschenkerstage

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| countryCode | varchar | 8000 | 1 |  |  |  |
| countryOfOrigin | varchar | 8000 | 1 |  |  |  |
| harmonizedCode | varchar | 8000 | 1 |  |  |  |
| itemId | varchar | 8000 | 1 |  |  |  |
| itemName | varchar | 8000 | 1 |  |  |  |
| netSalesPrice | decimal | 9 | 1 |  |  |  |
| quantity | float | 8 | 1 |  |  |  |
| shipmentId | varchar | 8000 | 1 |  |  |  |
| unitPrice | decimal | 9 | 1 |  |  |  |
| warehouse | varchar | 8000 | 1 |  |  |  |
| _upstream.MessageId | varchar | 8000 | 1 |  |  |  |
| Sequence | bigint | 8 | 1 |  |  |  |
| _upstream.EnqueuedTimeUTC | datetime2 | 8 | 1 |  |  |  |
| Size | int | 4 | 1 |  |  |  |
| Subject | varchar | 8000 | 1 |  |  |  |
| ExpireAtUTC | datetime2 | 8 | 1 |  |  |  |
| unitPriceOriginal | decimal | 9 | 1 |  |  |  |
| netSalesPriceOriginal | decimal | 9 | 1 |  |  |  |
| _RowIndex | int | 4 | 1 |  |  |  |
