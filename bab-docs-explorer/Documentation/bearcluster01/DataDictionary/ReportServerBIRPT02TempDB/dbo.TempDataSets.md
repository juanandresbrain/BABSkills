# dbo.TempDataSets

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | uniqueidentifier | 16 | 0 | YES |  |  |
| ItemID | uniqueidentifier | 16 | 0 |  | YES |  |
| LinkID | uniqueidentifier | 16 | 1 |  |  |  |
| Name | nvarchar | 520 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.AddDataSet](../../StoredProcedures/ReportServerBIRPT02/dbo.AddDataSet.md)
- [ReportServerBIRPT02: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredEditSessions.md)
- [ReportServerBIRPT02: dbo.DeleteDataSets](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteDataSets.md)
- [ReportServerBIRPT02: dbo.DeleteObject](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteObject.md)

