# WEB.PartyTransferOrdersShipped

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyID | int | 4 | 1 |  |  |  |
| PartyDate | date | 3 | 1 |  |  |  |
| StoreNumber | varchar | 4 | 1 |  |  |  |
| Style | varchar | 8 | 1 |  |  |  |
| SKUDescription | varchar | 100 | 1 |  |  |  |
| QtyShipped | int | 4 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ShipMethod | varchar | 100 | 1 |  |  |  |
| TrackingNumber | varchar | 52 | 1 |  |  |  |
| TransferNumber | varchar | 100 | 1 |  |  |  |
| TransferUnitsSent | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spEmailPartyWebOrderShippedSummary_BAK06172024](../../StoredProcedures/IntegrationStaging/WEB.spEmailPartyWebOrderShippedSummary_BAK06172024.md)

