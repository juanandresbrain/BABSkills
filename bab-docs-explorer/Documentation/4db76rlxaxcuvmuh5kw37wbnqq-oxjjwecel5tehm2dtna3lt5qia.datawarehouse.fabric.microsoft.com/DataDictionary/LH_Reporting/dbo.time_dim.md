# dbo.time_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| time_key | int | 4 | 1 |  |  |  |
| hour | int | 4 | 1 |  |  |  |
| minute | int | 4 | 1 |  |  |  |
| daypart | varchar | 8000 | 1 |  |  |  |
| half_hour_id | int | 4 | 1 |  |  |  |
| qtr_hour_id | int | 4 | 1 |  |  |  |
| HourMinuteKey | varchar | 8000 | 1 |  |  |  |
| HourMinuteDisplay | varchar | 8000 | 1 |  |  |  |
| HourDescription | varchar | 8000 | 1 |  |  |  |
| HalfHourDescription | varchar | 8000 | 1 |  |  |  |
| HalfHourKey | int | 4 | 1 |  |  |  |
| QuarterHourDescription | varchar | 8000 | 1 |  |  |  |
| QuarterHourKey | int | 4 | 1 |  |  |  |
| dayPartKey | int | 4 | 1 |  |  |  |
