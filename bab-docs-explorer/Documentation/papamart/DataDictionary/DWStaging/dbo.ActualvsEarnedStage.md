# dbo.ActualvsEarnedStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StartDate | date | 3 | 1 |  |  |  |
| EndDate | date | 3 | 1 |  |  |  |
| Year | int | 4 | 1 |  |  |  |
| Week | int | 4 | 1 |  |  |  |
| WeekID | int | 4 | 1 |  |  |  |
| PeriodID | int | 4 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| ActualHours | numeric | 17 | 1 |  |  |  |
| EarnedHours | numeric | 17 | 1 |  |  |  |
| Variance | numeric | 17 | 1 |  |  |  |
| PercentOfActual | numeric | 17 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| AdjustedSales | numeric | 17 | 1 |  |  |  |
| AdjustedSalesRounded | numeric | 17 | 1 |  |  |  |
| BaseHours | int | 4 | 1 |  |  |  |
