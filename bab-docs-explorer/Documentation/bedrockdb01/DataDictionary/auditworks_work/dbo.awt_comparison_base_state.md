# dbo.awt_comparison_base_state

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| comparison_id | int | 4 | 0 |  |  |  |
| table_name | varchar | 30 | 0 |  |  |  |
| validation_area | varchar | 30 | 0 |  |  |  |
| comparison_key | varchar | 255 | 0 |  |  |  |
| comparison_text1 | varchar | 255 | 1 |  |  |  |
| comparison_text2 | varchar | 255 | 1 |  |  |  |
| comparison_text_minor | varchar | 255 | 1 |  |  |  |
