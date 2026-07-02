# dbo.tblCompareSummaryIB

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_store | int | 4 | 0 |  |  |  |
| ib_date | datetime | 8 | 0 |  |  |  |
| ib_units | int | 4 | 1 |  |  |  |
| ib_sales | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_AW_vs_IB_sales](../../StoredProcedures/me_01/dbo.sp_AW_vs_IB_sales.md)

