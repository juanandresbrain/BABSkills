# dbo.process_error_log

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_error_log_id | bigint | 8 | 0 | YES |  |  |
| process_type | smallint | 2 | 0 |  |  |  |
| log_date_time | smalldatetime | 4 | 0 |  |  |  |
| area | nvarchar | 200 | 1 |  |  |  |
| entity | nvarchar | 400 | 1 |  |  |  |
| description | nvarchar | 4000 | 1 |  |  |  |

