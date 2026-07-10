# dbo.LaborCreditRejects

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DateSubmitted | varchar | 50 | 1 |  |  |  |
| StoreNumber | varchar | 50 | 1 |  |  |  |
| Month | varchar | 50 | 1 |  |  |  |
| WeekNumber | varchar | 50 | 1 |  |  |  |
| Credit | varchar | 50 | 1 |  |  |  |
| Reason | varchar | 1000 | 1 |  |  |  |
| RequestedBy | varchar | 1000 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime | 8 | 1 |  |  |  |
