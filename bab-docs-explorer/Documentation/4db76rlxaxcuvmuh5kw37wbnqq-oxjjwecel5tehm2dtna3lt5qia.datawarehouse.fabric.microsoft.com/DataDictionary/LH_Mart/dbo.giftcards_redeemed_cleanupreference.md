# dbo.giftcards_redeemed_cleanupreference

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| actual_date | datetime2 | 8 | 1 |  |  |  |
| recID | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| redemption_amount | decimal | 9 | 1 |  |  |  |
| discount_amount | decimal | 9 | 1 |  |  |  |
| giftcard_no | varchar | 8000 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| MID | varchar | 8000 | 1 |  |  |  |
| daysSinceLastActivation | int | 4 | 1 |  |  |  |
| lift_amount | decimal | 9 | 1 |  |  |  |
| activation_discount_amount | decimal | 9 | 1 |  |  |  |
| source | varchar | 8000 | 1 |  |  |  |
| VLVerified | bit | 1 | 1 |  |  |  |
| VLA9520_DiscAmount | decimal | 9 | 1 |  |  |  |
| OriginalActivationDiscountAmount | decimal | 9 | 1 |  |  |  |
| RemainingActivationDiscountAmount | decimal | 9 | 1 |  |  |  |
| ActionType | varchar | 8000 | 1 |  |  |  |
| Ranking | bigint | 8 | 1 |  |  |  |
| activation_discount_amount_to_be_applied | decimal | 9 | 1 |  |  |  |
