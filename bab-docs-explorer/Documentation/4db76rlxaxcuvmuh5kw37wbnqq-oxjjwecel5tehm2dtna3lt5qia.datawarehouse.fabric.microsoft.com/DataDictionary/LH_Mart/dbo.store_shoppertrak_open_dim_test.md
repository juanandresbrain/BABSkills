# dbo.store_shoppertrak_open_dim_test

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key_from | int | 4 | 1 |  |  |  |
| date_key_thru | int | 4 | 1 |  |  |  |
| hour_day_start | int | 4 | 1 |  |  |  |
| hour_day_end | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
