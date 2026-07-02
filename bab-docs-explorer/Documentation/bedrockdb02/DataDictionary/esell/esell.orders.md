# esell.orders

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| order_id | nvarchar | 60 | 0 | YES |  |  |
| transition_seq | int | 4 | 0 | YES |  |  |
| billing_cust_id | nvarchar | 40 | 1 |  |  |  |
| selling_outlet_id | nvarchar | 40 | 1 |  |  |  |
| current_state | nvarchar | 40 | 1 |  |  |  |
| order_type | nvarchar | 40 | 1 |  |  |  |
| last_order_event | nvarchar | 40 | 1 |  |  |  |
| event_timestamp | datetime | 8 | 1 |  |  |  |
| modified_by | nvarchar | 40 | 1 |  |  |  |
| sales_associate | nvarchar | 40 | 1 |  |  |  |
| comments | nvarchar | 2048 | 1 |  |  |  |
| order_date | datetime | 8 | 1 |  |  |  |

