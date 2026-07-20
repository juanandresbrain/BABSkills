# dbo.jumpmind_sls_tender_settlement_line_itm

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| session_id | varchar | 8000 | 1 |  |  |  |
| till_id | varchar | 8000 | 1 |  |  |  |
| store_bank_id | varchar | 8000 | 1 |  |  |  |
| tender_type_code | varchar | 8000 | 1 |  |  |  |
| tender_code | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| open_session_amount | decimal | 17 | 1 |  |  |  |
| close_session_amount | decimal | 17 | 1 |  |  |  |
| counted_session_amount | decimal | 17 | 1 |  |  |  |
| over_under_session_amount | decimal | 17 | 1 |  |  |  |
| open_media_quantity | int | 4 | 1 |  |  |  |
| close_media_quantity | int | 4 | 1 |  |  |  |
| counted_media_quantity | int | 4 | 1 |  |  |  |
| over_under_media_quantity | int | 4 | 1 |  |  |  |
| from_repository | varchar | 8000 | 1 |  |  |  |
| to_repository | varchar | 8000 | 1 |  |  |  |
| pickup_amount | decimal | 17 | 1 |  |  |  |
| reason_code | varchar | 8000 | 1 |  |  |  |
| difference_reason | varchar | 8000 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| expected_pickup_amount | decimal | 9 | 1 |  |  |  |
