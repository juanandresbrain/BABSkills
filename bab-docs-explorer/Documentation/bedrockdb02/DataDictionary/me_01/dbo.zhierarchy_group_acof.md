# dbo.zhierarchy_group_acof

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_label | nvarchar | 80 | 0 |  |  |  |
| hierarchy_group_short_label | nvarchar | 40 | 0 |  |  |  |
| alternate_hierarchy_group_code | nvarchar | 40 | 1 |  |  |  |
| hierarchy_id | smallint | 2 | 1 |  |  |  |
| parent_group_id | int | 4 | 1 |  |  |  |
| hierarchy_level_id | int | 4 | 1 |  |  |  |
| goal_imu_percent | decimal | 5 | 1 |  |  |  |
| imu_tolerance_percent | decimal | 5 | 1 |  |  |  |
| plu_description | nvarchar | 80 | 1 |  |  |  |
| shrinkage_provision_percent | decimal | 5 | 1 |  |  |  |
| ticket_format_id | smallint | 2 | 1 |  |  |  |
| leased_flag | bit | 1 | 1 |  |  |  |
| pos_merch_group_key | int | 4 | 1 |  |  |  |
| sl_minimum_cost_percent | decimal | 5 | 1 |  |  |  |
| sl_maximum_cost_percent | decimal | 5 | 1 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| pos_dept_group_key | int | 4 | 1 |  |  |  |
| plu_dept_group_description | nvarchar | 100 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |
| planning_jurisdiction_id | smallint | 2 | 1 |  |  |  |

