# dbo.ma_price_status

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_status_id | int | 4 | 1 |  |  |  |
| price_status_code | varchar | 8000 | 1 |  |  |  |
| price_status_desc | varchar | 8000 | 1 |  |  |  |
| alloc_replen_price_point | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
