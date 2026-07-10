# dbo.FranchiseeTransactionFacts_Stage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | varchar | 20 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 0 |  |  |  |
| transaction_key | varchar | 92 | 0 |  |  |  |
| transaction_no | varchar | 20 | 0 |  |  |  |
| register_no | int | 4 | 0 |  |  |  |
| line_count | int | 4 | 1 |  |  |  |
| party_flag | int | 4 | 0 |  |  |  |
| GAAP_transaction_flag | int | 4 | 0 |  |  |  |
| donation_only_flag | int | 4 | 0 |  |  |  |
| giftcard_only_flag | int | 4 | 0 |  |  |  |
| party_deposit_only_flag | int | 4 | 0 |  |  |  |
| GAAP_sales_amount | numeric | 17 | 1 |  |  |  |
| net_sales_amount | numeric | 17 | 1 |  |  |  |
| total_units | int | 4 | 1 |  |  |  |
| unit_net_amount | numeric | 17 | 1 |  |  |  |
| unit_gross_amount | numeric | 17 | 1 |  |  |  |
| reward_certificate_amount | int | 4 | 0 |  |  |  |
| buy_stuff_amount | int | 4 | 0 |  |  |  |
| tax_amount | numeric | 17 | 1 |  |  |  |
| redemption_amount | numeric | 17 | 1 |  |  |  |
| unit_discount_amount | numeric | 17 | 1 |  |  |  |
| coupon_discount_amount | int | 4 | 0 |  |  |  |
| coupon_discount_units | int | 4 | 0 |  |  |  |
| giftcard_discount_amount | numeric | 17 | 1 |  |  |  |
| total_discount_amount | numeric | 17 | 1 |  |  |  |
| receipt_total_amount | numeric | 17 | 1 |  |  |  |
| merchandise_uga | numeric | 17 | 1 |  |  |  |
| merchandise_units | int | 4 | 1 |  |  |  |
| gaap_units | int | 4 | 1 |  |  |  |
| donations_UGA | int | 4 | 0 |  |  |  |
| donations_units | int | 4 | 0 |  |  |  |
| party_deposit_UGA | int | 4 | 0 |  |  |  |
| party_deposit_units | int | 4 | 0 |  |  |  |
| giftcard_uga | numeric | 17 | 1 |  |  |  |
| giftcard_units | int | 4 | 1 |  |  |  |
| animal_UGA | numeric | 17 | 1 |  |  |  |
| animal_units | int | 4 | 1 |  |  |  |
| non_animal_UGA | numeric | 17 | 1 |  |  |  |
| non_animal_units | int | 4 | 1 |  |  |  |
| footwear_UGA | numeric | 17 | 1 |  |  |  |
| footwear_units | int | 4 | 1 |  |  |  |
| accessories_UGA | numeric | 17 | 1 |  |  |  |
| accessories_units | int | 4 | 1 |  |  |  |
| sounds_UGA | numeric | 17 | 1 |  |  |  |
| sounds_units | int | 4 | 1 |  |  |  |
| clothing_UGA | numeric | 17 | 1 |  |  |  |
| clothing_units | int | 4 | 1 |  |  |  |
| other_UGA | numeric | 17 | 1 |  |  |  |
| other_units | int | 4 | 1 |  |  |  |
| shipping_UGA | int | 4 | 0 |  |  |  |
| shipping_units | int | 4 | 0 |  |  |  |
| other_fees_UGA | int | 4 | 0 |  |  |  |
| other_fees_units | int | 4 | 0 |  |  |  |
| cub_cash_UGA | int | 4 | 0 |  |  |  |
| cub_cash_units | int | 4 | 0 |  |  |  |
| paid_outs_UGA | int | 4 | 0 |  |  |  |
| paid_outs_units | int | 4 | 0 |  |  |  |
| stuffing_supplies_UGA | int | 4 | 0 |  |  |  |
| stuffing_supplies_units | int | 4 | 0 |  |  |  |
| sports_UGA | numeric | 17 | 1 |  |  |  |
| sports_units | int | 4 | 1 |  |  |  |
| prestuffed_UGA | numeric | 17 | 1 |  |  |  |
| prestuffed_units | int | 4 | 1 |  |  |  |
| fin_GAAP_sales_amount | money | 8 | 1 |  |  |  |
| upsell_discount_amount | money | 8 | 1 |  |  |  |
| cashier_key | int | 4 | 0 |  |  |  |
| merchandise_cost | numeric | 17 | 1 |  |  |  |
| animal_cost | numeric | 17 | 1 |  |  |  |
| non_animal_cost | numeric | 17 | 1 |  |  |  |
| footwear_cost | numeric | 17 | 1 |  |  |  |
| accessories_cost | numeric | 17 | 1 |  |  |  |
| sounds_cost | numeric | 17 | 1 |  |  |  |
| clothing_cost | numeric | 17 | 1 |  |  |  |
| other_cost | numeric | 17 | 1 |  |  |  |
| sports_cost | numeric | 17 | 1 |  |  |  |
| prestuffed_cost | numeric | 17 | 1 |  |  |  |
| Scents_UGA | numeric | 17 | 1 |  |  |  |
| Scents_units | int | 4 | 1 |  |  |  |
| Scents_cost | numeric | 17 | 1 |  |  |  |
| Store_transaction_flag | int | 4 | 0 |  |  |  |
| Store_Sales_Amount | numeric | 17 | 1 |  |  |  |
| Store_units | int | 4 | 1 |  |  |  |
| fin_Store_sales_amount | numeric | 17 | 1 |  |  |  |
