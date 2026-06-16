# WEB.WMShippedCartons

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderType | varchar | 2 | 1 |  |  |  |
| ShipTo | varchar | 100 | 1 |  |  |  |
| CartonNumber | varchar | 20 | 1 |  |  |  |
| Style | varchar | 8 | 1 |  |  |  |
| SKUDescription | varchar | 100 | 1 |  |  |  |
| Qty | numeric | 5 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| WebOrderNumber | varchar | 20 | 1 |  |  |  |
| PartyID | int | 4 | 1 |  |  |  |
| PartyType | varchar | 20 | 1 |  |  |  |
| PartyDate | date | 3 | 1 |  |  |  |
| ShipMethod | varchar | 100 | 1 |  |  |  |
| TrackingNumber | varchar | 52 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| Transmitted | bit | 1 | 1 |  |  |  |
| TransmitDate | datetime | 8 | 1 |  |  |  |

