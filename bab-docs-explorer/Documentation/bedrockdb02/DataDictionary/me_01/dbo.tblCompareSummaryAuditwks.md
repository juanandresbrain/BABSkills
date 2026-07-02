# dbo.tblCompareSummaryAuditwks

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| aw_store | int | 4 | 0 |  |  |  |
| aw_date | smalldatetime | 4 | 0 |  |  |  |
| aw_units | int | 4 | 1 |  |  |  |
| aw_sales | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_AW_vs_IB_sales](../../StoredProcedures/me_01/dbo.sp_AW_vs_IB_sales.md)

