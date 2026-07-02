# dbo.sysssispackagefolders

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| folderid | uniqueidentifier | 16 | 0 | YES |  |  |
| parentfolderid | uniqueidentifier | 16 | 1 |  |  |  |
| foldername | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_ssis_addfolder](../../StoredProcedures/msdb/dbo.sp_ssis_addfolder.md)
- [msdb: dbo.sp_ssis_deletefolder](../../StoredProcedures/msdb/dbo.sp_ssis_deletefolder.md)
- [msdb: dbo.sp_ssis_getfolder](../../StoredProcedures/msdb/dbo.sp_ssis_getfolder.md)
- [msdb: dbo.sp_ssis_listfolders](../../StoredProcedures/msdb/dbo.sp_ssis_listfolders.md)
- [msdb: dbo.sp_ssis_renamefolder](../../StoredProcedures/msdb/dbo.sp_ssis_renamefolder.md)

