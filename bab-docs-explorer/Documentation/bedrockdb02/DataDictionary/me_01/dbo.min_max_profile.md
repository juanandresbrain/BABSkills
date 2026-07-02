# dbo.min_max_profile

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| presentation_stock | int | 4 | 1 |  |  |  |
| capacity_maximum | int | 4 | 1 |  |  |  |
| minimum | int | 4 | 1 |  |  |  |
| maximum | int | 4 | 1 |  |  |  |
| dynamic_minimum | int | 4 | 1 |  |  |  |
| dynamic_maximum | int | 4 | 1 |  |  |  |
| dynamic_start_date | smalldatetime | 4 | 1 |  |  |  |
| order_point | tinyint | 1 | 0 |  |  |  |
| incl_pres_stock_with_ord_pt_fl | bit | 1 | 0 |  |  |  |
| source | tinyint | 1 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingInsertMinMaxProfileArchive](../../StoredProcedures/me_01/dbo.spMerchandisingInsertMinMaxProfileArchive.md)
- [me_01: dbo.spMerchandisingMinMaxHistory](../../StoredProcedures/me_01/dbo.spMerchandisingMinMaxHistory.md)
- [me_01: dbo.spMerchandisingMinMaxRunCheck](../../StoredProcedures/me_01/dbo.spMerchandisingMinMaxRunCheck.md)
- [me_01: dbo.spMerchandisingReportStoreSkinReview](../../StoredProcedures/me_01/dbo.spMerchandisingReportStoreSkinReview.md)

