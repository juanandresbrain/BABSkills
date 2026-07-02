# dbo.w4_export_queue

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| export_queue_id | numeric | 9 | 0 |  |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| action_code | char | 2 | 0 |  |  |  |
| action_date | smalldatetime | 4 | 0 |  |  |  |
| entity_id | numeric | 9 | 0 |  |  |  |
| other_entity_id | numeric | 9 | 1 |  |  |  |
| other_entity_id2 | varchar | 30 | 1 |  |  |  |

