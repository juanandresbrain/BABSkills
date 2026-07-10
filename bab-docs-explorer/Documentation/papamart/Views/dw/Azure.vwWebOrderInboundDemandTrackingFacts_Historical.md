# Azure.vwWebOrderInboundDemandTrackingFacts_Historical

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWebOrderInboundDemandTrackingFacts_Historical"]
    product_dim(["product_dim"]) --> VIEW
    dbo_WebOrderInboundDemandTrackingFactsV2_TEMP(["dbo.WebOrderInboundDemandTrackingFactsV2_TEMP"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| product_dim |
| dbo.WebOrderInboundDemandTrackingFactsV2_TEMP |

## View Code

```sql
CREATE view [Azure].[vwWebOrderInboundDemandTrackingFacts_Historical] 

as 



with UKVatExempt as 
	(
		select distinct cast (sku as varchar) as sku
		from product_dim
		where (department_code in ('R-B-U-46','R-B-U-80') and jurisdiction_code = 'UK')
	)
SELECT [OrderDate]
      ,[OrderNumber]
      ,[DeckSku]
      ,[ItemDescription]
      ,[KeyStory],
      --,[GrossProductSales]
	  case 
		when u.sku is null and isUK = 1 then GrossProductSales/1.2 
		else GrossProductSales
	   end as GrossProductSales,
      [ProductDiscounts],
      --,[NetProductSales]
	  case 
		when u.sku is null and isUK = 1 then NetProductSales/1.2
		else NetProductSales 
	   end as NetProductSales,
      [GrossShippingRevenue]
      ,[ShippingDiscounts]
      ,[NetShippingRevenue]
      ,[OrderUnits]
      ,[PartyEGiftCardUnits]
      ,[PartyEGiftCardValue]
      ,[UpsellEGiftCardUnits]
      ,[UpsellEGiftCardValue]
      ,[EGiftCardUnits]
      ,[EGiftCardValue]
      ,[PhysicalGiftCardUnits]
      ,[PhysicalGiftCardValue]
      ,[DonationUnits]
      ,[DonationValue]
      ,[CondoUnits]
      ,[GiftBoxUnits]
      ,[isGiftOrder]
      ,[GiftOrderUnits]
      ,[GiftOrderValue]
      ,[ProductCost]
      ,[isGiftCard]
      ,[isPhysicalGiftCard]
      ,[isEGiftCard]
      ,[isPartyEGiftCard]
      ,[isUpsellEGiftCard]
      ,[isDonation]
      ,[isCondo]
      ,[isGiftBox]
      ,[hasGiftMessage]
      ,[isBundleMaster]
      ,[isStuffed]
      ,[isUnstuffed]
      ,[isDressed]
      ,[isUndressed]
      ,[ChainAverageOnHandCost]
      ,[ChainAverageOnHandCostGBP]
      ,[isUS]
      ,[isUK]
      ,[isShipFromStore]
      ,[isBillingVShippingDiff],
      --,isnull([CurrentStatus],'Pending') as 'CurrentStatus'
	  case 
			when CurrentStatus is NULL 
				and (
						isEGiftCard=1
						or isDonation=1
					) 
			then 'Complete'
			else isnull(CurrentStatus,'Pending')
		end as CurrentStatus
      ,[PendingStatusDate]
      ,[WavedStatusDate]
      ,[ShippedCompletedStatusDate]
      ,[LastStatusDate]
      ,[DaysBetweenWavedAndShipped]
      ,[DaysSinceWavedStatus]
      ,[DaysBetweenPendingAndWaved]
      ,[DaysBetweenPendingAndShipped]
	 ,isnull([DaysSincePendingStatus],datediff(dd, OrderDate, getdate())) as 'DaysSincePendingStatus'
      ,isnull([DaysSinceLastStatus],datediff(dd, OrderDate, getdate())) as 'DaysSinceLastStatus'
	  ,case 
			when Channel = 'ES' then 'Enterprise Selling'
			when Channel = 'ChannelAdvisor' then 'Channel Advisor'
			else 'Web'
		end as Channel
	 ,[InsertDate]
  FROM [dbo].[WebOrderInboundDemandTrackingFactsV2_TEMP] f
  left join UKVatExempt u on f.DeckSku=u.sku
  --where datediff(dd, OrderDate, getdate())<=45
```

