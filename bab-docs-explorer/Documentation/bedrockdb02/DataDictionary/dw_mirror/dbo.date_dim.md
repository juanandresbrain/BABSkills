# dbo.date_dim

**Database:** dw_mirror  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| date_key | int | 4 | 0 | YES |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| season | varchar | 20 | 1 |  |  |  |
| fiscal_quarter | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| fiscal_week | int | 4 | 1 |  |  |  |
| month | int | 4 | 1 |  |  |  |
| year | int | 4 | 1 |  |  |  |
| month_name | varchar | 20 | 1 |  |  |  |
| day_of_month | int | 4 | 1 |  |  |  |
| day_of_year | int | 4 | 1 |  |  |  |
| day_name | varchar | 20 | 1 |  |  |  |
| weekend_y_n | varchar | 20 | 1 |  |  |  |
| day_of_week | int | 4 | 1 |  |  |  |
| week_of_period | int | 4 | 1 |  |  |  |
| week_of_quarter | int | 4 | 1 |  |  |  |
| period_of_quarter | int | 4 | 1 |  |  |  |
| day_id | int | 4 | 1 |  |  |  |
| holiday_period_code | varchar | 20 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| quarter_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spAnnualReminder_FiscalQuarterCheck](../../StoredProcedures/me_01/dbo.spAnnualReminder_FiscalQuarterCheck.md)
- [me_01: dbo.spDW_CurrentRetail](../../StoredProcedures/me_01/dbo.spDW_CurrentRetail.md)
- [me_01: dbo.spDW_DoorCount](../../StoredProcedures/me_01/dbo.spDW_DoorCount.md)
- [ma_01: dbo.spDW_Inventory](../../StoredProcedures/ma_01/dbo.spDW_Inventory.md)
- [ma_01: dbo.spDW_TopStyleTy](../../StoredProcedures/ma_01/dbo.spDW_TopStyleTy.md)
- [ma_01: dbo.spDW_TopStyleTyBACKUP20180108](../../StoredProcedures/ma_01/dbo.spDW_TopStyleTyBACKUP20180108.md)

