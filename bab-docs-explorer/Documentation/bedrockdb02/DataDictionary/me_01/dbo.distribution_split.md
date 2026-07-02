# dbo.distribution_split

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | bigint | 8 | 0 | YES |  |  |
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

- [me_01: dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDate](../../StoredProcedures/me_01/dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDate.md)
- [me_01: dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDate_BJB20161212](../../StoredProcedures/me_01/dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDate_BJB20161212.md)
- [me_01: dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDateBACKUP20180702](../../StoredProcedures/me_01/dbo.sp_DistroRowsReadyForSplitForAGivenStoreAndDateBACKUP20180702.md)
- [me_01: dbo.sp_DynamicsDistroRowsReadyForSplitForAGivenStoreAndDate](../../StoredProcedures/me_01/dbo.sp_DynamicsDistroRowsReadyForSplitForAGivenStoreAndDate.md)
- [me_01: dbo.sp_SelectDistroSplitDetailsByStore](../../StoredProcedures/me_01/dbo.sp_SelectDistroSplitDetailsByStore.md)
- [me_01: dbo.sp_SelectDynamicsDistroSplitDetailsByStore](../../StoredProcedures/me_01/dbo.sp_SelectDynamicsDistroSplitDetailsByStore.md)
- [me_01: dbo.spDistroSplitDetailList](../../StoredProcedures/me_01/dbo.spDistroSplitDetailList.md)
- [me_01: dbo.spDistroSplitSummaryList](../../StoredProcedures/me_01/dbo.spDistroSplitSummaryList.md)
- [me_01: dbo.spDistroUpdateDataAfterSplit](../../StoredProcedures/me_01/dbo.spDistroUpdateDataAfterSplit.md)
- [me_01: dbo.spDynamicsDistroUpdateDataAfterSplit](../../StoredProcedures/me_01/dbo.spDynamicsDistroUpdateDataAfterSplit.md)
- [me_01: dbo.spMerchandisingReportRecType](../../StoredProcedures/me_01/dbo.spMerchandisingReportRecType.md)
- [me_01: dbo.spMerchandisingSplitReport_ALL_WHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_ALL_WHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_BHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_BHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_UK](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_UK.md)
- [me_01: dbo.spMerchandisingSplitReport_WC](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_WC.md)
- [me_01: dbo.spMerchandisingStageDistroSplit](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistroSplit.md)
- [me_01: dbo.spMerchandisingToCNDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToCNDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToUKDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToUKDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWCDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWCDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWmDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWmDistroExportNotification.md)

