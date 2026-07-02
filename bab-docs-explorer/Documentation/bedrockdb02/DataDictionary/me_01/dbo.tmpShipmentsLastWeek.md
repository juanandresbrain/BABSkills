# dbo.tmpShipmentsLastWeek

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WHSE | nvarchar | 40 | 0 |  |  |  |
| STYLE | nvarchar | 40 | 0 |  |  |  |
| CARTONS | int | 4 | 1 |  |  |  |
| SHIP_WEEK | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportCartonsShippedSummary](../../StoredProcedures/me_01/dbo.spMerchandisingReportCartonsShippedSummary.md)

