# dbo.WebShippingFactsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CreateDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 32 | 1 |  |  |  |
| ShipToState | nvarchar | 100 | 1 |  |  |  |
| ShipToCountry | nvarchar | 100 | 1 |  |  |  |
| TrackingNumber | varchar | 50 | 1 |  |  |  |
| Shipping | money | 8 | 1 |  |  |  |
| SiteCode | varchar | 10 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ShipmentTrackingNumber | varchar | 50 | 1 |  |  |  |
| ServiceType | varchar | 50 | 1 |  |  |  |
| ShipmentDeliveryDate | varchar | 50 | 1 |  |  |  |
| NetChargeAmountUSD | varchar | 50 | 1 |  |  |  |
| Invoicedate | varchar | 50 | 1 |  |  |  |
| MasterTrackingNumber | varchar | 50 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
