# WMS.TrueCommercePostWaveData

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WaveNumber | nvarchar | 200 | 1 |  |  |  |
| ShipmentId | nvarchar | 200 | 1 |  |  |  |
| SalesOrderNumber | nvarchar | 50 | 1 |  |  |  |
| Purpose | varchar | 8 | 1 |  |  |  |
| CustomerAccount | nvarchar | 50 | 1 |  |  |  |
| ShipToName | nvarchar | 200 | 1 |  |  |  |
| DateShipped | datetime | 8 | 1 |  |  |  |
| ShippedQuantity | int | 4 | 1 |  |  |  |
| ShippedUOM | varchar | 6 | 1 |  |  |  |
| TotalWeight | numeric | 17 | 1 |  |  |  |
| TotalVolume | numeric | 17 | 1 |  |  |  |
| ShippedFromName | varchar | 25 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeTrueCommercePostWaveData](../../StoredProcedures/IntegrationStaging/WMS.spMergeTrueCommercePostWaveData.md)

