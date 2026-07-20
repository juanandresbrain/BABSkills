# dbo.dynamicstenderexchangefactsstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| line_sequence | decimal | 5 | 1 |  |  |  |
| line_id | decimal | 5 | 1 |  |  |  |
| line_object_description | varchar | 8000 | 1 |  |  |  |
| line_action_display_descr | varchar | 8000 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| line_action | int | 4 | 1 |  |  |  |
| gross_line_amount | decimal | 9 | 1 |  |  |  |
| pos_discount_amount | decimal | 9 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| currency_code | varchar | 8000 | 1 |  |  |  |
