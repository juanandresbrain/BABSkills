# dbo.ukgiftcard_storesummary_updated1

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| giftcard_no | varchar | 8000 | 1 |  |  |  |
| redeemed_Store | int | 4 | 1 |  |  |  |
| redeemed_register_no | int | 4 | 1 |  |  |  |
| redeemed_transaction_no | int | 4 | 1 |  |  |  |
| redeemed_transaction_date | datetime2 | 8 | 1 |  |  |  |
| redeemed_amount | decimal | 9 | 1 |  |  |  |
| redeemed_currency | varchar | 8000 | 1 |  |  |  |
| redeemed_country | varchar | 8000 | 1 |  |  |  |
| activated_Store | int | 4 | 1 |  |  |  |
| activated_register_no | int | 4 | 1 |  |  |  |
| activated_transaction_no | int | 4 | 1 |  |  |  |
| activated_transaction_date | datetime2 | 8 | 1 |  |  |  |
| activated_amount | decimal | 13 | 1 |  |  |  |
| activated_discount | decimal | 13 | 1 |  |  |  |
| activated_currency | varchar | 8000 | 1 |  |  |  |
| pos_discount_amount | decimal | 9 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
| currency_Code | varchar | 8000 | 1 |  |  |  |
| gross_line_amount | decimal | 9 | 1 |  |  |  |
| redeemed_amount1 | varchar | 8000 | 1 |  |  |  |
| Discount_Applied | decimal | 17 | 1 |  |  |  |
