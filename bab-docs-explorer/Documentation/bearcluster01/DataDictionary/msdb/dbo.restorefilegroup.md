# dbo.restorefilegroup

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| restore_history_id | int | 4 | 0 |  | YES |  |
| filegroup_name | nvarchar | 256 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.kk_SP_DeleteBackupHistory](../../StoredProcedures/DBAUtility/dbo.kk_SP_DeleteBackupHistory.md)

