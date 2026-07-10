# dbo.work_tmptransrollup

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| party_y_n | char | 2 | 1 |  |  |  |
| transaction_type | varchar | 20 | 1 |  |  |  |
| Merchandise_UGA | decimal | 5 | 1 |  |  |  |
| Coupon_Amt | decimal | 5 | 1 |  |  |  |
| Coupon_Units | decimal | 5 | 1 |  |  |  |
| Discounts | decimal | 5 | 1 |  |  |  |
| Gift_Card_Sold | decimal | 5 | 1 |  |  |  |
| Bear_Buck_Tender | decimal | 5 | 1 |  |  |  |
| Gift_Card_Tender | decimal | 5 | 1 |  |  |  |
| Tax_Tender | decimal | 5 | 1 |  |  |  |
| Cash_Tender | decimal | 5 | 1 |  |  |  |
| Check_Tender | decimal | 5 | 1 |  |  |  |
| Other_Tender | decimal | 5 | 1 |  |  |  |
| Amex_Tender | decimal | 5 | 1 |  |  |  |
| Discover_Tender | decimal | 5 | 1 |  |  |  |
| MasterCard_Tender | decimal | 5 | 1 |  |  |  |
| Visa_Tender | decimal | 5 | 1 |  |  |  |
| BuyStuff_Tender | decimal | 5 | 1 |  |  |  |
| Reward_Cert_Tender | decimal | 5 | 1 |  |  |  |
| Shipping | decimal | 5 | 1 |  |  |  |
| Other_Fee | decimal | 5 | 1 |  |  |  |
| Donations | decimal | 5 | 1 |  |  |  |
| Cub_Cash | decimal | 5 | 1 |  |  |  |
| GiftCardDiscounts | decimal | 5 | 1 |  |  |  |
| Party_Deposit_Merch | decimal | 5 | 1 |  |  |  |
| StuffingAndSupplies | decimal | 5 | 1 |  |  |  |
| Units | decimal | 5 | 1 |  |  |  |
| Donation_Only | bit | 1 | 1 |  |  |  |
| Gift_Card_Only | bit | 1 | 1 |  |  |  |
| Party_Dep_Only | bit | 1 | 1 |  |  |  |
| Paid_Outs | decimal | 5 | 1 |  |  |  |
| Net_Sale | decimal | 5 | 1 |  |  |  |
| GAAP_Sale | decimal | 5 | 1 |  |  |  |
| Receipt_Ttl | decimal | 5 | 1 |  |  |  |
| ttlHoney | decimal | 9 | 1 |  |  |  |
