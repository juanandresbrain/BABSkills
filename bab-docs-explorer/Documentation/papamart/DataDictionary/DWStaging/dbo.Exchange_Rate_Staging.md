# dbo.Exchange_Rate_Staging

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FR_CURR_CODE | char | 5 | 0 |  |  |  |
| TO_CURR_CODE | char | 5 | 0 |  |  |  |
| FR_CURR_KEY | int | 4 | 1 |  |  |  |
| TO_CURR_KEY | int | 4 | 1 |  |  |  |
| FISCAL_PERIOD | int | 4 | 1 |  |  |  |
| FISCAL_YEAR | int | 4 | 1 |  |  |  |
| RATE | decimal | 9 | 1 |  |  |  |
| Monthly_AVG | decimal | 9 | 1 |  |  |  |
| EndOfMonthRate | decimal | 9 | 1 |  |  |  |
| Actual_Date | date | 3 | 1 |  |  |  |
