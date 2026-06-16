# dbo.tmpPrestage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 20 | 1 |  |  |  |
| PRODUCT_NUMBER | nvarchar | 14 | 1 |  |  |  |
| ITEMNUMBER | nvarchar | 14 | 1 |  |  |  |
| PRODUCTNUMBER | nvarchar | 14 | 1 |  |  |  |
| PRODUCTDESCRIPTION | nvarchar | 240 | 1 |  |  |  |
| PRODUCTNAME | nvarchar | 240 | 1 |  |  |  |
| SEARCHNAME | nvarchar | 240 | 0 |  |  |  |
| HARMONIZEDSYSTEMCODE | varchar | 15 | 0 |  |  |  |
| ORIGINCOUNTRYREGIONID | nvarchar | 40 | 1 |  |  |  |
| PRODUCTCATEGORYNAME | nvarchar | 126 | 1 |  |  |  |
| PRODUCTCATEGORYHIERARCHYNAME | varchar | 24 | 0 |  |  |  |
| UNDERDELIVERYPCT | varchar | 3 | 0 |  |  |  |
| PROPERTYID | varchar | 5 | 0 |  |  |  |
| OVERDELIVERYPCT | varchar | 1 | 0 |  |  |  |
| ITEMGROUPID | varchar | 9 | 1 |  |  |  |
| PRODUCTTYPE | varchar | 1 | 0 |  |  |  |
| PRODUCTSUBTYPE | varchar | 1 | 0 |  |  |  |
| PRODUCTSEARCHNAME | nvarchar | 200 | 1 |  |  |  |
| TRACKINGDIMENSIONGROUPNAME | varchar | 4 | 1 |  |  |  |
| STORAGEDIMENSIONGROUPNAME | varchar | 6 | 0 |  |  |  |
| UNITCOSTQUANTITY | float | 8 | 1 |  |  |  |
| UNITCOST | float | 8 | 1 |  |  |  |
| SALESUNITSYMBOL | varchar | 2 | 1 |  |  |  |
| SALESUNDERDELIVERYPERCENTAGE | int | 4 | 1 |  |  |  |
| SALESPRICEQUANTITY | float | 8 | 1 |  |  |  |
| SALESPRICE | float | 8 | 1 |  |  |  |
| SALESOVERDELIVERYPERCENTAGE | int | 4 | 1 |  |  |  |
| PURCHASEUNITSYMBOL | varchar | 2 | 1 |  |  |  |
| PURCHASEUNDERDELIVERYPERCENTAGE | int | 4 | 1 |  |  |  |
| PURCHASEPRICEQUANTITY | float | 8 | 1 |  |  |  |
| PURCHASEPRICE | float | 8 | 1 |  |  |  |
| PURCHASEOVERDELIVERYPERCENTAGE | int | 4 | 1 |  |  |  |
| ITEMMODELGROUPID | varchar | 7 | 1 |  |  |  |
| INVENTORYUNITSYMBOL | varchar | 2 | 1 |  |  |  |
| ARETRANSPORTATIONMANAGEMENTPROCESSESENABLED | int | 4 | 1 |  |  |  |
| NMFCCODE | varchar | 5 | 1 |  |  |  |
| ISPRODUCTKIT | int | 4 | 1 |  |  |  |
| UNITCONVERSIONSEQUENCEGROUPID | varchar | 10 | 1 |  |  |  |
| WAREHOUSEMOBILEDEVICEDESCRIPTIONLINE2 | varchar | 3 | 0 |  |  |  |
| PRODUCTGROUPID | varchar | 10 | 1 |  |  |  |
| INVENTORYRESERVATIONHIERARCHYNAME | varchar | 10 | 1 |  |  |  |
| COLORDESCRIPTION | nvarchar | 40 | 1 |  |  |  |
| APPROVEDVENDORCHECKMETHOD | varchar | 12 | 0 |  |  |  |
| ServiceItem | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spQueryItemCreateEcoResProductCategoryAssignmentXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateEcoResProductCategoryAssignmentXML.md)
- [IntegrationStaging: WMS.spQueryItemCreateEcoResProductV2XML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateEcoResProductV2XML.md)
- [IntegrationStaging: WMS.spQueryItemCreateEcoResReleasedProductV2XML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateEcoResReleasedProductV2XML.md)
- [IntegrationStaging: WMS.spQueryItemCreateVendorProdDescXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateVendorProdDescXML.md)
- [IntegrationStaging: WMS.spQueryItemCreateVendorXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateVendorXML.md)

