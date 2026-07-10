# dbo.GiftCard_BatchAdjustment_Record

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| batch_id | int | 4 | 0 |  |  |  |
| record_id | int | 4 | 0 | YES |  |  |
| record_format_indicator | char | 1 | 0 |  |  |  |
| reserved1 | char | 4 | 0 |  |  |  |
| merchant_id | char | 16 | 0 |  |  |  |
| reserved2 | char | 4 | 0 |  |  |  |
| alternate_merchant_number | char | 16 | 0 |  |  |  |
| terminal_id | char | 4 | 0 |  |  |  |
| terminal_transaction_number | char | 17 | 0 |  |  |  |
| account_number | char | 19 | 0 |  |  |  |
| request_code | char | 5 | 0 |  |  |  |
| sign1 | char | 1 | 0 |  |  |  |
| transaction_amount | char | 10 | 0 |  |  |  |
| clerk_id | char | 8 | 0 |  |  |  |
| terminal_local_timestamp | char | 13 | 0 |  |  |  |
| replaced_by_account_number | char | 19 | 0 |  |  |  |
| reserved3 | char | 8 | 0 |  |  |  |
| card_class | char | 4 | 0 |  |  |  |
| apply_adjustment | char | 1 | 0 |  |  |  |
| card_cost | char | 10 | 0 |  |  |  |
| escheatable_transaction | char | 1 | 0 |  |  |  |
| reference_number | char | 16 | 0 |  |  |  |
| user1 | char | 20 | 0 |  |  |  |
| user2 | char | 20 | 0 |  |  |  |
| card_available_for_use_date | char | 8 | 0 |  |  |  |
| expiration_date | char | 8 | 0 |  |  |  |
| currency_code | char | 3 | 0 |  |  |  |
| filler | char | 63 | 0 |  |  |  |
