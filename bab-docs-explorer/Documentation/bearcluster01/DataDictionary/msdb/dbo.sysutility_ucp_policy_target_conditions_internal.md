# dbo.sysutility_ucp_policy_target_conditions_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rollup_object_type | int | 4 | 0 | YES |  |  |
| target_type | int | 4 | 0 | YES |  |  |
| resource_type | int | 4 | 0 | YES |  |  |
| utilization_type | int | 4 | 0 | YES |  |  |
| facet_name | sysname | 256 | 0 | YES |  |  |
| attribute_name | sysname | 256 | 0 | YES |  |  |
| operator_type | int | 4 | 0 |  |  |  |
| property_name | sysname | 256 | 0 |  |  |  |

