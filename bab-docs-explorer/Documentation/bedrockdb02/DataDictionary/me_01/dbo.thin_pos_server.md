# dbo.thin_pos_server

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| thin_pos_server_id | smallint | 2 | 0 | YES |  |  |
| pos_server_code | nvarchar | 20 | 0 |  |  |  |
| pos_server_name | nvarchar | 100 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| register_type_id | tinyint | 1 | 0 |  |  |  |
| polling_reference | int | 4 | 0 |  |  |  |
| es_flag | bit | 1 | 0 |  |  |  |
| currency_id | decimal | 9 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

