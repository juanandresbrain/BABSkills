# dbo.util_comparison_current_state

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | int | 4 | 0 |  |  |  |
| comparison_id | int | 4 | 0 |  |  |  |
| table_name | nvarchar | 60 | 0 |  |  |  |
| validation_area | nvarchar | 60 | 0 |  |  |  |
| comparison_key | nvarchar | 510 | 0 |  |  |  |
| comparison_text1 | nvarchar | 510 | 1 |  |  |  |
| comparison_text2 | nvarchar | 510 | 1 |  |  |  |
| comparison_text_minor | nvarchar | 510 | 1 |  |  |  |
