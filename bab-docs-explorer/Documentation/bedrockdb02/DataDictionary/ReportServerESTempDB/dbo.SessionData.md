# dbo.SessionData

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | varchar | 32 | 0 |  |  |  |
| CompiledDefinition | uniqueidentifier | 16 | 1 |  |  |  |
| SnapshotDataID | uniqueidentifier | 16 | 1 |  |  |  |
| IsPermanentSnapshot | bit | 1 | 1 |  |  |  |
| ReportPath | nvarchar | 928 | 1 |  |  |  |
| Timeout | int | 4 | 0 |  |  |  |
| AutoRefreshSeconds | int | 4 | 1 |  |  |  |
| Expiration | datetime | 8 | 0 |  |  |  |
| ShowHideInfo | image | 256 | 1 |  |  |  |
| DataSourceInfo | image | 256 | 1 |  |  |  |
| OwnerID | uniqueidentifier | 16 | 0 |  |  |  |
| EffectiveParams | ntext | 256 | 1 |  |  |  |
| CreationTime | datetime | 8 | 0 |  |  |  |
| HasInteractivity | bit | 1 | 1 |  |  |  |
| SnapshotExpirationDate | datetime | 8 | 1 |  |  |  |
| HistoryDate | datetime | 8 | 1 |  |  |  |
| PageHeight | float | 8 | 1 |  |  |  |
| PageWidth | float | 8 | 1 |  |  |  |
| TopMargin | float | 8 | 1 |  |  |  |
| BottomMargin | float | 8 | 1 |  |  |  |
| LeftMargin | float | 8 | 1 |  |  |  |
| RightMargin | float | 8 | 1 |  |  |  |
| AwaitingFirstExecution | bit | 1 | 1 |  |  |  |
| EditSessionID | varchar | 32 | 1 |  |  |  |
| DataSetInfo | varbinary | -1 | 1 |  |  |  |
| SitePath | nvarchar | 880 | 1 |  |  |  |
| SiteZone | int | 4 | 0 |  |  |  |
| ReportDefinitionPath | nvarchar | 928 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerES: dbo.AddPersistedStream](../../StoredProcedures/ReportServerES/dbo.AddPersistedStream.md)
- [ReportServerES: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredEditSessions.md)
- [ReportServerES: dbo.CleanExpiredSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredSessions.md)
- [ReportServerES: dbo.ClearSessionSnapshot](../../StoredProcedures/ReportServerES/dbo.ClearSessionSnapshot.md)
- [ReportServerES: dbo.CreateSession](../../StoredProcedures/ReportServerES/dbo.CreateSession.md)
- [ReportServerES: dbo.DereferenceSessionSnapshot](../../StoredProcedures/ReportServerES/dbo.DereferenceSessionSnapshot.md)
- [ReportServerES: dbo.GetSessionData](../../StoredProcedures/ReportServerES/dbo.GetSessionData.md)
- [ReportServerES: dbo.RemoveReportFromSession](../../StoredProcedures/ReportServerES/dbo.RemoveReportFromSession.md)
- [ReportServerES: dbo.SetSessionCredentials](../../StoredProcedures/ReportServerES/dbo.SetSessionCredentials.md)
- [ReportServerES: dbo.SetSessionData](../../StoredProcedures/ReportServerES/dbo.SetSessionData.md)
- [ReportServerES: dbo.SetSessionParameters](../../StoredProcedures/ReportServerES/dbo.SetSessionParameters.md)

