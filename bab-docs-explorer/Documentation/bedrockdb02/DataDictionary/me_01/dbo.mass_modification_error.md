# dbo.mass_modification_error

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 | YES |  |  |
| mass_modification_error_id | smallint | 2 | 0 | YES |  |  |
| entity_id | decimal | 9 | 1 |  |  |  |
| error_text | nvarchar | 510 | 0 |  |  |  |

