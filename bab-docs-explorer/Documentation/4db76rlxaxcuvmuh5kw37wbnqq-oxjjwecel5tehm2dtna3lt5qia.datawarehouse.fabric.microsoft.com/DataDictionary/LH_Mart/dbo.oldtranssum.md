# dbo.oldtranssum

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transkey | varchar | 8000 | 1 |  |  |  |
| transaction_summary_key | int | 4 | 1 |  |  |  |
| process_name | varchar | 8000 | 1 |  |  |  |
| process_date | datetime2 | 8 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| trans_no | int | 4 | 1 |  |  |  |
| Gift_Card_Tender | decimal | 5 | 1 |  |  |  |
| Tax_Tender | decimal | 5 | 1 |  |  |  |
| Cash_Tender | decimal | 5 | 1 |  |  |  |
| Check_Tender | decimal | 5 | 1 |  |  |  |
| BuyStuff_Tender | decimal | 5 | 1 |  |  |  |
| Other_Tender | decimal | 5 | 1 |  |  |  |
| Amex_Tender | decimal | 5 | 1 |  |  |  |
| Discover_Tender | decimal | 5 | 1 |  |  |  |
| MasterCard_Tender | decimal | 5 | 1 |  |  |  |
| Visa_Tender | decimal | 5 | 1 |  |  |  |
| Bear_Buck_Tender | decimal | 5 | 1 |  |  |  |
| Party_Deposit_Tender | decimal | 5 | 1 |  |  |  |
| Reward_Cert_Tender | decimal | 5 | 1 |  |  |  |
| Party_Deposit_Merch | decimal | 5 | 1 |  |  |  |
| Discounts | decimal | 5 | 1 |  |  |  |
| GiftCardDiscounts | decimal | 5 | 1 |  |  |  |
| Gift_Card_Sold | decimal | 5 | 1 |  |  |  |
| Coupon_Amt | decimal | 5 | 1 |  |  |  |
| Coupon_Units | decimal | 5 | 1 |  |  |  |
| Units | decimal | 5 | 1 |  |  |  |
| UGA | decimal | 5 | 1 |  |  |  |
| Merchandise_UGA | decimal | 5 | 1 |  |  |  |
| Donations | decimal | 5 | 1 |  |  |  |
| StuffingAndSupplies | decimal | 5 | 1 |  |  |  |
| Cub_Cash | decimal | 5 | 1 |  |  |  |
| Paid_Outs | decimal | 5 | 1 |  |  |  |
| Shipping | decimal | 5 | 1 |  |  |  |
| Other_Fee | decimal | 5 | 1 |  |  |  |
| GAAP_Sale | decimal | 5 | 1 |  |  |  |
| Net_Sale | decimal | 5 | 1 |  |  |  |
| Receipt_Ttl | decimal | 5 | 1 |  |  |  |
| donation_only | bit | 1 | 1 |  |  |  |
| gift_card_only | bit | 1 | 1 |  |  |  |
| party_dep_only | bit | 1 | 1 |  |  |  |
| party_y_n | varchar | 8000 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
