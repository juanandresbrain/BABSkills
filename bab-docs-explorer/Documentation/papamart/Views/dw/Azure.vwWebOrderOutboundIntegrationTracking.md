# Azure.vwWebOrderOutboundIntegrationTracking

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWebOrderOutboundIntegrationTracking"]
    WebOrderIntegrationOutboundTracking(["WebOrderIntegrationOutboundTracking"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WebOrderIntegrationOutboundTracking |

## View Code

```sql
CREATE view [Azure].[vwWebOrderOutboundIntegrationTracking]
as
with 
PreStage1 as
	(
		select
			TrackingIdentifier,
			ExposedShippedDate as ShipDate,
			ExposedShippedOrder as ShippedOrder,
			case when ShippedFromCountry = 'US' then 1 else 0 end as isUS,
			case when ShippedFromCountry = 'UK' then 1 else 0 end as isUK,
			1 as isShipped,
			case when DynamicsShippedInvoiceDate is not null then 1 else 0 end as isShippedUS,
			case when UKShippedDate is not null then 1 else 0 end as isShippedUK,
			case when IntegrationShippedDate is not null then 1 else 0 end as isInUSIntegration,
			case when UKShippedDate is not null then 1 else 0 end as isInUKIntegration,--technically the integration data is the source for UK
			case when WebOrderProcessingShippedStatusDate is not null then 1 else 0 end as isWOPShipped,
			case 
				when 
					isnull(SettlementDate,DeckShipDate) is not null 
					or SalesAuditTransactionDate is not null ---if it's in sales audit, let's not flag it as not shipped in oms...waste of time to investigate
				then 1 else 0 end as isOMSShipped,
			case when DeckCancelDate is not null then 1 else 0 end as isOMSCancelled,
			isSettled,
			DeckCurrentStatus as OMSCurrentStatus,
			case when SalesAuditTransactionDate is not null then 1 else 0 end as isSalesAuditShipped
		from WebOrderIntegrationOutboundTracking
	),
PreStage2 as
	(
		select 
			p1.ShipDate,
			p1.ShippedOrder,
			p1.isShipped,
			case when datediff(dd, p1.ShipDate, getdate()) = 0
				then 1
				else 0
			end as isShippedToday,
			case when datediff(dd, p1.ShipDate, getdate()) > 0
				then 1
				else 0
			end as isShippedBeforeToday,
			p1.isUS,
			p1.isUK,
			p1.isShippedUS,
			p1.isShippedUK,
			p1.isInUSIntegration,
			p1.isInUKIntegration,
			p1.isWOPShipped,
			p1.isOMSShipped,
			p1.isOMSCancelled,
			p1.isSettled,
			case when p1.isSettled=0
				then 1
				else 0
			end as isNotSettled,
			p1.OMSCurrentStatus,
			p1.isSalesAuditShipped,
			case 
				when p1.isUS=1
				and p1.isShippedUS=1
				and isInUSIntegration=0
				then 1
				else 0
			end as isNotShippedInUSIntegration,
			case
				when p1.isUK=1
				and p1.isShippedUK=1
				and p1.isInUKIntegration=0
				then 1
				else 0
			end as isNotShippedInUKIntegration,
			case 
				when p1.isShipped=1
				and p1.isInUSIntegration=0
				and p1.isInUKIntegration=0
				then 1
				else 0
			end as isNotShippedInIntegration,
			case 
				when p1.isUS=1
				and p1.isShippedUS=1
				and isWOPShipped=0
				then 1
				else 0
			end as isNotShippedInUSWebOrderProcessing,
			case 
				when p1.isUK=1
				and p1.isShippedUK=1
				and isWOPShipped=0
				then 1
				else 0
			end as isNotShippedInUKWebOrderProcessing,
			case 
				when p1.isShipped=1
				and p1.isWOPShipped=0
				then 1
				else 0
			end as isNotShippedInWebOrderProcessing,
			case
				when p1.isUS=1
				and p1.isShippedUS=1
				and isOMSShipped=0
				then 1
				else 0
			end as isNotShippedUSInOMS,
			case
				when p1.isUK=1
				and p1.isShippedUK=1
				and p1.isOMSShipped=0
				then 1
				else 0
			end as isNotShippedUKInOMS,
			case 
				when p1.isShipped=1
				and p1.isOMSShipped=0
				then 1
				else 0
			end as isNotShippedInOMS,
			case
				when p1.isUS=1
				and p1.isShippedUS=1
				and isSalesAuditShipped=0
				then 1
				else 0
			end as isNotInUSSalesAudit,
			case
				when p1.isUK=1
				and p1.isShippedUK=1
				and isSalesAuditShipped=0
				then 1
				else 0
			end as isNotInUKSalesAudit,
			case
				when p1.isShipped=1
				and isSalesAuditShipped=0
				then 1
				else 0
			end as isNotInSalesAudit
		from PreStage1 p1
	)
select 
	ShipDate,
	ShippedOrder,	
	isShipped,	
	isShippedToday,
	isShippedBeforeToday,
	isUS,	
	isUK,	
	isShippedUS,	
	isShippedUK,	
	isInUSIntegration,	
	isInUKIntegration,	
	isWOPShipped,	
	isOMSShipped,	
	isOMSCancelled,
	isSettled,
	OMSCurrentStatus,
	isSalesAuditShipped,	
	isNotShippedInUSIntegration,	
	isNotShippedInUKIntegration,	
	isNotShippedInIntegration,	
	isNotShippedInUSWebOrderProcessing,	
	isNotShippedInUKWebOrderProcessing,	
	isNotShippedInWebOrderProcessing,	
	isNotShippedUSInOMS,	
	isNotShippedUKInOMS,	
	isNotShippedInOMS,	
	isNotSettled,
	isNotInUSSalesAudit,	
	isNotInUKSalesAudit,	
	isNotInSalesAudit
from PreStage2
```

