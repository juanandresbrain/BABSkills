# esell.reporting_batch_history

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| REPORT_BATCH_ID | nvarchar | 200 | 1 |  |  |  |
| REPORT_BATCH_TYPE | nvarchar | 100 | 1 |  |  |  |
| REPORT_BATCH_START_TIME | datetime | 8 | 1 |  |  |  |
| REPORT_BATCH_END_TIME | datetime | 8 | 1 |  |  |  |
| REPORT_BATCH_STATUS | nvarchar | 40 | 1 |  |  |  |
| ROWINSERTED | int | 4 | 1 |  |  |  |

