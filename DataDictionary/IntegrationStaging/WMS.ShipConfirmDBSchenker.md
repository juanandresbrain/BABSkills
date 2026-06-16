# WMS.ShipConfirmDBSchenker

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | int | 4 | 1 |  |  |  |
| itemId | nvarchar | 200 | 1 |  |  |  |
| itemName | nvarchar | 200 | 1 |  |  |  |
| countryOfOrigin | nvarchar | 200 | 1 |  |  |  |
| harmonizedCode | nvarchar | 200 | 1 |  |  |  |
| quantity | numeric | 9 | 1 |  |  |  |
| unitPrice | numeric | 9 | 1 |  |  |  |
| netSalesPrice | numeric | 9 | 1 |  |  |  |
| loadNumber | nvarchar | 200 | 1 |  |  |  |
| warehouse | nvarchar | 200 | 1 |  |  |  |
| ShipToCountry | nvarchar | 40 | 1 |  |  |  |
| _upstream.EnqueuedTimeUTC | nvarchar | 8000 | 1 |  |  |  |
| _upstream.MessageId | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| SentToHA | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeShipConfirmDBSchenker](../../StoredProcedures/IntegrationStaging/WMS.spMergeShipConfirmDBSchenker.md)
- [IntegrationStaging: WMS.spWMPrintDBSchenkerShipments](../../StoredProcedures/IntegrationStaging/WMS.spWMPrintDBSchenkerShipments.md)
- [IntegrationStaging: WMS.spWMSelectDBSchenkerShipments](../../StoredProcedures/IntegrationStaging/WMS.spWMSelectDBSchenkerShipments.md)

