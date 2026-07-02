# dbo.le_sales_schedule

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| le_sales_schedule_id | T_ID | 16 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| cycle_period | tinyint | 1 | 0 |  |  |  |
| cycle_frequency | smallint | 2 | 0 |  |  |  |
| next_run_date | smalldatetime | 4 | 1 |  |  |  |
| last_run_date | smalldatetime | 4 | 1 |  |  |  |
| application_server_id | T_ID | 16 | 0 |  |  |  |
| no_prior_weeks | smallint | 2 | 0 |  |  |  |
| run_on_sunday | bit | 1 | 1 |  |  |  |
| run_on_monday | bit | 1 | 1 |  |  |  |
| run_on_tuesday | bit | 1 | 1 |  |  |  |
| run_on_wednesday | bit | 1 | 1 |  |  |  |
| run_on_thursday | bit | 1 | 1 |  |  |  |
| run_on_friday | bit | 1 | 1 |  |  |  |
| run_on_saturday | bit | 1 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

