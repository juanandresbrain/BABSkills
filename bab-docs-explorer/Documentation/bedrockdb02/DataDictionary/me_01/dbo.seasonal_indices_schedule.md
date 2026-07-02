# dbo.seasonal_indices_schedule

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| seasonal_profile_group_id | decimal | 9 | 0 | YES | YES |  |
| next_run_date | smalldatetime | 4 | 1 |  |  |  |
| last_run_date | smalldatetime | 4 | 1 |  |  |  |
| application_server_id | T_ID | 16 | 0 |  |  |  |
| num_future_years | smallint | 2 | 0 |  |  |  |
| num_past_years | smallint | 2 | 0 |  |  |  |
| num_past_years_average | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

