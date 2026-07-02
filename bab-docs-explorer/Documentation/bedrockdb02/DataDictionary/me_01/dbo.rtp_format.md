# dbo.rtp_format

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rtp_format_id | smallint | 2 | 0 | YES |  |  |
| format_code | nvarchar | 30 | 0 |  |  |  |
| format_name | nvarchar | 120 | 0 |  |  |  |
| format_description | nvarchar | 510 | 0 |  |  |  |
| format_physical_name | nvarchar | 510 | 0 |  |  |  |
| format_type | nvarchar | 12 | 1 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 0 |  |  |  |

