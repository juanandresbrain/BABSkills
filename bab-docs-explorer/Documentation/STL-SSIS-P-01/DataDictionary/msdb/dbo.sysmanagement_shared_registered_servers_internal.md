# dbo.sysmanagement_shared_registered_servers_internal

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_id | int | 4 | 0 | YES |  |  |
| server_group_id | int | 4 | 1 |  | YES |  |
| name | sysname | 256 | 0 |  |  |  |
| server_name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 4096 | 0 |  |  |  |
| server_type | int | 4 | 0 |  |  |  |

