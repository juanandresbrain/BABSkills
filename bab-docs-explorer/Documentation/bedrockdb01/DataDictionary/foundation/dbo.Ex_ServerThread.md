# dbo.Ex_ServerThread

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| thread_index | int | 4 | 0 |  |  |  |
| active | bit | 1 | 0 |  |  |  |
| curr_status | smallint | 2 | 0 |  |  |  |
| curr_execution_id | int | 4 | 1 |  |  |  |
| requested_status | smallint | 2 | 1 |  |  |  |
| curr_pid | int | 4 | 1 |  |  |  |
