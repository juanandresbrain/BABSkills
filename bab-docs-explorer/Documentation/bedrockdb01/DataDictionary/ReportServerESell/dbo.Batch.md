# dbo.Batch

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BatchID | uniqueidentifier | 16 | 0 |  |  |  |
| AddedOn | datetime | 8 | 0 |  |  |  |
| Action | varchar | 32 | 0 |  |  |  |
| Item | nvarchar | 850 | 1 |  |  |  |
| Parent | nvarchar | 850 | 1 |  |  |  |
| Param | nvarchar | 850 | 1 |  |  |  |
| BoolParam | bit | 1 | 1 |  |  |  |
| Content | image | 16 | 1 |  |  |  |
| Properties | ntext | 16 | 1 |  |  |  |
