# dbo.mess_field_value_test

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_type_id | int | 4 | 0 |  |  |  |
| interface_id | int | 4 | 0 |  |  |  |
| message_id | int | 4 | 0 |  |  |  |
| field_id | int | 4 | 0 |  |  |  |
| message_role | int | 4 | 0 |  |  |  |
| group_sequence | int | 4 | 0 |  |  |  |
| test_sequence | int | 4 | 0 |  |  |  |
| data_source | int | 4 | 0 |  |  |  |
| attribute_id | int | 4 | 1 |  |  |  |
| internal_type | int | 4 | 1 |  |  |  |
| operator | varchar | 2 | 0 |  |  |  |
| field_value | nvarchar | 50 | 1 |  |  |  |
| expression_operator | varchar | 3 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
