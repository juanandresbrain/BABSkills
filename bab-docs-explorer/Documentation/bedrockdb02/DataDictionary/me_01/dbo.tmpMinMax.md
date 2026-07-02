# dbo.tmpMinMax

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| presentation_stock | int | 4 | 1 |  |  |  |
| capacity_maximum | varchar | 6 | 1 |  |  |  |
| minimum | varchar | 6 | 1 |  |  |  |
| maximum | varchar | 6 | 1 |  |  |  |
| dyamic_minimum | int | 4 | 1 |  |  |  |
| dyamic_maximum | int | 4 | 1 |  |  |  |
| dyamic_start_date | datetime | 8 | 0 |  |  |  |
| order_point | varchar | 1 | 0 |  |  |  |
| incl_pres_stock_with_ord_pt_fl | int | 4 | 1 |  |  |  |
| source | int | 4 | 1 |  |  |  |
| last_activity_date | datetime | 8 | 0 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |

