# dbo.export_past_due_on_order_loc

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merchandise_code | nvarchar | 40 | 0 |  |  |  |
| loc_hierarchy_group_code | nvarchar | 40 | 1 |  |  |  |
| current_week | int | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| due_on_order_retail | decimal | 9 | 1 |  |  |  |
| due_on_order_units | int | 4 | 1 |  |  |  |
| due_on_order_cost | decimal | 9 | 1 |  |  |  |
| due_on_order_retail_local | decimal | 9 | 1 |  |  |  |
| due_on_order_cost_local | decimal | 9 | 1 |  |  |  |

