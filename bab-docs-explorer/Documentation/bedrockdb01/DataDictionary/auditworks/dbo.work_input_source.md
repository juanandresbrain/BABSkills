# dbo.work_input_source

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| input_id | numeric | 9 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| av_transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| lookup_pos_code | nvarchar | 1000 | 1 |  |  |  |
