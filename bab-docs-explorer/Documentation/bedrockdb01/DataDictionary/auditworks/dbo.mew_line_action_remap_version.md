# dbo.mew_line_action_remap_version

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| version_code | nvarchar | 100 | 0 |  |  |  |
| system_ownership_flag | tinyint | 1 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| replacement_line_action | smallint | 2 | 1 |  |  |  |
| merch_transaction_type | smallint | 2 | 1 |  |  |  |
