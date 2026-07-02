# dbo.plu_tps_4676

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| thin_pos_server_id | smallint | 2 | 0 | YES |  |  |
| pos_server_code | nvarchar | 20 | 1 |  |  |  |
| pos_server_name | nvarchar | 100 | 1 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| register_type_id | tinyint | 1 | 0 |  |  |  |
| polling_reference | int | 4 | 0 |  |  |  |
| es_flag | bit | 1 | 0 |  |  |  |
| full_regenerate_flag | bit | 1 | 1 |  |  |  |
| valid_flag | bit | 1 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
| tax_by_size_flag | bit | 1 | 1 |  |  |  |
| override_plu_key_to_sku | bit | 1 | 1 |  |  |  |

