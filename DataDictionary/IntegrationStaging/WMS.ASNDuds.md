# WMS.ASNDuds

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PO_nbr | nvarchar | 50 | 1 |  |  |  |
| Po_Shipment_Line_nbr | int | 4 | 1 |  |  |  |
| ItemId | nvarchar | 50 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| shipment | nvarchar | 30 | 1 |  |  |  |
| lpn | nvarchar | 40 | 1 |  |  |  |
| Unit | varchar | 2 | 1 |  |  |  |
| Vehicle | nvarchar | 40 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailASNExportSummary](../../StoredProcedures/IntegrationStaging/WMS.spEmailASNExportSummary.md)

