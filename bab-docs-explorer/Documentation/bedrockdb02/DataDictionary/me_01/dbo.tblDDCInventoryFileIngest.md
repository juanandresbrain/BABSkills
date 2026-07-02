# dbo.tblDDCInventoryFileIngest

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReportDate | varchar | 52 | 1 |  |  |  |
| ReportTime | varchar | 52 | 1 |  |  |  |
| Stylecode | varchar | 52 | 1 |  |  |  |
| Quantityonhand | int | 4 | 1 |  |  |  |
| Quantityonhold | int | 4 | 1 |  |  |  |
| QuantityAvailable | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportDDCFileSummaries](../../StoredProcedures/me_01/dbo.spMerchandisingReportDDCFileSummaries.md)

