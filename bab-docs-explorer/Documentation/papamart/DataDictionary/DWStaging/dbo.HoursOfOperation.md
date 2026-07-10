# dbo.HoursOfOperation

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Country | varchar | 2 | 1 |  |  |  |
| STR_NUM | int | 4 | 1 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| yearWeek | varchar | 6 | 1 |  |  |  |
| strt_tm | datetime | 8 | 1 |  |  |  |
| end_tm | datetime | 8 | 1 |  |  |  |
| hoursSched | numeric | 9 | 1 |  |  |  |
| isOverriden | int | 4 | 1 |  |  |  |
| hoursNormalSched | numeric | 9 | 1 |  |  |  |
| BearitoryName | varchar | 52 | 1 |  |  |  |
| NM_ABBRV | varchar | 52 | 1 |  |  |  |
