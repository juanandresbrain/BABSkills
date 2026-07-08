# dbo.ORDERS

**Database:** tpcc  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| o_id | int | 4 | 0 |  |  |  |
| o_d_id | tinyint | 1 | 0 |  |  |  |
| o_w_id | int | 4 | 0 |  |  |  |
| o_c_id | int | 4 | 0 |  |  |  |
| o_carrier_id | tinyint | 1 | 1 |  |  |  |
| o_ol_cnt | tinyint | 1 | 1 |  |  |  |
| o_all_local | tinyint | 1 | 1 |  |  |  |
| o_entry_d | datetime | 8 | 1 |  |  |  |
