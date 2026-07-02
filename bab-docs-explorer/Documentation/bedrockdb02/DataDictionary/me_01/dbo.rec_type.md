# dbo.rec_type

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rectype | int | 4 | 1 |  |  |  |
| reasoncode | nvarchar | 510 | 1 |  |  |  |
| message | nvarchar | 510 | 1 |  |  |  |
| priority | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingDistroImport](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImport.md)
- [me_01: dbo.spMerchandisingDistroImport_BAK_20181119](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImport_BAK_20181119.md)
- [me_01: dbo.spMerchandisingDistroImportBACKUP20150909](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportBACKUP20150909.md)
- [me_01: dbo.spMerchandisingEmailWarehouseShipmentInformation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailWarehouseShipmentInformation.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN_bak_20180608](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN_bak_20180608.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN_BAK20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN_BAK20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsUK](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsUK.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsUK_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsUK_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_NEW](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_NEW.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20220731.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230403](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230403.md)
- [me_01: dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230414](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWCShipmentsAllocAdj_BAK20230414.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365.md)
- [me_01: dbo.spMerchandisingReportRecType](../../StoredProcedures/me_01/dbo.spMerchandisingReportRecType.md)
- [me_01: dbo.spMerchandisingSelectCondosBalesDistrosAndTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCondosBalesDistrosAndTransfers.md)
- [me_01: dbo.spMerchandisingSelectCostcoDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCostcoDistributions.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributions.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsWIP20220406.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_BAK20220731.md)
- [me_01: dbo.spMerchandisingSplitReport_ALL_WHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_ALL_WHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_BHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_BHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_UK](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_UK.md)
- [me_01: dbo.spMerchandisingSplitReport_WC](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_WC.md)
- [me_01: dbo.spMerchandisingStageDistrosToStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistrosToStoreShipments.md)
- [me_01: dbo.spMerchandisingStageDistrosToStoreShipmentsBAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistrosToStoreShipmentsBAK20220731.md)

