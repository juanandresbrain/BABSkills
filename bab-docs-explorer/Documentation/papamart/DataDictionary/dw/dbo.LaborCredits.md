# dbo.LaborCredits

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DateSubmitted | date | 3 | 1 |  |  |  |
| StoreNumber | int | 4 | 1 |  |  |  |
| Month | varchar | 50 | 1 |  |  |  |
| WeekNumber | int | 4 | 1 |  |  |  |
| Credit | decimal | 17 | 1 |  |  |  |
| Reason | varchar | 1000 | 1 |  |  |  |
| RequestedBy | varchar | 1000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
