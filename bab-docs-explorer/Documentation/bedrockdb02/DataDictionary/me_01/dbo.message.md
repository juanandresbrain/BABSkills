# dbo.message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| message_id | decimal | 9 | 0 | YES |  |  |
| message_type_id | decimal | 9 | 0 |  |  |  |
| message_code | nvarchar | 30 | 0 |  |  |  |
| message | nvarchar | 510 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

