# Views: IntegrationStaging

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [vw_BAB_POS_Pricebook](dbo.vw_BAB_POS_Pricebook.md) | web.PricebookFact |
| dbo | [vwStoreSalesCheck_FinalStats](dbo.vwStoreSalesCheck_FinalStats.md) | dbo.StoreSalesCheck_Diff |
| ERP | [ShipmentInvoiceXML](ERP.ShipmentInvoiceXML.md) | ERP.ShipmentInvoice |
| ERP | [VW_CNStoreMaster](ERP.VW_CNStoreMaster.md) | ERP.vwWarehouseIDToLocationCode, ERP.WarehouseMaster, WMS.CountryCodes |
| ERP | [VW_CNVendorMaster](ERP.VW_CNVendorMaster.md) | ERP.PLM_Vendor, ERP.vwFactoryAddress |
| ERP | [vwAptosDistributionDynamicsOrderLookup](ERP.vwAptosDistributionDynamicsOrderLookup.md) | wms.DynamicsAPILog, WMS.StoreShipmentExport |
| ERP | [vwAvailableSupplies](ERP.vwAvailableSupplies.md) | ERP.WarehouseOnHand |
| ERP | [vwCostcoPOtoD365XML](ERP.vwCostcoPOtoD365XML.md) | ERP.CostcoInboundPODetail, ERP.CostcoInboundPOHeader |
| ERP | [vwDistributionData](ERP.vwDistributionData.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, ERP.ItemMaster, ERP.ItemMasterProducts, ERP.ItemsUOM, ERP.vwWarehouseIDToLocationCode |
| ERP | [vwDistributionsReadyToRelease](ERP.vwDistributionsReadyToRelease.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, erp.vwDistributionsReleased, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM |
| ERP | [vwDistributionsReadyToRelease_BAK20231205](ERP.vwDistributionsReadyToRelease_BAK20231205.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, erp.vwDistributionsReleased, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM |
| ERP | [vwDistributionsReadyToReleaseBAK20181206](ERP.vwDistributionsReadyToReleaseBAK20181206.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, ERP.ItemMaster, ERP.ItemMasterProducts, ERP.ItemsUOM, ERP.vwWarehouseIDToLocationCode |
| ERP | [vwDistributionsReadyToReleaseBAK20200202](ERP.vwDistributionsReadyToReleaseBAK20200202.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, ERP.ItemMaster, ERP.ItemMasterProducts, ERP.ItemsUOM, erp.vwDistributionsReleased, ERP.vwWarehouseIDToLocationCode |
| ERP | [vwDistributionsReadyToReleaseBAK20200205](ERP.vwDistributionsReadyToReleaseBAK20200205.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, erp.vwDistributionsReleased, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM, WMS.vwItemType |
| ERP | [vwDistributionsReadyToReleaseBAK20220801](ERP.vwDistributionsReadyToReleaseBAK20220801.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, erp.vwDistributionsReleased, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM |
| ERP | [vwDistributionsReadyToReleaseDevTest](ERP.vwDistributionsReadyToReleaseDevTest.md) | dbo.distribution_split, ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, ERP.ItemMaster, ERP.ItemMasterProducts, ERP.ItemsUOM, ERP.vwWarehouseIDToLocationCode |
| ERP | [vwDistributionsReleased](ERP.vwDistributionsReleased.md) | ERP.DistributionAddressDim, ERP.DistributionDetail, ERP.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM |
| ERP | [vwDistrosALL](ERP.vwDistrosALL.md) | ERP.DistributionAddressDim, erp.DistributionDetail, erp.DistributionHeader, ERP.DistributionRectype, ERP.FranchiseeLocationMap, ERP.ItemMaster, ERP.ItemMasterProducts, ERP.ItemsUOM, ERP.vwWarehouseIDToLocationCode |
| ERP | [vwFactoryAddress](ERP.vwFactoryAddress.md) | ERP.VendorMaster |
| ERP | [vwItemCompareDynamicsToAptosLoad](ERP.vwItemCompareDynamicsToAptosLoad.md) | ERP.ItemLoadtoD365, wms.ItemMaster, wms.ItemMasterProducts |
| ERP | [vwItemFactoryCN](ERP.vwItemFactoryCN.md) | erp.PurchaseOrderHeader, erp.PurchaseOrderLines, erp.VendorMaster, erp.vwFactoryAddress, WMS.ItemMaster, WMS.ItemMasterProducts |
| ERP | [vwItemFactoryMaster](ERP.vwItemFactoryMaster.md) | erp.PurchaseOrderHeader, erp.PurchaseOrderLines, erp.VendorMaster, erp.vwVendorFactoryAddress, WMS.ItemMasterProducts |
| ERP | [vwItemLoadReleasedProductCreationXML](ERP.vwItemLoadReleasedProductCreationXML.md) | ERP.ItemLoadtoD365, erp.ItemMasterProducts |
| ERP | [vwItemLoadReleasedProductsXML](ERP.vwItemLoadReleasedProductsXML.md) | ERP.ItemLoadtoD365, erp.ItemMasterProducts |
| ERP | [vwItemLoadToWhseStage](ERP.vwItemLoadToWhseStage.md) | ERP.ItemMaster, ERP.ItemMasterProducts, ERP.ItemsUOM |
| ERP | [vwItemMasterCN](ERP.vwItemMasterCN.md) | ERP.ItemMasterToWM |
| ERP | [vwItemMasterCNBonded](ERP.vwItemMasterCNBonded.md) | ERP.ItemMasterToWM, wms.AptosItemsTo3PL |
| ERP | [vwItemMasterCNNonBonded](ERP.vwItemMasterCNNonBonded.md) | ERP.ItemMasterToWM, wms.AptosItemsTo3PL |
| ERP | [vwItemMasterUKxml](ERP.vwItemMasterUKxml.md) | erp.ItemMasterToWM |
| ERP | [vwItemMasterUKxmlBACKUP20180703](ERP.vwItemMasterUKxmlBACKUP20180703.md) | erp.ItemMasterToWMStage |
| ERP | [vwItemMasterUKxmlBACKUP20201104](ERP.vwItemMasterUKxmlBACKUP20201104.md) | erp.ItemMasterToWM |
| ERP | [vwItemMasterUOM](ERP.vwItemMasterUOM.md) | wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| ERP | [vwItemMasterWC](ERP.vwItemMasterWC.md) | erp.ItemMasterToWM |
| ERP | [vwItemMasterWM](ERP.vwItemMasterWM.md) | ERP.vwItemFactoryMaster, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| ERP | [vwItemMasterWMBACKUP20180703](ERP.vwItemMasterWMBACKUP20180703.md) | ERP.vwItemMasterUOM |
| ERP | [vwItemMasterWMxml](ERP.vwItemMasterWMxml.md) | erp.ItemMasterToWM |
| ERP | [vwItemUOMCasePacks](ERP.vwItemUOMCasePacks.md) | ERP.vwItemMasterUOM, wms.ItemMaster, wms.ItemsUOM |
| ERP | [vwMerchandiseInventoryAdjustment](ERP.vwMerchandiseInventoryAdjustment.md) | ERP.ItemLoadtoD365, ERP.ItemMaster, ERP.WarehouseMaster |
| ERP | [vwPOReceiptIntegrationExceptionLog](ERP.vwPOReceiptIntegrationExceptionLog.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.PurchaseOrderReceiptExceptions, ERP.PurchaseOrderReceiptStage, WMS.ItemsUOM |
| ERP | [vwProductDimensionLookup](ERP.vwProductDimensionLookup.md) | erp.ItemMasterProducts, ERP.ItemsUOM, erp.PurchaseOrderHeader, erp.PurchaseOrderLines, erp.VendorMaster, erp.vwVendorFactoryAddress |
| ERP | [vwPurchaseOrderCN](ERP.vwPurchaseOrderCN.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwVendorFactoryAddress, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM, WMS.vwAptosPOtoDynamicsLog |
| ERP | [vwPurchaseOrderDBSchenker](ERP.vwPurchaseOrderDBSchenker.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwVendorFactoryAddress, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, WMS.ItemsUOM, WMS.vwAptosPOtoDynamicsLog |
| ERP | [vwPurchaseOrderDBSchenkerBAK20190625](ERP.vwPurchaseOrderDBSchenkerBAK20190625.md) | ERP.ItemMaster, ERP.ItemMasterProducts, ERP.ItemsUOM, ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwVendorFactoryAddress, ERP.vwWarehouseIDToLocationCode |
| ERP | [vwPurchaseOrderDBSchenkerBAK20220310](ERP.vwPurchaseOrderDBSchenkerBAK20220310.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwVendorFactoryAddress, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, WMS.ItemsUOM, WMS.vwAptosPOtoDynamicsLog |
| ERP | [vwPurchaseOrderDBSchenkerBAK20220322](ERP.vwPurchaseOrderDBSchenkerBAK20220322.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwVendorFactoryAddress, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, WMS.ItemsUOM, WMS.vwAptosPOtoDynamicsLog |
| ERP | [vwPurchaseOrderDBSchenkerONDemand](ERP.vwPurchaseOrderDBSchenkerONDemand.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwVendorFactoryAddress, ERP.vwWarehouseIDToLocationCode, WMS.ItemMaster, WMS.ItemMasterProducts, WMS.ItemsUOM |
| ERP | [vwPurchaseOrderHeaderDynamicsExtract](ERP.vwPurchaseOrderHeaderDynamicsExtract.md) | ERP.PurchaseOrderHeaderStage |
| ERP | [vwPurchaseOrderHeaderDynamicsExtractBAK20210929](ERP.vwPurchaseOrderHeaderDynamicsExtractBAK20210929.md) | ERP.PurchaseOrderHeaderStage, erp.PurchaseOrderLinesStage |
| ERP | [vwPurchaseOrderLinesDynamicsExtract](ERP.vwPurchaseOrderLinesDynamicsExtract.md) | ERP.PurchaseOrderLinesStage |
| ERP | [vwPurchaseOrderLinesDynamicsExtractServiceItems](ERP.vwPurchaseOrderLinesDynamicsExtractServiceItems.md) | ERP.PurchaseOrderLinesStage |
| ERP | [vwPurchaseOrderReceipts](ERP.vwPurchaseOrderReceipts.md) | ERP.PurchaseOrderReceipt, ERP.tmpReceiptID |
| ERP | [vwPurchaseOrderReceiptXML](ERP.vwPurchaseOrderReceiptXML.md) | ERP.vwPurchaseOrderReceipts |
| ERP | [vwPurchaseOrderReceiptXML_BAK20230123](ERP.vwPurchaseOrderReceiptXML_BAK20230123.md) | ERP.vwPurchaseOrderReceipts |
| ERP | [vwPurchaseOrderReceiptXML_workInprogress](ERP.vwPurchaseOrderReceiptXML_workInprogress.md) | ERP.vwPurchaseOrderReceipts |
| ERP | [vwPurchaseOrderTPM](ERP.vwPurchaseOrderTPM.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, erp.PurchaseOrderLinesServiceItems, ERP.PurchaseOrderResendTPM, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM, WMS.vwAptosPOtoDynamicsLog |
| ERP | [vwPurchaseOrderTPM_BAK20210927](ERP.vwPurchaseOrderTPM_BAK20210927.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.PurchaseOrderResendTPM, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM, WMS.vwAptosPOtoDynamicsLog |
| ERP | [vwPurchaseOrderTPM_XML](ERP.vwPurchaseOrderTPM_XML.md) | ERP.tmpTPMpo, ERP.vwPurchaseOrderTPM |
| ERP | [vwPurchaseOrderUK](ERP.vwPurchaseOrderUK.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwVendorFactoryAddress, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM, WMS.vwAptosPOtoDynamicsLog |
| ERP | [vwPurchaseOrderUK_BAK072325](ERP.vwPurchaseOrderUK_BAK072325.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, ERP.vwItemMasterUOM, ERP.vwVendorFactoryAddress, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM, WMS.vwAptosPOtoDynamicsLog |
| ERP | [vwPurchaseOrderWholesale](ERP.vwPurchaseOrderWholesale.md) | ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.VendorMaster, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| ERP | [vwShipmentInvoice_SalesOrderXML](ERP.vwShipmentInvoice_SalesOrderXML.md) | ERP.ShipmentInvoice |
| ERP | [vwShipmentInvoice_TransferXML](ERP.vwShipmentInvoice_TransferXML.md) | ERP.ShipmentInvoice |
| ERP | [vwShipmentInvoiceStage](ERP.vwShipmentInvoiceStage.md) | ERP.DistributionDetail, erp.DistributionHeader, erp.ShipmentInvoicePreStage, ERP.vwWarehouseIDToLocationCode, ERP.vwWarehouseIDToLocationCodeRetailInventory, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| ERP | [vwShipmentInvoiceStage_Bak20220817](ERP.vwShipmentInvoiceStage_Bak20220817.md) | ERP.DistributionDetail, erp.DistributionHeader, erp.ShipmentInvoicePreStage, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| ERP | [vwShipmentInvoiceStage_Bak20230414](ERP.vwShipmentInvoiceStage_Bak20230414.md) | ERP.DistributionDetail, erp.DistributionHeader, erp.ShipmentInvoicePreStage, ERP.vwWarehouseIDToLocationCode, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| ERP | [vwSuppliesOnOrder](ERP.vwSuppliesOnOrder.md) | ERP.ItemMaster, ERP.ItemsUOM, ERP.PurchaseOrderHeader, ERP.PurchaseOrderLines, ERP.PurchaseOrderReceipt, ERP.WhseReceipt_NonPO |
| ERP | [vwSuppliesReceived](ERP.vwSuppliesReceived.md) | ERP.ItemMaster, ERP.ItemsUOM, ERP.PurchaseOrderReceipt, ERP.WhseReceipt_NonPO |
| ERP | [vwTransferReceiptXML](ERP.vwTransferReceiptXML.md) | ERP.ShipmentInvoice, erp.vwItemMasterUOM, erp.vwWarehouseIDToLocationCode, erp.wcPalletReceipts |
| ERP | [vwValidation_POReceipts](ERP.vwValidation_POReceipts.md) | ERP.PurchaseOrderReceipt |
| ERP | [vwVendorFactoryAddress](ERP.vwVendorFactoryAddress.md) | erp.FactoryAddress, erp.VendorMaster |
| ERP | [vwVendorFactoryAddressBAK20190507](ERP.vwVendorFactoryAddressBAK20190507.md) | erp.FactoryAddress, erp.VendorMaster |
| ERP | [vwWarehouseIDToLocationCode](ERP.vwWarehouseIDToLocationCode.md) | ERP.WarehouseMaster |
| ERP | [vwWarehouseIDToLocationCodeBAK20180720](ERP.vwWarehouseIDToLocationCodeBAK20180720.md) | ERP.WarehouseMaster |
| ERP | [vwWarehouseIDToLocationCodeBAK20220801](ERP.vwWarehouseIDToLocationCodeBAK20220801.md) | ERP.WarehouseMaster |
| ERP | [vwWarehouseIDToLocationCodeRetailInventory](ERP.vwWarehouseIDToLocationCodeRetailInventory.md) | erp.vwWarehouseIDToLocationCode, erp.WarehouseMaster |
| ERP | [vwWarehouseIDToLocationCodeRetailInventory_InventorySync](ERP.vwWarehouseIDToLocationCodeRetailInventory_InventorySync.md) | erp.vwWarehouseIDToLocationCode, erp.WarehouseMaster |
| ERP | [vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated](ERP.vwWarehouseIDToLocationCodeRetailInventory_PartnerOperated.md) | erp.vwWarehouseIDToLocationCode, erp.WarehouseMaster |
| ERP | [vwWarehouseIDToLocationCodeTEST](ERP.vwWarehouseIDToLocationCodeTEST.md) | ERP.WarehouseMaster |
| ERP | [vwWmStoreMasterXML](ERP.vwWmStoreMasterXML.md) | ERP.DistributionAddressDim |
| ES | [vwEnterpriseSellingOMSExtensions](ES.vwEnterpriseSellingOMSExtensions.md) | WEB.ProductCatalogMasterAttributes |
| ES | [vwEnterpriseSellingOMSExtensions_1_1](ES.vwEnterpriseSellingOMSExtensions_1_1.md) | WEB.ProductCatalogMasterAttributes |
| POS | [vwPOSOutbound_Products](POS.vwPOSOutbound_Products.md) | dbo.jumpmind_tax_group, POS.ProductCatalogMasterAttributesStage |
| POS | [vwPOSOutbound_Products_QA](POS.vwPOSOutbound_Products_QA.md) | dbo.jumpmind_tax_group, POS.ProductCatalogMasterAttributesStage |
| POS | [vwPOSProductImageURL](POS.vwPOSProductImageURL.md) | pos.ProductCatalogMasterAttributesStage, pos.ProductImageURL |
| POS | [vwProductNameDescriptions](POS.vwProductNameDescriptions.md) | POS.ProductCatalogMasterAttributesStage, POS.ProductNameDescription, POS.ProductNameDescriptionStage |
| TXT | [vwFinalData](TXT.vwFinalData.md) | dbo.date_dim, TXT.AptosMerchFields, TXT.BOPOHCostTotal, TXT.BOPOHRetailTotalTE, TXT.BOPOHUnitsTotal, TXT.EOPOHCostTotal, TXT.EOPOHRetailTotalTE, TXT.EOPOHUnitsTotal, TXT.ItemDetailsDynamics, TXT.ItemDetailsPLM, TXT.NetReceiptCost, TXT.NetReceiptsRetailTE, TXT.NetReceiptUnits, TXT.NetSalesCost, TXT.NetSalesRetailTE, TXT.NetSalesUnits, TXT.OnOrderCost, TXT.OnOrderCost6Month, TXT.OnOrderRetailTE, TXT.OnOrderRetailTE6Month, TXT.OnOrderUnits, TXT.OnOrderUnits6Month, TXT.PrdDates, TXT.ShrinkActualRetailTE, TXT.ShrinkActualUnits |
| WEB | [AlternateImagePivot](WEB.AlternateImagePivot.md) | WEB.AlternateImagesStage |
| WEB | [vwBundlePricebookFactPreStage](WEB.vwBundlePricebookFactPreStage.md) | web.BundlePricebookFactPreStage |
| WEB | [vwBundlePricebookFactPreStage_Bak20241003](WEB.vwBundlePricebookFactPreStage_Bak20241003.md) | web.BundlePricebookFactPreStage |
| WEB | [vwCouponCustomPreferences](WEB.vwCouponCustomPreferences.md) | WEB.DiscountCouponExport |
| WEB | [vwDynamicActionOrderCountValidation](WEB.vwDynamicActionOrderCountValidation.md) | web.DynamicActionOrderHeaderStage, web.DynamicActionOrderLinesStage |
| WEB | [vwInventoryCSV](WEB.vwInventoryCSV.md) | WEB.InventoryFact, WEB.ProductCatalogMasterAttributes |
| WEB | [vwInventoryCSV_BACKUP20210909](WEB.vwInventoryCSV_BACKUP20210909.md) | WEB.InventoryFact, WEB.ProductCatalogMasterAttributes |
| WEB | [vwInventoryCSV_WorkInProgress](WEB.vwInventoryCSV_WorkInProgress.md) | WEB.InventoryFact, web.LocationStage, web.PreOrderBackOrderInventory, WEB.ProductCatalogMasterAttributes |
| WEB | [vwInventoryXML](WEB.vwInventoryXML.md) | WEB.InventoryFact, web.LocationStage, WEB.ProductCatalogMasterAttributes |
| WEB | [vwInventoryXML_BACKUP20180327](WEB.vwInventoryXML_BACKUP20180327.md) | WEB.InventoryFact, web.LocationStage, WEB.ProductCatalogMasterAttributes |
| WEB | [vwLocationsXML](WEB.vwLocationsXML.md) | WEB.LocationStage |
| WEB | [vwPartyWebOrdersShipped](WEB.vwPartyWebOrdersShipped.md) | WMS.ItemMasterProducts, WMS.PartyHeader, WMS.PartyLines, WMS.PartyShipDetails |
| WEB | [vwPOSpricebook](WEB.vwPOSpricebook.md) | web.PricebookFact |
| WEB | [vwPOSproducts](WEB.vwPOSproducts.md) | dbo.vwPOSProductHierarchy, Web.ProductCatalogMasterAttributes |
| WEB | [vwPricebookListUKXML](WEB.vwPricebookListUKXML.md) | web.PricebookBundleSkuFact, WEB.PricebookFact, WEB.PricebookFactArchive |
| WEB | [vwPricebookListUKXML_BAK20220705](WEB.vwPricebookListUKXML_BAK20220705.md) | WEB.PricebookFact, WEB.PricebookFactArchive |
| WEB | [vwPricebookListUKXML_BAK20240806](WEB.vwPricebookListUKXML_BAK20240806.md) | WEB.PricebookFact, WEB.PricebookFactArchive |
| WEB | [vwPricebookListUKXML_FULL](WEB.vwPricebookListUKXML_FULL.md) | WEB.PricebookFact |
| WEB | [vwPricebookListUSXML](WEB.vwPricebookListUSXML.md) | web.PricebookBundleSkuFact, WEB.PricebookFact, WEB.PricebookFactArchive |
| WEB | [vwPricebookListUSXML_BAK20220705](WEB.vwPricebookListUSXML_BAK20220705.md) | WEB.PricebookFact, WEB.PricebookFactArchive |
| WEB | [vwPricebookListUSXML_BAK20240806](WEB.vwPricebookListUSXML_BAK20240806.md) | WEB.PricebookFact, WEB.PricebookFactArchive |
| WEB | [vwPricebookListUSXML_Full](WEB.vwPricebookListUSXML_Full.md) | WEB.PricebookFact |
| WEB | [vwPricebookSaleUKXML](WEB.vwPricebookSaleUKXML.md) | web.PricebookFact, WEB.PricebookFactArchive, web.ProductCatalogMasterAttributes |
| WEB | [vwPricebookSaleUSXML](WEB.vwPricebookSaleUSXML.md) | web.PricebookFact, WEB.PricebookFactArchive, web.ProductCatalogMasterAttributes |
| WEB | [vwPricebooksUKXML](WEB.vwPricebooksUKXML.md) | WEB.vwPricebookListUKXML |
| WEB | [vwPricebooksUKXML_BAK20220705](WEB.vwPricebooksUKXML_BAK20220705.md) | WEB.vwPricebookListUKXML, WEB.vwPricebookSaleUKXML |
| WEB | [vwPricebooksUKXML_FULL](WEB.vwPricebooksUKXML_FULL.md) | WEB.vwPricebookListUKXML_FULL |
| WEB | [vwPricebooksUSXML](WEB.vwPricebooksUSXML.md) | WEB.vwPricebookListUSXML |
| WEB | [vwPricebooksUSXML_BAK20220705](WEB.vwPricebooksUSXML_BAK20220705.md) | WEB.vwPricebookListUSXML, WEB.vwPricebookSaleUSXML |
| WEB | [vwPricebooksUSXML_FULL](WEB.vwPricebooksUSXML_FULL.md) | WEB.vwPricebookListUSXML_FULL |
| WEB | [vwPriceLists_BABWServices](WEB.vwPriceLists_BABWServices.md) | web.PricebookFact, web.ProductCatalogMasterAttributes |
| WEB | [vwProductCatalogMasterDeltaXML](WEB.vwProductCatalogMasterDeltaXML.md) | WEB.AlternateImages, WEB.AlternateImagesArchive, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterCategory, WEB.ProductCatalogMasterCategoryArchive, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive, WEB.ProductStorefrontCategoryMap |
| WEB | [vwProductCatalogMasterFullXML](WEB.vwProductCatalogMasterFullXML.md) | WEB.AlternateImages, Web.AltImageTags, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterCategory, WEB.ProductCatalogMasterCategoryArchive, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive, WEB.ProductStorefrontCategoryMap |
| WEB | [vwProductCatalogMasterFullXML_BACKUP](WEB.vwProductCatalogMasterFullXML_BACKUP.md) | WEB.AlternateImages, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterCategory, WEB.ProductCatalogMasterCategoryArchive, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive, WEB.ProductStorefrontCategoryMap |
| WEB | [vwProductCatalogMasterFullXML_BACKUP20190826](WEB.vwProductCatalogMasterFullXML_BACKUP20190826.md) | WEB.AlternateImages, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterCategory, WEB.ProductCatalogMasterCategoryArchive, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive, WEB.ProductStorefrontCategoryMap |
| WEB | [vwProductCatalogMasterFullXML_BACKUP20201102](WEB.vwProductCatalogMasterFullXML_BACKUP20201102.md) | WEB.AlternateImages, Web.AltImageTags, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterCategory, WEB.ProductCatalogMasterCategoryArchive, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive, WEB.ProductStorefrontCategoryMap |
| WEB | [vwProductCatalogMasterFullXML_BACKUP20221101](WEB.vwProductCatalogMasterFullXML_BACKUP20221101.md) | WEB.AlternateImages, Web.AltImageTags, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterCategory, WEB.ProductCatalogMasterCategoryArchive, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive, WEB.ProductStorefrontCategoryMap |
| WEB | [vwProductCatalogMasterFullXMLBackup20220818](WEB.vwProductCatalogMasterFullXMLBackup20220818.md) | WEB.AlternateImages, Web.AltImageTags, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterAttributesArchive, WEB.ProductCatalogMasterCategory, WEB.ProductCatalogMasterCategoryArchive, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive, WEB.ProductStorefrontCategoryMap |
| WEB | [vwProductCatalogMasterXML](WEB.vwProductCatalogMasterXML.md) | WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterCategoryStage, WEB.ProductCategoryMap, WEB.ProductCategoryMapArchive |
| WEB | [vwProductCatalogPimberly](WEB.vwProductCatalogPimberly.md) | WEB.AlternateImages, Web.AltImageTags, WEB.ProductCatalogMasterAttributes, WEB.ProductStorefrontCategoryMap |
| WEB | [vwProductCategoryMap](WEB.vwProductCategoryMap.md) | WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogMasterCategoryStage |
| WEB | [vwProductInventoryBySellingGeography](WEB.vwProductInventoryBySellingGeography.md) | WEB.InventoryFact |
| WEB | [vwProductionOrderItemLookups](WEB.vwProductionOrderItemLookups.md) | WEB.ProductCatalogMasterAttributes |
| WEB | [vwProductPrice](WEB.vwProductPrice.md) | WEB.PricebookPreStageBase, Web.ProductCatalogMasterAttributes, WEB.WebStyleAttributes |
| WEB | [vwProductStorefrontCatalogCategories](WEB.vwProductStorefrontCatalogCategories.md) | WEB.CategoryXREF |
| WEB | [vwProductStorefrontCatalogUKdeltaXML](WEB.vwProductStorefrontCatalogUKdeltaXML.md) | WEB.ProductCatalogStorefrontCategory, WEB.ProductCatalogStorefrontCategoryArchive, WEB.ProductStorefrontCategoryMap, WEB.ProductStorefrontCategoryMapArchive |
| WEB | [vwProductStorefrontCatalogUKfullXML](WEB.vwProductStorefrontCatalogUKfullXML.md) | WEB.ProductCatalogStorefrontCategory, WEB.ProductCatalogStorefrontCategoryArchive, WEB.ProductStorefrontCategoryMap, WEB.ProductStorefrontCategoryMapArchive |
| WEB | [vwProductStorefrontCatalogUSdeltaXML](WEB.vwProductStorefrontCatalogUSdeltaXML.md) | WEB.ProductCatalogStorefrontCategory, WEB.ProductCatalogStorefrontCategoryArchive, WEB.ProductStorefrontCategoryMap, WEB.ProductStorefrontCategoryMapArchive |
| WEB | [vwProductStorefrontCatalogUSfullXML](WEB.vwProductStorefrontCatalogUSfullXML.md) | WEB.ProductCatalogStorefrontCategory, WEB.ProductCatalogStorefrontCategoryArchive, WEB.ProductStorefrontCategoryMap, WEB.ProductStorefrontCategoryMapArchive |
| WEB | [vwProductStorefrontCatalogXML](WEB.vwProductStorefrontCatalogXML.md) | WEB.vwProductStorefrontCatalogUKXML, WEB.vwProductStorefrontCatalogUSXML |
| WEB | [vwProductStorefrontCategoryMap](WEB.vwProductStorefrontCategoryMap.md) | WEB.AttributeNullExceptions, WEB.CategoryExceptions, WEB.CategoryXREF, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogStorefrontCategory |
| WEB | [vwProductStorefrontCategoryMapBAK20180402](WEB.vwProductStorefrontCategoryMapBAK20180402.md) | WEB.AttributeNullExceptions, WEB.CategoryExceptions, WEB.CategoryXREF, WEB.ProductCatalogMasterAttributes, WEB.ProductCatalogStorefrontCategory |
| WEB | [vwStoreInventoryBuffer](WEB.vwStoreInventoryBuffer.md) | WEB.InventoryFact, WEB.ProductCatalogMasterAttributes, WEB.StoreInventoryBuffers |
| WEB | [vwStoreInventoryCSV](WEB.vwStoreInventoryCSV.md) | WEB.InventoryFact, Web.LocationStage, WEB.ProductCatalogMasterAttributes, WEB.StoreInventoryBuffers |
| WEB | [vwStoreInventoryCSV_TESTING](WEB.vwStoreInventoryCSV_TESTING.md) | WEB.InventoryFact, Web.LocationStage, WEB.ProductCatalogMasterAttributes, WEB.StoreInventoryBuffers |
| WEB | [vwWebIncludedStyles](WEB.vwWebIncludedStyles.md) | WEB.ProductCatalogMasterAttributes |
| WM | [vwOMSStyleCodeGTINLookup](WM.vwOMSStyleCodeGTINLookup.md) | WEB.ProductCatalogMasterAttributes |
| WM | [vwWMPickticketXML](WM.vwWMPickticketXML.md) | wm.OrderItems, wm.orders |
| WMS | [vwAptosDistrosInDynamics](WMS.vwAptosDistrosInDynamics.md) | wms.DynamicsAPILog, wms.ItemMasterProducts, wms.StoreShipmentExport |
| WMS | [vwAptosDistrosVsDynamicsPostWave](WMS.vwAptosDistrosVsDynamicsPostWave.md) | wms.CartonsCancelledToHA, wms.CartonsSummaryToHA, wms.DynamicsAPILog, wms.ItemMasterProducts, wms.StoreShipmentExport |
| WMS | [vwAptosDistrosVsDynamicsShipments](WMS.vwAptosDistrosVsDynamicsShipments.md) | wms.DynamicsAPILog, wms.ShipmentConfirmAptos, wms.StoreShipmentExport |
| WMS | [vwAptosDistrosVsShipments](WMS.vwAptosDistrosVsShipments.md) | wms.DynamicsAPILog, wms.ShipmentConfirmAptos, WMS.StoreShipmentExport |
| WMS | [vwAptosDistrosWaveAllocatedVsShipConfirm](WMS.vwAptosDistrosWaveAllocatedVsShipConfirm.md) | wms.ShipmentConfirmAptos, wms.vwAptosDistrosVsDynamicsPostWave |
| WMS | [vwAptosPOtoDynamicsLog](WMS.vwAptosPOtoDynamicsLog.md) | WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwAptosPOtoDynamicsLogDetail](WMS.vwAptosPOtoDynamicsLogDetail.md) | erp.VendorMaster, wms.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwASNtoDynamicsAPI](WMS.vwASNtoDynamicsAPI.md) | erp.PurchaseOrderHeader, erp.VendorMaster, ERP.vwItemMasterUOM, WMS.ASN_TPMToDynamics, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwASNtoDynamicsAPI_Back20231212](WMS.vwASNtoDynamicsAPI_Back20231212.md) | erp.PurchaseOrderHeader, erp.VendorMaster, ERP.vwItemMasterUOM, WMS.ASN_TPMToDynamics, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwASNtoDynamicsAPI_BAK_20230411](WMS.vwASNtoDynamicsAPI_BAK_20230411.md) | erp.PurchaseOrderHeader, erp.VendorMaster, ERP.vwItemMasterUOM, WMS.ASN_TPMToDynamics, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwASNtoDynamicsAPI_BAK20230710](WMS.vwASNtoDynamicsAPI_BAK20230710.md) | erp.PurchaseOrderHeader, erp.VendorMaster, ERP.vwItemMasterUOM, WMS.ASN_TPMToDynamics, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwASNtoDynamicsAPI_OnDemand](WMS.vwASNtoDynamicsAPI_OnDemand.md) | erp.PurchaseOrderHeader, erp.VendorMaster, ERP.vwItemMasterUOM, WMS.ASN_TPMToDynamics, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwAvailableSupplies](WMS.vwAvailableSupplies.md) | WMS.vwItemType, WMS.WarehouseOnHand |
| WMS | [vwCostcoAPIResponse](WMS.vwCostcoAPIResponse.md) | wms.DynamicsAPILog |
| WMS | [vwCostcoOrdersShipped](WMS.vwCostcoOrdersShipped.md) | ERP.CostcoInboundPODetail, ERP.CostcoInboundPOHeader, wms.DynamicsAPILog, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM, wms.SalesOrderStatusUpdateShipped |
| WMS | [vwCostcoPOtoDynamicsSO](WMS.vwCostcoPOtoDynamicsSO.md) | ERP.CostcoInboundPODetail, ERP.CostcoInboundPOHeader, wms.ItemMaster, wms.ItemsUOM |
| WMS | [vwDeckOrdersByWaveId](WMS.vwDeckOrdersByWaveId.md) | WMS.SalesOrderStatusUpdateWaved |
| WMS | [vwDistributionRecTypeByCountryForLookup](WMS.vwDistributionRecTypeByCountryForLookup.md) | erp.DistributionRecType |
| WMS | [vwDynamicsPOReceiptFromDBSchenkerASN](WMS.vwDynamicsPOReceiptFromDBSchenkerASN.md) | erp.VendorMaster, WMS.DBSchenkerFullInGateFile, WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwDynamicsPOReceiptVarianceVsAptos](WMS.vwDynamicsPOReceiptVarianceVsAptos.md) | dbo.location, dbo.po, dbo.po_receipt, dbo.po_receipt_detail, dbo.style, WMS.vwDynamicsPurchaseOrderReceipts |
| WMS | [vwDynamicsPurchaseOrderReceipts](WMS.vwDynamicsPurchaseOrderReceipts.md) | WMS.DynamicsProductReceiptHeaderStage, WMS.DynamicsProductReceiptLineStage, wms.ItemMaster, wms.ItemMasterProducts, WMS.vwPurchaseOrderDynamicsPOtoAptosPO |
| WMS | [vwDynamicsPurchaseOrderReceipts_NonAptos](WMS.vwDynamicsPurchaseOrderReceipts_NonAptos.md) | WMS.DynamicsProductReceiptHeaderStage, WMS.DynamicsProductReceiptLineStage, wms.ItemMaster, wms.ItemMasterProducts, WMS.vwPurchaseOrderDynamicsPOtoAptosPO |
| WMS | [vwDynamicsPurchaseOrderReceiptsBAK20220801](WMS.vwDynamicsPurchaseOrderReceiptsBAK20220801.md) | WMS.DynamicsProductReceiptHeaderStage, WMS.DynamicsProductReceiptLineStage, wms.ItemMaster, wms.ItemMasterProducts, WMS.vwPurchaseOrderDynamicsPOtoAptosPO |
| WMS | [vwDynamicsPurchaseOrdersFromAptos](WMS.vwDynamicsPurchaseOrdersFromAptos.md) | WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwDynamicsPurchaseOrdersFromAptosWithStyleCode](WMS.vwDynamicsPurchaseOrdersFromAptosWithStyleCode.md) | WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwDynamicsTendersCardTypes](WMS.vwDynamicsTendersCardTypes.md) | wms.RetailStoreTenderTypeStage, wms.RetailTenderTypeCardStage |
| WMS | [vwDynamicsVendorInvoiceDim](WMS.vwDynamicsVendorInvoiceDim.md) | erp.VendorMaster, ERP.WarehouseMaster, WMS.DynamicsVendorInvoiceJournalLineStage |
| WMS | [vwDynamicsVendorInvoiceDimV2](WMS.vwDynamicsVendorInvoiceDimV2.md) | erp.VendorMaster, ERP.WarehouseMaster, WMS.DynamicsVendorInvoiceJournalLineStage |
| WMS | [vweCommNewWaves](WMS.vweCommNewWaves.md) | WMS.eCommWaveStatus, WMS.vwSalesOrderStatusUpdateWaved |
| WMS | [vweCommWavedMessageCount](WMS.vweCommWavedMessageCount.md) | WMS.eCommWaveStatus, WMS.vwSalesOrderStatusUpdateWaved |
| WMS | [vwInventorySync_3PW](WMS.vwInventorySync_3PW.md) | erp.vwItemMasterUOM, wms.ItemMaster, WMS.WarehouseOnHand |
| WMS | [vwItemCasePackCN](WMS.vwItemCasePackCN.md) | WMS.ItemCasePack, wms.ItemMaster |
| WMS | [vwItemCasePackSrc](WMS.vwItemCasePackSrc.md) | WMS.ItemCasePackStage, wms.ItemMaster |
| WMS | [vwItemMasterTo3PL](WMS.vwItemMasterTo3PL.md) | wms.CountryCodes, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| WMS | [vwItemMasterUnitSymbol](WMS.vwItemMasterUnitSymbol.md) | WMS.ItemMaster |
| WMS | [vwItemStandardCaseQuantityWeightVolume](WMS.vwItemStandardCaseQuantityWeightVolume.md) | wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| WMS | [vwItemsWithoutHTS_COO_Factory](WMS.vwItemsWithoutHTS_COO_Factory.md) | erp.PurchaseOrderHeader, erp.PurchaseOrderLines, erp.VendorMaster, erp.vwVendorFactoryAddress, wms.ItemMaster, wms.ItemMasterProducts, wms.PurchaseOrderMerchToDynamics |
| WMS | [vwItemsWithoutHTS_COO_Factory_UK](WMS.vwItemsWithoutHTS_COO_Factory_UK.md) | wms.ItemMaster, wms.ItemMasterProducts |
| WMS | [vwItemType](WMS.vwItemType.md) | WMS.ItemMaster |
| WMS | [vwMerchDistrosLookup](WMS.vwMerchDistrosLookup.md) | dbo.location, dbo.store_shipment, dbo.store_shipment_detail, dbo.style, ERP.vwWarehouseIDToLocationCode, wms.DynamicsAPILog, wms.ShipmentConfirmAptos, WMS.StoreShipmentExport |
| WMS | [vwModeOfDeliveryWeb](WMS.vwModeOfDeliveryWeb.md) | WMS.ModeOfDeliveryWeb |
| WMS | [vwNightlyWaveCartonDetails](WMS.vwNightlyWaveCartonDetails.md) | erp.DistributionRecType, WMS.CartonsSummaryToHA, wms.ItemMaster, WMS.vwAptosDistrosInDynamics |
| WMS | [vwNightlyWaveControl](WMS.vwNightlyWaveControl.md) | WMS.CartonsSummaryToHA, WMS.WaveControl |
| WMS | [vwNonWarehouseOnHand](WMS.vwNonWarehouseOnHand.md) | WMS.NonWarehouseOnHand |
| WMS | [vwPartyAPIResponse](WMS.vwPartyAPIResponse.md) | wms.DynamicsAPILog, WMS.StoreShipmentExport |
| WMS | [vwPOAptosToDynamics](WMS.vwPOAptosToDynamics.md) | erp.VendorMaster, wms.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwPOAptosToDynamicsBACKUP20210628](WMS.vwPOAptosToDynamicsBACKUP20210628.md) | erp.VendorMaster, wms.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwPurchaseOrderDynamicsPOtoAptosPO](WMS.vwPurchaseOrderDynamicsPOtoAptosPO.md) | erp.VendorMaster, WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwPurchaseOrderDynamicsPOtoAptosPOBAK20220801](WMS.vwPurchaseOrderDynamicsPOtoAptosPOBAK20220801.md) | erp.VendorMaster, WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwPurchaseOrderDynamicsPOtoAptosPOWithItemNumber](WMS.vwPurchaseOrderDynamicsPOtoAptosPOWithItemNumber.md) | erp.VendorMaster, WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwPurchaseOrderReceiptDBStoDynamics1200XML](WMS.vwPurchaseOrderReceiptDBStoDynamics1200XML.md) | WMS.vwDynamicsPOReceiptFromDBSchenkerASN |
| WMS | [vwPurchaseOrderReceiptsToday](WMS.vwPurchaseOrderReceiptsToday.md) | erp.PurchaseOrderReceipt, wms.ItemMasterProducts, wms.PurchaseOrderReceipt |
| WMS | [vwRecentlyWavedCartons](WMS.vwRecentlyWavedCartons.md) | WM.Orders, WMS.SalesOrderStatusUpdateShipped |
| WMS | [vwReportBearhouseWebStoreInvoiceUpdate](WMS.vwReportBearhouseWebStoreInvoiceUpdate.md) | wms.ModeOfDeliveryWeb, wms.SalesOrderStatusUpdateShipped |
| WMS | [vwSalesOrderStatusUpdateWaved](WMS.vwSalesOrderStatusUpdateWaved.md) | WMS.SalesOrderStatusUpdateWaved |
| WMS | [vwSalesOrderStatusUpdateWaved_All](WMS.vwSalesOrderStatusUpdateWaved_All.md) | WMS.SalesOrderStatusUpdateWaved |
| WMS | [vwShipmentInvoice1200FromWMPOReceipt](WMS.vwShipmentInvoice1200FromWMPOReceipt.md) | erp.VendorMaster, WMS.DynamicsAPILog, WMS.PurchaseOrderMerchToDynamics, WMS.PurchaseOrderReceipt |
| WMS | [vwShipmentInvoice1200FromWMPOReceiptXML](WMS.vwShipmentInvoice1200FromWMPOReceiptXML.md) | WMS.vwShipmentInvoice1200FromWMPOReceipt |
| WMS | [vwStoreShipmentReport](WMS.vwStoreShipmentReport.md) | wms.InboundShipmentLoad, wms.ItemsUOM, wms.ShipmentConfirmAptos, wms.StoreTransferOrderReceipt, WMS.vwStoreShipmentReportLookupUOM, WMS.vwStoreShipmentReportStyles |
| WMS | [vwStoreShipmentReportLookupUOM](WMS.vwStoreShipmentReportLookupUOM.md) | wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| WMS | [vwStoreShipmentReportStyles](WMS.vwStoreShipmentReportStyles.md) | pos.ProductCatalogMasterAttributesStage, wms.ItemMasterProducts, wms.vwItemType |
| WMS | [vwStoreShipmentReportV2](WMS.vwStoreShipmentReportV2.md) | wms.InboundShipmentLoad, wms.ItemsUOM, wms.ShipmentConfirmAptos, wms.StoreTransferOrderReceipt, WMS.vwStoreShipmentReportLookupUOM, WMS.vwStoreShipmentReportStyles |
| WMS | [vwStoreShipmentsSummary](WMS.vwStoreShipmentsSummary.md) | erp.ShipmentInvoice, wms.ShipmentConfirmAptos |
| WMS | [vwStoreShipmentsToDynamicsPOtoSO](WMS.vwStoreShipmentsToDynamicsPOtoSO.md) | erp.WarehouseMaster, WMS.StoreShipmentExport |
| WMS | [vwStoreShipmentsToDynamicsPOtoSO_ONDEMAND](WMS.vwStoreShipmentsToDynamicsPOtoSO_ONDEMAND.md) | erp.WarehouseMaster, WMS.StoreShipmentExport |
| WMS | [vwStoreShipmentsToDynamicsPOtoSOBAK20220801](WMS.vwStoreShipmentsToDynamicsPOtoSOBAK20220801.md) | erp.WarehouseMaster, WMS.StoreShipmentExport |
| WMS | [vwStoreShipmentsToDynamicsTO](WMS.vwStoreShipmentsToDynamicsTO.md) | WMS.StoreShipmentExport |
| WMS | [vwStoreShipmentsToDynamicsTOBAK20220801](WMS.vwStoreShipmentsToDynamicsTOBAK20220801.md) | WMS.StoreShipmentExport |
| WMS | [vwStoreShipmentsToDynamicsTOCheck](WMS.vwStoreShipmentsToDynamicsTOCheck.md) | wms.DynamicsAPILog, wms.DynamicsPackageAPILog, WMS.StoreShipmentExport |
| WMS | [vwUKItemMasterWarehouse](WMS.vwUKItemMasterWarehouse.md) | wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsNMFC, wms.ItemsUOM, wms.vwItemType |
| WMS | [vwUKItemsUSWeight](WMS.vwUKItemsUSWeight.md) | wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| WMS | [vwUKItemsWithoutUSWeight](WMS.vwUKItemsWithoutUSWeight.md) | dbo.po, dbo.po_line, dbo.sku, dbo.style, dbo.upc, erp.PurchaseOrderLines, wms.ItemMaster, wms.ItemMasterProducts |
| WMS | [vwUKItemsWithoutUSWeightV2](WMS.vwUKItemsWithoutUSWeightV2.md) | dbo.ClipperInventoryTC, dbo.po, dbo.po_line, dbo.sku, dbo.style, dbo.upc, erp.PurchaseOrderLines, wms.ItemMaster, wms.ItemMasterProducts, wms.ItemsUOM |
| WMS | [vwUKItemsWithoutUSWeightV3](WMS.vwUKItemsWithoutUSWeightV3.md) | azure.vwMerchOnOrder, azure.vwProducts, dbo.ClipperInventoryTC, dbo.date_dim, dbo.store_dim, erp.PurchaseOrderLines, Reporting.UKItemCostUom, wms.ItemMaster |
| WMS | [vwUKItemsWithoutUSWeightV4](WMS.vwUKItemsWithoutUSWeightV4.md) | azure.vwMerchOnOrder, azure.vwProducts, dbo.ClipperInventoryTC, dbo.date_dim, dbo.store_dim, erp.PurchaseOrderLines, Reporting.UKItemCostUom, wms.ItemMaster, WMS.vwItemsWithoutHTS_COO_Factory_UK |
| WMS | [vwUKItemsWithoutUSWeightV5](WMS.vwUKItemsWithoutUSWeightV5.md) | azure.vwMerchOnOrder, azure.vwProducts, dbo.ClipperInventoryTC, dbo.date_dim, dbo.store_dim, erp.PurchaseOrderLines, Reporting.UKItemCostUom, wms.ItemMaster, WMS.vwItemsWithoutHTS_COO_Factory_UK |
| WMS | [vwValidatePOAptosToDynamics](WMS.vwValidatePOAptosToDynamics.md) | erp.VendorMaster, WMS.PurchaseOrderMerchToDynamics |
| WMS | [vwWarehouseOnOrder](WMS.vwWarehouseOnOrder.md) | WMS.NonWarehouseOnHand, wms.WarehouseOnHand, wms.WarehouseOnHand9980 |
| WMS | [vwWaveLastThirtyMinutes](WMS.vwWaveLastThirtyMinutes.md) | wms.CartonsSummaryToHA |
| WMS | [vwWebOrderSalesOrderLookup](WMS.vwWebOrderSalesOrderLookup.md) | wms.DynamicsAPILog |
