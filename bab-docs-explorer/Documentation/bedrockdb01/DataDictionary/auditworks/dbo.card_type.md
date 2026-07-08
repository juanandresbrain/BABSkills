# dbo.card_type

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| card_type | char | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| card_type_description | varchar | 255 | 0 |  |  |  |
| check_digit_routine_number | tinyint | 1 | 0 |  |  |  |
| payment_line_object | smallint | 2 | 1 |  |  |  |
| gl_replacement_value | varchar | 20 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| code_meaning_control | char | 1 | 1 |  |  |  |
