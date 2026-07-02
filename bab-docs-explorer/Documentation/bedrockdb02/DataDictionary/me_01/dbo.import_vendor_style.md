# dbo.import_vendor_style

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_vendor_style_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |
| current_cost_currency_code | nvarchar | 6 | 1 |  |  |  |
| primary_vendor_flag | nchar | 2 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |

