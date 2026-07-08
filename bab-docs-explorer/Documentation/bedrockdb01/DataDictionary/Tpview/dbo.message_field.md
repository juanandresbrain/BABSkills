# dbo.message_field

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| message_id | int | 4 | 0 |  |  |  |
| field_id | int | 4 | 0 |  |  |  |
| parent_field_id | int | 4 | 1 |  |  |  |
| field_iso_number | int | 4 | 1 |  |  |  |
| field_name | varchar | 25 | 0 |  |  |  |
| field_offset | int | 4 | 1 |  |  |  |
| field_length | int | 4 | 1 |  |  |  |
| field_separator | int | 4 | 1 |  |  |  |
| field_scale | int | 4 | 1 |  |  |  |
| field_justification | int | 4 | 1 |  |  |  |
| field_padding | int | 4 | 1 |  |  |  |
| field_header | int | 4 | 1 |  |  |  |
| field_format | varchar | 25 | 0 |  |  |  |
| sequence | int | 4 | 0 |  |  |  |
| sub_sequence | int | 4 | 1 |  |  |  |
| data_type | int | 4 | 0 |  |  |  |
| db_col_name | int | 4 | 1 |  |  |  |
| mandatory | int | 4 | 0 |  |  |  |
| field_length_type | int | 4 | 0 |  |  |  |
| field_header_length | int | 4 | 1 |  |  |  |
| field_header_type | int | 4 | 1 |  |  |  |
| field_header_encoding | int | 4 | 0 |  |  |  |
| field_encoding | int | 4 | 0 |  |  |  |
| field_null_in_string | int | 4 | 0 |  |  |  |
| field_header_key | int | 4 | 0 |  |  |  |
| field_header_key_type | int | 4 | 1 |  |  |  |
| field_header_key_length | int | 4 | 1 |  |  |  |
| field_header_key_encoding | int | 4 | 1 |  |  |  |
| field_header_key_value | varchar | 25 | 1 |  |  |  |
| field_role | int | 4 | 0 |  |  |  |
| length_starts | int | 4 | 0 |  |  |  |
| length_starts_field_id | int | 4 | 0 |  |  |  |
| length_ends | int | 4 | 0 |  |  |  |
| length_ends_field_id | int | 4 | 0 |  |  |  |
| field_iso_bitmap_id | int | 4 | 0 |  |  |  |
| bitmap_id | int | 4 | 0 |  |  |  |
| bitmap_base_field_number | int | 4 | 0 |  |  |  |
| field_header_key_ordered | int | 4 | 0 |  |  |  |
| field_header_bitmap | int | 4 | 0 |  |  |  |
| field_header_bitmap_offset | int | 4 | 0 |  |  |  |
| field_header_bitmap_length | int | 4 | 0 |  |  |  |
| separator_scope | int | 4 | 0 |  |  |  |
| field_header_scope | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
