# dbo.azure_gift_card_manager_gift_card_fact

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| GiftCardID | int | 4 | 1 |  |  |  |
| GiftCardNumber | varchar | 8000 | 1 |  |  |  |
| PurchaseOrderNumber | varchar | 8000 | 1 |  |  |  |
| PurchaseOrderDateTime | date | 3 | 1 |  |  |  |
| LocationID | int | 4 | 1 |  |  |  |
| RequestedDeliveryDate | date | 3 | 1 |  |  |  |
| ShipDateTime | date | 3 | 1 |  |  |  |
| ShipperTrackingNumber | varchar | 8000 | 1 |  |  |  |
| InvoiceNumber | varchar | 8000 | 1 |  |  |  |
| ActivationDate | date | 3 | 1 |  |  |  |
| DeactivationDate | date | 3 | 1 |  |  |  |
