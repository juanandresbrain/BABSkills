# dbo.message_field

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| message_id | int | 4 | 0 |  |  |  |
| field_id | int | 4 | 0 |  |  |  |
| parent_field_id | int | 4 | 1 |  |  |  |
| field_iso_number | int | 4 | 1 |  |  |  |
| field_name | nvarchar | 200 | 0 |  |  |  |
| field_offset | int | 4 | 1 |  |  |  |
| field_length | int | 4 | 1 |  |  |  |
| SPRTR_VAL | nvarchar | 50 | 1 |  |  |  |
| field_scale | int | 4 | 1 |  |  |  |
| field_justification | int | 4 | 1 |  |  |  |
| PAD_VAL | nvarchar | 28 | 1 |  |  |  |
| field_header | int | 4 | 1 |  |  |  |
| field_format | varchar | 25 | 0 |  |  |  |
| sequence | int | 4 | 0 |  |  |  |
| sub_sequence | int | 4 | 1 |  |  |  |
| data_type | int | 4 | 0 |  |  |  |
| mandatory | int | 4 | 0 |  |  |  |
| field_length_type | int | 4 | 0 |  |  |  |
| field_header_length | int | 4 | 1 |  |  |  |
| field_header_type | int | 4 | 1 |  |  |  |
| field_header_encoding | int | 4 | 0 |  |  |  |
| field_encoding | int | 4 | 0 |  |  |  |
| field_header_key | int | 4 | 0 |  |  |  |
| field_header_key_type | int | 4 | 1 |  |  |  |
| field_header_key_length | int | 4 | 1 |  |  |  |
| field_header_key_encoding | int | 4 | 1 |  |  |  |
| field_header_key_value | nvarchar | 50 | 1 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
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
| SPRTR_SCP | int | 4 | 0 |  |  |  |
| field_header_scope | int | 4 | 0 |  |  |  |
| SNSTV_INFRMTN | int | 4 | 0 |  |  |  |
| PAD | int | 4 | 0 |  |  |  |
| SPRTR | int | 4 | 0 |  |  |  |
| SPRTR_TYPE | int | 4 | 0 |  |  |  |
| SPRTR_ENCDNG | int | 4 | 0 |  |  |  |
| SPRTR_LEN | int | 4 | 0 |  |  |  |
