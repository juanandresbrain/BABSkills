# dbo.ib_allocation

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_allocation_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| allocated_units | int | 4 | 0 |  |  |  |
| purchase_order_number | nvarchar | 40 | 1 |  |  |  |
| allocation_number | nvarchar | 40 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_location_prices_validation_$sp](../../StoredProcedures/me_01/dbo.copy_location_prices_validation_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)
- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.insert_alloc_sku_$sp](../../StoredProcedures/me_01/dbo.insert_alloc_sku_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.on_order_pack_create_modify_$sp](../../StoredProcedures/me_01/dbo.on_order_pack_create_modify_$sp.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_S](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_S.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W2](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W2.md)
- [me_01: dbo.spMerchandisingOutputBaleCondo](../../StoredProcedures/me_01/dbo.spMerchandisingOutputBaleCondo.md)
- [me_01: dbo.spMerchandisingProcessCNShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessCNShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingReportCanceledDistros](../../StoredProcedures/me_01/dbo.spMerchandisingReportCanceledDistros.md)
- [me_01: dbo.spMerchandisingReportStoreSkinReview](../../StoredProcedures/me_01/dbo.spMerchandisingReportStoreSkinReview.md)
- [me_01: dbo.spMerchandisingSelectCanceledDistros](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCanceledDistros.md)
- [me_01: dbo.spMerchandisingSelectDistroComplete](../../StoredProcedures/me_01/dbo.spMerchandisingSelectDistroComplete.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_BAK20220731.md)
- [me_01: dbo.spPartyManager_ActiveDistro](../../StoredProcedures/me_01/dbo.spPartyManager_ActiveDistro.md)
- [me_01: dbo.spUKAvailSupplies](../../StoredProcedures/me_01/dbo.spUKAvailSupplies.md)

