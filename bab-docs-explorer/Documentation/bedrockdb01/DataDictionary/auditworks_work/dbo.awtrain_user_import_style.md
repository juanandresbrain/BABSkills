# dbo.awtrain_user_import_style

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | char | 1 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| style_long_description | varchar | 120 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| cost | money | 8 | 0 |  |  |  |
| subclass_code | tinyint | 1 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
