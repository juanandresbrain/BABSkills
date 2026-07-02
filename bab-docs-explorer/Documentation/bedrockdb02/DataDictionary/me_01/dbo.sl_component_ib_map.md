# dbo.sl_component_ib_map

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sl_component_ib_map_id | decimal | 9 | 0 | YES |  |  |
| sl_component_id | decimal | 9 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 1 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| ib_value_type | tinyint | 1 | 0 |  |  |  |
| operator | smallint | 2 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)

