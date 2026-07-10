# Azure.vwWebOrderInboundIntegrationTracking

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWebOrderInboundIntegrationTracking"]
    WebOrderIntegrationInboundTracking(["WebOrderIntegrationInboundTracking"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WebOrderIntegrationInboundTracking |

## View Code

```sql
CREATE view [Azure].[vwWebOrderInboundIntegrationTracking]

as

with
PreStage1 as
	(
		select 
			TrackingIdentifier,
			ExposedOrderNumber,
			case when DeckOrderNumber is not null then 1 else 0 end as isDeckFiled,
			case when ImportedOrderNumber is not null then 1 else 0 end as isImported,
			case when WOPOrderNumber is not null then 1 else 0 end as isWebOrderProcessing,
			case when DynamicsAPIWebOrderNumber is not null then 1 else 0 end as isDynamicsAPI,
			case when DynamicsSalesOrderNumber is not null then 1 else 0 end as isDynamicsWMS,
			case when UKFTPWebOrderNumber is not null then 1 else 0 end as isUKFTP,
			case when UKCreatedWebOrderNumber is not null then 1 else 0 end as isUKCreated,
			case when isnull(Country,'xx') = 'US' then 1 else 0 end as isUS,
			case when isnull(Country,'xx') = 'UK' then 1 else 0 end as isUK,
			case when isnull(WOPFulfillmentLocation,'xx') in ('0013','2013') then 1 else 0 end as isWeb,
			case when isnull(WOPFulfillmentLocation,'xx') not in ('xx','0013','2013') then 1 else 0 end as isStore,
			isRecordYourVoice,
			isRecorded,
			case 
				when isRecordYourVoice=1 and isRecorded=0 
				then 1
				else 0
			end as isWaitingOnRecordYourVoice
		from WebOrderIntegrationInboundTracking
	),
PreStage2 as
	(
		select 
			case 
				when ps1.isDeckFiled=1 then w.DeckOrderDate
				when ps1.isDeckFiled=0 and ps1.isImported=1 then w.ImportedDate
				when ps1.isDeckFiled=0 and ps1.isImported=0 and ps1.isWebOrderProcessing=1 then w.WOPNewOrderStatusDate
				when ps1.isDeckFiled=0 and ps1.isImported=0 and ps1.isWebOrderProcessing=0 and ps1.isDynamicsAPI=1 then w.DynamicsAPILogDate
				when ps1.isDeckFiled=0 and ps1.isImported=0 and ps1.isWebOrderProcessing=0 and ps1.isDynamicsAPI=0 and ps1.isDynamicsWMS=1 then DynamicsOrderCreationDateTime
				when ps1.isDeckFiled=0 and ps1.isImported=0 and ps1.isWebOrderProcessing=0 and ps1.isDynamicsAPI=0 and ps1.isDynamicsWMS=0 and ps1.isUKFTP=1 then w.UKFTPLogDate
				when ps1.isDeckFiled=0 and ps1.isImported=0 and ps1.isWebOrderProcessing=0 and ps1.isDynamicsAPI=0 and ps1.isDynamicsWMS=0 and ps1.isUKFTP=0 and ps1.isUKCreated=1 then UKCreatedLogDate
				else NULL
			end as ExposedDate,
			ps1.ExposedOrderNumber,
			ps1.isRecordYourVoice,
			ps1.isRecorded,
			ps1.isWaitingOnRecordYourVoice,
			w.DeckOrderNumber,	
			w.DeckOrderNetTotal,	
			w.DeckOrderDate,	
			w.ImportedOrderNumber,	
			w.ImportedWebOrderNumber,	
			w.ImportedDate,	
			w.WOPOrderNumber,	
			w.WOPWebOrderNumber,	
			w.WOPCountry,	
			w.WOPFulfillmentLocation,	
			w.WOPNewOrderStatusDate,	
			w.DynamicsAPIOrderNumber,	
			w.DynamicsAPIWebOrderNumber,	
			w.DynamicsAPISalesOrderNumber,	
			w.DynamicsAPILogDate,	
			w.DynamicsSalesOrderNumber,	
			w.DynamicsOrderCreationDateTime,	
			w.UKFTPOrderNumber,	
			w.UKFTPWebOrderNumber,	
			w.UKFTPLogDate,	
			w.UKCreatedOrderNumber,	
			w.UKCreatedWebOrderNumber,	
			w.UKCreatedLogDate,	
			ps1.isDeckFiled,
			ps1.isImported,
			ps1.isWebOrderProcessing,
			ps1.isDynamicsAPI,
			ps1.isDynamicsWMS,
			ps1.isUKFTP,
			ps1.isUKCreated,
			ps1.isUS,
			ps1.isUK,
			ps1.isWeb,
			ps1.isStore,
			case when isUS=1 and isWeb=1 then 1 else 0 end as isUSWeb,
			case when isUS=1 and isStore=1 then 1 else 0 end as isUSStore,
			case when isUK=1 and isWeb=1 then 1 else 0 end as isUKWeb,
			case when isUK=1 and isStore=1 then 1 else 0  end as isUKStore,
			case when ps1.isDeckFiled=0 then 1 else 0 end as isMissingInDeckFile,
			case when ps1.isImported=0 then 1 else 0 end as isMissingInImportLog,
			case 
				when 
					ps1.isWaitingOnRecordYourVoice=0
					and ps1.isWebOrderProcessing=0 
				then 1 
				else 0 
			end as isMissingInWebOrderProcessing,			
			case 
				when 
					ps1.isUS=1
					and ps1.isWeb=1
					and ps1.isWaitingOnRecordYourVoice=0
					and ps1.isDynamicsAPI=0 
				then 1 
				else 0 
			end as isMissingDynamicsAPI,
			case 
				when 
					ps1.isUS=1
					and ps1.isWeb=1
					and ps1.isWaitingOnRecordYourVoice=0
					and ps1.isDynamicsWMS=0
				then 1 
				else 0
			end as isMissingInDynamics,
			case 
				when 
					ps1.isUK=1
					and ps1.isWeb=1
					and ps1.isWaitingOnRecordYourVoice=0
					and ps1.isUKFTP=0
				then 1
				else 0
			end as isMissingInUKFTP,
			case 
				when 
					ps1.isUK=1
					and ps1.isWeb=1
					and ps1.isWaitingOnRecordYourVoice=0
					and ps1.isUKCreated=0
				then 1
				else 0
			end as isMissingInUKwms
		from prestage1 ps1
		join WebOrderIntegrationInboundTracking w on ps1.TrackingIdentifier=w.TrackingIdentifier
	)
select 
	ExposedDate,	
	ExposedOrderNumber,	
	isRecordYourVoice,	
	isRecorded,	
	isWaitingOnRecordYourVoice,
	DeckOrderNumber,	
	DeckOrderNetTotal,	
	DeckOrderDate,	
	ImportedOrderNumber,	
	ImportedWebOrderNumber,	
	ImportedDate,	
	WOPOrderNumber,	
	WOPWebOrderNumber,	
	WOPCountry,	
	WOPFulfillmentLocation,	
	WOPNewOrderStatusDate,	
	DynamicsAPIOrderNumber,	
	DynamicsAPIWebOrderNumber,	
	DynamicsAPISalesOrderNumber,	
	DynamicsAPILogDate,	
	DynamicsSalesOrderNumber,	
	DynamicsOrderCreationDateTime,	
	UKFTPOrderNumber,	
	UKFTPWebOrderNumber,	
	UKFTPLogDate,	
	UKCreatedOrderNumber,	
	UKCreatedWebOrderNumber,	
	UKCreatedLogDate,	
	isDeckFiled,	
	isImported,	
	isWebOrderProcessing,	
	isDynamicsAPI,	
	isDynamicsWMS,	
	isUKFTP,	
	isUKCreated,	
	isUS,	
	isUK,	
	isWeb,	
	isStore,
	isUSWeb,	
	isUSStore,	
	isUKWeb,	
	isUKStore,	
	isMissingInDeckFile,	
	isMissingInImportLog,	
	isMissingInWebOrderProcessing,	
	isMissingDynamicsAPI,	
	isMissingInDynamics,	
	isMissingInUKFTP,	
	isMissingInUKwms	
from PreStage2
where datediff(dd, ExposedDate, getdate()) <= 10
```

