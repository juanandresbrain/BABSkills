# dbo.StoreGroupBookingHour

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| GroupID | int | 4 | 0 | YES |  |  |
| DayOfWeek | int | 4 | 0 | YES |  |  |
| StartHour | time | 5 | 1 |  |  |  |
| EndHour | time | 5 | 1 |  |  |  |

