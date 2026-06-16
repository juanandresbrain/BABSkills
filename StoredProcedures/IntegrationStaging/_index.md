# Stored Procedures: IntegrationStaging

| Schema | Name | Table Dependencies |
|---|---|---|
| ComHub | [spFTPCommercehubCostcoWebConfirmations](ComHub.spFTPCommercehubCostcoWebConfirmations.md) | ComHub.ComhubFTPLog, ComHub.ComhubFTPTransmissionLogDump, ComHub.tmpComhubFTP |
| ComHub | [spFTPCommercehubCostcoWebFAs](ComHub.spFTPCommercehubCostcoWebFAs.md) | ComHub.ComhubFTPLog, ComHub.ComhubFTPTransmissionLogDump, ComHub.tmpComhubFTP |
| ComHub | [spFTPGetCommercehubCostcoPOs](ComHub.spFTPGetCommercehubCostcoPOs.md) | ComHub.ComhubFTPTransmissionLogDump, ComHub.tmpComhubFTP |
| dbo | [sp_alterdiagram](dbo.sp_alterdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_creatediagram](dbo.sp_creatediagram.md) | dbo.sysdiagrams |
| dbo | [sp_dropdiagram](dbo.sp_dropdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagramdefinition](dbo.sp_helpdiagramdefinition.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagrams](dbo.sp_helpdiagrams.md) | dbo.sysdiagrams |
| dbo | [sp_renamediagram](dbo.sp_renamediagram.md) | dbo.sysdiagrams |
| dbo | [sp_upgraddiagrams](dbo.sp_upgraddiagrams.md) | dbo.dtproperties, dbo.sysdiagrams |
| dbo | [sp_VoucherLookup](dbo.sp_VoucherLookup.md) | dbo.address, dbo.Country, dbo.cust_liability, dbo.cust_liability_history, dbo.customer, dbo.Discount |
| dbo | [spAdyen_Bank_Export](dbo.spAdyen_Bank_Export.md) | dbo.babw_adyen, dbo.tmp_adyen_bank, dbo.tmp_adyen_bank_control, dbo.tmp_adyen_bank_out |
| dbo | [spAdyenFileCheck](dbo.spAdyenFileCheck.md) | dbo.babw_babcanpos, dbo.babw_babgbrpos, dbo.babw_babgbrweb, dbo.babw_babusapos, dbo.babw_babusaweb |
| dbo | [spAdyenFileControl](dbo.spAdyenFileControl.md) | dbo.babw_adyen_merchant, dbo.babw_babcanpos, dbo.babw_babgbrpos, dbo.babw_babgbrweb, dbo.babw_babusapos, dbo.babw_babusaweb |
| dbo | [spAmex_Bank_Export](dbo.spAmex_Bank_Export.md) | dbo.babw_amexUS, dbo.tmp_amex_bank, dbo.tmp_amex_bank_control, dbo.tmp_amex_bank_out |
| dbo | [spDecryptFiles](dbo.spDecryptFiles.md) |  |
| dbo | [spDeleteOldFiles](dbo.spDeleteOldFiles.md) | dbo.xp_cmdshell |
| dbo | [spDeleteOldFilesHardCodedDirectories](dbo.spDeleteOldFilesHardCodedDirectories.md) | dbo.usp_delete_old_files |
| dbo | [spDynamicActionSQLJobHistoryEmail](dbo.spDynamicActionSQLJobHistoryEmail.md) | dbo.agent_datetime, dbo.DynamicActionSQLJobHistory, dbo.jh, dbo.sp_send_dbmail, dbo.sysjobhistory, dbo.sysjobs |
| dbo | [spEasyMetricsTransform](dbo.spEasyMetricsTransform.md) | dbo.BabEasyMetricsWmsStaging, dbo.BabEasyMetricsWmsStagingTransformed |
| dbo | [spEasyMetricsTransform_Bak20231212](dbo.spEasyMetricsTransform_Bak20231212.md) | dbo.BabEasyMetricsWmsStaging, dbo.BabEasyMetricsWmsStagingTransformed |
| dbo | [spEmailSQLAgentJobStart](dbo.spEmailSQLAgentJobStart.md) | dbo.sp_send_dbmail |
| dbo | [spFTPtest](dbo.spFTPtest.md) |  |
| dbo | [spFTPtest2](dbo.spFTPtest2.md) |  |
| dbo | [spGetCRMCustomerNumberByEmailAddress](dbo.spGetCRMCustomerNumberByEmailAddress.md) | dbo.customer, dbo.email, dbo.email_division |
| dbo | [spIndexRebuildReorganize](dbo.spIndexRebuildReorganize.md) |  |
| dbo | [spMergePimBundleSkuExtract](dbo.spMergePimBundleSkuExtract.md) | dbo.PimBundleSkuExtract, dbo.PimBundleSkuExtractStageConsolidatedAndCleansed |
| dbo | [spMergePimBundleSkuExtract_Bak20240905](dbo.spMergePimBundleSkuExtract_Bak20240905.md) | dbo.PimBundleSkuExtract, dbo.PimBundleSkuExtractStageConsolidatedAndCleansed |
| dbo | [spMergePimBundleSkuExtract_Bak20241003](dbo.spMergePimBundleSkuExtract_Bak20241003.md) | dbo.PimBundleSkuExtract, dbo.PimBundleSkuExtractStageConsolidatedAndCleansed |
| dbo | [spMergeSQLBackupsJobHistory](dbo.spMergeSQLBackupsJobHistory.md) | dbo.SQLBackupsJobHistory, dbo.SQLBackupsJobHistoryStage |
| dbo | [spMergeUsersMultipleLocs](dbo.spMergeUsersMultipleLocs.md) | ERP.UserLoadtoD365multipleLocations, ERP.UserLoadtoD365multipleLocationsStage |
| dbo | [spOutputXMLFile](dbo.spOutputXMLFile.md) |  |
| dbo | [spPaymentech_CopyFiles_CAN](dbo.spPaymentech_CopyFiles_CAN.md) | dbo.sp_send_dbmail |
| dbo | [spPaymentech_CopyFiles_US](dbo.spPaymentech_CopyFiles_US.md) | dbo.sp_send_dbmail |
| dbo | [spRestartHungSQLAgentJobs](dbo.spRestartHungSQLAgentJobs.md) | dbo.sp_start_job, dbo.sp_stop_job, dbo.sysjobactivity, dbo.sysjobs_view |
| dbo | [spSalesToDynamicsWeeklyUpdateJobHistoryEmail](dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail.md) | dbo.agent_datetime, dbo.date_dim, dbo.jh, dbo.SalesToDynamicsWeeklyUpdateSQLJobHistory, dbo.sp_send_dbmail, dbo.sysjobhistory, dbo.sysjobs |
| dbo | [spStoreSalesCheck_EmailAlerts](dbo.spStoreSalesCheck_EmailAlerts.md) | dbo.sp_send_dbmail, dbo.StoreSalesCheck_Diff |
| dbo | [spStoreSalesCheck_EmailAlerts_NotifyBusiness](dbo.spStoreSalesCheck_EmailAlerts_NotifyBusiness.md) | dbo.sp_send_dbmail, dbo.StoreSalesCheck_Diff, dbo.tmpStoresZeroSales |
| dbo | [spStoreSalesCheck_Find_SalesDiff](dbo.spStoreSalesCheck_Find_SalesDiff.md) | dbo.POLLING_STORES, dbo.POSSalesTotalByDay, dbo.spPOSSalesTotalByDay, dbo.spPOSSalesTotalByDayByTransaction, dbo.StoreSalesCheck_Diff, dbo.StoreSalesCheck_StoreList, dbo.StoreSalesCheck_StoreSales, dbo.sv_merchandise_detail, dbo.transaction_header, dbo.transaction_line |
| dbo | [spStoreSalesCheck_Find_SalesDiff_Backup20230417](dbo.spStoreSalesCheck_Find_SalesDiff_Backup20230417.md) | dbo.POLLING_STORES, dbo.StoreSalesCheck_Diff, dbo.StoreSalesCheck_StoreList, dbo.StoreSalesCheck_StoreSales, dbo.sv_merchandise_detail, dbo.transaction_header, dbo.transaction_line |
| dbo | [spStoreSalesCheck_Find_SalesDiff_backup20240131](dbo.spStoreSalesCheck_Find_SalesDiff_backup20240131.md) | dbo.POLLING_STORES, dbo.POSSalesTotalByDay, dbo.spPOSSalesTotalByDay, dbo.spPOSSalesTotalByDayByTransaction, dbo.StoreSalesCheck_Diff, dbo.StoreSalesCheck_StoreList, dbo.StoreSalesCheck_StoreSales, dbo.sv_merchandise_detail, dbo.transaction_header, dbo.transaction_line |
| dbo | [spStoreSalesCheck_Find_SalesDiff_Bak20230815](dbo.spStoreSalesCheck_Find_SalesDiff_Bak20230815.md) | dbo.POLLING_STORES, dbo.StoreSalesCheck_Diff, dbo.StoreSalesCheck_StoreList, dbo.StoreSalesCheck_StoreSales, dbo.sv_merchandise_detail, dbo.transaction_header, dbo.transaction_line, dbo.vwPOSSalesTotalByDay |
| dbo | [spStoreSalesCheck_Insert_WebSales](dbo.spStoreSalesCheck_Insert_WebSales.md) | dbo.NSBTranslate_batch, dbo.NSBTranslate_logTrans, dbo.StoreSalesCheck_StoreSales |
| dbo | [spValidateGetReturn](dbo.spValidateGetReturn.md) | dbo.all_customer_keys, Item.value |
| dbo | [WMS.[spMergeDynamicsAverageCost](dbo_WMS._spMergeDynamicsAverageCost.md) | WMS.DynamicsAverageCost, WMS.DynamicsAverageCostStage |
| ERP | [spDistributionsReadyToRelease](ERP.spDistributionsReadyToRelease.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, erp.tmpDistributionsReadyToRelease, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM |
| ERP | [spDistributionsReadyToRelease_Bak20231205](ERP.spDistributionsReadyToRelease_Bak20231205.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, erp.tmpDistributionsReadyToRelease, erp.vwDistributionsReleased, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM |
| ERP | [spEmailItemsMissingDimensionData](ERP.spEmailItemsMissingDimensionData.md) | dbo.sp_send_dbmail, dbo.tmpERPItemsMissingDimensionData, ERP.vwProductDimensionLookup |
| ERP | [spEmailPoReceiptsValidation](ERP.spEmailPoReceiptsValidation.md) | dbo.sp_send_dbmail, ERP.vwValidation_POReceipts |
| ERP | [spItemLoadReleasedProductCreationXML](ERP.spItemLoadReleasedProductCreationXML.md) | ERP.ItemLoadtoD365, wms.ItemMaster, wms.vwItemsCompareMerchvsDynamics |
| ERP | [spItemLoadReleasedProductsXML](ERP.spItemLoadReleasedProductsXML.md) | ERP.ItemLoadtoD365, erp.ItemMaster |
| ERP | [spMergeCostcoInboundPODetail](ERP.spMergeCostcoInboundPODetail.md) | ERP.CostcoInboundPODetail, ERP.CostcoInboundPODetailStage |
| ERP | [spMergeCostcoInboundPOHeader](ERP.spMergeCostcoInboundPOHeader.md) | ERP.CostcoInboundPOHeader, ERP.CostcoInboundPOHeaderStage |
| ERP | [spMergeDistributionAddressDim](ERP.spMergeDistributionAddressDim.md) | ERP.DistributionAddressDim, erp.DistributionAddressDimStage, erp.FranchiseeLocationMap |
| ERP | [spMergeDistributiondDetail](ERP.spMergeDistributiondDetail.md) | ERP.DistributionDetail, ERP.DistributionDetailStage |
| ERP | [spMergeDistributiondDetail_BAK20231117](ERP.spMergeDistributiondDetail_BAK20231117.md) | ERP.DistributionDetail, ERP.DistributionDetailStage |
| ERP | [spMergeFranchiseeLocationMap](ERP.spMergeFranchiseeLocationMap.md) | ERP.FranchiseeLocationMap, ERP.FranchiseeLocationMapStage |
| ERP | [spMergeItemLoadtoD365](ERP.spMergeItemLoadtoD365.md) | ERP.ItemLoadtoD365, ERP.ItemLoadtoD365Archive, ERP.ItemLoadtoD365Stage |
| ERP | [spMergeItemLoadtoD365BAK20220801](ERP.spMergeItemLoadtoD365BAK20220801.md) | ERP.ItemLoadtoD365, ERP.ItemLoadtoD365Archive, ERP.ItemLoadtoD365Stage |
| ERP | [spMergeItemLoadtoD365BAK20231113](ERP.spMergeItemLoadtoD365BAK20231113.md) | ERP.ItemLoadtoD365, ERP.ItemLoadtoD365Archive, ERP.ItemLoadtoD365Stage |
| ERP | [spMergeItemMasterToWM](ERP.spMergeItemMasterToWM.md) | erp.ItemMasterToWM, erp.ItemMasterToWMStage |
| ERP | [spMergeItemVendorLoadtoD365](ERP.spMergeItemVendorLoadtoD365.md) | ERP.ItemVendorLoadtoD365, ERP.ItemVendorLoadtoD365Stage |
| ERP | [spMergePurchaseOrderHeader](ERP.spMergePurchaseOrderHeader.md) | ERP.PurchaseOrderHeader, ERP.vwPurchaseOrderHeaderDynamicsExtract |
| ERP | [spMergePurchaseOrderHeader_Bak20210125](ERP.spMergePurchaseOrderHeader_Bak20210125.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderHeaderStage |
| ERP | [spMergePurchaseOrderLines](ERP.spMergePurchaseOrderLines.md) | ERP.PurchaseOrderLines, ERP.PurchaseOrderLinesStage, ERP.vwPurchaseOrderLinesDynamicsExtract |
| ERP | [spMergePurchaseOrderLines_Bak20210125](ERP.spMergePurchaseOrderLines_Bak20210125.md) | ERP.PurchaseOrderLines, ERP.PurchaseOrderLinesStage |
| ERP | [spMergePurchaseOrderLinesServiceItems](ERP.spMergePurchaseOrderLinesServiceItems.md) | ERP.PurchaseOrderLinesServiceItems, ERP.PurchaseOrderLinesStage, ERP.vwPurchaseOrderLinesDynamicsExtractServiceItems |
| ERP | [spMergePurchaseOrderReceipt](ERP.spMergePurchaseOrderReceipt.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.PurchaseOrderReceipt, ERP.PurchaseOrderReceiptExceptions, ERP.PurchaseOrderReceiptStage, wms.ItemsUOM, wms.vwAptosPOtoDynamicsLogDetail |
| ERP | [spMergePurchTableSDL](ERP.spMergePurchTableSDL.md) | ERP.PurchTableSDL, ERP.PurchTableSDLStage |
| ERP | [spMergeVendorMaster](ERP.spMergeVendorMaster.md) | ERP.VendorMaster, ERP.VendorMasterStage |
| ERP | [spMergeVendorMasterBACKUP20231113](ERP.spMergeVendorMasterBACKUP20231113.md) | ERP.VendorMaster, ERP.VendorMasterStage |
| ERP | [spMergeWarehouseInventoryAdjustment_BAK20230911](ERP.spMergeWarehouseInventoryAdjustment_BAK20230911.md) | ERP.WarehouseInventoryAdjustment, ERP.WarehouseInventoryAdjustmentStage |
| ERP | [spMergeWhseReceipt_NonPO](ERP.spMergeWhseReceipt_NonPO.md) | ERP.WhseReceipt_NonPO, ERP.WhseReceiptStage_NonPO |
| ERP | [spOutputCostcoPOxml](ERP.spOutputCostcoPOxml.md) | ERP.CostcoInboundPODetail, ERP.CostcoInboundPOHeader, WEB.spOutputXMLFile |
| ERP | [spOutputD365PurchaseOrderReceiptXMLByEntity](ERP.spOutputD365PurchaseOrderReceiptXMLByEntity.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderReceipt, ERP.spOutputXMLFile, ERP.tmpReceiptID, wms.ItemMaster, WMS.PurchaseOrderMerchToDynamics |
| ERP | [spOutputD365PurchaseOrderReceiptXMLByEntityBAK20230123](ERP.spOutputD365PurchaseOrderReceiptXMLByEntityBAK20230123.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderReceipt, ERP.spOutputXMLFile, ERP.tmpReceiptID, wms.ItemMaster, WMS.PurchaseOrderMerchToDynamics |
| ERP | [spOutputItemLoadxml](ERP.spOutputItemLoadxml.md) | ERP.ItemLoadtoD365, WEB.spOutputXMLFile |
| ERP | [spOutputShipmentInvoice_TransferXML](ERP.spOutputShipmentInvoice_TransferXML.md) | ERP.OrderShipmentInvoice, WEB.spOutputXMLFile |
| ERP | [spOutputShipmentInvoice_TransferXMLByEntity](ERP.spOutputShipmentInvoice_TransferXMLByEntity.md) | ERP.ShipmentInvoice, WEB.spOutputXMLFile |
| ERP | [spOutputTPMPurchaseOrderXML](ERP.spOutputTPMPurchaseOrderXML.md) | dbo.L, dbo.L2, ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.PurchaseOrderLinesServiceItems, ERP.spOutputXMLFile, ERP.tmpTPMpo, ERP.vwPurchaseOrderTPM |
| ERP | [spOutputTPMPurchaseOrderXML_BAK20210927](ERP.spOutputTPMPurchaseOrderXML_BAK20210927.md) | dbo.L, ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.spOutputXMLFile, ERP.tmpTPMpo, ERP.vwPurchaseOrderTPM |
| ERP | [spOutputWMStoreMasterXML](ERP.spOutputWMStoreMasterXML.md) | ERP.DistributionAddressDim, ERP.spOutputXMLFile |
| ERP | [spOutputXMLFile](ERP.spOutputXMLFile.md) |  |
| ERP | [spPFTGetOpenToByRollingCountsAndAttributes_ERP](ERP.spPFTGetOpenToByRollingCountsAndAttributes_ERP.md) | dbo.tmpPFTStyleRollingCountsAndAttributes_ERP, ERP.InventoryMovementJournalEntryStage, ERP.ItemMaster, ERP.ItemMasterProducts, ERP.ItemsUOM, ERP.SupplyCategoryAssignments, ERP.tmpPFTStyleRollingCountsAndAttributes_ERP, ERP.vwSuppliesOnOrder, ERP.vwSuppliesReceived, ERP.WarehouseOnHand |
| ERP | [spPOReceiptsImportCN](ERP.spPOReceiptsImportCN.md) | ERP.PurchaseOrderReceiptPreStage |
| ERP | [spPOReceiptsImportUK](ERP.spPOReceiptsImportUK.md) | ERP.PurchaseOrderReceiptPreStage |
| ERP | [spPOReceiptsImportWC](ERP.spPOReceiptsImportWC.md) | dbo.rcpt_dir, dbo.wc_receipt_file, dbo.wc_xfer_receipt_file, ERP.PurchaseOrderReceiptPreStage, ERP.WCPalletReceipts |
| ERP | [spPurchaseOrderDBS_FileCreateFTP](ERP.spPurchaseOrderDBS_FileCreateFTP.md) | dbo.ftpPUTdbsPOexport, ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.PurchaseOrderToDBSchenker |
| ERP | [spPurchaseOrderReceiptXML](ERP.spPurchaseOrderReceiptXML.md) | ERP.PurchaseOrderLines, ERP.vwPurchaseOrderReceipts |
| ERP | [spPurchaseOrderReceiptXML_Bak_20230123](ERP.spPurchaseOrderReceiptXML_Bak_20230123.md) | ERP.PurchaseOrderLines, ERP.vwPurchaseOrderReceipts |
| ERP | [spPurchaseOrderUpdateSendDataBAK20210929](ERP.spPurchaseOrderUpdateSendDataBAK20210929.md) | erp.PurchaseOrderHeader, ERP.PurchaseOrderLines |
| ERP | [spShipmentInvoice_TransferXML](ERP.spShipmentInvoice_TransferXML.md) | ERP.ShipmentInvoice |
| ES | [spGetEndlessAisleOrdersNotInEsell](ES.spGetEndlessAisleOrdersNotInEsell.md) | dbo.JMC_sls_order, dbo.JMC_sls_order_line_item, ES.EndlessAisleOrdersNotInEnterpriseSelling, ES.OMSReferenceNumberBridge, esell.orders |
| ES | [spMergeOMSReferenceNumberBridge](ES.spMergeOMSReferenceNumberBridge.md) | ES.OMSReferenceNumberBridge, ES.ReferenceNumberType |
| NOCDev | [spGetOrdersNotInSalesAudit](NOCDev.spGetOrdersNotInSalesAudit.md) | WM.OrdersNotInSalesAudit |
| NOCDev | [spGetRYVRecords](NOCDev.spGetRYVRecords.md) | dbo.Orders |
| NOCDev | [spGetRYVTransfers](NOCDev.spGetRYVTransfers.md) | dbo.Orders |
| NOCDev | [spGetSelfUpdaterLogErrors](NOCDev.spGetSelfUpdaterLogErrors.md) | dbo.UpdateLog |
| NOCDev | [spGetSQLJobStatus_All](NOCDev.spGetSQLJobStatus_All.md) | dbo.agent_datetime, dbo.sysjobhistory, dbo.sysjobs |
| NOCDev | [spGetSQLJobStatus_Shipped](NOCDev.spGetSQLJobStatus_Shipped.md) | dbo.agent_datetime, dbo.sysjobhistory, dbo.sysjobs |
| NOCDev | [spGetSQLJobStatus_UpdateDeckStatus](NOCDev.spGetSQLJobStatus_UpdateDeckStatus.md) | dbo.agent_datetime, dbo.sysjobhistory, dbo.sysjobs |
| NOCDev | [spGetSQLJobStatus_Waved](NOCDev.spGetSQLJobStatus_Waved.md) | dbo.agent_datetime, dbo.sysjobhistory, dbo.sysjobs |
| NOCDev | [spGetWaveOrders](NOCDev.spGetWaveOrders.md) | WMS.SalesOrderStatusUpdateWaved |
| NOCDev | [spGetWaveTimes](NOCDev.spGetWaveTimes.md) | WM.WaveJob |
| NOCDev | [spGetWeeklyUpdateSets](NOCDev.spGetWeeklyUpdateSets.md) | dbo.UpdateLog |
| POS | [spMergeStoreInventoryForEnterpriseInventory](POS.spMergeStoreInventoryForEnterpriseInventory.md) | POS.StoreInventoryForEnterpriseInventory, POS.StoreInventoryForEnterpriseInventoryStage |
| POS | [spMergeZebraLabelPricing](POS.spMergeZebraLabelPricing.md) | dbo.custom_property, dbo.entity_custom_property, dbo.hierarchy_group, dbo.sku, dbo.style, dbo.style_description, dbo.style_group, dbo.style_retail, dbo.upc, POS.ZebraLabelProductInfo |
| POS | [spZebraBarcodeAPI_GetStylesWithUPC](POS.spZebraBarcodeAPI_GetStylesWithUPC.md) | dbo.ZebraLabelProductInfo |
| Reporting | [spEmailErrosWhenDroppingInvalidSQLServerLogins](Reporting.spEmailErrosWhenDroppingInvalidSQLServerLogins.md) | dbo.sp_send_dbmail, Reporting.SQLServerUserAccountCleanupFailures |
| StoreForce | [spMergeStoreHours](StoreForce.spMergeStoreHours.md) | StoreForce.StoreHours, StoreForce.StoreHoursStage |
| TXT | [spItemDetailsPLM](TXT.spItemDetailsPLM.md) | archive.Products, dbo.product_dim, TXT.ItemDetailsPLM |
| TXT | [spOnHandFields](TXT.spOnHandFields.md) | dbo.dynamics_InventTrans, dbo.dynamics_InventTransOrigin, dbo.Dynamics_SalesLine, TXT.BOPOHRetailTotalTE, TXT.BOPOHUnitsTotal, TXT.EOPOHCostTotal, TXT.EOPOHRetailTotalTE, TXT.EOPOHUnitsTotal, TXT.PrdDates |
| TXT | [spPeriodDates](TXT.spPeriodDates.md) | dbo.date_dim, TXT.PrdDates |
| TXT | [spWeeklyReportTable](TXT.spWeeklyReportTable.md) | txt.PrdDates |
| WEB | [spEmailPartyWebOrderShippedSummary_BAK06172024](WEB.spEmailPartyWebOrderShippedSummary_BAK06172024.md) | dbo.sp_send_dbmail, WEB.PartyTransferOrdersShipped |
| WEB | [spFTPgetUKfiles_Web_WinSCP](WEB.spFTPgetUKfiles_Web_WinSCP.md) | dbo.sftpGETLogUKWhseWeb |
| WEB | [spFTPukORDERSTEST](WEB.spFTPukORDERSTEST.md) | dbo.sp_send_dbmail, WEB.tmpFTPukWeb |
| WEB | [spFTPukWarehouseOrderStatusUpdate](WEB.spFTPukWarehouseOrderStatusUpdate.md) | WEB.tmpFTGetWeb, WEB.UKFTPTransmissionLogDump |
| WEB | [spFTPukWarehouseOrderStatusUpdatesTest](WEB.spFTPukWarehouseOrderStatusUpdatesTest.md) | WEB.tmpFTGetWeb, WEB.UKFTPTransmissionLogDump |
| WEB | [spGoogleAdsInventoryLoad](WEB.spGoogleAdsInventoryLoad.md) | dbo.product_dim, dbo.str_dim, dbo.str_open_dim, web.GoogleAdsPricebookStage, web.PricebookFact, web.vwStoreInventoryCSV |
| WEB | [spMergeAlternateImages](WEB.spMergeAlternateImages.md) | WEB.AlternateImages, WEB.AlternateImagesArchive, WEB.AlternateImagesStage |
| WEB | [spMergeAltImageTags](WEB.spMergeAltImageTags.md) | Web.AltImageTags, Web.AltImageTagsStage |
| WEB | [spMergeInventoryFactFromWM](WEB.spMergeInventoryFactFromWM.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.style, dbo.vwWebHierarchy, dbo.vwWebIncludedStyles, WEB.InventoryFact, WEB.ProductCatalogMasterAttributes, web.UKWebstoreProductBalance, WEB.WMInventoryStage |
| WEB | [spMergeInventoryFactFromWMbackup20191208](WEB.spMergeInventoryFactFromWMbackup20191208.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.style, WEB.InventoryFact, WEB.ProductCatalogMasterAttributes, WEB.WMInventoryStage |
| WEB | [spMergePreOrderBackOrderInventory](WEB.spMergePreOrderBackOrderInventory.md) | web.PreOrderBackOrderInventory, web.PreOrderBackOrderInventoryStage |
| WEB | [spMergePricebookBundleSkuFact](WEB.spMergePricebookBundleSkuFact.md) | WEB.PricebookBundleSkuFact, WEB.vwBundlePricebookFactPreStage |
| WEB | [spMergePricebookBundleSkuFact_Bak20241003](WEB.spMergePricebookBundleSkuFact_Bak20241003.md) | WEB.PricebookBundleSkuFact, WEB.vwBundlePricebookFactPreStage |
| WEB | [spMergePricebookFact](WEB.spMergePricebookFact.md) | WEB.PricebookFact, WEB.PricebookFactArchive, WEB.PricebookStage |
| WEB | [spMergePricebookFact_BAK20220705](WEB.spMergePricebookFact_BAK20220705.md) | WEB.PricebookFact, WEB.PricebookFactArchive, WEB.PricebookStage |
| WEB | [spMergePricebookPreStage](WEB.spMergePricebookPreStage.md) | WEB.PricebookPreStage, WEB.PricebookPreStageBase |
| WEB | [spMergeProductCatalogMasterAttributes](WEB.spMergeProductCatalogMasterAttributes.md) | web.InventoryFact, web.PricebookFact, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterAttributesStage |
| WEB | [spMergeProductCatalogMasterAttributes_backup20221102](WEB.spMergeProductCatalogMasterAttributes_backup20221102.md) | web.InventoryFact, web.PricebookFact, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterAttributesStage |
| WEB | [spMergeProductCatalogPimberly](WEB.spMergeProductCatalogPimberly.md) | WEB.ProductCatalogPimberly, WEB.ProductCatalogPimberlyStage |
| WEB | [spMergeProductCatalogStorefrontCategory](WEB.spMergeProductCatalogStorefrontCategory.md) | WEB.ProductCatalogStorefrontCategory, WEB.ProductCatalogStorefrontCategoryArchive, WEB.ProductCatalogStorefrontCategoryStage |
| WEB | [spMergeProductStorefrontCategoryMap](WEB.spMergeProductStorefrontCategoryMap.md) | WEB.ProductStorefrontCategoryMap, WEB.ProductStorefrontCategoryMapArchive, WEB.ProductStorefrontCategoryMapStage |
| WEB | [spMergeUKWebProductBalance](WEB.spMergeUKWebProductBalance.md) | WEB.UKWebstoreProductBalance, WEB.UKWebstoreProductBalanceStage |
| WEB | [spMergeUKWebProductBalance_BAK20230822](WEB.spMergeUKWebProductBalance_BAK20230822.md) | WEB.UKWebstoreProductBalance, WEB.UKWebstoreProductBalanceStage |
| WEB | [spOutputMasterCatalog](WEB.spOutputMasterCatalog.md) | WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterCategory, WEB.ProductCatalogMasterCategoryArchive, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive, WEB.spOutputXMLFile |
| WEB | [spOutputPricebooks](WEB.spOutputPricebooks.md) | web.PricebookBundleSkuFact, web.PricebookFact, WEB.spOutputXMLFile |
| WEB | [spOutputPricebooks_Bak20220705](WEB.spOutputPricebooks_Bak20220705.md) | WEB.spOutputXMLFile |
| WEB | [spOutputPricebooks_BAK20240806](WEB.spOutputPricebooks_BAK20240806.md) | web.PricebookFact, WEB.spOutputXMLFile |
| WEB | [spOutputPricebooks_FULL](WEB.spOutputPricebooks_FULL.md) | web.PricebookFact, WEB.spOutputXMLFile |
| WEB | [spRunWEBPricebookExports](WEB.spRunWEBPricebookExports.md) | catalog.create_execution, catalog.set_execution_parameter_value, dbo.sp_start_job, dbo.sysjobactivity, dbo.sysjobs_view |
| WEB | [spSelectProductCatalogMasterAttributes](WEB.spSelectProductCatalogMasterAttributes.md) | WEB.ProductCatalogMasterAttributesPreStage, Web.RetiredMerchAttributeArchive, WEB.WebIncludedStyles, WEB.WebStyleAttributes, WMS.vwWarehouseOnOrder |
| WEB | [spUpdateProductMasterCatalogOnlineFlag](WEB.spUpdateProductMasterCatalogOnlineFlag.md) | WEB.ProductCatalogMasterAttributesStage, WEB.ProductCatalogMasterDataExceptions |
| WM | [PrintFiles](WM.PrintFiles.md) |  |
| WMS | [spCreateFileWMSPurchaseOrderReceipts](WMS.spCreateFileWMSPurchaseOrderReceipts.md) | WMS.PurchaseOrderReceipt |
| WMS | [spEmailAptosDistributionExportValidation](WMS.spEmailAptosDistributionExportValidation.md) | dbo.sp_send_dbmail, wms.DynamicsAPILog, WMS.DynamicsPackageAPILog, WMS.StoreShipmentExport, WMS.ValidationAptosDistroAfterSplit, WMS.ValidationAptosStoreShipmentExport |
| WMS | [spEmailAptosPONotInTPM](WMS.spEmailAptosPONotInTPM.md) | dbo.sp_send_dbmail, WMS.ValidationStage_AptosPONotInTPM |
| WMS | [spEmailASNExportSummary](WMS.spEmailASNExportSummary.md) | dbo.sp_send_dbmail, WMS.ASN_TPMToDynamics, wms.ASNDuds, WMS.DynamicsAPILog |
| WMS | [spEmailCostcoInventory](WMS.spEmailCostcoInventory.md) | dbo.sp_send_dbmail, WMS.WarehouseOnHand |
| WMS | [spEmailCostcoPOExport](WMS.spEmailCostcoPOExport.md) | dbo.sp_send_dbmail, dbo.vwCostcoAPIResponse |
| WMS | [spEmailCostcoTrackingUpdateGiftcardDB](WMS.spEmailCostcoTrackingUpdateGiftcardDB.md) | dbo.po, dbo.PurchaseOrder, dbo.PurchaseOrderStatus, dbo.sp_send_dbmail, dbo.Status, WMS.vwCostcoOrdersShipped |
| WMS | [spEmailDistrosVsShipmentsValidation](WMS.spEmailDistrosVsShipmentsValidation.md) | dbo.sp_send_dbmail, WMS.AptosDistrosWithoutShipments |
| WMS | [spEmailFedExTracking](WMS.spEmailFedExTracking.md) | dbo.sp_send_dbmail, wms.ItemMasterProducts, wms.ItemsUOM, wms.ShipmentConfirmAptos |
| WMS | [spEmailPOExportSummary](WMS.spEmailPOExportSummary.md) | dbo.sp_send_dbmail, erp.VendorMaster, WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics, WMS.ValidateAptosPOtoStage, wms.vwValidatePOAptosToDynamics |
| WMS | [spEmailPOExportSummaryBAK20220801](WMS.spEmailPOExportSummaryBAK20220801.md) | dbo.sp_send_dbmail, erp.VendorMaster, WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics, WMS.ValidateAptosPOtoStage, wms.vwValidatePOAptosToDynamics |
| WMS | [spEmailTransferOrderSalesOrderExport](WMS.spEmailTransferOrderSalesOrderExport.md) | dbo.sp_send_dbmail, wms.DynamicsAPILog, WMS.ItemMasterProducts, WMS.StoreShipmentExport |
| WMS | [spEmailUKpartnerOperatedTransferOrder](WMS.spEmailUKpartnerOperatedTransferOrder.md) | dbo.Dynamics_EcoResProduct, dbo.Dynamics_EcoResProductTranslation, dbo.Dynamics_inventtransferline, dbo.Dynamics_inventtransfertable, dbo.sp_send_dbmail, dbo.tmpUKpartnerOperatedTransferOrder |
| WMS | [spEmailVendorsWithSameVendorFactory](WMS.spEmailVendorsWithSameVendorFactory.md) | dbo.sp_send_dbmail, erp.VendorMaster |
| WMS | [spFTPCNDistros](WMS.spFTPCNDistros.md) | dbo.ftpPUT_Distro, dbo.sp_send_dbmail |
| WMS | [spFTPUKDistros](WMS.spFTPUKDistros.md) | dbo.SFTP_upload_UK_Distro, dbo.sp_send_dbmail |
| WMS | [spFTPWCDistros](WMS.spFTPWCDistros.md) | dbo.ftpPUT_WCDistro, dbo.sp_send_dbmail |
| WMS | [spInsertDynamicsAPILog](WMS.spInsertDynamicsAPILog.md) | WMS.DynamicsAPILog |
| WMS | [spMerchandisingFtpCN_GetInvAdjFiles](WMS.spMerchandisingFtpCN_GetInvAdjFiles.md) | dbo.ftpCN_GETInvAdj, dbo.ftpCN_GETInvAdjDIR, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFtpCN_GetInventoryFiles](WMS.spMerchandisingFtpCN_GetInventoryFiles.md) | dbo.ftpCN_GETInventory, dbo.ftpCN_GETInventoryDIR, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFtpCN_GetPoReceiptFiles](WMS.spMerchandisingFtpCN_GetPoReceiptFiles.md) | dbo.ftpCN_GETReceipts, dbo.ftpCN_GETReceiptsDIR, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFtpCN_GetShipmentFiles](WMS.spMerchandisingFtpCN_GetShipmentFiles.md) | dbo.ftpCN_GETShipments, dbo.ftpCN_GETShipmentsDIR, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFtpCNDistro](WMS.spMerchandisingFtpCNDistro.md) | dbo.ftpPUT_Distro, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFTPgetDDCAdjustmentsWinSCP](WMS.spMerchandisingFTPgetDDCAdjustmentsWinSCP.md) | dbo.ftpWC_GETInvAdj, dbo.ftpWC_GETInvAdjDIR, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFTPgetDDCinventoryWinSCP](WMS.spMerchandisingFTPgetDDCinventoryWinSCP.md) | dbo.ftpWC_GETInventory, dbo.ftpWC_GETInventoryDIR, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFTPgetDDCreceiptsWinSCP](WMS.spMerchandisingFTPgetDDCreceiptsWinSCP.md) | dbo.ftpWC_GETReceipts, dbo.ftpWC_GETReceiptsDIR, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFTPgetDDCshipmentsWinSCP](WMS.spMerchandisingFTPgetDDCshipmentsWinSCP.md) | dbo.ftpWC_GETShipments, dbo.ftpWC_GETShipmentsDIR, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFTPgetUKfiles_Web_WinSCP](WMS.spMerchandisingFTPgetUKfiles_Web_WinSCP.md) | dbo.sftpGETLogUKWhseWeb, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFTPgetUKfiles_WinSCP](WMS.spMerchandisingFTPgetUKfiles_WinSCP.md) | dbo.sftpGETLogUKWhse, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFTPUKDistro_WinSCP](WMS.spMerchandisingFTPUKDistro_WinSCP.md) | dbo.SFTP_upload_UK_Distro, dbo.sp_send_dbmail |
| WMS | [spMerchandisingFtpWCDistroWinSCP](WMS.spMerchandisingFtpWCDistroWinSCP.md) | dbo.ftpPUT_WCDistro, dbo.sp_send_dbmail |
| WMS | [spMerchandisingProcessCNStoreShipments](WMS.spMerchandisingProcessCNStoreShipments.md) | WMS.ERP_DynamicsShipmentStage_CN |
| WMS | [spMerchandisingProcessUKStoreShipments](WMS.spMerchandisingProcessUKStoreShipments.md) | WMS.ERP_DynamicsShipmentStage_UK |
| WMS | [spMerchandisingProcessWCStoreShipments](WMS.spMerchandisingProcessWCStoreShipments.md) | wms.ERP_DynamicsShipmentStage_WC |
| WMS | [spMerchandisingReportStoreShipmentExportConfirmationUK](WMS.spMerchandisingReportStoreShipmentExportConfirmationUK.md) | dbo.sp_send_dbmail, dbo.ukExport, wms.DynamicsTo3PLOrderExport |
| WMS | [spMerchandisingReportStoreShipmentExportConfirmationWC](WMS.spMerchandisingReportStoreShipmentExportConfirmationWC.md) | dbo.sp_send_dbmail, dbo.WCExport, wms.DynamicsTo3PLOrderExport |
| WMS | [spMergeAgedWebOrdersInDynamics](WMS.spMergeAgedWebOrdersInDynamics.md) | WMS.AgedWebOrdersInDynamics, WMS.AgedWebOrdersInDynamicsStage |
| WMS | [spMergeAgedWebOrdersInDynamicsbackup20230906](WMS.spMergeAgedWebOrdersInDynamicsbackup20230906.md) | WMS.AgedWebOrdersInDynamics, WMS.AgedWebOrdersInDynamicsStage |
| WMS | [spMergeASN_TPMToDynamics](WMS.spMergeASN_TPMToDynamics.md) | WMS.ASN_TPMToDynamics, WMS.ASN_TPMToDynamicsStage |
| WMS | [spMergeASN_TPMToDynamics_Bak20231208](WMS.spMergeASN_TPMToDynamics_Bak20231208.md) | WMS.ASN_TPMToDynamics, WMS.ASN_TPMToDynamicsStage |
| WMS | [spMergeASNCreateConfirmation](WMS.spMergeASNCreateConfirmation.md) | WMS.ASN_CreateConfirmation, WMS.ASN_CreateConfirmationStage |
| WMS | [spMergeASNCreateConfirmation_BAK20260512](WMS.spMergeASNCreateConfirmation_BAK20260512.md) | WMS.ASN_CreateConfirmation, WMS.ASN_CreateConfirmationStage |
| WMS | [spMergeASNCreateEmails](WMS.spMergeASNCreateEmails.md) | dbo.sp_send_dbmail, WMS.ASN_CreateConfirmation |
| WMS | [spMergeASNCreateEmails_BAK20260513](WMS.spMergeASNCreateEmails_BAK20260513.md) | dbo.sp_send_dbmail, WMS.ASN_CreateConfirmation |
| WMS | [spMergeCartonsCancelledToHA](WMS.spMergeCartonsCancelledToHA.md) | WMS.CartonsCancelledToHA, WMS.CartonsCancelledToHAStage |
| WMS | [spMergeCartonsCreatedToHA](WMS.spMergeCartonsCreatedToHA.md) | WMS.CartonsCreatedToHA, WMS.CartonsCreatedToHAStage |
| WMS | [spMergeCartonsSummaryToHA](WMS.spMergeCartonsSummaryToHA.md) | WMS.CartonsSummaryToHA, wms.CartonsSummaryToHAStage |
| WMS | [spMergeDBSchenkerFullInGateFile](WMS.spMergeDBSchenkerFullInGateFile.md) | WMS.DBSchenkerFullInGateFile, WMS.DBSchenkerFullInGateFileStage |
| WMS | [spMergeDuplicateWebOrderDetection](WMS.spMergeDuplicateWebOrderDetection.md) | WMS.DuplicateWebOrderDetection, WMS.DuplicateWebOrderDetectionStage |
| WMS | [spMergeDynamicsAverageCost](WMS.spMergeDynamicsAverageCost.md) | WMS.DynamicsAverageCost, WMS.DynamicsAverageCostStage |
| WMS | [spMergeDynamicsContainer](WMS.spMergeDynamicsContainer.md) | WMS.DynamicsContainer, WMS.DynamicsContainerStage |
| WMS | [spMergeDynamicsTo3PLOrderExport](WMS.spMergeDynamicsTo3PLOrderExport.md) | dbo.store_shipment_export, wms.DynamicsTo3PLOrderExport, WMS.fnDynanmicsTo3plOrderExportSource |
| WMS | [spMergeDynamicsWMSInventory](WMS.spMergeDynamicsWMSInventory.md) | dbo.DynamicsWMSInventoryStage, WMS.DynamicsWMSInventory |
| WMS | [spMergeDynamicsWMSNonWhseInventory](WMS.spMergeDynamicsWMSNonWhseInventory.md) | dbo.DynamicsWMSNonWhseInventoryStage, WMS.DynamicsWMSNonWhseInventory |
| WMS | [spMergeERDMatrix](WMS.spMergeERDMatrix.md) | WMS.ERDMatrix, WMS.ERDMatrixStage |
| WMS | [spMergeInboundShipmentLoad](WMS.spMergeInboundShipmentLoad.md) | WMS.InboundShipmentLoad, wms.InboundShipmentLoadStage |
| WMS | [spMergeInboundShipmentLoad_Bak20231030](WMS.spMergeInboundShipmentLoad_Bak20231030.md) | WMS.InboundShipmentLoad, wms.InboundShipmentLoadStage |
| WMS | [spMergeInventoryAdjustments](WMS.spMergeInventoryAdjustments.md) | WMS.InventoryAdjustments, WMS.InventoryAdjustmentsStage |
| WMS | [spMergeInventorySync](WMS.spMergeInventorySync.md) | WMS.InventorySync, WMS.InventorySyncStage |
| WMS | [spMergeItemCasePack](WMS.spMergeItemCasePack.md) | WMS.ItemCasePack, WMS.vwItemCasePackSrc |
| WMS | [spMergeItemMaster](WMS.spMergeItemMaster.md) | WMS.ItemMaster, WMS.ItemMasterStage |
| WMS | [spMergeItemMasterProducts](WMS.spMergeItemMasterProducts.md) | WMS.ItemMasterProducts, WMS.ItemMasterProductsStage |
| WMS | [spMergeItemMasterProducts_BAK20221107](WMS.spMergeItemMasterProducts_BAK20221107.md) | WMS.ItemMasterProducts, WMS.ItemMasterProductsStage |
| WMS | [spMergeItemMasterProductsXtra](WMS.spMergeItemMasterProductsXtra.md) | WMS.ItemMasterProductsXtra, WMS.ItemMasterProductsXtraStage |
| WMS | [spMergeItemMasterXtra](WMS.spMergeItemMasterXtra.md) | WMS.ItemMasterXtra, WMS.ItemMasterXtraStage |
| WMS | [spMergeItemsNMFC](WMS.spMergeItemsNMFC.md) | WMS.ItemsNMFC, WMS.ItemsNMFCStage |
| WMS | [spMergeItemsUOM](WMS.spMergeItemsUOM.md) | WMS.ItemsUOM, WMS.ItemsUOMStage |
| WMS | [spMergeItemsUOMXtra](WMS.spMergeItemsUOMXtra.md) | WMS.ItemsUOM, WMS.ItemsUOMStage |
| WMS | [spMergeNonWarehouseOnHand](WMS.spMergeNonWarehouseOnHand.md) | WMS.NonWarehouseOnHand, wms.NonWarehouseOnHandStage |
| WMS | [spMergePartyHeader](WMS.spMergePartyHeader.md) | WMS.PartyHeader, WMS.PartyHeaderStage |
| WMS | [spMergePartyHeaderAPI](WMS.spMergePartyHeaderAPI.md) | WMS.PartyHeader, WMS.vwPartyAPIResponse |
| WMS | [spMergePartyLines](WMS.spMergePartyLines.md) | WMS.PartyLines, WMS.PartyLinesStage |
| WMS | [spMergePurchaseOrderMerchToDynamics](WMS.spMergePurchaseOrderMerchToDynamics.md) | wms.PurchaseOrderMerchToDynamics, wms.PurchaseOrderMerchToDynamicsStage |
| WMS | [spMergePurchaseOrderReceipt](WMS.spMergePurchaseOrderReceipt.md) | WMS.PurchaseOrderReceipt, WMS.PurchaseOrderReceiptStage |
| WMS | [spMergePurchaseOrderReceiptFromDynamicsReceiptHeaderAndLine](WMS.spMergePurchaseOrderReceiptFromDynamicsReceiptHeaderAndLine.md) | erp.vwWarehouseIDToLocationCode, WMS.PurchaseOrderReceipt, wms.vwDynamicsPurchaseOrderReceipts |
| WMS | [spMergePurchaseOrderReceiptFromDynamicsReceiptHeaderAndLineBAK20220801](WMS.spMergePurchaseOrderReceiptFromDynamicsReceiptHeaderAndLineBAK20220801.md) | erp.vwWarehouseIDToLocationCode, WMS.PurchaseOrderReceipt, wms.vwDynamicsPurchaseOrderReceipts |
| WMS | [spMergeReleasedProducts](WMS.spMergeReleasedProducts.md) | WMS.ReleasedProducts, WMS.ReleasedProductsStage |
| WMS | [spMergeRetailStore](WMS.spMergeRetailStore.md) | WMS.RetailStore, WMS.RetailStoreStage |
| WMS | [spMergeRetailStoreTenderType](WMS.spMergeRetailStoreTenderType.md) | WMS.RetailStoreTenderType, WMS.RetailStoreTenderTypeStage |
| WMS | [spMergeRetailTenderType](WMS.spMergeRetailTenderType.md) | WMS.RetailTenderType, WMS.RetailTenderTypeStage |
| WMS | [spMergeRetailTenderTypeCard](WMS.spMergeRetailTenderTypeCard.md) | WMS.RetailTenderTypeCard, WMS.RetailTenderTypeCardStage |
| WMS | [spMergeShipConfirmDBSchenker](WMS.spMergeShipConfirmDBSchenker.md) | WMS.ShipConfirmDBSchenker, WMS.ShipConfirmDBSchenkerStage |
| WMS | [spMergeShipmentConfirmAptos](WMS.spMergeShipmentConfirmAptos.md) | WMS.ShipmentConfirmAptos, WMS.ShipmentConfirmAptosStage |
| WMS | [spMergeShipmentInvoiceFromPOReceipt](WMS.spMergeShipmentInvoiceFromPOReceipt.md) | ERP.ShipmentInvoice, erp.VendorMaster, WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics, WMS.PurchaseOrderReceipt |
| WMS | [spMergeStoreShipmentExport](WMS.spMergeStoreShipmentExport.md) | WMS.StoreShipmentExport, WMS.StoreShipmentExportStage |
| WMS | [spMergeStoreShipmentExport_BAK20220801](WMS.spMergeStoreShipmentExport_BAK20220801.md) | WMS.StoreShipmentExport, WMS.StoreShipmentExportStage |
| WMS | [spMergeStoreShipmentExportParty](WMS.spMergeStoreShipmentExportParty.md) | WMS.PartyToDynamics, WMS.StoreShipmentExport |
| WMS | [spMergeStoreToStoreTransferLicensePlate](WMS.spMergeStoreToStoreTransferLicensePlate.md) | WMS.StoreToStoreTransferLicensePlate, wms.StoreToStoreTransferLicensePlateStage, wms.StoreToStoreTransferMessage |
| WMS | [spMergeStoreToStoreTransferMessage](WMS.spMergeStoreToStoreTransferMessage.md) | WMS.StoreToStoreTransferMessage, WMS.StoreToStoreTransferMessageStage |
| WMS | [spMergeStoreTransferOrderReceipt](WMS.spMergeStoreTransferOrderReceipt.md) | wms.InboundShipmentLoad, WMS.StoreTransferOrderReceipt, wms.StoreTransferOrderReceiptStage |
| WMS | [spMergeStoreTransferOrderReceipt_Bak20230926](WMS.spMergeStoreTransferOrderReceipt_Bak20230926.md) | WMS.StoreTransferOrderReceipt, WMS.StoreTransferOrderReceiptStage |
| WMS | [spMergeStoreTransferOrderReceipt_BAK20231011](WMS.spMergeStoreTransferOrderReceipt_BAK20231011.md) | wms.InboundShipmentLoad, WMS.StoreTransferOrderReceipt, wms.StoreTransferOrderReceiptStage |
| WMS | [spMergeTrueCommercePostWaveData](WMS.spMergeTrueCommercePostWaveData.md) | wms.TrueCommercePostWaveData, wms.TrueCommercePostWaveDataStage |
| WMS | [spMergeTrueCommerceShipmentData](WMS.spMergeTrueCommerceShipmentData.md) | wms.TrueCommerceShipmentData, wms.TrueCommerceShipmentDataStage |
| WMS | [spMergeVendorMasterTo3PL](WMS.spMergeVendorMasterTo3PL.md) | WMS.VendorMasterTo3PL, WMS.VendorMasterTo3PLStage |
| WMS | [spMergeWarehouseOnHand](WMS.spMergeWarehouseOnHand.md) | dbo.sp_send_dbmail, WMS.WarehouseOnHand, wms.WarehouseOnHandStage |
| WMS | [spMergeWarehouseOnHand9980](WMS.spMergeWarehouseOnHand9980.md) | WMS.WarehouseOnHand9980, wms.WarehouseOnHand9980Stage |
| WMS | [spOutputDynamicsDistroFilesCN](WMS.spOutputDynamicsDistroFilesCN.md) | dbo.d, WMS.DynamicsTo3PLOrderExport |
| WMS | [spOutputDynamicsDistroFilesCN_BAK20220804](WMS.spOutputDynamicsDistroFilesCN_BAK20220804.md) | WMS.DynamicsTo3PLOrderExport |
| WMS | [spOutputDynamicsDistroFilesCN_BAK20220825](WMS.spOutputDynamicsDistroFilesCN_BAK20220825.md) | dbo.d, WMS.DynamicsTo3PLOrderExport |
| WMS | [spOutputDynamicsDistroFilesUK](WMS.spOutputDynamicsDistroFilesUK.md) | dbo.d, WMS.DynamicsTo3PLOrderExport |
| WMS | [spOutputDynamicsDistroFilesUK_BAK20220825](WMS.spOutputDynamicsDistroFilesUK_BAK20220825.md) | dbo.d, WMS.DynamicsTo3PLOrderExport |
| WMS | [spOutputDynamicsDistroFilesWC](WMS.spOutputDynamicsDistroFilesWC.md) | dbo.d, WMS.DynamicsTo3PLOrderExport |
| WMS | [spOutputDynamicsDistroFilesWC_BAK20220825](WMS.spOutputDynamicsDistroFilesWC_BAK20220825.md) | dbo.d, WMS.DynamicsTo3PLOrderExport |
| WMS | [spOutputPurchaseOrderReceiptDBStoDynamics1200XML](WMS.spOutputPurchaseOrderReceiptDBStoDynamics1200XML.md) | ERP.spOutputXMLFile, WMS.DBSchenkerFullInGateFile, WMS.vwDynamicsPOReceiptFromDBSchenkerASN |
| WMS | [spOutputShipmentInvoiceFromWMSPOReceipt](WMS.spOutputShipmentInvoiceFromWMSPOReceipt.md) | WEB.spOutputXMLFile, WMS.PurchaseOrderReceipt, WMS.vwShipmentInvoice1200FromWMPOReceipt |
| WMS | [spOutputWMSAllocAdj](WMS.spOutputWMSAllocAdj.md) | dbo.tmpAllocationsAdjWMS |
| WMS | [spOutputWMSShipment](WMS.spOutputWMSShipment.md) | WMS.tmpWMSShipmentImport |
| WMS | [spPartyStageForDynamics](WMS.spPartyStageForDynamics.md) | ERP.vwWarehouseIDToLocationCode, ERP.WarehouseMaster, WMS.PartyHeader, WMS.PartyLines, WMS.PartyToDynamics, WMS.vwDistributionRecTypeByCountryForLookup |
| WMS | [spPrintInventoryAdjustments](WMS.spPrintInventoryAdjustments.md) | WMS.InventoryAdjustments |
| WMS | [spProcessShipmentAllocationAdjPipelineData](WMS.spProcessShipmentAllocationAdjPipelineData.md) | dbo.s, ERP.DistributionRecType, ERP.vwWarehouseIDToLocationCode, WMS.ERDMatrix, wms.ItemsUOM, wms.ShipmentConfirmAptos, wms.StoreShipmentExport, WMS.tmpWMSShipmentImport |
| WMS | [spQueryItemCreateEcoResProductCategoryAssignmentXML](WMS.spQueryItemCreateEcoResProductCategoryAssignmentXML.md) | dbo.tmpPreStage, ERP.ItemLoadtoD365 |
| WMS | [spQueryItemCreateEcoResProductSpecificUOMXML](WMS.spQueryItemCreateEcoResProductSpecificUOMXML.md) | ERP.ItemLoadtoD365, WMS.ItemUOMStageForDynamics |
| WMS | [spQueryItemCreateEcoResProductV2XML](WMS.spQueryItemCreateEcoResProductV2XML.md) | dbo.tmpPrestage, ERP.ItemLoadtoD365 |
| WMS | [spQueryItemCreateEcoResReleasedProductV2XML](WMS.spQueryItemCreateEcoResReleasedProductV2XML.md) | dbo.tmpPrestage, ERP.ItemLoadtoD365 |
| WMS | [spQueryItemCreatePreStage](WMS.spQueryItemCreatePreStage.md) | ERP.ItemLoadtoD365, wms.ItemMaster, wms.ItemMasterProducts |
| WMS | [spQueryItemCreateVendorProdDescXML](WMS.spQueryItemCreateVendorProdDescXML.md) | dbo.tmpPreStage, ERP.ItemLoadtoD365, ERP.ItemVendorLoadtoD365 |
| WMS | [spQueryItemCreateVendorXML](WMS.spQueryItemCreateVendorXML.md) | dbo.tmpPreStage, ERP.ItemLoadtoD365, ERP.ItemVendorLoadtoD365 |
| WMS | [spQueryItemCreateXMLBAK20230327](WMS.spQueryItemCreateXMLBAK20230327.md) | ERP.ItemLoadtoD365, wms.ItemMaster, wms.ItemMasterProducts, WMS.ItemUOMStageForDynamics |
| WMS | [spQueryItemCreateXMLBAK20231113](WMS.spQueryItemCreateXMLBAK20231113.md) | ERP.ItemLoadtoD365, wms.ItemMaster, wms.ItemMasterProducts, WMS.ItemUOMStageForDynamics |
| WMS | [spQueryItemCreateXMLPreRetailInventory20221027](WMS.spQueryItemCreateXMLPreRetailInventory20221027.md) | ERP.ItemLoadtoD365, wms.ItemMaster, wms.ItemMasterProducts, WMS.ItemUOMStageForDynamics |
| WMS | [spQueryItemUPCXML](WMS.spQueryItemUPCXML.md) | erp.ItemLoadtoD365 |
| WMS | [spReportBearhouseWebStoreInvoiceUpdate](WMS.spReportBearhouseWebStoreInvoiceUpdate.md) | wms.ModeOfDeliveryWeb, wms.SalesOrderStatusUpdateShipped, WMS.WebOrdersInvoicedToday |
| WMS | [spReportDynamicsNonAptosPOReceipts](WMS.spReportDynamicsNonAptosPOReceipts.md) | wms.vwDynamicsPurchaseOrderReceipts_NonAptos |
| WMS | [spReportStoreShipToDynamicsTOCheck](WMS.spReportStoreShipToDynamicsTOCheck.md) | dbo.sp_send_dbmail, WMS.vwStoreShipmentsToDynamicsTOCheck |
| WMS | [spReportTPMtoD365errors](WMS.spReportTPMtoD365errors.md) | wms.ASN_CreateConfirmation, WMS.ASN_TPMToDynamics, WMS.DynamicsAPILog |
| WMS | [spReportWebOrderMakeup](WMS.spReportWebOrderMakeup.md) | dbo.sp_send_dbmail, pos.ProductCatalogMasterAttributesStage, Web.ProductCatalogMasterAttributesStage, WMS.SalesOrderStatusUpdateShipped |
| WMS | [spReportWebSalesOrdersAging](WMS.spReportWebSalesOrdersAging.md) | WMS.AgedWebOrdersInDynamics |
| WMS | [spReportWebSalesOrdersAging_v2](WMS.spReportWebSalesOrdersAging_v2.md) | WMS.AgedWebOrdersInDynamics |
| WMS | [spReportWMSPOReceiptVsAptosPOReceipt](WMS.spReportWMSPOReceiptVsAptosPOReceipt.md) | dbo.location, dbo.po, dbo.po_receipt, dbo.po_receipt_detail, dbo.style, WMS.vwDynamicsPurchaseOrderReceipts |
| WMS | [spRetryReleasedOutOfOrderWaves](WMS.spRetryReleasedOutOfOrderWaves.md) | WM.WaveJob, WMS.SalesOrderStatusUpdateWaved, WMS.SalesOrderStatusUpdateWavedRetryLog |
| WMS | [spSelectInventoryAdjustments](WMS.spSelectInventoryAdjustments.md) | WMS.InventoryAdjustments |
| WMS | [spSelectWMSPurchaseOrderReceipts](WMS.spSelectWMSPurchaseOrderReceipts.md) | WMS.PurchaseOrderReceipt |
| WMS | [spSelectWMSPurchaseOrderReceiptsBACKUP20210628](WMS.spSelectWMSPurchaseOrderReceiptsBACKUP20210628.md) | WMS.PurchaseOrderReceipt |
| WMS | [spSelectWMSPurchaseOrderReceiptsBAK20220525](WMS.spSelectWMSPurchaseOrderReceiptsBAK20220525.md) | WMS.PurchaseOrderReceipt |
| WMS | [spSelectWMSPurchaseOrderReceiptsWIP20220525](WMS.spSelectWMSPurchaseOrderReceiptsWIP20220525.md) | WMS.PurchaseOrderReceipt |
| WMS | [spShippedNotReceivedDetailReport](WMS.spShippedNotReceivedDetailReport.md) | WMS.ShippedNotReceivedDetail |
| WMS | [spShippedNotReceivedReport](WMS.spShippedNotReceivedReport.md) | WMS.ShippedNotReceived |
| WMS | [spShippedNotReceivedReportDetailPrep](WMS.spShippedNotReceivedReportDetailPrep.md) | dbo.BEARITORY_DIM, dbo.CNTCT_DIM, dbo.Dynamics_EcoResProduct, dbo.Dynamics_EcoResProductTranslation, dbo.dynamics_inventtransferline, dbo.dynamics_inventtransfertable, dbo.dynamics_purchline, dbo.dynamics_purchtable, dbo.dynamics_salestable, dbo.STR_DIM, WMS.ShippedNotReceivedDetail |
| WMS | [spShippedNotReceivedReportDistricts](WMS.spShippedNotReceivedReportDistricts.md) | dbo.BEARITORY_RGN_DIM, dbo.CNTCT_DIM, dbo.RGN_BEARRNG_DIM, dbo.STR_DIM |
| WMS | [spShippedNotReceivedReportPrep](WMS.spShippedNotReceivedReportPrep.md) | dbo.BEARITORY_DIM, dbo.CNTCT_DIM, dbo.dynamics_inventtransferline, dbo.dynamics_inventtransfertable, dbo.dynamics_purchline, dbo.dynamics_purchtable, dbo.dynamics_salestable, dbo.STR_DIM, WMS.ShippedNotReceived |
| WMS | [spShippedNotReceivedStoreReportPrep](WMS.spShippedNotReceivedStoreReportPrep.md) | dbo.Dynamics_EcoResProduct, dbo.Dynamics_EcoResProductTranslation, dbo.Dynamics_UnitOfMeasureProducts, dbo.dynamics_whsasnitem, dbo.dynamics_whsloadline, dbo.Dynamics_WHSOutboundSortPositionTrans, dbo.Dynamics_WHSShipmentTable, dbo.dynamics_whsuomstructure, dbo.dynamics_whsworktable, dbo.productcatalogmasterattributesstage, dbo.tmpShippedNotReceivedStage, WMS.ShippedNotReceived_StoreReportStage |
| WMS | [spStoreShipmentReport](WMS.spStoreShipmentReport.md) | wms.InboundShipmentLoad, wms.ItemsUOM, wms.ShipmentConfirmAptos, wms.StoreTransferOrderReceipt, WMS.vwStoreShipmentReportLookupUOM, WMS.vwStoreShipmentReportStyles |
| WMS | [spStoreShipmentReport_Last24hourSnapshot](WMS.spStoreShipmentReport_Last24hourSnapshot.md) | wms.InboundShipmentLoad, wms.ItemsUOM, wms.ShipmentConfirmAptos, wms.StoreTransferOrderReceipt, WMS.vwStoreShipmentReportLookupUOM, WMS.vwStoreShipmentReportStyles |
| WMS | [spStoreShipmentReportD365](WMS.spStoreShipmentReportD365.md) | WMS.ShippedNotReceived_StoreReportStage |
| WMS | [spStoreShipmentReportD365_Last24hourSnapshot](WMS.spStoreShipmentReportD365_Last24hourSnapshot.md) | WMS.ShippedNotReceived_StoreReportStage |
| WMS | [spStoreShipmentReportTotals](WMS.spStoreShipmentReportTotals.md) | Azure.vwProducts, WMS.InboundShipmentLoad, wms.ItemsUOM, wms.ShipmentConfirmAptos, wms.StoreTransferOrderReceipt, wms.StoreTransferOrderReceiptStage |
| WMS | [spStoreShipmentReportTotalsD365](WMS.spStoreShipmentReportTotalsD365.md) | WMS.ShippedNotReceived_StoreReportStage |
| WMS | [spStoreShipmentReportTotalsD365_Last24hourSnapshot](WMS.spStoreShipmentReportTotalsD365_Last24hourSnapshot.md) | WMS.ShippedNotReceived_StoreReportStage |
| WMS | [spStoreShipmentReportTotalsV2](WMS.spStoreShipmentReportTotalsV2.md) | WMS.InboundShipmentLoad, wms.ItemsUOM, wms.ShipmentConfirmAptos, wms.StoreTransferOrderReceipt, WMS.vwStoreShipmentReportStyles |
| WMS | [spStoreShipmentReportTotalsV2_Last24hourSnapshot](WMS.spStoreShipmentReportTotalsV2_Last24hourSnapshot.md) | WMS.InboundShipmentLoad, wms.ItemsUOM, wms.ShipmentConfirmAptos, wms.StoreTransferOrderReceipt, WMS.vwStoreShipmentReportStyles |
| WMS | [spUpdateReleaseDateAndTime](WMS.spUpdateReleaseDateAndTime.md) | dbo.w2, WM.WaveJob, WMS.eCommWaveStatus, WMS.SalesOrderStatusUpdateWaved |
| WMS | [spWMPrintDBSchenkerShipments](WMS.spWMPrintDBSchenkerShipments.md) | dbo.sp_send_dbmail, WMS.ShipConfirmDBSchenker |
| WMS | [spWMSelectDBSchenkerShipments](WMS.spWMSelectDBSchenkerShipments.md) | dbo.tmpDBS, WMS.ShipConfirmDBSchenker |
