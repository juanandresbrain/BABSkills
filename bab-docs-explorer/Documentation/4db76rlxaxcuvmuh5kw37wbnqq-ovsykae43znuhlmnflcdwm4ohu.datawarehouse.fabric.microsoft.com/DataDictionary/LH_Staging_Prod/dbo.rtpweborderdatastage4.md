# dbo.rtpweborderdatastage4

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SiteCode | varchar | 8000 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| CreateDate | date | 3 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| TotalUnits | int | 4 | 1 |  |  |  |
| AnimalUnits | int | 4 | 1 |  |  |  |
| FootwearUnits | int | 4 | 1 |  |  |  |
| AccessoriesUnits | int | 4 | 1 |  |  |  |
| SoundUnits | int | 4 | 1 |  |  |  |
| ClothingUnits | int | 4 | 1 |  |  |  |
| GiftcardUnits | int | 4 | 1 |  |  |  |
| SportsUnits | int | 4 | 1 |  |  |  |
| OtherUnits | int | 4 | 1 |  |  |  |
| ShipToState | varchar | 8000 | 1 |  |  |  |
| ShipToCountry | varchar | 8000 | 1 |  |  |  |
| TrackingNumber | varchar | 8000 | 1 |  |  |  |
| GaapSales | decimal | 17 | 1 |  |  |  |
| Shipping | decimal | 9 | 1 |  |  |  |
| ShipmentTrackingNumber | varchar | 8000 | 1 |  |  |  |
| ServiceType | varchar | 8000 | 1 |  |  |  |
| ShipmentDeliveryDate | varchar | 8000 | 1 |  |  |  |
| NetChargeAmountUSD | varchar | 8000 | 1 |  |  |  |
| Invoicedate | varchar | 8000 | 1 |  |  |  |
| MasterTrackingNumber | varchar | 8000 | 1 |  |  |  |
