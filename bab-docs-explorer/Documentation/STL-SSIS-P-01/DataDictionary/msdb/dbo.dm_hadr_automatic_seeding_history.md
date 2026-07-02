# dbo.dm_hadr_automatic_seeding_history

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| start_time | datetime | 8 | 0 |  |  |  |
| completion_time | datetime | 8 | 1 |  |  |  |
| ag_id | uniqueidentifier | 16 | 0 |  |  |  |
| ag_db_id | uniqueidentifier | 16 | 0 |  |  |  |
| ag_remote_replica_id | uniqueidentifier | 16 | 0 |  |  |  |
| operation_id | uniqueidentifier | 16 | 0 |  |  |  |
| is_source | bit | 1 | 0 |  |  |  |
| current_state | nvarchar | 8000 | 0 |  |  |  |
| performed_seeding | bit | 1 | 0 |  |  |  |
| failure_state | int | 4 | 1 |  |  |  |
| failure_state_desc | nvarchar | 8000 | 1 |  |  |  |
| error_code | int | 4 | 1 |  |  |  |
| number_of_attempts | int | 4 | 0 |  |  |  |

