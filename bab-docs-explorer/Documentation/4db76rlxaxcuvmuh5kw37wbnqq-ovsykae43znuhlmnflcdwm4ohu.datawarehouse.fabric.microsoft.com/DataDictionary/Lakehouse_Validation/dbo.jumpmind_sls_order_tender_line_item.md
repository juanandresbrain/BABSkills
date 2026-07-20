# dbo.jumpmind_sls_order_tender_line_item

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| tender_code | varchar | 8000 | 1 |  |  |  |
| tender_type_code | varchar | 8000 | 1 |  |  |  |
| change_flag | int | 4 | 1 |  |  |  |
| customer_account_number | varchar | 8000 | 1 |  |  |  |
| tender_account_number | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| tender_amount | decimal | 17 | 1 |  |  |  |
| cash_back_amount | decimal | 17 | 1 |  |  |  |
| iso_foreign_currency_code | varchar | 8000 | 1 |  |  |  |
| foreign_currency_amount | decimal | 17 | 1 |  |  |  |
| exchange_rate | decimal | 17 | 1 |  |  |  |
| overtendered | int | 4 | 1 |  |  |  |
| partially_approved | int | 4 | 1 |  |  |  |
| tender_finance_id | varchar | 8000 | 1 |  |  |  |
| certificate_number | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| tender_auth_method_code | varchar | 8000 | 1 |  |  |  |
| tender_group | varchar | 8000 | 1 |  |  |  |
| voucher_id | varchar | 8000 | 1 |  |  |  |
| loyalty_points_redeemed | decimal | 17 | 1 |  |  |  |
