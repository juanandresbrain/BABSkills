# internal.execution_data_taps

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| data_tap_id | bigint | 8 | 0 | YES |  |  |
| execution_id | bigint | 8 | 0 |  | YES |  |
| package_path | nvarchar | -1 | 1 |  |  |  |
| dataflow_path_id_string | nvarchar | 8000 | 1 |  |  |  |
| dataflow_task_guid | uniqueidentifier | 16 | 1 |  |  |  |
| max_rows | int | 4 | 1 |  |  |  |
| filename | nvarchar | 8000 | 1 |  |  |  |

