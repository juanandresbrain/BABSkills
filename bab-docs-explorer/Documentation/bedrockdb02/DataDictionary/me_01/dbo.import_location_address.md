# dbo.import_location_address

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_location_address_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| address_type | nvarchar | 40 | 0 |  |  |  |
| address_name | nvarchar | 120 | 1 |  |  |  |
| address_line1 | nvarchar | 100 | 0 |  |  |  |
| address_line2 | nvarchar | 100 | 1 |  |  |  |
| address_city | nvarchar | 40 | 1 |  |  |  |
| address_state | nvarchar | 40 | 1 |  |  |  |
| country_code | nvarchar | 6 | 0 |  |  |  |
| address_zip_code | nvarchar | 30 | 1 |  |  |  |
| address_email | nvarchar | 120 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |

