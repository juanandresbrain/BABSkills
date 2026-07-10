# dbo.tmpPreviousFiscalWeekSold

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| fiscal_week | nvarchar | 60 | 1 |  |  |  |
| PreviousWeekSold | int | 4 | 1 |  |  |  |
