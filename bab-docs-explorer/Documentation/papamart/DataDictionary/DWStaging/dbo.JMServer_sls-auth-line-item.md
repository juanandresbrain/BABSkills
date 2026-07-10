# dbo.JMServer_sls-auth-line-item

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 50 | 1 |  |  |  |
| business_date | varchar | 50 | 1 |  |  |  |
| sequence_number | varchar | 50 | 1 |  |  |  |
| line_sequence_number | varchar | 50 | 1 |  |  |  |
| ref_line_sequence_number | varchar | 50 | 1 |  |  |  |
| card_line_sequence_number | varchar | 50 | 1 |  |  |  |
| voided | varchar | 50 | 1 |  |  |  |
| post_void | varchar | 50 | 1 |  |  |  |
| auth_type_code | varchar | 50 | 1 |  |  |  |
| result_code | varchar | 50 | 1 |  |  |  |
| requested_amount | varchar | 50 | 1 |  |  |  |
| authorized_amount | varchar | 50 | 1 |  |  |  |
| remaining_balance_amount | varchar | 50 | 1 |  |  |  |
| auth_code | varchar | 50 | 1 |  |  |  |
| verification_method_code | varchar | 50 | 1 |  |  |  |
| auth_method_code | varchar | 50 | 1 |  |  |  |
| auth_result_code | varchar | 50 | 1 |  |  |  |
| iso_currency_code | varchar | 50 | 1 |  |  |  |
| partially_approved | varchar | 50 | 1 |  |  |  |
| payment_token | varchar | 50 | 1 |  |  |  |
| token_type | varchar | 50 | 1 |  |  |  |
| emv_application_id | varchar | 50 | 1 |  |  |  |
| emv_application_cryptogram | varchar | 50 | 1 |  |  |  |
| provider_name | varchar | 50 | 1 |  |  |  |
| signature_format_code | varchar | 50 | 1 |  |  |  |
| signature_name | varchar | 50 | 1 |  |  |  |
| receipt_text | varchar | 50 | 1 |  |  |  |
| store_only_receipt_text | varchar | 50 | 1 |  |  |  |
| signature | varchar | 50 | 1 |  |  |  |
| stan | varchar | 50 | 1 |  |  |  |
| session_data | varchar | 50 | 1 |  |  |  |
| auth_time | varchar | 50 | 1 |  |  |  |
| merchant_ref | varchar | 50 | 1 |  |  |  |
| terminal_id | varchar | 50 | 1 |  |  |  |
| referenced_return | varchar | 50 | 1 |  |  |  |
