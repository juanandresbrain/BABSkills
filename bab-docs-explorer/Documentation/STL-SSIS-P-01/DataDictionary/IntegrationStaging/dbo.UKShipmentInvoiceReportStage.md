# dbo.UKShipmentInvoiceReportStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShipFrom | varchar | 4 | 1 |  |  |  |
| ShipTo | varchar | 4 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ItemNumber | varchar | 6 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| Multiple | varchar | 4 | 1 |  |  |  |
| ProductDescription | varchar | 50 | 1 |  |  |  |
| HTS | varchar | 20 | 1 |  |  |  |
| CountryOfOrigin | varchar | 20 | 1 |  |  |  |
| NetWeight | float | 8 | 1 |  |  |  |
| UnitCost | float | 8 | 1 |  |  |  |
| ExtendedCost | float | 8 | 1 |  |  |  |
| address_name | nvarchar | 120 | 1 |  |  |  |
| address_line1 | nvarchar | 100 | 1 |  |  |  |
| address_line2 | nvarchar | 100 | 1 |  |  |  |
| address_city | nvarchar | 40 | 1 |  |  |  |
| address_state | nvarchar | 40 | 1 |  |  |  |
| address_zip_code | nvarchar | 30 | 1 |  |  |  |
| country_code | nvarchar | 6 | 1 |  |  |  |
| Invoice | varchar | 20 | 1 |  |  |  |
| ShipFrom | varchar | 4 | 1 |  |  |  |
| ShipTo | varchar | 4 | 1 |  |  |  |
| ShipDate | date | 3 | 1 |  |  |  |
| ItemNumber | varchar | 6 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| Multiple | varchar | 4 | 1 |  |  |  |
| ProductDescription | varchar | 50 | 1 |  |  |  |
| HTS | varchar | 20 | 1 |  |  |  |
| CountryOfOrigin | varchar | 20 | 1 |  |  |  |
| NetWeight | float | 8 | 1 |  |  |  |
| address_name | nvarchar | 120 | 1 |  |  |  |
| address_line1 | nvarchar | 100 | 1 |  |  |  |
| address_line2 | nvarchar | 100 | 1 |  |  |  |
| address_city | nvarchar | 40 | 1 |  |  |  |
| address_state | nvarchar | 40 | 1 |  |  |  |
| address_zip_code | nvarchar | 30 | 1 |  |  |  |
| country_code | nvarchar | 6 | 1 |  |  |  |
| Invoice | varchar | 20 | 1 |  |  |  |
| InventoryUnitSymbol | nvarchar | 20 | 1 |  |  |  |
| FromUnitSymbol | nvarchar | 20 | 1 |  |  |  |
| ToUnitSymbol | nvarchar | 20 | 1 |  |  |  |
| Factor | nvarchar | 20 | 1 |  |  |  |
| UnitCost | numeric | 9 | 1 |  |  |  |
| ShipmentFileProcessingDate | date | 3 | 1 |  |  |  |

