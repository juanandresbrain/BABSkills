# dbo.webshippingfactsstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
