# dbo.TempDataSets

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | uniqueidentifier | 16 | 0 | YES |  |  |
| ItemID | uniqueidentifier | 16 | 0 |  | YES |  |
| LinkID | uniqueidentifier | 16 | 1 |  |  |  |
| Name | nvarchar | 520 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerES: dbo.AddDataSet](../../StoredProcedures/ReportServerES/dbo.AddDataSet.md)
- [ReportServerES: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredEditSessions.md)
- [ReportServerES: dbo.DeleteDataSets](../../StoredProcedures/ReportServerES/dbo.DeleteDataSets.md)
- [ReportServerES: dbo.DeleteObject](../../StoredProcedures/ReportServerES/dbo.DeleteObject.md)

