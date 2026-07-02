# dbo.view_detail_temp

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 0 |  |  |  |
| po_line_id | smallint | 2 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| entity_type | int | 4 | 0 |  |  |  |
| prim_size_label | varchar | 8 | 1 |  |  |  |
| prim_seq_no | smallint | 2 | 1 |  |  |  |
| sec_size_label | varchar | 8 | 1 |  |  |  |
| sec_seq_no | smallint | 2 | 1 |  |  |  |
| size_code | varchar | 17 | 1 |  |  |  |
| no_size_flag | int | 4 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| color_short_description | varchar | 8 | 1 |  |  |  |
| color_long_description | varchar | 20 | 1 |  |  |  |
| ordered_units | decimal | 17 | 1 |  |  |  |
| received_units | decimal | 17 | 1 |  |  |  |

