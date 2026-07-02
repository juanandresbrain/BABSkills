# ERP.ItemLoadtoD365BAK20231113

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

