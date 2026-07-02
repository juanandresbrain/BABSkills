# dbo.sysssispackages

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 | YES |  |  |
| id | uniqueidentifier | 16 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| createdate | datetime | 8 | 0 |  |  |  |
| folderid | uniqueidentifier | 16 | 0 | YES |  |  |
| ownersid | varbinary | 85 | 0 |  |  |  |
| packagedata | image | 16 | 0 |  |  |  |
| packageformat | int | 4 | 0 |  |  |  |
| packagetype | int | 4 | 0 |  |  |  |
| vermajor | int | 4 | 0 |  |  |  |
| verminor | int | 4 | 0 |  |  |  |
| verbuild | int | 4 | 0 |  |  |  |
| vercomments | nvarchar | 2048 | 1 |  |  |  |
| verid | uniqueidentifier | 16 | 0 |  |  |  |
| isencrypted | bit | 1 | 0 |  |  |  |
| readrolesid | varbinary | 85 | 1 |  |  |  |
| writerolesid | varbinary | 85 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_ssis_checkexists](../../StoredProcedures/msdb/dbo.sp_ssis_checkexists.md)
- [msdb: dbo.sp_ssis_deletefolder](../../StoredProcedures/msdb/dbo.sp_ssis_deletefolder.md)
- [msdb: dbo.sp_ssis_deletepackage](../../StoredProcedures/msdb/dbo.sp_ssis_deletepackage.md)
- [msdb: dbo.sp_ssis_getpackage](../../StoredProcedures/msdb/dbo.sp_ssis_getpackage.md)
- [msdb: dbo.sp_ssis_getpackageroles](../../StoredProcedures/msdb/dbo.sp_ssis_getpackageroles.md)
- [msdb: dbo.sp_ssis_listpackages](../../StoredProcedures/msdb/dbo.sp_ssis_listpackages.md)
- [msdb: dbo.sp_ssis_putpackage](../../StoredProcedures/msdb/dbo.sp_ssis_putpackage.md)
- [msdb: dbo.sp_ssis_setpackageroles](../../StoredProcedures/msdb/dbo.sp_ssis_setpackageroles.md)
- [msdb: dbo.sp_syscollector_create_collector_type](../../StoredProcedures/msdb/dbo.sp_syscollector_create_collector_type.md)
- [msdb: dbo.sp_syscollector_create_tsql_query_collector](../../StoredProcedures/msdb/dbo.sp_syscollector_create_tsql_query_collector.md)
- [msdb: dbo.sp_syscollector_event_onpackagebegin](../../StoredProcedures/msdb/dbo.sp_syscollector_event_onpackagebegin.md)
- [msdb: dbo.sp_syscollector_get_tsql_query_collector_package_ids](../../StoredProcedures/msdb/dbo.sp_syscollector_get_tsql_query_collector_package_ids.md)
- [msdb: dbo.sp_syscollector_update_collector_type](../../StoredProcedures/msdb/dbo.sp_syscollector_update_collector_type.md)

