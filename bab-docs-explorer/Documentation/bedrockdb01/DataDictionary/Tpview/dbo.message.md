# dbo.message

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| message_id | int | 4 | 0 | YES |  |  |
| description | varchar | 50 | 0 |  |  |  |
| structure_type | int | 4 | 0 |  |  |  |
| header_offset | int | 4 | 1 |  |  |  |
| header_length | int | 4 | 1 |  |  |  |
| reply_indicator_field_id | int | 4 | 1 |  |  |  |
| reply_indicator_value | varchar | 5 | 1 |  |  |  |
| start_token | varchar | 5 | 1 |  |  |  |
| mess_code_field_id | int | 4 | 1 |  |  |  |
| field_default_encoding | int | 4 | 0 |  |  |  |
| field_header_key_ordered | int | 4 | 0 |  |  |  |
| byte_order | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| message_length_field_id | int | 4 | 0 |  |  |  |
