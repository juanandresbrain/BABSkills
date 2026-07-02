# dbo.restorefile

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| restore_history_id | int | 4 | 0 |  | YES |  |
| file_number | numeric | 9 | 1 |  |  |  |
| destination_phys_drive | nvarchar | 520 | 1 |  |  |  |
| destination_phys_name | nvarchar | 520 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.kk_SP_DeleteBackupHistory](../../StoredProcedures/DBAUtility/dbo.kk_SP_DeleteBackupHistory.md)

