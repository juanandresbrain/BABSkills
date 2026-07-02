# dbo.store_shipment_export

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_number | varchar | 20 | 1 |  |  |  |
| document_number | varchar | 20 | 1 |  |  |  |
| distribution_line_number | int | 4 | 1 |  |  |  |
| warehouse | varchar | 4 | 1 |  |  |  |
| location_code | varchar | 10 | 1 |  |  |  |
| rec_type | varchar | 10 | 1 |  |  |  |
| rec_label | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| short_desc | varchar | 100 | 1 |  |  |  |
| vendor_style | varchar | 52 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| exported | int | 4 | 1 |  |  |  |
| expected_ship_date | date | 3 | 1 |  |  |  |
| Cancelled | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingExportStoreDistributionsCN](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN_bak_20180608](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN_bak_20180608.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN_BAK20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN_BAK20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsUK](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsUK.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsUK_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsUK_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_NEW](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_NEW.md)
- [me_01: dbo.spMerchandisingProcessCNShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessCNShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingReportStoreShipmentExportConfirmationCN](../../StoredProcedures/me_01/dbo.spMerchandisingReportStoreShipmentExportConfirmationCN.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentCN](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentCN.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentUK_BAK20220804](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentUK_BAK20220804.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CNBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CNBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CNWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CNWIP20220406.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_BAK20220731.md)
- [me_01: dbo.spMerchandisingStageDistrosToStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistrosToStoreShipments.md)
- [me_01: dbo.spMerchandisingStageDistrosToStoreShipmentsBAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistrosToStoreShipmentsBAK20220731.md)

