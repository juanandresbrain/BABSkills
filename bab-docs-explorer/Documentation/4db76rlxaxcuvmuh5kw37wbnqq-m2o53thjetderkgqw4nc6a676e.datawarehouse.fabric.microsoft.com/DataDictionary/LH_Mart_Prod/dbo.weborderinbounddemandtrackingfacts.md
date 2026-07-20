# dbo.weborderinbounddemandtrackingfacts

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| DeckSku | varchar | 8000 | 1 |  |  |  |
| ItemDescription | varchar | 8000 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| GrossProductSales | decimal | 9 | 1 |  |  |  |
| ProductDiscounts | decimal | 9 | 1 |  |  |  |
| NetProductSales | decimal | 9 | 1 |  |  |  |
| GrossShippingRevenue | decimal | 9 | 1 |  |  |  |
| ShippingDiscounts | decimal | 9 | 1 |  |  |  |
| NetShippingRevenue | decimal | 9 | 1 |  |  |  |
| OrderUnits | int | 4 | 1 |  |  |  |
| PartyEGiftCardUnits | int | 4 | 1 |  |  |  |
| PartyEGiftCardValue | decimal | 9 | 1 |  |  |  |
| UpsellEGiftCardUnits | int | 4 | 1 |  |  |  |
| UpsellEGiftCardValue | decimal | 9 | 1 |  |  |  |
| EGiftCardUnits | int | 4 | 1 |  |  |  |
| EGiftCardValue | decimal | 9 | 1 |  |  |  |
| PhysicalGiftCardUnits | int | 4 | 1 |  |  |  |
| PhysicalGiftCardValue | decimal | 9 | 1 |  |  |  |
| DonationUnits | int | 4 | 1 |  |  |  |
| DonationValue | decimal | 9 | 1 |  |  |  |
| CondoUnits | int | 4 | 1 |  |  |  |
| GiftBoxUnits | int | 4 | 1 |  |  |  |
| isGiftOrder | int | 4 | 1 |  |  |  |
| GiftOrderUnits | int | 4 | 1 |  |  |  |
| GiftOrderValue | decimal | 9 | 1 |  |  |  |
| ProductCost | decimal | 9 | 1 |  |  |  |
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
| ChainAverageOnHandCost | decimal | 9 | 1 |  |  |  |
| ChainAverageOnHandCostGBP | decimal | 9 | 1 |  |  |  |
| isUS | int | 4 | 1 |  |  |  |
| isUK | int | 4 | 1 |  |  |  |
| isShipFromStore | int | 4 | 1 |  |  |  |
| isBillingVShippingDiff | int | 4 | 1 |  |  |  |
| CurrentStatus | varchar | 8000 | 1 |  |  |  |
| PendingStatusDate | datetime2 | 8 | 1 |  |  |  |
| WavedStatusDate | datetime2 | 8 | 1 |  |  |  |
| ShippedCompletedStatusDate | datetime2 | 8 | 1 |  |  |  |
| LastStatusDate | datetime2 | 8 | 1 |  |  |  |
| DaysBetweenWavedAndShipped | int | 4 | 1 |  |  |  |
| DaysSinceWavedStatus | int | 4 | 1 |  |  |  |
| DaysBetweenPendingAndWaved | int | 4 | 1 |  |  |  |
| DaysBetweenPendingAndShipped | int | 4 | 1 |  |  |  |
| DaysSincePendingStatus | int | 4 | 1 |  |  |  |
| DaysSinceLastStatus | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| Channel | varchar | 8000 | 1 |  |  |  |
| OrderItemGrouping | int | 4 | 1 |  |  |  |
