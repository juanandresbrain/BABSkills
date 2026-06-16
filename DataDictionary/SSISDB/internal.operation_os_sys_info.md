# internal.operation_os_sys_info

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| info_id | bigint | 8 | 0 | YES |  |  |
| operation_id | bigint | 8 | 0 |  | YES |  |
| total_physical_memory_kb | bigint | 8 | 0 |  |  |  |
| available_physical_memory_kb | bigint | 8 | 1 |  |  |  |
| total_page_file_kb | bigint | 8 | 1 |  |  |  |
| available_page_file_kb | bigint | 8 | 0 |  |  |  |
| cpu_count | int | 4 | 0 |  |  |  |

