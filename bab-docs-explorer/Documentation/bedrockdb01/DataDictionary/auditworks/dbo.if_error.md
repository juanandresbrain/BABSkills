# dbo.if_error

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_error_id | numeric | 9 | 0 | YES |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| resource_id | int | 4 | 1 |  |  |  |
| token | nvarchar | 510 | 1 |  |  |  |
| resource_string | nvarchar | 510 | 1 |  |  |  |
| exception_type | smallint | 2 | 0 |  |  |  |
| entity_code | smallint | 2 | 1 |  |  |  |
| object_key | nvarchar | 510 | 1 |  |  |  |
| sys_code | int | 4 | 1 |  |  |  |
| sys_message | nvarchar | 510 | 1 |  |  |  |
| internal_class_name | nvarchar | 510 | 1 |  |  |  |
| method_name | nvarchar | 510 | 1 |  |  |  |
