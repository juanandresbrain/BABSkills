# dbo.WebOrderInboundDemandTrackingStageV2

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 50 | 1 |  |  |  |
| DeckSku | varchar | 100 | 1 |  |  |  |
| ItemDescription | varchar | 255 | 1 |  |  |  |
| GrossProductSales | numeric | 9 | 1 |  |  |  |
| ProductDiscounts | numeric | 9 | 1 |  |  |  |
| NetProductSales | numeric | 9 | 1 |  |  |  |
| GiftCardValue | numeric | 9 | 1 |  |  |  |
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
| KeyStory | nvarchar | 60 | 1 |  |  |  |
| ChainAverageOnHandCost | numeric | 9 | 1 |  |  |  |
| ChainAverageOnHandCostGBP | numeric | 9 | 1 |  |  |  |
| isUS | int | 4 | 1 |  |  |  |
| isUK | int | 4 | 1 |  |  |  |
| isShipFromStore | int | 4 | 1 |  |  |  |
| isBillingVShippingDiff | int | 4 | 1 |  |  |  |
| OrderShippingAmount | money | 8 | 1 |  |  |  |
| OrderShippingDiscount | money | 8 | 1 |  |  |  |
| CurrentStatus | varchar | 25 | 1 |  |  |  |
| PendingStatusDate | datetime | 8 | 1 |  |  |  |
| WavedStatusDate | datetime | 8 | 1 |  |  |  |
| ShippedCompletedStatusDate | datetime | 8 | 1 |  |  |  |
| Channel | varchar | 100 | 1 |  |  |  |
| OrderItemGrouping | int | 4 | 1 |  |  |  |
