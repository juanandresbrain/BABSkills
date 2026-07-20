# dbo.giftcardmstr_purchaseordersline

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderLineID | int | 4 | 1 |  |  |  |
| PurchaseOrderID | int | 4 | 1 |  |  |  |
| POLineNumber | int | 4 | 1 |  |  |  |
| VendorPOQuantityOrdered | decimal | 5 | 1 |  |  |  |
| QuantityOrdered | decimal | 5 | 1 |  |  |  |
| UnitOfMeasureID | int | 4 | 1 |  |  |  |
| UnitPrice | decimal | 5 | 1 |  |  |  |
| VendorCatalogNumberID | bigint | 8 | 1 |  |  |  |
| VendorPartNumber | varchar | 8000 | 1 |  |  |  |
| CRTED_BY | varchar | 8000 | 1 |  |  |  |
| CRTED_DT | datetime2 | 8 | 1 |  |  |  |
| UPDTD_BY | varchar | 8000 | 1 |  |  |  |
| UPDTD_DT | datetime2 | 8 | 1 |  |  |  |
