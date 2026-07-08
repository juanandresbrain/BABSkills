# dbo.tblPostingJobsFile

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PostingJobsFileID | numeric | 9 | 0 | YES |  |  |
| RemoteNumber | numeric | 9 | 0 |  |  |  |
| PostingJobID | int | 4 | 0 |  |  |  |
| FileSize | int | 4 | 0 |  |  |  |
| EventTime | datetime | 8 | 0 |  |  |  |
| Comments | varchar | 255 | 0 |  |  |  |
| Source | varchar | 255 | 0 |  |  |  |
| Destination | varchar | 255 | 0 |  |  |  |
| PostingJobsError | int | 4 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| ErrorDesc | varchar | 255 | 0 |  |  |  |
