# dbo.coupondimpromotionstudio

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| coupon_key | int | 4 | 1 |  |  |  |
| Retail_Pro | varchar | 8000 | 1 |  |  |  |
| coupon_desc | varchar | 8000 | 1 |  |  |  |
| start_date | datetime2 | 8 | 1 |  |  |  |
| stop_date | datetime2 | 8 | 1 |  |  |  |
| qty_distributed | int | 4 | 1 |  |  |  |
| event_id | int | 4 | 1 |  |  |  |
| event_name | varchar | 8000 | 1 |  |  |  |
| category_id | int | 4 | 1 |  |  |  |
| category | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| dmDiscountID | int | 4 | 1 |  |  |  |
| categoryTypeID | varchar | 8000 | 1 |  |  |  |
