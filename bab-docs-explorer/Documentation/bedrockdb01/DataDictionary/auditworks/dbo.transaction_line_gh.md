# dbo.transaction_line_gh

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_sequence | numeric | 5 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| gross_line_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| pos_discount_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| db_cr_none | smallint | 2 | 0 |  |  |  |
| attachment_qty | tinyint | 1 | 0 |  |  |  |
| exception_flag | tinyint | 1 | 0 |  |  |  |
| interface_rejection_flag | tinyint | 1 | 0 |  |  |  |
| line_void_flag | tinyint | 1 | 0 |  |  |  |
| voiding_reversal_flag | smallint | 2 | 0 |  |  |  |
| line_modified_flag | tinyint | 1 | 0 |  |  |  |
| edit_timestamp | float | 8 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| discountable_group | smallint | 2 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| invalid_reference_no | nvarchar | 160 | 1 |  |  |  |
| unit_of_measure | smallint | 2 | 1 |  |  |  |
