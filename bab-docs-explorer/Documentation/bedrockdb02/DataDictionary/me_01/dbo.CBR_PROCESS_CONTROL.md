# dbo.CBR_PROCESS_CONTROL

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | nvarchar | 40 | 0 |  |  |  |
| computer_name | nvarchar | 40 | 0 |  |  |  |
| file_location | nvarchar | 200 | 0 |  |  |  |
| user_name | nvarchar | 40 | 0 |  |  |  |
| batch_pull | nvarchar | 100 | 0 |  |  |  |
| status | nvarchar | 2 | 0 |  |  |  |
| description | nvarchar | 200 | 1 |  |  |  |
| last_update_time | datetime | 8 | 1 |  |  |  |

