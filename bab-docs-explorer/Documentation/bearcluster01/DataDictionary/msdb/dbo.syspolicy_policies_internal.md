# dbo.syspolicy_policies_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| policy_id | int | 4 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| condition_id | int | 4 | 0 |  | YES |  |
| root_condition_id | int | 4 | 1 |  | YES |  |
| date_created | datetime | 8 | 0 |  |  |  |
| execution_mode | int | 4 | 0 |  |  |  |
| policy_category_id | int | 4 | 1 |  | YES |  |
| schedule_uid | uniqueidentifier | 16 | 1 |  |  |  |
| description | nvarchar | -1 | 0 |  |  |  |
| help_text | nvarchar | 8000 | 0 |  |  |  |
| help_link | nvarchar | 4166 | 0 |  |  |  |
| object_set_id | int | 4 | 1 |  | YES |  |
| is_enabled | bit | 1 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 1 |  | YES |  |
| created_by | sysname | 256 | 0 |  |  |  |
| modified_by | sysname | 256 | 1 |  |  |  |
| date_modified | datetime | 8 | 1 |  |  |  |
| is_system | bit | 1 | 0 |  |  |  |

