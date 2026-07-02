# dbo.merch_loc_dist_param

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| warehouse_id | smallint | 2 | 0 |  |  |  |
| location_lead_time | int | 4 | 0 |  |  |  |
| crossdock_processing_time | int | 4 | 0 |  |  |  |
| bulk_processing_time | int | 4 | 0 |  |  |  |
| additional_days_supply | int | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |

