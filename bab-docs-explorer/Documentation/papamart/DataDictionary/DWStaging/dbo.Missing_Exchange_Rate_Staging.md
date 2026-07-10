# dbo.Missing_Exchange_Rate_Staging

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FR_CURR_CODE | char | 3 | 0 |  |  |  |
| TO_CURR_CODE | char | 3 | 0 |  |  |  |
| FR_CURR_KEY | int | 4 | 0 |  |  |  |
| TO_CURR_KEY | int | 4 | 0 |  |  |  |
| BBW_RATE | decimal | 9 | 0 |  |  |  |
| MONTH_AVG_RATE | decimal | 9 | 0 |  |  |  |
| MONTH_END_RATE | decimal | 9 | 0 |  |  |  |
| DATE | datetime | 8 | 0 |  |  |  |
| EMAILED | bit | 1 | 0 |  |  |  |
