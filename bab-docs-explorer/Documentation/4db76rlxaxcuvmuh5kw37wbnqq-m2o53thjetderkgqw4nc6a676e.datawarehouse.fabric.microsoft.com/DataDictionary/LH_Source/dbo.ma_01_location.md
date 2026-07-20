# dbo.ma_01_location

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | int | 4 | 1 |  |  |  |
| location_type | int | 4 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| location_name | varchar | 8000 | 1 |  |  |  |
| location_short_name | varchar | 8000 | 1 |  |  |  |
| location_status_id | int | 4 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| gl_company_id | int | 4 | 1 |  |  |  |
| gl_location_number | varchar | 8000 | 1 |  |  |  |
| selling_space | decimal | 9 | 1 |  |  |  |
| non_selling_space | decimal | 9 | 1 |  |  |  |
| target_sales | decimal | 9 | 1 |  |  |  |
| occupancy_cost | decimal | 9 | 1 |  |  |  |
| shrinkage_factor | decimal | 5 | 1 |  |  |  |
| open_date | datetime2 | 8 | 1 |  |  |  |
| comparative_date | datetime2 | 8 | 1 |  |  |  |
| reopen_date | datetime2 | 8 | 1 |  |  |  |
| closed_date | datetime2 | 8 | 1 |  |  |  |
| closed_reason | varchar | 8000 | 1 |  |  |  |
| remodel_start_date | datetime2 | 8 | 1 |  |  |  |
| remodel_end_date | datetime2 | 8 | 1 |  |  |  |
| open_to_receive_date | datetime2 | 8 | 1 |  |  |  |
| jurisdiction_id | int | 4 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| routing_priority | int | 4 | 1 |  |  |  |
| send_inv_move_to_es_flag | bit | 1 | 1 |  |  |  |
| selling_location | bit | 1 | 1 |  |  |  |
