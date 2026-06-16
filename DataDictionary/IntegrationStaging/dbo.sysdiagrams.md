# dbo.sysdiagrams

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 |  |  |  |
| principal_id | int | 4 | 0 |  |  |  |
| diagram_id | int | 4 | 0 | YES |  |  |
| version | int | 4 | 1 |  |  |  |
| definition | varbinary | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.sp_alterdiagram](../../StoredProcedures/IntegrationStaging/dbo.sp_alterdiagram.md)
- [IntegrationStaging: dbo.sp_creatediagram](../../StoredProcedures/IntegrationStaging/dbo.sp_creatediagram.md)
- [IntegrationStaging: dbo.sp_dropdiagram](../../StoredProcedures/IntegrationStaging/dbo.sp_dropdiagram.md)
- [IntegrationStaging: dbo.sp_helpdiagramdefinition](../../StoredProcedures/IntegrationStaging/dbo.sp_helpdiagramdefinition.md)
- [IntegrationStaging: dbo.sp_helpdiagrams](../../StoredProcedures/IntegrationStaging/dbo.sp_helpdiagrams.md)
- [IntegrationStaging: dbo.sp_renamediagram](../../StoredProcedures/IntegrationStaging/dbo.sp_renamediagram.md)
- [IntegrationStaging: dbo.sp_upgraddiagrams](../../StoredProcedures/IntegrationStaging/dbo.sp_upgraddiagrams.md)

