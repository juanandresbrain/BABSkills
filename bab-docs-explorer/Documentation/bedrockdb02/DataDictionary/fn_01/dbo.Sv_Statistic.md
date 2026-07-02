# dbo.Sv_Statistic

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| exec_id | int | 4 | 0 |  |  |  |
| view_id | int | 4 | 0 | YES |  |  |
| query_id | int | 4 | 0 | YES |  |  |
| period_id | int | 4 | 0 | YES |  |  |
| folder_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| user_id | int | 4 | 0 | YES |  |  |
| rows_count | int | 4 | 0 |  |  |  |
| cols_count | smallint | 2 | 0 |  |  |  |
| drill_count | int | 4 | 0 |  |  |  |
| table_count | smallint | 2 | 0 |  |  |  |
| drilled_to | bit | 1 | 0 |  |  |  |
| user_cancelled | bit | 1 | 0 |  |  |  |
| data_view_type | char | 1 | 0 |  |  |  |
| start_date_time | datetime | 8 | 0 | YES |  |  |
| loading_time | int | 4 | 0 |  |  |  |
| prepare_time | int | 4 | 0 |  |  |  |
| exec_time | int | 4 | 0 |  |  |  |
| retreive_time | int | 4 | 0 |  |  |  |
| usage_time | int | 4 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_SaveStatistic](../../StoredProcedures/fn_01/dbo.Sv_SaveStatistic.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_SaveStatistic](../../StoredProcedures/smartlook_01/dbo.Sv_SaveStatistic.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

