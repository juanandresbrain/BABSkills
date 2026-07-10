# dbo.spMergeWebOrders

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeWebOrders"]
    dbo_WebOrders(["dbo.WebOrders"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WebOrders |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeWebOrders]

as




-------------------------------------------------------------------------
-- spMergeWebOrders
-- 2017-10-18- Dan Tweedie - Created Proc
-------------------------------------------------------------------------


select transactionID, orderid, ordernum, max(StatusDate) MaxStatus
into #dedupe
from dwstaging.dbo.WebOrders
group by transactionID, orderid, ordernum


set nocount on

Merge into dw.dbo.WebOrders as target
Using (
		select distinct wo.* 
		from dwstaging.dbo.WebOrders wo where exists
			(
				select d.TransactionID
				from #dedupe d
				where d.TransactionID=wo.TransactionID
				and d.OrderID=wo.OrderID
				and d.OrderNum=wo.OrderNum
				and d.MaxStatus=wo.StatusDate
			)
		) as source
On (
			target.TransactionID = source.TransactionID
			and
			target.OrderID = source.OrderID
			and 
			target.Ordernum = source.OrderNum
	)
when matched 
	and
		(
			isnull(target.SourceSite,'xx') <> isnull(source.SourceSite,'xx')
			OR
			isnull(target.OrderDate,'3030-12-31') <> isnull(source.OrderDate,'3030-12-31')
			OR
			isnull(target.ShippingAmount,'0') <> isnull(source.ShippingAmount,'0')
			OR
			isnull(target.OrderStatus,'xx') <> isnull(source.OrderStatus,'xx')
			OR
			isnull(target.StatusDate,'3030-12-31') <> isnull(source.StatusDate,'3030-12-31')
			OR
			isnull(target.Physical,'xx') <> isnull(source.Physical,'xx')
			OR
			isnull(target.StatusSortOrder,'99999') <> isnull(source.StatusSortOrder,'99999')
			OR
			isnull(target.ShipToPostalCode,'xx') <> isnull(source.ShipToPostalCode,'xx')
			OR
			isnull(target.ShipToState,'xx') <> isnull(source.ShipToState,'xx')
			OR
			isnull(target.ShipToCountry,'xx') <> isnull(source.ShipToCountry,'xx')
			OR 
			isnull(target.ESReferenceNbr, 'x') <> isnull(source.ESReferenceNbr,'x')
			or
			isnull(target.BillToFirstName, 'x') <> isnull(source.BillToFirstName,'x') 
			or
			isnull(target.BillToLastName, 'x') <> isnull(source.BillToLastName,'x') 
			or
			isnull(target.BillToCity, 'x') <> isnull(source.BillToCity,'x') 
			or
			isnull(target.BillToState, 'x') <> isnull(source.BillToState,'x')
			or
			isnull(target.BillToPostCode, 'x') <> isnull(source.BillToPostCode,'x')
			or
			isnull(target.BillToCountry, 'x') <> isnull(source.BillToCountry,'x')
			or
			isnull(target.BillToEmailAddress, 'x') <> isnull(source.BillToEmailAddress,'x')
			or
			isnull(target.BillToCustomerNumber, 'x') <> isnull(source.BillToCustomerNumber,'x')
			
		)
		then UPDATE
			set
			target.SourceSite = source.SourceSite,
			target.OrderDate = source.OrderDate,
			target.ShippingAmount = source.ShippingAmount,
			target.OrderStatus = source.OrderStatus,
			target.StatusDate = source.StatusDate,
			target.Physical = source.Physical,
			target.StatusSortOrder = source.StatusSortOrder,
			target.ShipToPostalCode = source.ShipToPostalCode,
			target.ShipToState = source.ShipToState,
			target.ShipToCountry = source.ShipToCountry,
			target.ESReferenceNbr = source.ESReferenceNbr,
			target.BillToFirstName=source.BillToFirstName,
			target.BillToLastName=source.BillToLastName,
			target.BillToCity=source.BillToCity,
			target.BillToState=source.BillToState,
			target.BillToPostCode=source.BillToPostCode,
			target.BillToCountry=source.BillToCountry,
			target.BillToEmailAddress=source.BillToEmailAddress,
			target.BillToCustomerNumber=source.BillToCustomerNumber,
			target.UpdateDate = getdate()
When Not Matched By Target 
	Then 
		Insert (
					SourceSite,
					TransactionID,
					OrderID,
					OrderNum,
					OrderDate,
					ShippingAmount,
					OrderStatus,
					StatusDate,
					Physical,
					StatusSortOrder,
					ShipToPostalCode,
					ShipToState,
					ShipToCountry,
					ESReferenceNbr,
					BillToFirstName,
					BillToLastName,
					BillToCity,
					BillToState,
					BillToPostCode,
					BillToCountry,
					BillToEmailAddress,
					BillToCustomerNumber,
					InsertDate,
					UpdateDate
				)
		Values (	
					source.SourceSite,
					source.TransactionID,
					source.OrderID,
					source.OrderNum,
					source.OrderDate,
					source.ShippingAmount,
					source.OrderStatus,
					source.StatusDate,
					source.Physical,
					source.StatusSortOrder,
					source.ShipToPostalCode,
					source.ShipToState,
					source.ShipToCountry,
					source.ESReferenceNbr,
					source.BillToFirstName,
					source.BillToLastName,
					source.BillToCity,
					source.BillToState,
					source.BillToPostCode,
					source.BillToCountry,
					source.BillToEmailAddress,
					source.BillToCustomerNumber,
					getdate(),
					getdate()
				)
;
```

