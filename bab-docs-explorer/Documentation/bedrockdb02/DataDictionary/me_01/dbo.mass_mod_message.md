# dbo.mass_mod_message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 | YES |  |  |
| mass_mod_message_id | smallint | 2 | 0 | YES |  |  |
| message_type_id | decimal | 9 | 0 |  | YES |  |
| message | nvarchar | 510 | 1 |  |  |  |
| action | smallint | 2 | 0 |  |  |  |

