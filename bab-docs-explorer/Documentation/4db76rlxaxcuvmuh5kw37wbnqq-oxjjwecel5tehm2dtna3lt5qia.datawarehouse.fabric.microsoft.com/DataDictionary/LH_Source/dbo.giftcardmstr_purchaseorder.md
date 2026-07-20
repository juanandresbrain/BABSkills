# dbo.giftcardmstr_purchaseorder

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderID | int | 4 | 1 |  |  |  |
| PurchaseOrderNumber | varchar | 8000 | 1 |  |  |  |
| PurchaseOrderDateTime | datetime2 | 8 | 1 |  |  |  |
| BillingLocationID | int | 4 | 1 |  |  |  |
| DeliveryLocationID | int | 4 | 1 |  |  |  |
| RequestedDeliveryDate | date | 3 | 1 |  |  |  |
| ShipDateTime | datetime2 | 8 | 1 |  |  |  |
| ShipperTrackingNumber | varchar | 8000 | 1 |  |  |  |
| InvoiceNumber | varchar | 8000 | 1 |  |  |  |
| Comments | varchar | 8000 | 1 |  |  |  |
| CurrentStatusID | int | 4 | 1 |  |  |  |
| CRTED_BY | varchar | 8000 | 1 |  |  |  |
| CRTED_DT | datetime2 | 8 | 1 |  |  |  |
| UPDTD_BY | varchar | 8000 | 1 |  |  |  |
| UPDTD_DT | datetime2 | 8 | 1 |  |  |  |
