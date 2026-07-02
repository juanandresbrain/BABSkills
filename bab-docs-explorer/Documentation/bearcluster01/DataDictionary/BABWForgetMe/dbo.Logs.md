# dbo.Logs

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogID | int | 4 | 0 | YES |  |  |
| Message | nvarchar | -1 | 0 |  |  |  |
| Type | nvarchar | 100 | 1 |  |  |  |
| Location | nvarchar | 100 | 1 |  |  |  |
| Stack | nvarchar | -1 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |

