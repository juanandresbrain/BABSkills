# dbo.distribution

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| distribution_number | nvarchar | 40 | 0 |  |  |  |
| distribution_description | nvarchar | 120 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| distribution_status | smallint | 2 | 0 |  |  |  |
| status_date | smalldatetime | 4 | 0 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| distribution_method | smallint | 2 | 1 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| reserve_location_id | smallint | 2 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| po_shipment_id | smallint | 2 | 1 |  |  |  |
| po_receipt_id | decimal | 9 | 1 |  |  |  |
| advance_shipping_notice_id | decimal | 9 | 1 |  |  |  |
| asn_po_location_id | decimal | 9 | 1 |  |  |  |
| apply_eligibility_flag | bit | 1 | 0 |  |  |  |
| retain_for_distribution_flag | bit | 1 | 0 |  |  |  |
| po_quantities_required_flag | bit | 1 | 0 |  |  |  |
| po_generated_flag | bit | 1 | 0 |  |  |  |
| available_quantity_known | smallint | 2 | 0 |  |  |  |
| average_sales_basis | smallint | 2 | 1 |  |  |  |
| volume_grade_basis | smallint | 2 | 1 |  |  |  |
| volume_hierarchy_group_id | int | 4 | 1 |  |  |  |
| prior_distribution_available | int | 4 | 1 |  |  |  |
| sales_data_basis | smallint | 2 | 1 |  |  |  |
| plan_calendar_period_id | decimal | 9 | 1 |  |  |  |
| sales_from_calendar_week_id | decimal | 9 | 1 |  |  |  |
| sales_to_calendar_week_id | decimal | 9 | 1 |  |  |  |
| sell_thru_hierarchy_group_id | int | 4 | 1 |  |  |  |
| apply_scale | smallint | 2 | 1 |  |  |  |
| scale_entry_indicator | smallint | 2 | 1 |  |  |  |
| distribution_multiple | int | 4 | 0 |  |  |  |
| dist_multiple_rounding_pct | int | 4 | 0 |  |  |  |
| target_pct_need | decimal | 5 | 1 |  |  |  |
| plan_hierarchy_group_id | int | 4 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| previous_status | smallint | 2 | 1 |  |  |  |
| number_active_stores | smallint | 2 | 1 |  |  |  |
| hist_unit_sales_all_stores | bigint | 8 | 1 |  |  |  |
| hist_effect_inv_all_stores | bigint | 8 | 1 |  |  |  |
| hist_on_hand_all_stores | bigint | 8 | 1 |  |  |  |
| plan_unit_sales_all_stores | bigint | 8 | 1 |  |  |  |
| print_for_picking_flag | bit | 1 | 1 |  |  |  |
| allow_size_substitution_flag | bit | 1 | 0 |  |  |  |
| consider_effect_inv_flag | bit | 1 | 0 |  |  |  |
| parent_distribution_id | bigint | 8 | 1 |  |  |  |
| root_distribution_id | bigint | 8 | 1 |  |  |  |
| total_distributed_detail_qty | int | 4 | 0 |  |  |  |
| total_suggested_detail_qty | int | 4 | 0 |  |  |  |
| plan_remain_sales_all_stores | bigint | 8 | 1 |  |  |  |
| plan_on_hand_all_stores | bigint | 8 | 1 |  |  |  |
| update_po_quantity_flag | bit | 1 | 0 |  |  |  |
| weeks_of_supply_loc_need | smallint | 2 | 0 |  |  |  |
| incl_effect_inv_loc_need_flag | bit | 1 | 0 |  |  |  |
| apply_max_constraint_flag | bit | 1 | 0 |  |  |  |
| grade_type_for_assortment | smallint | 2 | 0 |  |  |  |
| remove_qty_start_from | smallint | 2 | 0 |  |  |  |
| add_qty_start_from | smallint | 2 | 0 |  |  |  |
| keep_in_reserve | smallint | 2 | 0 |  |  |  |
| max_pack_type_per_loc | smallint | 2 | 0 |  |  |  |
| allow_pack_alloc_exceed_loc | smallint | 2 | 0 |  |  |  |
| allow_pk_alloc_exceed_sku_unit | smallint | 2 | 0 |  |  |  |
| available_qty_is_known | bit | 1 | 0 |  |  |  |
| store_pack_definition_released | bit | 1 | 0 |  |  |  |
| store_pack_definition_locked | bit | 1 | 0 |  |  |  |
| prior_dist_actual_available | int | 4 | 1 |  |  |  |
| ranking_group_code | nvarchar | 40 | 1 |  |  |  |
| ranking_group_hierarchy_grp_id | int | 4 | 1 |  |  |  |
| ranking_group_style_id | decimal | 9 | 1 |  |  |  |
| ranking_group_type | smallint | 2 | 1 |  |  |  |
| pack_size_threshold | smallint | 2 | 0 |  |  |  |
| allow_pk_alloc_exceed_sku_pct | smallint | 2 | 0 |  |  |  |
| minimum_one_pack_per_loc_flag | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_S](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_S.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W2](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W2.md)
- [me_01: dbo.spMerchandisingDistroImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportValidation.md)
- [me_01: dbo.spMerchandisingDistroTransfersValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroTransfersValidation.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdjWEB](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdjWEB.md)
- [me_01: dbo.spMerchandisingReportCanceledDistros](../../StoredProcedures/me_01/dbo.spMerchandisingReportCanceledDistros.md)
- [me_01: dbo.spMerchandisingSelectCanceledDistros](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCanceledDistros.md)
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
- [me_01: dbo.spMerchandisingWhsePickReviewSummary](../../StoredProcedures/me_01/dbo.spMerchandisingWhsePickReviewSummary.md)
- [me_01: dbo.spPartyManager_ActiveDistro](../../StoredProcedures/me_01/dbo.spPartyManager_ActiveDistro.md)
- [me_01: dbo.spUKAvailSupplies](../../StoredProcedures/me_01/dbo.spUKAvailSupplies.md)
- [me_01: dbo.zzz_set_dist_method_$sp](../../StoredProcedures/me_01/dbo.zzz_set_dist_method_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)

