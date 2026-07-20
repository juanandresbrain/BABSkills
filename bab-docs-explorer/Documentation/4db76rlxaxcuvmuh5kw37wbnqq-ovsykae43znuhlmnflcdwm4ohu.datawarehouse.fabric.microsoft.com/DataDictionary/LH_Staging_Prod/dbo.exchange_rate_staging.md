# dbo.exchange_rate_staging

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FR_CURR_CODE | varchar | 8000 | 1 |  |  |  |
| TO_CURR_CODE | varchar | 8000 | 1 |  |  |  |
| FR_CURR_KEY | int | 4 | 1 |  |  |  |
| TO_CURR_KEY | int | 4 | 1 |  |  |  |
| FISCAL_PERIOD | int | 4 | 1 |  |  |  |
| FISCAL_YEAR | int | 4 | 1 |  |  |  |
| RATE | decimal | 9 | 1 |  |  |  |
| Monthly_AVG | decimal | 9 | 1 |  |  |  |
| EndOfMonthRate | decimal | 9 | 1 |  |  |  |
| Actual_Date | date | 3 | 1 |  |  |  |
