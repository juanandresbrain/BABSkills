# dbo.import_style_cust_prop

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_style_cust_prop_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| custom_property_code | nvarchar | 12 | 0 |  |  |  |
| custom_property_value | nvarchar | 60 | 0 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |

