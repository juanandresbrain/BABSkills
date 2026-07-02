# Stored Procedures: esell

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [FNDTN_RGSTR_TBL_$SP](dbo.FNDTN_RGSTR_TBL_$SP.md) | dbo.FNDTN_TBL_LIST |
| dbo | [FNDTN_UNRGSTR_TBL_$SP](dbo.FNDTN_UNRGSTR_TBL_$SP.md) | dbo.FNDTN_TBL_LIST |
| /* Procedure | [: FNDTN_UNREGISTER_TABLE_$SP](Procedure._FNDTN_UNREGISTER_TABLE_$SP.md) |  |
| /* Author | [: Ian Kendrick](Author._Ian_Kendrick.md) |  |
| /* Date | [: 25 Feb 2005](Date._25_Feb_2005.md) |  |
| /* Purpose | [: Unregister a table created for a session with foundation](Purpose._Unregister_a_table_created_for_a_session_with_foundation.md) |  |
| dbo | [get_clndr_chld_cnt_$sp](dbo.get_clndr_chld_cnt_$sp.md) | dbo.CLNDR_TMPLT_ALGRTHM |
| dbo | [get_clndr_chld_lbl_$sp](dbo.get_clndr_chld_lbl_$sp.md) | dbo.CLNDR_LVL_TYPE, dbo.CLNDR_MNTH_LANG, dbo.CLNDR_TMPLT_ALGRTHM |
| Tokens understood by procedure : | [[CalendarStartDate]](Tokens_understood_by_procedure_._CalendarStartDate.md) |  |
| dbo | [mass_create_store_location_$sp](dbo.mass_create_store_location_$sp.md) | dbo.ADT_TRL_DTL, dbo.ADT_TRL_HDR, dbo.ADT_TRL_QRY, dbo.ORG_CHN_LOC, dbo.ORG_CHN_LOC_FNCTN, dbo.ORG_CHN_LOC_FNCTN_A, dbo.T_LONG_INTEGER, dbo.to_hex |
| Date | [Name           Def# Desc](Date.Name_Def#_Desc.md) |  |
| @function_list_length | [int,](@function_list_length.int,.md) |  |
| ORG_CHN_NUM | [int NOT NULL,  --T_LONG_INTEGER](ORG_CHN_NUM.int_NOT_NULL,_--T_LONG_INTEGER.md) |  |
| FNCTN_NUM | [int NOT NULL,  --T_LONG_INTEGER](FNCTN_NUM.int_NOT_NULL,_--T_LONG_INTEGER.md) |  |
| ENTRY_ID | [binary(16) NULL)](ENTRY_ID.binary_16_NULL.md) |  |
| dbo | [SCRTY_CHK_IS_GRP_IN_SET_$SP](dbo.SCRTY_CHK_IS_GRP_IN_SET_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A |
| 2010 0208 JHardin | [CRDM Merge renaming](2010_0208_JHardin.CRDM_Merge_renaming.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cosmetic cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cosmetic_cleanup.md) |  |
| dbo | [SCRTY_CHK_IS_SUBSET_$SP](dbo.SCRTY_CHK_IS_SUBSET_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SUBSET |
| Return Value: | [1 (True) -](Return_Value_.1_True_-.md) |  |
| Create Date: | [2011 0107](Create_Date_.2011_0107.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cosmetic cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cosmetic_cleanup.md) |  |
| dbo | [SCRTY_CHK_IS_SUBSET_PRPR_$SP](dbo.SCRTY_CHK_IS_SUBSET_PRPR_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A, dbo.ORG_CHN_HRCHY_LVL_GRP_SUBSET |
| Return Value: | [1 (True) -](Return_Value_.1_True_-.md) |  |
| Create Date: | [2010 1018](Create_Date_.2010_1018.md) |  |
| 2011 0110 JHardin | [RETURN the result as well as SELECTing it](2011_0110_JHardin.RETURN_the_result_as_well_as_SELECTing_it.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cleanup.md) |  |
| dbo | [SCRTY_GET_CMPLMNT_SET_ID_$SP](dbo.SCRTY_GET_CMPLMNT_SET_ID_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A, dbo.SCRTY_GET_SET_ID_$SP |
| Return Value: | [set id of A - B](Return_Value_.set_id_of_A_-_B.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cleanup.md) |  |
| dbo | [SCRTY_GET_GRPS_IN_SET_$SP](dbo.SCRTY_GET_GRPS_IN_SET_$SP.md) | dbo.ORG_CHN_HRCHY, dbo.ORG_CHN_HRCHY_APP, dbo.ORG_CHN_HRCHY_LVL, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.ORG_CHN_HRCHY_LVL_GRP_LANG, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A |
| 2010-02-08 JHardin | [CRDM Merge query changes - code is NOT specific to CRM app!](2010-02-08_JHardin.CRDM_Merge_query_changes_-_code_is_NOT_specific_to_CRM_app!.md) |  |
| 2012-05-07 WWilkie | [Updated to use config from ORG_CHN_HRCHY_APP table.](2012-05-07_WWilkie_Updated_to_use_config_from_ORG_CHN_HRCHY_APP_table..md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cosmetic cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cosmetic_cleanup.md) |  |
| dbo | [SCRTY_GET_INTRSCT_SET_ID_$SP](dbo.SCRTY_GET_INTRSCT_SET_ID_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A, dbo.SCRTY_GET_SET_ID_$SP |
| Return Value: | [set_id of intersection](Return_Value_.set_id_of_intersection.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cleanup.md) |  |
| dbo | [SCRTY_GET_SET_FMLY_ID_$SP](dbo.SCRTY_GET_SET_FMLY_ID_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_F_A, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_F_I, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_FMLY, dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP |
| Return Value: | [HRCHY_LVL_GRP_SET_FMLY_ID (a.k.a. division set family ID)](Return_Value_HRCHY_LVL_GRP_SET_FMLY_ID_a_k_a._division_set_family_ID.md) |  |
| 2012 0320 JHardin | [Maintain family_id = 0 (self-healing)](2012_0320_JHardin.Maintain_family_id_=_0_self-healing.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cleanup.md) |  |
| dbo | [SCRTY_GET_SET_ID_$SP](dbo.SCRTY_GET_SET_ID_$SP.md) | dbo.ORG_CHN_HRCHY_APP, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.ORG_CHN_HRCHY_LVL_GRP_SET, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A, dbo.ORG_CHN_HRCHY_LVL_GRP_SUBSET, dbo.SCRTY_GET_SET_FMLY_ID_$SP, dbo.SCRTY_MNT_POP_ALL_SUBSETS_$SP, dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP, dbo.SCRTY_MNT_POP_SET_SUBSETS_$SP |
| Return Value: | [HRCHY_LVL_GRP_SET_ID (a.k.a. division set ID)](Return_Value_HRCHY_LVL_GRP_SET_ID_a_k_a._division_set_ID.md) |  |
| 2009-03-30 WWilkie | [Misc cleanup.](2009-03-30_WWilkie_Misc_cleanup..md) |  |
| 2009-11-18 JHardin | [Misc cleanup, add population and maintenance of division_subset](2009-11-18_JHardin.Misc_cleanup,_add_population_and_maintenance_of_division_subset.md) |  |
| 2010-02-08 JHardin | [CRDM Merge query changes and major restructuring - code is NOT specific to CRM app!](2010-02-08_JHardin.CRDM_Merge_query_changes_and_major_restructuring_-_code_is_NOT_specific_to_CRM_app!.md) |  |
| 2010-11-17 JHardin | [Performance improvements](2010-11-17_JHardin.Performance_improvements.md) |  |
| 2011-03-10 JHardin | [Performance improvements](2011-03-10_JHardin.Performance_improvements.md) |  |
| 2011-07-29 JHardin | [Maintain membership of division_set_id = -1 (self-healing)](2011-07-29_JHardin.Maintain_membership_of_division_set_id_=_-1_self-healing.md) |  |
| 2011-09-01 WWilkie | [Added correct validation against ORG_CHN_HRCHY_APP table for division](2011-09-01_WWilkie.Added_correct_validation_against_ORG_CHN_HRCHY_APP_table_for_division.md) |  |
| 2012 0320 JHardin | [Maintain division_set_id = 0 (self-healing)](2012_0320_JHardin.Maintain_division_set_id_=_0_self-healing.md) |  |
| 2012 0424 JHardin | [Restore user divsec restriction to optimized query path](2012_0424_JHardin.Restore_user_divsec_restriction_to_optimized_query_path.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cleanup.md) |  |
| dbo | [SCRTY_GET_USER_SET_ID_$SP](dbo.SCRTY_GET_USER_SET_ID_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A, dbo.SCRTY_ACS_HRCHY_LVL_GRP_SET, dbo.SCRTY_GET_SET_ID_$SP |
| Return Value: | [HRCHY_LVL_GRP_SET_ID (a.k.a. division set ID)](Return_Value_HRCHY_LVL_GRP_SET_ID_a_k_a._division_set_ID.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cleanup.md) |  |
| -- | [PRINT 'generated division list: "' + @scratchDivisionList + '"';](--.PRINT_'generated_division_list_'_+_@scratchDivisionList_+_'_';.md) |  |
| dbo | [SCRTY_MNT_POP_ALL_SUBSETS_$SP](dbo.SCRTY_MNT_POP_ALL_SUBSETS_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET, dbo.SCRTY_MNT_POP_SET_SUBSETS_$SP |
| 2012 0613 JHardin | [CRDM merge final renaming, cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cleanup.md) |  |
| dbo | [SCRTY_MNT_POP_FMLY_INTRSCT_$SP](dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_F_A, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_F_I, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_FMLY |
| Return Value: | [nonzero on error](Return_Value_.nonzero_on_error.md) |  |
| dbo | [SCRTY_MNT_POP_SET_SUBSETS_$SP](dbo.SCRTY_MNT_POP_SET_SUBSETS_$SP.md) | dbo.ORG_CHN_HRCHY_LVL_GRP_SET, dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A, dbo.ORG_CHN_HRCHY_LVL_GRP_SUBSET |
| Return Value: | [none](Return_Value_.none.md) |  |
| 2012 0613 JHardin | [CRDM merge final renaming, cleanup](2012_0613_JHardin.CRDM_merge_final_renaming,_cleanup.md) |  |
| 2013 0221 JHardin | [If the division set is the set of all divisions, the -1 division set is an improper subset](2013_0221_JHardin.If_the_division_set_is_the_set_of_all_divisions,_the_-1_division_set_is_an_improper_subset.md) |  |
| dbo | [sp_alterdiagram](dbo.sp_alterdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_creatediagram](dbo.sp_creatediagram.md) | dbo.sysdiagrams |
| dbo | [sp_dropdiagram](dbo.sp_dropdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_EA_Order_Purge](dbo.sp_EA_Order_Purge.md) | dbo.SP_ORDER_PURGE_by_orderid |
| dbo | [sp_helpdiagramdefinition](dbo.sp_helpdiagramdefinition.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagrams](dbo.sp_helpdiagrams.md) | dbo.sysdiagrams |
| dbo | [SP_ORDER_PURGE_by_orderid](dbo.SP_ORDER_PURGE_by_orderid.md) | esell.SP_ORDER_ARCHIVE_PURGE |
| dbo | [sp_renamediagram](dbo.sp_renamediagram.md) | dbo.sysdiagrams |
| dbo | [sp_upgraddiagrams](dbo.sp_upgraddiagrams.md) | dbo.dtproperties, dbo.sysdiagrams |
| dbo | [spES_Aged_Orders_Check](dbo.spES_Aged_Orders_Check.md) | dbo.notification_history, dbo.sp_send_dbmail, esell.batch_order_status, esell.order_state |
| -- Description: | [Checks for ES orders older than 30 days and notifies via email accordingly](--_Description_.Checks_for_ES_orders_older_than_30_days_and_notifies_via_email_accordingly.md) |  |
| dbo | [spES_Rejected_Files_Check](dbo.spES_Rejected_Files_Check.md) | dbo.notification_history, dbo.sp_send_dbmail |
| -- Description: | [Checks for rejected ES files & notifies via email accordingly](--_Description_.Checks_for_rejected_ES_files_&_notifies_via_email_accordingly.md) |  |
| dbo | [spMergeEnterpriseSellingStoreOrderQty](dbo.spMergeEnterpriseSellingStoreOrderQty.md) | dbo.StoreOrderQtyStage, dbo.WebToESInventoryUpdateLog, esell.outlet_sku_xref, esell.sku |
| -- | [Dan Tweedie](--.Dan_Tweedie.md) |  |
| dbo | [spMergeEnterpriseSellingWebOrderQty](dbo.spMergeEnterpriseSellingWebOrderQty.md) | dbo.WebOrderQtyStage, dbo.WebToESInventoryUpdateLog, esell.outlet_sku_xref, esell.sku |
| -- | [Dan Tweedie](--.Dan_Tweedie.md) |  |
| dbo | [spSelectEnterpriseSellingInventory](dbo.spSelectEnterpriseSellingInventory.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.Style, dbo.vwWebHierarchy, dbo.vwWebIncludedStyles, dbo.vwWebLocations, dbo.WebInventoryStage, dbo.WebProductCatalogMasterAttributes, esell.outlet_sku_xref, esell.sku |
| --2018-02-08 - | [Dan Tweedie](--2018-02-08_-.Dan_Tweedie.md) |  |
| --2018-08-17 | [Dan Tweedie](--2018-08-17.Dan_Tweedie.md) |  |
| dbo | [spSelectEnterpriseSellingStoreInventory](dbo.spSelectEnterpriseSellingStoreInventory.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.location, dbo.StoreInventoryStage, dbo.Style, dbo.vwWebHierarchy, dbo.vwWebIncludedStyles, dbo.vwWebLocations, dbo.WebProductCatalogMasterAttributes, esell.outlet_sku_xref, esell.sku |
| --Dan Tweedie | [2020-04-09](--Dan_Tweedie.2020-04-09.md) |  |
| --Dan Tweedie | [2020-08-05](--Dan_Tweedie.2020-08-05.md) |  |
| dbo | [spSelectEnterpriseSellingStoreInventory_BACKUP20200805](dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.StoreInventoryStage, dbo.Style, dbo.vwWebHierarchy, dbo.vwWebIncludedStyles, dbo.vwWebLocations, dbo.WebProductCatalogMasterAttributes, esell.outlet_sku_xref, esell.sku |
| --Dan Tweedie | [2020-04-09](--Dan_Tweedie.2020-04-09.md) |  |
| dbo | [spSelectEnterpriseSellingStoreInventoryBAK20220711](dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.location, dbo.StoreInventoryStage, dbo.Style, dbo.vwWebHierarchy, dbo.vwWebIncludedStyles, dbo.vwWebLocations, dbo.WebProductCatalogMasterAttributes, esell.outlet_sku_xref, esell.sku |
| --Dan Tweedie | [2020-04-09](--Dan_Tweedie.2020-04-09.md) |  |
| --Dan Tweedie | [2020-08-05](--Dan_Tweedie.2020-08-05.md) |  |
| dbo | [spUpdateDigitalSoundsInfiniteInventory](dbo.spUpdateDigitalSoundsInfiniteInventory.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.hierarchy_group, dbo.location, dbo.style, dbo.style_group, esell.outlet_sku_xref, esell.sku |
| -- | [2019-9-20](--.2019-9-20.md) |  |
| -- | [2020-08-04](--.2020-08-04.md) |  |
| -- | [2021-07-19](--.2021-07-19.md) |  |
| dbo | [spUpdateDigitalSoundsInfiniteInventory_BACKUP20200805](dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20200805.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.hierarchy_group, dbo.style, dbo.style_group, esell.outlet_sku_xref, esell.sku |
| -- | [2019-9-20](--.2019-9-20.md) |  |
| -- | [2020-08-04](--.2020-08-04.md) |  |
| dbo | [spUpdateDigitalSoundsInfiniteInventory_BACKUP20210719](dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20210719.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.hierarchy_group, dbo.location, dbo.style, dbo.style_group, esell.outlet_sku_xref, esell.sku |
| -- | [2019-9-20](--.2019-9-20.md) |  |
| -- | [2020-08-04](--.2020-08-04.md) |  |
| esell | [GETFULFILLMENTRATES](esell.GETFULFILLMENTRATES.md) | dbo.batch_fulfillment_rates, dbo.fGetDelimitedAttributeValues, dbo.fGetDelimitedLocationValues, dbo.GETHIERARCHYLOCATIONLIST, dbo.GETLOCATIONATTRIBUTELIST, dbo.ORG_CHN_HRCHY_LVL, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.ORG_CHN_HRCHY_LVL_GRP_A |
| esell | [GETHIERARCHYLOCATIONLIST](esell.GETHIERARCHYLOCATIONLIST.md) | esell.fGetLocationAttributeIds |
| esell | [GETLOCATIONATTRIBUTELIST](esell.GETLOCATIONATTRIBUTELIST.md) | esell.fGetLocationAttributeIds |
| esell | [GETNOSTOCKREPORT](esell.GETNOSTOCKREPORT.md) | dbo.batch_no_stock, dbo.batch_no_stock_t_location, dbo.event_reason, dbo.fGetDelimitedAttributeValues, dbo.fGetDelimitedLocationValues, dbo.fGetDelimitedNoStockReasonIds, dbo.GETHIERARCHYLOCATIONLIST, dbo.GETLOCATIONATTRIBUTELIST, dbo.ORG_CHN_HRCHY_LVL, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.Org_Chn_Hrchy_Lvl_Grp_A |
| esell | [GETNOSTOCKREPORTLOCATION](esell.GETNOSTOCKREPORTLOCATION.md) | dbo.batch_no_stock_location, dbo.batch_no_stock_t_location, dbo.fGetDelimitedAttributeValues, dbo.fGetDelimitedLocationValues, dbo.fGetDelimitedNoStockReasonIds, dbo.GETHIERARCHYLOCATIONLIST, dbo.GETLOCATIONATTRIBUTELIST, dbo.Org_Chn_Hrchy_Lvl, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.Org_Chn_Hrchy_Lvl_Grp_A |
| esell | [GETORDERSTATUSREPORT](esell.GETORDERSTATUSREPORT.md) | dbo.batch_order_status, dbo.fGetDelimitedAttributeValues, dbo.fGetDelimitedLocationValues, dbo.fGetDelimitedOrderStatuses, dbo.GETHIERARCHYLOCATIONLIST, dbo.GETLOCATIONATTRIBUTELIST, dbo.order_state, dbo.ORG_CHN_HRCHY_LVL, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.ORG_CHN_HRCHY_LVL_GRP_A |
| esell | [GETORDERSTATUSREPORTLOCATION](esell.GETORDERSTATUSREPORTLOCATION.md) | dbo.batch_order_status, dbo.fGetDelimitedAttributeValues, dbo.fGetDelimitedLocationValues, dbo.fGetDelimitedOrderStatuses, dbo.GETHIERARCHYLOCATIONLIST, dbo.GETLOCATIONATTRIBUTELIST, dbo.ORG_CHN_HRCHY_LVL, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.ORG_CHN_HRCHY_LVL_GRP_A |
| esell | [GETORDERSUMMARY](esell.GETORDERSUMMARY.md) | dbo.batch_order_summary, dbo.fGetDelimitedAttributeValues, dbo.fGetDelimitedLocationValues, dbo.GETHIERARCHYLOCATIONLIST, dbo.GETLOCATIONATTRIBUTELIST, dbo.ORG_CHN_HRCHY_LVL, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.ORG_CHN_HRCHY_LVL_GRP_A |
| esell | [GETSKUDEMANDREPORT](esell.GETSKUDEMANDREPORT.md) | dbo.batch_sku_demand, dbo.fGetDelimitedAttributeValues, dbo.fGetDelimitedLocationValues, dbo.GETHIERARCHYLOCATIONLIST, dbo.GETLOCATIONATTRIBUTELIST, dbo.ORG_CHN_HRCHY_LVL, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.ORG_CHN_HRCHY_LVL_GRP_A, dbo.sku |
| esell | [GETSKUDEMANDREPORTLOCATION](esell.GETSKUDEMANDREPORTLOCATION.md) | dbo.batch_sku_demand, dbo.fGetDelimitedAttributeValues, dbo.fGetDelimitedLocationValues, dbo.GETHIERARCHYLOCATIONLIST, dbo.GETLOCATIONATTRIBUTELIST, dbo.ORG_CHN_HRCHY_LVL, dbo.ORG_CHN_HRCHY_LVL_GRP, dbo.ORG_CHN_HRCHY_LVL_GRP_A |
| esell | [POPULATEFULFILLMENTRATES](esell.POPULATEFULFILLMENTRATES.md) | dbo.batch_fulfillment_rates_bak, dbo.order_fulfillment, dbo.order_state, dbo.ORDERS |
| esell | [POPULATENOSTOCKREPORT](esell.POPULATENOSTOCKREPORT.md) | dbo.batch_no_stock_bak, dbo.event_reason, dbo.order_fulfillment, dbo.order_line_item, dbo.orders, dbo.sku |
| esell | [POPULATENOSTOCKREPORTLOCATION](esell.POPULATENOSTOCKREPORTLOCATION.md) | dbo.batch_no_stock_location_bak, dbo.batch_no_stock_t_location_bak, dbo.event_reason, dbo.order_fulfillment, dbo.order_line_item, dbo.orders, dbo.sku |
| esell | [POPULATEORDERSTATUS](esell.POPULATEORDERSTATUS.md) | dbo.batch_order_status_bak, dbo.order_fulfillment, dbo.order_fulfillment_extn, dbo.order_line_item, dbo.ORDER_STATE, dbo.orders, dbo.Route_History |
| esell | [POPULATEORDERSUMMARY](esell.POPULATEORDERSUMMARY.md) | dbo.batch_order_summary_bak, dbo.event_reason, dbo.order_line_item, dbo.order_state, dbo.ORDERS |
| esell | [POPULATESKUDEMAND](esell.POPULATESKUDEMAND.md) | dbo.batch_sku_demand_bak, dbo.order_line_item, dbo.orders, dbo.outlet_query_log, dbo.sku |
| esell | [SP_ORDER_ARCHIVE_PURGE](esell.SP_ORDER_ARCHIVE_PURGE.md) |  |
| esell | [SP_ORDER_PURGE](esell.SP_ORDER_PURGE.md) | dbo.SP_ORDER_ARCHIVE_PURGE |
| esell | [SP_ORDER_PURGE_BJB](esell.SP_ORDER_PURGE_BJB.md) | esell.SP_ORDER_ARCHIVE_PURGE |
| esell | [sp_purge_df_tables](esell.sp_purge_df_tables.md) | dbo.zone_group_xref |
| esell | [SP_VERIFY_DFT_COLUMNS](esell.SP_VERIFY_DFT_COLUMNS.md) | dbo.data_validation_log |
