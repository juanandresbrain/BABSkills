# dbo.Comment_Archive

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CommentID | int | 4 | 0 |  |  |  |
| EventID | int | 4 | 1 |  |  |  |
| CreatedDate | datetime | 8 | 1 |  |  |  |
| Comment | varchar | 512 | 1 |  |  |  |
| CreatedBy | varchar | 128 | 1 |  |  |  |
| LastUpdated | datetime | 8 | 1 |  |  |  |

