# dbo.StoreBookingHour_DEL_After_20220430

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RowIndex | bigint | 8 | 0 |  |  |  |
| StoreID | int | 4 | 0 |  |  |  |
| DayOfWeek | int | 4 | 0 |  |  |  |
| StartHour | time | 5 | 0 |  |  |  |
| EndHour | time | 5 | 1 |  |  |  |

