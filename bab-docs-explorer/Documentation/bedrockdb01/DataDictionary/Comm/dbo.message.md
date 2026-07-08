# dbo.message

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| message_id | int | 4 | 0 | YES |  |  |
| description | nvarchar | 200 | 0 |  |  |  |
| structure_type | int | 4 | 0 |  |  |  |
| reply_indicator_field_id | int | 4 | 1 |  |  |  |
| reply_indicator_value | nvarchar | 200 | 1 |  |  |  |
| STRT_TKN_VAL | nvarchar | 200 | 0 |  |  |  |
| END_TKN_VAL | nvarchar | 200 | 0 |  |  |  |
| mess_code_field_id | int | 4 | 1 |  |  |  |
| field_default_encoding | int | 4 | 0 |  |  |  |
| message_length_field_id | int | 4 | 0 |  |  |  |
| field_header_key_ordered | int | 4 | 0 |  |  |  |
| byte_order | int | 4 | 0 |  |  |  |
| method_name | varchar | 100 | 0 |  |  |  |
| EVNT_TYPE_ID | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| ROLE_TYPE | int | 4 | 0 |  |  |  |
| STRT_TKN | int | 4 | 0 |  |  |  |
| END_TKN | int | 4 | 0 |  |  |  |
| STRT_TKN_TYPE | int | 4 | 0 |  |  |  |
| END_TKN_TYPE | int | 4 | 0 |  |  |  |
| STRT_TKN_LEN | int | 4 | 0 |  |  |  |
| END_TKN_LEN | int | 4 | 0 |  |  |  |
| STRT_TKN_ENCDNG | int | 4 | 0 |  |  |  |
| END_TKN_ENCDNG | int | 4 | 0 |  |  |  |
