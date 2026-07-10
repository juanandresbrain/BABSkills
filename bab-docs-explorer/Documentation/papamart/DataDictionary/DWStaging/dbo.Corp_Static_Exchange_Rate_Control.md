# dbo.Corp_Static_Exchange_Rate_Control

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FR_CURR_CODE | char | 5 | 0 |  |  |  |
| TO_CURR_CODE | char | 5 | 0 |  |  |  |
| FR_CURR_KEY | int | 4 | 1 |  |  |  |
| TO_CURR_KEY | int | 4 | 1 |  |  |  |
| RATE | decimal | 9 | 0 |  |  |  |
