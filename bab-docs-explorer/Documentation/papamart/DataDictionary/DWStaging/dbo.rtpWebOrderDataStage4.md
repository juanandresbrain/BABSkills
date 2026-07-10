# dbo.rtpWebOrderDataStage4

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SiteCode | varchar | 10 | 1 |  |  |  |
| OrderNumber | varchar | 32 | 1 |  |  |  |
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
| ShipToState | nvarchar | 100 | 1 |  |  |  |
| ShipToCountry | nvarchar | 100 | 1 |  |  |  |
| TrackingNumber | varchar | 50 | 1 |  |  |  |
| GaapSales | numeric | 17 | 1 |  |  |  |
| Shipping | money | 8 | 1 |  |  |  |
| ShipmentTrackingNumber | varchar | 50 | 1 |  |  |  |
| ServiceType | varchar | 50 | 1 |  |  |  |
| ShipmentDeliveryDate | varchar | 50 | 1 |  |  |  |
| NetChargeAmountUSD | varchar | 50 | 1 |  |  |  |
| Invoicedate | varchar | 50 | 1 |  |  |  |
| MasterTrackingNumber | varchar | 50 | 1 |  |  |  |
