# dbo.distribution_split_rpt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | bigint | 8 | 0 |  |  |  |
| sourceid | varchar | 20 | 0 |  |  |  |
| destid | varchar | 21 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| rec_type | varchar | 6 | 0 |  |  |  |
| sequencenbr | bigint | 8 | 0 |  |  |  |
| distribution_number | varchar | 20 | 0 |  |  |  |
| ref_field_1 | int | 4 | 0 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| active_pick_flag | varchar | 1 | 0 |  |  |  |
| released | bit | 1 | 1 |  |  |  |
| exported_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDate_rpt](../../StoredProcedures/me_01/dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDate_rpt.md)
- [me_01: dbo.sp_SelectDistroSplitDetailsByStore_rpt](../../StoredProcedures/me_01/dbo.sp_SelectDistroSplitDetailsByStore_rpt.md)
- [me_01: dbo.spDistroUpdateDataAfterSplit_rpt](../../StoredProcedures/me_01/dbo.spDistroUpdateDataAfterSplit_rpt.md)
- [me_01: dbo.spMerchandisingSplitReport_ALL_WHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_ALL_WHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_BHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_BHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_UK](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_UK.md)
- [me_01: dbo.spMerchandisingSplitReport_WC](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_WC.md)

