# dbo.GiftCard_Detail

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LineID | int | 4 | 0 | YES |  |  |
| FileID | int | 4 | 0 |  |  |  |
| line_number | int | 4 | 1 |  |  |  |
| merchant_id | varchar | 16 | 1 |  |  |  |
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| terminal_id | int | 4 | 1 |  |  |  |
| terminal_transaction_number | bigint | 8 | 1 |  |  |  |
| account_number | varchar | 19 | 1 |  |  |  |
| request_code | int | 4 | 1 |  |  |  |
| transaction_amount | money | 8 | 1 |  |  |  |
| base_amount | money | 8 | 1 |  |  |  |
| reporting_amount | money | 8 | 1 |  |  |  |
| base_currency_code | int | 4 | 1 |  |  |  |
| local_currency_code | int | 4 | 1 |  |  |  |
| reporting_currency_code | int | 4 | 1 |  |  |  |
| exchange_rate | numeric | 9 | 1 |  |  |  |
| response_code | int | 4 | 1 |  |  |  |
| source_code | int | 4 | 1 |  |  |  |
| clerk_id | varchar | 8 | 1 |  |  |  |
| reversal_flag | char | 1 | 1 |  |  |  |
| balance | money | 8 | 1 |  |  |  |
| consortium_code | int | 4 | 1 |  |  |  |
| promotion_code | int | 4 | 1 |  |  |  |
| FDMS_local_timestamp | datetime | 8 | 1 |  |  |  |
| terminal_local_timestamp | datetime | 8 | 1 |  |  |  |
| replaced_by_account_number | varchar | 19 | 1 |  |  |  |
| authcode | varchar | 8 | 1 |  |  |  |
| userid | varchar | 8 | 1 |  |  |  |
| card_class | int | 4 | 1 |  |  |  |
| expiration_date | datetime | 8 | 1 |  |  |  |
| card_cost | money | 8 | 1 |  |  |  |
| escheatable_transaction | char | 1 | 1 |  |  |  |
| reference_number | varchar | 16 | 1 |  |  |  |
| user1 | varchar | 20 | 1 |  |  |  |
| user2 | varchar | 20 | 1 |  |  |  |
| cashback | money | 8 | 1 |  |  |  |
| base_cashback | money | 8 | 1 |  |  |  |
| reporting_cashback | money | 8 | 1 |  |  |  |
| local_lock_amount | money | 8 | 1 |  |  |  |
| lock_amount | money | 8 | 1 |  |  |  |
| reversed_timestamp | datetime | 8 | 1 |  |  |  |
| processed_date | datetime | 8 | 1 |  |  |  |
| original_request_code | int | 4 | 1 |  |  |  |
| internal_request_code | int | 4 | 1 |  |  |  |
| exported_date | datetime | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
