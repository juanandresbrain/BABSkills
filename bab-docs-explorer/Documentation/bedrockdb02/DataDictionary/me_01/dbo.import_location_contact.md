# dbo.import_location_contact

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_location_contact_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| contact_type | nchar | 2 | 0 |  |  |  |
| contact_description1 | nvarchar | 60 | 0 |  |  |  |
| contact_description2 | nvarchar | 60 | 1 |  |  |  |
| contact_number | nvarchar | 100 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |
| main_flag | nvarchar | 2 | 1 |  |  |  |

