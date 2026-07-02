# dbo.SessionData

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

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

- [ReportServerBIRPT02: dbo.AddPersistedStream](../../StoredProcedures/ReportServerBIRPT02/dbo.AddPersistedStream.md)
- [ReportServerBIRPT02: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredEditSessions.md)
- [ReportServerBIRPT02: dbo.CleanExpiredSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredSessions.md)
- [ReportServerBIRPT02: dbo.ClearSessionSnapshot](../../StoredProcedures/ReportServerBIRPT02/dbo.ClearSessionSnapshot.md)
- [ReportServerBIRPT02: dbo.CreateSession](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateSession.md)
- [ReportServerBIRPT02: dbo.DereferenceSessionSnapshot](../../StoredProcedures/ReportServerBIRPT02/dbo.DereferenceSessionSnapshot.md)
- [ReportServerBIRPT02: dbo.GetSessionData](../../StoredProcedures/ReportServerBIRPT02/dbo.GetSessionData.md)
- [ReportServerBIRPT02: dbo.RemoveReportFromSession](../../StoredProcedures/ReportServerBIRPT02/dbo.RemoveReportFromSession.md)
- [ReportServerBIRPT02: dbo.SetSessionCredentials](../../StoredProcedures/ReportServerBIRPT02/dbo.SetSessionCredentials.md)
- [ReportServerBIRPT02: dbo.SetSessionData](../../StoredProcedures/ReportServerBIRPT02/dbo.SetSessionData.md)
- [ReportServerBIRPT02: dbo.SetSessionParameters](../../StoredProcedures/ReportServerBIRPT02/dbo.SetSessionParameters.md)

