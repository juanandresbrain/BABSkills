# dbo.startup_mc_sl_log

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| startup_sl_log_id | int | 4 | 0 |  |  |  |
| proc_name | nvarchar | 200 | 0 |  |  |  |
| hist_period_processed | decimal | 9 | 0 |  |  |  |
| start_location_id | smallint | 2 | 0 |  |  |  |
| end_location_id | smallint | 2 | 0 |  |  |  |
| end_time | datetime | 8 | 0 |  |  |  |
| completed_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)
- [me_01: dbo.startup_sl_history_single_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_single_jurisdiction_$sp.md)

