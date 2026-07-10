# dbo.ld_transaction_pos_facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| time_key | int | 4 | 0 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| product_key | int | 4 | 0 |  |  |  |
| transaction_id | decimal | 9 | 0 |  |  |  |
| Transaction_No | int | 4 | 1 |  |  |  |
| register_num | int | 4 | 0 |  |  |  |
| party_y_n | char | 1 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| upsell_disc_allocated | money | 8 | 1 |  |  |  |
