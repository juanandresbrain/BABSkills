# dbo.z_inventory_oh_0316

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| transaction_cost | decimal | 17 | 1 |  |  |  |
| transaction_valuation_retail | decimal | 17 | 1 |  |  |  |
| transaction_selling_retail | decimal | 17 | 1 |  |  |  |
| transaction_cost_local | decimal | 17 | 1 |  |  |  |

