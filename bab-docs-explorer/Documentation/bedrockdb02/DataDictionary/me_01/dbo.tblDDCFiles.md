# dbo.tblDDCFiles

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DDCFileName | varchar | 52 | 1 |  |  |  |
| DDCFileType | varchar | 52 | 1 |  |  |  |
| Capture_Date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportDDCFileSummaries](../../StoredProcedures/me_01/dbo.spMerchandisingReportDDCFileSummaries.md)
- [me_01: dbo.spMerchandisingSelectDDCFiles](../../StoredProcedures/me_01/dbo.spMerchandisingSelectDDCFiles.md)

