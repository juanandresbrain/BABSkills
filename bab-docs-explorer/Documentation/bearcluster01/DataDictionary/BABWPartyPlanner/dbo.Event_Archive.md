# dbo.Event_Archive

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EventID | int | 4 | 0 |  |  |  |
| EventStart | datetime | 8 | 1 |  |  |  |
| EventEnd | datetime | 8 | 1 |  |  |  |
| EventType | int | 4 | 1 |  |  |  |
| CreatedDate | datetime | 8 | 1 |  |  |  |
| CreatedBy | varchar | 128 | 1 |  |  |  |
| LastUpdated | datetime | 8 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| Active | bit | 1 | 1 |  |  |  |

