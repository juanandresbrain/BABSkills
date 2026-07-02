# dbo.z_pr_inv

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_date | varchar | 11 | 1 |  |  |  |
| transaction_type_code | varchar | 3 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| other_location_id | int | 4 | 1 |  |  |  |
| transaction_reason_id | int | 4 | 1 |  |  |  |
| document_number | int | 4 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | int | 4 | 0 |  |  |  |
| transaction_valuation_retail | decimal | 17 | 1 |  |  |  |
| transaction_selling_retail | int | 4 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| total_on_hand_units | int | 4 | 1 |  |  |  |

