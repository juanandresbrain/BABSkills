# dbo.aw_Load_Statistics

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Interval Start | datetime | 8 | 1 |  |  |  |
| Interval End | datetime | 8 | 1 |  |  |  |
| Input - ED Rows Received | int | 4 | 1 |  |  |  |
| Input - SM Rows Received | int | 4 | 1 |  |  |  |
| Input - SS Rows Received | int | 4 | 1 |  |  |  |
| Cache - ED Rows | int | 4 | 1 |  |  |  |
| Cache - SM Rows | int | 4 | 1 |  |  |  |
| Cache - SS Rows | int | 4 | 1 |  |  |  |
| Output - Unchanged Rows Sent | int | 4 | 1 |  |  |  |
| Output - New Rows Sent | int | 4 | 1 |  |  |  |
| Output - Deleted Rows Sent | int | 4 | 1 |  |  |  |
| Output - Updated SCD1 Rows Sent | int | 4 | 1 |  |  |  |
| Output - Expired SCD2 Rows Sent | int | 4 | 1 |  |  |  |
| Output - New SCD2 Rows Sent | int | 4 | 1 |  |  |  |
| Match Prep - Work Units Built | int | 4 | 1 |  |  |  |
| Match Prep - Rows Built Into Work Units | int | 4 | 1 |  |  |  |
| Match Prep - Bulk Matched Rows | int | 4 | 1 |  |  |  |
| Match Prep - Work Unit Count | int | 4 | 1 |  |  |  |
| Matching - Matched Key Queue Length | int | 4 | 1 |  |  |  |
| Matching - Skipped Rows | int | 4 | 1 |  |  |  |
| Matching - Regular Determination | int | 4 | 1 |  |  |  |
| Matching - Sort Optimization Determination | int | 4 | 1 |  |  |  |
| Matching - Undetermined | int | 4 | 1 |  |  |  |
| Thread Delay - Waiting For Input | int | 4 | 1 |  |  |  |
| Thread Delay - Matching Waiting On Caching | int | 4 | 1 |  |  |  |
| Thread Delay - Processing Waiting On Matching | int | 4 | 1 |  |  |  |
| Thread Delay - Input Waiting On Row Processing | int | 4 | 1 |  |  |  |
