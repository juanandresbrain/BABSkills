# dbo.CRMde4

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transactionID | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| event_name | varchar | 200 | 1 |  |  |  |
| category | varchar | 200 | 1 |  |  |  |
| unit_gross_amount | numeric | 17 | 1 |  |  |  |
| coupon_desc | varchar | 50 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| recID | int | 4 | 0 | YES |  |  |
| couponNumber | varchar | 200 | 1 |  |  |  |
| certificateNumber | varchar | 200 | 1 |  |  |  |
