# dbo.backupmediafamily

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| media_set_id | int | 4 | 0 | YES | YES |  |
| family_sequence_number | tinyint | 1 | 0 | YES |  |  |
| media_family_id | uniqueidentifier | 16 | 1 |  |  |  |
| media_count | int | 4 | 1 |  |  |  |
| logical_device_name | nvarchar | 256 | 1 |  |  |  |
| physical_device_name | nvarchar | 520 | 1 |  |  |  |
| device_type | tinyint | 1 | 1 |  |  |  |
| physical_block_size | int | 4 | 1 |  |  |  |
| mirror | tinyint | 1 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_delete_backuphistory](../../StoredProcedures/msdb/dbo.sp_delete_backuphistory.md)
- [msdb: dbo.sp_delete_database_backuphistory](../../StoredProcedures/msdb/dbo.sp_delete_database_backuphistory.md)
- [DBAUtility: dbo.kk_SP_DeleteBackupHistory](../../StoredProcedures/DBAUtility/dbo.kk_SP_DeleteBackupHistory.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)

