# dbo.ContentCache

**Database:** ReportServerBIRPT02TempDB  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ContentCacheID | bigint | 8 | 0 | YES |  |  |
| CatalogItemID | uniqueidentifier | 16 | 0 |  |  |  |
| CreatedDate | datetime | 8 | 0 |  |  |  |
| ParamsHash | int | 4 | 1 |  |  |  |
| EffectiveParams | nvarchar | -1 | 1 |  |  |  |
| ContentType | nvarchar | 512 | 1 |  |  |  |
| ExpirationDate | datetime | 8 | 0 |  |  |  |
| Version | smallint | 2 | 1 |  |  |  |
| Content | varbinary | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.CleanExpiredContentCache](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanExpiredContentCache.md)
- [ReportServerBIRPT02: dbo.CreateOrUpdateContentCache](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateOrUpdateContentCache.md)
- [ReportServerBIRPT02: dbo.FlushContentCache](../../StoredProcedures/ReportServerBIRPT02/dbo.FlushContentCache.md)
- [ReportServerBIRPT02: dbo.GetContentCache](../../StoredProcedures/ReportServerBIRPT02/dbo.GetContentCache.md)
- [ReportServerBIRPT02: dbo.GetContentCacheDetails](../../StoredProcedures/ReportServerBIRPT02/dbo.GetContentCacheDetails.md)

