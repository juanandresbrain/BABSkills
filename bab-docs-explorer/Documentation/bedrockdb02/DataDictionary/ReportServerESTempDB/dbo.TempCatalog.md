# dbo.TempCatalog

**Database:** ReportServerESTempDB  
**Server:** bedrockdb02  

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

- [ReportServerES: dbo.CleanExpiredEditSessions](../../StoredProcedures/ReportServerES/dbo.CleanExpiredEditSessions.md)
- [ReportServerES: dbo.CreateEditSession](../../StoredProcedures/ReportServerES/dbo.CreateEditSession.md)
- [ReportServerES: dbo.DeleteObject](../../StoredProcedures/ReportServerES/dbo.DeleteObject.md)
- [ReportServerES: dbo.ExtendEditSessionLifetime](../../StoredProcedures/ReportServerES/dbo.ExtendEditSessionLifetime.md)
- [ReportServerES: dbo.SetAllProperties](../../StoredProcedures/ReportServerES/dbo.SetAllProperties.md)
- [ReportServerES: dbo.SetObjectContent](../../StoredProcedures/ReportServerES/dbo.SetObjectContent.md)

