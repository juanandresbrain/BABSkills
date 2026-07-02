# dbo.dist_line

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| dist_line_id | int | 4 | 0 | YES |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| available_quantity | int | 4 | 1 |  |  |  |
| po_line_id | smallint | 2 | 1 |  |  |  |
| po_receipt_id | decimal | 9 | 1 |  |  |  |
| line_state | smallint | 2 | 1 |  |  |  |
| advance_shipping_notice_id | decimal | 9 | 1 |  |  |  |
| comp_set_id | bigint | 8 | 1 |  |  |  |
| primary_style_color_flag | bit | 1 | 0 |  |  |  |
| total_distributed_detail_qty | int | 4 | 0 |  |  |  |
| total_suggested_detail_qty | int | 4 | 0 |  |  |  |
| available_quantity_known | smallint | 2 | 0 |  |  |  |
| apply_comp_set_flag | bit | 1 | 1 |  |  |  |
| minimum_one_pack_per_loc_flag | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.spMerchandisingDistroImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportValidation.md)
- [me_01: dbo.spMerchandisingDistroTransfersValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroTransfersValidation.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdjWEB](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdjWEB.md)
- [me_01: dbo.spMerchandisingReportCanceledDistros](../../StoredProcedures/me_01/dbo.spMerchandisingReportCanceledDistros.md)
- [me_01: dbo.spMerchandisingSelectCanceledDistros](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCanceledDistros.md)
- [me_01: dbo.spMerchandisingSelectDistroComplete](../../StoredProcedures/me_01/dbo.spMerchandisingSelectDistroComplete.md)
- [me_01: dbo.spMerchandisingSplitReport_BHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_BHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_UK](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_UK.md)
- [me_01: dbo.spMerchandisingSplitReport_WC](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_WC.md)
- [me_01: dbo.spMerchandisingToCNDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToCNDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToUKDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToUKDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWCDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWCDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWmDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWmDistroExportNotification.md)

