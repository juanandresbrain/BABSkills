# dbo.distribution_data_after_split

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

- [me_01: dbo.spDistroInsertAfterSplitData](../../StoredProcedures/me_01/dbo.spDistroInsertAfterSplitData.md)
- [me_01: dbo.spDistroSplitDetailList](../../StoredProcedures/me_01/dbo.spDistroSplitDetailList.md)
- [me_01: dbo.spDistroSplitSummaryList](../../StoredProcedures/me_01/dbo.spDistroSplitSummaryList.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN_bak_20180608](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN_bak_20180608.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN_BAK20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN_BAK20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsUK](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsUK.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsUK_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsUK_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_NEW](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_NEW.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWM](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWM.md)
- [me_01: dbo.spMerchandisingExportWebDistros](../../StoredProcedures/me_01/dbo.spMerchandisingExportWebDistros.md)
- [me_01: dbo.spMerchandisingExportWebDistros_bak_20191023](../../StoredProcedures/me_01/dbo.spMerchandisingExportWebDistros_bak_20191023.md)
- [me_01: dbo.spMerchandisingOutputItemMasterHTS](../../StoredProcedures/me_01/dbo.spMerchandisingOutputItemMasterHTS.md)
- [me_01: dbo.spMerchandisingReportZeroQtyDistros](../../StoredProcedures/me_01/dbo.spMerchandisingReportZeroQtyDistros.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributions.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsWIP20220406.md)
- [me_01: dbo.spMerchandisingStageDistrosToStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistrosToStoreShipments.md)
- [me_01: dbo.spMerchandisingStageDistrosToStoreShipmentsBAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistrosToStoreShipmentsBAK20220731.md)
- [me_01: dbo.spMerchandisingToCNDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToCNDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToUKDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToUKDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWCDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWCDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWmDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWmDistroExportNotification.md)

