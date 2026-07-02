# dbo.cum_val_ib_map

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cum_val_ib_map_id | decimal | 9 | 0 | YES |  |  |
| cum_val_type | tinyint | 1 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| operator | smallint | 2 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |

