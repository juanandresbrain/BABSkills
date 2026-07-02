# dbo.TempCatalog

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EditSessionID | varchar | 32 | 0 | YES |  |  |
| TempCatalogID | uniqueidentifier | 16 | 0 |  |  |  |
| ContextPath | nvarchar | 850 | 0 | YES |  |  |
| Name | nvarchar | 850 | 0 |  |  |  |
| Content | varbinary | -1 | 1 |  |  |  |
| Description | nvarchar | -1 | 1 |  |  |  |
| Intermediate | uniqueidentifier | 16 | 1 |  |  |  |
| IntermediateIsPermanent | bit | 1 | 0 |  |  |  |
| Property | nvarchar | -1 | 1 |  |  |  |
| Parameter | nvarchar | -1 | 1 |  |  |  |
| OwnerID | uniqueidentifier | 16 | 0 |  |  |  |
| CreationTime | datetime | 8 | 0 |  |  |  |
| ExpirationTime | datetime | 8 | 0 |  |  |  |
| DataCacheHash | varbinary | 64 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredEditSessions.md)
- [ReportServerBIRPT02: dbo.CreateEditSession](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateEditSession.md)
- [ReportServerBIRPT02: dbo.DeleteObject](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteObject.md)
- [ReportServerBIRPT02: dbo.ExtendEditSessionLifetime](../../StoredProcedures/ReportServerBIRPT02/dbo.ExtendEditSessionLifetime.md)
- [ReportServerBIRPT02: dbo.SetAllProperties](../../StoredProcedures/ReportServerBIRPT02/dbo.SetAllProperties.md)
- [ReportServerBIRPT02: dbo.SetObjectContent](../../StoredProcedures/ReportServerBIRPT02/dbo.SetObjectContent.md)

