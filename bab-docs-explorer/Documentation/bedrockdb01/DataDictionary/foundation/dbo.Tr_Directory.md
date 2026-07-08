# dbo.Tr_Directory

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| company_id | int | 4 | 0 |  |  |  |
| path | varchar | 255 | 0 |  |  |  |
| done_file_type | int | 4 | 1 |  |  |  |
| done_file_date_time | datetime | 8 | 1 |  |  |  |
| dir_close_date_time | datetime | 8 | 1 |  |  |  |
