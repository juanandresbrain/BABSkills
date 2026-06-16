# dbo.autoadmin_task_agent_metadata

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| task_agent_guid | uniqueidentifier | 16 | 0 | YES |  |  |
| autoadmin_id | bigint | 8 | 0 | YES |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| task_agent_data | xml | -1 | 1 |  |  |  |
| schema_version | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.autoadmin_metadata_delete_task_agent_data_for_database](../../StoredProcedures/msdb/dbo.autoadmin_metadata_delete_task_agent_data_for_database.md)
- [msdb: dbo.autoadmin_metadata_delete_task_agent_global_data](../../StoredProcedures/msdb/dbo.autoadmin_metadata_delete_task_agent_global_data.md)
- [msdb: dbo.autoadmin_metadata_insert_task_agent_global_data](../../StoredProcedures/msdb/dbo.autoadmin_metadata_insert_task_agent_global_data.md)
- [msdb: dbo.autoadmin_metadata_query_dbs](../../StoredProcedures/msdb/dbo.autoadmin_metadata_query_dbs.md)
- [msdb: dbo.autoadmin_metadata_query_task_agent_global_data](../../StoredProcedures/msdb/dbo.autoadmin_metadata_query_task_agent_global_data.md)
- [msdb: dbo.autoadmin_metadata_update_task_agent_data_for_database](../../StoredProcedures/msdb/dbo.autoadmin_metadata_update_task_agent_data_for_database.md)
- [msdb: dbo.autoadmin_metadata_update_task_agent_global_data](../../StoredProcedures/msdb/dbo.autoadmin_metadata_update_task_agent_global_data.md)

