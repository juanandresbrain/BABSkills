# dbo.restorefile

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| restore_history_id | int | 4 | 0 |  | YES |  |
| file_number | numeric | 9 | 1 |  |  |  |
| destination_phys_drive | nvarchar | 520 | 1 |  |  |  |
| destination_phys_name | nvarchar | 520 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_delete_backuphistory](../../StoredProcedures/msdb/dbo.sp_delete_backuphistory.md)
- [msdb: dbo.sp_delete_database_backuphistory](../../StoredProcedures/msdb/dbo.sp_delete_database_backuphistory.md)
- [DBAUtility: dbo.kk_SP_DeleteBackupHistory](../../StoredProcedures/DBAUtility/dbo.kk_SP_DeleteBackupHistory.md)

