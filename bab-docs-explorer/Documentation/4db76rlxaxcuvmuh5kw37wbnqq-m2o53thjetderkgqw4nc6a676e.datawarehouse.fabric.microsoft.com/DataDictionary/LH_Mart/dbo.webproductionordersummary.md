# dbo.webproductionordersummary

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductionOrderId | int | 4 | 1 |  |  |  |
| ProductionOrderNumber | varchar | 8000 | 1 |  |  |  |
| ProductionOrderSubTotal | decimal | 9 | 1 |  |  |  |
| ProductionOrderShippingAndHandling | decimal | 9 | 1 |  |  |  |
| ProductionOrderPromoCode | varchar | 8000 | 1 |  |  |  |
| ProductionOrderPromoDiscount | decimal | 9 | 1 |  |  |  |
| ProductionOrderPromoDescription | varchar | 8000 | 1 |  |  |  |
| ProductionOrderBearBucksNumber | varchar | 8000 | 1 |  |  |  |
| ProductionOrderTotal | decimal | 9 | 1 |  |  |  |
| ProductionOrderSpecialInstructions | varchar | 8000 | 1 |  |  |  |
| ProductionOrderGiftMessage | varchar | 8000 | 1 |  |  |  |
| ProductionOrderDateTimeCreated | datetime2 | 8 | 1 |  |  |  |
| ProductionOrderDeferredShipDate | datetime2 | 8 | 1 |  |  |  |
| ProductionOrderDateTimeShipped | datetime2 | 8 | 1 |  |  |  |
| ProductionOrderShippingMethod | varchar | 8000 | 1 |  |  |  |
| ProductionOrderTrackingNumber | varchar | 8000 | 1 |  |  |  |
| ProductionOrderBillingStateProvince | varchar | 8000 | 1 |  |  |  |
| ProductionOrderBillingZipPostalCode | varchar | 8000 | 1 |  |  |  |
| ProductionOrderBillingCountry | varchar | 8000 | 1 |  |  |  |
| ProductionOrderShippingStateProvince | varchar | 8000 | 1 |  |  |  |
| ProductionOrderShippingZipPostalCode | varchar | 8000 | 1 |  |  |  |
| ProductionOrderShippingCountry | varchar | 8000 | 1 |  |  |  |
| ProductionOrderIsWillCall | bit | 1 | 1 |  |  |  |
| ProductionOrderIsLoyaltyMember | bit | 1 | 1 |  |  |  |
| ProductionOrderLoyaltyNumber | varchar | 8000 | 1 |  |  |  |
| ProductionOrderIsRush | bit | 1 | 1 |  |  |  |
| ProductionOrderWebOrderStatus | varchar | 8000 | 1 |  |  |  |
| ProductionOrderCatalogName | varchar | 8000 | 1 |  |  |  |
| ProductionOrderNumberOfPackages | int | 4 | 1 |  |  |  |
| ProductionOrderWebCartOrderId | int | 4 | 1 |  |  |  |
| ProductionOrderWebCartUpdateMsgSent | int | 4 | 1 |  |  |  |
| ProductionOrderSiteCode | varchar | 8000 | 1 |  |  |  |
| ProductionOrderBearBuilderId | varchar | 8000 | 1 |  |  |  |
| ProductionOrderBuyStuffStamps | int | 4 | 1 |  |  |  |
| ProductionOrderActuallShippingCost | decimal | 9 | 1 |  |  |  |
| ProductionOrderHasShippableProducts | bit | 1 | 1 |  |  |  |
| ProductionOrderWH_version | int | 4 | 1 |  |  |  |
| ProductionOrderReceiptCode | varchar | 8000 | 1 |  |  |  |
| ProductionOrderServerName | varchar | 8000 | 1 |  |  |  |
| ProductionOrderStatusID | int | 4 | 1 |  |  |  |
| StatusDate | datetime2 | 8 | 1 |  |  |  |
| ESReferenceNbr | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
