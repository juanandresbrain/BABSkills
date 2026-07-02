# dbo.TempDataSources

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

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

- [ReportServerBIRPT02: dbo.AddDataSource](../../StoredProcedures/ReportServerBIRPT02/dbo.AddDataSource.md)
- [ReportServerBIRPT02: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredEditSessions.md)
- [ReportServerBIRPT02: dbo.DeleteDataSources](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteDataSources.md)
- [ReportServerBIRPT02: dbo.DeleteObject](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteObject.md)

