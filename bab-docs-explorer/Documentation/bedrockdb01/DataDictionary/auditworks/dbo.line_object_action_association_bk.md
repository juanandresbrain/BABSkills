# dbo.line_object_action_association_bk

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_category | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| db_cr_none | smallint | 2 | 0 |  |  |  |
| gl_account_segment1 | varchar | 20 | 1 |  |  |  |
| gl_account_segment2 | varchar | 20 | 1 |  |  |  |
| gl_account_segment3 | varchar | 20 | 1 |  |  |  |
| gl_account_segment4 | varchar | 20 | 1 |  |  |  |
| gl_account_segment5 | varchar | 20 | 1 |  |  |  |
| gl_account_segment6 | varchar | 20 | 1 |  |  |  |
| gl_account_segment7 | varchar | 20 | 1 |  |  |  |
| gl_account_segment8 | varchar | 20 | 1 |  |  |  |
| lookup_segment1 | tinyint | 1 | 1 |  |  |  |
| lookup_segment2 | tinyint | 1 | 1 |  |  |  |
| lookup_segment3 | tinyint | 1 | 1 |  |  |  |
| lookup_segment4 | tinyint | 1 | 1 |  |  |  |
| lookup_segment5 | tinyint | 1 | 1 |  |  |  |
| lookup_segment6 | tinyint | 1 | 1 |  |  |  |
| lookup_segment7 | tinyint | 1 | 1 |  |  |  |
| lookup_segment8 | tinyint | 1 | 1 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| discountable_group | smallint | 2 | 0 |  |  |  |
| media_category | tinyint | 1 | 0 |  |  |  |
| exception_reason | smallint | 2 | 1 |  |  |  |
| basic_subcode | char | 3 | 1 |  |  |  |
| update_register_activity | smallint | 2 | 0 |  |  |  |
| store_balance_group | tinyint | 1 | 1 |  |  |  |
| reference_no_option | tinyint | 1 | 1 |  |  |  |
| available_as_link_attachment | tinyint | 1 | 0 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| auto_config_verified | tinyint | 1 | 0 |  |  |  |
