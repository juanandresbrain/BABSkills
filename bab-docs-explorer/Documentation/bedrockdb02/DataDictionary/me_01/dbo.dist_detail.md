# dbo.dist_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| dist_detail_id | bigint | 8 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| eligibility_flag | bit | 1 | 0 |  |  |  |
| suggested_quantity | int | 4 | 0 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| skipped_reason | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.spMerchandisingDistroImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportValidation.md)
- [me_01: dbo.spMerchandisingDistroTransfersValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroTransfersValidation.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdjWEB](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdjWEB.md)
- [me_01: dbo.spMerchandisingSelectDistroComplete](../../StoredProcedures/me_01/dbo.spMerchandisingSelectDistroComplete.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentCN](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentCN.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentUK](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentUK.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentUK_BAK20220804](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentUK_BAK20220804.md)
- [me_01: dbo.spMerchandisingSelectMissingStoreShipmentWC](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMissingStoreShipmentWC.md)
- [me_01: dbo.spMerchandisingSplitReport_BHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_BHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_UK](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_UK.md)
- [me_01: dbo.spMerchandisingSplitReport_WC](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_WC.md)
- [me_01: dbo.spMerchandisingToCNDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToCNDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToUKDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToUKDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWCDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWCDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWmDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWmDistroExportNotification.md)
- [me_01: dbo.xfers_from_distro_$sp](../../StoredProcedures/me_01/dbo.xfers_from_distro_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)

