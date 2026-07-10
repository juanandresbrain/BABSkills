# dbo.WebProductionOrderSummary

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductionOrderId | int | 4 | 1 |  |  |  |
| ProductionOrderNumber | varchar | 32 | 1 |  |  |  |
| ProductionOrderSubTotal | money | 8 | 1 |  |  |  |
| ProductionOrderShippingAndHandling | money | 8 | 1 |  |  |  |
| ProductionOrderPromoCode | varchar | 16 | 1 |  |  |  |
| ProductionOrderPromoDiscount | money | 8 | 1 |  |  |  |
| ProductionOrderPromoDescription | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderBearBucksNumber | varchar | 85 | 1 |  |  |  |
| ProductionOrderTotal | money | 8 | 1 |  |  |  |
| ProductionOrderDateTimeCreated | datetime | 8 | 1 |  |  |  |
| ProductionOrderDeferredShipDate | datetime | 8 | 1 |  |  |  |
| ProductionOrderShippingMethod | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderTrackingNumber | varchar | 50 | 1 |  |  |  |
| ProductionOrderBillingStateProvince | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderBillingZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderBillingCountry | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderShippingStateProvince | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderShippingZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderShippingCountry | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderIsWillCall | bit | 1 | 1 |  |  |  |
| ProductionOrderIsLoyaltyMember | bit | 1 | 1 |  |  |  |
| ProductionOrderLoyaltyNumber | varchar | 32 | 1 |  |  |  |
| ProductionOrderIsRush | bit | 1 | 1 |  |  |  |
| ProductionOrderWebOrderStatus | varchar | 50 | 1 |  |  |  |
| ProductionOrderCatalogName | varchar | 32 | 1 |  |  |  |
| ProductionOrderNumberOfPackages | int | 4 | 1 |  |  |  |
| ProductionOrderWebCartOrderId | int | 4 | 1 |  |  |  |
| ProductionOrderWebCartUpdateMsgSent | int | 4 | 1 |  |  |  |
| ProductionOrderSiteCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderBearBuilderId | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderBuyStuffStamps | int | 4 | 1 |  |  |  |
| ProductionOrderActuallShippingCost | money | 8 | 1 |  |  |  |
| ProductionOrderHasShippableProducts | bit | 1 | 1 |  |  |  |
| ProductionOrderWH_version | int | 4 | 1 |  |  |  |
| ProductionOrderReceiptCode | varchar | 32 | 1 |  |  |  |
| ProductionOrderServerName | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderStatusID | int | 4 | 1 |  |  |  |
| StatusDate | datetime | 8 | 1 |  |  |  |
| ESReferenceNbr | varchar | 19 | 1 |  |  |  |
