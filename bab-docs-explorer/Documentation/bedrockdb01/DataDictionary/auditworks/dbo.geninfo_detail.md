# dbo.geninfo_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| display_def_id | smallint | 2 | 1 |  |  |  |
| form_name | nvarchar | 510 | 0 |  |  |  |
| field_name | nvarchar | 510 | 0 |  |  |  |
| field_datatype | nchar | 2 | 0 |  |  |  |
| field_data_string | nvarchar | 3000 | 1 |  |  |  |
| field_data_date | datetime | 8 | 1 |  |  |  |
| field_data_num | numeric | 9 | 1 |  |  |  |
