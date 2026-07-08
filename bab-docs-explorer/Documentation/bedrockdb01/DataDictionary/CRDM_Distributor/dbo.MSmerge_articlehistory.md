# dbo.MSmerge_articlehistory

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| session_id | int | 4 | 0 |  |  |  |
| phase_id | int | 4 | 1 |  |  |  |
| article_name | sysname | 256 | 1 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| duration | int | 4 | 1 |  |  |  |
| inserts | int | 4 | 0 |  |  |  |
| updates | int | 4 | 0 |  |  |  |
| deletes | int | 4 | 0 |  |  |  |
| conflicts | int | 4 | 0 |  |  |  |
| rows_retried | int | 4 | 0 |  |  |  |
| percent_complete | decimal | 5 | 0 |  |  |  |
| estimated_changes | int | 4 | 1 |  |  |  |
| relative_cost | decimal | 9 | 0 |  |  |  |
