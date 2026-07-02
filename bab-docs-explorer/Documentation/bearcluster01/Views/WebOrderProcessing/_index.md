# Views: WebOrderProcessing

| Schema | View | Table Dependencies |
|---|---|---|
| ComHub | [vwPOWebOrderCurrentStatus](ComHub.vwPOWebOrderCurrentStatus.md) | ComHub.POWebOrder, ComHub.POWebOrderStatus |
| dbo | [vwBopisLocalTime](dbo.vwBopisLocalTime.md) | dbo.vwDWOpenStores, dbo.WebDemandOrderItemz, dbo.WebDemandOrderz |
| dbo | [vwBopisLocalTime_Bak20241203](dbo.vwBopisLocalTime_Bak20241203.md) | dbo.vwDWOpenStores, dbo.WebDemandOrderItemz, dbo.WebDemandOrderz |
| dbo | [vwCurrentOrderIds](dbo.vwCurrentOrderIds.md) | WM.OrderItems, WM.Orders, WM.OrderStatus |
| dbo | [vwCurrentOrderItemQuantities](dbo.vwCurrentOrderItemQuantities.md) | WM.OrderItems, WM.Orders, WM.OrderStatus |
| dbo | [vwDWFlashGaapWeb](dbo.vwDWFlashGaapWeb.md) | dbo.NSBTranslate_batch, dbo.NSBTranslate_logTrans, wm.ItemStatus, wm.OrderItems, wm.Orders, wm.ShippingDiscounts |
| dbo | [vwDWFlashGaapWeb_BAK20200915](dbo.vwDWFlashGaapWeb_BAK20200915.md) | wm.OMSCustomOrderExport, wm.Orders, wm.Transactions |
| dbo | [vwDWFlashGaapWebBACKUP20201230](dbo.vwDWFlashGaapWebBACKUP20201230.md) | wm.OMSCustomOrderExport, wm.Orders, wm.Transactions |
| dbo | [vwDWFlashGaapWebBAK20210112](dbo.vwDWFlashGaapWebBAK20210112.md) | wm.OrderItems, wm.Orders, wm.OrderStatus, wm.ShippingDiscounts, wm.Transactions |
| dbo | [vwDWFlashGaapWebBAK20210113](dbo.vwDWFlashGaapWebBAK20210113.md) | dbo.NSBTranslate_batch, dbo.NSBTranslate_logTrans, wm.OrderItems, wm.Orders, wm.ShippingDiscounts, wm.Transactions |
| dbo | [vwDWFlashGaapWebV2](dbo.vwDWFlashGaapWebV2.md) | dbo.NSBTranslate_batch, dbo.NSBTranslate_logTrans, WM.OMSTransactionDetails, wm.Orders, wm.OrderStatus, WM.Transactions |
| dbo | [vwDWFlashGaapWebV2BAK20210118](dbo.vwDWFlashGaapWebV2BAK20210118.md) | WM.OMSTransactionDetails, WM.Orders, WM.Transactions, WM.vwOrderOrderTransactionIdentifier |
| dbo | [vwOrderItemTransactionDetail](dbo.vwOrderItemTransactionDetail.md) | WM.ItemStatus, WM.OMSTransactionDetails, WM.OrderItems, WM.Orders |
| dbo | [vwStoreforceBopisAndPartyBySlot](dbo.vwStoreforceBopisAndPartyBySlot.md) | dbo.vwBopisLocalTime, dbo.vwPartiesBookedEvery30Minutes, dbo.vwStoreForcePartiesBookedEvery30Minutes, dbo.WebDemandOrderItemz |
| dbo | [vwWavePriority](dbo.vwWavePriority.md) | WM.Orders |
| WM | [vwCurrentOrderIds](WM.vwCurrentOrderIds.md) | WM.OrderItems, WM.Orders, WM.OrderStatus |
| WM | [vwDeckOrderItemStatusPivot](WM.vwDeckOrderItemStatusPivot.md) | wm.OMSCustomOrderExport |
| WM | [vwDeckOrderStatusPivot](WM.vwDeckOrderStatusPivot.md) | wm.OMSCustomOrderExport |
| WM | [vwDistinctItemStatuses](WM.vwDistinctItemStatuses.md) | WM.ItemStatus |
| WM | [vwDistinctOrderItems](WM.vwDistinctOrderItems.md) | WM.OrderItems |
| WM | [vwDonationInfo](WM.vwDonationInfo.md) | WM.ProductCatalogMasterAttributes_Mirror |
| WM | [vwDWOrderItemDiscounts](WM.vwDWOrderItemDiscounts.md) | wm.ItemDiscounts, wm.OrderItems, wm.Orders |
| WM | [vwEGiftCards](WM.vwEGiftCards.md) | WM.ProductCatalogMasterAttributes_Mirror |
| WM | [vwGiftCardInfo](WM.vwGiftCardInfo.md) | WM.ProductCatalogMasterAttributes_Mirror |
| WM | [vwGiftMessageHeartbox](WM.vwGiftMessageHeartbox.md) | wm.GiftMessage |
| WM | [vwOrderItemStatusPivot_V2](WM.vwOrderItemStatusPivot_V2.md) | WM.ItemStatus |
| WM | [vwOrderItemStatusPivotHistoric](WM.vwOrderItemStatusPivotHistoric.md) | WM.ItemStatus |
| WM | [vwOrderItemStatusWithArchive](WM.vwOrderItemStatusWithArchive.md) | WM.ItemStatus, WM.ItemStatus_Archive |
| WM | [vwOrderItemTransactionDetail](WM.vwOrderItemTransactionDetail.md) | WM.OMSTransactionDetails, WM.OrderItems, WM.Orders, WM.vwOrderItemStatusWithArchive |
| WM | [vwOrderNumPickupStore](WM.vwOrderNumPickupStore.md) | WM.Orders, WM.tmpOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [vwOrderNumPickupStore_BJB20210830](WM.vwOrderNumPickupStore_BJB20210830.md) | WM.Orders, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_V2 |
| WM | [vwOrderOrderTransactionIdentifier](WM.vwOrderOrderTransactionIdentifier.md) | WM.ItemStatus, WM.OMSTransactionDetails, WM.OrderItems, WM.Orders, WM.Transactions |
| WM | [vwOrderOrderTransactionIdentifier_BJB20210607](WM.vwOrderOrderTransactionIdentifier_BJB20210607.md) | WM.ItemStatus, WM.OMSTransactionDetails, WM.OrderItems, WM.Orders, WM.Transactions |
| WM | [vwOrderOrderTransactionIdentifier_BJB20210712](WM.vwOrderOrderTransactionIdentifier_BJB20210712.md) | WM.ItemStatus, WM.OrderItems, WM.Orders, WM.Transactions, WM.vwDonationInfo, WM.vwGiftCardInfo |
| WM | [vwOrderOrderTransactionIdentifier_V1_1](WM.vwOrderOrderTransactionIdentifier_V1_1.md) | WM.ItemStatus, WM.OMSTransactionDetails, WM.OrderItems, WM.Orders, WM.Transactions |
| WM | [vwOrderOrderTransactionIdentifier_V1_2](WM.vwOrderOrderTransactionIdentifier_V1_2.md) | WM.ItemStatus, WM.OrderItems, WM.Orders, WM.vwDonationInfo, WM.vwGiftCardInfo |
| WM | [vwOrderStatusPivot](WM.vwOrderStatusPivot.md) | wm.Orders, wm.OrderStatus |
| WM | [vwPartyRequestStoreLookup](WM.vwPartyRequestStoreLookup.md) | dbo.CNTRY_DIM, dbo.ST_PRVNC_DIM, dbo.STR_ADDR_DIM, dbo.STR_DIM |
| WM | [vwProductionOrderItem](WM.vwProductionOrderItem.md) | wm.OrderItems, WM.Orders, wm.vwProductionOrderSummary |
| WM | [vwProductionOrderSummary](WM.vwProductionOrderSummary.md) | WM.ItemDiscounts, WM.OrderItems, WM.Orders, wm.OrderStatus, WM.ShippingDiscounts, WM.Transactions |
| WM | [vwRptWebOrderLookup](WM.vwRptWebOrderLookup.md) | wm.OMSTransactionDetails, wm.OrderItems, wm.Orders |
| WM | [vwSalesAuditSalesForReturn](WM.vwSalesAuditSalesForReturn.md) | WM.ItemStatus, WM.OMSTransactionDetails, WM.OrderItems, WM.Orders, WM.Transactions |
| WM | [vwSalesAuditShippingForReturn](WM.vwSalesAuditShippingForReturn.md) | WM.OMSTransactionDetails, WM.Transactions |
| WM | [vwSalesAuditShippingForReturn_V2](WM.vwSalesAuditShippingForReturn_V2.md) | WM.OMSTransactionDetails, WM.Transactions |
| WM | [vwSalesAuditTaxesForReturn](WM.vwSalesAuditTaxesForReturn.md) | WM.OMSTransactionDetails, WM.Transactions |
| WM | [vwSalesAuditTaxesForReturn_V2](WM.vwSalesAuditTaxesForReturn_V2.md) | WM.Transactions, WM.vwTransactionDetail_V2 |
| WM | [vwSalesAuditTaxesForReturn_V3](WM.vwSalesAuditTaxesForReturn_V3.md) | WM.Transactions, WM.vwTransactionDetail_V3 |
| WM | [vwSAOrderItemOverrideOptions](WM.vwSAOrderItemOverrideOptions.md) | WM.SAOrderItemOverride, WM.vwStoreMDMRanges |
| WM | [vwStoreMDMRanges](WM.vwStoreMDMRanges.md) | dbo.BEARITORY_DIM, dbo.CNTRY_DIM, dbo.RGN_CNTRY_DIM, dbo.STR_DIM |
| WM | [vwTransactionDetail](WM.vwTransactionDetail.md) | WM.ItemStatus, WM.OMSTransactionDetails, WM.OrderItems, WM.Transactions |
| WM | [vwTransactionDetail_BJB_Delete_After20171231](WM.vwTransactionDetail_BJB_Delete_After20171231.md) | WM.OMSTransactionDetails, WM.Orders, WM.Transactions, WM.vwOrderItemStatusPivot |
| WM | [vwTransactionDetail_BJB20200716](WM.vwTransactionDetail_BJB20200716.md) | WM.ItemStatus, WM.OMSTransactionDetails, WM.OrderItems, WM.Transactions |
| WM | [vwTransactionDetail_V2](WM.vwTransactionDetail_V2.md) | WM.vwTransactionDetailPayments |
| WM | [vwTransactionDetail_V3](WM.vwTransactionDetail_V3.md) | WM.vwTransactionDetailPayments_V2 |
| WM | [vwTransactionDetailAll](WM.vwTransactionDetailAll.md) | WEB.vwGiftCardDisplayNameLookup, WM.OMSTransactionDetails, WM.OrderItems, WM.Orders, WM.Transactions, WM.vwTransactionDetailPayments_All_1_1 |
| WM | [vwTransactionDetailAll_1_1](WM.vwTransactionDetailAll_1_1.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwTransactionDetailPayments_All_1_1 |
| WM | [vwTransactionDetailAll_BJB_Delete_After20190522](WM.vwTransactionDetailAll_BJB_Delete_After20190522.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwTransactionDetailPayments_All_1_1 |
| WM | [vwTransactionDetailAll_BJB20181122](WM.vwTransactionDetailAll_BJB20181122.md) | WEB.vwGiftCardDisplayNameLookup, WM.OMSTransactionDetails, WM.OrderItems, WM.Orders, WM.Transactions, WM.vwTransactionDetailPayments_All_1_1 |
| WM | [vwTransactionDetailPayments](WM.vwTransactionDetailPayments.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwDistinctItemStatuses, WM.vwDistinctOrderItems |
| WM | [vwTransactionDetailPayments_All](WM.vwTransactionDetailPayments_All.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwDistinctItemStatuses, WM.vwDistinctOrderItems |
| WM | [vwTransactionDetailPayments_All_1_1](WM.vwTransactionDetailPayments_All_1_1.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwDistinctItemStatuses, WM.vwDistinctOrderItems, WM.vwOrderOrderTransactionIdentifier, WM.vwTransactionDetailPayments_All_V2 |
| WM | [vwTransactionDetailPayments_All_1_1_BJB20200716](WM.vwTransactionDetailPayments_All_1_1_BJB20200716.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwDistinctItemStatuses, WM.vwDistinctOrderItems |
| WM | [vwTransactionDetailPayments_All_Special](WM.vwTransactionDetailPayments_All_Special.md) | WM.OMSTransactionDetails, WM.Transactions |
| WM | [vwTransactionDetailPayments_All_V2](WM.vwTransactionDetailPayments_All_V2.md) | WM.OMSTransactionDetails, WM.Transactions |
| WM | [vwTransactionDetailPayments_BJB_DeleteAfter20180305](WM.vwTransactionDetailPayments_BJB_DeleteAfter20180305.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwDistinctItemStatuses, WM.vwDistinctOrderItems |
| WM | [vwTransactionDetailPayments_DMT](WM.vwTransactionDetailPayments_DMT.md) | WM.OMSTransactionDetails, WM.Transactions, WM.vwDistinctItemStatuses, WM.vwDistinctOrderItems |
| WM | [vwTransactionDetailPayments_V2](WM.vwTransactionDetailPayments_V2.md) | WM.OMSTransactionDetails, WM.Transactions |
| WM | [vwTransactionDetailPayments_V2_BJB20210607](WM.vwTransactionDetailPayments_V2_BJB20210607.md) | WM.OMSTransactionDetails, WM.Transactions |
| WM | [vwTransactionsShipments_vs_Shipped](WM.vwTransactionsShipments_vs_Shipped.md) | WM.Orders, WM.OrderStatus, WM.Payments, WM.Transactions |
| WM | [vwWaveJob_D365](WM.vwWaveJob_D365.md) | WM.WaveJob |
| WM | [vwWebSalesFlashGaapCapture](WM.vwWebSalesFlashGaapCapture.md) | dbo.NSBTranslate_LogTrans, dbo.PartyEnterpriseSellingXRef, wm.Orders, wm.vwTransactionDetailALL |
| WM | [vwWMPickticketXML](WM.vwWMPickticketXML.md) | wm.ItemStatus, wm.OrderItems, wm.Orders, wm.Orderstatus |
| WM | [vwWMPickticketXML_OnDEMAND](WM.vwWMPickticketXML_OnDEMAND.md) | wm.ItemStatus, wm.OrderItems, wm.Orders, WM.OrdersNotInWM, wm.Orderstatus |
