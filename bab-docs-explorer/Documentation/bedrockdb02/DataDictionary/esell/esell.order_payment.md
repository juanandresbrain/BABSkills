# esell.order_payment

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| order_id | nvarchar | 60 | 0 | YES |  |  |
| transition_seq | int | 4 | 0 | YES |  |  |
| order_payment_id | int | 4 | 0 | YES |  |  |
| payment_status | nvarchar | 20 | 1 |  |  |  |
| payment_method_id | nvarchar | 40 | 1 |  |  |  |
| payment_amount | int | 4 | 1 |  |  |  |
| payment_number | nvarchar | 50 | 1 |  |  |  |
| payment_exp_dt | nvarchar | 40 | 1 |  |  |  |
| payment_auth_num | nvarchar | 200 | 1 |  |  |  |
| payment_info | nvarchar | 8000 | 1 |  |  |  |

