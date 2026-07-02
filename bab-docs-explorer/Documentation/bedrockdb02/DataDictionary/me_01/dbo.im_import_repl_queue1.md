# dbo.im_import_repl_queue1

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| im_import_repl_queue_id | decimal | 9 | 0 | YES |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| replication_action | nvarchar | 4 | 0 |  |  |  |
| action_date | smalldatetime | 4 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| other_entity_id | decimal | 9 | 0 |  |  |  |
| other_entity_key | nvarchar | 40 | 0 |  |  |  |

