# dbo.jmserver_sls_auth_line_item

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | varchar | 8000 | 1 |  |  |  |
| ref_line_sequence_number | varchar | 8000 | 1 |  |  |  |
| card_line_sequence_number | varchar | 8000 | 1 |  |  |  |
| voided | varchar | 8000 | 1 |  |  |  |
| post_void | varchar | 8000 | 1 |  |  |  |
| auth_type_code | varchar | 8000 | 1 |  |  |  |
| result_code | varchar | 8000 | 1 |  |  |  |
| requested_amount | varchar | 8000 | 1 |  |  |  |
| authorized_amount | varchar | 8000 | 1 |  |  |  |
| remaining_balance_amount | varchar | 8000 | 1 |  |  |  |
| auth_code | varchar | 8000 | 1 |  |  |  |
| verification_method_code | varchar | 8000 | 1 |  |  |  |
| auth_method_code | varchar | 8000 | 1 |  |  |  |
| auth_result_code | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| partially_approved | varchar | 8000 | 1 |  |  |  |
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
| auth_time | varchar | 8000 | 1 |  |  |  |
| merchant_ref | varchar | 8000 | 1 |  |  |  |
| terminal_id | varchar | 8000 | 1 |  |  |  |
| referenced_return | varchar | 8000 | 1 |  |  |  |
