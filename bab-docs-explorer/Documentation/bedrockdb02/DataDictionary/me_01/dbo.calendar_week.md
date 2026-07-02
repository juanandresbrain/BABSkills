# dbo.calendar_week

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| calendar_week_id | decimal | 9 | 0 | YES |  |  |
| calendar_week_code | tinyint | 1 | 0 |  |  |  |
| calendar_week_start_date | smalldatetime | 4 | 0 |  |  |  |
| calendar_week_end_date | smalldatetime | 4 | 0 |  |  |  |
| calendar_year_id | smallint | 2 | 0 |  |  |  |
| calendar_period_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.get_curr_slpd_$fn](../../StoredProcedures/me_01/dbo.get_curr_slpd_$fn.md)
- [me_01: dbo.get_first_prev_slpd_ly_$fn](../../StoredProcedures/me_01/dbo.get_first_prev_slpd_ly_$fn.md)
- [me_01: dbo.get_first_prev_slpd_ty_$fn](../../StoredProcedures/me_01/dbo.get_first_prev_slpd_ty_$fn.md)
- [me_01: dbo.get_first_slpd_ly_$fn](../../StoredProcedures/me_01/dbo.get_first_slpd_ly_$fn.md)
- [me_01: dbo.get_first_slpd_ty_$fn](../../StoredProcedures/me_01/dbo.get_first_slpd_ty_$fn.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

