# ERP.ItemsUOM

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DENOMINATOR | int | 4 | 1 |  |  |  |
| FACTOR | numeric | 17 | 1 |  |  |  |
| FROMUNITSYMBOL | varchar | 50 | 1 |  |  |  |
| INNEROFFSET | numeric | 17 | 1 |  |  |  |
| NUMERATOR | int | 4 | 1 |  |  |  |
| OUTEROFFSET | numeric | 17 | 1 |  |  |  |
| PRODUCTNUMBER | varchar | 50 | 1 |  |  |  |
| ROUNDING | varchar | 50 | 1 |  |  |  |
| TOUNITSYMBOL | varchar | 50 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| Denominator | int | 4 | 1 |  |  |  |
| Factor | float | 8 | 1 |  |  |  |
| FromUnitSymbol | nvarchar | 8000 | 1 |  |  |  |
| InnerOffset | float | 8 | 1 |  |  |  |
| Numerator | int | 4 | 1 |  |  |  |
| OuterOffset | float | 8 | 1 |  |  |  |
| ProductNumber | nvarchar | 8000 | 1 |  |  |  |
| Rounding | nvarchar | 510 | 1 |  |  |  |
| ToUnitSymbol | nvarchar | 8000 | 1 |  |  |  |
| Entity | nvarchar | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spPFTGetOpenToByRollingCountsAndAttributes_ERP](../../StoredProcedures/IntegrationStaging/ERP.spPFTGetOpenToByRollingCountsAndAttributes_ERP.md)

