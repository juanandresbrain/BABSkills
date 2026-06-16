# dbo.restorehistory

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| restore_history_id | int | 4 | 0 | YES |  |  |
| restore_date | datetime | 8 | 1 |  |  |  |
| destination_database_name | nvarchar | 256 | 1 |  |  |  |
| user_name | nvarchar | 256 | 1 |  |  |  |
| backup_set_id | int | 4 | 0 |  | YES |  |
| restore_type | char | 1 | 1 |  |  |  |
| replace | bit | 1 | 1 |  |  |  |
| recovery | bit | 1 | 1 |  |  |  |
| restart | bit | 1 | 1 |  |  |  |
| stop_at | datetime | 8 | 1 |  |  |  |
| device_count | tinyint | 1 | 1 |  |  |  |
| stop_at_mark_name | nvarchar | 256 | 1 |  |  |  |
| stop_before | bit | 1 | 1 |  |  |  |

