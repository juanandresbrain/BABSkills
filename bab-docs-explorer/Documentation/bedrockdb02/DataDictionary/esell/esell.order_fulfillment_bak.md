# esell.order_fulfillment_bak

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 |  |  |  |
| order_id | nvarchar | 60 | 0 |  |  |  |
| transition_seq | int | 4 | 0 |  |  |  |
| order_fulfill_id | int | 4 | 0 |  |  |  |
| fulfill_cust_id | nvarchar | 40 | 1 |  |  |  |
| fulfill_outlet_id | nvarchar | 40 | 1 |  |  |  |
| fulfill_method | nvarchar | 40 | 0 |  |  |  |
| fulfill_date | datetime | 8 | 1 |  |  |  |
| fulfill_status | nvarchar | 40 | 1 |  |  |  |
| pos_trans_code | nvarchar | 120 | 1 |  |  |  |
| shipmt_track_num | nvarchar | 120 | 1 |  |  |  |
| delivery_instr | nvarchar | 2048 | 1 |  |  |  |
| comments | nvarchar | 2048 | 1 |  |  |  |
| shipping_amount | int | 4 | 1 |  |  |  |
| tax_amount | int | 4 | 1 |  |  |  |
| total_price | int | 4 | 1 |  |  |  |
| fulfill_create_timestamp | datetime | 8 | 0 |  |  |  |

