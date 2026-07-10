# dbo.coupon_dim_changes_toApply

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| coupon_key | int | 4 | 0 |  |  |  |
| coupon_desc | varchar | 50 | 0 |  |  |  |
| start_date | datetime | 8 | 1 |  |  |  |
| stop_date | datetime | 8 | 1 |  |  |  |
| qty_distributed | int | 4 | 1 |  |  |  |
| event_name | varchar | 200 | 1 |  |  |  |
| category | varchar | 200 | 1 |  |  |  |
| updt_dt | datetime | 8 | 1 |  |  |  |
| dmDiscountID | int | 4 | 0 |  |  |  |
| categoryTypeID | int | 4 | 0 |  |  |  |
