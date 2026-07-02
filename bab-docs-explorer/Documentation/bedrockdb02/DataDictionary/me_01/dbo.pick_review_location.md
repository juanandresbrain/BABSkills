# dbo.pick_review_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pick_review_parameter_id | int | 4 | 0 |  |  |  |
| merchandise_hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| warehouse_id | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| suspend_distribution | bit | 1 | 0 |  |  |  |
| suspend_distribution_from | smalldatetime | 4 | 1 |  |  |  |
| suspend_distribution_to | smalldatetime | 4 | 1 |  |  |  |
| effective_inventory_time_frame | int | 4 | 0 |  |  |  |

