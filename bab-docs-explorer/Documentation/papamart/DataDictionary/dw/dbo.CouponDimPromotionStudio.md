# dbo.CouponDimPromotionStudio

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| coupon_key | int | 4 | 0 | YES |  |  |
| Retail_Pro | varchar | 128 | 1 |  |  |  |
| coupon_desc | varchar | 128 | 1 |  |  |  |
| start_date | datetime | 8 | 1 |  |  |  |
| stop_date | datetime | 8 | 1 |  |  |  |
| qty_distributed | int | 4 | 1 |  |  |  |
| event_id | int | 4 | 1 |  |  |  |
| event_name | varchar | 200 | 1 |  |  |  |
| category_id | int | 4 | 1 |  |  |  |
| category | varchar | 200 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  |  |
| UPDT_DT | datetime | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| dmDiscountID | int | 4 | 1 |  |  |  |
| categoryTypeID | varchar | 100 | 1 |  |  |  |
