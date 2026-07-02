# dbo.process_progress

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_progress_id | bigint | 8 | 0 | YES |  |  |
| process_type | smallint | 2 | 0 |  |  |  |
| number_items_to_process | int | 4 | 0 |  |  |  |
| number_items_processed | int | 4 | 0 |  |  |  |
| last_message | nvarchar | 512 | 0 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 1 |  |  |  |
| process_status | smallint | 2 | 0 |  |  |  |

