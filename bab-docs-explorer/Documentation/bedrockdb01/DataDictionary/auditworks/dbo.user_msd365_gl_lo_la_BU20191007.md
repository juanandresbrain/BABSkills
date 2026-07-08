# dbo.user_msd365_gl_lo_la_BU20191007

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_category | int | 4 | 0 |  |  |  |
| line_object | int | 4 | 0 |  |  |  |
| line_action | int | 4 | 0 |  |  |  |
| category_description | nvarchar | 510 | 0 |  |  |  |
| line_object_description | nvarchar | 510 | 0 |  |  |  |
| line_action_display_descr | nvarchar | 510 | 0 |  |  |  |
| account_display_value | nvarchar | 510 | 1 |  |  |  |
| bank_trans_type | nvarchar | 510 | 1 |  |  |  |
| country_code | varchar | 3 | 0 |  |  |  |
