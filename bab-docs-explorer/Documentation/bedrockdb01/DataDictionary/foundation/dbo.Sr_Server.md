# dbo.Sr_Server

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_id | int | 4 | 0 |  |  |  |
| server_name | nvarchar | 60 | 1 |  |  |  |
| any_job | bit | 1 | 0 |  |  |  |
| max_jobs | smallint | 2 | 0 |  |  |  |
| curr_status | smallint | 2 | 0 |  |  |  |
| requested_status | smallint | 2 | 1 |  |  |  |
| machine_id | int | 4 | 0 |  |  |  |
| autostart | smallint | 2 | 0 |  |  |  |
| application_module | varchar | 500 | 1 |  |  |  |
| used_for_reporting | bit | 1 | 1 |  |  |  |
| reporting_server_description | nvarchar | 100 | 1 |  |  |  |
| blackout_period_details | varchar | 255 | 1 |  |  |  |
