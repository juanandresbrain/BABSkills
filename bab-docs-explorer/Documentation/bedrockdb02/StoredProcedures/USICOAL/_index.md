# Stored Procedures: USICOAL

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [BI_GET_MAX_ID](dbo.BI_GET_MAX_ID.md) | dbo.RETAIL_TRANSACTION |
| dbo | [BI_GET_SALES](dbo.BI_GET_SALES.md) | dbo.ITEM_TAX_AUTH, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [DC_BOOK_PRC_CHG](dbo.DC_BOOK_PRC_CHG.md) | dbo.ITEM_QUANTITY, dbo.PRICE_CHANGE, dbo.PRICE_CHANGE_ITEM, dbo.TMP_PRC_CHANGE |
| * | [This procedure books dataconnect price changes.](This_procedure_books_dataconnect_price_changes..md) |  |
| * | [@PRM_PRC_CHG_ID - price change id](.@PRM_PRC_CHG_ID_-_price_change_id.md) |  |
| * | [@PRM_STORE_NO - store number](.@PRM_STORE_NO_-_store_number.md) |  |
| * | [@PRM_PRC_CHG_NO - price change number](.@PRM_PRC_CHG_NO_-_price_change_number.md) |  |
| * | [@LOCAL_FLG - local price change flag](.@LOCAL_FLG_-_local_price_change_flag.md) |  |
| * | [exec DC_BOOK_PRC_CHG 15, 123](.exec_DC_BOOK_PRC_CHG_15,_123.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if price booking failed.](1_if_price_booking_failed..md) |  |
| * | [Stock ledger account records are updated separately.](Stock_ledger_account_records_are_updated_separately..md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| * | [7/25/00 (L. Rubakhin) - Added population of](7_25_00_L._Rubakhin_-_Added_population_of.md) |  |
| * | [10/23/00 (L. Rubakhin) - Processed case where there is no price change items](10_23_00_L._Rubakhin_-_Processed_case_where_there_is_no_price_change_items.md) |  |
| * | [12/14/01 (L. Rubakhin) - Added filter by store number](12_14_01_L._Rubakhin_-_Added_filter_by_store_number.md) |  |
| * | [07/28/15 (S. Mouras) - Move the check for matching store number to the LEFT OUTER JOIN clause instead of the WHERE clause so that if there is no matching item with the local store number in ITEM_QUANTITY the record still gets added to PRICE_CHANGE_ITEM, only with a zero quantity.](07_28_15_S_Mouras_-_Move_the_check_for_matching_store_number_to_the_LEFT_OUTER_JOIN_clause_instead_of_the_WHERE_clause_so_that_if_there_is_no_matching_item_with_the_local_store_number_in_ITEM_QUANTITY_the_record_still_gets_added_to_PRICE_CHANGE_ITEM,_only_with_a_zero_quantity..md) |  |
| dbo | [DC_CALC_PRC_CHG](dbo.DC_CALC_PRC_CHG.md) | dbo.DC_PRC_CHG_ITEM, dbo.ITEM, dbo.PRICE_CHANGE, dbo.STORE_ITEM, dbo.TMP_PRC_CHANGE |
| * | [This procedure calcs and stores all price changes into TMP_PRC_CHANGE](.This_procedure_calcs_and_stores_all_price_changes_into_TMP_PRC_CHANGE.md) |  |
| * | [@PRM_GLBL_PRC - 1 global price dominates local](.@PRM_GLBL_PRC_-_1_global_price_dominates_local.md) |  |
| * | [@PRM_PRC_CHG_ID - price change id](.@PRM_PRC_CHG_ID_-_price_change_id.md) |  |
| * | [@PRM_STORE_NO - store number](.@PRM_STORE_NO_-_store_number.md) |  |
| * | [exec DC_PRC_CHANGE 0, 1, 123](.exec_DC_PRC_CHANGE_0,_1,_123.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [11/01/01 (L. Rubakhin) - Created](11_01_01_L._Rubakhin_-_Created.md) |  |
| * | [1/2/03 (O. Blevins)](1_2_03_O._Blevins.md) |  |
| * | [07/08/04 (L. Rubakhin) - added support for local permanent prices](07_08_04_L._Rubakhin_-_added_support_for_local_permanent_prices.md) |  |
| dbo | [DC_CHK_ITM_REF_INTGR](dbo.DC_CHK_ITM_REF_INTGR.md) | dbo.CATEGORY, dbo.CLASS, dbo.COLOR, dbo.DC_ITEM, dbo.DEPARTMENT, dbo.LIFE_STYLE, dbo.SEASON, dbo.SIZE, dbo.SPIFF_DEFINITION, dbo.STYLE, dbo.SUB_CATEGORY, dbo.SUB_CLASS, dbo.SUB_DEPARTMENT |
| * | [This procedure checks referencial integrity of some](.This_procedure_checks_referencial_integrity_of_some.md) |  |
| * | [data supplied via dataconnect.](data_supplied_via_dataconnect..md) |  |
| * | [@PRM_DIV](.@PRM_DIV.md) |  |
| * | [exec DC_CHK_ITM_REF_INTGR 0](.exec_DC_CHK_ITM_REF_INTGR_0.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns the result set:](.This_procedure_returns_the_result_set.md) |  |
| * | [DEPT_ERR, SUB_DEPT_ERR, CATEGORY_ERR, SUB_CATEGORY_ERR, CLASS_ERR,](.DEPT_ERR,_SUB_DEPT_ERR,_CATEGORY_ERR,_SUB_CATEGORY_ERR,_CLASS_ERR,.md) |  |
| * | [SUB_CLASS_ERR, SEASON_ERR, SIZE_ERR, COLOR_ERR, STYLE_ERR, LIFE_STYLE_ERR, SPIFF_ERR](.SUB_CLASS_ERR,_SEASON_ERR,_SIZE_ERR,_COLOR_ERR,_STYLE_ERR,_LIFE_STYLE_ERR,_SPIFF_ERR.md) |  |
| * | [This result set has only one record that shows the](.This_result_set_has_only_one_record_that_shows_the.md) |  |
| * | [number of errors related to the corresponding entity.](number_of_errors_related_to_the_corresponding_entity..md) |  |
| * | [3/16/00 (L. Rubakhin) - Created](3_16_00_L._Rubakhin_-_Created.md) |  |
| * | [10/18/00 (L. Rubakhin) - Added SPIFF](10_18_00_L._Rubakhin_-_Added_SPIFF.md) |  |
| dbo | [DC_CHK_ZIP_CODE_TAX_ZONE_OVRLP](dbo.DC_CHK_ZIP_CODE_TAX_ZONE_OVRLP.md) | dbo.TMP_ZIP_CODE_TAX_ZONE |
| dbo | [DC_CRT_DC_EQUAL_TAX_ZONE](dbo.DC_CRT_DC_EQUAL_TAX_ZONE.md) |  |
| * | [This procedure creates DC_EQUAL_TAX_ZONE table.](This_procedure_creates_DC_EQUAL_TAX_ZONE_table..md) |  |
| * | [DC_CRT_DC_EQUAL_TAX_ZONE](.DC_CRT_DC_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_EQUAL_TAX_ZONE_LANG](dbo.DC_CRT_DC_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [This procedure creates DC_EQUAL_TAX_ZONE_LANG table.](This_procedure_creates_DC_EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [DC_CRT_DC_EQUAL_TAX_ZONE_LANG](.DC_CRT_DC_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAX_AUTHORITY](dbo.DC_CRT_DC_TAX_AUTHORITY.md) |  |
| * | [This procedure creates DC_TAX_AUTHORITY table.](This_procedure_creates_DC_TAX_AUTHORITY_table..md) |  |
| * | [DC_CRT_DC_TAX_AUTHORITY](.DC_CRT_DC_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAX_AUTHORITY_LANG](dbo.DC_CRT_DC_TAX_AUTHORITY_LANG.md) |  |
| * | [This procedure creates DC_TAX_AUTHORITY_LANG table.](This_procedure_creates_DC_TAX_AUTHORITY_LANG_table..md) |  |
| * | [DC_CRT_DC_TAX_AUTHORITY_LANG](.DC_CRT_DC_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAX_EXEMPT_CERT](dbo.DC_CRT_DC_TAX_EXEMPT_CERT.md) |  |
| * | [This procedure creates DC_TAX_EXEMPT_CERT table.](This_procedure_creates_DC_TAX_EXEMPT_CERT_table..md) |  |
| * | [DC_CRT_DC_TAX_EXEMPT_CERT](.DC_CRT_DC_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAX_GRP_ZONE_AUTH](dbo.DC_CRT_DC_TAX_GRP_ZONE_AUTH.md) |  |
| * | [This procedure creates DC_TAX_GRP_ZONE_AUTH table.](This_procedure_creates_DC_TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [DC_CRT_DC_TAX_GRP_ZONE_AUTH](.DC_CRT_DC_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAX_RULE](dbo.DC_CRT_DC_TAX_RULE.md) |  |
| * | [This procedure creates DC_TAX_RULE table.](This_procedure_creates_DC_TAX_RULE_table..md) |  |
| * | [DC_CRT_DC_TAX_RULE](.DC_CRT_DC_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAX_RULE_LANG](dbo.DC_CRT_DC_TAX_RULE_LANG.md) |  |
| * | [This procedure creates DC_TAX_RULE_LANG table.](This_procedure_creates_DC_TAX_RULE_LANG_table..md) |  |
| * | [DC_CRT_DC_TAX_RULE_LANG](.DC_CRT_DC_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAX_SCHEDULE](dbo.DC_CRT_DC_TAX_SCHEDULE.md) |  |
| * | [This procedure creates DC_TAX_SCHEDULE table.](This_procedure_creates_DC_TAX_SCHEDULE_table..md) |  |
| * | [DC_CRT_DC_TAX_SCHEDULE](.DC_CRT_DC_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAX_ZONE_TAX_AUTH](dbo.DC_CRT_DC_TAX_ZONE_TAX_AUTH.md) |  |
| * | [This procedure creates DC_TAX_ZONE_TAX_AUTH table.](This_procedure_creates_DC_TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [DC_CRT_DC_TAX_ZONE_TAX_AUTH](.DC_CRT_DC_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAXABLE_ITEM_GRP](dbo.DC_CRT_DC_TAXABLE_ITEM_GRP.md) |  |
| * | [This procedure creates DC_TAXABLE_ITEM_GRP table.](This_procedure_creates_DC_TAXABLE_ITEM_GRP_table..md) |  |
| * | [DC_CRT_DC_TAXABLE_ITEM_GRP](.DC_CRT_DC_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_TAXABLE_ITEM_GRP_LANG](dbo.DC_CRT_DC_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [This procedure creates DC_TAXABLE_ITEM_GRP_LANG table.](This_procedure_creates_DC_TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [DC_CRT_DC_TAXABLE_ITEM_GRP_LANG](.DC_CRT_DC_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_VALUE_ADDED_TAX](dbo.DC_CRT_DC_VALUE_ADDED_TAX.md) |  |
| * | [This procedure creates DC_VALUE_ADDED_TAX table.](This_procedure_creates_DC_VALUE_ADDED_TAX_table..md) |  |
| * | [DC_CRT_DC_VALUE_ADDED_TAX](.DC_CRT_DC_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_VALUE_ADDED_TAX_LANG](dbo.DC_CRT_DC_VALUE_ADDED_TAX_LANG.md) |  |
| * | [This procedure creates DC_VALUE_ADDED_TAX_LANG table.](This_procedure_creates_DC_VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [DC_CRT_DC_VALUE_ADDED_TAX_LANG](.DC_CRT_DC_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_DC_ZIP_CODE_TAX_ZONE](dbo.DC_CRT_DC_ZIP_CODE_TAX_ZONE.md) |  |
| * | [This procedure creates DC_ZIP_CODE_TAX_ZONE table.](This_procedure_creates_DC_ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [DC_CRT_DC_ZIP_CODE_TAX_ZONE](.DC_CRT_DC_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_EQUAL_TAX_ZONE](dbo.DC_CRT_TMP_EQUAL_TAX_ZONE.md) |  |
| * | [This procedure creates TMP_EQUAL_TAX_ZONE table.](This_procedure_creates_TMP_EQUAL_TAX_ZONE_table..md) |  |
| * | [DC_CRT_TMP_EQUAL_TAX_ZONE](.DC_CRT_TMP_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_EQUAL_TAX_ZONE_LANG](dbo.DC_CRT_TMP_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [This procedure creates TMP_EQUAL_TAX_ZONE_LANG table.](This_procedure_creates_TMP_EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [DC_CRT_TMP_EQUAL_TAX_ZONE_LANG](.DC_CRT_TMP_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_ITM](dbo.DC_CRT_TMP_ITM.md) |  |
| * | [This procedure creates temporary tables to become new item tables:](.This_procedure_creates_temporary_tables_to_become_new_item_tables.md) |  |
| * | [TMP_ITEM, TMP_STORE_ITEM, TMP_ITEM_POS_SELL_RULE, TMP_ITEM_KEYWORD,](.TMP_ITEM,_TMP_STORE_ITEM,_TMP_ITEM_POS_SELL_RULE,_TMP_ITEM_KEYWORD,.md) |  |
| * | [TMP_ITEM_ADDL_INFO.  It also creates temporary table to store price](TMP_ITEM_ADDL_INFO._It_also_creates_temporary_table_to_store_price.md) |  |
| * | [changes.](changes..md) |  |
| * | [exec DC_CRT_TMP_ITM](.exec_DC_CRT_TMP_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure creates temporary item related tables that are based](.This_procedure_creates_temporary_item_related_tables_that_are_based.md) |  |
| * | [on real item tables.](on_real_item_tables..md) |  |
| * | [3/14/00 (L. Rubakhin) - Created](3_14_00_L._Rubakhin_-_Created.md) |  |
| * | [4/26/00 (L. Rubakhin) - Replaced SELECT INTO by CREATE TABLE](4_26_00_L._Rubakhin_-_Replaced_SELECT_INTO_by_CREATE_TABLE.md) |  |
| * | [10/19/00 (L. Rubakhin) - TMP_ITEM_POS_SELL_RULE SPIFF_ID instead of SPIFF_AMOUNT,](10_19_00_L._Rubakhin_-_TMP_ITEM_POS_SELL_RULE_SPIFF_ID_instead_of_SPIFF_AMOUNT,.md) |  |
| * | [5/31/01 (L. Rubakhin) - Modified datatype of ITEM_WASTE_FCTR to T_DEC_NUMBER](5_31_01_L._Rubakhin_-_Modified_datatype_of_ITEM_WASTE_FCTR_to_T_DEC_NUMBER.md) |  |
| * | [8/9/01 (L. Rubakhin) - Added association group](8_9_01_L._Rubakhin_-_Added_association_group.md) |  |
| * | [10/17/01 (L. Rubakhin) - Added activate flag, tender type id](10_17_01_L._Rubakhin_-_Added_activate_flag,_tender_type_id.md) |  |
| * | [10/31/01 (L. Rubakhin) - replaced alert with tender info](10_31_01_L._Rubakhin_-_replaced_alert_with_tender_info.md) |  |
| * | [10/31/01 (L. Rubakhin) - replaced alert with tender info](10_31_01_L._Rubakhin_-_replaced_alert_with_tender_info.md) |  |
| * | [12/03/04 (L. Rubakhin) - added [dbo] prefix to [TMP_ITEM_ADDL_INFO] table](12_03_04_L._Rubakhin_-_added_dbo_prefix_to_TMP_ITEM_ADDL_INFO_table.md) |  |
| * | [3/24/05 (L. Rubakhin) - Added buy back price, defective item action code,](3_24_05_L._Rubakhin_-_Added_buy_back_price,_defective_item_action_code,.md) |  |
| * | [9/27/05 (L. Rubakhin) - Added CIRCUMSTANCE_NO and ITEM_GROUP_ID to POS_ITEM_ADDL_INFO](9_27_05_L._Rubakhin_-_Added_CIRCUMSTANCE_NO_and_ITEM_GROUP_ID_to_POS_ITEM_ADDL_INFO.md) |  |
| * | [2/18/07 (L. Rubakhin) - Added Unicode support](2_18_07_L._Rubakhin_-_Added_Unicode_support.md) |  |
| * | [9/25/09 (L. Rubakhin) - Extended ITEM_NO, PLU_CODE and POS_ITEM_NO](9_25_09_L._Rubakhin_-_Extended_ITEM_NO,_PLU_CODE_and_POS_ITEM_NO.md) |  |
| * | [10/21/14 (L. Rubakhin) - Added INVOICEABLE_FLG](10_21_14_L._Rubakhin_-_Added_INVOICEABLE_FLG.md) |  |
| * | [2/29/15 (O. Blevins) - Restored LOYALTY_DSCNT_FLG](2_29_15_O._Blevins_-_Restored_LOYALTY_DSCNT_FLG.md) |  |
| dbo | [DC_CRT_TMP_PLU](dbo.DC_CRT_TMP_PLU.md) |  |
| * | [This procedure creates TMP_PLU and TMP_POS_ID_PLU_CODE tables.](This_procedure_creates_TMP_PLU_and_TMP_POS_ID_PLU_CODE_tables..md) |  |
| * | [exec DC_CRT_TMP_PLU](.exec_DC_CRT_TMP_PLU.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| * | [4/4/00 (L. Rubakhin) - Added creation of TMP_POS_ITEM_ALERT](4_4_00_L._Rubakhin_-_Added_creation_of_TMP_POS_ITEM_ALERT.md) |  |
| * | [4/26/00 (L. Rubakhin) - Replaced SELECT INTO by CREATE TABLE](4_26_00_L._Rubakhin_-_Replaced_SELECT_INTO_by_CREATE_TABLE.md) |  |
| * | [10/19/00 (L. Rubakhin) - Replaced field SPIFF_AMOUNT by SPIFF_TYPE_CODE, SPIFF_PCT, SPIFF_AMT](10_19_00_L._Rubakhin_-_Replaced_field_SPIFF_AMOUNT_by_SPIFF_TYPE_CODE,_SPIFF_PCT,_SPIFF_AMT.md) |  |
| * | [5/31/01 (L. Rubakhin) - Replaced field datatype of SEASON_CODE from T_CODE2 to T_CODE4](5_31_01_L._Rubakhin_-_Replaced_field_datatype_of_SEASON_CODE_from_T_CODE2_to_T_CODE4.md) |  |
| * | [10/18/01 (L. Rubakhin) - Added fields to PLU table](10_18_01_L._Rubakhin_-_Added_fields_to_PLU_table.md) |  |
| * | [10/29/01 (L. Rubakhin) - Replaced alert with additional info](10_29_01_L._Rubakhin_-_Replaced_alert_with_additional_info.md) |  |
| * | [11/20/02 (L. Rubakhin) - Added 6 new fields to PLU file](11_20_02_L._Rubakhin_-_Added_6_new_fields_to_PLU_file.md) |  |
| * | [02/09/04 (L. Rubakhin) - Added 5 new fields to PLU file](02_09_04_L._Rubakhin_-_Added_5_new_fields_to_PLU_file.md) |  |
| * | [07/07/04 (L. Rubakhin) - Added ITEM_DESC field to PLU table](07_07_04_L._Rubakhin_-_Added_ITEM_DESC_field_to_PLU_table.md) |  |
| * | [3/24/05 (L. Rubakhin) - Added buy back price, defective item action code,](3_24_05_L._Rubakhin_-_Added_buy_back_price,_defective_item_action_code,.md) |  |
| * | [9/27/05 (L. Rubakhin) - Added CIRCUMSTANCE_NO and ITEM_GROUP_ID to POS_ITEM_ADDL_INFO](9_27_05_L._Rubakhin_-_Added_CIRCUMSTANCE_NO_and_ITEM_GROUP_ID_to_POS_ITEM_ADDL_INFO.md) |  |
| * | [2/18/07 (L. Rubakhin) - Added Unicode support](2_18_07_L._Rubakhin_-_Added_Unicode_support.md) |  |
| * | [9/25/09 (L. Rubakhin) - Extended PLU_CODE](9_25_09_L._Rubakhin_-_Extended_PLU_CODE.md) |  |
| * | [3/18/11 (L. Rubakhin) - Added COST](3_18_11_L._Rubakhin_-_Added_COST.md) |  |
| * | [6/15/12 (L. Rubakhin) - increased size of STYLE_CODE to varchar(30)](6_15_12_L._Rubakhin_-_increased_size_of_STYLE_CODE_to_varchar_30.md) |  |
| * | [10/21/14 (L. Rubakhin) - Added INVOICEABLE_FLG](10_21_14_L._Rubakhin_-_Added_INVOICEABLE_FLG.md) |  |
| * | [2/29/15 (O. Blevins) - Restored LOYALTY_DSCNT_FLG](2_29_15_O._Blevins_-_Restored_LOYALTY_DSCNT_FLG.md) |  |
| dbo | [DC_CRT_TMP_PRC](dbo.DC_CRT_TMP_PRC.md) |  |
| * | [This procedure creates temporary table to store price changes.](This_procedure_creates_temporary_table_to_store_price_changes..md) |  |
| * | [exec DC_CRT_TMP_PRC](.exec_DC_CRT_TMP_PRC.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [11/01/01 (L. Rubakhin) - Created](11_01_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_CRT_TMP_SMPL_DISCNT](dbo.DC_CRT_TMP_SMPL_DISCNT.md) |  |
| * | [This procedure creates TMP_SIMPLE_DISCOUNT table.](This_procedure_creates_TMP_SIMPLE_DISCOUNT_table..md) |  |
| * | [DC_CRT_TMP_SMPL_DISCNT](.DC_CRT_TMP_SMPL_DISCNT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [1/8/02 (L. Rubakhin) - Created](1_8_02_L._Rubakhin_-_Created.md) |  |
| * | [2/7/02 (L. Rubakhin) - CREATION_DATETIME not null](2_7_02_L._Rubakhin_-_CREATION_DATETIME_not_null.md) |  |
| * | [2/18/07 (L. Rubakhin) - Added Unicode support](2_18_07_L._Rubakhin_-_Added_Unicode_support.md) |  |
| * | [9/25/09 (L. Rubakhin) - Extended ITEM_NO](9_25_09_L._Rubakhin_-_Extended_ITEM_NO.md) |  |
| dbo | [DC_CRT_TMP_STR_ITEM](dbo.DC_CRT_TMP_STR_ITEM.md) |  |
| * | [This procedure inserts and updates store items](.This_procedure_inserts_and_updates_store_items.md) |  |
| * | [in STORE_ITEM table.](in_STORE_ITEM_table..md) |  |
| * | [exec DC_CRT_TMP_STR_ITEM](.exec_DC_CRT_TMP_STR_ITEM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if price booking failed.](1_if_price_booking_failed..md) |  |
| * | [Stock ledger account records are updated separately.](Stock_ledger_account_records_are_updated_separately..md) |  |
| * | [2/18/07 (L. Rubakhin) - Added Unicode support](2_18_07_L._Rubakhin_-_Added_Unicode_support.md) |  |
| * | [9/25/09 (L. Rubakhin) - Extended ITEM_NO](9_25_09_L._Rubakhin_-_Extended_ITEM_NO.md) |  |
| dbo | [DC_CRT_TMP_TAX_AUTHORITY](dbo.DC_CRT_TMP_TAX_AUTHORITY.md) |  |
| * | [This procedure creates TMP_TAX_AUTHORITY table.](This_procedure_creates_TMP_TAX_AUTHORITY_table..md) |  |
| * | [DC_CRT_TMP_TAX_AUTHORITY](.DC_CRT_TMP_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAX_AUTHORITY_LANG](dbo.DC_CRT_TMP_TAX_AUTHORITY_LANG.md) |  |
| * | [This procedure creates TMP_TAX_AUTHORITY_LANG table.](This_procedure_creates_TMP_TAX_AUTHORITY_LANG_table..md) |  |
| * | [DC_CRT_TMP_TAX_AUTHORITY_LANG](.DC_CRT_TMP_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAX_EXEMPT_CERT](dbo.DC_CRT_TMP_TAX_EXEMPT_CERT.md) |  |
| * | [This procedure creates TMP_TAX_EXEMPT_CERT table.](This_procedure_creates_TMP_TAX_EXEMPT_CERT_table..md) |  |
| * | [DC_CRT_TMP_TAX_EXEMPT_CERT](.DC_CRT_TMP_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAX_GRP_ZONE_AUTH](dbo.DC_CRT_TMP_TAX_GRP_ZONE_AUTH.md) |  |
| * | [This procedure creates TMP_TAX_GRP_ZONE_AUTH table.](This_procedure_creates_TMP_TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [DC_CRT_TMP_TAX_GRP_ZONE_AUTH](.DC_CRT_TMP_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAX_RULE](dbo.DC_CRT_TMP_TAX_RULE.md) |  |
| * | [This procedure creates TMP_TAX_RULE table.](This_procedure_creates_TMP_TAX_RULE_table..md) |  |
| * | [DC_CRT_TMP_TAX_RULE](.DC_CRT_TMP_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAX_RULE_LANG](dbo.DC_CRT_TMP_TAX_RULE_LANG.md) |  |
| * | [This procedure creates TMP_TAX_RULE_LANG table.](This_procedure_creates_TMP_TAX_RULE_LANG_table..md) |  |
| * | [DC_CRT_TMP_TAX_RULE_LANG](.DC_CRT_TMP_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAX_SCHEDULE](dbo.DC_CRT_TMP_TAX_SCHEDULE.md) |  |
| * | [This procedure creates TMP_TAX_SCHEDULE table.](This_procedure_creates_TMP_TAX_SCHEDULE_table..md) |  |
| * | [DC_CRT_TMP_TAX_SCHEDULE](.DC_CRT_TMP_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAX_ZONE_TAX_AUTH](dbo.DC_CRT_TMP_TAX_ZONE_TAX_AUTH.md) |  |
| * | [This procedure creates TMP_TAX_ZONE_TAX_AUTH table.](This_procedure_creates_TMP_TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [DC_CRT_TMP_TAX_ZONE_TAX_AUTH](.DC_CRT_TMP_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAXABLE_ITEM_GRP](dbo.DC_CRT_TMP_TAXABLE_ITEM_GRP.md) |  |
| * | [This procedure creates TMP_TAXABLE_ITEM_GRP table.](This_procedure_creates_TMP_TAXABLE_ITEM_GRP_table..md) |  |
| * | [DC_CRT_TMP_TAXABLE_ITEM_GRP](.DC_CRT_TMP_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_TAXABLE_ITEM_GRP_LANG](dbo.DC_CRT_TMP_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [This procedure creates TMP_TAXABLE_ITEM_GRP_LANG table.](This_procedure_creates_TMP_TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [DC_CRT_TMP_TAXABLE_ITEM_GRP_LANG](.DC_CRT_TMP_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_UPC](dbo.DC_CRT_TMP_UPC.md) |  |
| * | [This procedure creates temporary TMP_POS_IDENTITY table.](This_procedure_creates_temporary_TMP_POS_IDENTITY_table..md) |  |
| * | [exec DC_CRT_TMP_UPC](.exec_DC_CRT_TMP_UPC.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/28/00 (L. Rubakhin) - Created](3_28_00_L._Rubakhin_-_Created.md) |  |
| * | [7/12/01 (L. Rubakhin) - Relaxed NOT NULL constraint for nonPK columns](7_12_01_L._Rubakhin_-_Relaxed_NOT_NULL_constraint_for_nonPK_columns.md) |  |
| * | [2/18/07 (L. Rubakhin) - Added Unicode support](2_18_07_L._Rubakhin_-_Added_Unicode_support.md) |  |
| * | [9/25/09 (L. Rubakhin) - Extended POS_ITEM_NO](9_25_09_L._Rubakhin_-_Extended_POS_ITEM_NO.md) |  |
| * | [3/21/16 (L. Rubakhin) - Made POS_ITEM_NO nvarchar](3_21_16_L._Rubakhin_-_Made_POS_ITEM_NO_nvarchar.md) |  |
| dbo | [DC_CRT_TMP_VALUE_ADDED_TAX](dbo.DC_CRT_TMP_VALUE_ADDED_TAX.md) |  |
| * | [This procedure creates TMP_VALUE_ADDED_TAX table.](This_procedure_creates_TMP_VALUE_ADDED_TAX_table..md) |  |
| * | [DC_CRT_TMP_VALUE_ADDED_TAX](.DC_CRT_TMP_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_VALUE_ADDED_TAX_LANG](dbo.DC_CRT_TMP_VALUE_ADDED_TAX_LANG.md) |  |
| * | [This procedure creates TMP_VALUE_ADDED_TAX_LANG table.](This_procedure_creates_TMP_VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [DC_CRT_TMP_VALUE_ADDED_TAX_LANG](.DC_CRT_TMP_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_CRT_TMP_ZIP_CODE_TAX_ZONE](dbo.DC_CRT_TMP_ZIP_CODE_TAX_ZONE.md) |  |
| * | [This procedure creates TMP_ZIP_CODE_TAX_ZONE table.](This_procedure_creates_TMP_ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [DC_CRT_TMP_ZIP_CODE_TAX_ZONE](.DC_CRT_TMP_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_EQUAL_TAX_ZONE](dbo.DC_DEL_EQUAL_TAX_ZONE.md) | dbo.DC_EQUAL_TAX_ZONE, dbo.EQUAL_TAX_ZONE, dbo.TMP_EQUAL_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE table from the](.TMP_EQUAL_TAX_ZONE_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE table and the](.DC_EQUAL_TAX_ZONE_table_and_the.md) |  |
| * | [EQUAL_TAX_ZONE table.](EQUAL_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_table.md) |  |
| * | [are deletes from the EQUAL_TAX_ZONE table.](are_deletes_from_the_EQUAL_TAX_ZONE_table..md) |  |
| * | [DC_DEL_EQUAL_TAX_ZONE](.DC_DEL_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_EQUAL_TAX_ZONE_LANG](dbo.DC_DEL_EQUAL_TAX_ZONE_LANG.md) | dbo.DC_EQUAL_TAX_ZONE_LANG, dbo.EQUAL_TAX_ZONE_LANG, dbo.TMP_EQUAL_TAX_ZONE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE_LANG table from the](.TMP_EQUAL_TAX_ZONE_LANG_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE_LANG table and the](.DC_EQUAL_TAX_ZONE_LANG_table_and_the.md) |  |
| * | [EQUAL_TAX_ZONE_LANG table.](EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE_LANG table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_LANG_table.md) |  |
| * | [are deletes from the EQUAL_TAX_ZONE_LANG table.](are_deletes_from_the_EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [DC_DEL_EQUAL_TAX_ZONE_LANG](.DC_DEL_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_ORPHAN_STK](dbo.DC_DEL_ORPHAN_STK.md) | dbo.ITEM, dbo.ITEM_QUANTITY, dbo.STK_LEDGER_ACCOUNT |
| * | [This procedure deletes orphan stock records from](.This_procedure_deletes_orphan_stock_records_from.md) |  |
| * | [ITEM_QUANTITY and STK_LEDGER_ACCOUNT TABLES.](ITEM_QUANTITY_and_STK_LEDGER_ACCOUNT_TABLES..md) |  |
| * | [DC_DEL_ORPHAN_STK](.DC_DEL_ORPHAN_STK.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if deletion failed.](1_if_deletion_failed..md) |  |
| * | [5/8/00 (L. Rubakhin) - Created](5_8_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_DEL_PRC_CHG](dbo.DC_DEL_PRC_CHG.md) | dbo.PRICE_CHANGE, dbo.PRICE_CHANGE_ITEM |
| * | [This procedure deletes price change.](This_procedure_deletes_price_change..md) |  |
| * | [@PRM_PRC_CHG_ID - price change id](.@PRM_PRC_CHG_ID_-_price_change_id.md) |  |
| * | [@PRM_STORE_NO - store number](.@PRM_STORE_NO_-_store_number.md) |  |
| * | [exec DC_DEL_PRC_CHG 15, 123](.exec_DC_DEL_PRC_CHG_15,_123.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if price change delete failed.](1_if_price_change_delete_failed..md) |  |
| * | [Stock ledger account records are updated separately.](Stock_ledger_account_records_are_updated_separately..md) |  |
| * | [4/12/00 (L. Rubakhin) - Created](4_12_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_DEL_TAX_AUTHORITY](dbo.DC_DEL_TAX_AUTHORITY.md) | dbo.DC_TAX_AUTHORITY, dbo.TAX_AUTHORITY, dbo.TMP_TAX_AUTHORITY |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY table from the](.TMP_TAX_AUTHORITY_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY table and the](.DC_TAX_AUTHORITY_table_and_the.md) |  |
| * | [TAX_AUTHORITY table.](TAX_AUTHORITY_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY table](.The_records_in_the_TMP_TAX_AUTHORITY_table.md) |  |
| * | [are deletes from the TAX_AUTHORITY table.](are_deletes_from_the_TAX_AUTHORITY_table..md) |  |
| * | [DC_DEL_TAX_AUTHORITY](.DC_DEL_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_TAX_AUTHORITY_LANG](dbo.DC_DEL_TAX_AUTHORITY_LANG.md) | dbo.DC_TAX_AUTHORITY_LANG, dbo.TAX_AUTHORITY_LANG, dbo.TMP_TAX_AUTHORITY_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY_LANG table from the](.TMP_TAX_AUTHORITY_LANG_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY_LANG table and the](.DC_TAX_AUTHORITY_LANG_table_and_the.md) |  |
| * | [TAX_AUTHORITY_LANG table.](TAX_AUTHORITY_LANG_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY_LANG table](.The_records_in_the_TMP_TAX_AUTHORITY_LANG_table.md) |  |
| * | [are deletes from the TAX_AUTHORITY_LANG table.](are_deletes_from_the_TAX_AUTHORITY_LANG_table..md) |  |
| * | [DC_DEL_TAX_AUTHORITY_LANG](.DC_DEL_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_TAX_EXEMPT_CERT](dbo.DC_DEL_TAX_EXEMPT_CERT.md) | dbo.DC_TAX_EXEMPT_CERT, dbo.TAX_EXEMPT_CERT, dbo.TMP_TAX_EXEMPT_CERT |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_EXEMPT_CERT table from the](.TMP_TAX_EXEMPT_CERT_table_from_the.md) |  |
| * | [DC_TAX_EXEMPT_CERT table and the](.DC_TAX_EXEMPT_CERT_table_and_the.md) |  |
| * | [TAX_EXEMPT_CERT table.](TAX_EXEMPT_CERT_table..md) |  |
| * | [The records in the TMP_TAX_EXEMPT_CERT table](.The_records_in_the_TMP_TAX_EXEMPT_CERT_table.md) |  |
| * | [are deletes from the TAX_EXEMPT_CERT table.](are_deletes_from_the_TAX_EXEMPT_CERT_table..md) |  |
| * | [DC_DEL_TAX_EXEMPT_CERT](.DC_DEL_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_TAX_GRP_ZONE_AUTH](dbo.DC_DEL_TAX_GRP_ZONE_AUTH.md) | dbo.DC_TAX_GRP_ZONE_AUTH, dbo.TAX_EXEMPT_CERT, dbo.TAX_GRP_ZONE_AUTH, dbo.TMP_TAX_GRP_ZONE_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_GRP_ZONE_AUTH table from the](.TMP_TAX_GRP_ZONE_AUTH_table_from_the.md) |  |
| * | [DC_TAX_GRP_ZONE_AUTH table and the](.DC_TAX_GRP_ZONE_AUTH_table_and_the.md) |  |
| * | [TAX_GRP_ZONE_AUTH table.](TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_GRP_ZONE_AUTH table](.The_records_in_the_TMP_TAX_GRP_ZONE_AUTH_table.md) |  |
| * | [are deletes from the TAX_GRP_ZONE_AUTH table.](are_deletes_from_the_TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [DC_DEL_TAX_GRP_ZONE_AUTH](.DC_DEL_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| * | [4/4/13 (O. Blevins) - Fixed referential integrity for tax exemptions](4_4_13_O._Blevins_-_Fixed_referential_integrity_for_tax_exemptions.md) |  |
| dbo | [DC_DEL_TAX_RULE](dbo.DC_DEL_TAX_RULE.md) | dbo.DC_TAX_RULE, dbo.TAX_RULE, dbo.TMP_TAX_RULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE table from the](.TMP_TAX_RULE_table_from_the.md) |  |
| * | [DC_TAX_RULE table and the](.DC_TAX_RULE_table_and_the.md) |  |
| * | [TAX_RULE table.](TAX_RULE_table..md) |  |
| * | [The records in the TMP_TAX_RULE table](.The_records_in_the_TMP_TAX_RULE_table.md) |  |
| * | [are deletes from the TAX_RULE table.](are_deletes_from_the_TAX_RULE_table..md) |  |
| * | [DC_DEL_TAX_RULE](.DC_DEL_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_TAX_RULE_LANG](dbo.DC_DEL_TAX_RULE_LANG.md) | dbo.DC_TAX_RULE_LANG, dbo.TAX_RULE_LANG, dbo.TMP_TAX_RULE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE_LANG table from the](.TMP_TAX_RULE_LANG_table_from_the.md) |  |
| * | [DC_TAX_RULE_LANG table and the](.DC_TAX_RULE_LANG_table_and_the.md) |  |
| * | [TAX_RULE_LANG table.](TAX_RULE_LANG_table..md) |  |
| * | [The records in the TMP_TAX_RULE_LANG table](.The_records_in_the_TMP_TAX_RULE_LANG_table.md) |  |
| * | [are deletes from the TAX_RULE_LANG table.](are_deletes_from_the_TAX_RULE_LANG_table..md) |  |
| * | [DC_DEL_TAX_RULE_LANG](.DC_DEL_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_TAX_SCHEDULE](dbo.DC_DEL_TAX_SCHEDULE.md) | dbo.DC_TAX_SCHEDULE, dbo.TAX_SCHEDULE, dbo.TMP_TAX_SCHEDULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_SCHEDULE table from the](.TMP_TAX_SCHEDULE_table_from_the.md) |  |
| * | [DC_TAX_SCHEDULE table and the](.DC_TAX_SCHEDULE_table_and_the.md) |  |
| * | [TAX_SCHEDULE table.](TAX_SCHEDULE_table..md) |  |
| * | [The records in the TMP_TAX_SCHEDULE table](.The_records_in_the_TMP_TAX_SCHEDULE_table.md) |  |
| * | [are deletes from the TAX_SCHEDULE table.](are_deletes_from_the_TAX_SCHEDULE_table..md) |  |
| * | [DC_DEL_TAX_SCHEDULE](.DC_DEL_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_TAX_ZONE_TAX_AUTH](dbo.DC_DEL_TAX_ZONE_TAX_AUTH.md) | dbo.DC_TAX_ZONE_TAX_AUTH, dbo.TAX_ZONE_TAX_AUTH, dbo.TMP_TAX_ZONE_TAX_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_ZONE_TAX_AUTH table from the](.TMP_TAX_ZONE_TAX_AUTH_table_from_the.md) |  |
| * | [DC_TAX_ZONE_TAX_AUTH table and the](.DC_TAX_ZONE_TAX_AUTH_table_and_the.md) |  |
| * | [TAX_ZONE_TAX_AUTH table.](TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_ZONE_TAX_AUTH table](.The_records_in_the_TMP_TAX_ZONE_TAX_AUTH_table.md) |  |
| * | [are deletes from the TAX_ZONE_TAX_AUTH table.](are_deletes_from_the_TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [DC_DEL_TAX_ZONE_TAX_AUTH](.DC_DEL_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_TAXABLE_ITEM_GRP](dbo.DC_DEL_TAXABLE_ITEM_GRP.md) | dbo.DC_TAXABLE_ITEM_GRP, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAXABLE_ITEM_GRP |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP table from the](.TMP_TAXABLE_ITEM_GRP_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP table and the](.DC_TAXABLE_ITEM_GRP_table_and_the.md) |  |
| * | [TAXABLE_ITEM_GRP table.](TAXABLE_ITEM_GRP_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_table.md) |  |
| * | [are deletes from the TAXABLE_ITEM_GRP table.](are_deletes_from_the_TAXABLE_ITEM_GRP_table..md) |  |
| * | [DC_DEL_TAXABLE_ITEM_GRP](.DC_DEL_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_TAXABLE_ITEM_GRP_LANG](dbo.DC_DEL_TAXABLE_ITEM_GRP_LANG.md) | dbo.DC_TAXABLE_ITEM_GRP_LANG, dbo.TAXABLE_ITEM_GRP_LANG, dbo.TMP_TAXABLE_ITEM_GRP_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP_LANG table from the](.TMP_TAXABLE_ITEM_GRP_LANG_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP_LANG table and the](.DC_TAXABLE_ITEM_GRP_LANG_table_and_the.md) |  |
| * | [TAXABLE_ITEM_GRP_LANG table.](TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP_LANG table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_LANG_table.md) |  |
| * | [are deletes from the TAXABLE_ITEM_GRP_LANG table.](are_deletes_from_the_TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [DC_DEL_TAXABLE_ITEM_GRP_LANG](.DC_DEL_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_VALUE_ADDED_TAX](dbo.DC_DEL_VALUE_ADDED_TAX.md) | dbo.DC_VALUE_ADDED_TAX, dbo.TMP_VALUE_ADDED_TAX, dbo.VALUE_ADDED_TAX |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX table from the](.TMP_VALUE_ADDED_TAX_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX table and the](.DC_VALUE_ADDED_TAX_table_and_the.md) |  |
| * | [VALUE_ADDED_TAX table.](VALUE_ADDED_TAX_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX table](.The_records_in_the_TMP_VALUE_ADDED_TAX_table.md) |  |
| * | [are deletes from the VALUE_ADDED_TAX table.](are_deletes_from_the_VALUE_ADDED_TAX_table..md) |  |
| * | [DC_DEL_VALUE_ADDED_TAX](.DC_DEL_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_VALUE_ADDED_TAX_LANG](dbo.DC_DEL_VALUE_ADDED_TAX_LANG.md) | dbo.DC_VALUE_ADDED_TAX_LANG, dbo.TMP_VALUE_ADDED_TAX_LANG, dbo.VALUE_ADDED_TAX_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX_LANG table from the](.TMP_VALUE_ADDED_TAX_LANG_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX_LANG table and the](.DC_VALUE_ADDED_TAX_LANG_table_and_the.md) |  |
| * | [VALUE_ADDED_TAX_LANG table.](VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX_LANG table](.The_records_in_the_TMP_VALUE_ADDED_TAX_LANG_table.md) |  |
| * | [are deletes from the VALUE_ADDED_TAX_LANG table.](are_deletes_from_the_VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [DC_DEL_VALUE_ADDED_TAX_LANG](.DC_DEL_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DEL_ZIP_CODE_TAX_ZONE](dbo.DC_DEL_ZIP_CODE_TAX_ZONE.md) | dbo.DC_ZIP_CODE_TAX_ZONE, dbo.TMP_ZIP_CODE_TAX_ZONE, dbo.ZIP_CODE_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_ZIP_CODE_TAX_ZONE table from the](.TMP_ZIP_CODE_TAX_ZONE_table_from_the.md) |  |
| * | [DC_ZIP_CODE_TAX_ZONE table and the](.DC_ZIP_CODE_TAX_ZONE_table_and_the.md) |  |
| * | [ZIP_CODE_TAX_ZONE table.](ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_ZIP_CODE_TAX_ZONE table](.The_records_in_the_TMP_ZIP_CODE_TAX_ZONE_table.md) |  |
| * | [are deletes from the ZIP_CODE_TAX_ZONE table.](are_deletes_from_the_ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [DC_DEL_ZIP_CODE_TAX_ZONE](.DC_DEL_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_DRP_IDX_PRC_CHG](dbo.DC_DRP_IDX_PRC_CHG.md) |  |
| * | [This procedure finds the name of PK constraint on](.This_procedure_finds_the_name_of_PK_constraint_on.md) |  |
| * | [PRICE_CHANGE_ITEM table and drops it.](PRICE_CHANGE_ITEM_table_and_drops_it..md) |  |
| * | [exec DC_DRP_IDX_PRC_CHG](.exec_DC_DRP_IDX_PRC_CHG.md) |  |
| * | [@inx_name - name of PK constraint](.@inx_name_-_name_of_PK_constraint.md) |  |
| * | [@sql_text - text of SQL statement](.@sql_text_-_text_of_SQL_statement.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure dynamically builds sql statement.](This_procedure_dynamically_builds_sql_statement..md) |  |
| * | [11/7/01 (L. Rubakhin) - Created](11_7_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_DRP_IDX_STK_ADJ_ITM](dbo.DC_DRP_IDX_STK_ADJ_ITM.md) |  |
| * | [This procedure finds the name of PK constraint on](.This_procedure_finds_the_name_of_PK_constraint_on.md) |  |
| * | [STK_ADJ_ITEM table and drops it.](STK_ADJ_ITEM_table_and_drops_it..md) |  |
| * | [exec DC_DRP_IDX_STK_ITM](.exec_DC_DRP_IDX_STK_ITM.md) |  |
| * | [@inx_name - name of PK constraint](.@inx_name_-_name_of_PK_constraint.md) |  |
| * | [@sql_text - text of SQL statement](.@sql_text_-_text_of_SQL_statement.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure dynamically builds sql statement.](This_procedure_dynamically_builds_sql_statement..md) |  |
| * | [5/15/00 (L. Rubakhin) - Created](5_15_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_DRP_TMP_PLU](dbo.DC_DRP_TMP_PLU.md) |  |
| * | [This procedure drops TMP_PLU and TMP_POS_ID_UPC_CODE tables.](This_procedure_drops_TMP_PLU_and_TMP_POS_ID_UPC_CODE_tables..md) |  |
| * | [exec DC_DRP_TMP_PLU](.exec_DC_DRP_TMP_PLU.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| * | [4/4/00 (L. Rubakhin) - Added drop of TMP_POS_ITEM_ALERT](4_4_00_L._Rubakhin_-_Added_drop_of_TMP_POS_ITEM_ALERT.md) |  |
| * | [10/29/01 (L. Rubakhin) - Replaced alert with additional info](10_29_01_L._Rubakhin_-_Replaced_alert_with_additional_info.md) |  |
| dbo | [DC_DRP_TMP_PRC](dbo.DC_DRP_TMP_PRC.md) |  |
| * | [This procedure creates temporary table to store price changes.](This_procedure_creates_temporary_table_to_store_price_changes..md) |  |
| * | [exec DC_DRP_TMP_PRC](.exec_DC_DRP_TMP_PRC.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [11/07/01 (L. Rubakhin) - Created](11_07_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_DRP_TMP_UPC](dbo.DC_DRP_TMP_UPC.md) |  |
| * | [This procedure drops TMP_POS_IDENTITY table.](This_procedure_drops_TMP_POS_IDENTITY_table..md) |  |
| * | [exec DC_DRP_TMP_UPC](.exec_DC_DRP_TMP_UPC.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/28/00 (L. Rubakhin) - Created](3_28_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_EQUAL_TAX_ZONE_ERR](dbo.DC_EQUAL_TAX_ZONE_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_EQUAL_TAX_ZONE_ERR](.exec_DC_EQUAL_TAX_ZONE_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_EQUAL_TAX_ZONE_LANG_ERR](dbo.DC_EQUAL_TAX_ZONE_LANG_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_EQUAL_TAX_ZONE_LANG_ERR](.exec_DC_EQUAL_TAX_ZONE_LANG_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_ID_TO_SKU_MAP](dbo.DC_ID_TO_SKU_MAP.md) | dbo.ITEM |
| * | [This procedure returns the map of item ids to SKU.](This_procedure_returns_the_map_of_item_ids_to_SKU..md) |  |
| * | [exec DC_ID_TO_SKU_MAP](.exec_DC_ID_TO_SKU_MAP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/29/00 (M. Zajac) - Created](3_29_00_M._Zajac_-_Created.md) |  |
| ** | [Get SKU, Division, and Item ID from Item table](.Get_SKU,_Division,_and_Item_ID_from_Item_table.md) |  |
| dbo | [DC_IDX_DC_EQUAL_TAX_ZONE](dbo.DC_IDX_DC_EQUAL_TAX_ZONE.md) |  |
| * | [This procedure creates index in DC_EQUAL_TAX_ZONE table](.This_procedure_creates_index_in_DC_EQUAL_TAX_ZONE_table.md) |  |
| * | [exec DC_IDX_DC_EQUAL_TAX_ZONE](.exec_DC_IDX_DC_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_EQUAL_TAX_ZONE_LANG](dbo.DC_IDX_DC_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [This procedure creates index in DC_EQUAL_TAX_ZONE_LANG table](.This_procedure_creates_index_in_DC_EQUAL_TAX_ZONE_LANG_table.md) |  |
| * | [exec DC_IDX_DC_EQUAL_TAX_ZONE_LANG](.exec_DC_IDX_DC_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_ITEM](dbo.DC_IDX_DC_ITEM.md) |  |
| * | [This procedure builds clustered index IDX_ITEM_ID on DC_ITEM.ItemID](This_procedure_builds_clustered_index_IDX_ITEM_ID_on_DC_ITEM.ItemID.md) |  |
| * | [to speed up the joins.](to_speed_up_the_joins..md) |  |
| * | [exec DC_IDX_DC_ITEM](.exec_DC_IDX_DC_ITEM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/15/00 (L. Rubakhin) - Created](3_15_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_IDX_DC_PRC_CHG](dbo.DC_IDX_DC_PRC_CHG.md) |  |
| * | [This procedure builds clustered index IDX_ITEM_ID on DC_PRC_CHG_ITEM.ItemID](This_procedure_builds_clustered_index_IDX_ITEM_ID_on_DC_PRC_CHG_ITEM.ItemID.md) |  |
| * | [to speed up the joins.](to_speed_up_the_joins..md) |  |
| * | [exec DC_IDX_DC_PRC_CHG](.exec_DC_IDX_DC_PRC_CHG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [11/7/01 (L. Rubakhin) - Created](11_7_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_IDX_DC_STORE_ITEM](dbo.DC_IDX_DC_STORE_ITEM.md) |  |
| * | [This procedure builds clustered index IDX_ITEM_ID on DC_ITEM.ItemID](This_procedure_builds_clustered_index_IDX_ITEM_ID_on_DC_ITEM.ItemID.md) |  |
| * | [to speed up the joins.](to_speed_up_the_joins..md) |  |
| * | [exec DC_IDX_DC_STORE_ITEM](.exec_DC_IDX_DC_STORE_ITEM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| dbo | [DC_IDX_DC_TAX_AUTHORITY](dbo.DC_IDX_DC_TAX_AUTHORITY.md) |  |
| * | [This procedure creates index in DC_TAX_AUTHORITY table](.This_procedure_creates_index_in_DC_TAX_AUTHORITY_table.md) |  |
| * | [exec DC_IDX_DC_TAX_AUTHORITY](.exec_DC_IDX_DC_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAX_AUTHORITY_LANG](dbo.DC_IDX_DC_TAX_AUTHORITY_LANG.md) |  |
| * | [This procedure creates index in DC_TAX_AUTHORITY_LANG table](.This_procedure_creates_index_in_DC_TAX_AUTHORITY_LANG_table.md) |  |
| * | [exec DC_IDX_DC_TAX_AUTHORITY_LANG](.exec_DC_IDX_DC_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAX_EXEMPT_CERT](dbo.DC_IDX_DC_TAX_EXEMPT_CERT.md) |  |
| * | [This procedure creates index in DC_TAX_EXEMPT_CERT table](.This_procedure_creates_index_in_DC_TAX_EXEMPT_CERT_table.md) |  |
| * | [exec DC_IDX_DC_TAX_EXEMPT_CERT](.exec_DC_IDX_DC_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAX_GRP_ZONE_AUTH](dbo.DC_IDX_DC_TAX_GRP_ZONE_AUTH.md) |  |
| * | [This procedure creates index in DC_TAX_GRP_ZONE_AUTH table](.This_procedure_creates_index_in_DC_TAX_GRP_ZONE_AUTH_table.md) |  |
| * | [exec DC_IDX_DC_TAX_GRP_ZONE_AUTH](.exec_DC_IDX_DC_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAX_RULE](dbo.DC_IDX_DC_TAX_RULE.md) |  |
| * | [This procedure creates index in DC_TAX_RULE table](.This_procedure_creates_index_in_DC_TAX_RULE_table.md) |  |
| * | [exec DC_IDX_DC_TAX_RULE](.exec_DC_IDX_DC_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAX_RULE_LANG](dbo.DC_IDX_DC_TAX_RULE_LANG.md) |  |
| * | [This procedure creates index in DC_TAX_RULE_LANG table](.This_procedure_creates_index_in_DC_TAX_RULE_LANG_table.md) |  |
| * | [exec DC_IDX_DC_TAX_RULE_LANG](.exec_DC_IDX_DC_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAX_SCHEDULE](dbo.DC_IDX_DC_TAX_SCHEDULE.md) |  |
| * | [This procedure creates index in DC_TAX_SCHEDULE table](.This_procedure_creates_index_in_DC_TAX_SCHEDULE_table.md) |  |
| * | [exec DC_IDX_DC_TAX_SCHEDULE](.exec_DC_IDX_DC_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAX_ZONE_TAX_AUTH](dbo.DC_IDX_DC_TAX_ZONE_TAX_AUTH.md) |  |
| * | [This procedure creates index in DC_TAX_ZONE_TAX_AUTH table](.This_procedure_creates_index_in_DC_TAX_ZONE_TAX_AUTH_table.md) |  |
| * | [exec DC_IDX_DC_TAX_ZONE_TAX_AUTH](.exec_DC_IDX_DC_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAXABLE_ITEM_GRP](dbo.DC_IDX_DC_TAXABLE_ITEM_GRP.md) |  |
| * | [This procedure creates index in DC_TAXABLE_ITEM_GRP table](.This_procedure_creates_index_in_DC_TAXABLE_ITEM_GRP_table.md) |  |
| * | [exec DC_IDX_DC_TAXABLE_ITEM_GRP](.exec_DC_IDX_DC_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_TAXABLE_ITEM_GRP_LANG](dbo.DC_IDX_DC_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [This procedure creates index in DC_TAXABLE_ITEM_GRP_LANG table](.This_procedure_creates_index_in_DC_TAXABLE_ITEM_GRP_LANG_table.md) |  |
| * | [exec DC_IDX_DC_TAXABLE_ITEM_GRP_LANG](.exec_DC_IDX_DC_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_VALUE_ADDED_TAX](dbo.DC_IDX_DC_VALUE_ADDED_TAX.md) |  |
| * | [This procedure creates index in DC_VALUE_ADDED_TAX table](.This_procedure_creates_index_in_DC_VALUE_ADDED_TAX_table.md) |  |
| * | [exec DC_IDX_DC_VALUE_ADDED_TAX](.exec_DC_IDX_DC_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_VALUE_ADDED_TAX_LANG](dbo.DC_IDX_DC_VALUE_ADDED_TAX_LANG.md) |  |
| * | [This procedure creates index in DC_VALUE_ADDED_TAX_LANG table](.This_procedure_creates_index_in_DC_VALUE_ADDED_TAX_LANG_table.md) |  |
| * | [exec DC_IDX_DC_VALUE_ADDED_TAX_LANG](.exec_DC_IDX_DC_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_DC_ZIP_CODE_TAX_ZONE](dbo.DC_IDX_DC_ZIP_CODE_TAX_ZONE.md) |  |
| * | [This procedure creates index in DC_ZIP_CODE_TAX_ZONE table](.This_procedure_creates_index_in_DC_ZIP_CODE_TAX_ZONE_table.md) |  |
| * | [exec DC_IDX_DC_ZIP_CODE_TAX_ZONE](.exec_DC_IDX_DC_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_ITEM](dbo.DC_IDX_ITEM.md) |  |
| * | [This procedure creates PK and index in TMP_ITEM table](.This_procedure_creates_PK_and_index_in_TMP_ITEM_table.md) |  |
| * | [exec DC_IDX_ITEM](.exec_DC_IDX_ITEM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/22/00 (L. Rubakhin) - Created](3_22_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_IDX_PLU](dbo.DC_IDX_PLU.md) |  |
| * | [This procedure creates PK for TMP_PLU table.](This_procedure_creates_PK_for_TMP_PLU_table..md) |  |
| * | [exec DC_IDX_PLU](.exec_DC_IDX_PLU.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| * | [1/6/04 (S.Bogdanski) - added index to ITEM_ID](1_6_04_S.Bogdanski_-_added_index_to_ITEM_ID.md) |  |
| dbo | [DC_IDX_POS_ALERT](dbo.DC_IDX_POS_ALERT.md) |  |
| * | [This procedure creates PK for TMP_POS_ITEM_ALERT.](This_procedure_creates_PK_for_TMP_POS_ITEM_ALERT..md) |  |
| * | [exec DC_IDX_POS_ALERT](.exec_DC_IDX_POS_ALERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [4/4/00 (L. Rubakhin) - Created](4_4_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_IDX_POS_ITEM_ADDL_INFO](dbo.DC_IDX_POS_ITEM_ADDL_INFO.md) |  |
| * | [This procedure creates PK for TMP_POS_ITEM_ADDL_INFO.](This_procedure_creates_PK_for_TMP_POS_ITEM_ADDL_INFO..md) |  |
| * | [exec DC_IDX_POS_ITEM_ADDL_INFO](.exec_DC_IDX_POS_ITEM_ADDL_INFO.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [10/29/00 (L. Rubakhin) - Created](10_29_00_L._Rubakhin_-_Created.md) |  |
| * | [9/27/05 (L. Rubakhin) - Added CIRCUMSTANCE_NO and ITEM_GROUP_ID to PK of POS_ITEM_ADDL_INFO](9_27_05_L._Rubakhin_-_Added_CIRCUMSTANCE_NO_and_ITEM_GROUP_ID_to_PK_of_POS_ITEM_ADDL_INFO.md) |  |
| dbo | [DC_IDX_PRC_CHG](dbo.DC_IDX_PRC_CHG.md) |  |
| * | [This procedure adds PKs to PRICE_CHANGE_ITEM table](.This_procedure_adds_PKs_to_PRICE_CHANGE_ITEM_table.md) |  |
| * | [exec DC_IDX_PRC_CHG](.exec_DC_IDX_PRC_CHG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [11/7/01 (L. Rubakhin) - Created](11_7_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_IDX_STK_ADJ_ITM](dbo.DC_IDX_STK_ADJ_ITM.md) |  |
| * | [This procedure creates PK constraint on](.This_procedure_creates_PK_constraint_on.md) |  |
| * | [STK_ADJ_ITEM table.](STK_ADJ_ITEM_table..md) |  |
| * | [exec DC_IDX_STK_ITM](.exec_DC_IDX_STK_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [5/15/00 (L. Rubakhin) - Created](5_15_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_IDX_STK_ITM](dbo.DC_IDX_STK_ITM.md) |  |
| * | [This procedure builds clustered index IDX_ITEM_ID on](.This_procedure_builds_clustered_index_IDX_ITEM_ID_on.md) |  |
| * | [DC_STOCK_ITEM.ItemID and DC_STOCK_ITEM.StoreNum to speed up the joins.](DC_STOCK_ITEM_ItemID_and_DC_STOCK_ITEM_StoreNum_to_speed_up_the_joins..md) |  |
| * | [exec DC_IDX_STK_ITM](.exec_DC_IDX_STK_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [4/24/00 (L. Rubakhin) - Created](4_24_00_L._Rubakhin_-_Created.md) |  |
| * | [5/30/01 (O. Blevins) - Added StoreNum to the index](5_30_01_O._Blevins_-_Added_StoreNum_to_the_index.md) |  |
| dbo | [DC_IDX_TMP_EQUAL_TAX_ZONE](dbo.DC_IDX_TMP_EQUAL_TAX_ZONE.md) |  |
| * | [This procedure creates index in TMP_EQUAL_TAX_ZONE table](.This_procedure_creates_index_in_TMP_EQUAL_TAX_ZONE_table.md) |  |
| * | [exec DC_IDX_TMP_EQUAL_TAX_ZONE](.exec_DC_IDX_TMP_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_EQUAL_TAX_ZONE_LANG](dbo.DC_IDX_TMP_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [This procedure creates index in TMP_EQUAL_TAX_ZONE_LANG table](.This_procedure_creates_index_in_TMP_EQUAL_TAX_ZONE_LANG_table.md) |  |
| * | [exec DC_IDX_TMP_EQUAL_TAX_ZONE_LANG](.exec_DC_IDX_TMP_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_ITM](dbo.DC_IDX_TMP_ITM.md) |  |
| * | [This procedure adds PKs to all temporary item related](.This_procedure_adds_PKs_to_all_temporary_item_related.md) |  |
| * | [tables:  TMP_STORE_ITEM, TMP_ITEM_POS_SELL_RULE,](.tables_TMP_STORE_ITEM,_TMP_ITEM_POS_SELL_RULE,.md) |  |
| * | [TMP_ITEM_KEYWORD, TMP_ITEM_ALERT, TMP_PRC_CHANGE.](TMP_ITEM_KEYWORD,_TMP_ITEM_ALERT,_TMP_PRC_CHANGE..md) |  |
| * | [exec DC_IDX_TMP_ITM](.exec_DC_IDX_TMP_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/27/00 (L. Rubakhin) - Created](3_27_00_L._Rubakhin_-_Created.md) |  |
| * | [10/31/01 (L. Rubakhin) - replace alert with addl info](10_31_01_L._Rubakhin_-_replace_alert_with_addl_info.md) |  |
| * | [9/27/05 (L. Rubakhin) - Added CIRCUMSTANCE_NO and ITEM_GROUP_ID to TMP_ITEM_ADDL_INFO](9_27_05_L._Rubakhin_-_Added_CIRCUMSTANCE_NO_and_ITEM_GROUP_ID_to_TMP_ITEM_ADDL_INFO.md) |  |
| dbo | [DC_IDX_TMP_PRC_CHG](dbo.DC_IDX_TMP_PRC_CHG.md) |  |
| * | [This procedure adds PKs to TMP_PRC_CHANGE table](.This_procedure_adds_PKs_to_TMP_PRC_CHANGE_table.md) |  |
| * | [exec DC_IDX_TMP_PRC_CHG](.exec_DC_IDX_TMP_PRC_CHG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [11/7/01 (L. Rubakhin) - Created](11_7_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_IDX_TMP_SMPL_DISCNT](dbo.DC_IDX_TMP_SMPL_DISCNT.md) |  |
| * | [This procedure creates index in TMP_SIMPLE_DISCNT table](.This_procedure_creates_index_in_TMP_SIMPLE_DISCNT_table.md) |  |
| * | [exec DC_IDX_TMP_SMPL_DISCNT](.exec_DC_IDX_TMP_SMPL_DISCNT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [1/8/02 (L. Rubakhin) - Created](1_8_02_L._Rubakhin_-_Created.md) |  |
| * | [2/7/02 (L. Rubakhin) - replaced index with PK](2_7_02_L._Rubakhin_-_replaced_index_with_PK.md) |  |
| dbo | [DC_IDX_TMP_STR_ITM](dbo.DC_IDX_TMP_STR_ITM.md) |  |
| * | [This procedure adds PKs to TMP_STORE_ITEM table](.This_procedure_adds_PKs_to_TMP_STORE_ITEM_table.md) |  |
| * | [exec DC_IDX_TMP_STR_ITM](.exec_DC_IDX_TMP_STR_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| dbo | [DC_IDX_TMP_TAX_AUTHORITY](dbo.DC_IDX_TMP_TAX_AUTHORITY.md) |  |
| * | [This procedure creates index in TMP_TAX_AUTHORITY table](.This_procedure_creates_index_in_TMP_TAX_AUTHORITY_table.md) |  |
| * | [exec DC_IDX_TMP_TAX_AUTHORITY](.exec_DC_IDX_TMP_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAX_AUTHORITY_LANG](dbo.DC_IDX_TMP_TAX_AUTHORITY_LANG.md) |  |
| * | [This procedure creates index in TMP_TAX_AUTHORITY_LANG table](.This_procedure_creates_index_in_TMP_TAX_AUTHORITY_LANG_table.md) |  |
| * | [exec DC_IDX_TMP_TAX_AUTHORITY_LANG](.exec_DC_IDX_TMP_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAX_EXEMPT_CERT](dbo.DC_IDX_TMP_TAX_EXEMPT_CERT.md) |  |
| * | [This procedure creates index in TMP_TAX_EXEMPT_CERT table](.This_procedure_creates_index_in_TMP_TAX_EXEMPT_CERT_table.md) |  |
| * | [exec DC_IDX_TMP_TAX_EXEMPT_CERT](.exec_DC_IDX_TMP_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAX_GRP_ZONE_AUTH](dbo.DC_IDX_TMP_TAX_GRP_ZONE_AUTH.md) |  |
| * | [This procedure creates index in TMP_TAX_GRP_ZONE_AUTH table](.This_procedure_creates_index_in_TMP_TAX_GRP_ZONE_AUTH_table.md) |  |
| * | [exec DC_IDX_TMP_TAX_GRP_ZONE_AUTH](.exec_DC_IDX_TMP_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAX_RULE](dbo.DC_IDX_TMP_TAX_RULE.md) |  |
| * | [This procedure creates index in TMP_TAX_RULE table](.This_procedure_creates_index_in_TMP_TAX_RULE_table.md) |  |
| * | [exec DC_IDX_TMP_TAX_RULE](.exec_DC_IDX_TMP_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAX_RULE_LANG](dbo.DC_IDX_TMP_TAX_RULE_LANG.md) |  |
| * | [This procedure creates index in TMP_TAX_RULE_LANG table](.This_procedure_creates_index_in_TMP_TAX_RULE_LANG_table.md) |  |
| * | [exec DC_IDX_TMP_TAX_RULE_LANG](.exec_DC_IDX_TMP_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAX_SCHEDULE](dbo.DC_IDX_TMP_TAX_SCHEDULE.md) |  |
| * | [This procedure creates index in TMP_TAX_SCHEDULE table](.This_procedure_creates_index_in_TMP_TAX_SCHEDULE_table.md) |  |
| * | [exec DC_IDX_TMP_TAX_SCHEDULE](.exec_DC_IDX_TMP_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAX_ZONE_TAX_AUTH](dbo.DC_IDX_TMP_TAX_ZONE_TAX_AUTH.md) |  |
| * | [This procedure creates index in TMP_TAX_ZONE_TAX_AUTH table](.This_procedure_creates_index_in_TMP_TAX_ZONE_TAX_AUTH_table.md) |  |
| * | [exec DC_IDX_TMP_TAX_ZONE_TAX_AUTH](.exec_DC_IDX_TMP_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAXABLE_ITEM_GRP](dbo.DC_IDX_TMP_TAXABLE_ITEM_GRP.md) |  |
| * | [This procedure creates index in TMP_TAXABLE_ITEM_GRP table](.This_procedure_creates_index_in_TMP_TAXABLE_ITEM_GRP_table.md) |  |
| * | [exec DC_IDX_TMP_TAXABLE_ITEM_GRP](.exec_DC_IDX_TMP_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_TAXABLE_ITEM_GRP_LANG](dbo.DC_IDX_TMP_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [This procedure creates index in TMP_TAXABLE_ITEM_GRP_LANG table](.This_procedure_creates_index_in_TMP_TAXABLE_ITEM_GRP_LANG_table.md) |  |
| * | [exec DC_IDX_TMP_TAXABLE_ITEM_GRP_LANG](.exec_DC_IDX_TMP_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_VALUE_ADDED_TAX](dbo.DC_IDX_TMP_VALUE_ADDED_TAX.md) |  |
| * | [This procedure creates index in TMP_VALUE_ADDED_TAX table](.This_procedure_creates_index_in_TMP_VALUE_ADDED_TAX_table.md) |  |
| * | [exec DC_IDX_TMP_VALUE_ADDED_TAX](.exec_DC_IDX_TMP_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_VALUE_ADDED_TAX_LANG](dbo.DC_IDX_TMP_VALUE_ADDED_TAX_LANG.md) |  |
| * | [This procedure creates index in TMP_VALUE_ADDED_TAX_LANG table](.This_procedure_creates_index_in_TMP_VALUE_ADDED_TAX_LANG_table.md) |  |
| * | [exec DC_IDX_TMP_VALUE_ADDED_TAX_LANG](.exec_DC_IDX_TMP_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_TMP_ZIP_CODE_TAX_ZONE](dbo.DC_IDX_TMP_ZIP_CODE_TAX_ZONE.md) |  |
| * | [This procedure creates index in TMP_ZIP_CODE_TAX_ZONE table](.This_procedure_creates_index_in_TMP_ZIP_CODE_TAX_ZONE_table.md) |  |
| * | [exec DC_IDX_TMP_ZIP_CODE_TAX_ZONE](.exec_DC_IDX_TMP_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_IDX_UPC](dbo.DC_IDX_UPC.md) |  |
| * | [This procedure creates PK for TMP_POS_IDENTITY table.](This_procedure_creates_PK_for_TMP_POS_IDENTITY_table..md) |  |
| * | [exec DC_IDX_UPC](.exec_DC_IDX_UPC.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/28/00 (L. Rubakhin) - Created](3_28_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_IDX_UPC_SKU](dbo.DC_IDX_UPC_SKU.md) |  |
| * | [Creates PK in TMP_POS_ID_PLU_CODE table.](Creates_PK_in_TMP_POS_ID_PLU_CODE_table..md) |  |
| * | [exec DC_IDX_UPC_SKU](.exec_DC_IDX_UPC_SKU.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_INS_EQUAL_TAX_ZONE](dbo.DC_INS_EQUAL_TAX_ZONE.md) | dbo.DC_EQUAL_TAX_ZONE, dbo.EQUAL_TAX_ZONE, dbo.TMP_EQUAL_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE table from the](.TMP_EQUAL_TAX_ZONE_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE table and the](.DC_EQUAL_TAX_ZONE_table_and_the.md) |  |
| * | [EQUAL_TAX_ZONE table.](EQUAL_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_table.md) |  |
| * | [are inserts to the EQUAL_TAX_ZONE table.](are_inserts_to_the_EQUAL_TAX_ZONE_table..md) |  |
| * | [DC_INS_EQUAL_TAX_ZONE](.DC_INS_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_EQUAL_TAX_ZONE_LANG](dbo.DC_INS_EQUAL_TAX_ZONE_LANG.md) | dbo.DC_EQUAL_TAX_ZONE_LANG, dbo.EQUAL_TAX_ZONE, dbo.EQUAL_TAX_ZONE_LANG, dbo.LANGUAGE, dbo.TMP_EQUAL_TAX_ZONE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE_LANG table from the](.TMP_EQUAL_TAX_ZONE_LANG_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE_LANG table and the](.DC_EQUAL_TAX_ZONE_LANG_table_and_the.md) |  |
| * | [EQUAL_TAX_ZONE_LANG table.](EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE_LANG table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_LANG_table.md) |  |
| * | [are inserts to the EQUAL_TAX_ZONE_LANG table.](are_inserts_to_the_EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [DC_INS_EQUAL_TAX_ZONE_LANG](.DC_INS_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_ITEM](dbo.DC_INS_ITEM.md) | dbo.CATEGORY, dbo.CLASS, dbo.COLOR, dbo.DC_ITEM, dbo.DEPARTMENT, dbo.ITEM, dbo.LIFE_STYLE, dbo.SEASON, dbo.SIZE, dbo.STYLE, dbo.SUB_CATEGORY, dbo.SUB_CLASS, dbo.SUB_DEPARTMENT, dbo.TMP_ITEM |
| * | [This procedure inserts new data from DC_ITEM to TMP_ITEM](.This_procedure_inserts_new_data_from_DC_ITEM_to_TMP_ITEM.md) |  |
| * | [table.](table..md) |  |
| * | [@PRM_DIV](.@PRM_DIV.md) |  |
| * | [exec DC_INS_ITEM 1](.exec_DC_INS_ITEM_1.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [UPDATE_CODE:](.UPDATE_CODE.md) |  |
| * | [4/5/00 (L. Rubakhin) - Created](4_5_00_L._Rubakhin_-_Created.md) |  |
| * | [8/9/01 (L. Rubakhin) - Added Association Group](8_9_01_L._Rubakhin_-_Added_Association_Group.md) |  |
| * | [10/18/01 (L. Rubakhin) - Added tender type id and activate flag](10_18_01_L._Rubakhin_-_Added_tender_type_id_and_activate_flag.md) |  |
| * | [1/27/2003 ( Madhulika Sharma ) - Field Item_type_code is filled correctly now for issue# 87376](.1_27_2003_Madhulika_Sharma_-_Field_Item_type_code_is_filled_correctly_now_for_issue#_87376.md) |  |
| * | [3/24/05 (L. Rubakhin) - Added buy back price, defective item action code,](3_24_05_L._Rubakhin_-_Added_buy_back_price,_defective_item_action_code,.md) |  |
| * | [5/19/05 (L. Rubakhin) - Support for null values in SIZE.SIZE_TYPE_CODE](5_19_05_L_Rubakhin_-_Support_for_null_values_in_SIZE.SIZE_TYPE_CODE.md) |  |
| dbo | [DC_INS_ITM_ADDL_INFO](dbo.DC_INS_ITM_ADDL_INFO.md) | dbo.DC_ITEM, dbo.ITEM_ADDL_INFO, dbo.TMP_ITEM, dbo.TMP_ITEM_ADDL_INFO |
| * | [This procedure inserts new records into](.This_procedure_inserts_new_records_into.md) |  |
| * | [TMP_ITEM_ADDL_INFO table](.TMP_ITEM_ADDL_INFO_table.md) |  |
| * | [DC_INS_ITM_ADDL_INFO](.DC_INS_ITM_ADDL_INFO.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [10/30/01 (L. Rubakhin) - Created](10_30_01_L._Rubakhin_-_Created.md) |  |
| * | [9/27/05 (L. Rubakhin) - Added CIRCUMSTANCE_NO and ITEM_GROUP_ID to TMP_ITEM_ADDL_INFO](9_27_05_L._Rubakhin_-_Added_CIRCUMSTANCE_NO_and_ITEM_GROUP_ID_to_TMP_ITEM_ADDL_INFO.md) |  |
| dbo | [DC_INS_ITM_KYWRD](dbo.DC_INS_ITM_KYWRD.md) | dbo.DC_ITEM, dbo.ITEM_KEYWORD, dbo.TMP_ITEM, dbo.TMP_ITEM_KEYWORD |
| * | [This procedure adds new item keywords to DC_INS_ITM_KYWRD](.This_procedure_adds_new_item_keywords_to_DC_INS_ITM_KYWRD.md) |  |
| * | [table.  Old keywords are preserved.](table_Old_keywords_are_preserved..md) |  |
| * | [DC_INS_ITM_KYWRD](.DC_INS_ITM_KYWRD.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [4/6/00 (L. Rubakhin) - Created](4_6_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_INS_ITM_QTY](dbo.DC_INS_ITM_QTY.md) | dbo.DC_STOCK_ITEM, dbo.ITEM, dbo.ITEM_QUANTITY, dbo.STK_LEDGER_ACCOUNT, dbo.STORE_ITEM |
| * | [This procedure inserts item quantities. Then ledger is](This_procedure_inserts_item_quantities._Then_ledger_is.md) |  |
| * | [@PRM_COST_METHOD - method used for cost calculation,](.@PRM_COST_METHOD_-_method_used_for_cost_calculation,.md) |  |
| * | [@PRM_PRD_ID - ID of current period](.@PRM_PRD_ID_-_ID_of_current_period.md) |  |
| * | [exec DC_INS_ITM_QTY](.exec_DC_INS_ITM_QTY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 on failure.](1_on_failure..md) |  |
| * | [Stock ledger account records are updated separately.](Stock_ledger_account_records_are_updated_separately..md) |  |
| * | [9/27/01 (O. Blevins) - Created](9_27_01_O._Blevins_-_Created.md) |  |
| * | [1/2/03 (O. Blevins)](1_2_03_O._Blevins.md) |  |
| * | [7/12/07 (L. Rubakhin) - added @PRM_LEDGER_MAINT_LEVEL and @PRM_REF_STORE_NO](7_12_07_L._Rubakhin_-_added_@PRM_LEDGER_MAINT_LEVEL_and_@PRM_REF_STORE_NO.md) |  |
| dbo | [DC_INS_SMPL_DISCNT](dbo.DC_INS_SMPL_DISCNT.md) | dbo.SIMPLE_DISCOUNT, dbo.TMP_SIMPLE_DISCOUNT |
| * | [This procedure adds old simple discounts to](.This_procedure_adds_old_simple_discounts_to.md) |  |
| * | [TMP_SIMPLE_DISCOUNT table.](TMP_SIMPLE_DISCOUNT_table..md) |  |
| * | [DC_INS_SMPL_DISCNT](.DC_INS_SMPL_DISCNT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure should be called only in "add" scenario](.This_procedure_should_be_called_only_in_add_scenario.md) |  |
| * | [1/8/02 (L. Rubakhin) - Created](1_8_02_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_INS_STK_ITM](dbo.DC_INS_STK_ITM.md) | dbo.ITEM, dbo.ITEM_QUANTITY, dbo.STK_LEDGER_ACCOUNT |
| * | [This procedure initializes records for new item](.This_procedure_initializes_records_for_new_item.md) |  |
| * | [in item ledger and item quantity tables.](in_item_ledger_and_item_quantity_tables..md) |  |
| * | [@PRM_STORE_NO - Store Number](.@PRM_STORE_NO_-_Store_Number.md) |  |
| * | [@PRM_PRD_ID - ID of current period](.@PRM_PRD_ID_-_ID_of_current_period.md) |  |
| * | [DC_INS_STK_ITM](.DC_INS_STK_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure uses information in UPDATE_CODE field](.This_procedure_uses_information_in_UPDATE_CODE_field.md) |  |
| * | [in ITEM table.](in_ITEM_table..md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if price booking failed.](1_if_price_booking_failed..md) |  |
| * | [4/7/00 (L. Rubakhin) - Created](4_7_00_L._Rubakhin_-_Created.md) |  |
| * | [7/12/07 (L. Rubakhin) - added @PRM_LEDGER_MAINT_LEVEL (see above)](7_12_07_L._Rubakhin_-_added_@PRM_LEDGER_MAINT_LEVEL_see_above.md) |  |
| dbo | [DC_INS_STK_ITM_GRP](dbo.DC_INS_STK_ITM_GRP.md) | dbo.ITEM, dbo.ITEM_QUANTITY, dbo.STK_LEDGER_ACCOUNT, dbo.STORE_GROUP, dbo.STORE_GROUP_STORE, dbo.STORE_ITEM |
| * | [This procedure initializes records for new item](.This_procedure_initializes_records_for_new_item.md) |  |
| * | [in item ledger and item quantity tables for all the stores](.in_item_ledger_and_item_quantity_tables_for_all_the_stores.md) |  |
| * | ['STIM' store group](.'STIM'_store_group.md) |  |
| * | [@PRM_PRD_ID - ID of current period](.@PRM_PRD_ID_-_ID_of_current_period.md) |  |
| * | [@PRM_LOCAL_STORE_NO int - Store number to remove from list for updates.](@PRM_LOCAL_STORE_NO_int_-_Store_number_to_remove_from_list_for_updates..md) |  |
| * | [DC_INS_STK_ITM_GRP](.DC_INS_STK_ITM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure uses information in UPDATE_CODE field](.This_procedure_uses_information_in_UPDATE_CODE_field.md) |  |
| * | [in ITEM table.](in_ITEM_table..md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if price booking failed.](1_if_price_booking_failed..md) |  |
| * | [11/20/01 (L. Rubakhin) - Created](11_20_01_L._Rubakhin_-_Created.md) |  |
| * | [7/12/07 (L. Rubakhin) - added @PRM_LEDGER_MAINT_LEVEL (see above)](7_12_07_L._Rubakhin_-_added_@PRM_LEDGER_MAINT_LEVEL_see_above.md) |  |
| dbo | [DC_INS_STR_ITEM](dbo.DC_INS_STR_ITEM.md) | dbo.AGE_RESTRICT_GRP, dbo.DC_STORE_ITEM, dbo.ITEM, dbo.SPCL_RESTRICT_GRP, dbo.STORE_ITEM, dbo.TMP_STORE_ITEM |
| * | [This procedure inserts the new store items](.This_procedure_inserts_the_new_store_items.md) |  |
| * | [exec DC_INS_STR_ITEM](.exec_DC_INS_STR_ITEM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| dbo | [DC_INS_TAX_AUTHORITY](dbo.DC_INS_TAX_AUTHORITY.md) | dbo.DC_TAX_AUTHORITY, dbo.TAX_AUTHORITY, dbo.TMP_TAX_AUTHORITY |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY table from the](.TMP_TAX_AUTHORITY_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY table and the](.DC_TAX_AUTHORITY_table_and_the.md) |  |
| * | [TAX_AUTHORITY table.](TAX_AUTHORITY_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY table](.The_records_in_the_TMP_TAX_AUTHORITY_table.md) |  |
| * | [are inserts to the TAX_AUTHORITY table.](are_inserts_to_the_TAX_AUTHORITY_table..md) |  |
| * | [DC_INS_TAX_AUTHORITY](.DC_INS_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_TAX_AUTHORITY_LANG](dbo.DC_INS_TAX_AUTHORITY_LANG.md) | dbo.DC_TAX_AUTHORITY_LANG, dbo.LANGUAGE, dbo.TAX_AUTHORITY, dbo.TAX_AUTHORITY_LANG, dbo.TMP_TAX_AUTHORITY_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY_LANG table from the](.TMP_TAX_AUTHORITY_LANG_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY_LANG table and the](.DC_TAX_AUTHORITY_LANG_table_and_the.md) |  |
| * | [TAX_AUTHORITY_LANG table.](TAX_AUTHORITY_LANG_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY_LANG table](.The_records_in_the_TMP_TAX_AUTHORITY_LANG_table.md) |  |
| * | [are inserts to the TAX_AUTHORITY_LANG table.](are_inserts_to_the_TAX_AUTHORITY_LANG_table..md) |  |
| * | [DC_INS_TAX_AUTHORITY_LANG](.DC_INS_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_TAX_EXEMPT_CERT](dbo.DC_INS_TAX_EXEMPT_CERT.md) | dbo.CUSTOMER, dbo.DC_TAX_EXEMPT_CERT, dbo.TAX_EXEMPT_CERT, dbo.TMP_TAX_EXEMPT_CERT |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_EXEMPT_CERT table from the](.TMP_TAX_EXEMPT_CERT_table_from_the.md) |  |
| * | [DC_TAX_EXEMPT_CERT table and the](.DC_TAX_EXEMPT_CERT_table_and_the.md) |  |
| * | [TAX_EXEMPT_CERT table.](TAX_EXEMPT_CERT_table..md) |  |
| * | [The records in the TMP_TAX_EXEMPT_CERT table](.The_records_in_the_TMP_TAX_EXEMPT_CERT_table.md) |  |
| * | [are inserts to the TAX_EXEMPT_CERT table.](are_inserts_to_the_TAX_EXEMPT_CERT_table..md) |  |
| * | [DC_INS_TAX_EXEMPT_CERT](.DC_INS_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_TAX_GRP_ZONE_AUTH](dbo.DC_INS_TAX_GRP_ZONE_AUTH.md) | dbo.DC_TAX_GRP_ZONE_AUTH, dbo.EQUAL_TAX_ZONE, dbo.TAX_AUTHORITY, dbo.TAX_EXEMPT_CERT, dbo.TAX_GRP_ZONE_AUTH, dbo.TAX_RULE, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAX_GRP_ZONE_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_GRP_ZONE_AUTH table from the](.TMP_TAX_GRP_ZONE_AUTH_table_from_the.md) |  |
| * | [DC_TAX_GRP_ZONE_AUTH table and the](.DC_TAX_GRP_ZONE_AUTH_table_and_the.md) |  |
| * | [TAX_GRP_ZONE_AUTH table.](TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_GRP_ZONE_AUTH table](.The_records_in_the_TMP_TAX_GRP_ZONE_AUTH_table.md) |  |
| * | [are inserts to the TAX_GRP_ZONE_AUTH table.](are_inserts_to_the_TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [DC_INS_TAX_GRP_ZONE_AUTH](.DC_INS_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| * | [4/4/13 (O. Blevins) - Fixed referential integrity for tax exemptions](4_4_13_O._Blevins_-_Fixed_referential_integrity_for_tax_exemptions.md) |  |
| dbo | [DC_INS_TAX_RULE](dbo.DC_INS_TAX_RULE.md) | dbo.DC_TAX_RULE, dbo.TAX_RULE, dbo.TMP_TAX_RULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE table from the](.TMP_TAX_RULE_table_from_the.md) |  |
| * | [DC_TAX_RULE table and the](.DC_TAX_RULE_table_and_the.md) |  |
| * | [TAX_RULE table.](TAX_RULE_table..md) |  |
| * | [The records in the TMP_TAX_RULE table](.The_records_in_the_TMP_TAX_RULE_table.md) |  |
| * | [are inserts to the TAX_RULE table.](are_inserts_to_the_TAX_RULE_table..md) |  |
| * | [DC_INS_TAX_RULE](.DC_INS_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_TAX_RULE_LANG](dbo.DC_INS_TAX_RULE_LANG.md) | dbo.DC_TAX_RULE_LANG, dbo.LANGUAGE, dbo.TAX_RULE, dbo.TAX_RULE_LANG, dbo.TMP_TAX_RULE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE_LANG table from the](.TMP_TAX_RULE_LANG_table_from_the.md) |  |
| * | [DC_TAX_RULE_LANG table and the](.DC_TAX_RULE_LANG_table_and_the.md) |  |
| * | [TAX_RULE_LANG table.](TAX_RULE_LANG_table..md) |  |
| * | [The records in the TMP_TAX_RULE_LANG table](.The_records_in_the_TMP_TAX_RULE_LANG_table.md) |  |
| * | [are inserts to the TAX_RULE_LANG table.](are_inserts_to_the_TAX_RULE_LANG_table..md) |  |
| * | [DC_INS_TAX_RULE_LANG](.DC_INS_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_TAX_SCHEDULE](dbo.DC_INS_TAX_SCHEDULE.md) | dbo.DC_TAX_SCHEDULE, dbo.TAX_RULE, dbo.TAX_SCHEDULE, dbo.TMP_TAX_SCHEDULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_SCHEDULE table from the](.TMP_TAX_SCHEDULE_table_from_the.md) |  |
| * | [DC_TAX_SCHEDULE table and the](.DC_TAX_SCHEDULE_table_and_the.md) |  |
| * | [TAX_SCHEDULE table.](TAX_SCHEDULE_table..md) |  |
| * | [The records in the TMP_TAX_SCHEDULE table](.The_records_in_the_TMP_TAX_SCHEDULE_table.md) |  |
| * | [are inserts to the TAX_SCHEDULE table.](are_inserts_to_the_TAX_SCHEDULE_table..md) |  |
| * | [DC_INS_TAX_SCHEDULE](.DC_INS_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_TAX_ZONE_TAX_AUTH](dbo.DC_INS_TAX_ZONE_TAX_AUTH.md) | dbo.DC_TAX_ZONE_TAX_AUTH, dbo.EQUAL_TAX_ZONE, dbo.TAX_AUTHORITY, dbo.TAX_ZONE_TAX_AUTH, dbo.TMP_TAX_ZONE_TAX_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_ZONE_TAX_AUTH table from the](.TMP_TAX_ZONE_TAX_AUTH_table_from_the.md) |  |
| * | [DC_TAX_ZONE_TAX_AUTH table and the](.DC_TAX_ZONE_TAX_AUTH_table_and_the.md) |  |
| * | [TAX_ZONE_TAX_AUTH table.](TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_ZONE_TAX_AUTH table](.The_records_in_the_TMP_TAX_ZONE_TAX_AUTH_table.md) |  |
| * | [are inserts to the TAX_ZONE_TAX_AUTH table.](are_inserts_to_the_TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [DC_INS_TAX_ZONE_TAX_AUTH](.DC_INS_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_TAXABLE_ITEM_GRP](dbo.DC_INS_TAXABLE_ITEM_GRP.md) | dbo.DC_TAXABLE_ITEM_GRP, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAXABLE_ITEM_GRP |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP table from the](.TMP_TAXABLE_ITEM_GRP_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP table and the](.DC_TAXABLE_ITEM_GRP_table_and_the.md) |  |
| * | [TAXABLE_ITEM_GRP table.](TAXABLE_ITEM_GRP_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_table.md) |  |
| * | [are inserts to the TAXABLE_ITEM_GRP table.](are_inserts_to_the_TAXABLE_ITEM_GRP_table..md) |  |
| * | [DC_INS_TAXABLE_ITEM_GRP](.DC_INS_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_TAXABLE_ITEM_GRP_LANG](dbo.DC_INS_TAXABLE_ITEM_GRP_LANG.md) | dbo.DC_TAXABLE_ITEM_GRP_LANG, dbo.LANGUAGE, dbo.TAXABLE_ITEM_GRP, dbo.TAXABLE_ITEM_GRP_LANG, dbo.TMP_TAXABLE_ITEM_GRP_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP_LANG table from the](.TMP_TAXABLE_ITEM_GRP_LANG_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP_LANG table and the](.DC_TAXABLE_ITEM_GRP_LANG_table_and_the.md) |  |
| * | [TAXABLE_ITEM_GRP_LANG table.](TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP_LANG table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_LANG_table.md) |  |
| * | [are inserts to the TAXABLE_ITEM_GRP_LANG table.](are_inserts_to_the_TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [DC_INS_TAXABLE_ITEM_GRP_LANG](.DC_INS_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_UPC](dbo.DC_INS_UPC.md) | dbo.ITEM, dbo.POS_IDENTITY, dbo.TMP_POS_IDENTITY |
| * | [This procedure adds old UPCs to TMP_POS_IDENTITY](.This_procedure_adds_old_UPCs_to_TMP_POS_IDENTITY.md) |  |
| * | [table based on information in DC_INS_UPC table.](table_based_on_information_in_DC_INS_UPC_table..md) |  |
| * | [DC_INS_UPC](.DC_INS_UPC.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [New UPCs should be already in TMP_POS_IDENTITY after](.New_UPCs_should_be_already_in_TMP_POS_IDENTITY_after.md) |  |
| * | [the bulk insert.](the_bulk_insert..md) |  |
| * | [4/6/00 (L. Rubakhin) - Created](4_6_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_INS_VALUE_ADDED_TAX](dbo.DC_INS_VALUE_ADDED_TAX.md) | dbo.DC_VALUE_ADDED_TAX, dbo.TMP_VALUE_ADDED_TAX, dbo.VALUE_ADDED_TAX |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX table from the](.TMP_VALUE_ADDED_TAX_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX table and the](.DC_VALUE_ADDED_TAX_table_and_the.md) |  |
| * | [VALUE_ADDED_TAX table.](VALUE_ADDED_TAX_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX table](.The_records_in_the_TMP_VALUE_ADDED_TAX_table.md) |  |
| * | [are inserts to the VALUE_ADDED_TAX table.](are_inserts_to_the_VALUE_ADDED_TAX_table..md) |  |
| * | [DC_INS_VALUE_ADDED_TAX](.DC_INS_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_VALUE_ADDED_TAX_LANG](dbo.DC_INS_VALUE_ADDED_TAX_LANG.md) | dbo.DC_VALUE_ADDED_TAX_LANG, dbo.LANGUAGE, dbo.TMP_VALUE_ADDED_TAX_LANG, dbo.VALUE_ADDED_TAX, dbo.VALUE_ADDED_TAX_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX_LANG table from the](.TMP_VALUE_ADDED_TAX_LANG_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX_LANG table and the](.DC_VALUE_ADDED_TAX_LANG_table_and_the.md) |  |
| * | [VALUE_ADDED_TAX_LANG table.](VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX_LANG table](.The_records_in_the_TMP_VALUE_ADDED_TAX_LANG_table.md) |  |
| * | [are inserts to the VALUE_ADDED_TAX_LANG table.](are_inserts_to_the_VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [DC_INS_VALUE_ADDED_TAX_LANG](.DC_INS_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INS_ZIP_CODE_TAX_ZONE](dbo.DC_INS_ZIP_CODE_TAX_ZONE.md) | dbo.DC_CHK_ZIP_CODE_TAX_ZONE_OVRLP, dbo.DC_ZIP_CODE_TAX_ZONE, dbo.EQUAL_TAX_ZONE, dbo.TMP_ZIP_CODE_TAX_ZONE, dbo.ZIP_CODE_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_ZIP_CODE_TAX_ZONE table from the](.TMP_ZIP_CODE_TAX_ZONE_table_from_the.md) |  |
| * | [DC_ZIP_CODE_TAX_ZONE table and the](.DC_ZIP_CODE_TAX_ZONE_table_and_the.md) |  |
| * | [ZIP_CODE_TAX_ZONE table.](ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_ZIP_CODE_TAX_ZONE table](.The_records_in_the_TMP_ZIP_CODE_TAX_ZONE_table.md) |  |
| * | [are inserts to the ZIP_CODE_TAX_ZONE table.](are_inserts_to_the_ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [DC_INS_ZIP_CODE_TAX_ZONE](.DC_INS_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_EQUAL_TAX_ZONE](dbo.DC_INSUPD_EQUAL_TAX_ZONE.md) | dbo.DC_EQUAL_TAX_ZONE, dbo.EQUAL_TAX_ZONE, dbo.TMP_EQUAL_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE table from the](.TMP_EQUAL_TAX_ZONE_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE table and the](.DC_EQUAL_TAX_ZONE_table_and_the.md) |  |
| * | [EQUAL_TAX_ZONE table.](EQUAL_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_table.md) |  |
| * | [are inserts/updates to the EQUAL_TAX_ZONE table.](are_inserts_updates_to_the_EQUAL_TAX_ZONE_table..md) |  |
| * | [DC_INSUPD_EQUAL_TAX_ZONE](.DC_INSUPD_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_EQUAL_TAX_ZONE_LANG](dbo.DC_INSUPD_EQUAL_TAX_ZONE_LANG.md) | dbo.DC_EQUAL_TAX_ZONE_LANG, dbo.EQUAL_TAX_ZONE, dbo.EQUAL_TAX_ZONE_LANG, dbo.LANGUAGE, dbo.TMP_EQUAL_TAX_ZONE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE_LANG table from the](.TMP_EQUAL_TAX_ZONE_LANG_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE_LANG table and the](.DC_EQUAL_TAX_ZONE_LANG_table_and_the.md) |  |
| * | [EQUAL_TAX_ZONE_LANG table.](EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE_LANG table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_LANG_table.md) |  |
| * | [are inserts/updates to the EQUAL_TAX_ZONE_LANG table.](are_inserts_updates_to_the_EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [DC_INSUPD_EQUAL_TAX_ZONE_LANG](.DC_INSUPD_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAX_AUTHORITY](dbo.DC_INSUPD_TAX_AUTHORITY.md) | dbo.DC_TAX_AUTHORITY, dbo.TAX_AUTHORITY, dbo.TMP_TAX_AUTHORITY |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY table from the](.TMP_TAX_AUTHORITY_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY table and the](.DC_TAX_AUTHORITY_table_and_the.md) |  |
| * | [TAX_AUTHORITY table.](TAX_AUTHORITY_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY table](.The_records_in_the_TMP_TAX_AUTHORITY_table.md) |  |
| * | [are inserts/updates to the TAX_AUTHORITY table.](are_inserts_updates_to_the_TAX_AUTHORITY_table..md) |  |
| * | [DC_INSUPD_TAX_AUTHORITY](.DC_INSUPD_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAX_AUTHORITY_LANG](dbo.DC_INSUPD_TAX_AUTHORITY_LANG.md) | dbo.DC_TAX_AUTHORITY_LANG, dbo.LANGUAGE, dbo.TAX_AUTHORITY, dbo.TAX_AUTHORITY_LANG, dbo.TMP_TAX_AUTHORITY_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY_LANG table from the](.TMP_TAX_AUTHORITY_LANG_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY_LANG table and the](.DC_TAX_AUTHORITY_LANG_table_and_the.md) |  |
| * | [TAX_AUTHORITY_LANG table.](TAX_AUTHORITY_LANG_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY_LANG table](.The_records_in_the_TMP_TAX_AUTHORITY_LANG_table.md) |  |
| * | [are inserts/updates to the TAX_AUTHORITY_LANG table.](are_inserts_updates_to_the_TAX_AUTHORITY_LANG_table..md) |  |
| * | [DC_INSUPD_TAX_AUTHORITY_LANG](.DC_INSUPD_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAX_EXEMPT_CERT](dbo.DC_INSUPD_TAX_EXEMPT_CERT.md) | dbo.CUSTOMER, dbo.DC_TAX_EXEMPT_CERT, dbo.TAX_EXEMPT_CERT, dbo.TMP_TAX_EXEMPT_CERT |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_EXEMPT_CERT table from the](.TMP_TAX_EXEMPT_CERT_table_from_the.md) |  |
| * | [DC_TAX_EXEMPT_CERT table and the](.DC_TAX_EXEMPT_CERT_table_and_the.md) |  |
| * | [TAX_EXEMPT_CERT table.](TAX_EXEMPT_CERT_table..md) |  |
| * | [The records in the TMP_TAX_EXEMPT_CERT table](.The_records_in_the_TMP_TAX_EXEMPT_CERT_table.md) |  |
| * | [are inserts/updates to the TAX_EXEMPT_CERT table.](are_inserts_updates_to_the_TAX_EXEMPT_CERT_table..md) |  |
| * | [DC_INSUPD_TAX_EXEMPT_CERT](.DC_INSUPD_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAX_GRP_ZONE_AUTH](dbo.DC_INSUPD_TAX_GRP_ZONE_AUTH.md) | dbo.DC_TAX_GRP_ZONE_AUTH, dbo.EQUAL_TAX_ZONE, dbo.TAX_AUTHORITY, dbo.TAX_EXEMPT_CERT, dbo.TAX_GRP_ZONE_AUTH, dbo.TAX_RULE, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAX_GRP_ZONE_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_GRP_ZONE_AUTH table from the](.TMP_TAX_GRP_ZONE_AUTH_table_from_the.md) |  |
| * | [DC_TAX_GRP_ZONE_AUTH table and the](.DC_TAX_GRP_ZONE_AUTH_table_and_the.md) |  |
| * | [TAX_GRP_ZONE_AUTH table.](TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_GRP_ZONE_AUTH table](.The_records_in_the_TMP_TAX_GRP_ZONE_AUTH_table.md) |  |
| * | [are inserts/updates to the TAX_GRP_ZONE_AUTH table.](are_inserts_updates_to_the_TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [DC_INSUPD_TAX_GRP_ZONE_AUTH](.DC_INSUPD_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| * | [4/4/13 (O. Blevins) - Fixed referential integrity for tax exemptions](4_4_13_O._Blevins_-_Fixed_referential_integrity_for_tax_exemptions.md) |  |
| dbo | [DC_INSUPD_TAX_RULE](dbo.DC_INSUPD_TAX_RULE.md) | dbo.DC_TAX_RULE, dbo.TAX_RULE, dbo.TMP_TAX_RULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE table from the](.TMP_TAX_RULE_table_from_the.md) |  |
| * | [DC_TAX_RULE table and the](.DC_TAX_RULE_table_and_the.md) |  |
| * | [TAX_RULE table.](TAX_RULE_table..md) |  |
| * | [The records in the TMP_TAX_RULE table](.The_records_in_the_TMP_TAX_RULE_table.md) |  |
| * | [are inserts/updates to the TAX_RULE table.](are_inserts_updates_to_the_TAX_RULE_table..md) |  |
| * | [DC_INSUPD_TAX_RULE](.DC_INSUPD_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAX_RULE_LANG](dbo.DC_INSUPD_TAX_RULE_LANG.md) | dbo.DC_TAX_RULE_LANG, dbo.LANGUAGE, dbo.TAX_RULE, dbo.TAX_RULE_LANG, dbo.TMP_TAX_RULE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE_LANG table from the](.TMP_TAX_RULE_LANG_table_from_the.md) |  |
| * | [DC_TAX_RULE_LANG table and the](.DC_TAX_RULE_LANG_table_and_the.md) |  |
| * | [TAX_RULE_LANG table.](TAX_RULE_LANG_table..md) |  |
| * | [The records in the TMP_TAX_RULE_LANG table](.The_records_in_the_TMP_TAX_RULE_LANG_table.md) |  |
| * | [are inserts/updates to the TAX_RULE_LANG table.](are_inserts_updates_to_the_TAX_RULE_LANG_table..md) |  |
| * | [DC_INSUPD_TAX_RULE_LANG](.DC_INSUPD_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAX_SCHEDULE](dbo.DC_INSUPD_TAX_SCHEDULE.md) | dbo.DC_TAX_SCHEDULE, dbo.TAX_RULE, dbo.TAX_SCHEDULE, dbo.TMP_TAX_SCHEDULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_SCHEDULE table from the](.TMP_TAX_SCHEDULE_table_from_the.md) |  |
| * | [DC_TAX_SCHEDULE table and the](.DC_TAX_SCHEDULE_table_and_the.md) |  |
| * | [TAX_SCHEDULE table.](TAX_SCHEDULE_table..md) |  |
| * | [The records in the TMP_TAX_SCHEDULE table](.The_records_in_the_TMP_TAX_SCHEDULE_table.md) |  |
| * | [are inserts/updates to the TAX_SCHEDULE table.](are_inserts_updates_to_the_TAX_SCHEDULE_table..md) |  |
| * | [DC_INSUPD_TAX_SCHEDULE](.DC_INSUPD_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAX_ZONE_TAX_AUTH](dbo.DC_INSUPD_TAX_ZONE_TAX_AUTH.md) | dbo.DC_TAX_ZONE_TAX_AUTH, dbo.EQUAL_TAX_ZONE, dbo.TAX_AUTHORITY, dbo.TAX_ZONE_TAX_AUTH, dbo.TMP_TAX_ZONE_TAX_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_ZONE_TAX_AUTH table from the](.TMP_TAX_ZONE_TAX_AUTH_table_from_the.md) |  |
| * | [DC_TAX_ZONE_TAX_AUTH table and the](.DC_TAX_ZONE_TAX_AUTH_table_and_the.md) |  |
| * | [TAX_ZONE_TAX_AUTH table.](TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_ZONE_TAX_AUTH table](.The_records_in_the_TMP_TAX_ZONE_TAX_AUTH_table.md) |  |
| * | [are inserts/updates to the TAX_ZONE_TAX_AUTH table.](are_inserts_updates_to_the_TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [DC_INSUPD_TAX_ZONE_TAX_AUTH](.DC_INSUPD_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAXABLE_ITEM_GRP](dbo.DC_INSUPD_TAXABLE_ITEM_GRP.md) | dbo.DC_TAXABLE_ITEM_GRP, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAXABLE_ITEM_GRP |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP table from the](.TMP_TAXABLE_ITEM_GRP_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP table and the](.DC_TAXABLE_ITEM_GRP_table_and_the.md) |  |
| * | [TAXABLE_ITEM_GRP table.](TAXABLE_ITEM_GRP_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_table.md) |  |
| * | [are inserts/updates to the TAXABLE_ITEM_GRP table.](are_inserts_updates_to_the_TAXABLE_ITEM_GRP_table..md) |  |
| * | [DC_INSUPD_TAXABLE_ITEM_GRP](.DC_INSUPD_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_TAXABLE_ITEM_GRP_LANG](dbo.DC_INSUPD_TAXABLE_ITEM_GRP_LANG.md) | dbo.DC_TAXABLE_ITEM_GRP_LANG, dbo.LANGUAGE, dbo.TAXABLE_ITEM_GRP, dbo.TAXABLE_ITEM_GRP_LANG, dbo.TMP_TAXABLE_ITEM_GRP_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP_LANG table from the](.TMP_TAXABLE_ITEM_GRP_LANG_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP_LANG table and the](.DC_TAXABLE_ITEM_GRP_LANG_table_and_the.md) |  |
| * | [TAXABLE_ITEM_GRP_LANG table.](TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP_LANG table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_LANG_table.md) |  |
| * | [are inserts/updates to the TAXABLE_ITEM_GRP_LANG table.](are_inserts_updates_to_the_TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [DC_INSUPD_TAXABLE_ITEM_GRP_LANG](.DC_INSUPD_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_VALUE_ADDED_TAX](dbo.DC_INSUPD_VALUE_ADDED_TAX.md) | dbo.DC_VALUE_ADDED_TAX, dbo.TMP_VALUE_ADDED_TAX, dbo.VALUE_ADDED_TAX |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX table from the](.TMP_VALUE_ADDED_TAX_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX table and the](.DC_VALUE_ADDED_TAX_table_and_the.md) |  |
| * | [VALUE_ADDED_TAX table.](VALUE_ADDED_TAX_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX table](.The_records_in_the_TMP_VALUE_ADDED_TAX_table.md) |  |
| * | [are inserts/updates to the VALUE_ADDED_TAX table.](are_inserts_updates_to_the_VALUE_ADDED_TAX_table..md) |  |
| * | [DC_INSUPD_VALUE_ADDED_TAX](.DC_INSUPD_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_VALUE_ADDED_TAX_LANG](dbo.DC_INSUPD_VALUE_ADDED_TAX_LANG.md) | dbo.DC_VALUE_ADDED_TAX_LANG, dbo.LANGUAGE, dbo.TMP_VALUE_ADDED_TAX_LANG, dbo.VALUE_ADDED_TAX, dbo.VALUE_ADDED_TAX_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX_LANG table from the](.TMP_VALUE_ADDED_TAX_LANG_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX_LANG table and the](.DC_VALUE_ADDED_TAX_LANG_table_and_the.md) |  |
| * | [VALUE_ADDED_TAX_LANG table.](VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX_LANG table](.The_records_in_the_TMP_VALUE_ADDED_TAX_LANG_table.md) |  |
| * | [are inserts/updates to the VALUE_ADDED_TAX_LANG table.](are_inserts_updates_to_the_VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [DC_INSUPD_VALUE_ADDED_TAX_LANG](.DC_INSUPD_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_INSUPD_ZIP_CODE_TAX_ZONE](dbo.DC_INSUPD_ZIP_CODE_TAX_ZONE.md) | dbo.DC_CHK_ZIP_CODE_TAX_ZONE_OVRLP, dbo.DC_ZIP_CODE_TAX_ZONE, dbo.EQUAL_TAX_ZONE, dbo.TMP_ZIP_CODE_TAX_ZONE, dbo.ZIP_CODE_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_ZIP_CODE_TAX_ZONE table from the](.TMP_ZIP_CODE_TAX_ZONE_table_from_the.md) |  |
| * | [DC_ZIP_CODE_TAX_ZONE table and the](.DC_ZIP_CODE_TAX_ZONE_table_and_the.md) |  |
| * | [ZIP_CODE_TAX_ZONE table.](ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_ZIP_CODE_TAX_ZONE table](.The_records_in_the_TMP_ZIP_CODE_TAX_ZONE_table.md) |  |
| * | [are inserts/updates to the ZIP_CODE_TAX_ZONE table.](are_inserts_updates_to_the_ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [DC_INSUPD_ZIP_CODE_TAX_ZONE](.DC_INSUPD_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_ITM_ERR](dbo.DC_ITM_ERR.md) | dbo.DC_ITEM |
| * | [This procedure cleans up in the case of error.  It purges](This_procedure_cleans_up_in_the_case_of_error._It_purges.md) |  |
| * | [DC_ITEM table and drops the index. It also drops the temporary](DC_ITEM_table_and_drops_the_index._It_also_drops_the_temporary.md) |  |
| * | [tables.](tables..md) |  |
| * | [exec DC_ITM_ERR](.exec_DC_ITM_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [All the data from DC item table is deleted.  This operation is not](All_the_data_from_DC_item_table_is_deleted._This_operation_is_not.md) |  |
| * | [logged.  It means that complete database backup should be performed](logged._It_means_that_complete_database_backup_should_be_performed.md) |  |
| * | [after bulk data is inserted.](after_bulk_data_is_inserted..md) |  |
| * | [This procedure invalidates log backup sequence so the database will](.This_procedure_invalidates_log_backup_sequence_so_the_database_will.md) |  |
| * | [get into log truncate mode. To get the database back out of log](get_into_log_truncate_mode._To_get_the_database_back_out_of_log.md) |  |
| * | [truncate mode the complete database backup should be done after the](.truncate_mode_the_complete_database_backup_should_be_done_after_the.md) |  |
| * | [data import is complete.](data_import_is_complete..md) |  |
| * | [3/21/00 (L. Rubakhin) - Created](3_21_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_MOVE_PLU](dbo.DC_MOVE_PLU.md) | dbo.PLU, dbo.TMP_PLU |
| dbo | [DC_MOVE_POS_ADDL_INFO](dbo.DC_MOVE_POS_ADDL_INFO.md) | dbo.POS_ITEM_ADDL_INFO, dbo.TMP_POS_ITEM_ADDL_INFO |
| dbo | [DC_MOVE_UPC_SKU](dbo.DC_MOVE_UPC_SKU.md) | dbo.POS_ID_PLU_CODE, dbo.TMP_POS_ID_PLU_CODE |
| dbo | [DC_PRC_CHANGE](dbo.DC_PRC_CHANGE.md) | dbo.DC_ITEM, dbo.ITEM, dbo.STORE_ITEM, dbo.TMP_PRC_CHANGE |
| * | [This procedure stores all price changes into TMP_PRC_CHANGE](.This_procedure_stores_all_price_changes_into_TMP_PRC_CHANGE.md) |  |
| * | [@PRM_GLBL_PRC - 1 global price dominates local](.@PRM_GLBL_PRC_-_1_global_price_dominates_local.md) |  |
| * | [@PRM_GLBL_PRC - 0 global price does not effect local](.@PRM_GLBL_PRC_-_0_global_price_does_not_effect_local.md) |  |
| * | [exec DC_PRC_CHANGE 123, 0](.exec_DC_PRC_CHANGE_123,_0.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/24/00 (L. Rubakhin) - Created](3_24_00_L._Rubakhin_-_Created.md) |  |
| * | [12/14/01 (L. Rubakhin) - Added store number parameter](12_14_01_L._Rubakhin_-_Added_store_number_parameter.md) |  |
| begin | [insert into TMP_PRC_CHANGE (](begin.insert_into_TMP_PRC_CHANGE.md) |  |
| else | [-- global price changes but local stays the same](else.--_global_price_changes_but_local_stays_the_same.md) |  |
| dbo | [DC_PRC_CHG_STR_ITM](dbo.DC_PRC_CHG_STR_ITM.md) | dbo.DC_STORE_ITEM, dbo.ITEM, dbo.STORE_ITEM, dbo.TMP_PRC_CHANGE |
| * | [This procedure stores all price changes into TMP_PRC_CHANGE](.This_procedure_stores_all_price_changes_into_TMP_PRC_CHANGE.md) |  |
| * | [@PRM_STORE_NO - store number to use for generation of PLU file](.@PRM_STORE_NO_-_store_number_to_use_for_generation_of_PLU_file.md) |  |
| * | [exec DC_PRC_CHG_STR_ITM 123](.exec_DC_PRC_CHG_STR_ITM_123.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [11/26/01 (L. Rubakhin) - Created](11_26_01_L._Rubakhin_-_Created.md) |  |
| * | [6/22/07 (L. Rubakhin) - Added @PRM_STORE_NO filter](6_22_07_L._Rubakhin_-_Added_@PRM_STORE_NO_filter.md) |  |
| dbo | [DC_PREP_ITM_BULK](dbo.DC_PREP_ITM_BULK.md) | dbo.DC_ITEM |
| * | [This procedure prepares bulk insert of item data. It truncates](This_procedure_prepares_bulk_insert_of_item_data._It_truncates.md) |  |
| * | [DC_ITEM table and drops the index.  This is necessary to](DC_ITEM_table_and_drops_the_index._This_is_necessary_to.md) |  |
| * | [guarantee that DC will work even after abnormal termination.](guarantee_that_DC_will_work_even_after_abnormal_termination..md) |  |
| * | [exec DC_PREP_ITM_BULK](.exec_DC_PREP_ITM_BULK.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [All the data from DC item table is deleted.  This operation is not](All_the_data_from_DC_item_table_is_deleted._This_operation_is_not.md) |  |
| * | [logged.  It means that complete database backup should be performed](logged._It_means_that_complete_database_backup_should_be_performed.md) |  |
| * | [after bulk data is inserted.](after_bulk_data_is_inserted..md) |  |
| * | [This procedure invalidates log backup sequence so the database will](.This_procedure_invalidates_log_backup_sequence_so_the_database_will.md) |  |
| * | [get into log truncate mode. To get the database back out of log](get_into_log_truncate_mode._To_get_the_database_back_out_of_log.md) |  |
| * | [truncate mode the complete database backup should be done after the](.truncate_mode_the_complete_database_backup_should_be_done_after_the.md) |  |
| * | [data import is complete.](data_import_is_complete..md) |  |
| * | [3/14/00 (L. Rubakhin) - Created](3_14_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_PREP_PRC_CHG](dbo.DC_PREP_PRC_CHG.md) | dbo.DC_PRC_CHG_ITEM |
| * | [This procedure prepares bulk update of prices. It truncates](This_procedure_prepares_bulk_update_of_prices._It_truncates.md) |  |
| * | [DC_PRC_CHG_ITEM table and drops the index.  This is necessary to](DC_PRC_CHG_ITEM_table_and_drops_the_index._This_is_necessary_to.md) |  |
| * | [guarantee that DC will work even after abnormal termination.](guarantee_that_DC_will_work_even_after_abnormal_termination..md) |  |
| * | [exec DC_PREP_PRC_CHG](.exec_DC_PREP_PRC_CHG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [All the data from DC price change item table is deleted.](All_the_data_from_DC_price_change_item_table_is_deleted..md) |  |
| * | [11/01/01 (L. Rubakhin) - Created](11_01_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_PREP_STR_ITM_BULK](dbo.DC_PREP_STR_ITM_BULK.md) | dbo.DC_STORE_ITEM |
| * | [This procedure prepares bulk insert of storeitem data. It truncates](This_procedure_prepares_bulk_insert_of_storeitem_data._It_truncates.md) |  |
| * | [DC_STORE_ITEM table and drops the index.  This is necessary to](DC_STORE_ITEM_table_and_drops_the_index._This_is_necessary_to.md) |  |
| * | [guarantee that DC will work even after abnormal termination.](guarantee_that_DC_will_work_even_after_abnormal_termination..md) |  |
| * | [exec DC_PREP_STR_ITM_BULK](.exec_DC_PREP_STR_ITM_BULK.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [All the data from DC storeitem table is deleted.  This operation is not](All_the_data_from_DC_storeitem_table_is_deleted._This_operation_is_not.md) |  |
| * | [logged.  It means that complete database backup should be performed](logged._It_means_that_complete_database_backup_should_be_performed.md) |  |
| * | [after bulk data is inserted.](after_bulk_data_is_inserted..md) |  |
| * | [This procedure invalidates log backup sequence so the database will](.This_procedure_invalidates_log_backup_sequence_so_the_database_will.md) |  |
| * | [get into log truncate mode. To get the database back out of log](get_into_log_truncate_mode._To_get_the_database_back_out_of_log.md) |  |
| * | [truncate mode the complete database backup should be done after the](.truncate_mode_the_complete_database_backup_should_be_done_after_the.md) |  |
| * | [data import is complete.](data_import_is_complete..md) |  |
| dbo | [DC_RENAME_EQUAL_TAX_ZONE](dbo.DC_RENAME_EQUAL_TAX_ZONE.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [EQUAL_TAX_ZONE->BAK_EQUAL_TAX_ZONE](.EQUAL_TAX_ZONE-_BAK_EQUAL_TAX_ZONE.md) |  |
| * | [TMP_EQUAL_TAX_ZONE->EQUAL_TAX_ZONE](.TMP_EQUAL_TAX_ZONE-_EQUAL_TAX_ZONE.md) |  |
| * | [exec DC_RENAME_EQUAL_TAX_ZONE](.exec_DC_RENAME_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_EQUAL_TAX_ZONE_LANG](dbo.DC_RENAME_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [EQUAL_TAX_ZONE_LANG->BAK_EQUAL_TAX_ZONE_LANG](.EQUAL_TAX_ZONE_LANG-_BAK_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [TMP_EQUAL_TAX_ZONE_LANG->EQUAL_TAX_ZONE_LANG](.TMP_EQUAL_TAX_ZONE_LANG-_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [exec DC_RENAME_EQUAL_TAX_ZONE_LANG](.exec_DC_RENAME_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_ITM](dbo.DC_RENAME_ITM.md) |  |
| * | [This procedure renames temporary item tables and archives old with](.This_procedure_renames_temporary_item_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [ITEM->BAK_ITEM](.ITEM-_BAK_ITEM.md) |  |
| * | [STORE_ITEM->BAK_STORE_ITEM](.STORE_ITEM-_BAK_STORE_ITEM.md) |  |
| * | [ITEM_POS_SELL_RULE->BAK_ITEM_POS_SELL_RULE](.ITEM_POS_SELL_RULE-_BAK_ITEM_POS_SELL_RULE.md) |  |
| * | [ITEM_KEYWORD->BAK_ITEM_KEYWORD](.ITEM_KEYWORD-_BAK_ITEM_KEYWORD.md) |  |
| * | [ITEM_ADDL_INFO->BAK_ITEM_ADDL_INFO](.ITEM_ADDL_INFO-_BAK_ITEM_ADDL_INFO.md) |  |
| * | [TMP_ITEM->ITEM](.TMP_ITEM-_ITEM.md) |  |
| * | [TMP_STORE_ITEM->STORE_ITEM](.TMP_STORE_ITEM-_STORE_ITEM.md) |  |
| * | [TMP_ITEM_POS_SELL_RULE->ITEM_POS_SELL_RULE](.TMP_ITEM_POS_SELL_RULE-_ITEM_POS_SELL_RULE.md) |  |
| * | [TMP_ITEM_KEYWORD->ITEM_KEYWORD](.TMP_ITEM_KEYWORD-_ITEM_KEYWORD.md) |  |
| * | [TMP_ITEM_ADDL_INFO->ITEM_ADDL_INFO](.TMP_ITEM_ADDL_INFO-_ITEM_ADDL_INFO.md) |  |
| * | [exec DC_RENAME_ITM](.exec_DC_RENAME_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [3/27/00 (L. Rubakhin) - Created](3_27_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| * | [10/31/01 (L. Rubakhin) - replaced alert with additional info](10_31_01_L._Rubakhin_-_replaced_alert_with_additional_info.md) |  |
| dbo | [DC_RENAME_PLU](dbo.DC_RENAME_PLU.md) |  |
| * | [This procedure renames temporary plu tables and archives old with](.This_procedure_renames_temporary_plu_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [PLU->BAK_PLU](.PLU-_BAK_PLU.md) |  |
| * | [TMP_PLU->PLU](.TMP_PLU-_PLU.md) |  |
| * | [exec DC_RENAME_PLU](.exec_DC_RENAME_PLU.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| dbo | [DC_RENAME_POS_ADDL_INFO](dbo.DC_RENAME_POS_ADDL_INFO.md) |  |
| * | [This procedure renames temporary pos item alert table](.This_procedure_renames_temporary_pos_item_alert_table.md) |  |
| * | [and archives old with BAK prefix:](.and_archives_old_with_BAK_prefix.md) |  |
| * | [POS_ITEM_ADDL_INFO->BAK_POS_ITEM_ADDL_INFO](.POS_ITEM_ADDL_INFO-_BAK_POS_ITEM_ADDL_INFO.md) |  |
| * | [TMP_POS_ITEM_ADDL_INFO->POS_ITEM_ADDL_INFO](.TMP_POS_ITEM_ADDL_INFO-_POS_ITEM_ADDL_INFO.md) |  |
| * | [exec DC_RENAME_POS_ADDL_INFO](.exec_DC_RENAME_POS_ADDL_INFO.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [10/29/01 (L. Rubakhin) - Created](10_29_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_RENAME_POS_ALERT](dbo.DC_RENAME_POS_ALERT.md) |  |
| * | [This procedure renames temporary pos item alert table](.This_procedure_renames_temporary_pos_item_alert_table.md) |  |
| * | [and archives old with BAK prefix:](.and_archives_old_with_BAK_prefix.md) |  |
| * | [POS_ITEM_ALERT->BAK_POS_ITEM_ALERT](.POS_ITEM_ALERT-_BAK_POS_ITEM_ALERT.md) |  |
| * | [TMP_POS_ITEM_ALERT->POS_ITEM_ALERT](.TMP_POS_ITEM_ALERT-_POS_ITEM_ALERT.md) |  |
| * | [exec DC_RENAME_POS_ALERT](.exec_DC_RENAME_POS_ALERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [4/4/00 (L. Rubakhin) - Created](4_4_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| dbo | [DC_RENAME_SMPL_DISCNT](dbo.DC_RENAME_SMPL_DISCNT.md) |  |
| * | [This procedure renames temporary plu tables and archives old with](.This_procedure_renames_temporary_plu_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [SIMPLE_DISCOUNT->BAK_SIMPLE_DISCOUNT](.SIMPLE_DISCOUNT-_BAK_SIMPLE_DISCOUNT.md) |  |
| * | [TMP_SIMPLE_DISCOUNT->SIMPLE_DISCOUNT](.TMP_SIMPLE_DISCOUNT-_SIMPLE_DISCOUNT.md) |  |
| * | [exec DC_RENAME_SMPL_DISCNT](.exec_DC_RENAME_SMPL_DISCNT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [1/8/02 (L. Rubakhin) - Created](1_8_02_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_RENAME_STR_ITM](dbo.DC_RENAME_STR_ITM.md) |  |
| * | [This procedure renames:](.This_procedure_renames.md) |  |
| * | [exec DC_RENAME_STR_ITM](.exec_DC_RENAME_STR_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| dbo | [DC_RENAME_TAX_AUTHORITY](dbo.DC_RENAME_TAX_AUTHORITY.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAX_AUTHORITY->BAK_TAX_AUTHORITY](.TAX_AUTHORITY-_BAK_TAX_AUTHORITY.md) |  |
| * | [TMP_TAX_AUTHORITY->TAX_AUTHORITY](.TMP_TAX_AUTHORITY-_TAX_AUTHORITY.md) |  |
| * | [exec DC_RENAME_TAX_AUTHORITY](.exec_DC_RENAME_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAX_AUTHORITY_LANG](dbo.DC_RENAME_TAX_AUTHORITY_LANG.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAX_AUTHORITY_LANG->BAK_TAX_AUTHORITY_LANG](.TAX_AUTHORITY_LANG-_BAK_TAX_AUTHORITY_LANG.md) |  |
| * | [TMP_TAX_AUTHORITY_LANG->TAX_AUTHORITY_LANG](.TMP_TAX_AUTHORITY_LANG-_TAX_AUTHORITY_LANG.md) |  |
| * | [exec DC_RENAME_TAX_AUTHORITY_LANG](.exec_DC_RENAME_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAX_EXEMPT_CERT](dbo.DC_RENAME_TAX_EXEMPT_CERT.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAX_EXEMPT_CERT->BAK_TAX_EXEMPT_CERT](.TAX_EXEMPT_CERT-_BAK_TAX_EXEMPT_CERT.md) |  |
| * | [TMP_TAX_EXEMPT_CERT->TAX_EXEMPT_CERT](.TMP_TAX_EXEMPT_CERT-_TAX_EXEMPT_CERT.md) |  |
| * | [exec DC_RENAME_TAX_EXEMPT_CERT](.exec_DC_RENAME_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAX_GRP_ZONE_AUTH](dbo.DC_RENAME_TAX_GRP_ZONE_AUTH.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAX_GRP_ZONE_AUTH->BAK_TAX_GRP_ZONE_AUTH](.TAX_GRP_ZONE_AUTH-_BAK_TAX_GRP_ZONE_AUTH.md) |  |
| * | [TMP_TAX_GRP_ZONE_AUTH->TAX_GRP_ZONE_AUTH](.TMP_TAX_GRP_ZONE_AUTH-_TAX_GRP_ZONE_AUTH.md) |  |
| * | [exec DC_RENAME_TAX_GRP_ZONE_AUTH](.exec_DC_RENAME_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAX_RULE](dbo.DC_RENAME_TAX_RULE.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAX_RULE->BAK_TAX_RULE](.TAX_RULE-_BAK_TAX_RULE.md) |  |
| * | [TMP_TAX_RULE->TAX_RULE](.TMP_TAX_RULE-_TAX_RULE.md) |  |
| * | [exec DC_RENAME_TAX_RULE](.exec_DC_RENAME_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAX_RULE_LANG](dbo.DC_RENAME_TAX_RULE_LANG.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAX_RULE_LANG->BAK_TAX_RULE_LANG](.TAX_RULE_LANG-_BAK_TAX_RULE_LANG.md) |  |
| * | [TMP_TAX_RULE_LANG->TAX_RULE_LANG](.TMP_TAX_RULE_LANG-_TAX_RULE_LANG.md) |  |
| * | [exec DC_RENAME_TAX_RULE_LANG](.exec_DC_RENAME_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAX_SCHEDULE](dbo.DC_RENAME_TAX_SCHEDULE.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAX_SCHEDULE->BAK_TAX_SCHEDULE](.TAX_SCHEDULE-_BAK_TAX_SCHEDULE.md) |  |
| * | [TMP_TAX_SCHEDULE->TAX_SCHEDULE](.TMP_TAX_SCHEDULE-_TAX_SCHEDULE.md) |  |
| * | [exec DC_RENAME_TAX_SCHEDULE](.exec_DC_RENAME_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAX_ZONE_TAX_AUTH](dbo.DC_RENAME_TAX_ZONE_TAX_AUTH.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAX_ZONE_TAX_AUTH->BAK_TAX_ZONE_TAX_AUTH](.TAX_ZONE_TAX_AUTH-_BAK_TAX_ZONE_TAX_AUTH.md) |  |
| * | [TMP_TAX_ZONE_TAX_AUTH->TAX_ZONE_TAX_AUTH](.TMP_TAX_ZONE_TAX_AUTH-_TAX_ZONE_TAX_AUTH.md) |  |
| * | [exec DC_RENAME_TAX_ZONE_TAX_AUTH](.exec_DC_RENAME_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAXABLE_ITEM_GRP](dbo.DC_RENAME_TAXABLE_ITEM_GRP.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAXABLE_ITEM_GRP->BAK_TAXABLE_ITEM_GRP](.TAXABLE_ITEM_GRP-_BAK_TAXABLE_ITEM_GRP.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP->TAXABLE_ITEM_GRP](.TMP_TAXABLE_ITEM_GRP-_TAXABLE_ITEM_GRP.md) |  |
| * | [exec DC_RENAME_TAXABLE_ITEM_GRP](.exec_DC_RENAME_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_TAXABLE_ITEM_GRP_LANG](dbo.DC_RENAME_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [TAXABLE_ITEM_GRP_LANG->BAK_TAXABLE_ITEM_GRP_LANG](.TAXABLE_ITEM_GRP_LANG-_BAK_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP_LANG->TAXABLE_ITEM_GRP_LANG](.TMP_TAXABLE_ITEM_GRP_LANG-_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [exec DC_RENAME_TAXABLE_ITEM_GRP_LANG](.exec_DC_RENAME_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_UPC](dbo.DC_RENAME_UPC.md) |  |
| * | [This procedure renames temporary pos identity table and archives old with](.This_procedure_renames_temporary_pos_identity_table_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [POS_IDENTITY->BAK_POS_IDENTITY](.POS_IDENTITY-_BAK_POS_IDENTITY.md) |  |
| * | [TMP_POS_IDENTITY->POS_IDENTITY](.TMP_POS_IDENTITY-_POS_IDENTITY.md) |  |
| * | [exec DC_RENAME_UPC](.exec_DC_RENAME_UPC.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [3/28/00 (L. Rubakhin) - Created](3_28_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| dbo | [DC_RENAME_UPC_SKU](dbo.DC_RENAME_UPC_SKU.md) |  |
| * | [This procedure renames temporary upc to sku mapping](.This_procedure_renames_temporary_upc_to_sku_mapping.md) |  |
| * | [table and archives old with BAK prefix:](.table_and_archives_old_with_BAK_prefix.md) |  |
| * | [POS_ID_PLU_CODE->BAK_POS_ID_PLU_CODE](.POS_ID_PLU_CODE-_BAK_POS_ID_PLU_CODE.md) |  |
| * | [TMP_POS_ID_PLU_CODE->POS_ID_PLU_CODE](.TMP_POS_ID_PLU_CODE-_POS_ID_PLU_CODE.md) |  |
| * | [exec DC_RENAME_UPC_SKU](.exec_DC_RENAME_UPC_SKU.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [4/4/00 (L. Rubakhin) - Created](4_4_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| dbo | [DC_RENAME_VALUE_ADDED_TAX](dbo.DC_RENAME_VALUE_ADDED_TAX.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [VALUE_ADDED_TAX->BAK_VALUE_ADDED_TAX](.VALUE_ADDED_TAX-_BAK_VALUE_ADDED_TAX.md) |  |
| * | [TMP_VALUE_ADDED_TAX->VALUE_ADDED_TAX](.TMP_VALUE_ADDED_TAX-_VALUE_ADDED_TAX.md) |  |
| * | [exec DC_RENAME_VALUE_ADDED_TAX](.exec_DC_RENAME_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_VALUE_ADDED_TAX_LANG](dbo.DC_RENAME_VALUE_ADDED_TAX_LANG.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [VALUE_ADDED_TAX_LANG->BAK_VALUE_ADDED_TAX_LANG](.VALUE_ADDED_TAX_LANG-_BAK_VALUE_ADDED_TAX_LANG.md) |  |
| * | [TMP_VALUE_ADDED_TAX_LANG->VALUE_ADDED_TAX_LANG](.TMP_VALUE_ADDED_TAX_LANG-_VALUE_ADDED_TAX_LANG.md) |  |
| * | [exec DC_RENAME_VALUE_ADDED_TAX_LANG](.exec_DC_RENAME_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RENAME_ZIP_CODE_TAX_ZONE](dbo.DC_RENAME_ZIP_CODE_TAX_ZONE.md) |  |
| * | [This procedure renames temporary tax rule assign tables and archives old with](.This_procedure_renames_temporary_tax_rule_assign_tables_and_archives_old_with.md) |  |
| * | [BAK prefix:](.BAK_prefix.md) |  |
| * | [ZIP_CODE_TAX_ZONE->BAK_ZIP_CODE_TAX_ZONE](.ZIP_CODE_TAX_ZONE-_BAK_ZIP_CODE_TAX_ZONE.md) |  |
| * | [TMP_ZIP_CODE_TAX_ZONE->ZIP_CODE_TAX_ZONE](.TMP_ZIP_CODE_TAX_ZONE-_ZIP_CODE_TAX_ZONE.md) |  |
| * | [exec DC_RENAME_ZIP_CODE_TAX_ZONE](.exec_DC_RENAME_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RESUME_ITEM_REPL](dbo.DC_RESUME_ITEM_REPL.md) | dbo.RPL_PUB_SUB, dbo.RPL_RUN_DISTR_AGENTS, dbo.RPL_RUN_SNAPSHOT_AGENTS_SYNC |
| dbo | [DC_RPL_EQUAL_TAX_ZONE](dbo.DC_RPL_EQUAL_TAX_ZONE.md) | dbo.DC_EQUAL_TAX_ZONE, dbo.TMP_EQUAL_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE table from the](.TMP_EQUAL_TAX_ZONE_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE table.](DC_EQUAL_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_table.md) |  |
| * | [are replacements to the EQUAL_TAX_ZONE table.](are_replacements_to_the_EQUAL_TAX_ZONE_table..md) |  |
| * | [DC_RPL_EQUAL_TAX_ZONE](.DC_RPL_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_EQUAL_TAX_ZONE_LANG](dbo.DC_RPL_EQUAL_TAX_ZONE_LANG.md) | dbo.DC_EQUAL_TAX_ZONE_LANG, dbo.EQUAL_TAX_ZONE, dbo.LANGUAGE, dbo.TMP_EQUAL_TAX_ZONE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE_LANG table from the](.TMP_EQUAL_TAX_ZONE_LANG_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE_LANG table.](DC_EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE_LANG table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_LANG_table.md) |  |
| * | [are replacements to the EQUAL_TAX_ZONE_LANG table.](are_replacements_to_the_EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [DC_RPL_EQUAL_TAX_ZONE_LANG](.DC_RPL_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_ITEM](dbo.DC_RPL_ITEM.md) | dbo.CATEGORY, dbo.CLASS, dbo.COLOR, dbo.DC_ITEM, dbo.DEPARTMENT, dbo.ITEM, dbo.LIFE_STYLE, dbo.SEASON, dbo.SIZE, dbo.STYLE, dbo.SUB_CATEGORY, dbo.SUB_CLASS, dbo.SUB_DEPARTMENT, dbo.TMP_ITEM |
| * | [This procedure inserts data from DC_ITEM to TMP_ITEM](.This_procedure_inserts_data_from_DC_ITEM_to_TMP_ITEM.md) |  |
| * | [table.  The assumption is that items in DC_ITEM table](table._The_assumption_is_that_items_in_DC_ITEM_table.md) |  |
| * | [are to replace items in ITEM table.](are_to_replace_items_in_ITEM_table..md) |  |
| * | [@PRM_DIV](.@PRM_DIV.md) |  |
| * | [@PRM_DEL](.@PRM_DEL.md) |  |
| * | [exec DC_RPL_ITEM 0, 1](.exec_DC_RPL_ITEM_0,_1.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure is used in replace all scenario.](This_procedure_is_used_in_replace_all_scenario..md) |  |
| * | [UPDATE_CODE:](.UPDATE_CODE.md) |  |
| * | [3/21/00 (L. Rubakhin) - Created](3_21_00_L._Rubakhin_-_Created.md) |  |
| * | [8/9/01 (L. Rubakhin) - Added Association Group](8_9_01_L._Rubakhin_-_Added_Association_Group.md) |  |
| * | [10/18/01 (L. Rubakhin) - Added tender type id and activate flag](10_18_01_L._Rubakhin_-_Added_tender_type_id_and_activate_flag.md) |  |
| * | [12/13/2002 ( Madhulika Sharma ) - Field Item_type_code is filled correctly now for issue# 86936.](12_13_2002_Madhulika_Sharma_-_Field_Item_type_code_is_filled_correctly_now_for_issue#_86936..md) |  |
| * | [3/24/05 (L. Rubakhin) - Added buy back price, defective item action code,](3_24_05_L._Rubakhin_-_Added_buy_back_price,_defective_item_action_code,.md) |  |
| dbo | [DC_RPL_ITM_ADDL_INFO](dbo.DC_RPL_ITM_ADDL_INFO.md) | dbo.DC_ITEM, dbo.TMP_ITEM_ADDL_INFO |
| * | [This procedure inserts data from DC_ITEM to TMP_ITEM_ADDL_INFO](.This_procedure_inserts_data_from_DC_ITEM_to_TMP_ITEM_ADDL_INFO.md) |  |
| * | [table.  The assumption is that items in DC_ITEM table](table._The_assumption_is_that_items_in_DC_ITEM_table.md) |  |
| * | [are to replace items in ITEM table.  In this replace mode](are_to_replace_items_in_ITEM_table._In_this_replace_mode.md) |  |
| * | [we do not insert discountinued item into TMP_ITEM_ADDL_INFO.](we_do_not_insert_discountinued_item_into_TMP_ITEM_ADDL_INFO..md) |  |
| * | [exec DC_RPL_ITM_ADDL_INFO](.exec_DC_RPL_ITM_ADDL_INFO.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure is used in replace all scenario.](This_procedure_is_used_in_replace_all_scenario..md) |  |
| * | [10/30/01 (L. Rubakhin) - Created](10_30_01_L._Rubakhin_-_Created.md) |  |
| * | [9/27/05 (L. Rubakhin) - Added CIRCUMSTANCE_NO and ITEM_GROUP_ID to TMP_ITEM_ADDL_INFO](9_27_05_L._Rubakhin_-_Added_CIRCUMSTANCE_NO_and_ITEM_GROUP_ID_to_TMP_ITEM_ADDL_INFO.md) |  |
| dbo | [DC_RPL_ITM_ALERT](dbo.DC_RPL_ITM_ALERT.md) | dbo.DC_ITEM, dbo.TMP_ITEM_ALERT |
| * | [This procedure inserts data from DC_ITEM to TMP_ITEM_ALERT](.This_procedure_inserts_data_from_DC_ITEM_to_TMP_ITEM_ALERT.md) |  |
| * | [table.  The assumption is that items in DC_ITEM table](table._The_assumption_is_that_items_in_DC_ITEM_table.md) |  |
| * | [are to replace items in ITEM table.  In this replace mode](are_to_replace_items_in_ITEM_table._In_this_replace_mode.md) |  |
| * | [we do not insert discountinued item into TMP_ITEM_ALERT.](we_do_not_insert_discountinued_item_into_TMP_ITEM_ALERT..md) |  |
| * | [exec DC_RPL_ITM_ALERT](.exec_DC_RPL_ITM_ALERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure is used in replace all scenario.](This_procedure_is_used_in_replace_all_scenario..md) |  |
| * | [3/27/00 (L. Rubakhin) - Created](3_27_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_RPL_ITM_KYWRD](dbo.DC_RPL_ITM_KYWRD.md) | dbo.DC_ITEM, dbo.TMP_ITEM_KEYWORD |
| * | [This procedure inserts data from DC_ITEM to TMP_ITEM_KEYWORD](.This_procedure_inserts_data_from_DC_ITEM_to_TMP_ITEM_KEYWORD.md) |  |
| * | [table.  The assumption is that items in DC_ITEM table](table._The_assumption_is_that_items_in_DC_ITEM_table.md) |  |
| * | [are to replace items in ITEM table.  In this replace mode](are_to_replace_items_in_ITEM_table._In_this_replace_mode.md) |  |
| * | [we do not insert discountinued item into TMP_ITEM_KEYWORD](.we_do_not_insert_discountinued_item_into_TMP_ITEM_KEYWORD.md) |  |
| * | [exec DC_RPL_ITM_KYWRD](.exec_DC_RPL_ITM_KYWRD.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure is used in replace all scenario.](This_procedure_is_used_in_replace_all_scenario..md) |  |
| * | [3/28/00 (L. Rubakhin) - Created](3_28_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_RPL_PLU](dbo.DC_RPL_PLU.md) | dbo.CATEGORY, dbo.CLASS, dbo.COLOR, dbo.ITEM, dbo.ITEM_ADDL_INFO, dbo.ITEM_POS_SELL_RULE, dbo.SEASON, dbo.SIZE, dbo.SPIFF_DEFINITION, dbo.STORE_ITEM, dbo.STYLE, dbo.SUB_CATEGORY, dbo.SUB_CLASS, dbo.SUB_DEPARTMENT, dbo.TMP_PLU |
| * | [This procedure populates TMP_PLU table from item tables.](This_procedure_populates_TMP_PLU_table_from_item_tables..md) |  |
| * | [No old PLU records are moved to TMP_PLU table.](No_old_PLU_records_are_moved_to_TMP_PLU_table..md) |  |
| * | [@PRM_PKTYPE - type of PK for PLU table](.@PRM_PKTYPE_-_type_of_PK_for_PLU_table.md) |  |
| * | [@PRM_STORE_NO - store number to use for generation of PLU file](.@PRM_STORE_NO_-_store_number_to_use_for_generation_of_PLU_file.md) |  |
| * | [@ACTIVE_ITEMS_ONLY - flag that shows that only active ITEMs are](.@ACTIVE_ITEMS_ONLY_-_flag_that_shows_that_only_active_ITEMs_are.md) |  |
| * | [exec DC_RPL_PLU 'SKU'](.exec_DC_RPL_PLU_'SKU'.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| * | [5/11/00 (L. Rubakhin) - Added @PRM_PKTYPE](5_11_00_L._Rubakhin_-_Added_@PRM_PKTYPE.md) |  |
| * | [10/19/00 (L. Rubakhin) - Added spiff support](10_19_00_L._Rubakhin_-_Added_spiff_support.md) |  |
| * | [8/9/01 (L. Rubakhin) - Added association group](8_9_01_L._Rubakhin_-_Added_association_group.md) |  |
| * | [10/18/01 (L. Rubakhin) - Added Alert flag logic and](10_18_01_L._Rubakhin_-_Added_Alert_flag_logic_and.md) |  |
| * | [10/31/01 (L. Rubakhin) - replaced alert flag with addl info](10_31_01_L._Rubakhin_-_replaced_alert_flag_with_addl_info.md) |  |
| * | [12/14/01 (L. Rubakhin) - Added store number parameter](12_14_01_L._Rubakhin_-_Added_store_number_parameter.md) |  |
| * | [1/9/02 (L. Rubakhin) - If compare price is not set](1_9_02_L._Rubakhin_-_If_compare_price_is_not_set.md) |  |
| * | [11/20/02 (L. Rubakhin) - Added 6 fields to PLU table](11_20_02_L._Rubakhin_-_Added_6_fields_to_PLU_table.md) |  |
| * | [02/09/04 (L. Rubakhin) - Added 5 fields to PLU table](02_09_04_L._Rubakhin_-_Added_5_fields_to_PLU_table.md) |  |
| * | [07/07/04 (L. Rubakhin) - Added ITEM_DESC field to PLU table](07_07_04_L._Rubakhin_-_Added_ITEM_DESC_field_to_PLU_table.md) |  |
| * | [3/24/05 (L. Rubakhin) - Added buy back price, defective item action code,](3_24_05_L._Rubakhin_-_Added_buy_back_price,_defective_item_action_code,.md) |  |
| * | [5/19/05 (L. Rubakhin) - Added STORE_NO filter to ITEM_POS_SELL_RULE join](5_19_05_L._Rubakhin_-_Added_STORE_NO_filter_to_ITEM_POS_SELL_RULE_join.md) |  |
| * | [10/28/05 (L. Rubakhin) - Added ITEM_STATUS_CODE and @ACTIVE_ITEM_ONLY parameter](10_28_05_L._Rubakhin_-_Added_ITEM_STATUS_CODE_and_@ACTIVE_ITEM_ONLY_parameter.md) |  |
| * | [3/18/11 (L. Rubakhin) - Added COST to PLU table](3_18_11_L._Rubakhin_-_Added_COST_to_PLU_table.md) |  |
| * | [10/21/14 (L. Rubakhin) - Added INVOICEABLE_FLG](10_21_14_L._Rubakhin_-_Added_INVOICEABLE_FLG.md) |  |
| * | [2/29/15 (O. Blevins) - Restored LOYALTY_DSCNT_FLG](2_29_15_O._Blevins_-_Restored_LOYALTY_DSCNT_FLG.md) |  |
| dbo | [DC_RPL_POS_ADDL_INFO](dbo.DC_RPL_POS_ADDL_INFO.md) | dbo.ITEM, dbo.ITEM_ADDL_INFO, dbo.TMP_POS_ITEM_ADDL_INFO |
| * | [This procedure populates TMP_POS_ITEM_ADDL_INFO table from ITEM_ADDL_INFO.](This_procedure_populates_TMP_POS_ITEM_ADDL_INFO_table_from_ITEM_ADDL_INFO..md) |  |
| * | [No old ADDL_INFO records are moved to TMP_POS_ITEM_ADDL_INFO table.](No_old_ADDL_INFO_records_are_moved_to_TMP_POS_ITEM_ADDL_INFO_table..md) |  |
| * | [@PRM_PKTYPE - type of PK for PLU table](.@PRM_PKTYPE_-_type_of_PK_for_PLU_table.md) |  |
| * | [exec DC_RPL_POS_ADDL_INFO 'SKU'](.exec_DC_RPL_POS_ADDL_INFO_'SKU'.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [5/30/01 (L. Rubakhin) - Created](5_30_01_L._Rubakhin_-_Created.md) |  |
| * | [9/27/05 (L. Rubakhin) - Added CIRCUMSTANCE_NO and ITEM_GROUP_ID to TMP_POS_ITEM_ADDL_INFO](9_27_05_L._Rubakhin_-_Added_CIRCUMSTANCE_NO_and_ITEM_GROUP_ID_to_TMP_POS_ITEM_ADDL_INFO.md) |  |
| dbo | [DC_RPL_POS_ALERT](dbo.DC_RPL_POS_ALERT.md) | dbo.ITEM, dbo.ITEM_ALERT, dbo.TMP_POS_ITEM_ALERT |
| * | [This procedure populates TMP_POS_ITEM_ALERT table from ITEM_ALERT.](This_procedure_populates_TMP_POS_ITEM_ALERT_table_from_ITEM_ALERT..md) |  |
| * | [No old ALERT records are moved to TMP_POS_ITEM_ALERT table.](No_old_ALERT_records_are_moved_to_TMP_POS_ITEM_ALERT_table..md) |  |
| * | [@PRM_PKTYPE - type of PK for PLU table](.@PRM_PKTYPE_-_type_of_PK_for_PLU_table.md) |  |
| * | [exec DC_RPL_POS_ALERT 'SKU'](.exec_DC_RPL_POS_ALERT_'SKU'.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [4/4/00 (L. Rubakhin) - Created](4_4_00_L._Rubakhin_-_Created.md) |  |
| * | [5/11/00 (L. Rubakhin) - Added @PRM_PKTYPE](5_11_00_L._Rubakhin_-_Added_@PRM_PKTYPE.md) |  |
| dbo | [DC_RPL_POS_RULE](dbo.DC_RPL_POS_RULE.md) | dbo.DC_ITEM, dbo.SPIFF_DEFINITION, dbo.TMP_ITEM_POS_SELL_RULE |
| * | [This procedure inserts data from DC_ITEM to TMP_ITEM_POS_SELL_RULE](.This_procedure_inserts_data_from_DC_ITEM_to_TMP_ITEM_POS_SELL_RULE.md) |  |
| * | [table.  The assumption is that items in DC_ITEM table](table._The_assumption_is_that_items_in_DC_ITEM_table.md) |  |
| * | [are to replace items in ITEM table.  In this replace mode](are_to_replace_items_in_ITEM_table._In_this_replace_mode.md) |  |
| * | [we do not insert discountinued item into TMP_ITEM_POS_SELL_RULE.](we_do_not_insert_discountinued_item_into_TMP_ITEM_POS_SELL_RULE..md) |  |
| * | [@PRM_STORE_NO - Store Number](.@PRM_STORE_NO_-_Store_Number.md) |  |
| * | [exec DC_RPL_POS_RULE](.exec_DC_RPL_POS_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure is used in replace all scenario.](This_procedure_is_used_in_replace_all_scenario..md) |  |
| * | [3/27/00 (L. Rubakhin) - Created](3_27_00_L._Rubakhin_-_Created.md) |  |
| * | [10/19/00 (L. Rubakhin) - Added spiff support](10_19_00_L._Rubakhin_-_Added_spiff_support.md) |  |
| * | [10/19/01 (L. Rubakhin) - Added price auth amount](10_19_01_L._Rubakhin_-_Added_price_auth_amount.md) |  |
| * | [10/21/14 (L. Rubakhin) - Added INVOICEABLE_FLG](10_21_14_L._Rubakhin_-_Added_INVOICEABLE_FLG.md) |  |
| * | [2/29/15 (O. Blevins) - Restored LOYALTY_DSCNT_FLG](2_29_15_O._Blevins_-_Restored_LOYALTY_DSCNT_FLG.md) |  |
| dbo | [DC_RPL_STR_ITEM](dbo.DC_RPL_STR_ITEM.md) | dbo.AGE_RESTRICT_GRP, dbo.DC_STORE_ITEM, dbo.ITEM, dbo.SPCL_RESTRICT_GRP, dbo.TMP_STORE_ITEM |
| * | [This procedure inserts data from DC_STORE_ITEM to TMP_STORE_ITEM](.This_procedure_inserts_data_from_DC_STORE_ITEM_to_TMP_STORE_ITEM.md) |  |
| * | [table.  The assumption is that items in DC_STORE_ITEM table](table._The_assumption_is_that_items_in_DC_STORE_ITEM_table.md) |  |
| * | [are to replace items in STORE_ITEM table.  In this replace mode](are_to_replace_items_in_STORE_ITEM_table._In_this_replace_mode.md) |  |
| * | [we do not insert discountinued item into TMP_STORE_ITEM.](we_do_not_insert_discountinued_item_into_TMP_STORE_ITEM..md) |  |
| * | [exec DC_RPL_STR_ITEM](.exec_DC_RPL_STR_ITEM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure is used in replace all scenario.](This_procedure_is_used_in_replace_all_scenario..md) |  |
| * | [12/12/01 (Radhika Jayanti) Modified age and special restriction join](.12_12_01_Radhika_Jayanti_Modified_age_and_special_restriction_join.md) |  |
| * | [02/21/02  (Radhika Jayanti) Added GlobalPermanentPriceDominance parameter](.02_21_02_Radhika_Jayanti_Added_GlobalPermanentPriceDominance_parameter.md) |  |
| * | [04/20/11 (Leonid Rubakhin) Added TaxGroupId to store item dataconnect.](04_20_11_Leonid_Rubakhin_Added_TaxGroupId_to_store_item_dataconnect..md) |  |
| dbo | [DC_RPL_STR_ITM](dbo.DC_RPL_STR_ITM.md) | dbo.AGE_RESTRICT_GRP, dbo.DC_ITEM, dbo.SPCL_RESTRICT_GRP, dbo.TMP_STORE_ITEM |
| * | [This procedure inserts data from DC_ITEM to TMP_STORE_ITEM](.This_procedure_inserts_data_from_DC_ITEM_to_TMP_STORE_ITEM.md) |  |
| * | [table.  The assumption is that items in DC_ITEM table](table._The_assumption_is_that_items_in_DC_ITEM_table.md) |  |
| * | [are to replace items in ITEM table.  In this replace mode](are_to_replace_items_in_ITEM_table._In_this_replace_mode.md) |  |
| * | [we do not insert discountinued item into TMP_STORE_ITEM.](we_do_not_insert_discountinued_item_into_TMP_STORE_ITEM..md) |  |
| * | [Also local price is set to NULL.](Also_local_price_is_set_to_NULL..md) |  |
| * | [@PRM_STORE_NO - Store Number](.@PRM_STORE_NO_-_Store_Number.md) |  |
| * | [exec DC_RPL_STR_ITM 0](.exec_DC_RPL_STR_ITM_0.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure is used in replace all scenario.](This_procedure_is_used_in_replace_all_scenario..md) |  |
| * | [3/27/00 (L. Rubakhin) - Created](3_27_00_L._Rubakhin_-_Created.md) |  |
| * | [4/21/00 (L. Rubakhin) - Added support for item status](4_21_00_L._Rubakhin_-_Added_support_for_item_status.md) |  |
| dbo | [DC_RPL_TAX_AUTHORITY](dbo.DC_RPL_TAX_AUTHORITY.md) | dbo.DC_TAX_AUTHORITY, dbo.TMP_TAX_AUTHORITY |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY table from the](.TMP_TAX_AUTHORITY_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY table.](DC_TAX_AUTHORITY_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY table](.The_records_in_the_TMP_TAX_AUTHORITY_table.md) |  |
| * | [are replacements to the TAX_AUTHORITY table.](are_replacements_to_the_TAX_AUTHORITY_table..md) |  |
| * | [DC_RPL_TAX_AUTHORITY](.DC_RPL_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_TAX_AUTHORITY_LANG](dbo.DC_RPL_TAX_AUTHORITY_LANG.md) | dbo.DC_TAX_AUTHORITY_LANG, dbo.LANGUAGE, dbo.TAX_AUTHORITY, dbo.TMP_TAX_AUTHORITY_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY_LANG table from the](.TMP_TAX_AUTHORITY_LANG_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY_LANG table.](DC_TAX_AUTHORITY_LANG_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY_LANG table](.The_records_in_the_TMP_TAX_AUTHORITY_LANG_table.md) |  |
| * | [are replacements to the TAX_AUTHORITY_LANG table.](are_replacements_to_the_TAX_AUTHORITY_LANG_table..md) |  |
| * | [DC_RPL_TAX_AUTHORITY_LANG](.DC_RPL_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_TAX_EXEMPT_CERT](dbo.DC_RPL_TAX_EXEMPT_CERT.md) | dbo.CUSTOMER, dbo.DC_TAX_EXEMPT_CERT, dbo.TMP_TAX_EXEMPT_CERT |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_EXEMPT_CERT table from the](.TMP_TAX_EXEMPT_CERT_table_from_the.md) |  |
| * | [DC_TAX_EXEMPT_CERT table.](DC_TAX_EXEMPT_CERT_table..md) |  |
| * | [The records in the TMP_TAX_EXEMPT_CERT table](.The_records_in_the_TMP_TAX_EXEMPT_CERT_table.md) |  |
| * | [are replacements to the TAX_EXEMPT_CERT table.](are_replacements_to_the_TAX_EXEMPT_CERT_table..md) |  |
| * | [DC_RPL_TAX_EXEMPT_CERT](.DC_RPL_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_TAX_GRP_ZONE_AUTH](dbo.DC_RPL_TAX_GRP_ZONE_AUTH.md) | dbo.DC_TAX_GRP_ZONE_AUTH, dbo.EQUAL_TAX_ZONE, dbo.TAX_AUTHORITY, dbo.TAX_EXEMPT_CERT, dbo.TAX_RULE, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAX_GRP_ZONE_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_GRP_ZONE_AUTH table from the](.TMP_TAX_GRP_ZONE_AUTH_table_from_the.md) |  |
| * | [DC_TAX_GRP_ZONE_AUTH table.](DC_TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_GRP_ZONE_AUTH table](.The_records_in_the_TMP_TAX_GRP_ZONE_AUTH_table.md) |  |
| * | [are replacements to the TAX_GRP_ZONE_AUTH table.](are_replacements_to_the_TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [DC_RPL_TAX_GRP_ZONE_AUTH](.DC_RPL_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| * | [4/4/13 (O. Blevins) - Fixed referential integrity for tax exemptions](4_4_13_O._Blevins_-_Fixed_referential_integrity_for_tax_exemptions.md) |  |
| dbo | [DC_RPL_TAX_RULE](dbo.DC_RPL_TAX_RULE.md) | dbo.DC_TAX_RULE, dbo.TMP_TAX_RULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE table from the](.TMP_TAX_RULE_table_from_the.md) |  |
| * | [DC_TAX_RULE table.](DC_TAX_RULE_table..md) |  |
| * | [The records in the TMP_TAX_RULE table](.The_records_in_the_TMP_TAX_RULE_table.md) |  |
| * | [are replacements to the TAX_RULE table.](are_replacements_to_the_TAX_RULE_table..md) |  |
| * | [DC_RPL_TAX_RULE](.DC_RPL_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_TAX_RULE_LANG](dbo.DC_RPL_TAX_RULE_LANG.md) | dbo.DC_TAX_RULE_LANG, dbo.LANGUAGE, dbo.TAX_RULE, dbo.TMP_TAX_RULE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE_LANG table from the](.TMP_TAX_RULE_LANG_table_from_the.md) |  |
| * | [DC_TAX_RULE_LANG table.](DC_TAX_RULE_LANG_table..md) |  |
| * | [The records in the TMP_TAX_RULE_LANG table](.The_records_in_the_TMP_TAX_RULE_LANG_table.md) |  |
| * | [are replacements to the TAX_RULE_LANG table.](are_replacements_to_the_TAX_RULE_LANG_table..md) |  |
| * | [DC_RPL_TAX_RULE_LANG](.DC_RPL_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_TAX_SCHEDULE](dbo.DC_RPL_TAX_SCHEDULE.md) | dbo.DC_TAX_SCHEDULE, dbo.TAX_RULE, dbo.TMP_TAX_SCHEDULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_SCHEDULE table from the](.TMP_TAX_SCHEDULE_table_from_the.md) |  |
| * | [DC_TAX_SCHEDULE table.](DC_TAX_SCHEDULE_table..md) |  |
| * | [The records in the TMP_TAX_SCHEDULE table](.The_records_in_the_TMP_TAX_SCHEDULE_table.md) |  |
| * | [are replacements to the TAX_SCHEDULE table.](are_replacements_to_the_TAX_SCHEDULE_table..md) |  |
| * | [DC_RPL_TAX_SCHEDULE](.DC_RPL_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_TAX_ZONE_TAX_AUTH](dbo.DC_RPL_TAX_ZONE_TAX_AUTH.md) | dbo.DC_TAX_ZONE_TAX_AUTH, dbo.EQUAL_TAX_ZONE, dbo.TAX_AUTHORITY, dbo.TMP_TAX_ZONE_TAX_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_ZONE_TAX_AUTH table from the](.TMP_TAX_ZONE_TAX_AUTH_table_from_the.md) |  |
| * | [DC_TAX_ZONE_TAX_AUTH table.](DC_TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_ZONE_TAX_AUTH table](.The_records_in_the_TMP_TAX_ZONE_TAX_AUTH_table.md) |  |
| * | [are replacements to the TAX_ZONE_TAX_AUTH table.](are_replacements_to_the_TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [DC_RPL_TAX_ZONE_TAX_AUTH](.DC_RPL_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_TAXABLE_ITEM_GRP](dbo.DC_RPL_TAXABLE_ITEM_GRP.md) | dbo.DC_TAXABLE_ITEM_GRP, dbo.TMP_TAXABLE_ITEM_GRP |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP table from the](.TMP_TAXABLE_ITEM_GRP_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP table.](DC_TAXABLE_ITEM_GRP_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_table.md) |  |
| * | [are replacements to the TAXABLE_ITEM_GRP table.](are_replacements_to_the_TAXABLE_ITEM_GRP_table..md) |  |
| * | [DC_RPL_TAXABLE_ITEM_GRP](.DC_RPL_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_TAXABLE_ITEM_GRP_LANG](dbo.DC_RPL_TAXABLE_ITEM_GRP_LANG.md) | dbo.DC_TAXABLE_ITEM_GRP_LANG, dbo.LANGUAGE, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAXABLE_ITEM_GRP_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP_LANG table from the](.TMP_TAXABLE_ITEM_GRP_LANG_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP_LANG table.](DC_TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP_LANG table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_LANG_table.md) |  |
| * | [are replacements to the TAXABLE_ITEM_GRP_LANG table.](are_replacements_to_the_TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [DC_RPL_TAXABLE_ITEM_GRP_LANG](.DC_RPL_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_UPC_SKU](dbo.DC_RPL_UPC_SKU.md) | dbo.ITEM, dbo.POS_IDENTITY, dbo.TMP_POS_ID_PLU_CODE |
| * | [This procedure populates TMP_POS_ID_PLU_CODE table from POS_IDENTITY.](This_procedure_populates_TMP_POS_ID_PLU_CODE_table_from_POS_IDENTITY..md) |  |
| * | [No old PLU records are moved to TMP_PLU table.](No_old_PLU_records_are_moved_to_TMP_PLU_table..md) |  |
| * | [@PRM_PKTYPE - type of PK for PLU table](.@PRM_PKTYPE_-_type_of_PK_for_PLU_table.md) |  |
| * | [exec DC_RPL_UPC_SKU 'SKU'](.exec_DC_RPL_UPC_SKU_'SKU'.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| * | [5/11/00 (L. Rubakhin) - Added @PRM_PKTYPE](5_11_00_L._Rubakhin_-_Added_@PRM_PKTYPE.md) |  |
| dbo | [DC_RPL_VALUE_ADDED_TAX](dbo.DC_RPL_VALUE_ADDED_TAX.md) | dbo.DC_VALUE_ADDED_TAX, dbo.TMP_VALUE_ADDED_TAX |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX table from the](.TMP_VALUE_ADDED_TAX_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX table.](DC_VALUE_ADDED_TAX_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX table](.The_records_in_the_TMP_VALUE_ADDED_TAX_table.md) |  |
| * | [are replacements to the VALUE_ADDED_TAX table.](are_replacements_to_the_VALUE_ADDED_TAX_table..md) |  |
| * | [DC_RPL_VALUE_ADDED_TAX](.DC_RPL_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_VALUE_ADDED_TAX_LANG](dbo.DC_RPL_VALUE_ADDED_TAX_LANG.md) | dbo.DC_VALUE_ADDED_TAX_LANG, dbo.LANGUAGE, dbo.TMP_VALUE_ADDED_TAX_LANG, dbo.VALUE_ADDED_TAX |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX_LANG table from the](.TMP_VALUE_ADDED_TAX_LANG_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX_LANG table.](DC_VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX_LANG table](.The_records_in_the_TMP_VALUE_ADDED_TAX_LANG_table.md) |  |
| * | [are replacements to the VALUE_ADDED_TAX_LANG table.](are_replacements_to_the_VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [DC_RPL_VALUE_ADDED_TAX_LANG](.DC_RPL_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_RPL_ZIP_CODE_TAX_ZONE](dbo.DC_RPL_ZIP_CODE_TAX_ZONE.md) | dbo.DC_CHK_ZIP_CODE_TAX_ZONE_OVRLP, dbo.DC_ZIP_CODE_TAX_ZONE, dbo.EQUAL_TAX_ZONE, dbo.TMP_ZIP_CODE_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_ZIP_CODE_TAX_ZONE table from the](.TMP_ZIP_CODE_TAX_ZONE_table_from_the.md) |  |
| * | [DC_ZIP_CODE_TAX_ZONE table.](DC_ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_ZIP_CODE_TAX_ZONE table](.The_records_in_the_TMP_ZIP_CODE_TAX_ZONE_table.md) |  |
| * | [are replacements to the ZIP_CODE_TAX_ZONE table.](are_replacements_to_the_ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [DC_RPL_ZIP_CODE_TAX_ZONE](.DC_RPL_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_SMPL_DISCNT_ERR](dbo.DC_SMPL_DISCNT_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_SMPL_DISCNT_ERR](.exec_DC_SMPL_DISCNT_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [1/8/02 (L. Rubakhin) - Created](1_8_02_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_STK_ITM_ERR](dbo.DC_STK_ITM_ERR.md) | dbo.DC_STOCK_ITEM |
| * | [This procedure cleans up in the case of error.  It purges](This_procedure_cleans_up_in_the_case_of_error._It_purges.md) |  |
| * | [DC_STOCK_ITEM table and drops the index.](DC_STOCK_ITEM_table_and_drops_the_index..md) |  |
| * | [exec DC_STK_ITM_ERR](.exec_DC_STK_ITM_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [All the data from DC stock item table is deleted.](All_the_data_from_DC_stock_item_table_is_deleted..md) |  |
| * | [4/25/00 (L. Rubakhin) - Created](4_25_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_STR_ITM_ERR](dbo.DC_STR_ITM_ERR.md) | dbo.DC_STORE_ITEM |
| * | [This procedure cleans up in the case of error.  It purges](This_procedure_cleans_up_in_the_case_of_error._It_purges.md) |  |
| * | [DC_STORE_ITEM table and drops the index. It also drops the temporary](DC_STORE_ITEM_table_and_drops_the_index._It_also_drops_the_temporary.md) |  |
| * | [tables.](tables..md) |  |
| * | [exec DC_STR_ITM_ERR](.exec_DC_STR_ITM_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [All the data from DC store item table is deleted.  This operation is not](All_the_data_from_DC_store_item_table_is_deleted._This_operation_is_not.md) |  |
| * | [logged.  It means that complete database backup should be performed](logged._It_means_that_complete_database_backup_should_be_performed.md) |  |
| * | [after bulk data is inserted.](after_bulk_data_is_inserted..md) |  |
| dbo | [DC_SUSPEND_ITEM_REPL](dbo.DC_SUSPEND_ITEM_REPL.md) | dbo.syspublications |
| dbo | [DC_TAX_AUTHORITY_ERR](dbo.DC_TAX_AUTHORITY_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAX_AUTHORITY_ERR](.exec_DC_TAX_AUTHORITY_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAX_AUTHORITY_LANG_ERR](dbo.DC_TAX_AUTHORITY_LANG_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAX_AUTHORITY_LANG_ERR](.exec_DC_TAX_AUTHORITY_LANG_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAX_EXEMPT_CERT_ERR](dbo.DC_TAX_EXEMPT_CERT_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAX_EXEMPT_CERT_ERR](.exec_DC_TAX_EXEMPT_CERT_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAX_GRP_ZONE_AUTH_ERR](dbo.DC_TAX_GRP_ZONE_AUTH_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAX_GRP_ZONE_AUTH_ERR](.exec_DC_TAX_GRP_ZONE_AUTH_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAX_RULE_ERR](dbo.DC_TAX_RULE_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAX_RULE_ERR](.exec_DC_TAX_RULE_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAX_RULE_LANG_ERR](dbo.DC_TAX_RULE_LANG_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAX_RULE_LANG_ERR](.exec_DC_TAX_RULE_LANG_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAX_SCHEDULE_ERR](dbo.DC_TAX_SCHEDULE_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAX_SCHEDULE_ERR](.exec_DC_TAX_SCHEDULE_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAX_ZONE_TAX_AUTH_ERR](dbo.DC_TAX_ZONE_TAX_AUTH_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAX_ZONE_TAX_AUTH_ERR](.exec_DC_TAX_ZONE_TAX_AUTH_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAXABLE_ITEM_GRP_ERR](dbo.DC_TAXABLE_ITEM_GRP_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAXABLE_ITEM_GRP_ERR](.exec_DC_TAXABLE_ITEM_GRP_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_TAXABLE_ITEM_GRP_LANG_ERR](dbo.DC_TAXABLE_ITEM_GRP_LANG_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_TAXABLE_ITEM_GRP_LANG_ERR](.exec_DC_TAXABLE_ITEM_GRP_LANG_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UNDO_RENAME_ITM](dbo.DC_UNDO_RENAME_ITM.md) |  |
| * | [This procedure restores archived old item tables:](.This_procedure_restores_archived_old_item_tables.md) |  |
| * | [BAK_ITEM->ITEM](.BAK_ITEM-_ITEM.md) |  |
| * | [BAK_STORE_ITEM->STORE_ITEM](.BAK_STORE_ITEM-_STORE_ITEM.md) |  |
| * | [BAK_ITEM_POS_SELL_RULE->ITEM_POS_SELL_RULE](.BAK_ITEM_POS_SELL_RULE-_ITEM_POS_SELL_RULE.md) |  |
| * | [BAK_ITEM_KEYWORD->ITEM_KEYWORD](.BAK_ITEM_KEYWORD-_ITEM_KEYWORD.md) |  |
| * | [BAK_ITEM_ADDL_INFO->ITEM_ADDL_INFO](.BAK_ITEM_ADDL_INFO-_ITEM_ADDL_INFO.md) |  |
| * | [ITEM->TMP_ITEM](.ITEM-_TMP_ITEM.md) |  |
| * | [STORE_ITEM->TMP_STORE_ITEM](.STORE_ITEM-_TMP_STORE_ITEM.md) |  |
| * | [ITEM_POS_SELL_RULE->TMP_ITEM_POS_SELL_RULE](.ITEM_POS_SELL_RULE-_TMP_ITEM_POS_SELL_RULE.md) |  |
| * | [ITEM_KEYWORD->TMP_ITEM_KEYWORD](.ITEM_KEYWORD-_TMP_ITEM_KEYWORD.md) |  |
| * | [ITEM_ADDL_INFO->TMP_ITEM_ADDL_INFO](.ITEM_ADDL_INFO-_TMP_ITEM_ADDL_INFO.md) |  |
| * | [exec DC_UNDO_RENAME_ITM](.exec_DC_UNDO_RENAME_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [3/27/00 (L. Rubakhin) - Created](3_27_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| * | [4/12/00 (L. Rubakhin) - Replaced alert with addl info](4_12_00_L._Rubakhin_-_Replaced_alert_with_addl_info.md) |  |
| dbo | [DC_UNDO_RENAME_PLU](dbo.DC_UNDO_RENAME_PLU.md) |  |
| * | [This procedure restores archived old plu table:](.This_procedure_restores_archived_old_plu_table.md) |  |
| * | [PLU->BAK_PLU](.PLU-_BAK_PLU.md) |  |
| * | [TMP_PLU->PLU](.TMP_PLU-_PLU.md) |  |
| * | [exec DC_UNDO_RENAME_PLU](.exec_DC_UNDO_RENAME_PLU.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [3/29/00 (L. Rubakhin) - Created](3_29_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| dbo | [DC_UNDO_RENAME_POS_ADDL_INFO](dbo.DC_UNDO_RENAME_POS_ADDL_INFO.md) |  |
| * | [This procedure restores archived pos item alert table:](.This_procedure_restores_archived_pos_item_alert_table.md) |  |
| * | [POS_ITEM_ADDL_INFO->BAK_POS_ITEM_ADDL_INFO](.POS_ITEM_ADDL_INFO-_BAK_POS_ITEM_ADDL_INFO.md) |  |
| * | [TMP_POS_ITEM_ADDL_INFO->POS_ITEM_ADDL_INFO](.TMP_POS_ITEM_ADDL_INFO-_POS_ITEM_ADDL_INFO.md) |  |
| * | [exec DC_UNDO_RENAME_POS_ADDL_INFO](.exec_DC_UNDO_RENAME_POS_ADDL_INFO.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [10/29/01 (L. Rubakhin) - Created](10_29_01_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_UNDO_RENAME_POS_ALERT](dbo.DC_UNDO_RENAME_POS_ALERT.md) |  |
| * | [This procedure restores archived pos item alert table:](.This_procedure_restores_archived_pos_item_alert_table.md) |  |
| * | [POS_ITEM_ALERT->BAK_POS_ITEM_ALERT](.POS_ITEM_ALERT-_BAK_POS_ITEM_ALERT.md) |  |
| * | [TMP_POS_ITEM_ALERT->POS_ITEM_ALERT](.TMP_POS_ITEM_ALERT-_POS_ITEM_ALERT.md) |  |
| * | [exec DC_UNDO_RENAME_POS_ALERT](.exec_DC_UNDO_RENAME_POS_ALERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [4/4/00 (L. Rubakhin) - Created](4_4_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| dbo | [DC_UNDO_RENAME_STR_ITM](dbo.DC_UNDO_RENAME_STR_ITM.md) |  |
| * | [This procedure renames:](.This_procedure_renames.md) |  |
| * | [exec DC_UNDO_RENAME_STR_ITM](.exec_DC_UNDO_RENAME_STR_ITM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| dbo | [DC_UNDO_RENAME_UPC](dbo.DC_UNDO_RENAME_UPC.md) |  |
| * | [This procedure restores archived old pos id table:](.This_procedure_restores_archived_old_pos_id_table.md) |  |
| * | [POS_IDENTITY->TMP_POS_IDENTITY](.POS_IDENTITY-_TMP_POS_IDENTITY.md) |  |
| * | [BAK_POS_IDENTITY->POS_IDENTITY](.BAK_POS_IDENTITY-_POS_IDENTITY.md) |  |
| * | [exec DC_UNDO_RENAME_UPC](.exec_DC_UNDO_RENAME_UPC.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [3/28/00 (L. Rubakhin) - Created](3_28_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| dbo | [DC_UNDO_RENAME_UPC_SKU](dbo.DC_UNDO_RENAME_UPC_SKU.md) |  |
| * | [This procedure restores archived old upc to sku mapping  table:](.This_procedure_restores_archived_old_upc_to_sku_mapping_table.md) |  |
| * | [POS_ID_PLU_CODE->BAK_POS_ID_PLU_CODE](.POS_ID_PLU_CODE-_BAK_POS_ID_PLU_CODE.md) |  |
| * | [TMP_POS_ID_PLU_CODE->POS_ID_PLU_CODE](.TMP_POS_ID_PLU_CODE-_POS_ID_PLU_CODE.md) |  |
| * | [exec DC_UNDO_RENAME_UPC_SKU](.exec_DC_UNDO_RENAME_UPC_SKU.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if renaming failed.](1_if_renaming_failed..md) |  |
| * | [4/4/00 (L. Rubakhin) - Created](4_4_00_L._Rubakhin_-_Created.md) |  |
| * | [4/12/00 (L. Rubakhin) - Added transaction wrapper](4_12_00_L._Rubakhin_-_Added_transaction_wrapper.md) |  |
| dbo | [DC_UPD_EQUAL_TAX_ZONE](dbo.DC_UPD_EQUAL_TAX_ZONE.md) | dbo.DC_EQUAL_TAX_ZONE, dbo.EQUAL_TAX_ZONE, dbo.TMP_EQUAL_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE table from the](.TMP_EQUAL_TAX_ZONE_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE table and the](.DC_EQUAL_TAX_ZONE_table_and_the.md) |  |
| * | [EQUAL_TAX_ZONE table.](EQUAL_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_table.md) |  |
| * | [are updates to the EQUAL_TAX_ZONE table.](are_updates_to_the_EQUAL_TAX_ZONE_table..md) |  |
| * | [exec DC_UPD_EQUAL_TAX_ZONE](.exec_DC_UPD_EQUAL_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_EQUAL_TAX_ZONE_LANG](dbo.DC_UPD_EQUAL_TAX_ZONE_LANG.md) | dbo.DC_EQUAL_TAX_ZONE_LANG, dbo.EQUAL_TAX_ZONE, dbo.EQUAL_TAX_ZONE_LANG, dbo.LANGUAGE, dbo.TMP_EQUAL_TAX_ZONE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_EQUAL_TAX_ZONE_LANG table from the](.TMP_EQUAL_TAX_ZONE_LANG_table_from_the.md) |  |
| * | [DC_EQUAL_TAX_ZONE_LANG table and the](.DC_EQUAL_TAX_ZONE_LANG_table_and_the.md) |  |
| * | [EQUAL_TAX_ZONE_LANG table.](EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [The records in the TMP_EQUAL_TAX_ZONE_LANG table](.The_records_in_the_TMP_EQUAL_TAX_ZONE_LANG_table.md) |  |
| * | [are updates to the EQUAL_TAX_ZONE_LANG table.](are_updates_to_the_EQUAL_TAX_ZONE_LANG_table..md) |  |
| * | [exec DC_UPD_EQUAL_TAX_ZONE_LANG](.exec_DC_UPD_EQUAL_TAX_ZONE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_ITEM](dbo.DC_UPD_ITEM.md) | dbo.CATEGORY, dbo.CLASS, dbo.COLOR, dbo.DC_ITEM, dbo.DEPARTMENT, dbo.ITEM, dbo.LIFE_STYLE, dbo.SEASON, dbo.SIZE, dbo.STYLE, dbo.SUB_CATEGORY, dbo.SUB_CLASS, dbo.SUB_DEPARTMENT, dbo.TMP_ITEM |
| * | [This procedure moves items from ITEM table to TMP_ITEM](.This_procedure_moves_items_from_ITEM_table_to_TMP_ITEM.md) |  |
| * | [table and updates data based on info in DC_ITEM table.](table_and_updates_data_based_on_info_in_DC_ITEM_table..md) |  |
| * | [@PRM_DIV](.@PRM_DIV.md) |  |
| * | [exec DC_UPD_ITEM 1](.exec_DC_UPD_ITEM_1.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [UPDATE_CODE:](.UPDATE_CODE.md) |  |
| * | [4/5/00 (L. Rubakhin) - Created](4_5_00_L._Rubakhin_-_Created.md) |  |
| * | [6/30/00 (L. Rubakhin) - Added population of datetime fields](6_30_00_L._Rubakhin_-_Added_population_of_datetime_fields.md) |  |
| * | [8/9/01 (L. Rubakhin) - Added association group](8_9_01_L._Rubakhin_-_Added_association_group.md) |  |
| * | [10/18/01 (L. Rubakhin) - Added tender type id and activate flag](10_18_01_L._Rubakhin_-_Added_tender_type_id_and_activate_flag.md) |  |
| * | [1/27/2003 ( Madhulika Sharma ) - Field Item_type_code is filled correctly now for issue# 87376](.1_27_2003_Madhulika_Sharma_-_Field_Item_type_code_is_filled_correctly_now_for_issue#_87376.md) |  |
| * | [3/24/05 (L. Rubakhin) - Added buy back price, defective item action code,](3_24_05_L._Rubakhin_-_Added_buy_back_price,_defective_item_action_code,.md) |  |
| * | [5/19/05 (L. Rubakhin) - Support for null values in SIZE.SIZE_TYPE_CODE](5_19_05_L_Rubakhin_-_Support_for_null_values_in_SIZE.SIZE_TYPE_CODE.md) |  |
| * | [1/21/08 (Madhulika Sharma) - Field ITEM.MODEL_NUMBER is filled correctly now for issue# 97173](1_21_08_Madhulika_Sharma_-_Field_ITEM.MODEL_NUMBER_is_filled_correctly_now_for_issue#_97173.md) |  |
| dbo | [DC_UPD_ITM_ALERT](dbo.DC_UPD_ITM_ALERT.md) | dbo.DC_ITEM, dbo.ITEM_ALERT, dbo.TMP_ITEM, dbo.TMP_ITEM_ALERT |
| * | [This procedure updates TMP_ITEM_ALERT](.This_procedure_updates_TMP_ITEM_ALERT.md) |  |
| * | [table based on information in DC_ITEM table.](table_based_on_information_in_DC_ITEM_table..md) |  |
| * | [DC_UPD_ITM_ALERT](.DC_UPD_ITM_ALERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [4/6/00 (L. Rubakhin) - Created](4_6_00_L._Rubakhin_-_Created.md) |  |
| dbo | [DC_UPD_ITM_PRC](dbo.DC_UPD_ITM_PRC.md) | dbo.ITEM, dbo.ITEM_QUANTITY, dbo.PRICE_CHANGE, dbo.PRICE_CHANGE_ITEM, dbo.STK_LEDGER_ACCOUNT, dbo.STORE_ITEM, dbo.TMP_PRC_CHANGE |
| * | [This procedure books dataconnect price changes](.This_procedure_books_dataconnect_price_changes.md) |  |
| * | [updates item tables and stock ledger](.updates_item_tables_and_stock_ledger.md) |  |
| * | [@PRM_PRC_CHG_ID - price change id](.@PRM_PRC_CHG_ID_-_price_change_id.md) |  |
| * | [@PRM_STORE_NO - store number](.@PRM_STORE_NO_-_store_number.md) |  |
| * | [@PRM_GLBL_PRC - 1 global price dominates local](.@PRM_GLBL_PRC_-_1_global_price_dominates_local.md) |  |
| * | [exec DC_UPD_ITM_PRC 15, 123](.exec_DC_UPD_ITM_PRC_15,_123.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [Price changes booked and item prices are modified.](Price_changes_booked_and_item_prices_are_modified..md) |  |
| * | [Stock ledger is updated.](Stock_ledger_is_updated..md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if price booking failed.](1_if_price_booking_failed..md) |  |
| * | [11/7/01 (L. Rubakhin) - Created](11_7_01_L._Rubakhin_-_Created.md) |  |
| * | [1/2/03 (O. Blevins)](1_2_03_O._Blevins.md) |  |
| * | [07/15/04 (L. Rubakhin) - Added support for local prices](07_15_04_L._Rubakhin_-_Added_support_for_local_prices.md) |  |
| declare | [@local_flg smallint](declare.@local_flg_smallint.md) |  |
| dbo | [DC_UPD_ITM_QTY](dbo.DC_UPD_ITM_QTY.md) | dbo.DC_STOCK_ITEM, dbo.ITEM, dbo.ITEM_QUANTITY, dbo.STK_ADJ_ITEM, dbo.STK_LEDGER_ACCOUNT, dbo.STOCK_ADJUSTMENT, dbo.STORE_ITEM |
| * | [This procedure updates item quantities and books](.This_procedure_updates_item_quantities_and_books.md) |  |
| * | [it in STOCK_ADJUSTMENT table. Then ledger is updated](it_in_STOCK_ADJUSTMENT_table._Then_ledger_is_updated.md) |  |
| * | [accordingly.](accordingly..md) |  |
| * | [@PRM_STK_ADJ_ID - stock adjustment ID](.@PRM_STK_ADJ_ID_-_stock_adjustment_ID.md) |  |
| * | [@PRM_STK_ADJ_NO - stock adjustment number](.@PRM_STK_ADJ_NO_-_stock_adjustment_number.md) |  |
| * | [@PRM_COST_METHOD - method used for cost calculation,](.@PRM_COST_METHOD_-_method_used_for_cost_calculation,.md) |  |
| * | [@PRM_BOOK_ADJ - book change of qty in stock adjustment table](.@PRM_BOOK_ADJ_-_book_change_of_qty_in_stock_adjustment_table.md) |  |
| * | [exec DC_UPD_ITM_QTY](.exec_DC_UPD_ITM_QTY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [This procedure returns 0 on success and](.This_procedure_returns_0_on_success_and.md) |  |
| * | [1 if price booking failed.](1_if_price_booking_failed..md) |  |
| * | [Stock ledger account records are updated separately.](Stock_ledger_account_records_are_updated_separately..md) |  |
| * | [4/24/00 (L. Rubakhin) - Created](4_24_00_L._Rubakhin_-_Created.md) |  |
| * | [5/15/00 (L. Rubakhin) - Added @PRM_BOOK_ADJ](5_15_00_L._Rubakhin_-_Added_@PRM_BOOK_ADJ.md) |  |
| * | [5/30/00 (O. Blevins) - Added StoreNum to join between](5_30_00_O._Blevins_-_Added_StoreNum_to_join_between.md) |  |
| * | [DC_STOCK_ITEM and ITEM_QUANTITY](.DC_STOCK_ITEM_and_ITEM_QUANTITY.md) |  |
| * | [7/12/07 (L. Rubakhin) - added @PRM_LEDGER_MAINT_LEVEL and @PRM_REF_STORE_NO](7_12_07_L._Rubakhin_-_added_@PRM_LEDGER_MAINT_LEVEL_and_@PRM_REF_STORE_NO.md) |  |
| dbo | [DC_UPD_PLU_PRICE](dbo.DC_UPD_PLU_PRICE.md) | dbo.ITEM, dbo.PLU_PRICE, dbo.STORE_ITEM |
| * | [This procedure updates PLU_PRICE table from item tables.](This_procedure_updates_PLU_PRICE_table_from_item_tables..md) |  |
| * | [@PRM_PKTYPE - type of PK for PLU table](.@PRM_PKTYPE_-_type_of_PK_for_PLU_table.md) |  |
| * | [@PRM_STORE_NO - global store number to not include in update of PLU_PRICE table](.@PRM_STORE_NO_-_global_store_number_to_not_include_in_update_of_PLU_PRICE_table.md) |  |
| * | [@ACTIVE_ITEMS_ONLY - flag that shows that only active ITEMs are](.@ACTIVE_ITEMS_ONLY_-_flag_that_shows_that_only_active_ITEMs_are.md) |  |
| * | [exec DC_UPD_PLU_PRICE 'SKU' 1234](.exec_DC_UPD_PLU_PRICE_'SKU'_1234.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [3/20/09 (T. Koenig) - Created](3_20_09_T._Koenig_-_Created.md) |  |
| * | [9/29/10 (T. Koenig) - Updated](9_29_10_T._Koenig_-_Updated.md) |  |
| * | [10/14/10 (T. Koenig) - Updated](10_14_10_T._Koenig_-_Updated.md) |  |
| dbo | [DC_UPD_POS_RULE](dbo.DC_UPD_POS_RULE.md) | dbo.DC_ITEM, dbo.ITEM_POS_SELL_RULE, dbo.SPIFF_DEFINITION, dbo.TMP_ITEM, dbo.TMP_ITEM_POS_SELL_RULE |
| * | [This procedure creates records in TMP_ITEM_POS_SELL_RULE](.This_procedure_creates_records_in_TMP_ITEM_POS_SELL_RULE.md) |  |
| * | [table based on information in DC_ITEM and TMP_ITEM tables.](table_based_on_information_in_DC_ITEM_and_TMP_ITEM_tables..md) |  |
| * | [@PRM_STORE_NO - Store Number](.@PRM_STORE_NO_-_Store_Number.md) |  |
| * | [DC_UPD_POS_RULE 123, 0](.DC_UPD_POS_RULE_123,_0.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [4/6/00 (L. Rubakhin) - Created](4_6_00_L._Rubakhin_-_Created.md) |  |
| * | [10/19/00 (L. Rubakhin) - Created](10_19_00_L._Rubakhin_-_Created.md) |  |
| * | [10/19/01 (L. Rubakhin) - Added price auth amount](10_19_01_L._Rubakhin_-_Added_price_auth_amount.md) |  |
| * | [10/21/14 (L. Rubakhin) - Added INVOICEABLE_FLG](10_21_14_L._Rubakhin_-_Added_INVOICEABLE_FLG.md) |  |
| * | [2/29/15 (O. Blevins) - Restored LOYALTY_DSCNT_FLG](2_29_15_O._Blevins_-_Restored_LOYALTY_DSCNT_FLG.md) |  |
| dbo | [DC_UPD_STK_LDG](dbo.DC_UPD_STK_LDG.md) | dbo.STK_LEDGER_ACCOUNT, dbo.TMP_PRC_CHANGE |
| * | [This procedure updates STK_LEDGER_ACCOUNT table](.This_procedure_updates_STK_LEDGER_ACCOUNT_table.md) |  |
| * | [based on the information in TMP_PRC_CHANGE.](based_on_the_information_in_TMP_PRC_CHANGE..md) |  |
| * | [DC_UPD_STK_LDG 123](.DC_UPD_STK_LDG_123.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [4/7/00 (L. Rubakhin) - Created](4_7_00_L._Rubakhin_-_Created.md) |  |
| * | [12/14/01 (L. Rubakhin) - Added store number parameter](12_14_01_L._Rubakhin_-_Added_store_number_parameter.md) |  |
| dbo | [DC_UPD_STR_ITEM](dbo.DC_UPD_STR_ITEM.md) | dbo.AGE_RESTRICT_GRP, dbo.DC_STORE_ITEM, dbo.ITEM, dbo.SPCL_RESTRICT_GRP, dbo.STORE_ITEM, dbo.TMP_STORE_ITEM |
| * | [This procedure  updates the old store items](.This_procedure_updates_the_old_store_items.md) |  |
| * | [exec DC_UPD_STR_ITEM](.exec_DC_UPD_STR_ITEM.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [12/12/01 (Radhika Jayanti) Modified age and special restriction join](.12_12_01_Radhika_Jayanti_Modified_age_and_special_restriction_join.md) |  |
| * | [02/21/02  (Radhika Jayanti)Added GlobalPermanentPriceDominance prm](.02_21_02_Radhika_Jayanti_Added_GlobalPermanentPriceDominance_prm.md) |  |
| * | [04/20/11 (Leonid Rubakhin) Added TaxGroupId to store item dataconnect.](04_20_11_Leonid_Rubakhin_Added_TaxGroupId_to_store_item_dataconnect..md) |  |
| dbo | [DC_UPD_STR_ITM](dbo.DC_UPD_STR_ITM.md) | dbo.AGE_RESTRICT_GRP, dbo.DC_ITEM, dbo.SPCL_RESTRICT_GRP, dbo.STORE_ITEM, dbo.TMP_ITEM, dbo.TMP_STORE_ITEM |
| * | [This procedure creates records in TMP_STORE_ITEM](.This_procedure_creates_records_in_TMP_STORE_ITEM.md) |  |
| * | [table based on information in DC_ITEM and TMP_ITEM tables.](table_based_on_information_in_DC_ITEM_and_TMP_ITEM_tables..md) |  |
| * | [@PRM_STORE_NO - Store Number](.@PRM_STORE_NO_-_Store_Number.md) |  |
| * | [@PRM_GLBL_PRC:](.@PRM_GLBL_PRC.md) |  |
| * | [DC_UPD_STR_ITM 123, 0](.DC_UPD_STR_ITM_123,_0.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [4/6/00 (L. Rubakhin) - Created](4_6_00_L._Rubakhin_-_Created.md) |  |
| * | [4/21/00 (L. Rubakhin) - Added support for item status](4_21_00_L._Rubakhin_-_Added_support_for_item_status.md) |  |
| * | [11/15/01 (L. Rubakhin) - Added store number filter](11_15_01_L._Rubakhin_-_Added_store_number_filter.md) |  |
| * | [6/2/05 (L. Rubakhin) - Corrected setting of local prices](6_2_05_L._Rubakhin_-_Corrected_setting_of_local_prices.md) |  |
| dbo | [DC_UPD_TAX_AUTHORITY](dbo.DC_UPD_TAX_AUTHORITY.md) | dbo.DC_TAX_AUTHORITY, dbo.TAX_AUTHORITY, dbo.TMP_TAX_AUTHORITY |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY table from the](.TMP_TAX_AUTHORITY_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY table and the](.DC_TAX_AUTHORITY_table_and_the.md) |  |
| * | [TAX_AUTHORITY table.](TAX_AUTHORITY_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY table](.The_records_in_the_TMP_TAX_AUTHORITY_table.md) |  |
| * | [are updates to the TAX_AUTHORITY table.](are_updates_to_the_TAX_AUTHORITY_table..md) |  |
| * | [exec DC_UPD_TAX_AUTHORITY](.exec_DC_UPD_TAX_AUTHORITY.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_TAX_AUTHORITY_LANG](dbo.DC_UPD_TAX_AUTHORITY_LANG.md) | dbo.DC_TAX_AUTHORITY_LANG, dbo.LANGUAGE, dbo.TAX_AUTHORITY, dbo.TAX_AUTHORITY_LANG, dbo.TMP_TAX_AUTHORITY_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_AUTHORITY_LANG table from the](.TMP_TAX_AUTHORITY_LANG_table_from_the.md) |  |
| * | [DC_TAX_AUTHORITY_LANG table and the](.DC_TAX_AUTHORITY_LANG_table_and_the.md) |  |
| * | [TAX_AUTHORITY_LANG table.](TAX_AUTHORITY_LANG_table..md) |  |
| * | [The records in the TMP_TAX_AUTHORITY_LANG table](.The_records_in_the_TMP_TAX_AUTHORITY_LANG_table.md) |  |
| * | [are updates to the TAX_AUTHORITY_LANG table.](are_updates_to_the_TAX_AUTHORITY_LANG_table..md) |  |
| * | [exec DC_UPD_TAX_AUTHORITY_LANG](.exec_DC_UPD_TAX_AUTHORITY_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_TAX_EXEMPT_CERT](dbo.DC_UPD_TAX_EXEMPT_CERT.md) | dbo.CUSTOMER, dbo.DC_TAX_EXEMPT_CERT, dbo.TAX_EXEMPT_CERT, dbo.TMP_TAX_EXEMPT_CERT |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_EXEMPT_CERT table from the](.TMP_TAX_EXEMPT_CERT_table_from_the.md) |  |
| * | [DC_TAX_EXEMPT_CERT table and the](.DC_TAX_EXEMPT_CERT_table_and_the.md) |  |
| * | [TAX_EXEMPT_CERT table.](TAX_EXEMPT_CERT_table..md) |  |
| * | [The records in the TMP_TAX_EXEMPT_CERT table](.The_records_in_the_TMP_TAX_EXEMPT_CERT_table.md) |  |
| * | [are updates to the TAX_EXEMPT_CERT table.](are_updates_to_the_TAX_EXEMPT_CERT_table..md) |  |
| * | [exec DC_UPD_TAX_EXEMPT_CERT](.exec_DC_UPD_TAX_EXEMPT_CERT.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_TAX_GRP_ZONE_AUTH](dbo.DC_UPD_TAX_GRP_ZONE_AUTH.md) | dbo.DC_TAX_GRP_ZONE_AUTH, dbo.EQUAL_TAX_ZONE, dbo.TAX_AUTHORITY, dbo.TAX_EXEMPT_CERT, dbo.TAX_GRP_ZONE_AUTH, dbo.TAX_RULE, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAX_GRP_ZONE_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_GRP_ZONE_AUTH table from the](.TMP_TAX_GRP_ZONE_AUTH_table_from_the.md) |  |
| * | [DC_TAX_GRP_ZONE_AUTH table and the](.DC_TAX_GRP_ZONE_AUTH_table_and_the.md) |  |
| * | [TAX_GRP_ZONE_AUTH table.](TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_GRP_ZONE_AUTH table](.The_records_in_the_TMP_TAX_GRP_ZONE_AUTH_table.md) |  |
| * | [are updates to the TAX_GRP_ZONE_AUTH table.](are_updates_to_the_TAX_GRP_ZONE_AUTH_table..md) |  |
| * | [exec DC_UPD_TAX_GRP_ZONE_AUTH](.exec_DC_UPD_TAX_GRP_ZONE_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| * | [4/4/13 (O. Blevins) - Fixed referential integrity for tax exemptions](4_4_13_O._Blevins_-_Fixed_referential_integrity_for_tax_exemptions.md) |  |
| dbo | [DC_UPD_TAX_RULE](dbo.DC_UPD_TAX_RULE.md) | dbo.DC_TAX_RULE, dbo.TAX_RULE, dbo.TMP_TAX_RULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE table from the](.TMP_TAX_RULE_table_from_the.md) |  |
| * | [DC_TAX_RULE table and the](.DC_TAX_RULE_table_and_the.md) |  |
| * | [TAX_RULE table.](TAX_RULE_table..md) |  |
| * | [The records in the TMP_TAX_RULE table](.The_records_in_the_TMP_TAX_RULE_table.md) |  |
| * | [are updates to the TAX_RULE table.](are_updates_to_the_TAX_RULE_table..md) |  |
| * | [exec DC_UPD_TAX_RULE](.exec_DC_UPD_TAX_RULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_TAX_RULE_LANG](dbo.DC_UPD_TAX_RULE_LANG.md) | dbo.DC_TAX_RULE_LANG, dbo.LANGUAGE, dbo.TAX_RULE, dbo.TAX_RULE_LANG, dbo.TMP_TAX_RULE_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_RULE_LANG table from the](.TMP_TAX_RULE_LANG_table_from_the.md) |  |
| * | [DC_TAX_RULE_LANG table and the](.DC_TAX_RULE_LANG_table_and_the.md) |  |
| * | [TAX_RULE_LANG table.](TAX_RULE_LANG_table..md) |  |
| * | [The records in the TMP_TAX_RULE_LANG table](.The_records_in_the_TMP_TAX_RULE_LANG_table.md) |  |
| * | [are updates to the TAX_RULE_LANG table.](are_updates_to_the_TAX_RULE_LANG_table..md) |  |
| * | [exec DC_UPD_TAX_RULE_LANG](.exec_DC_UPD_TAX_RULE_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_TAX_SCHEDULE](dbo.DC_UPD_TAX_SCHEDULE.md) | dbo.DC_TAX_SCHEDULE, dbo.TAX_RULE, dbo.TAX_SCHEDULE, dbo.TMP_TAX_SCHEDULE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_SCHEDULE table from the](.TMP_TAX_SCHEDULE_table_from_the.md) |  |
| * | [DC_TAX_SCHEDULE table and the](.DC_TAX_SCHEDULE_table_and_the.md) |  |
| * | [TAX_SCHEDULE table.](TAX_SCHEDULE_table..md) |  |
| * | [The records in the TMP_TAX_SCHEDULE table](.The_records_in_the_TMP_TAX_SCHEDULE_table.md) |  |
| * | [are updates to the TAX_SCHEDULE table.](are_updates_to_the_TAX_SCHEDULE_table..md) |  |
| * | [exec DC_UPD_TAX_SCHEDULE](.exec_DC_UPD_TAX_SCHEDULE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_TAX_ZONE_TAX_AUTH](dbo.DC_UPD_TAX_ZONE_TAX_AUTH.md) | dbo.DC_TAX_ZONE_TAX_AUTH, dbo.EQUAL_TAX_ZONE, dbo.TAX_AUTHORITY, dbo.TAX_ZONE_TAX_AUTH, dbo.TMP_TAX_ZONE_TAX_AUTH |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAX_ZONE_TAX_AUTH table from the](.TMP_TAX_ZONE_TAX_AUTH_table_from_the.md) |  |
| * | [DC_TAX_ZONE_TAX_AUTH table and the](.DC_TAX_ZONE_TAX_AUTH_table_and_the.md) |  |
| * | [TAX_ZONE_TAX_AUTH table.](TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [The records in the TMP_TAX_ZONE_TAX_AUTH table](.The_records_in_the_TMP_TAX_ZONE_TAX_AUTH_table.md) |  |
| * | [are updates to the TAX_ZONE_TAX_AUTH table.](are_updates_to_the_TAX_ZONE_TAX_AUTH_table..md) |  |
| * | [exec DC_UPD_TAX_ZONE_TAX_AUTH](.exec_DC_UPD_TAX_ZONE_TAX_AUTH.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_TAXABLE_ITEM_GRP](dbo.DC_UPD_TAXABLE_ITEM_GRP.md) | dbo.DC_TAXABLE_ITEM_GRP, dbo.TAXABLE_ITEM_GRP, dbo.TMP_TAXABLE_ITEM_GRP |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP table from the](.TMP_TAXABLE_ITEM_GRP_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP table and the](.DC_TAXABLE_ITEM_GRP_table_and_the.md) |  |
| * | [TAXABLE_ITEM_GRP table.](TAXABLE_ITEM_GRP_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_table.md) |  |
| * | [are updates to the TAXABLE_ITEM_GRP table.](are_updates_to_the_TAXABLE_ITEM_GRP_table..md) |  |
| * | [exec DC_UPD_TAXABLE_ITEM_GRP](.exec_DC_UPD_TAXABLE_ITEM_GRP.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_TAXABLE_ITEM_GRP_LANG](dbo.DC_UPD_TAXABLE_ITEM_GRP_LANG.md) | dbo.DC_TAXABLE_ITEM_GRP_LANG, dbo.LANGUAGE, dbo.TAXABLE_ITEM_GRP, dbo.TAXABLE_ITEM_GRP_LANG, dbo.TMP_TAXABLE_ITEM_GRP_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_TAXABLE_ITEM_GRP_LANG table from the](.TMP_TAXABLE_ITEM_GRP_LANG_table_from_the.md) |  |
| * | [DC_TAXABLE_ITEM_GRP_LANG table and the](.DC_TAXABLE_ITEM_GRP_LANG_table_and_the.md) |  |
| * | [TAXABLE_ITEM_GRP_LANG table.](TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [The records in the TMP_TAXABLE_ITEM_GRP_LANG table](.The_records_in_the_TMP_TAXABLE_ITEM_GRP_LANG_table.md) |  |
| * | [are updates to the TAXABLE_ITEM_GRP_LANG table.](are_updates_to_the_TAXABLE_ITEM_GRP_LANG_table..md) |  |
| * | [exec DC_UPD_TAXABLE_ITEM_GRP_LANG](.exec_DC_UPD_TAXABLE_ITEM_GRP_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_VALUE_ADDED_TAX](dbo.DC_UPD_VALUE_ADDED_TAX.md) | dbo.DC_VALUE_ADDED_TAX, dbo.TMP_VALUE_ADDED_TAX, dbo.VALUE_ADDED_TAX |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX table from the](.TMP_VALUE_ADDED_TAX_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX table and the](.DC_VALUE_ADDED_TAX_table_and_the.md) |  |
| * | [VALUE_ADDED_TAX table.](VALUE_ADDED_TAX_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX table](.The_records_in_the_TMP_VALUE_ADDED_TAX_table.md) |  |
| * | [are updates to the VALUE_ADDED_TAX table.](are_updates_to_the_VALUE_ADDED_TAX_table..md) |  |
| * | [exec DC_UPD_VALUE_ADDED_TAX](.exec_DC_UPD_VALUE_ADDED_TAX.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_VALUE_ADDED_TAX_LANG](dbo.DC_UPD_VALUE_ADDED_TAX_LANG.md) | dbo.DC_VALUE_ADDED_TAX_LANG, dbo.LANGUAGE, dbo.TMP_VALUE_ADDED_TAX_LANG, dbo.VALUE_ADDED_TAX, dbo.VALUE_ADDED_TAX_LANG |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_VALUE_ADDED_TAX_LANG table from the](.TMP_VALUE_ADDED_TAX_LANG_table_from_the.md) |  |
| * | [DC_VALUE_ADDED_TAX_LANG table and the](.DC_VALUE_ADDED_TAX_LANG_table_and_the.md) |  |
| * | [VALUE_ADDED_TAX_LANG table.](VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [The records in the TMP_VALUE_ADDED_TAX_LANG table](.The_records_in_the_TMP_VALUE_ADDED_TAX_LANG_table.md) |  |
| * | [are updates to the VALUE_ADDED_TAX_LANG table.](are_updates_to_the_VALUE_ADDED_TAX_LANG_table..md) |  |
| * | [exec DC_UPD_VALUE_ADDED_TAX_LANG](.exec_DC_UPD_VALUE_ADDED_TAX_LANG.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_UPD_ZIP_CODE_TAX_ZONE](dbo.DC_UPD_ZIP_CODE_TAX_ZONE.md) | dbo.DC_CHK_ZIP_CODE_TAX_ZONE_OVRLP, dbo.DC_ZIP_CODE_TAX_ZONE, dbo.EQUAL_TAX_ZONE, dbo.TMP_ZIP_CODE_TAX_ZONE, dbo.ZIP_CODE_TAX_ZONE |
| * | [This procedure builds the](.This_procedure_builds_the.md) |  |
| * | [TMP_ZIP_CODE_TAX_ZONE table from the](.TMP_ZIP_CODE_TAX_ZONE_table_from_the.md) |  |
| * | [DC_ZIP_CODE_TAX_ZONE table and the](.DC_ZIP_CODE_TAX_ZONE_table_and_the.md) |  |
| * | [ZIP_CODE_TAX_ZONE table.](ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [The records in the TMP_ZIP_CODE_TAX_ZONE table](.The_records_in_the_TMP_ZIP_CODE_TAX_ZONE_table.md) |  |
| * | [are updates to the ZIP_CODE_TAX_ZONE table.](are_updates_to_the_ZIP_CODE_TAX_ZONE_table..md) |  |
| * | [exec DC_UPD_ZIP_CODE_TAX_ZONE](.exec_DC_UPD_ZIP_CODE_TAX_ZONE.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_VALUE_ADDED_TAX_ERR](dbo.DC_VALUE_ADDED_TAX_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_VALUE_ADDED_TAX_ERR](.exec_DC_VALUE_ADDED_TAX_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_VALUE_ADDED_TAX_LANG_ERR](dbo.DC_VALUE_ADDED_TAX_LANG_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_VALUE_ADDED_TAX_LANG_ERR](.exec_DC_VALUE_ADDED_TAX_LANG_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DC_ZIP_CODE_TAX_ZONE_ERR](dbo.DC_ZIP_CODE_TAX_ZONE_ERR.md) |  |
| * | [This procedure cleans up in the case of error.](This_procedure_cleans_up_in_the_case_of_error..md) |  |
| * | [exec DC_ZIP_CODE_TAX_ZONE_ERR](.exec_DC_ZIP_CODE_TAX_ZONE_ERR.md) |  |
| * | [DataConnect](.DataConnect.md) |  |
| * | [7/25/12 (O. Blevins) - Created](7_25_12_O._Blevins_-_Created.md) |  |
| dbo | [DYN_ACTIVATE_DATA_CONTEXT](dbo.DYN_ACTIVATE_DATA_CONTEXT.md) | dbo.DYN_CREATE_DATA_CONTEXT, dbo.DYN_GEN_CONTEXT_HNDL |
| dbo | [DYN_CREATE_CALENDAR_SNAPSHOT](dbo.DYN_CREATE_CALENDAR_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_CALENDAR_SNAPSHOT |
| dbo | [DYN_CREATE_DATA_CONTEXT](dbo.DYN_CREATE_DATA_CONTEXT.md) | dbo.DM_DATA_CONTEXT |
| dbo | [DYN_CREATE_EMPLOYEE_SNAPSHOT](dbo.DYN_CREATE_EMPLOYEE_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_EMPLOYEE_SNAPSHOT |
| dbo | [DYN_CREATE_MISC_SNAPSHOT](dbo.DYN_CREATE_MISC_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_MISC_SNAPSHOT |
| dbo | [DYN_CREATE_ORDER_SNAPSHOT](dbo.DYN_CREATE_ORDER_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_ORDER_SNAPSHOT |
| dbo | [DYN_CREATE_PLU_SNAPSHOT](dbo.DYN_CREATE_PLU_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_PLU_SNAPSHOT |
| dbo | [DYN_CREATE_REWARDS_SNAPSHOT](dbo.DYN_CREATE_REWARDS_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_REWARDS_SNAPSHOT |
| dbo | [DYN_CREATE_SHIPPING_SNAPSHOT](dbo.DYN_CREATE_SHIPPING_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_SHIPPING_SNAPSHOT |
| dbo | [DYN_CREATE_STORE_SNAPSHOT](dbo.DYN_CREATE_STORE_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_STORE_SNAPSHOT |
| dbo | [DYN_CREATE_TAXES_SNAPSHOT](dbo.DYN_CREATE_TAXES_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_TAXES_SNAPSHOT |
| dbo | [DYN_CREATE_TENDERS_SNAPSHOT](dbo.DYN_CREATE_TENDERS_SNAPSHOT.md) | dbo.DYN_GEN_INSTANCE_NO, dbo.DYN_POPULATE_TENDERS_SNAPSHOT |
| dbo | [DYN_GEN_CONTEXT_HNDL](dbo.DYN_GEN_CONTEXT_HNDL.md) | dbo.DM_DATA_CONTEXT |
| dbo | [DYN_GEN_INSTANCE_NO](dbo.DYN_GEN_INSTANCE_NO.md) |  |
| dbo | [DYN_POPULATE_CALENDAR_SNAPSHOT](dbo.DYN_POPULATE_CALENDAR_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_EMPLOYEE_SNAPSHOT](dbo.DYN_POPULATE_EMPLOYEE_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_MISC_SNAPSHOT](dbo.DYN_POPULATE_MISC_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_ORDER_SNAPSHOT](dbo.DYN_POPULATE_ORDER_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_PLU_SNAPSHOT](dbo.DYN_POPULATE_PLU_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_REWARDS_SNAPSHOT](dbo.DYN_POPULATE_REWARDS_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_SHIPPING_SNAPSHOT](dbo.DYN_POPULATE_SHIPPING_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_STORE_SNAPSHOT](dbo.DYN_POPULATE_STORE_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_TAXES_SNAPSHOT](dbo.DYN_POPULATE_TAXES_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [DYN_POPULATE_TENDERS_SNAPSHOT](dbo.DYN_POPULATE_TENDERS_SNAPSHOT.md) | dbo.DM_CONFIG, dbo.DM_DATABASE_BLANK, dbo.DM_DATABASE_INSTANCE, dbo.DYN_CREATE_BLANK_DATABASES_SYNC |
| dbo | [GenDbConstants](dbo.GenDbConstants.md) | dbo.VERSION |
| print ' | [/// <summary>'](print_'._summary_'.md) |  |
| print ' | [/// This class contains table and field names for USICOAL database'](print_'._This_class_contains_table_and_field_names_for_USICOAL_database'.md) |  |
| print ' | [/// </summary>'](print_'._summary_'.md) |  |
| 'print '' | [#region '' + object_name(object_id(''?''));]('print_''.#region_''_+_object_name_object_id_''_''_;.md) |  |
| print '' | [#endregion'';](print_''.#endregion'';.md) |  |
| dbo | [IM_APPL_PRC_CHG](dbo.IM_APPL_PRC_CHG.md) | dbo.ITEM, dbo.ITEM_QUANTITY, dbo.PLU, dbo.PRICE_CHANGE, dbo.PRICE_CHANGE_ITEM, dbo.STORE_ITEM |
| * | [This procedure applies scheduled price changes](.This_procedure_applies_scheduled_price_changes.md) |  |
| * | [@PRM_PRICE_CHANGE_ID - price change id](.@PRM_PRICE_CHANGE_ID_-_price_change_id.md) |  |
| * | [@PRM_STORE_NO - store number](.@PRM_STORE_NO_-_store_number.md) |  |
| * | [@CUR_DT -- current datetime](.@CUR_DT_--_current_datetime.md) |  |
| * | [exec DC_PRC_CHANGE 12345, 123, '12-Jan-2005 19:07:23'](.exec_DC_PRC_CHANGE_12345,_123,_'12-Jan-2005_19_07_23'.md) |  |
| * | [@EXPIRATION_DT - price change expiration datetime](.@EXPIRATION_DT_-_price_change_expiration_datetime.md) |  |
| * | [@TMP_FLG](.@TMP_FLG.md) |  |
| * | [@LOCAL_FLG](.@LOCAL_FLG.md) |  |
| * | [@BEGIN_END_FLG](.@BEGIN_END_FLG.md) |  |
| * | [@PLU_MODIFIED - plu modified flag](.@PLU_MODIFIED_-_plu_modified_flag.md) |  |
| * | [Item Master Service](.Item_Master_Service.md) |  |
| * | [This procedure modifies prices in ITEM/STORE_ITEM, PLU,](.This_procedure_modifies_prices_in_ITEM_STORE_ITEM,_PLU,.md) |  |
| * | [PRICE_CHANGE and PRICE_CHANGE_ITEM](.PRICE_CHANGE_and_PRICE_CHANGE_ITEM.md) |  |
| * | [When temp price is activated on top of temp price](.When_temp_price_is_activated_on_top_of_temp_price.md) |  |
| * | [the corresponding rollback records in PRICE_CHANGE_ITEM](.the_corresponding_rollback_records_in_PRICE_CHANGE_ITEM.md) |  |
| * | [table should be set to canceled status. This procedure](table_should_be_set_to_canceled_status._This_procedure.md) |  |
| * | [does not do it.](does_not_do_it..md) |  |
| * | [This procedure returns 0 if successfule and 1 if failed.](This_procedure_returns_0_if_successfule_and_1_if_failed..md) |  |
| declare | [@EXPIRATION_DT datetime](declare.@EXPIRATION_DT_datetime.md) |  |
| declare | [@TMP_FLG int -- 1 - TEMP, 2 - PERM](declare.@TMP_FLG_int_--_1_-_TEMP,_2_-_PERM.md) |  |
| declare | [@LOCAL_FLG int -- 1 - LOCAL, 2 - GLOBAL](declare.@LOCAL_FLG_int_--_1_-_LOCAL,_2_-_GLOBAL.md) |  |
| declare | [@BEGIN_END_FLG int -- 1 - BEGIN, 2 - END](declare.@BEGIN_END_FLG_int_--_1_-_BEGIN,_2_-_END.md) |  |
| dbo | [NOR_SEL_EMPLOYEES](dbo.NOR_SEL_EMPLOYEES.md) | dbo.EMPLOYEE, dbo.EMPLOYEE_JOB_TYPE, dbo.JOB_TYPE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RETAIL_TRN_DOCUMENT, dbo.SALE_RTRN_LN_ITEM, dbo.SPIFF, dbo.STORE_EVENT |
| dbo | [NOR_SEL_RETAIL_TRN_DOCUMENT](dbo.NOR_SEL_RETAIL_TRN_DOCUMENT.md) | dbo.RETAIL_TRN_DOCUMENT |
| dbo | [NSB_SP_CUST_HIST1_TNDR](dbo.NSB_SP_CUST_HIST1_TNDR.md) | dbo.RETAIL_TRANSACTION, dbo.TENDER, dbo.TENDER_LINE_ITEM |
| dbo | [NSB_SP_CUST_HIST1_TRN](dbo.NSB_SP_CUST_HIST1_TRN.md) | dbo.CUSTOMER, dbo.CUSTOMER_PERSON, dbo.DEPARTMENT, dbo.ITEM, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_EMPL_FILE](dbo.NSB_SP_EMPL_FILE.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.OPR_RSRC_ACCESS, dbo.RPT_SELECT_OBJECT |
| dbo | [NSB_SP_EMPL_PROD1](dbo.NSB_SP_EMPL_PROD1.md) | dbo.EMPLOYEE, dbo.ITEM_DISCOUNT, dbo.OPERATOR, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_EMPL_PROD2](dbo.NSB_SP_EMPL_PROD2.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_EMPL_PROD3](dbo.NSB_SP_EMPL_PROD3.md) | dbo.EMPLOYEE, dbo.ITEM_DISCOUNT, dbo.OPERATOR, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_FLASH_SALES1](dbo.NSB_SP_FLASH_SALES1.md) | dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_FLASH_SALES2](dbo.NSB_SP_FLASH_SALES2.md) | dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_KPI1](dbo.NSB_SP_KPI1.md) | dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_LP_MAN_KEY_CARD1](dbo.NSB_SP_LP_MAN_KEY_CARD1.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.TENDER, dbo.TENDER_LINE_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_LP_NON_SALE1](dbo.NSB_SP_LP_NON_SALE1.md) | dbo.EMPLOYEE, dbo.NO_SALE_RSN_CODE, dbo.NO_SALE_TRN, dbo.OPERATOR, dbo.PAIDIO_TRANSACTION, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.TENDER_CONTROL_TRN, dbo.TNDR_CTRL_TRN_TNDR |
| dbo | [NSB_SP_LP_SUSP_TRN2](dbo.NSB_SP_LP_SUSP_TRN2.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SUSP_TRN_RSN_CODE, dbo.SUSPENDED_TRN, dbo.WORKSTATION |
| dbo | [NSB_SP_LP_VOID_ITEMS](dbo.NSB_SP_LP_VOID_ITEMS.md) | dbo.DEPARTMENT, dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_LP_VOID_TENDER](dbo.NSB_SP_LP_VOID_TENDER.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.TENDER, dbo.TENDER_LINE_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_LP_VOID_TRN2](dbo.NSB_SP_LP_VOID_TRN2.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.VOID_TRANSACTION, dbo.WORKSTATION |
| dbo | [NSB_SP_MAN_KEY_CARD1](dbo.NSB_SP_MAN_KEY_CARD1.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.TENDER, dbo.TENDER_LINE_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_MRCH_DEPT1](dbo.NSB_SP_MRCH_DEPT1.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM, dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_MRCH_DEPT2](dbo.NSB_SP_MRCH_DEPT2.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_MRCH_DEPT3](dbo.NSB_SP_MRCH_DEPT3.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM, dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_MRCH_DEPT4](dbo.NSB_SP_MRCH_DEPT4.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_MRCH_DEPT5](dbo.NSB_SP_MRCH_DEPT5.md) | dbo.CLASS, dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_MRCH_DEPT6](dbo.NSB_SP_MRCH_DEPT6.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM, dbo.STYLE |
| dbo | [NSB_SP_MRCH_DEPT7](dbo.NSB_SP_MRCH_DEPT7.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM_DISCOUNT, dbo.PLU, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_MRCH_DEPT8](dbo.NSB_SP_MRCH_DEPT8.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM_DISCOUNT, dbo.PLU, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_NON_MRCH1](dbo.NSB_SP_NON_MRCH1.md) | dbo.ITEM, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_NON_MRCH2](dbo.NSB_SP_NON_MRCH2.md) | dbo.EMPLOYEE, dbo.ITEM, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.SPIFF, dbo.WORKSTATION |
| dbo | [NSB_SP_NON_SALE1](dbo.NSB_SP_NON_SALE1.md) | dbo.EMPLOYEE, dbo.NO_SALE_TRN, dbo.OPERATOR, dbo.PAIDIO_TRANSACTION, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.TENDER_CONTROL_TRN, dbo.TNDR_CTRL_TRN_TNDR |
| dbo | [NSB_SP_NOT_ON_FILE](dbo.NSB_SP_NOT_ON_FILE.md) | dbo.DEPARTMENT, dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [NSB_SP_ORDER_DETAIL_CHARGES](dbo.NSB_SP_ORDER_DETAIL_CHARGES.md) | dbo.CUST_ORD_CHARGE |
| dbo | [NSB_SP_ORDER_DETAIL_ITEMS](dbo.NSB_SP_ORDER_DETAIL_ITEMS.md) | dbo.ACCOUNT, dbo.CUST_ORD_DISCOUNT, dbo.CUST_ORDER_ITEM, dbo.CUST_ORDER_TYPE, dbo.CUSTOMER, dbo.CUSTOMER_ADDRESS, dbo.CUSTOMER_ORDER, dbo.CUSTOMER_PERSON |
| dbo | [NSB_SP_ORDER_DETAIL_ITEMS2](dbo.NSB_SP_ORDER_DETAIL_ITEMS2.md) | dbo.ACCOUNT, dbo.CUST_ORD_DISCOUNT, dbo.CUST_ORDER_ITEM, dbo.CUST_ORDER_TYPE, dbo.CUSTOMER, dbo.CUSTOMER_ADDRESS, dbo.CUSTOMER_ORDER, dbo.CUSTOMER_PERSON |
| dbo | [NSB_SP_ORDER_DETAIL_PMT](dbo.NSB_SP_ORDER_DETAIL_PMT.md) | dbo.ACCOUNT_TRANSACTION |
| dbo | [NSB_SP_ORDER_SUMM](dbo.NSB_SP_ORDER_SUMM.md) | dbo.ACCOUNT, dbo.ACCOUNT_TRANSACTION, dbo.CUST_ORD_CHARGE, dbo.CUST_ORDER_TYPE, dbo.CUSTOMER, dbo.CUSTOMER_ADDRESS, dbo.CUSTOMER_ORDER, dbo.CUSTOMER_PERSON |
| dbo | [NSB_SP_PRICE_OVRD1](dbo.NSB_SP_PRICE_OVRD1.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.PRC_OVRD_RSN_CODE, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_PRICE_OVRD2](dbo.NSB_SP_PRICE_OVRD2.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.PRC_OVRD_RSN_CODE, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_PRICE_OVRD3](dbo.NSB_SP_PRICE_OVRD3.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.PRC_OVRD_RSN_CODE, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_STOR_PROD1](dbo.NSB_SP_STOR_PROD1.md) | dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_STOR_PROD2](dbo.NSB_SP_STOR_PROD2.md) | dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_STOR_PROD3](dbo.NSB_SP_STOR_PROD3.md) | dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_STOR_PROD4](dbo.NSB_SP_STOR_PROD4.md) | dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_SUSP_CUST_TRN1](dbo.NSB_SP_SUSP_CUST_TRN1.md) | dbo.CUSTOMER, dbo.CUSTOMER_ADDRESS, dbo.CUSTOMER_PERSON, dbo.DEPARTMENT, dbo.ITEM, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.SUSPENDED_TRN, dbo.WORKSTATION |
| dbo | [NSB_SP_SUSP_TRN1](dbo.NSB_SP_SUSP_TRN1.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SUSP_TRN_RSN_CODE, dbo.SUSPENDED_TRN, dbo.WORKSTATION |
| dbo | [NSB_SP_SUSP_TRN2](dbo.NSB_SP_SUSP_TRN2.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SUSP_TRN_RSN_CODE, dbo.SUSPENDED_TRN, dbo.WORKSTATION |
| dbo | [NSB_SP_TILL_DEC_SUMM](dbo.NSB_SP_TILL_DEC_SUMM.md) | dbo.SETTLEMENT_TRN, dbo.STLMNT_TRN_TNDR, dbo.TENDER |
| dbo | [NSB_SP_TRAN_DISC1](dbo.NSB_SP_TRAN_DISC1.md) | dbo.EMPLOYEE, dbo.ITEM_DISCOUNT, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_TRAN_DISC2](dbo.NSB_SP_TRAN_DISC2.md) | dbo.DISCOUNT_DEF, dbo.EMPLOYEE, dbo.ITEM_DISCOUNT, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [NSB_SP_VOID_TRN1](dbo.NSB_SP_VOID_TRN1.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.WORKSTATION |
| dbo | [NSB_SP_VOID_TRN2](dbo.NSB_SP_VOID_TRN2.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.VOID_TRANSACTION, dbo.WORKSTATION |
| dbo | [NSB53_SP_POS_FLASH](dbo.NSB53_SP_POS_FLASH.md) | dbo.DEPARTMENT, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPL_ADD_DISTR_SCHED](dbo.RPL_ADD_DISTR_SCHED.md) | dbo.sp_add_jobschedule, dbo.syscategories, dbo.sysjobs |
| dbo | [RPL_DROP_PUBLICATIONS](dbo.RPL_DROP_PUBLICATIONS.md) | dbo.syspublications |
| dbo | [RPL_RUN_SNAPSHOT_AGENTS](dbo.RPL_RUN_SNAPSHOT_AGENTS.md) | dbo.sp_start_job, dbo.sysjobs |
| dbo | [RPL_SUBSCRIBE](dbo.RPL_SUBSCRIBE.md) | dbo.RPL_PUB_SUB |
| dbo | [RPL_UNSUBSCRIBE](dbo.RPL_UNSUBSCRIBE.md) | dbo.RPL_PUB_SUB |
| dbo | [RPT_DAILY_TAX_RATES1](dbo.RPT_DAILY_TAX_RATES1.md) | dbo.STORE, dbo.STORE_TEXT_VARIABLE, dbo.TAX_GRP_ZONE_AUTH, dbo.TAX_RULE, dbo.VALUE_ADDED_TAX |
| dbo | [RPT_DAILY_TAX_RATES1_SUMM](dbo.RPT_DAILY_TAX_RATES1_SUMM.md) | dbo.STORE, dbo.STORE_TEXT_VARIABLE, dbo.TAX_GRP_ZONE_AUTH, dbo.TAX_RULE, dbo.VALUE_ADDED_TAX |
| dbo | [RPT_DAILY1](dbo.RPT_DAILY1.md) | dbo.DEPARTMENT, dbo.DOC_TRN_TYPE, dbo.ITEM_DISCOUNT, dbo.ITEM_TAX_AUTH, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RETAIL_TRN_DOCUMENT, dbo.SALE_RTRN_LN_ITEM, dbo.TENDER_LINE_ITEM |
| dbo | [RPT_DAILY1_SUMM](dbo.RPT_DAILY1_SUMM.md) | dbo.DOC_TRN_TYPE, dbo.ITEM_TAX_AUTH, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RETAIL_TRN_DOCUMENT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_EMPL_PROD_EXCL_TAX1](dbo.RPT_EMPL_PROD_EXCL_TAX1.md) | dbo.EMPLOYEE, dbo.ITEM_DISCOUNT, dbo.ITEM_TAX_AUTH, dbo.OPERATOR, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_EMPL_PROD_EXCL_TAX2](dbo.RPT_EMPL_PROD_EXCL_TAX2.md) | dbo.EMPLOYEE, dbo.ITEM_TAX_AUTH, dbo.OPERATOR, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_EMPL_PROD_EXCL_TAX3](dbo.RPT_EMPL_PROD_EXCL_TAX3.md) | dbo.EMPLOYEE, dbo.ITEM_DISCOUNT, dbo.ITEM_TAX_AUTH, dbo.OPERATOR, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_FLASH_SALES_EXCL_TAX1](dbo.RPT_FLASH_SALES_EXCL_TAX1.md) | dbo.ITEM_TAX_AUTH, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [RPT_GET_ALL_DEPT](dbo.RPT_GET_ALL_DEPT.md) | dbo.DEPARTMENT, dbo.DIVISION |
| dbo | [RPT_GET_ALL_DEPT_NO_DIV](dbo.RPT_GET_ALL_DEPT_NO_DIV.md) | dbo.DEPARTMENT |
| dbo | [RPT_GET_CUST_ORD_TYPE](dbo.RPT_GET_CUST_ORD_TYPE.md) | dbo.CUST_ORDER_TYPE |
| dbo | [RPT_GET_DEPT](dbo.RPT_GET_DEPT.md) | dbo.DEPARTMENT |
| dbo | [RPT_GET_DEPT_GROUP](dbo.RPT_GET_DEPT_GROUP.md) | dbo.DEPT_GROUP |
| dbo | [RPT_GET_DIV](dbo.RPT_GET_DIV.md) | dbo.DIVISION |
| dbo | [RPT_GET_EMPL](dbo.RPT_GET_EMPL.md) | dbo.EMPLOYEE, dbo.OPERATOR, dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_GET_ITEM_GROUP](dbo.RPT_GET_ITEM_GROUP.md) | dbo.ITEM_GROUP |
| dbo | [RPT_GET_ORDER_NUMBER](dbo.RPT_GET_ORDER_NUMBER.md) | dbo.CUSTOMER_ORDER |
| dbo | [RPT_GET_ORDER_TYPE_CODE](dbo.RPT_GET_ORDER_TYPE_CODE.md) | dbo.CUST_ORDER_TYPE |
| dbo | [RPT_GET_PRD_BGN_DT](dbo.RPT_GET_PRD_BGN_DT.md) | dbo.CUSTOM_PERIOD |
| dbo | [RPT_GET_TRN_SALE_TIME](dbo.RPT_GET_TRN_SALE_TIME.md) | dbo.RETAIL_TRANSACTION |
| dbo | [RPT_GET_WEEK](dbo.RPT_GET_WEEK.md) | dbo.FISCAL_DAY, dbo.FISCAL_WEEK |
| dbo | [RPT_GET_WEEK_ID](dbo.RPT_GET_WEEK_ID.md) | dbo.FISCAL_DAY |
| dbo | [RPT_HOURLY_SALES1](dbo.RPT_HOURLY_SALES1.md) | dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_MRCH_DEPT_EXCL_TAX1](dbo.RPT_MRCH_DEPT_EXCL_TAX1.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM, dbo.ITEM_DISCOUNT, dbo.ITEM_TAX_AUTH, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_MRCH_DEPT_EXCL_TAX2](dbo.RPT_MRCH_DEPT_EXCL_TAX2.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM, dbo.ITEM_TAX_AUTH, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_MRCH_DEPT_EXCL_TAX3](dbo.RPT_MRCH_DEPT_EXCL_TAX3.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM, dbo.ITEM_DISCOUNT, dbo.ITEM_TAX_AUTH, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_MRCH_DEPT_SUM2](dbo.RPT_MRCH_DEPT_SUM2.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM, dbo.ITEM_DISCOUNT, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_MRCH_RESTOCKING1](dbo.RPT_MRCH_RESTOCKING1.md) | dbo.COLOR, dbo.CUST_ORD_LN_ITEM, dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_MRCH_SUM_EXCL_TAX1](dbo.RPT_MRCH_SUM_EXCL_TAX1.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.ITEM, dbo.ITEM_DISCOUNT, dbo.ITEM_TAX_AUTH, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.RPT_SELECT_OBJECT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_NON_MRCH_EXCL_TAX1](dbo.RPT_NON_MRCH_EXCL_TAX1.md) | dbo.ITEM, dbo.ITEM_TAX_AUTH, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_RUS_KO4](dbo.RPT_RUS_KO4.md) | dbo.SAFE_TENDER_STLMNT, dbo.SETTLEMENT_TRN, dbo.SETTLEMENT_TRN_EXT, dbo.STORE_SAFE_TENDER, dbo.TENDER_CONTROL_TRN, dbo.TENDER_CONTROL_TRN_EXT |
| dbo | [RPT_SALES_BY_DEPT1](dbo.RPT_SALES_BY_DEPT1.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_SALES_PLAN1](dbo.RPT_SALES_PLAN1.md) | dbo.FISCAL_DAY, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.STORE_GOAL |
| dbo | [RPT_SALESPERSON_PROD1](dbo.RPT_SALESPERSON_PROD1.md) | dbo.EMPLOYEE, dbo.ITEM_DISCOUNT, dbo.OPERATOR, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.SPIFF |
| dbo | [RPT_SALESPERSON_PROD2](dbo.RPT_SALESPERSON_PROD2.md) | dbo.EMPLOYEE, dbo.ITEM_DISCOUNT, dbo.OPERATOR, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.SPIFF |
| dbo | [RPT_SEL_DEPT_FL_ITM_GRP](dbo.RPT_SEL_DEPT_FL_ITM_GRP.md) | dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_DEPT_FILL_ALL](dbo.RPT_SELECT_DEPT_FILL_ALL.md) | dbo.DEPARTMENT, dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_DEPT_FILL_DEPT](dbo.RPT_SELECT_DEPT_FILL_DEPT.md) | dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_DEPT_FILL_DIV](dbo.RPT_SELECT_DEPT_FILL_DIV.md) | dbo.DEPARTMENT, dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_DEPT_FILL_GROUP](dbo.RPT_SELECT_DEPT_FILL_GROUP.md) | dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_EMPL_FILL_ALL](dbo.RPT_SELECT_EMPL_FILL_ALL.md) | dbo.EMPLOYEE, dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_EMPL_FILL_EMPL](dbo.RPT_SELECT_EMPL_FILL_EMPL.md) | dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_OBJECT_DEL_ALL](dbo.RPT_SELECT_OBJECT_DEL_ALL.md) | dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_OBJECT_DEL_ID](dbo.RPT_SELECT_OBJECT_DEL_ID.md) | dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SELECT_TIME_PRD](dbo.RPT_SELECT_TIME_PRD.md) | dbo.DAY_TIME_BIN, dbo.RPT_SELECT_OBJECT |
| dbo | [RPT_SP_FLASH_SALES](dbo.RPT_SP_FLASH_SALES.md) | dbo.T_DATE_ONLY, dbo.T_FLG, dbo.T_KEY_NUMBER, dbo.WRKST_LOCAL_SALES |
| dbo | [RPT_SP_STORE_FLASH_SALES](dbo.RPT_SP_STORE_FLASH_SALES.md) | dbo.CUST_ORD_LN_ITEM, dbo.ITEM, dbo.ITEM_TAX_AUTH, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.T_DATE_ONLY, dbo.T_FLG, dbo.T_KEY_NUMBER, dbo.T_LONG_CODE_W |
| dbo | [RPT_SP_TRAFFIC_COUNT1](dbo.RPT_SP_TRAFFIC_COUNT1.md) | dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.TRAFFIC_COUNT |
| dbo | [RPT_STOR_PROD_EXCL_TAX1](dbo.RPT_STOR_PROD_EXCL_TAX1.md) | dbo.ITEM_DISCOUNT, dbo.ITEM_TAX_AUTH, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [RPT_STOR_PROD_EXCL_TAX2](dbo.RPT_STOR_PROD_EXCL_TAX2.md) | dbo.ITEM_TAX_AUTH, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [RPT_STOR_PROD_EXCL_TAX3](dbo.RPT_STOR_PROD_EXCL_TAX3.md) | dbo.ITEM_DISCOUNT, dbo.ITEM_TAX_AUTH, dbo.PRICE_OVERRIDE, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [RPT_STORE_DAILY_DOCS](dbo.RPT_STORE_DAILY_DOCS.md) | dbo.DOC_TRN_TYPE, dbo.RETAIL_TRANSACTION, dbo.RETAIL_TRN_DOCUMENT |
| dbo | [RPT_STORE_INFO](dbo.RPT_STORE_INFO.md) | dbo.STORE, dbo.STORE_TEXT_VARIABLE |
| dbo | [RPT_SYNC_CHECK_ID](dbo.RPT_SYNC_CHECK_ID.md) | dbo.RPT_SYNC |
| dbo | [RPT_SYNC_DEL_ALL](dbo.RPT_SYNC_DEL_ALL.md) | dbo.RPT_SYNC |
| dbo | [RPT_SYNC_DEL_ID](dbo.RPT_SYNC_DEL_ID.md) | dbo.RPT_SYNC |
| dbo | [RPT_SYNC_FILL_ID](dbo.RPT_SYNC_FILL_ID.md) | dbo.RPT_SYNC |
| dbo | [RPT_TOP_SELL_BY_QTY1](dbo.RPT_TOP_SELL_BY_QTY1.md) | dbo.COLOR, dbo.DEPARTMENT, dbo.DEPT_GROUP, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_WRKST_DAILY_INVOICES](dbo.RPT_WRKST_DAILY_INVOICES.md) | dbo.DOC_TRN_TYPE, dbo.PMT_ACCT_LN_ITEM, dbo.RETAIL_TRANSACTION, dbo.RETAIL_TRN_DOCUMENT, dbo.SALE_RTRN_LN_ITEM |
| dbo | [RPT_WRKST_DAILY_TOTALS](dbo.RPT_WRKST_DAILY_TOTALS.md) | dbo.PMT_ACCT_LN_ITEM, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.WORKSTATION |
| dbo | [RPT_WRKST_SALES_BY_VAT_RATE](dbo.RPT_WRKST_SALES_BY_VAT_RATE.md) | dbo.ITEM_TAX_AUTH, dbo.RETAIL_TRANSACTION, dbo.SALE_RTRN_LN_ITEM, dbo.STORE, dbo.TAX_GRP_ZONE_AUTH, dbo.TAX_RULE, dbo.VALUE_ADDED_TAX |
| dbo | [spTSM_Not_Posting](dbo.spTSM_Not_Posting.md) | dbo.retail_transaction, dbo.sp_send_dbmail |
| -- Description: | [Checks for the last time of the last transaction posted to RETAIL_TRANSACTION table](--_Description_.Checks_for_the_last_time_of_the_last_transaction_posted_to_RETAIL_TRANSACTION_table.md) |  |
| dbo | [spUSICOALTransCountCheck](dbo.spUSICOALTransCountCheck.md) | dbo.notification_history, dbo.RETAIL_TRANSACTION, dbo.sp_send_dbmail |
| -- Description: | [Sends email alerts if no or too few transaction have been posted to USICOAL db on POSDBS (ER)](--_Description_.Sends_email_alerts_if_no_or_too_few_transaction_have_been_posted_to_USICOAL_db_on_POSDBS_ER.md) |  |
