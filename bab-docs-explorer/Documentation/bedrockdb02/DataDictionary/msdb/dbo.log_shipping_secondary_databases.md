# dbo.log_shipping_secondary_databases

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| secondary_database | sysname | 256 | 0 | YES |  |  |
| secondary_id | uniqueidentifier | 16 | 0 |  |  |  |
| restore_delay | int | 4 | 0 |  |  |  |
| restore_all | bit | 1 | 0 |  |  |  |
| restore_mode | bit | 1 | 0 |  |  |  |
| disconnect_users | bit | 1 | 0 |  |  |  |
| block_size | int | 4 | 1 |  |  |  |
| buffer_count | int | 4 | 1 |  |  |  |
| max_transfer_size | int | 4 | 1 |  |  |  |
| last_restored_file | nvarchar | 1000 | 1 |  |  |  |
| last_restored_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [master: dbo.DatabaseBackup](../../StoredProcedures/master/dbo.DatabaseBackup.md)
- [master: dbo.spDatabaseBackupOnDemand](../../StoredProcedures/master/dbo.spDatabaseBackupOnDemand.md)
- [DBAUtility: dbo.DatabaseBackup](../../StoredProcedures/DBAUtility/dbo.DatabaseBackup.md)

