# dbo.azure_po_on_order

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 8000 | 1 |  |  |  |
| po_description | varchar | 8000 | 1 |  |  |  |
| CreateDate | date | 3 | 1 |  |  |  |
| FreightOnBoard | varchar | 8000 | 1 |  |  |  |
| PoAttributeCode | varchar | 8000 | 1 |  |  |  |
| PoAttributeLabel | varchar | 8000 | 1 |  |  |  |
| TotalFirstCost | decimal | 17 | 1 |  |  |  |
| VendorCode | varchar | 8000 | 1 |  |  |  |
| VendorName | varchar | 8000 | 1 |  |  |  |
| LocationCode | varchar | 8000 | 1 |  |  |  |
| style | varchar | 8000 | 1 |  |  |  |
| Cost | decimal | 17 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| SalesValue | decimal | 17 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| Currency_Code | varchar | 8000 | 1 |  |  |  |
| CHinese_total_First_Cost | decimal | 13 | 1 |  |  |  |
| ExpectedReceiptDate | date | 3 | 1 |  |  |  |
| SartShipDate | date | 3 | 1 |  |  |  |
| CancelShipDate | date | 3 | 1 |  |  |  |
| ChineseFirstCost | decimal | 17 | 1 |  |  |  |
