# dbo.corp_static_exchange_rate_control

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FR_CURR_CODE | varchar | 8000 | 1 |  |  |  |
| TO_CURR_CODE | varchar | 8000 | 1 |  |  |  |
| FR_CURR_KEY | int | 4 | 1 |  |  |  |
| TO_CURR_KEY | int | 4 | 1 |  |  |  |
| RATE | decimal | 9 | 1 |  |  |  |
