# dbo.webshippingfacts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CreateDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| ShipToState | varchar | 8000 | 1 |  |  |  |
| ShipToCountry | varchar | 8000 | 1 |  |  |  |
| TrackingNumber | varchar | 8000 | 1 |  |  |  |
| Shipping | decimal | 9 | 1 |  |  |  |
| SiteCode | varchar | 8000 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ShipmentTrackingNumber | varchar | 8000 | 1 |  |  |  |
| ServiceType | varchar | 8000 | 1 |  |  |  |
| ShipmentDeliveryDate | varchar | 8000 | 1 |  |  |  |
| NetChargeAmountUSD | varchar | 8000 | 1 |  |  |  |
| Invoicedate | varchar | 8000 | 1 |  |  |  |
| MasterTrackingNumber | varchar | 8000 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
| InsertDate | date | 3 | 1 |  |  |  |
| UpdateDate | date | 3 | 1 |  |  |  |
