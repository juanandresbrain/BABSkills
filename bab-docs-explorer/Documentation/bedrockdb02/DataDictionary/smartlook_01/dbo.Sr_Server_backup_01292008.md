# dbo.Sr_Server_backup_01292008

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_id | int | 4 | 0 |  |  |  |
| server_name | varchar | 30 | 1 |  |  |  |
| any_job | bit | 1 | 0 |  |  |  |
| max_jobs | smallint | 2 | 0 |  |  |  |
| curr_status | smallint | 2 | 0 |  |  |  |
| requested_status | smallint | 2 | 1 |  |  |  |
| machine_id | int | 4 | 0 |  |  |  |
| autostart | smallint | 2 | 0 |  |  |  |

