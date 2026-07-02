# ERP.vwPurchaseOrderTPM_XML

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwPurchaseOrderTPM_XML"]
    ERP_tmpTPMpo(["ERP.tmpTPMpo"]) --> VIEW
    ERP_vwPurchaseOrderTPM(["ERP.vwPurchaseOrderTPM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.tmpTPMpo |
| ERP.vwPurchaseOrderTPM |

## View Code

```sql
CREATE view [ERP].[vwPurchaseOrderTPM_XML]
------------------------------------------------------------------------------------------------------------------
--Dan Tweedie	-	2017-11-07	-	Created view to output XML for TPM PO file. Data is pre-staged from D365
--Tim Callahan	-	2021-09-29	-	Modified view  Header CTE to select max COO code as that is header information and coult result in multiple XML nodes
------------------------------------------------------------------------------------------------------------------

as

with 
Header as
	(
		select distinct
			po_no,
			AcceptedFlag,
			Type,
			AcceptRqdMode,
			OwnerID,
			eventcode,
			EventLocationInternalId,
			EventSourceLocationInternalId,
			ShipToldRef,
			TransportMethodDesc,
			FOBDesc,
			max (COOCode) as COOCode,
			ShipFromId,
			SupplierId,
			BillTold,
			Rep1Id,
			Rep2Id,
			FulFillFlag,
			InternalStatus,
			TypeCode,
			CurrencyDesc,
			OrderDate,
			PayTermsDesc,
			ShipToId
		from ERP.vwPurchaseOrderTPM
		WHERE po_no in (select PurchaseOrderNumber from ERP.tmpTPMpo where exported = 0) --controlled via loop so it's always working on a single po (spOutputTPMPurchaseOrderXML)
		group by 			po_no,
			AcceptedFlag,
			Type,
			AcceptRqdMode,
			OwnerID,
			eventcode,
			EventLocationInternalId,
			EventSourceLocationInternalId,
			ShipToldRef,
			TransportMethodDesc,
			FOBDesc,
			ShipFromId,
			SupplierId,
			BillTold,
			Rep1Id,
			Rep2Id,
			FulFillFlag,
			InternalStatus,
			TypeCode,
			CurrencyDesc,
			OrderDate,
			PayTermsDesc,
			ShipToId
	),
Detail as
	(
		select distinct
			AcceptedItemFlag,
			ItemDesc,
			OrderLine,
			ItemId,
			AltDetailKey,
			UOMCode,
			CurrQty,
			UnitCost,
			RetailPrice,
			InternalStatusDetail,
			StartShipDate,
			EndDeliverDateTime,
			CancelDate,
			ColorDesc,
			ColorCode,
			ItemAttr1,
			CatchWeightFlag,
			ShipToldRef,
			SupplierItemId,
			SupplierItemDesc,
			StdPackQty,
			StdCaseQty
		from ERP.vwPurchaseOrderTPM
		WHERE po_no in (select po_no from Header)
	),
XMLStage (XML) as
	(
		select
		---------->>OUTER HEADER
			convert(varchar, getdate(), 120) + '-' + 'TPMOr' as '@Id',
			'6.0.0' as '@Version',
			left(convert(varchar, getdate(), 126), 19) as '@Timestamp', --no milliseconds
			'2' as '@DocSourceType',
			(select '' as 'SenderId',
						'' as 'ReceiverId'
					for xml path('Delivery'), Type),
		----------->>>>HEADER
			(select po_no as '@Id',
					AcceptedFlag as '@AcceptedFlag',
					Type as '@Type',
					AcceptRqdMode as '@AcceptRqd',
					(select OwnerID as '@OrgInternalId'
					for xml path('Owner'), Type),
					'' as 'PartnerVisibility',
					(select convert(varchar, getdate(), 101) + ' ' + convert(varchar, getdate(), 108) as '@Id',
							eventcode as '@Code',
							(select EventLocationInternalId as '@InternalId'
							for xml path('EventLocation'), Type),
							'' as EventRefLocation,
							(select EventSourceLocationInternalId as '@InternalId'
							for xml path('EventSrcLocation'), Type),
							(select '' as 'EntityType',
							(select '' as 'Ref1',
								'' as 'Ref2',
								'' as 'Ref3',
								'' as 'Ref4',
								'' as 'Ref5'
								for xml path('EventRefs'), Type)
							for xml path('EventInfo'), Type)
							for xml path('Event'), Type),
					(select ShipToldRef as '@ShipToIdRef',
					(select TransportMethodDesc as '@Desc'
						for xml path('TransportationMethod'),Type),
					(select FOBDesc as '@Desc'
						for xml path('FOB'), Type),
					'' as 'Carrier',
					(select COOCode as '@Code'
						for xml path('COO'), Type),
					(select '' as 'OriginPort',
							'' as 'DestinationPort'
						for xml path('Ports'), Type)
						for xml path('ShipInfo'), Type),
					(select ShipFromId as '@Id',
						(select '' as 'ContactInfo'
						for xml path('Address'), Type)
						for xml path('ShipFrom'), Type),
					(select
						(select '' as 'ReceivingLocation'
						for xml path('Receipt'), Type),
					'' as 'MiscInfo'
						for xml path('OrderShipment'), Type),
					(Select
					(select '' as 'Weight',
							'' as 'Volume',
							'' as 'EstWeight',
							'' as 'EstVolume'
						for xml path('Measures'), Type)
					for xml path('Loaded'), Type),
					(Select
					(select '' as 'Weight',
							'' as 'Volume',
							'' as 'EstWeight',
							'' as 'EstVolume'
						for xml path('Measures'), Type)
					for xml path('Received'), Type),
					(select SupplierId as '@Id',
							(select '' as 'ContactInfo'
								for xml path('Address'), Type)
						for xml path('Supplier'), Type),
					(select 
					(select '' as 'ContactInfo'
						for xml path('Address'), Type)
						for xml path('Agent'), Type),
					(select
					(select '' as '@Id',
						(select '' as 'ContactInfo'
							for xml path('Address'), Type)
						for xml path('Hub1'), Type),
					(select
					(select '' as 'ContactInfo'
						for xml path('Address'), Type)
						for xml path('Hub2'), Type)
						for xml path('Hubs'), Type),
					(select
					(select '' as 'ContactInfo'
						for xml path('Address'), Type)
						for xml path('SoldTo'), Type),
					(Select BillTold as '@Id',
							(select '' as 'ContactInfo'
								for xml path('Address'), Type)
						for xml path('BillTo'), Type),
					(select
					(select '' as 'ContactInfo'
						for xml path('Address'), Type)
						for xml path('Store'), Type),
					(select
					(select Rep1Id as '@Id',
							(select '' as 'ContactInfo'
								for xml path('Address'), Type)
						for xml path('Rep1'), Type),
					(select Rep2Id as '@Id',
							(select '' as 'ContactInfo'
								for xml path('Address'), Type)
						for xml path('Rep2'), Type),
							(select
							(select '' as 'ContactInfo'
								for xml path('Address'), Type)
								for xml path('Rep3'), Type)
						for xml path('Reps'), Type),
					'' as 'Instructions',
					(select
					(select '' as 'Status'
						for xml path('Alert'), Type),
						(select FulFillFlag as '@FulfillFlag'
							for xml path('OrderAttributes'), Type),
						'' as 'Revision',
						'' as 'OrderRefs',
					(select InternalStatus as '@Nbr'
						for xml path('Status'), Type),
					'' as 'Priority',
					'' as 'Points',
					'' as 'OwnerPriority',
					'' as 'Style',
					(select TypeCode as '@Code'
						for xml path('OrderType'), Type),
					'' as 'Category',
					'' as 'Dept',
					'' as 'CustomerDivision',
					'' as 'CustomerDepartment',
						(select '' as 'Class01',
								'' as 'Class02',
								'' as 'Class03',
								'' as 'Class04',
								'' as 'Class05',
								'' as 'Class06',
								'' as 'Class07',
								'' as 'Class08',
								'' as 'Class09'
						for xml path('Classes'), Type),
						(select CurrencyDesc as '@Desc'
						for xml path('Currency'), Type),
					'' as 'PartnerCurrency',
					'' as 'CreditHold',
					(select OrderDate as '@Ordered'
						for xml path('OrderDates'), Type),
					(select PayTermsDesc as '@Desc'
						for xml path('PayTerms'), Type),
					'' as 'LetterOfCredit',
					(select
					(select '' as 'ContactInfo'
						for xml path('Address'), Type)
						for xml path('Notify'), Type),
					(select '' as 'HTS01',
							'' as 'HTS02'
						for xml path('HTS'), Type),
					'' as 'Quota',
					'' as 'DocTypes',
					'' as 'MiscInfo',
					'' as 'Policies'
						for xml path('OrderInfo'), Type),
					(select
					(select 
					(select '' as 'ContactInfo'
						for xml path('Address'), Type)
						for xml path('Location'), Type),
					'' as 'Status',
					(select
					(select
					(select '' as 'Defect'
						for xml path('Item'), Type),
						'' as 'Defect'
						for xml path('InspectedLPN'), Type),
							(select '' as 'Defect'
								for xml path('Item'), Type)
						for xml path('Sample'), Type)
						for xml path('Inspections'), Type)
						for xml path('Order'), type),
						(select 
						(select ShipToId as '@Id',
								'' as 'Address'
							for xml path('ShipTo'), Type)
							for xml path('ShipTos'), Type),

		----------->>>DETAIL
			(--DETAIL DATA
				select AcceptedItemFlag as '@AcceptedFlag',
						ItemDesc as '@Desc',
						OrderLine as '@OrderLine',
						ItemId as '@Id',
						AltDetailKey as '@AltKey',
						(select '' as 'Measures'
							for xml path('Loaded'), Type),
						(select '' as 'Measures'
							for xml path('Received'), Type),
						(select UOMCode as '@UOMCode',
								CurrQty as '@OrderQty'
							for xml path('ItemQuantities'), Type),
						(select UnitCost as '@Value'
							for xml path('UnitCost'), Type),
						(select RetailPrice as '@Value'
							for xml path('RetailPrice'), Type),
						(select
						(select
						(select InternalStatusDetail as '@Nbr'
							for xml path('Status'), Type)
							for xml path('Alert'), Type),
						(select '' as 'Address'
							for xml path('Store'), Type),
						(select StartShipDate as '@StartShip',
								EndDeliverDateTime as '@EndDeliver',
								CancelDate as '@Cancel'
							for xml path('OrderDates'), Type),
						(select ColorDesc as '@Desc',
								ColorCode as '@Code'
							for xml path('Color'), Type),
						(select ItemAttr1 as '@Attr1',
								CatchWeightFlag as '@CatchWeightFlag'
							for xml path('ItemAttributes'), Type),
						(select '' as 'Address'
							for xml path('ShipFrom'), Type),
						(select ShipToldRef as '@ShipToIdRef'
							for xml path('ItemShipInfo'), Type),
						(select SupplierItemId as '@Id',
								SupplierItemDesc as '@Desc'
							for xml path('SupplierItem'), Type),
						(select StdPackQty as '@Qty'
							for xml path('StdPack'), Type),
						(select StdCaseQty as '@Qty'
							for xml path('StdCase'), Type),
						'' as 'HTS'
						for xml path('ItemInfo'), Type)
						from Detail
					for xml path('OrderItem'), Type
			)
		from Header
		for xml path('MANH_TPM_Order')
	)
select 
	cast(XML as xml) as XMLData
from XMLStage
```

