# dbo.z_uk_sales_fix_list

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
| document_number | nvarchar | 40 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | numeric | 5 | 0 |  |  |  |
| transaction_valuation_retail | numeric | 9 | 1 |  |  |  |
| transaction_selling_retail | numeric | 5 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| units_affected | int | 4 | 1 |  |  |  |
| transaction_cost_local | numeric | 5 | 0 |  |  |  |
| updated_flag | bit | 1 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| batch_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |

