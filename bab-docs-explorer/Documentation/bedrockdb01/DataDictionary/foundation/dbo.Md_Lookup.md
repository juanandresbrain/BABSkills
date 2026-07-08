# dbo.Md_Lookup

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| lookup_id | int | 4 | 0 |  |  |  |
| lookup_descritpion_1 | varchar | 255 | 1 |  |  |  |
| lookup_descritpion_2 | varchar | 255 | 1 |  |  |  |
| table_id | int | 4 | 0 |  |  |  |
| display_expression_1 | varchar | 1024 | 0 |  |  |  |
| display_expression_2 | varchar | 1024 | 0 |  |  |  |
| value_expression | varchar | 60 | 0 |  |  |  |
| resolve_join | bit | 1 | 0 |  |  |  |
| where_expression | varchar | 255 | 1 |  |  |  |
