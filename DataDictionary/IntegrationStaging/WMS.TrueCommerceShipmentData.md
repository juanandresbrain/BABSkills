# WMS.TrueCommerceShipmentData

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UseTrueCommerceLabelSolution | varchar | 3 | 1 |  |  |  |
| WaveNumber | varchar | 12 | 1 |  |  |  |
| Pickticket | varchar | 10 | 1 |  |  |  |
| SalesOrderNumber | varchar | 20 | 1 |  |  |  |
| StoreNumber | varchar | 10 | 1 |  |  |  |
| UCC128 | varchar | 20 | 1 |  |  |  |
| ItemNumber | varchar | 8 | 1 |  |  |  |
| ItemDescription | varchar | 40 | 1 |  |  |  |
| ItemDepartment | varchar | 3 | 1 |  |  |  |
| Quantity | numeric | 5 | 1 |  |  |  |
| DateShipped | datetime | 8 | 1 |  |  |  |
| BillOfLading | varchar | 20 | 1 |  |  |  |
| InternalVendorId | varchar | 8 | 1 |  |  |  |
| ShipToName | varchar | 35 | 1 |  |  |  |
| ShipToAddress1 | varchar | 75 | 1 |  |  |  |
| ShipToCity | varchar | 40 | 1 |  |  |  |
| ShipToZip | varchar | 11 | 1 |  |  |  |
| ShipFromName | varchar | 27 | 1 |  |  |  |
| ShipFromAddress1 | varchar | 24 | 1 |  |  |  |
| ShipFromCity | varchar | 9 | 1 |  |  |  |
| ShipFromZip | varchar | 5 | 1 |  |  |  |
| Code | varchar | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeTrueCommerceShipmentData](../../StoredProcedures/IntegrationStaging/WMS.spMergeTrueCommerceShipmentData.md)

