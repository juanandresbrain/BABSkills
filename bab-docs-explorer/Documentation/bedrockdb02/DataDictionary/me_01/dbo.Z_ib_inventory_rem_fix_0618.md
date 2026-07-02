# dbo.Z_ib_inventory_rem_fix_0618

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | int | 4 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_date | varchar | 19 | 0 |  |  |  |
| transaction_type_code | varchar | 3 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| other_location_id | int | 4 | 1 |  |  |  |
| transaction_reason_id | int | 4 | 1 |  |  |  |
| document_number | varchar | 10 | 0 |  |  |  |
| transaction_units | int | 4 | 1 |  |  |  |
| transaction_cost | decimal | 17 | 1 |  |  |  |
| transaction_valuation_retail | decimal | 17 | 1 |  |  |  |
| transaction_selling_retail | decimal | 17 | 1 |  |  |  |
| price_change_type | int | 4 | 1 |  |  |  |
| units_affected | int | 4 | 1 |  |  |  |
| transaction_cost_local | decimal | 17 | 1 |  |  |  |
| updated_flag | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| batch_no | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |

