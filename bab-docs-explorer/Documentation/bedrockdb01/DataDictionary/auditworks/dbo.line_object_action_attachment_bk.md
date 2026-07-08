# dbo.line_object_action_attachment_bk

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| attachment_type | smallint | 2 | 0 |  |  |  |
| note_type | int | 4 | 0 |  |  |  |
| merchandise_category | smallint | 2 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| attachment_mandatory | tinyint | 1 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
| auto_config_verified | tinyint | 1 | 0 |  |  |  |
| approval_status_date | smalldatetime | 4 | 0 |  |  |  |
