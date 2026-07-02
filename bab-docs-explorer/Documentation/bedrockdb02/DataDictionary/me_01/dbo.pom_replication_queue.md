# dbo.pom_replication_queue

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pom_replication_queue_id | decimal | 9 | 0 | YES |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| replication_action | nvarchar | 4 | 0 |  |  |  |
| action_date | smalldatetime | 4 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| other_entity_id | decimal | 9 | 1 |  |  |  |
| other_entity_key | nvarchar | 60 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| changed_units | int | 4 | 1 |  |  |  |
| replication_data | nvarchar | 210 | 0 |  |  |  |

