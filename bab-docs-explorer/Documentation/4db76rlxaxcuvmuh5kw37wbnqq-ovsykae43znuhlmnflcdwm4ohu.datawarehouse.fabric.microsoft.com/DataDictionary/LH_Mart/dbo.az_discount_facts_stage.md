# dbo.az_discount_facts_stage

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Transaction_ID | varchar | 1280 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| Line_Sequence | varchar | 8000 | 1 |  |  |  |
| LineNum | varchar | 8000 | 1 |  |  |  |
| Cashier_No | varchar | 1280 | 1 |  |  |  |
| Gross_Line_Amount | decimal | 9 | 1 |  |  |  |
| Line_Object_Key | int | 4 | 1 |  |  |  |
| Reference_No | varchar | 1280 | 1 |  |  |  |
| Transaction_No | varchar | 1280 | 1 |  |  |  |
| Units | decimal | 9 | 1 |  |  |  |
| Coupon_Flag | int | 4 | 1 |  |  |  |
| coupon_key | int | 4 | 1 |  |  |  |
| origReference_no | varchar | 1280 | 1 |  |  |  |
| categoryTypeID | varchar | 1280 | 1 |  |  |  |
| isExpired | int | 4 | 1 |  |  |  |
| Lift_Amount | decimal | 9 | 1 |  |  |  |
| Store_No | int | 4 | 1 |  |  |  |
