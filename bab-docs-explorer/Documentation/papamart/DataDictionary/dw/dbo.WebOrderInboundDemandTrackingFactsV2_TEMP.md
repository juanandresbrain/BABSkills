# dbo.WebOrderInboundDemandTrackingFactsV2_TEMP

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 50 | 1 |  |  |  |
| DeckSku | varchar | 100 | 1 |  |  |  |
| ItemDescription | varchar | 255 | 1 |  |  |  |
| KeyStory | nvarchar | 60 | 1 |  |  |  |
| GrossProductSales | numeric | 9 | 1 |  |  |  |
| ProductDiscounts | numeric | 9 | 1 |  |  |  |
| NetProductSales | numeric | 9 | 1 |  |  |  |
| GrossShippingRevenue | money | 8 | 1 |  |  |  |
| ShippingDiscounts | money | 8 | 1 |  |  |  |
| NetShippingRevenue | money | 8 | 1 |  |  |  |
| OrderUnits | int | 4 | 1 |  |  |  |
| PartyEGiftCardUnits | int | 4 | 1 |  |  |  |
| PartyEGiftCardValue | numeric | 9 | 1 |  |  |  |
| UpsellEGiftCardUnits | int | 4 | 1 |  |  |  |
| UpsellEGiftCardValue | numeric | 9 | 1 |  |  |  |
| EGiftCardUnits | int | 4 | 1 |  |  |  |
| EGiftCardValue | numeric | 9 | 1 |  |  |  |
| PhysicalGiftCardUnits | int | 4 | 1 |  |  |  |
| PhysicalGiftCardValue | numeric | 9 | 1 |  |  |  |
| DonationUnits | int | 4 | 1 |  |  |  |
| DonationValue | numeric | 9 | 1 |  |  |  |
| CondoUnits | int | 4 | 1 |  |  |  |
| GiftBoxUnits | int | 4 | 1 |  |  |  |
| isGiftOrder | int | 4 | 1 |  |  |  |
| GiftOrderUnits | int | 4 | 1 |  |  |  |
| GiftOrderValue | numeric | 9 | 1 |  |  |  |
| ProductCost | numeric | 9 | 1 |  |  |  |
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
| ChainAverageOnHandCost | numeric | 9 | 1 |  |  |  |
| ChainAverageOnHandCostGBP | numeric | 9 | 1 |  |  |  |
| isUS | int | 4 | 1 |  |  |  |
| isUK | int | 4 | 1 |  |  |  |
| isShipFromStore | int | 4 | 1 |  |  |  |
| isBillingVShippingDiff | int | 4 | 1 |  |  |  |
| CurrentStatus | varchar | 25 | 1 |  |  |  |
| PendingStatusDate | datetime | 8 | 1 |  |  |  |
| WavedStatusDate | datetime | 8 | 1 |  |  |  |
| ShippedCompletedStatusDate | datetime | 8 | 1 |  |  |  |
| LastStatusDate | datetime | 8 | 1 |  |  |  |
| DaysBetweenWavedAndShipped | int | 4 | 1 |  |  |  |
| DaysSinceWavedStatus | int | 4 | 1 |  |  |  |
| DaysBetweenPendingAndWaved | int | 4 | 1 |  |  |  |
| DaysBetweenPendingAndShipped | int | 4 | 1 |  |  |  |
| DaysSincePendingStatus | int | 4 | 1 |  |  |  |
| DaysSinceLastStatus | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| Channel | varchar | 100 | 1 |  |  |  |
| OrderItemGrouping | int | 4 | 1 |  |  |  |
