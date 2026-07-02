# dbo.tmpWebProductionOrderSummary

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductionOrderId | int | 4 | 1 |  |  |  |
| ProductionOrderNumber | varchar | 32 | 1 |  |  |  |
| ProductionOrderSubTotal | money | 8 | 1 |  |  |  |
| ProductionOrderShippingAndHandling | money | 8 | 1 |  |  |  |
| ProductionOrderPromoCode | int | 4 | 1 |  |  |  |
| ProductionOrderPromoDiscount | money | 8 | 1 |  |  |  |
| ProductionOrderPromoDescription | int | 4 | 1 |  |  |  |
| ProductionOrderBearBucksNumber | int | 4 | 1 |  |  |  |
| ProductionOrderTotal | money | 8 | 1 |  |  |  |
| ProductionOrderDateTimeCreated | datetime | 8 | 1 |  |  |  |
| ProductionOrderDeferredShipDate | int | 4 | 1 |  |  |  |
| ProductionOrderShippingMethod | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderTrackingNumber | varchar | 50 | 1 |  |  |  |
| ProductionOrderBillingStateProvince | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderBillingZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderBillingCountry | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderShippingStateProvince | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderShippingZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderShippingCountry | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderIsWillCall | int | 4 | 1 |  |  |  |
| ProductionOrderIsLoyaltyMember | int | 4 | 1 |  |  |  |
| ProductionOrderLoyaltyNumber | int | 4 | 1 |  |  |  |
| ProductionOrderIsRush | bit | 1 | 1 |  |  |  |
| ProductionOrderWebOrderStatus | varchar | 50 | 1 |  |  |  |
| ProductionOrderCatalogName | varchar | 32 | 1 |  |  |  |
| ProductionOrderNumberOfPackages | int | 4 | 1 |  |  |  |
| ProductionOrderWebCartOrderId | int | 4 | 1 |  |  |  |
| ProductionOrderWebCartUpdateMsgSent | int | 4 | 1 |  |  |  |
| ProductionOrderSiteCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderBearBuilderId | int | 4 | 1 |  |  |  |
| ProductionOrderBuyStuffStamps | int | 4 | 1 |  |  |  |
| ProductionOrderActuallShippingCost | money | 8 | 1 |  |  |  |
| ProductionOrderHasShippableProducts | bit | 1 | 1 |  |  |  |
| ProductionOrderWH_version | int | 4 | 1 |  |  |  |
| ProductionOrderReceiptCode | int | 4 | 1 |  |  |  |
| ProductionOrderServerName | nvarchar | 100 | 1 |  |  |  |
| OrderStatusID | int | 4 | 1 |  |  |  |
| StatusDate | datetime | 8 | 1 |  |  |  |

