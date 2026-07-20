# dbo.jumpmind_bab_active_user

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| business_unit_id | varchar | 8000 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| last_name | varchar | 8000 | 1 |  |  |  |
| first_name | varchar | 8000 | 1 |  |  |  |
| last_login | datetime2 | 8 | 1 |  |  |  |
| locked_out_flag | int | 4 | 1 |  |  |  |
| alternate_id | varchar | 8000 | 1 |  |  |  |
| workgroup_id | varchar | 8000 | 1 |  |  |  |
| user_active_flag | int | 4 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
