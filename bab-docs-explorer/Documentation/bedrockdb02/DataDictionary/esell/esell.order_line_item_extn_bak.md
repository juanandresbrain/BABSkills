# esell.order_line_item_extn_bak

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
| unit_price | int | 4 | 0 |  |  |  |
| gift_wrap_code | nvarchar | 40 | 0 |  |  |  |
| item_serial_number | nvarchar | 80 | 0 |  |  |  |
| item_property_bag | nvarchar | 510 | 1 |  |  |  |
| height | int | 4 | 1 |  |  |  |
| depth | int | 4 | 1 |  |  |  |
| width | int | 4 | 1 |  |  |  |
| weight | int | 4 | 1 |  |  |  |
| gift_wrap_type | nvarchar | 510 | 1 |  |  |  |
| line_item_type | nvarchar | 80 | 1 |  |  |  |
| line_item_number | int | 4 | 0 |  |  |  |

