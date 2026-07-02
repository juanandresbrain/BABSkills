# dbo.sysmanagement_shared_server_groups_internal

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_group_id | int | 4 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 4096 | 0 |  |  |  |
| server_type | int | 4 | 0 |  |  |  |
| parent_id | int | 4 | 1 |  |  |  |
| is_system_object | bit | 1 | 1 |  |  |  |

