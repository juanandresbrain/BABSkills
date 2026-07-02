# dbo.StoreBookingHour

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RowIndex | bigint | 8 | 0 | YES |  |  |
| StoreID | int | 4 | 0 | YES |  |  |
| DayOfWeek | int | 4 | 0 | YES |  |  |
| StartHour | time | 5 | 0 | YES |  |  |
| EndHour | time | 5 | 1 |  |  |  |

