# dbo.work_line_object

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| lookup_line_object | smallint | 2 | 0 |  |  |  |
| new_line_object | smallint | 2 | 0 |  |  |  |
