# dbo.transaction_macys_fact

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TMF_KEY | int | 4 | 0 | YES |  |  |
| DATE_KEY | int | 4 | 1 |  |  |  |
| TIME_KEY | int | 4 | 1 |  |  |  |
| SELL_DIV | int | 4 | 1 |  |  |  |
| SELL_LOCATION | int | 4 | 1 |  |  |  |
| FILL_DIV | int | 4 | 1 |  |  |  |
| FILL_LOCATION | int | 4 | 1 |  |  |  |
| REGISTER | int | 4 | 1 |  |  |  |
| TRANS | int | 4 | 1 |  |  |  |
| TRANSTYPEID | int | 4 | 1 |  |  |  |
| SEQUENCE | int | 4 | 1 |  |  |  |
| RINGASSOCID | int | 4 | 1 |  |  |  |
| COMMASSOCID | int | 4 | 1 |  |  |  |
| TENDER1_TYPE | int | 4 | 1 |  |  |  |
| TENDER1_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER1_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER2_TYPE | int | 4 | 1 |  |  |  |
| TENDER2_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER2_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER3_TYPE | int | 4 | 1 |  |  |  |
| TENDER3_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER3_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER4_TYPE | int | 4 | 1 |  |  |  |
| TENDER4_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER4_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER5_TYPE | int | 4 | 1 |  |  |  |
| TENDER5_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER5_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER6_TYPE | int | 4 | 1 |  |  |  |
| TENDER6_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER6_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER7_TYPE | int | 4 | 1 |  |  |  |
| TENDER7_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER7_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER8_TYPE | int | 4 | 1 |  |  |  |
| TENDER8_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER8_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER9_TYPE | int | 4 | 1 |  |  |  |
| TENDER9_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER9_GIFTCARD | decimal | 9 | 1 |  |  |  |
| TENDER10_TYPE | int | 4 | 1 |  |  |  |
| TENDER10_AMOUNT | decimal | 9 | 1 |  |  |  |
| TENDER10_GIFTCARD | decimal | 9 | 1 |  |  |  |
| COUPON1_CODE | varchar | 20 | 1 |  |  |  |
| COUPON1_DISCOUNT | decimal | 9 | 1 |  |  |  |
| COUPON2_CODE | varchar | 20 | 1 |  |  |  |
| COUPON2_DISCOUNT | decimal | 9 | 1 |  |  |  |
| COUPON3_CODE | varchar | 20 | 1 |  |  |  |
| COUPON3_DISCOUNT | decimal | 9 | 1 |  |  |  |
| RESERVATION | decimal | 9 | 1 |  |  |  |
| LOYALTY | numeric | 5 | 1 |  |  |  |
| DEPT | int | 4 | 1 |  |  |  |
| CLASS | int | 4 | 1 |  |  |  |
| SKU | decimal | 9 | 1 |  |  |  |
| UNITS | int | 4 | 1 |  |  |  |
| PLUAMOUNT | decimal | 9 | 1 |  |  |  |
| SALEAMOUNT | decimal | 9 | 1 |  |  |  |
| DATE_KEY_ORIGDATE | int | 4 | 1 |  |  |  |
| ORIGLOCATION | int | 4 | 1 |  |  |  |
| ORIGREGISTER | int | 4 | 1 |  |  |  |
| ORIGTRANS | int | 4 | 1 |  |  |  |
| EMPLOYEE | int | 4 | 1 |  |  |  |
| AUDITED | bit | 1 | 0 |  |  |  |
