# dbo.z_ib_cost_fix_43943

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| other_location_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| document_number | varchar | 20 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | numeric | 9 | 1 |  |  |  |
| transaction_valuation_retail | int | 4 | 0 |  |  |  |
| transaction_selling_retail | int | 4 | 0 |  |  |  |
| price_change_type | int | 4 | 1 |  |  |  |
| units_affected | int | 4 | 1 |  |  |  |

