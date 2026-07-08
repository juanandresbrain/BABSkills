# dbo.Ex_OutputStat

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | int | 4 | 0 |  |  |  |
| sequence_no | int | 4 | 0 |  |  |  |
| output_type | int | 4 | 0 |  |  |  |
| record_count | int | 4 | 0 |  |  |  |
| work_file_name | varchar | 255 | 1 |  |  |  |
| work_file_size | int | 4 | 1 |  |  |  |
| work_return_code | int | 4 | 1 |  |  |  |
| work_date_time | datetime | 8 | 1 |  |  |  |
| backup_file_name | varchar | 255 | 1 |  |  |  |
| backup_file_size | int | 4 | 1 |  |  |  |
| backup_return_code | int | 4 | 1 |  |  |  |
| backup_date_time | datetime | 8 | 1 |  |  |  |
| merge_file_name | varchar | 255 | 1 |  |  |  |
| merge_file_size | int | 4 | 1 |  |  |  |
| merge_return_code | int | 4 | 1 |  |  |  |
| merge_date_time | datetime | 8 | 1 |  |  |  |
| final_file_name | varchar | 255 | 1 |  |  |  |
| final_file_size1 | int | 4 | 1 |  |  |  |
| final_file_size2 | int | 4 | 1 |  |  |  |
| final_return_code | int | 4 | 1 |  |  |  |
| final_date_time | datetime | 8 | 1 |  |  |  |
| append_flag | bit | 1 | 0 |  |  |  |
| flag_file_code | int | 4 | 1 |  |  |  |
| file_number | numeric | 9 | 1 |  |  |  |
