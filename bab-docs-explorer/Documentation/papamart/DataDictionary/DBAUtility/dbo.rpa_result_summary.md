# dbo.rpa_result_summary

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| seqno | int | 4 | 0 | YES |  |  |
| groupno | int | 4 | 1 |  |  |  |
| group_desc | varchar | 50 | 1 |  |  |  |
| category | varchar | 100 | 1 |  |  |  |
| bear | int | 4 | 1 |  |  |  |
| nonbear | int | 4 | 1 |  |  |  |
| total | int | 4 | 1 |  |  |  |
| comment | varchar | 200 | 1 |  |  |  |
| unique_y_n | char | 1 | 1 |  |  |  |
| process_date | datetime | 8 | 1 |  |  |  |
