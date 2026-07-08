# dbo.mess_field_value

**Database:** Tpview  
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
| data_source | int | 4 | 0 |  |  |  |
| attribute_id | int | 4 | 1 |  |  |  |
| internal_type | int | 4 | 1 |  |  |  |
| constant_value | varchar | 25 | 1 |  |  |  |
| loopback_code | int | 4 | 1 |  |  |  |
| loopback_mess | varchar | 255 | 1 |  |  |  |
| on_overflow | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
