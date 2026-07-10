# dbo.CRMTranFact6MStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| MonthRange | varchar | 15 | 1 |  |  |  |
| TransactionCount | int | 4 | 1 |  |  |  |
| RecencyCount | int | 4 | 1 |  |  |  |
| SalesTotal | numeric | 17 | 1 |  |  |  |
| minDaysBetween | int | 4 | 1 |  |  |  |
| maxDaysBetween | int | 4 | 1 |  |  |  |
| DaysBetween | int | 4 | 1 |  |  |  |
