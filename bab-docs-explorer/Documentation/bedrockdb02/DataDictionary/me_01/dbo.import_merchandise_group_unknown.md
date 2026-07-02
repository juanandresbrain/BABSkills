# dbo.import_merchandise_group_unknown

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_merchandise_group_id | decimal | 9 | 0 |  |  |  |
| entity_type | varchar | 2 | 0 |  |  |  |
| action_type | char | 1 | 0 |  |  |  |
| alternate_flag | char | 1 | 1 |  |  |  |
| hierarchy_name | varchar | 30 | 1 |  |  |  |
| hierarchy_level_label | varchar | 30 | 0 |  |  |  |
| parent_group_code | varchar | 20 | 0 |  |  |  |
| hierarchy_group_code | varchar | 20 | 0 |  |  |  |
| hierarchy_group_short_label | varchar | 20 | 0 |  |  |  |
| hierarchy_group_label | varchar | 40 | 1 |  |  |  |
| alternate_hierarchy_group_code | varchar | 20 | 1 |  |  |  |
| active_flag | char | 1 | 1 |  |  |  |
| goal_imu_percent | decimal | 5 | 1 |  |  |  |
| imu_tolerance_percent | decimal | 5 | 1 |  |  |  |
| pos_merch_group_key | decimal | 9 | 1 |  |  |  |
| shrinkage_provision_percent | decimal | 5 | 1 |  |  |  |
| ticket_format_code | varchar | 2 | 1 |  |  |  |
| plu_description | varchar | 40 | 1 |  |  |  |
| sl_minimum_cost_percent | decimal | 5 | 1 |  |  |  |
| sl_maximum_cost_percent | decimal | 5 | 1 |  |  |  |
| leased_flag | char | 1 | 1 |  |  |  |
| position_code | varchar | 20 | 1 |  |  |  |
| pos_dept_group_key | int | 4 | 1 |  |  |  |
| plu_dept_group_description | varchar | 50 | 1 |  |  |  |

