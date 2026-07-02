# Stored Procedures: WebOrderProcessing

| Schema | Name | Table Dependencies |
|---|---|---|
| ComHub | [spGenerateCommHubCostcoConfirmations](ComHub.spGenerateCommHubCostcoConfirmations.md) | ComHub.POWebOrder, ComHub.POWebOrderStatus, ComHub.Status, ComHub.tmpCostcoConfirmation, ComHub.vwPOWebOrderCurrentStatus, ComHub.xmlFile, dbo.xp_cmdshell, WM.Orders |
| ComHub | [spGenerateCommHubCostcoFAs](ComHub.spGenerateCommHubCostcoFAs.md) | ComHub.POWebOrder, ComHub.POWebOrderStatus, ComHub.Status, ComHub.tmpCostcoFA, ComHub.vwPOWebOrderCurrentStatus, ComHub.xmlFile, dbo.xp_cmdshell |
| ComHub | [spUpdatePOWebOrdersAcknowledged](ComHub.spUpdatePOWebOrdersAcknowledged.md) | ComHub.ComhubFTPLog, ComHub.POWebOrder, ComHub.POWebOrderStatus, ComHub.Status, ComHub.vwPOWebOrderCurrentStatus, ComHub.xmlFile |
| ComHub | [spUpdatePOWebOrdersFulFilled](ComHub.spUpdatePOWebOrdersFulFilled.md) | ComHub.ComhubFTPLog, ComHub.POWebOrder, ComHub.POWebOrderStatus, ComHub.Status, ComHub.vwPOWebOrderCurrentStatus, ComHub.xmlFile |
| dbo | [sp_alterdiagram](dbo.sp_alterdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_creatediagram](dbo.sp_creatediagram.md) | dbo.sysdiagrams |
| dbo | [sp_dropdiagram](dbo.sp_dropdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagramdefinition](dbo.sp_helpdiagramdefinition.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagrams](dbo.sp_helpdiagrams.md) | dbo.sysdiagrams |
| dbo | [sp_renamediagram](dbo.sp_renamediagram.md) | dbo.sysdiagrams |
| dbo | [sp_upgraddiagrams](dbo.sp_upgraddiagrams.md) | dbo.dtproperties, dbo.sysdiagrams |
| dbo | [spBabDynamics_MasterProcedure](dbo.spBabDynamics_MasterProcedure.md) | dbo.spBabDynamics0_BuildTargetTransactionsTable, dbo.spBabDynamics1_BuildDiscountStagingTable, dbo.spBabDynamics2_BuildHeaderStagingTable, dbo.spBabDynamics3_BuildSalesLineStagingTable, dbo.spBabDynamics4_BuildTaxStagingTable, dbo.spBabDynamics5_BuildTenderStagingTable, dbo.spBabDynamics6_BlankSoundChipInsert, dbo.spBabDynamics7_ShippingLineInserts |
| dbo | [spBabDynamics0_BuildTargetTransactionsTable](dbo.spBabDynamics0_BuildTargetTransactionsTable.md) | dbo.DynamicsTargetTransactions, wm.OMSTransactionDetails, wm.orders |
| dbo | [spBabDynamics1_BuildDiscountStagingTable](dbo.spBabDynamics1_BuildDiscountStagingTable.md) | dbo.DynamicsDiscountLineStage, dbo.DynamicsDiscountSumStage, dbo.DynamicsTargetTransactions, dbo.WebDemandOrderItemZ, dbo.WebDemandOrderz |
| dbo | [spBabDynamics1_BuildDiscountStagingTable_BAK20240617](dbo.spBabDynamics1_BuildDiscountStagingTable_BAK20240617.md) | dbo.DynamicsDiscountLineStage, dbo.DynamicsDiscountSumStage, dbo.WebDemandOrderItemZ |
| dbo | [spBabDynamics2_BuildHeaderStagingTable](dbo.spBabDynamics2_BuildHeaderStagingTable.md) | dbo.DynamicsDiscountSumStage, dbo.DynamicsHeaderStage, dbo.DynamicsTargetTransactions, dbo.WebDemandOrderItemZ, dbo.WebDemandOrderz |
| dbo | [spBabDynamics3_BuildSalesLineStagingTable](dbo.spBabDynamics3_BuildSalesLineStagingTable.md) | dbo.DynamicsDiscountLineStage, dbo.DynamicsDiscountSumStage, dbo.DynamicsSalesLineStage, dbo.DynamicsTargetTransactions, dbo.vwdynamics_serviceitemlookup, dbo.WebDemandOrderItemZ |
| dbo | [spBabDynamics4_BuildTaxStagingTable](dbo.spBabDynamics4_BuildTaxStagingTable.md) | dbo.DynamicsTargetTransactions, dbo.DynamicsTaxLineStage, dbo.WebDemandOrderItemZ |
| dbo | [spBabDynamics5_BuildTenderStagingTable](dbo.spBabDynamics5_BuildTenderStagingTable.md) | dbo.DynamicsHeaderStage, dbo.DynamicsTargetTransactions, dbo.DynamicsTenderLineStage, dbo.WebDemandOrderItemZ, wm.orders, WM.Payments |
| dbo | [spBabDynamics6_BlankSoundChipInsert](dbo.spBabDynamics6_BlankSoundChipInsert.md) | dbo.DynamicsSalesLineStage, dbo.DynamicsTaxLineStage, dbo.POSProducts |
| dbo | [spBabDynamics7_ShippingLineInserts](dbo.spBabDynamics7_ShippingLineInserts.md) | dbo.DynamicsDiscountLineStage, dbo.DynamicsSalesLineStage, dbo.DynamicsTargetTransactions, dbo.DynamicsTaxLineStage, dbo.WebDemandOrderz |
| dbo | [spDBA_WhoIsActive](dbo.spDBA_WhoIsActive.md) | agent_node.value, dbo.s, dbo.sysjobs, dbo.sysjobsteps, trans_node.value |
| dbo | [spMergePOSProducts](dbo.spMergePOSProducts.md) | dbo.POSProducts, POS.PBIProductCatalogMasterAttributesStage, POS.ProductCatalogMasterAttributesStage |
| dbo | [spMergeWebDemandOrderItemz](dbo.spMergeWebDemandOrderItemz.md) | dbo.WebDemandOrderItemsStage, dbo.WebDemandOrderItemz |
| dbo | [spMergeWebDemandOrderz](dbo.spMergeWebDemandOrderz.md) | dbo.WebDemandOrdersStage, dbo.WebDemandOrderz |
| dbo | [spStoreforceBopis](dbo.spStoreforceBopis.md) | dbo.date_dim, dbo.store_dim, dbo.time_dim, dbo.vwPOSActiveJumpMindStores, pos.ProductCatalogMasterAttributesStage, wm.OrderItems, wm.Orders, wm.OrderStatus |
| dbo | [spUpdateOrderItemsRecordYourVoiceNumber](dbo.spUpdateOrderItemsRecordYourVoiceNumber.md) | WM.OrderItems, WM.Orders |
| WM | [FlagCodosAndGiftBoxes](WM.FlagCodosAndGiftBoxes.md) | wm.OrderItems, wm.Orders, Wm.ProductCatalogMasterAttributes_Mirror |
| WM | [spEmailOrdersNotOnColumbusDB](WM.spEmailOrdersNotOnColumbusDB.md) | dbo.sp_send_dbmail, WM.OrdersNotOnColumbusDB |
| WM | [spEmailWebOrderProcessingSummary](WM.spEmailWebOrderProcessingSummary.md) | dbo.sp_send_dbmail |
| WM | [spEmailWebOrdersNotInSalesAudit](WM.spEmailWebOrdersNotInSalesAudit.md) | dbo.sp_send_dbmail, WM.OrdersNotInSalesAudit |
| WM | [spEmailWebOrdersNotShippedInOMS](WM.spEmailWebOrdersNotShippedInOMS.md) | dbo.sp_send_dbmail, WM.OrdersNotShippedInOMS |
| WM | [spEmailWebOrdersNotWavedInOMS](WM.spEmailWebOrdersNotWavedInOMS.md) | dbo.sp_send_dbmail, WM.OrdersNotWavedInOMS |
| WM | [spGetDonationInfo](WM.spGetDonationInfo.md) | WEB.ProductCatalogMasterAttributes |
| WM | [spGetESUpdateOrderStatus](WM.spGetESUpdateOrderStatus.md) | WM.Orders, WM.OrderStatus |
| WM | [spGetGiftCardInfo](WM.spGetGiftCardInfo.md) | WEB.ProductCatalogMasterAttributes |
| WM | [spGetPreviousWMOrderItemDiscounts](WM.spGetPreviousWMOrderItemDiscounts.md) | WM.ItemDiscounts, WM.ItemStatus, WM.OrderItems, WM.vwTransactionDetail |
| WM | [spGetPreviousWMOrderItemDiscounts_V2](WM.spGetPreviousWMOrderItemDiscounts_V2.md) | WM.ItemDiscounts, WM.vwDistinctItemStatuses, WM.vwDistinctOrderItems, WM.vwTransactionDetail_V2 |
| WM | [spGetPreviousWMOrderItemDiscounts_V3](WM.spGetPreviousWMOrderItemDiscounts_V3.md) | WM.ItemDiscounts, WM.ItemStatus, WM.OrderItems, WM.Orders, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetPreviousWMOrderItemDiscounts_V3_1](WM.spGetPreviousWMOrderItemDiscounts_V3_1.md) | WM.ItemDiscounts, WM.ItemStatus, WM.OrderItems, WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetReturnWMOrderPayments](WM.spGetReturnWMOrderPayments.md) | WM.Orders, WM.vwTransactionDetail, WM.vwTransactionDetailAll |
| WM | [spGetReturnWMOrderPayments_V2](WM.spGetReturnWMOrderPayments_V2.md) | WM.Orders, WM.vwTransactionDetailPayments, WM.vwTransactionDetailPayments_All_1_1 |
| WM | [spGetReturnWMOrderPayments_V3](WM.spGetReturnWMOrderPayments_V3.md) | WM.Orders, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetReturnWMOrderPayments_V3_1](WM.spGetReturnWMOrderPayments_V3_1.md) | WM.Orders, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetReturnWMOrderPayments_V3_1_BJB20210608](WM.spGetReturnWMOrderPayments_V3_1_BJB20210608.md) | WM.Orders, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetReturnWMOrderPayments_V3_2](WM.spGetReturnWMOrderPayments_V3_2.md) | WM.Orders, WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetReturnWMOrdersTaxes](WM.spGetReturnWMOrdersTaxes.md) | WM.vwSalesAuditTaxesForReturn, WM.vwTransactionDetail |
| WM | [spGetReturnWMOrdersTaxes_V2](WM.spGetReturnWMOrdersTaxes_V2.md) | WM.Transactions, WM.vwTransactionDetailPayments, WM.vwTransactionDetailPayments_All_1_1 |
| WM | [spGetReturnWMOrdersTaxes_V3](WM.spGetReturnWMOrdersTaxes_V3.md) | WM.OMSTransactionDetails, WM.Orders, WM.Transactions, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetReturnWMOrdersTaxes_V3_1](WM.spGetReturnWMOrdersTaxes_V3_1.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderBillTo](WM.spGetShippedWMOrderBillTo.md) | WM.vwTransactionDetail |
| WM | [spGetShippedWMOrderBillTo_V2](WM.spGetShippedWMOrderBillTo_V2.md) | WM.vwTransactionDetail_V2 |
| WM | [spGetShippedWMOrderBillTo_V3](WM.spGetShippedWMOrderBillTo_V3.md) | WM.vwOrderNumPickupStore, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderBillTo_V3_1](WM.spGetShippedWMOrderBillTo_V3_1.md) | WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderItemDiscounts](WM.spGetShippedWMOrderItemDiscounts.md) | WM.ItemDiscounts, WM.ItemStatus, WM.OrderItems, WM.vwTransactionDetail |
| WM | [spGetShippedWMOrderItemDiscounts_V2](WM.spGetShippedWMOrderItemDiscounts_V2.md) | WM.ItemDiscounts, WM.vwDistinctItemStatuses, WM.vwDistinctOrderItems, WM.vwTransactionDetail_V2 |
| WM | [spGetShippedWMOrderItemDiscounts_V3](WM.spGetShippedWMOrderItemDiscounts_V3.md) | WM.ItemDiscounts, WM.ItemStatus, WM.OrderItems, WM.vwOrderNumPickupStore, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderItemDiscounts_V3_1](WM.spGetShippedWMOrderItemDiscounts_V3_1.md) | WM.ItemDiscounts, WM.ItemStatus, WM.OrderItems, WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderItems](WM.spGetShippedWMOrderItems.md) | WM.ItemStatus, WM.OrderItems, WM.Orders, WM.vwSalesAuditSalesForReturn, WM.vwTransactionDetail |
| WM | [spGetShippedWMOrderItems_V2](WM.spGetShippedWMOrderItems_V2.md) | WM.ItemStatus, WM.OrderItems, WM.Orders, WM.vwSalesAuditSalesForReturn, WM.vwTransactionDetail_V2 |
| WM | [spGetShippedWMOrderItems_V3](WM.spGetShippedWMOrderItems_V3.md) | WM.ItemStatus, WM.OrderItems, WM.Orders, WM.vwOrderOrderTransactionIdentifier_BJB20210607, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderItems_V3_1](WM.spGetShippedWMOrderItems_V3_1.md) | WM.ItemStatus, WM.OrderItems, WM.Orders, WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderPayments](WM.spGetShippedWMOrderPayments.md) | WM.Orders, WM.vwTransactionDetail |
| WM | [spGetShippedWMOrderPayments_V2](WM.spGetShippedWMOrderPayments_V2.md) | WM.Orders, WM.vwTransactionDetailPayments |
| WM | [spGetShippedWMOrderPayments_V3](WM.spGetShippedWMOrderPayments_V3.md) | WM.Orders, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderPayments_V3_1](WM.spGetShippedWMOrderPayments_V3_1.md) | WM.Orders, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderPayments_V3_1_BJB2010608](WM.spGetShippedWMOrderPayments_V3_1_BJB2010608.md) | WM.Orders, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderPayments_V3_2](WM.spGetShippedWMOrderPayments_V3_2.md) | WM.Orders, WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderPayments_V3_2_BJB20250906](WM.spGetShippedWMOrderPayments_V3_2_BJB20250906.md) | WM.Orders, WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrders](WM.spGetShippedWMOrders.md) | WM.Orders, WM.Transactions, WM.vwSalesAuditShippingForReturn, WM.vwTransactionDetail |
| WM | [spGetShippedWMOrders_V2](WM.spGetShippedWMOrders_V2.md) | WM.Orders, WM.Transactions, WM.vwSalesAuditShippingForReturn, WM.vwTransactionDetail_V2 |
| WM | [spGetShippedWMOrders_V2_BJB20200430](WM.spGetShippedWMOrders_V2_BJB20200430.md) | WM.Orders, WM.Transactions, WM.vwSalesAuditShippingForReturn, WM.vwTransactionDetail_V2 |
| WM | [spGetShippedWMOrders_V3](WM.spGetShippedWMOrders_V3.md) | WM.Transactions, WM.vwOrderNumPickupStore, WM.vwOrderOrderTransactionIdentifier, WM.vwSalesAuditShippingForReturn, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrders_V3_1](WM.spGetShippedWMOrders_V3_1.md) | WM.tmpOrderOrderTransactionIdentifier, WM.Transactions, WM.vwSalesAuditShippingForReturn, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrders_V3_2](WM.spGetShippedWMOrders_V3_2.md) | WM.tmpOrderOrderTransactionIdentifier, WM.Transactions, WM.vwSalesAuditShippingForReturn, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderShippingDiscounts](WM.spGetShippedWMOrderShippingDiscounts.md) | WM.Orders, WM.ShippingDiscounts, WM.vwTransactionDetail |
| WM | [spGetShippedWMOrderShippingDiscounts_V2](WM.spGetShippedWMOrderShippingDiscounts_V2.md) | WM.Orders, WM.ShippingDiscounts, WM.vwTransactionDetail_V2 |
| WM | [spGetShippedWMOrderShippingDiscounts_V3](WM.spGetShippedWMOrderShippingDiscounts_V3.md) | WM.Orders, WM.ShippingDiscounts, WM.vwOrderNumPickupStore, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderShippingDiscounts_V3_1](WM.spGetShippedWMOrderShippingDiscounts_V3_1.md) | WM.ShippingDiscounts, WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderShipTo](WM.spGetShippedWMOrderShipTo.md) | WM.vwTransactionDetail |
| WM | [spGetShippedWMOrderShipTo_V2](WM.spGetShippedWMOrderShipTo_V2.md) | WM.vwTransactionDetail_V2 |
| WM | [spGetShippedWMOrderShipTo_V3](WM.spGetShippedWMOrderShipTo_V3.md) | WM.vwOrderNumPickupStore, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrderShipTo_V3_1](WM.spGetShippedWMOrderShipTo_V3_1.md) | WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrdersTaxes](WM.spGetShippedWMOrdersTaxes.md) | WM.Transactions, WM.vwSalesAuditTaxesForReturn, WM.vwTransactionDetail |
| WM | [spGetShippedWMOrdersTaxes_V2](WM.spGetShippedWMOrdersTaxes_V2.md) | WM.Transactions, WM.vwSalesAuditTaxesForReturn, WM.vwTransactionDetail_V2 |
| WM | [spGetShippedWMOrdersTaxes_V3](WM.spGetShippedWMOrdersTaxes_V3.md) | WM.Orders, WM.Transactions, WM.vwOrderNumPickupStore, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [spGetShippedWMOrdersTaxes_V3_1](WM.spGetShippedWMOrdersTaxes_V3_1.md) | WM.tmpOrderOrderTransactionIdentifier, WM.Transactions, WM.vwTransactionDetailPayments_V2 |
| WM | [spInsertOrderSentToWM](WM.spInsertOrderSentToWM.md) | WM.OrdersSentToWM |
| WM | [spOutputXMLFile](WM.spOutputXMLFile.md) |  |
| WM | [spRptWebOrderLookup](WM.spRptWebOrderLookup.md) | dbo.a, dbo.CRMTransactionFact, dbo.Currency_dim, dbo.POSSellingContextStage, dbo.Sales_GAAP_RawFromStoreServer, dbo.tender_dim, dbo.tender_facts, dbo.tmpWebSalesForPOSReturnsDetails, dbo.tmpWebSalesForPOSReturnsHeader, dbo.Transaction_Facts, POS.ProductCatalogMasterAttributesStage, wm.OMSTransactionDetails, wm.OrderItems, wm.Orders, wm.OrderStatus, wm.Payments |
| WM | [spRptWebOrderLookup_ForStorForce](WM.spRptWebOrderLookup_ForStorForce.md) | dbo.a, dbo.CRMTransactionFact, dbo.Currency_dim, dbo.POSSellingContextStage, dbo.Sales_GAAP_RawFromStoreServer, dbo.tender_dim, dbo.tender_facts, dbo.tmpWebSalesForPOSReturnsDetails, dbo.tmpWebSalesForPOSReturnsHeader, dbo.Transaction_Facts, POS.ProductCatalogMasterAttributesStage, wm.OMSTransactionDetails, wm.OrderItems, wm.Orders, wm.OrderStatus, wm.Payments |
| WM | [spRptWebOrderLookupBACKUP20231012](WM.spRptWebOrderLookupBACKUP20231012.md) | dbo.a, dbo.CRMTransactionFact, dbo.Currency_dim, dbo.POSSellingContextStage, dbo.Sales_GAAP_RawFromStoreServer, dbo.tender_dim, dbo.tender_facts, dbo.tmpWebSalesForPOSReturnsDetails, dbo.tmpWebSalesForPOSReturnsHeader, dbo.Transaction_Facts, wm.OMSTransactionDetails, wm.OrderItems, wm.Orders, wm.OrderStatus, wm.Payments |
| WM | [spTruncateAndReloadtmpOrderOrderTransactionIdentifier](WM.spTruncateAndReloadtmpOrderOrderTransactionIdentifier.md) | WM.tmpOrderOrderTransactionIdentifier, WM.vwOrderOrderTransactionIdentifier_BJB20210712 |
| WM | [spUKUpdateOrdersToShipped](WM.spUKUpdateOrdersToShipped.md) | WM.Orders, WM.OrderStatus, WMstg.stgOrderUpdateList |
| WM | [spUpdateBrokenInStoreFulfillmentOrders](WM.spUpdateBrokenInStoreFulfillmentOrders.md) | WM.Orders |
| WM | [spUpdateChannelAdvisorSets](WM.spUpdateChannelAdvisorSets.md) | WEB.vwPriceLists_BABWServices, WM.ItemStatus, WM.OrderItems, WM.Orders, WM.Payments |
| WM | [spUpdateOrderItemOverrideSounds](WM.spUpdateOrderItemOverrideSounds.md) | dbo.Sound, WM.OrderItemOverride |
| WM | [spUpdateWMItemStatus_to_SalesAuditComplete](WM.spUpdateWMItemStatus_to_SalesAuditComplete.md) | dbo.NSBTranslate_LogTrans, WM.OMSTransactionDetails, WM.Transactions, WM.vwOrderNumPickupStore |
| WM | [spUpdateWMItemStatus_to_SalesAuditComplete_BJB20200715](WM.spUpdateWMItemStatus_to_SalesAuditComplete_BJB20200715.md) | dbo.NSBTranslate_LogTrans, WM.OMSTransactionDetails, WM.Transactions, WM.vwTransactionDetail_V2 |
| WM | [spUpdateWMOrderStatus_to_SalesAuditComplete](WM.spUpdateWMOrderStatus_to_SalesAuditComplete.md) | WM.Orders, WM.OrderStatus, WM.vwTransactionsShipments_vs_Shipped |
| WM | [spUpdateWMOrderStatusByOrderID](WM.spUpdateWMOrderStatusByOrderID.md) | WM.OrderStatus |
| WM | [spVoucherCancelReserveLiability](WM.spVoucherCancelReserveLiability.md) | dbo.cust_liability |
| WM | [spVoucherReserveLiability](WM.spVoucherReserveLiability.md) | dbo.cust_liability |
| WM | [spWMPickticketXMLOnDemand](WM.spWMPickticketXMLOnDemand.md) | wm.ItemStatus, wm.OrderItems, wm.Orders, WM.OrdersNotInWM, wm.Orderstatus, wm.spOutputXMLFile |
