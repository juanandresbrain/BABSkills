# esell.order_fulfillment_extn

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| order_id | nvarchar | 60 | 0 | YES |  |  |
| transition_seq | int | 4 | 0 | YES |  |  |
| order_fulfill_id | int | 4 | 0 | YES |  |  |
| shipment_method | nvarchar | 2048 | 1 |  |  |  |
| gift_message | nvarchar | 510 | 1 |  |  |  |
| shipping_amount_tax | int | 4 | 1 |  |  |  |
| pickup_outlet_id | nvarchar | 40 | 1 |  |  |  |
| shipment_method_code | varchar | 10 | 1 |  |  |  |

