# dbo.oim_replication_queue

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_replication_queue_id | numeric | 9 | 0 | YES |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| replication_action | varchar | 2 | 0 |  |  |  |
| action_date | smalldatetime | 4 | 0 |  |  |  |
| entity_id | numeric | 9 | 0 |  |  |  |
| other_entity_id | numeric | 9 | 0 |  |  |  |
| other_entity_key | varchar | 20 | 0 |  |  |  |
| replication_data | varchar | 150 | 0 |  |  |  |
