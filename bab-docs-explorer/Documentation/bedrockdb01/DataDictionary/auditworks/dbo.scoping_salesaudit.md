# dbo.scoping_salesaudit

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tag | varchar | 20 | 0 |  |  |  |
| selection_criteria | varchar | 255 | 0 |  |  |  |
| list_method | tinyint | 1 | 0 |  |  |  |
| range_method | tinyint | 1 | 0 |  |  |  |
| lookup_method | tinyint | 1 | 0 |  |  |  |
| null_method | tinyint | 1 | 0 |  |  |  |
| default_method | tinyint | 1 | 0 |  |  |  |
| enable_lookup_button | tinyint | 1 | 0 |  |  |  |
| datatype | tinyint | 1 | 0 |  |  |  |
| lookup_dw | varchar | 40 | 1 |  |  |  |
| table_name | varchar | 30 | 0 |  |  |  |
| column_name | varchar | 30 | 0 |  |  |  |
| microhelp | varchar | 60 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| encryption_flag | tinyint | 1 | 0 |  |  |  |
| selection_criteria_key | varchar | 235 | 0 |  |  |  |
