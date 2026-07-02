# dbo.ticket_format_data

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ticket_format_id | smallint | 2 | 0 | YES |  |  |
| ticket_format_code | nvarchar | 4 | 0 |  |  |  |
| ticket_format_description | nvarchar | 80 | 0 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 1 |  |  |  |
| format_type | nvarchar | 60 | 0 |  |  |  |
| format_text1 | nvarchar | 510 | 0 |  |  |  |
| format_text2 | nvarchar | 510 | 1 |  |  |  |
| format_text3 | nvarchar | 510 | 1 |  |  |  |
| format_text4 | nvarchar | 510 | 1 |  |  |  |
| format_text5 | nvarchar | 510 | 1 |  |  |  |
| format_text6 | nvarchar | 510 | 1 |  |  |  |
| format_text7 | nvarchar | 510 | 1 |  |  |  |
| format_text8 | nvarchar | 510 | 1 |  |  |  |
| no_of_parts | nvarchar | 2 | 0 |  |  |  |
| header_format_id | decimal | 5 | 1 |  |  |  |
| header_position_flag | nchar | 2 | 0 |  |  |  |
| ticket_type | nvarchar | 12 | 1 |  |  |  |

