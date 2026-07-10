# dbo.spMergeWebOrderInboundDemandTrackingFacts

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeWebOrderInboundDemandTrackingFacts"]
    vwWebOrderInboundDemandTrackingStageForAzure(["vwWebOrderInboundDemandTrackingStageForAzure"]) --> SP
    dbo_WebOrderInboundDemandTrackingFacts(["dbo.WebOrderInboundDemandTrackingFacts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| vwWebOrderInboundDemandTrackingStageForAzure |
| dbo.WebOrderInboundDemandTrackingFacts |

## Stored Procedure Code

```sql
CREATE proc spMergeWebOrderInboundDemandTrackingFacts
as
set nocount on

--delete x 
--from dw.dbo.WebOrderInboundDemandTrackingFacts x
--where x.OrderDate <= cast(getdate()-15 as date)
;
Merge into dw.dbo.WebOrderInboundDemandTrackingFacts as target
using vwWebOrderInboundDemandTrackingStageForAzure as source
on target.OrderNumber=source.OrderNumber
and target.DeckSKU=source.DeckSKU
and isnull(target.OrderItemGrouping,99999)=isnull(source.OrderItemGrouping,99999)
when not matched by target
then insert
	(
		OrderDate,	
		OrderNumber,	
		DeckSku,	
		ItemDescription,	
		KeyStory,	
		GrossProductSales,	
		ProductDiscounts,	
		NetProductSales,	
		GrossShippingRevenue,	
		ShippingDiscounts,	
		NetShippingRevenue,	
		OrderUnits,	
		PartyEGiftCardUnits,	
		PartyEGiftCardValue,	
		UpsellEGiftCardUnits,	
		UpsellEGiftCardValue,	
		EGiftCardUnits,	
		EGiftCardValue,	
		PhysicalGiftCardUnits,	
		PhysicalGiftCardValue,	
		DonationUnits,	
		DonationValue,	
		CondoUnits,	
		GiftBoxUnits,	
		isGiftOrder,	
		GiftOrderUnits,	
		GiftOrderValue,	
		ProductCost,	
		isGiftCard,	
		isPhysicalGiftCard,	
		isEGiftCard,	
		isPartyEGiftCard,	
		isUpsellEGiftCard,	
		isDonation,	
		isCondo,	
		isGiftBox,	
		hasGiftMessage,	
		isBundleMaster,	
		isStuffed,	
		isUnstuffed,	
		isDressed,	
		isUndressed,	
		ChainAverageOnHandCost,	
		ChainAverageOnHandCostGBP,	
		isUS,	
		isUK,	
		isShipFromStore,	
		isBillingVShippingDiff,	
		CurrentStatus,	
		PendingStatusDate,	
		WavedStatusDate,	
		ShippedCompletedStatusDate,	
		LastStatusDate,	
		DaysBetweenWavedAndShipped,	
		DaysSinceWavedStatus,	
		DaysBetweenPendingAndWaved,	
		DaysBetweenPendingAndShipped,	
		DaysSincePendingStatus,	
		DaysSinceLastStatus,	
		InsertDate,	
		Channel,	
		OrderItemGrouping
	)
values
	(
		source.OrderDate,	
		source.OrderNumber,	
		source.DeckSku,	
		source.ItemDescription,	
		source.KeyStory,	
		source.GrossProductSales,	
		source.ProductDiscounts,	
		source.NetProductSales,	
		source.GrossShippingRevenue,	
		source.ShippingDiscounts,	
		source.NetShippingRevenue,	
		source.OrderUnits,	
		source.PartyEGiftCardUnits,	
		source.PartyEGiftCardValue,	
		source.UpsellEGiftCardUnits,	
		source.UpsellEGiftCardValue,	
		source.EGiftCardUnits,	
		source.EGiftCardValue,	
		source.PhysicalGiftCardUnits,	
		source.PhysicalGiftCardValue,	
		source.DonationUnits,	
		source.DonationValue,	
		source.CondoUnits,	
		source.GiftBoxUnits,	
		source.isGiftOrder,	
		source.GiftOrderUnits,	
		source.GiftOrderSales,	
		source.ProductCost,	
		source.isGiftCard,	
		source.isPhysicalGiftCard,	
		source.isEGiftCard,	
		source.isPartyEGiftCard,	
		source.isUpsellEGiftCard,	
		source.isDonation,	
		source.isCondo,	
		source.isGiftBox,	
		source.hasGiftMessage,	
		source.isBundleMaster,	
		source.isStuffed,	
		source.isUnstuffed,	
		source.isDressed,	
		source.isUndressed,	
		source.ChainAverageOnHandCost,	
		source.ChainAverageOnHandCostGBP,	
		source.isUS,	
		source.isUK,	
		source.isShipFromStore,	
		source.isBillingVShippingDiff,	
		source.CurrentStatus,	
		source.PendingStatusDate,	
		source.WavedStatusDate,	
		source.ShippedCompletedStatusDate,	
		source.LastStatusDate,	
		source.DaysBetweenWavedAndShipped,	
		source.DaysSinceWavedStatus,	
		source.DaysBetweenPendingAndWaved,	
		source.DaysBetweenPendingAndShipped,	
		source.DaysSincePendingStatus,	
		source.DaysSinceLastStatus,	
		source.InsertDate,	
		source.Channel,	
		source.OrderItemGrouping
	)
;
```

