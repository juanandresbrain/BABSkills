# dbo.TempDataSources

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DSID | uniqueidentifier | 16 | 0 | YES |  |  |
| ItemID | uniqueidentifier | 16 | 0 |  | YES |  |
| Name | nvarchar | 520 | 1 |  |  |  |
| Extension | nvarchar | 520 | 1 |  |  |  |
| Link | uniqueidentifier | 16 | 1 |  |  |  |
| CredentialRetrieval | int | 4 | 1 |  |  |  |
| Prompt | ntext | 16 | 1 |  |  |  |
| ConnectionString | image | 16 | 1 |  |  |  |
| OriginalConnectionString | image | 16 | 1 |  |  |  |
| OriginalConnectStringExpressionBased | bit | 1 | 1 |  |  |  |
| UserName | image | 16 | 1 |  |  |  |
| Password | image | 16 | 1 |  |  |  |
| Flags | int | 4 | 1 |  |  |  |
| Version | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerES: dbo.AddDataSource](../../StoredProcedures/ReportServerES/dbo.AddDataSource.md)
- [ReportServerES: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredEditSessions.md)
- [ReportServerES: dbo.DeleteDataSources](../../StoredProcedures/ReportServerES/dbo.DeleteDataSources.md)
- [ReportServerES: dbo.DeleteObject](../../StoredProcedures/ReportServerES/dbo.DeleteObject.md)

