# dbo.housekeeping_queue

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| housekeeping_queue_id | decimal | 9 | 0 | YES |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| housekeeping_action_id | smallint | 2 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| from_entity_id | decimal | 9 | 1 |  |  |  |
| to_entity_id | decimal | 9 | 1 |  |  |  |

