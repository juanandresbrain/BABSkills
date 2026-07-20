# dbo.hierarchy_group

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| hierarchy_group_code | varchar | 8000 | 1 |  |  |  |
| hierarchy_group_label | varchar | 8000 | 1 |  |  |  |
| hierarchy_group_short_label | varchar | 8000 | 1 |  |  |  |
| alternate_hierarchy_group_code | varchar | 8000 | 1 |  |  |  |
| hierarchy_id | int | 4 | 1 |  |  |  |
| parent_group_id | int | 4 | 1 |  |  |  |
| hierarchy_level_id | int | 4 | 1 |  |  |  |
| goal_imu_percent | decimal | 5 | 1 |  |  |  |
| imu_tolerance_percent | decimal | 5 | 1 |  |  |  |
| plu_description | varchar | 8000 | 1 |  |  |  |
| shrinkage_provision_percent | decimal | 5 | 1 |  |  |  |
| ticket_format_id | int | 4 | 1 |  |  |  |
| leased_flag | bit | 1 | 1 |  |  |  |
| pos_merch_group_key | int | 4 | 1 |  |  |  |
| sl_minimum_cost_percent | decimal | 5 | 1 |  |  |  |
| sl_maximum_cost_percent | decimal | 5 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| pos_dept_group_key | int | 4 | 1 |  |  |  |
| plu_dept_group_description | varchar | 8000 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |
| planning_jurisdiction_id | int | 4 | 1 |  |  |  |
