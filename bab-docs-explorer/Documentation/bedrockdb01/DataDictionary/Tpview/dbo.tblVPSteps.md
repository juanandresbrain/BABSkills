# dbo.tblVPSteps

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| VPID | int | 4 | 0 |  |  |  |
| StepID | int | 4 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| QueueID | numeric | 9 | 1 |  |  |  |
| PostingJobID | int | 4 | 1 |  |  |  |
| StepType | varchar | 2 | 0 |  |  |  |
