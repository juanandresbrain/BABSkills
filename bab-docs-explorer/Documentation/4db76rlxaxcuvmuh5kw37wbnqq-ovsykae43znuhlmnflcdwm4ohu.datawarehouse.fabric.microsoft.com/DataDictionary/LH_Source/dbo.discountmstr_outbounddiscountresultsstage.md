# dbo.discountmstr_outbounddiscountresultsstage

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| dmDiscountID | int | 4 | 1 |  |  |  |
| categoryTypeID | int | 4 | 1 |  |  |  |
| isExpired | bit | 1 | 1 |  |  |  |
| country | varchar | 8000 | 1 |  |  |  |
| numRedeemed | int | 4 | 1 |  |  |  |
| redeemedAmt | decimal | 9 | 1 |  |  |  |
| GAAP_Transactions | int | 4 | 1 |  |  |  |
| GAAP_Sales_Amount | decimal | 9 | 1 |  |  |  |
| countryID | int | 4 | 1 |  |  |  |
| ResultTypeID | int | 4 | 1 |  |  |  |
