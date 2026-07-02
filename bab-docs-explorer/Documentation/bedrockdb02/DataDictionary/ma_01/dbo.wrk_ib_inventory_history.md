# dbo.wrk_ib_inventory_history

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| datetime_Inserted | datetime | 8 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| ib_inventory_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_valuation_retail | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail | decimal | 9 | 0 |  |  |  |
| transaction_val_retail_te | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail_te | decimal | 9 | 0 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |

