# dbo.import_merchandise_group

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_merchandise_group_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| alternate_flag | nchar | 2 | 1 |  |  |  |
| hierarchy_name | nvarchar | 60 | 1 |  |  |  |
| hierarchy_level_label | nvarchar | 60 | 0 |  |  |  |
| parent_group_code | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_short_label | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_label | nvarchar | 80 | 1 |  |  |  |
| alternate_hierarchy_group_code | nvarchar | 40 | 1 |  |  |  |
| active_flag | nchar | 2 | 1 |  |  |  |
| goal_imu_percent | decimal | 5 | 1 |  |  |  |
| imu_tolerance_percent | decimal | 5 | 1 |  |  |  |
| pos_merch_group_key | decimal | 9 | 1 |  |  |  |
| shrinkage_provision_percent | decimal | 5 | 1 |  |  |  |
| ticket_format_code | nvarchar | 4 | 1 |  |  |  |
| plu_description | nvarchar | 80 | 1 |  |  |  |
| sl_minimum_cost_percent | decimal | 5 | 1 |  |  |  |
| sl_maximum_cost_percent | decimal | 5 | 1 |  |  |  |
| leased_flag | nchar | 2 | 1 |  |  |  |
| position_code | nvarchar | 40 | 1 |  |  |  |
| pos_dept_group_key | int | 4 | 1 |  |  |  |
| plu_dept_group_description | nvarchar | 100 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |

