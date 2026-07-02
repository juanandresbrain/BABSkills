# esell.order_paymt_method

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| payment_method_id | nvarchar | 40 | 0 | YES |  |  |
| payment_method_name | nvarchar | 80 | 1 |  |  |  |
| payment_method_desc | nvarchar | 200 | 1 |  |  |  |
| tender_type_code | nvarchar | 100 | 1 |  |  |  |

