# dbo.lyn_cum_val_history_post

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merch_hierarchy_group_id | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| calendar_period_id | decimal | 9 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| inventory_status_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_retail | decimal | 9 | 0 |  |  |  |
| transaction_units | decimal | 9 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |
| transaction_retail_local | decimal | 9 | 1 |  |  |  |

