# dbo.weborderinbounddemandtrackingstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| DeckSku | varchar | 8000 | 1 |  |  |  |
| ItemDescription | varchar | 8000 | 1 |  |  |  |
| GrossProductSales | decimal | 9 | 1 |  |  |  |
| ProductDiscounts | decimal | 9 | 1 |  |  |  |
| NetProductSales | decimal | 9 | 1 |  |  |  |
| GiftCardValue | decimal | 9 | 1 |  |  |  |
| isGiftCard | int | 4 | 1 |  |  |  |
| isPhysicalGiftCard | int | 4 | 1 |  |  |  |
| isEGiftCard | int | 4 | 1 |  |  |  |
| isPartyEGiftCard | int | 4 | 1 |  |  |  |
| isUpsellEGiftCard | int | 4 | 1 |  |  |  |
| isDonation | int | 4 | 1 |  |  |  |
| isCondo | int | 4 | 1 |  |  |  |
| isGiftBox | int | 4 | 1 |  |  |  |
| hasGiftMessage | int | 4 | 1 |  |  |  |
| isBundleMaster | int | 4 | 1 |  |  |  |
| isStuffed | int | 4 | 1 |  |  |  |
| isUnstuffed | int | 4 | 1 |  |  |  |
| isDressed | int | 4 | 1 |  |  |  |
| isUndressed | int | 4 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| ChainAverageOnHandCost | decimal | 9 | 1 |  |  |  |
| ChainAverageOnHandCostGBP | decimal | 9 | 1 |  |  |  |
| isUS | int | 4 | 1 |  |  |  |
| isUK | int | 4 | 1 |  |  |  |
| isShipFromStore | int | 4 | 1 |  |  |  |
| isBillingVShippingDiff | int | 4 | 1 |  |  |  |
| OrderShippingAmount | decimal | 9 | 1 |  |  |  |
| OrderShippingDiscount | decimal | 9 | 1 |  |  |  |
| CurrentStatus | varchar | 8000 | 1 |  |  |  |
| PendingStatusDate | datetime2 | 8 | 1 |  |  |  |
| WavedStatusDate | datetime2 | 8 | 1 |  |  |  |
| ShippedCompletedStatusDate | datetime2 | 8 | 1 |  |  |  |
| Channel | varchar | 8000 | 1 |  |  |  |
| OrderItemGrouping | int | 4 | 1 |  |  |  |
