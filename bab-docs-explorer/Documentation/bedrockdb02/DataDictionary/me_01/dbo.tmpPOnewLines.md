# dbo.tmpPOnewLines

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProjID | varchar | 6 | 1 |  |  |  |
| PurchaseOrder | varchar | 20 | 1 |  |  |  |
| PurposeCode | varchar | 10 | 1 |  |  |  |
| Division | varchar | 1 | 1 |  |  |  |
| Department | varchar | 8 | 1 |  |  |  |
| Buyer | varchar | 1 | 1 |  |  |  |
| SupplierName | varchar | 50 | 1 |  |  |  |
| SupplierCode | varchar | 20 | 1 |  |  |  |
| SupplierAddress1 | varchar | 1 | 1 |  |  |  |
| SupplierAddress2 | varchar | 1 | 1 |  |  |  |
| SupplierAddress3 | varchar | 1 | 1 |  |  |  |
| SupplierAddress4 | varchar | 1 | 1 |  |  |  |
| UNLOCCodeValue | varchar | 1 | 1 |  |  |  |
| ScheduleKCode1 | varchar | 1 | 1 |  |  |  |
| SupplierCity | varchar | 1 | 1 |  |  |  |
| SupplierState | varchar | 1 | 1 |  |  |  |
| SupplierCountry | varchar | 1 | 1 |  |  |  |
| SupplierPostal | varchar | 1 | 1 |  |  |  |
| OrderPaymentTerms | varchar | 3 | 1 |  |  |  |
| FreightPaymentTerms | varchar | 7 | 1 |  |  |  |
| OrderDate | varchar | 30 | 1 |  |  |  |
| PORef1 | varchar | 20 | 1 |  |  |  |
| PORef2 | varchar | 1 | 1 |  |  |  |
| PORef3 | varchar | 1 | 1 |  |  |  |
| ShipToName | varchar | 60 | 1 |  |  |  |
| ShipToCode | varchar | 20 | 1 |  |  |  |
| ShipToEmail | varchar | 1 | 1 |  |  |  |
| ShipToAddress1 | varchar | 1 | 1 |  |  |  |
| ShipToAddress2 | varchar | 1 | 1 |  |  |  |
| ShipToAddress3 | varchar | 1 | 1 |  |  |  |
| ShiptoAddress4 | varchar | 1 | 1 |  |  |  |
| UNLOCCode1 | varchar | 1 | 1 |  |  |  |
| ScheduleDorKCode | varchar | 1 | 1 |  |  |  |
| ShipToCountry | varchar | 1 | 1 |  |  |  |
| ShipToCity | varchar | 1 | 1 |  |  |  |
| ShipToState | varchar | 1 | 1 |  |  |  |
| ShipToZipCode | varchar | 1 | 1 |  |  |  |
| FactoryName | varchar | 30 | 1 |  |  |  |
| FactoryCode | varchar | 6 | 1 |  |  |  |
| FactoryAddress1 | varchar | 1 | 1 |  |  |  |
| FactoryAddress2 | varchar | 1 | 1 |  |  |  |
| FactoryAddress3 | varchar | 1 | 1 |  |  |  |
| FactoryAddress4 | varchar | 1 | 1 |  |  |  |
| UNLOCCode2 | varchar | 1 | 1 |  |  |  |
| ScheduleKCode2 | varchar | 1 | 1 |  |  |  |
| FactoryCity | varchar | 1 | 1 |  |  |  |
| FactoryState | varchar | 1 | 1 |  |  |  |
| FactoryCountry | varchar | 1 | 1 |  |  |  |
| FactoryPostal | varchar | 1 | 1 |  |  |  |
| ShipWindowStart | varchar | 30 | 1 |  |  |  |
| ShipWindowEnd | varchar | 30 | 1 |  |  |  |
| ShipWindowCancelDate | varchar | 1 | 1 |  |  |  |
| ProductDetailID | int | 4 | 1 |  |  |  |
| ProductDetailProductCode | varchar | 20 | 1 |  |  |  |
| ProductDetailProductDesc | varchar | 120 | 1 |  |  |  |
| ProductDetailHTS | varchar | 30 | 1 |  |  |  |
| ProductDetailOrderQuantity | decimal | 17 | 1 |  |  |  |
| QuantityUOM | varchar | 2 | 1 |  |  |  |
| UnitCost | decimal | 17 | 1 |  |  |  |
| Mode | varchar | 5 | 1 |  |  |  |
| ProductDetailMasterPackQty | int | 4 | 1 |  |  |  |
| ProductDetailNoOfPackages | varchar | 1 | 1 |  |  |  |
| ProductDetailInnerPackQty | int | 4 | 1 |  |  |  |
| ProductDetailTotalVolume | varchar | 1 | 1 |  |  |  |
| ProductDetailTotalWeight | varchar | 1 | 1 |  |  |  |
| ProductDetailProductPriority | varchar | 1 | 1 |  |  |  |
| ProductDetailManufacturerID | varchar | 1 | 1 |  |  |  |
| ProductDetailProductRef | varchar | 1 | 1 |  |  |  |
| ProductDetailProductRef2 | varchar | 1 | 1 |  |  |  |
| ProductDetailProductRef3 | varchar | 1 | 1 |  |  |  |
| ProductDetailProductRef4 | varchar | 1 | 1 |  |  |  |
| ProductDetailProductRef5 | varchar | 1 | 1 |  |  |  |
| OriginCountry | nvarchar | 510 | 1 |  |  |  |
| OriginCity | nvarchar | 510 | 1 |  |  |  |
| FinalDestination | varchar | 1 | 1 |  |  |  |
| POETA | varchar | 1 | 1 |  |  |  |
| ProductDate1 | varchar | 30 | 1 |  |  |  |
| ProductDate2 | varchar | 1 | 1 |  |  |  |
| Consolidator | varchar | 1 | 1 |  |  |  |
| Broker | varchar | 1 | 1 |  |  |  |
| Currency | varchar | 1 | 1 |  |  |  |
| SKUNumber | varchar | 1 | 1 |  |  |  |
| Size | varchar | 1 | 1 |  |  |  |
| Color | varchar | 8 | 1 |  |  |  |
| LineEndIndicator | varchar | 1 | 1 |  |  |  |

