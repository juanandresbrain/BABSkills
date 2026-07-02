# dbo.merch_replication_queue

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merch_replication_queue_id | decimal | 9 | 0 |  |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| replication_action | nvarchar | 4 | 0 |  |  |  |
| action_date | datetime | 8 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| parent_code | nvarchar | 40 | 0 |  |  |  |
| replication_data | nvarchar | 300 | 1 |  |  |  |

