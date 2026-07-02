# dbo.parameter_planning

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_planning_id | tinyint | 1 | 0 | YES |  |  |
| plan_by_division_flag | bit | 1 | 0 |  |  |  |
| division_code_suffix_flag | bit | 1 | 0 |  |  |  |
| location_hierarchy_level_id | int | 4 | 1 |  |  |  |
| mapping_loc_hier_level_id | int | 4 | 1 |  |  |  |
| mapping_merch_hier_level_id | int | 4 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| plan_export_crncy_type | int | 4 | 1 |  |  |  |

