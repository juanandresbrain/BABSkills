# esell.outlet

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| outlet_id | nvarchar | 40 | 0 | YES |  |  |
| outlet_desc | nvarchar | 80 | 1 |  |  |  |
| outlet1_address | nvarchar | 200 | 1 |  |  |  |
| outlet2_address | nvarchar | 200 | 1 |  |  |  |
| city_name | nvarchar | 120 | 1 |  |  |  |
| state_code | nvarchar | 40 | 1 |  |  |  |
| postal_code | nvarchar | 30 | 1 |  |  |  |
| country | nchar | 6 | 1 |  | YES |  |
| hours_desc | nvarchar | 200 | 1 |  |  |  |
| contact_text | nvarchar | 200 | 1 |  |  |  |
| search_allowed_cd | nchar | 2 | 1 |  |  |  |
| ship_rout_priority | int | 4 | 1 |  |  |  |
| latitude | float | 8 | 1 |  |  |  |
| longitude | float | 8 | 1 |  |  |  |
| order_volume | int | 4 | 0 |  |  |  |
| rec_update_date | datetime | 8 | 0 |  |  |  |
| rec_create_date | datetime | 8 | 0 |  |  |  |
| rec_update_id | int | 4 | 0 |  |  |  |
| group_id | nvarchar | 2 | 0 |  |  |  |

