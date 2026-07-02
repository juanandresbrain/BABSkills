# ERP.ItemLoadtoD365

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ITEMNUMBER | nvarchar | 14 | 1 |  |  |  |
| INVENTORYUNITSYMBOL | varchar | 2 | 1 |  |  |  |
| ITEMMODELGROUPID | varchar | 7 | 1 |  |  |  |
| PRODUCTDESCRIPTION | nvarchar | 240 | 1 |  |  |  |
| PRODUCTGROUPID | varchar | 11 | 1 |  |  |  |
| PRODUCTNAME | nvarchar | 240 | 1 |  |  |  |
| PRODUCTNUMBER | nvarchar | 14 | 1 |  |  |  |
| PRODUCTTYPE | varchar | 4 | 1 |  |  |  |
| PURCHASEPRICE | numeric | 17 | 1 |  |  |  |
| PURCHASEUNITSYMBOL | varchar | 2 | 1 |  |  |  |
| RETAILPRODUCTCATEGORYNAME | nvarchar | 80 | 1 |  |  |  |
| SALESUNITSYMBOL | varchar | 2 | 1 |  |  |  |
| SEARCHNAME | nvarchar | 240 | 1 |  |  |  |
| STORAGEDIMENSIONGROUPNAME | varchar | 6 | 1 |  |  |  |
| UNITCONVERSIONSEQUENCEGROUPID | varchar | 10 | 1 |  |  |  |
| UNITCOST | numeric | 17 | 1 |  |  |  |
| UNITCOSTQUANTITY | numeric | 17 | 1 |  |  |  |
| ISCATCHWEIGHTPRODUCT | varchar | 2 | 1 |  |  |  |
| ISPRODUCTKIT | varchar | 2 | 1 |  |  |  |
| PRODUCTSUBTYPE | varchar | 8 | 1 |  |  |  |
| TRACKINGDIMENSIONGROUPNAME | varchar | 4 | 1 |  |  |  |
| SALESPRICE | numeric | 17 | 1 |  |  |  |
| ISPURCHASEPRICEAUTOMATICALLYUPDATED | varchar | 3 | 1 |  |  |  |
| HarmonizedSystemCode | varchar | 15 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| WarehouseMobileDeviceDescriptionLine2 | nvarchar | 240 | 1 |  |  |  |
| AreTransportationManagementProcessesEnabled | nvarchar | 6 | 1 |  |  |  |
| OriginCountryRegionId | nvarchar | 40 | 1 |  |  |  |
| PropertyID | nvarchar | 40 | 1 |  |  |  |
| ReservationHierarchyName | nvarchar | 12 | 1 |  |  |  |
| NMFCCode | nvarchar | 20 | 1 |  |  |  |
| ProductSearchName | nvarchar | 240 | 1 |  |  |  |
| ServiceItem | int | 4 | 1 |  |  |  |
| UPC | varchar | 14 | 1 |  |  |  |
| ItemGroup | varchar | 9 | 1 |  |  |  |
| HierarchyGroup | nvarchar | 126 | 1 |  |  |  |
| ColorDescription | nvarchar | 40 | 1 |  |  |  |
| VendorProductDescription | nvarchar | 240 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spItemLoadReleasedProductCreationXML](../../StoredProcedures/IntegrationStaging/ERP.spItemLoadReleasedProductCreationXML.md)
- [IntegrationStaging: ERP.spItemLoadReleasedProductsXML](../../StoredProcedures/IntegrationStaging/ERP.spItemLoadReleasedProductsXML.md)
- [IntegrationStaging: ERP.spMergeItemLoadtoD365](../../StoredProcedures/IntegrationStaging/ERP.spMergeItemLoadtoD365.md)
- [IntegrationStaging: ERP.spMergeItemLoadtoD365BAK20220801](../../StoredProcedures/IntegrationStaging/ERP.spMergeItemLoadtoD365BAK20220801.md)
- [IntegrationStaging: ERP.spMergeItemLoadtoD365BAK20231113](../../StoredProcedures/IntegrationStaging/ERP.spMergeItemLoadtoD365BAK20231113.md)
- [IntegrationStaging: ERP.spOutputItemLoadxml](../../StoredProcedures/IntegrationStaging/ERP.spOutputItemLoadxml.md)
- [IntegrationStaging: WMS.spQueryItemCreateEcoResProductCategoryAssignmentXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateEcoResProductCategoryAssignmentXML.md)
- [IntegrationStaging: WMS.spQueryItemCreateEcoResProductSpecificUOMXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateEcoResProductSpecificUOMXML.md)
- [IntegrationStaging: WMS.spQueryItemCreateEcoResProductV2XML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateEcoResProductV2XML.md)
- [IntegrationStaging: WMS.spQueryItemCreateEcoResReleasedProductV2XML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateEcoResReleasedProductV2XML.md)
- [IntegrationStaging: WMS.spQueryItemCreatePreStage](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreatePreStage.md)
- [IntegrationStaging: WMS.spQueryItemCreateVendorProdDescXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateVendorProdDescXML.md)
- [IntegrationStaging: WMS.spQueryItemCreateVendorXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateVendorXML.md)
- [IntegrationStaging: WMS.spQueryItemCreateXMLBAK20230327](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateXMLBAK20230327.md)
- [IntegrationStaging: WMS.spQueryItemCreateXMLBAK20231113](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateXMLBAK20231113.md)
- [IntegrationStaging: WMS.spQueryItemCreateXMLPreRetailInventory20221027](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateXMLPreRetailInventory20221027.md)
- [IntegrationStaging: WMS.spQueryItemUPCXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemUPCXML.md)

