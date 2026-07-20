# dbo.giftcard_detail_idw

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LineID | int | 4 | 1 |  |  |  |
| FileID | int | 4 | 1 |  |  |  |
| line_number | int | 4 | 1 |  |  |  |
| merchant_id | varchar | 8000 | 1 |  |  |  |
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| terminal_id | int | 4 | 1 |  |  |  |
| terminal_transaction_number | bigint | 8 | 1 |  |  |  |
| account_number | varchar | 8000 | 1 |  |  |  |
| request_code | int | 4 | 1 |  |  |  |
| transaction_amount | decimal | 9 | 1 |  |  |  |
| base_amount | decimal | 9 | 1 |  |  |  |
| reporting_amount | decimal | 9 | 1 |  |  |  |
| base_currency_code | int | 4 | 1 |  |  |  |
| local_currency_code | int | 4 | 1 |  |  |  |
| reporting_currency_code | int | 4 | 1 |  |  |  |
| exchange_rate | decimal | 9 | 1 |  |  |  |
| response_code | int | 4 | 1 |  |  |  |
| source_code | int | 4 | 1 |  |  |  |
| clerk_id | varchar | 8000 | 1 |  |  |  |
| reversal_flag | varchar | 8000 | 1 |  |  |  |
| balance | decimal | 9 | 1 |  |  |  |
| consortium_code | int | 4 | 1 |  |  |  |
| promotion_code | int | 4 | 1 |  |  |  |
| FDMS_local_timestamp | datetime2 | 8 | 1 |  |  |  |
| terminal_local_timestamp | datetime2 | 8 | 1 |  |  |  |
| replaced_by_account_number | varchar | 8000 | 1 |  |  |  |
| authcode | varchar | 8000 | 1 |  |  |  |
| userid | varchar | 8000 | 1 |  |  |  |
| card_class | int | 4 | 1 |  |  |  |
| expiration_date | datetime2 | 8 | 1 |  |  |  |
| card_cost | decimal | 9 | 1 |  |  |  |
| escheatable_transaction | varchar | 8000 | 1 |  |  |  |
| reference_number | varchar | 8000 | 1 |  |  |  |
| user1 | varchar | 8000 | 1 |  |  |  |
| user2 | varchar | 8000 | 1 |  |  |  |
| cashback | decimal | 9 | 1 |  |  |  |
| base_cashback | decimal | 9 | 1 |  |  |  |
| reporting_cashback | decimal | 9 | 1 |  |  |  |
| local_lock_amount | decimal | 9 | 1 |  |  |  |
| lock_amount | decimal | 9 | 1 |  |  |  |
| reversed_timestamp | datetime2 | 8 | 1 |  |  |  |
| processed_date | datetime2 | 8 | 1 |  |  |  |
| original_request_code | int | 4 | 1 |  |  |  |
| internal_request_code | int | 4 | 1 |  |  |  |
| exported_date | datetime2 | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
