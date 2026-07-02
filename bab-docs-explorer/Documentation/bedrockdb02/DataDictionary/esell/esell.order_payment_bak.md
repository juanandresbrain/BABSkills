# esell.order_payment_bak

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 |  |  |  |
| order_id | nvarchar | 60 | 0 |  |  |  |
| transition_seq | int | 4 | 0 |  |  |  |
| order_payment_id | int | 4 | 0 |  |  |  |
| payment_status | nvarchar | 20 | 1 |  |  |  |
| payment_method_id | nvarchar | 40 | 1 |  |  |  |
| payment_amount | int | 4 | 1 |  |  |  |
| payment_number | nvarchar | 50 | 1 |  |  |  |
| payment_exp_dt | nvarchar | 40 | 1 |  |  |  |
| payment_auth_num | nvarchar | 200 | 1 |  |  |  |
| payment_info | nvarchar | 8000 | 1 |  |  |  |

