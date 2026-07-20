# dbo.az_transaction_detail_facts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | bigint | 8 | 1 |  |  |  |
| transaction_id | varchar | 800 | 1 |  |  |  |
| transaction_line_seq | varchar | 800 | 1 |  |  |  |
| transaction_no | varchar | 8000 | 1 |  |  |  |
| Register_Num | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| cashier_id | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 9 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_disc_amount | decimal | 9 | 1 |  |  |  |
| upsell_disc_allocated | decimal | 9 | 1 |  |  |  |
| vat_tax_amount | decimal | 9 | 1 |  |  |  |
| ext_cost | decimal | 9 | 1 |  |  |  |
| reference_no | varchar | 320 | 1 |  |  |  |
| party_y_n | varchar | 40 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| LineItemType | varchar | 320 | 1 |  |  |  |
| NativeItemId | varchar | 320 | 1 |  |  |  |
