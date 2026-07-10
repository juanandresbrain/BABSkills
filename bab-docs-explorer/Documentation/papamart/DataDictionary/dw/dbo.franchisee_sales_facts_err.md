# dbo.franchisee_sales_facts_err

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| week_ending_date_key | int | 4 | 1 |  |  |  |
| franchisee_store_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| total_sales | decimal | 9 | 1 |  |  |  |
| sales_plan | decimal | 9 | 1 |  |  |  |
| transaction_count | int | 4 | 1 |  |  |  |
| footware_sales | decimal | 9 | 1 |  |  |  |
| footware_units | int | 4 | 1 |  |  |  |
| sound_sales | decimal | 9 | 1 |  |  |  |
| sound_units | int | 4 | 1 |  |  |  |
| unstuffed_sales | decimal | 9 | 1 |  |  |  |
| unstuffed_units | int | 4 | 1 |  |  |  |
| party_sales | decimal | 9 | 1 |  |  |  |
| party_count | int | 4 | 1 |  |  |  |
| gift_card_sales | decimal | 9 | 1 |  |  |  |
| gift_card_units | int | 4 | 1 |  |  |  |
| accessories_sales | decimal | 9 | 1 |  |  |  |
| accessories_units | int | 4 | 1 |  |  |  |
| clothes_sales | decimal | 9 | 1 |  |  |  |
| clothes_units | int | 4 | 1 |  |  |  |
| sports_sales | decimal | 9 | 1 |  |  |  |
| sports_units | int | 4 | 1 |  |  |  |
| prestuffed_sales | decimal | 9 | 1 |  |  |  |
| prestuffed_units | int | 4 | 1 |  |  |  |
| Error | varchar | 100 | 1 |  |  |  |
| ErrorDateTime | smalldatetime | 4 | 1 |  |  |  |
| coupons_and_discounts | decimal | 9 | 1 |  |  |  |
| returns | decimal | 9 | 1 |  |  |  |
| giftcards_redeemed | decimal | 9 | 1 |  |  |  |
| exchange_rate | decimal | 9 | 1 |  |  |  |
| withholding_tax_rate | decimal | 9 | 1 |  |  |  |
