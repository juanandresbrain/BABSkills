# WMS.spReportWebSalesOrdersAging

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spReportWebSalesOrdersAging"]
    WMS_AgedWebOrdersInDynamics(["WMS.AgedWebOrdersInDynamics"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.AgedWebOrdersInDynamics |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spReportWebSalesOrdersAging] 
@detailIndicator int

as

---------------------------------------------------------------------------------------------------------------------------------------------------
--	Ian Wallace	  02/02/2021	subreport detail for WMS_WebSalesOrdersAging_Measures report on CLB SSRS server
---------------------------------------------------------------------------------------------------------------------------------------------------
set nocount on 

if (@detailIndicator = 1) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and cast(OrderCreationDateTime as date) <= cast(getdate()-11 as date)
	and DynamicsOrderAge >= 11
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
if (@detailIndicator = 2) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and cast(OrderCreationDateTime as date) between  cast(getdate()-10 as date) and cast(getdate()-5 as date)
	and DynamicsOrderAge between 5 and 10
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
if (@detailIndicator = 3) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and WaveID is null
	and isWaved = 0
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
if (@detailIndicator = 4) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and WaveID is not null
	and isWaved = 1
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
if (@detailIndicator = 5) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and cast(OrderCreationDateTime as date) between  cast(getdate()-999 as date) and cast(getdate()-0 as date)
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
	--order by DynamicsOrderAge asc
-- 6197 to 7283
END
if (@detailIndicator = 6) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and cast(OrderCreationDateTime as date) <= cast(getdate()-11 as date)
	and DynamicsOrderAge >= 11
	and ItemNumber = '027500'
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
if (@detailIndicator = 7) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and cast(OrderCreationDateTime as date) between  cast(getdate()-10 as date) and cast(getdate()-5 as date)
	and DynamicsOrderAge between 5 and 10
	and ItemNumber = '027500'
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
if (@detailIndicator = 8) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and cast(OrderCreationDateTime as date) <= cast(getdate()-11 as date)
	and DynamicsOrderAge >= 11
	and ItemNumber in ('000015', '022610', '023019')
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
if (@detailIndicator = 9) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	--and cast(OrderCreationDateTime as date) between  cast(getdate()-10 as date) and cast(getdate()-5 as date)
	and DynamicsOrderAge between 5 and 10
	and ItemNumber in ('000015', '022610', '023019')
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
if (@detailIndicator = 10) 
BEGIN
	select SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
	OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
	--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
	,DeckOrderDate,DynamicsOrderAge,case when isWaved = 1 then 'Yes'else 'No' end as isWaved
	,case when isShippedOrCancelledInDeck = 1 then 'Yes' else 'No' end as isShippedOrCancelledInDeck
	from WMS.AgedWebOrdersInDynamics with (nolock)
	where 1=1
	and isShippedOrCancelledInDeck = 1
	group by SalesOrderNumber,SalesOrderStatus,SalesOrderProcessingStatus,SalesOrderOriginCode,SalesOrderPoolId,ShippingCarrierId,ShippingCarrierServiceId,	
		OrderCreationDateTime,DeliveryModeCode,WebOrderNumber,WaveID,ReleasedDateAndTime
		--ItemNumber,OrderedSalesQuantity,LineDescription,WebOrderNumber,WaveID,ReleasedDateAndTime,ContainerID,WorkID
		,DeckOrderDate,DynamicsOrderAge,isWaved,isShippedOrCancelledInDeck
	order by SalesOrderNumber --, ItemNumber
END
```

