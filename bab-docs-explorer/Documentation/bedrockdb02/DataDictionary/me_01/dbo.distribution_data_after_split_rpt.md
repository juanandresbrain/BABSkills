# dbo.distribution_data_after_split_rpt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | bigint | 8 | 1 |  |  |  |
| SourceID | varchar | 20 | 1 |  |  |  |
| DestID | varchar | 21 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| rec_type | varchar | 6 | 1 |  |  |  |
| sequencenbr | bigint | 8 | 1 |  |  |  |
| distribution_number | varchar | 50 | 1 |  |  |  |
| ref_field_1 | int | 4 | 1 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| active_pick_flag | varchar | 1 | 1 |  |  |  |
| released | nchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spDistroInsertAfterSplitData_rpt](../../StoredProcedures/me_01/dbo.spDistroInsertAfterSplitData_rpt.md)
- [me_01: dbo.spMerchandisingSplitReport_ALL_WHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_ALL_WHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_BHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_BHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_UK](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_UK.md)
- [me_01: dbo.spMerchandisingSplitReport_WC](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_WC.md)

