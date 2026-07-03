# WM.fnFlashGaapWebSales

**Database:** WebOrderProcessing  
**Server:** bearcluster01  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["WM.fnFlashGaapWebSales"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @Days | int | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql


--SELECT * FROM wm.fnFlashGaapWebSales(60)
CREATE function [WM].[fnFlashGaapWebSales] (@Days int)

returns @Summary table
				(
					LocationCode varchar(4),
					LocationName varchar(50),
					RetailTransactionID int,
					StoreNumber int,
					WorkStationNumber int,
					RetailTransactionNumber int,
					OperatorNumber int,
					RetailTransactionTypeCode varchar(4),
					ItemNumber varchar(6),
					VoidFlag int,
					TransactionDateTime datetime,
					NetSales decimal(10,2),
					EntryDate datetime,
					Source varchar(10),
					WebOrderNumber varchar(20),
					TransDate date
				)
	 

as
begin

				;With 
				SettledOrders as
					(
						select 
							sOrderNumber OrderNumber
						from BABWeCommerce.dbo.NSBTranslate_LogTrans with (nolock)
						where 1=1 
						and datediff(dd, dTimeStamp, getdate()) <= @Days
						group by sOrderNumber
					),
				SourceSite as
					(
						select 
							o.TransactionID,
							case when right(o.SourceSite,2) = 'US' then '0013' else '2013' end as LocationCode,
							case when right(o.SourceSite,2) = 'US' then 'US Web' else 'UK Web' end as LocationName,
							case when right(o.SourceSite,2) = 'US' then 13 else 2013 end as StoreNumber
						from wm.Orders o with (nolock)
						where 1=1
						and exists (select so.OrderNumber from SettledOrders so where left(so.OrderNumber,8) = left(o.OrderNum,8))
						group by 
							o.TransactionID, 
							o.SourceSite,
							cast(left(o.EnterpriseSellingID, 19) as varchar(19))
					),
				RefNums as
					(
						select 
							o.TransactionID, 
							cast(left(o.EnterpriseSellingID, 19) as varchar(19)) as ESReferenceNo
						from wm.Orders o with(nolock) 
						where 1=1
						and datediff(dd, o.OrderDate, getdate()) <= @Days
						and o.EnterpriseSellingID is not NULL
						group by 
							o.TransactionID, 
							cast(left(o.EnterpriseSellingID, 19) as varchar(19))
					),
				PartyExclude as
					(
						select rf.TransactionID
						from babwpartyPlanner.dbo.PartyEnterpriseSellingXRef p with (nolock)
						join RefNums rf on left(p.EnterpriseSellingID,19) = rf.ESReferenceNo
					),
				SettledSales as
					(
						select 
							vw.TransactionID,
							vw.WMOrderNumber,
							vw.TransactionDate,
							sum(vw.TotalCharges*vw.CurrencyMultiplier) TotalCharges
						from wm.vwTransactionDetailALL vw
						where 1=1
						and substring(vw.WMOrderNumber, 9,1) = '_'
						and vw.isSAProcessed = 1
						and vw.BillToEmail <> 'guest.services@buildabear.com'
						and exists (select so.OrderNumber from SettledOrders so where left(so.OrderNumber,8) = left(vw.WMOrderNumber,8)) 
						group by 
							vw.TransactionID,
							vw.WMOrderNumber,
							vw.TransactionDate
					)

				insert @Summary
				select 
					ss.LocationCode,
					ss.LocationName,
					ss.TransactionID as RetailTransactionID,
					ss.StoreNumber,
					52 as WorkstationNumber,
					ss.TransactionID as RetailTransactionNumber,
					52 as OperatorNumber,
					'Sale' as RetailTransactionTypeCode,
					NULL as ItemNumber,
					NULL as VoidFlag,
					sss.TransactionDate as TransactionDateTime,
					sss.TotalCharges as NetSales,
					sss.TransactionDate as EntryDate,
					'Web Cart' as Source,
					cast(sss.WMOrderNumber as varchar(50)) as WebOrderNumber,
					cast(sss.TransactionDate as date) as TransDate
				from SourceSite ss
				join SettledSales sss on ss.TransactionID=sss.TransactionID
				where not exists (select pe.TransactionID from PartyExclude pe where pe.TransactionID = ss.TransactionID);

				return
end
```
