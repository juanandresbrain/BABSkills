# dbo.ORDER_LINE

**Database:** tpcc  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ol_o_id | int | 4 | 0 |  |  |  |
| ol_d_id | tinyint | 1 | 0 |  |  |  |
| ol_w_id | int | 4 | 0 |  |  |  |
| ol_number | tinyint | 1 | 0 |  |  |  |
| ol_i_id | int | 4 | 1 |  |  |  |
| ol_delivery_d | datetime | 8 | 1 |  |  |  |
| ol_amount | smallmoney | 4 | 1 |  |  |  |
| ol_supply_w_id | int | 4 | 1 |  |  |  |
| ol_quantity | smallint | 2 | 1 |  |  |  |
| ol_dist_info | char | 24 | 1 |  |  |  |
