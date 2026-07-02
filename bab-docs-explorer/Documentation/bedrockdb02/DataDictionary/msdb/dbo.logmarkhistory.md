# dbo.logmarkhistory

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| database_name | nvarchar | 256 | 0 |  |  |  |
| mark_name | nvarchar | 256 | 0 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| user_name | nvarchar | 256 | 0 |  |  |  |
| lsn | numeric | 13 | 0 |  |  |  |
| mark_time | datetime | 8 | 0 |  |  |  |

