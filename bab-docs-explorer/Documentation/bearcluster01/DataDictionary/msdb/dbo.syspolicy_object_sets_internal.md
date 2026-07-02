# dbo.syspolicy_object_sets_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_set_id | int | 4 | 0 | YES |  |  |
| object_set_name | sysname | 256 | 0 |  |  |  |
| facet_id | int | 4 | 1 |  | YES |  |
| is_system | bit | 1 | 0 |  |  |  |

