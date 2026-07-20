# dbo.wm_vwdeckorderitemstatuspivot

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SiteCode | varchar | 8000 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderDate | date | 3 | 1 |  |  |  |
| New | varchar | 8000 | 1 |  |  |  |
| Cancelled | varchar | 8000 | 1 |  |  |  |
| GiftCardProcessed | varchar | 8000 | 1 |  |  |  |
| DonationProcessed | varchar | 8000 | 1 |  |  |  |
| GiftCardDevalued | varchar | 8000 | 1 |  |  |  |
| NeedWarehouse | varchar | 8000 | 1 |  |  |  |
| NotAvailable | varchar | 8000 | 1 |  |  |  |
| PendingSound | varchar | 8000 | 1 |  |  |  |
| SoundRecorded | varchar | 8000 | 1 |  |  |  |
| PendingWave | varchar | 8000 | 1 |  |  |  |
| Waved | varchar | 8000 | 1 |  |  |  |
| StorePendingShip | varchar | 8000 | 1 |  |  |  |
| PickingForShipping | varchar | 8000 | 1 |  |  |  |
| StoreShipped | varchar | 8000 | 1 |  |  |  |
| ResendEGiftCardEmail | varchar | 8000 | 1 |  |  |  |
| ShippingError | varchar | 8000 | 1 |  |  |  |
| Shipped | varchar | 8000 | 1 |  |  |  |
| Returned | varchar | 8000 | 1 |  |  |  |
| ReturnNoCredit | varchar | 8000 | 1 |  |  |  |
| CurrentOrderStatus | varchar | 8000 | 1 |  |  |  |
| CurrentItemStatus | varchar | 8000 | 1 |  |  |  |
