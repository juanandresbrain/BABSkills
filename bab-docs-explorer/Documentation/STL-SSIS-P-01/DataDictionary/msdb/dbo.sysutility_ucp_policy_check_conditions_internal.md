# dbo.sysutility_ucp_policy_check_conditions_internal

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| target_type | int | 4 | 0 | YES |  |  |
| resource_type | int | 4 | 0 | YES |  |  |
| utilization_type | int | 4 | 0 | YES |  |  |
| facet_name | sysname | 256 | 0 | YES |  |  |
| attribute_name | sysname | 256 | 0 | YES |  |  |
| operator_type | int | 4 | 0 |  |  |  |
| property_name | sysname | 256 | 0 |  |  |  |

