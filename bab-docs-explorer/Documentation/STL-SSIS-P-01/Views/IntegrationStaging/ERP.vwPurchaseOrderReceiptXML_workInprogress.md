# ERP.vwPurchaseOrderReceiptXML_workInprogress

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwPurchaseOrderReceiptXML_workInprogress"]
    ERP_vwPurchaseOrderReceipts(["ERP.vwPurchaseOrderReceipts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.vwPurchaseOrderReceipts |

## View Code

```sql
create view [ERP].[vwPurchaseOrderReceiptXML_workInprogress]

as

---------------------------------------------------------------------
-- Dan Tweedie	-	2017-11-15	-	Created view, work in progress --
--									Need to update to pull data from Fact table, not Stage, and to only capture NEW receipts
---------------------------------------------------------------------

with 
Receipts as
	(
		select *
		from ERP.vwPurchaseOrderReceipts
	)
	,
XMLStage (XML) as
	(
		select 
			'NO' as 'CLOSEFORRECEIPT',
			r.ReceiptLocation as 'INVENTLOCATIONID',
			r.ITEMID,
			r.PurchaseOrderNumber as 'PURCHID',
			r.QTY,
			r.RECEIPTDATE,
			concat(
			datepart(yyyy, getdate()), 
			datepart(mm, getdate()),
			datepart(dd, getdate()),
			datepart(hh, getdate()),
			datepart(mi, getdate()),
			datepart(ss, getdate()),
			datepart(ms, getdate())
			) as RECEIPTID,
			r.UNITOFMEASURE,
			DENSE_RANK() OVER (ORDER BY r.ReceiptLocation, r.ITEMID, r.PurchaseOrderNumber, r.RECEIPTDATE, r.BOL) as ReceiptGrouping
		from Receipts r 
		order by r.ReceiptLocation, r.PurchaseOrderNumber, r.Qty
		for xml path('RSMWMSPurchaseReceiptEntity'), root('Document'), Type
	)
select XML as XMLData
from XMLStage
```

