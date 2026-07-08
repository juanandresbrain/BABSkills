# dbo.line_object_action_lookup

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| lookup_line_object | smallint | 2 | 0 |  |  |  |
| lookup_line_action | tinyint | 1 | 0 |  |  |  |
| lookup_pos_code | nvarchar | 1000 | 0 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| discount_reversal_flag | tinyint | 1 | 1 |  |  |  |
| lookup_code_type | tinyint | 1 | 0 |  |  |  |
