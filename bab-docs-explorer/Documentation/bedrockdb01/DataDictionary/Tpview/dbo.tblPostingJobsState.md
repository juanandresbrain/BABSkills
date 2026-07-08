# dbo.tblPostingJobsState

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PostingJobsStateID | numeric | 9 | 0 | YES |  |  |
| PostingJobID | int | 4 | 0 |  |  |  |
| EventTime | datetime | 8 | 0 |  |  |  |
| Comments | varchar | 255 | 0 |  |  |  |
| PostingJobsError | int | 4 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| ErrorDesc | varchar | 255 | 0 |  |  |  |
