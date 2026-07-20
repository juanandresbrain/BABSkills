# dbo.weborderinbounddemandtrackingfactsv2

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.weborderinbounddemandtrackingfactsv2"]
    dbo_weborderinbounddemandtrackingfactsv2(["dbo.weborderinbounddemandtrackingfactsv2"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.weborderinbounddemandtrackingfactsv2 |

## View Code

```sql
;

CREATE VIEW dbo.weborderinbounddemandtrackingfactsv2 AS SELECT OrderDate, OrderNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS OrderNumber, DeckSku COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS DeckSku, ItemDescription COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ItemDescription, KeyStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS KeyStory, GrossProductSales, ProductDiscounts, NetProductSales, GrossShippingRevenue, ShippingDiscounts, NetShippingRevenue, OrderUnits, PartyEGiftCardUnits, PartyEGiftCardValue, UpsellEGiftCardUnits, UpsellEGiftCardValue, EGiftCardUnits, EGiftCardValue, PhysicalGiftCardUnits, PhysicalGiftCardValue, DonationUnits, DonationValue, CondoUnits, GiftBoxUnits, isGiftOrder, GiftOrderUnits, GiftOrderValue, ProductCost, isGiftCard, isPhysicalGiftCard, isEGiftCard, isPartyEGiftCard, isUpsellEGiftCard, isDonation, isCondo, isGiftBox, hasGiftMessage, isBundleMaster, isStuffed, isUnstuffed, isDressed, isUndressed, ChainAverageOnHandCost, ChainAverageOnHandCostGBP, isUS, isUK, isShipFromStore, isBillingVShippingDiff, CurrentStatus COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS CurrentStatus, PendingStatusDate, WavedStatusDate, ShippedCompletedStatusDate, LastStatusDate, DaysBetweenWavedAndShipped, DaysSinceWavedStatus, DaysBetweenPendingAndWaved, DaysBetweenPendingAndShipped, DaysSincePendingStatus, DaysSinceLastStatus, InsertDate, Channel COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Channel, OrderItemGrouping FROM LH_Mart.dbo.weborderinbounddemandtrackingfactsv2;;
```

