# dbo.tmpHoldDBSchenkerPO_20120906

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProjID | varchar | 6 | 0 |  |  |  |
| PurchaseOrder | varchar | 20 | 0 |  |  |  |
| PurposeCode | varchar | 7 | 0 |  |  |  |
| Division | varchar | 1 | 0 |  |  |  |
| Department | varchar | 8 | 1 |  |  |  |
| Buyer | varchar | 1 | 0 |  |  |  |
| SupplierName | varchar | 50 | 0 |  |  |  |
| SupplierCode | varchar | 20 | 0 |  |  |  |
| SupplierAddress1 | varchar | 1 | 0 |  |  |  |
| SupplierAddress2 | varchar | 1 | 0 |  |  |  |
| SupplierAddress3 | varchar | 1 | 0 |  |  |  |
| SupplierAddress4 | varchar | 1 | 0 |  |  |  |
| UNLOCCodeValue | varchar | 1 | 0 |  |  |  |
| ScheduleKCode1 | varchar | 1 | 0 |  |  |  |
| SupplierCity | varchar | 1 | 0 |  |  |  |
| SupplierState | varchar | 1 | 0 |  |  |  |
| SupplierCountry | varchar | 1 | 0 |  |  |  |
| SupplierPostal | varchar | 1 | 0 |  |  |  |
| OrderPaymentTerms | varchar | 3 | 0 |  |  |  |
| FreightPaymentTerms | varchar | 7 | 0 |  |  |  |
| OrderDate | varchar | 30 | 1 |  |  |  |
| PORef1 | varchar | 20 | 1 |  |  |  |
| PORef2 | varchar | 1 | 0 |  |  |  |
| PORef3 | varchar | 1 | 0 |  |  |  |
| ShipToName | varchar | 60 | 1 |  |  |  |
| ShipToCode | varchar | 20 | 1 |  |  |  |
| ShipToEmail | varchar | 1 | 0 |  |  |  |
| ShipToAddress1 | varchar | 1 | 0 |  |  |  |
| ShipToAddress2 | varchar | 1 | 0 |  |  |  |
| ShipToAddress3 | varchar | 1 | 0 |  |  |  |
| ShiptoAddress4 | varchar | 1 | 0 |  |  |  |
| UNLOCCode1 | varchar | 1 | 0 |  |  |  |
| ScheduleDorKCode | varchar | 1 | 0 |  |  |  |
| ShipToCountry | varchar | 1 | 0 |  |  |  |
| ShipToCity | varchar | 1 | 0 |  |  |  |
| ShipToState | varchar | 1 | 0 |  |  |  |
| ShipToZipCode | varchar | 1 | 0 |  |  |  |
| FactoryName | varchar | 30 | 0 |  |  |  |
| FactoryCode | varchar | 6 | 0 |  |  |  |
| FactoryAddress1 | varchar | 1 | 0 |  |  |  |
| FactoryAddress2 | varchar | 1 | 0 |  |  |  |
| FactoryAddress3 | varchar | 1 | 0 |  |  |  |
| FactoryAddress4 | varchar | 1 | 0 |  |  |  |
| UNLOCCode2 | varchar | 1 | 0 |  |  |  |
| ScheduleKCode2 | varchar | 1 | 0 |  |  |  |
| FactoryCity | varchar | 1 | 0 |  |  |  |
| FactoryState | varchar | 1 | 0 |  |  |  |
| FactoryCountry | varchar | 1 | 0 |  |  |  |
| FactoryPostal | varchar | 1 | 0 |  |  |  |
| ShipWindowStart | varchar | 30 | 1 |  |  |  |
| ShipWindowEnd | varchar | 30 | 1 |  |  |  |
| ShipWindowCancelDate | varchar | 1 | 0 |  |  |  |
| ProductDetailID | int | 4 | 0 |  |  |  |
| ProductDetailProductCode | varchar | 20 | 0 |  |  |  |
| ProductDetailProductDesc | varchar | 120 | 1 |  |  |  |
| ProductDetailHTS | varchar | 30 | 1 |  |  |  |
| ProductDetailOrderQuantity | decimal | 17 | 1 |  |  |  |
| QuantityUOM | varchar | 2 | 0 |  |  |  |
| UnitCost | decimal | 17 | 1 |  |  |  |
| Mode | varchar | 5 | 0 |  |  |  |
| ProductDetailMasterPackQty | int | 4 | 1 |  |  |  |
| ProductDetailNoOfPackages | varchar | 1 | 0 |  |  |  |
| ProductDetailInnerPackQty | int | 4 | 1 |  |  |  |
| ProductDetailTotalVolume | varchar | 1 | 0 |  |  |  |
| ProductDetailTotalWeight | varchar | 1 | 0 |  |  |  |
| ProductDetailProductPriority | varchar | 1 | 0 |  |  |  |
| ProductDetailManufacturerID | varchar | 1 | 0 |  |  |  |
| ProductDetailProductRef | varchar | 1 | 0 |  |  |  |
| ProductDetailProductRef2 | varchar | 1 | 0 |  |  |  |
| ProductDetailProductRef3 | varchar | 1 | 0 |  |  |  |
| ProductDetailProductRef4 | varchar | 1 | 0 |  |  |  |
| ProductDetailProductRef5 | varchar | 1 | 0 |  |  |  |
| OriginCountry | nvarchar | 510 | 0 |  |  |  |
| OriginCity | nvarchar | 510 | 0 |  |  |  |
| FinalDestination | varchar | 1 | 0 |  |  |  |
| POETA | varchar | 1 | 0 |  |  |  |
| ProductDate1 | varchar | 30 | 1 |  |  |  |
| ProductDate2 | varchar | 1 | 0 |  |  |  |
| Consolidator | varchar | 1 | 0 |  |  |  |
| Broker | varchar | 1 | 0 |  |  |  |
| Currency | varchar | 1 | 0 |  |  |  |
| SKUNumber | varchar | 1 | 0 |  |  |  |
| Size | varchar | 1 | 0 |  |  |  |
| Color | varchar | 8 | 1 |  |  |  |
| LineEndIndicator | varchar | 1 | 0 |  |  |  |

