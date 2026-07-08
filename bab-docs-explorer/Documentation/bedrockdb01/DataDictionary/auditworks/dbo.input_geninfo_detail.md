# dbo.input_geninfo_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| input_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| display_def_id | smallint | 2 | 1 |  |  |  |
| form_name | nvarchar | 510 | 0 |  |  |  |
| field_name | nvarchar | 510 | 0 |  |  |  |
| field_datatype | nchar | 2 | 0 |  |  |  |
| field_data_string | nvarchar | 3000 | 1 |  |  |  |
| field_data_date | datetime | 8 | 1 |  |  |  |
| field_data_num | numeric | 9 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
