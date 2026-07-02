# WEB.WebOrderFactStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderId | uniqueidentifier | 16 | 0 |  |  |  |
| OrderNumber | varchar | 32 | 0 |  |  |  |
| OrderSubTotal | money | 8 | 0 |  |  |  |
| OrderShippingAndHandling | money | 8 | 0 |  |  |  |
| OrderPromoCode | varchar | 16 | 1 |  |  |  |
| OrderPromoDiscount | money | 8 | 1 |  |  |  |
| OrderPromoDescription | nvarchar | 100 | 1 |  |  |  |
| OrderBearBucksNumber | varchar | 85 | 1 |  |  |  |
| OrderTotal | money | 8 | 0 |  |  |  |
| OrderSpecialInstructions | nvarchar | 3000 | 1 |  |  |  |
| OrderGiftMessage | nvarchar | 3000 | 1 |  |  |  |
| OrderDateTimeCreated | datetime | 8 | 0 |  |  |  |
| OrderDeferredShipDate | datetime | 8 | 1 |  |  |  |
| OrderDateTimeShipped | datetime | 8 | 1 |  |  |  |
| OrderShippingMethod | nvarchar | 100 | 0 |  |  |  |
| OrderTrackingNumber | varchar | 50 | 1 |  |  |  |
| OrderBillingFirstName | nvarchar | 128 | 0 |  |  |  |
| OrderBillingLastName | nvarchar | 128 | 0 |  |  |  |
| OrderBillingEmailAddress | nvarchar | 160 | 1 |  |  |  |
| OrderBillingPhoneNumber | nvarchar | 160 | 0 |  |  |  |
| OrderBillingAddress1 | nvarchar | 160 | 0 |  |  |  |
| OrderBillingAddress2 | nvarchar | 160 | 1 |  |  |  |
| OrderBillingCity | nvarchar | 100 | 0 |  |  |  |
| OrderBillingStateProvince | nvarchar | 100 | 0 |  |  |  |
| OrderBillingZipPostalCode | nvarchar | 40 | 0 |  |  |  |
| OrderBillingCountry | nvarchar | 100 | 0 |  |  |  |
| OrderBillingCompanyName | nvarchar | 128 | 1 |  |  |  |
| OrderShippingFirstName | nvarchar | 128 | 1 |  |  |  |
| OrderShippingLastName | nvarchar | 128 | 1 |  |  |  |
| OrderShippingEmailAddress | nvarchar | 160 | 1 |  |  |  |
| OrderShippingPhoneNumber | nvarchar | 160 | 1 |  |  |  |
| OrderShippingAddress1 | nvarchar | 160 | 1 |  |  |  |
| OrderShippingAddress2 | nvarchar | 160 | 1 |  |  |  |
| OrderShippingCity | nvarchar | 100 | 1 |  |  |  |
| OrderShippingStateProvince | nvarchar | 100 | 1 |  |  |  |
| OrderShippingZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| OrderShippingCountry | nvarchar | 100 | 1 |  |  |  |
| OrderShippingCompanyName | nvarchar | 128 | 1 |  |  |  |
| OrderIsWillCall | bit | 1 | 0 |  |  |  |
| OrderIsLoyaltyMember | bit | 1 | 0 |  |  |  |
| OrderLoyaltyNumber | varchar | 32 | 1 |  |  |  |
| OrderIsRush | bit | 1 | 0 |  |  |  |
| OrderWebOrderStatus | varchar | 50 | 0 |  |  |  |
| OrderCatalogName | varchar | 32 | 0 |  |  |  |
| OrderNumberOfPackages | int | 4 | 1 |  |  |  |
| OrderWebCartOrderId | uniqueidentifier | 16 | 0 |  |  |  |
| OrderWebCartUpdateMsgSent | int | 4 | 0 |  |  |  |
| OrderSiteCode | nvarchar | 40 | 0 |  |  |  |
| OrderBearBuilderId | nvarchar | 100 | 1 |  |  |  |
| OrderBuyStuffStamps | int | 4 | 0 |  |  |  |
| OrderActuallShippingCost | money | 8 | 1 |  |  |  |
| OrderHasShippableProducts | bit | 1 | 0 |  |  |  |
| OrderWH_version | int | 4 | 1 |  |  |  |
| OrderReceiptCode | varchar | 32 | 1 |  |  |  |
| OrderServerName | nvarchar | 100 | 1 |  |  |  |

