# dbo.autoadmin_managed_databases

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| autoadmin_id | bigint | 8 | 0 | YES |  |  |
| db_name | nvarchar | 256 | 0 | YES |  |  |
| db_id | int | 4 | 0 | YES |  |  |
| db_guid | uniqueidentifier | 16 | 0 | YES |  |  |
| group_db_guid | uniqueidentifier | 16 | 1 |  |  |  |
| drop_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.autoadmin_metadata_delete_task_agent_data_for_database](../../StoredProcedures/msdb/dbo.autoadmin_metadata_delete_task_agent_data_for_database.md)
- [msdb: dbo.autoadmin_metadata_query_dbs](../../StoredProcedures/msdb/dbo.autoadmin_metadata_query_dbs.md)
- [msdb: dbo.autoadmin_metadata_update_task_agent_data_for_database](../../StoredProcedures/msdb/dbo.autoadmin_metadata_update_task_agent_data_for_database.md)

