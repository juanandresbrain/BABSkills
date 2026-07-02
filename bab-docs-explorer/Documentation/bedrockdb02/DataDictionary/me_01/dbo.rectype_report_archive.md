# dbo.rectype_report_archive

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| from_location_code | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_label | nvarchar | 80 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| qty_shipped | int | 4 | 1 |  |  |  |
| rectype | int | 4 | 1 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| distribution_no | nvarchar | 40 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportRecType](../../StoredProcedures/me_01/dbo.spMerchandisingReportRecType.md)

