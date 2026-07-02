# esell.order_line_item

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| order_id | nvarchar | 60 | 0 | YES |  |  |
| transition_seq | int | 4 | 0 | YES |  |  |
| sku_id | nvarchar | 48 | 0 | YES |  |  |
| order_fulfill_id | int | 4 | 0 | YES |  |  |
| department_id | nvarchar | 40 | 1 |  |  |  |
| pick_desc | nvarchar | 200 | 1 |  |  |  |
| unit_price | int | 4 | 0 | YES |  |  |
| quantity_ordered | int | 4 | 1 |  |  |  |
| gift_indicator | int | 4 | 1 |  |  |  |
| gift_wrap_code | nvarchar | 40 | 0 | YES |  |  |
| properties | nvarchar | 510 | 1 |  |  |  |
| event_reason_id | varchar | 20 | 0 | YES |  |  |
| item_serial_number | nvarchar | 80 | 0 | YES |  |  |
| line_item_number | int | 4 | 0 | YES |  |  |

