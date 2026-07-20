# dbo.giftcard_batchadjustment_record

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| batch_id | int | 4 | 1 |  |  |  |
| record_id | int | 4 | 1 |  |  |  |
| record_format_indicator | varchar | 8000 | 1 |  |  |  |
| reserved1 | varchar | 8000 | 1 |  |  |  |
| merchant_id | varchar | 8000 | 1 |  |  |  |
| reserved2 | varchar | 8000 | 1 |  |  |  |
| alternate_merchant_number | varchar | 8000 | 1 |  |  |  |
| terminal_id | varchar | 8000 | 1 |  |  |  |
| terminal_transaction_number | varchar | 8000 | 1 |  |  |  |
| account_number | varchar | 8000 | 1 |  |  |  |
| request_code | varchar | 8000 | 1 |  |  |  |
| sign1 | varchar | 8000 | 1 |  |  |  |
| transaction_amount | varchar | 8000 | 1 |  |  |  |
| clerk_id | varchar | 8000 | 1 |  |  |  |
| terminal_local_timestamp | varchar | 8000 | 1 |  |  |  |
| replaced_by_account_number | varchar | 8000 | 1 |  |  |  |
| reserved3 | varchar | 8000 | 1 |  |  |  |
| card_class | varchar | 8000 | 1 |  |  |  |
| apply_adjustment | varchar | 8000 | 1 |  |  |  |
| card_cost | varchar | 8000 | 1 |  |  |  |
| escheatable_transaction | varchar | 8000 | 1 |  |  |  |
| reference_number | varchar | 8000 | 1 |  |  |  |
| user1 | varchar | 8000 | 1 |  |  |  |
| user2 | varchar | 8000 | 1 |  |  |  |
| card_available_for_use_date | varchar | 8000 | 1 |  |  |  |
| expiration_date | varchar | 8000 | 1 |  |  |  |
| currency_code | varchar | 8000 | 1 |  |  |  |
| filler | varchar | 8000 | 1 |  |  |  |
