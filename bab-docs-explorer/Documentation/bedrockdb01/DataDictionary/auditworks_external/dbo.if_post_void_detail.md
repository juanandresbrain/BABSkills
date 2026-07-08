# dbo.if_post_void_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| post_voided_register | smallint | 2 | 0 |  |  |  |
| post_voided_trans_no | int | 4 | 0 |  |  |  |
| post_void_successful | tinyint | 1 | 0 |  |  |  |
| post_void_reason_code | smallint | 2 | 1 |  |  |  |
