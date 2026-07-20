# dbo.jumpmind_sls_order_pre_auth

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| auth_type_code | varchar | 8000 | 1 |  |  |  |
| result_code | varchar | 8000 | 1 |  |  |  |
| requested_amount | decimal | 17 | 1 |  |  |  |
| authorized_amount | decimal | 17 | 1 |  |  |  |
| remaining_balance_amount | decimal | 17 | 1 |  |  |  |
| auth_code | varchar | 8000 | 1 |  |  |  |
| verification_method_code | varchar | 8000 | 1 |  |  |  |
| auth_method_code | varchar | 8000 | 1 |  |  |  |
| auth_result_code | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| partially_approved | int | 4 | 1 |  |  |  |
| payment_token | varchar | 8000 | 1 |  |  |  |
| token_type | varchar | 8000 | 1 |  |  |  |
| emv_application_id | varchar | 8000 | 1 |  |  |  |
| emv_application_cryptogram | varchar | 8000 | 1 |  |  |  |
| provider_name | varchar | 8000 | 1 |  |  |  |
| signature_format_code | varchar | 8000 | 1 |  |  |  |
| signature_name | varchar | 8000 | 1 |  |  |  |
| receipt_text | varchar | 8000 | 1 |  |  |  |
| store_only_receipt_text | varchar | 8000 | 1 |  |  |  |
| signature | varchar | 8000 | 1 |  |  |  |
| stan | varchar | 8000 | 1 |  |  |  |
| session_data | varchar | 8000 | 1 |  |  |  |
| auth_time | datetime2 | 8 | 1 |  |  |  |
| merchant_ref | varchar | 8000 | 1 |  |  |  |
| terminal_id | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| original_sale_ref | varchar | 8000 | 1 |  |  |  |
| currency_conversion_text | varchar | 8000 | 1 |  |  |  |
| application_label | varchar | 8000 | 1 |  |  |  |
| application_id | varchar | 8000 | 1 |  |  |  |
| terminal_verification_result | varchar | 8000 | 1 |  |  |  |
| issuer_application_data | varchar | 8000 | 1 |  |  |  |
| transaction_status_information | varchar | 8000 | 1 |  |  |  |
| authorization_response_code | varchar | 8000 | 1 |  |  |  |
| application_cryptogram | varchar | 8000 | 1 |  |  |  |
