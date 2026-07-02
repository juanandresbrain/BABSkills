# dbo.aspnet_SchemaVersions

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Feature | nvarchar | 256 | 0 | YES |  |  |
| CompatibleSchemaVersion | nvarchar | 256 | 0 | YES |  |  |
| IsCurrentVersion | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.aspnet_CheckSchemaVersion](../../StoredProcedures/ApplicationResources/dbo.aspnet_CheckSchemaVersion.md)
- [ApplicationResources: dbo.aspnet_RegisterSchemaVersion](../../StoredProcedures/ApplicationResources/dbo.aspnet_RegisterSchemaVersion.md)
- [ApplicationResources: dbo.aspnet_UnRegisterSchemaVersion](../../StoredProcedures/ApplicationResources/dbo.aspnet_UnRegisterSchemaVersion.md)

