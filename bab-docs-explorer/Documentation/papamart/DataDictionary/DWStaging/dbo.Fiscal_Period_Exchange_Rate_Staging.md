# dbo.Fiscal_Period_Exchange_Rate_Staging

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FR_CURR_CODE | char | 5 | 0 |  |  |  |
| TO_CURR_CODE | char | 5 | 0 |  |  |  |
| FR_CURR_KEY | int | 4 | 1 |  |  |  |
| TO_CURR_KEY | int | 4 | 1 |  |  |  |
| FISCAL_PERIOD | int | 4 | 0 |  |  |  |
| FISCAL_YEAR | smallint | 2 | 0 |  |  |  |
| RATE | decimal | 9 | 0 |  |  |  |
| TRANSL_CODE | char | 2 | 0 |  |  |  |
