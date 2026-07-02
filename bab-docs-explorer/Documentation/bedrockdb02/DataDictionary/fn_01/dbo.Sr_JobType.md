# dbo.Sr_JobType

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_type | smallint | 2 | 0 | YES |  |  |
| exe_name | varchar | 512 | 1 |  |  |  |
| assembly_name | varchar | 255 | 1 |  |  |  |
| class_name | varchar | 255 | 1 |  |  |  |
| label | varchar | 255 | 0 |  |  |  |
| allow_new | bit | 1 | 0 |  |  |  |
| os_system | smallint | 2 | 0 |  |  |  |

