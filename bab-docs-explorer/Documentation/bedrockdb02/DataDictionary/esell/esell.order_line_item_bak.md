# esell.order_line_item_bak

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 |  |  |  |
| order_id | nvarchar | 60 | 0 |  |  |  |
| transition_seq | int | 4 | 0 |  |  |  |
| sku_id | nvarchar | 48 | 0 |  |  |  |
| order_fulfill_id | int | 4 | 0 |  |  |  |
| department_id | nvarchar | 40 | 1 |  |  |  |
| pick_desc | nvarchar | 200 | 1 |  |  |  |
| unit_price | int | 4 | 0 |  |  |  |
| quantity_ordered | int | 4 | 1 |  |  |  |
| gift_indicator | int | 4 | 1 |  |  |  |
| gift_wrap_code | nvarchar | 40 | 0 |  |  |  |
| properties | nvarchar | 510 | 1 |  |  |  |
| event_reason_id | varchar | 20 | 1 |  |  |  |
| item_serial_number | nvarchar | 80 | 1 |  |  |  |
| line_item_number | int | 4 | 1 |  |  |  |

