# dbo.MSsubscriber_schedule

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher | sysname | 256 | 0 |  |  |  |
| subscriber | sysname | 256 | 0 |  |  |  |
| agent_type | smallint | 2 | 0 |  |  |  |
| frequency_type | int | 4 | 0 |  |  |  |
| frequency_interval | int | 4 | 0 |  |  |  |
| frequency_relative_interval | int | 4 | 0 |  |  |  |
| frequency_recurrence_factor | int | 4 | 0 |  |  |  |
| frequency_subday | int | 4 | 0 |  |  |  |
| frequency_subday_interval | int | 4 | 0 |  |  |  |
| active_start_time_of_day | int | 4 | 0 |  |  |  |
| active_end_time_of_day | int | 4 | 0 |  |  |  |
| active_start_date | int | 4 | 0 |  |  |  |
| active_end_date | int | 4 | 0 |  |  |  |
