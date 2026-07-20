# dbo.coupon_dim_changes_toapply

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| coupon_key | int | 4 | 1 |  |  |  |
| coupon_desc | varchar | 8000 | 1 |  |  |  |
| start_date | datetime2 | 8 | 1 |  |  |  |
| stop_date | datetime2 | 8 | 1 |  |  |  |
| qty_distributed | int | 4 | 1 |  |  |  |
| event_name | varchar | 8000 | 1 |  |  |  |
| category | varchar | 8000 | 1 |  |  |  |
| updt_dt | datetime2 | 8 | 1 |  |  |  |
| dmDiscountID | int | 4 | 1 |  |  |  |
| categoryTypeID | int | 4 | 1 |  |  |  |
