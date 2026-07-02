# dbo.zz_crq_bk

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| core_replication_queue_id | decimal | 9 | 0 |  |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| replication_action | varchar | 2 | 0 |  |  |  |
| action_date | smalldatetime | 4 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| other_entity_id | decimal | 9 | 1 |  |  |  |
| primary_entity_key | varchar | 20 | 1 |  |  |  |
| secondary_entity_key | varchar | 20 | 1 |  |  |  |
| replication_data | varchar | 105 | 0 |  |  |  |

