# dbo.sa_rejection_reason

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| violated_sareject_rule | smallint | 2 | 0 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
| process_id | binary | 16 | 1 |  |  |  |
| lookup_pos_code | nvarchar | 1000 | 1 |  |  |  |
| override_flag | tinyint | 1 | 1 |  |  |  |
