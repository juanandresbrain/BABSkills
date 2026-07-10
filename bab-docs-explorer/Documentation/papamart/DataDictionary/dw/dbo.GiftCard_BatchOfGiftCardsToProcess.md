# dbo.GiftCard_BatchOfGiftCardsToProcess

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merchant_id | varchar | 20 | 1 |  |  |  |
| alternate_merchant_number | varchar | 16 | 1 |  |  |  |
| account_number | varchar | 20 | 1 |  |  |  |
| request_code | varchar | 10 | 1 |  |  |  |
| transaction_amount | money | 8 | 1 |  |  |  |
| local_currency_code | char | 3 | 1 |  |  |  |
