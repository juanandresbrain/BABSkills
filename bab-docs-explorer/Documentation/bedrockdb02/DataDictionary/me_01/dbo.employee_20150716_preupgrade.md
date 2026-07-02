# dbo.employee_20150716_preupgrade

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_id | decimal | 9 | 0 |  |  |  |
| employee_code | varchar | 20 | 0 |  |  |  |
| employee_home_location | decimal | 9 | 1 |  |  |  |
| employee_lastname | varchar | 30 | 0 |  |  |  |
| employee_firstname | varchar | 30 | 0 |  |  |  |
| employee_fullpart_flag | bit | 1 | 0 |  |  |  |
| employee_permtemp_flag | bit | 1 | 0 |  |  |  |
| employee_alternate_no | int | 4 | 1 |  |  |  |
| employee_house_account_no | decimal | 9 | 1 |  |  |  |
| employee_hired_date | smalldatetime | 4 | 0 |  |  |  |
| employee_discount | decimal | 5 | 1 |  |  |  |
| employee_max_discount | decimal | 5 | 1 |  |  |  |
| security_user_id | int | 4 | 1 |  |  |  |
| nt_user_name | varchar | 30 | 1 |  |  |  |
| domain_name | varchar | 30 | 1 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| employee_sin | varchar | 9 | 1 |  |  |  |

