# dbo.missing_exchange_rate_staging

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FR_CURR_CODE | varchar | 8000 | 1 |  |  |  |
| TO_CURR_CODE | varchar | 8000 | 1 |  |  |  |
| FR_CURR_KEY | int | 4 | 1 |  |  |  |
| TO_CURR_KEY | int | 4 | 1 |  |  |  |
| BBW_RATE | decimal | 9 | 1 |  |  |  |
| MONTH_AVG_RATE | decimal | 9 | 1 |  |  |  |
| MONTH_END_RATE | decimal | 9 | 1 |  |  |  |
| DATE | datetime2 | 8 | 1 |  |  |  |
| EMAILED | bit | 1 | 1 |  |  |  |
