# dbo.imat_message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_message_id | decimal | 9 | 0 | YES |  |  |
| message_type_id | decimal | 9 | 0 |  |  |  |
| message_text | nvarchar | 510 | 1 |  |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| parent_type | smallint | 2 | 0 |  |  |  |

