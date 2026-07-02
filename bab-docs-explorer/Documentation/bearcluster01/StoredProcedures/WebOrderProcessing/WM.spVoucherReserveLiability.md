# WM.spVoucherReserveLiability

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spVoucherReserveLiability"]
    dbo_cust_liability(["dbo.cust_liability"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.cust_liability |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spVoucherReserveLiability] 
	@voucher_number varchar(20)

-- =============================================================================================================
-- Name: WM.spVoucherReserveLiability 
--
-- Description:	Update pos_amount_1 value to 0 for the supplied reward coupon.  This reserves the funds so 
-- they cannot be redeemed multiple times
--
-- Output: 
--	
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		02/16/2018		Initial Creation
-- =============================================================================================================

AS
BEGIN

	SET NOCOUNT ON;

	--SELECT *
	--FROM BEDROCKDB01.auditworks.dbo.cust_liability
	--WHERE reference_type = 35 AND reference_no LIKE '12502007933760548'

	UPDATE BEDROCKDB01_WRITER.auditworks.dbo.cust_liability
	SET pos_amount_1 = 0
	WHERE reference_type = 35 AND reference_no LIKE @voucher_number
	
END

WM,spWebSalesFlashGaapDetailsCapture,--USE [WebOrderProcessing]
--GO

--/****** Object:  View [WM].[vwWebSalesFlashGaapCapture]    Script Date: 1/9/2023 8:56:20 AM ******/
--SET ANSI_NULLS ON
--GO

--SET QUOTED_IDENTIFIER ON
--GO






create proc [WM].[spWebSalesFlashGaapDetailsCapture] 

as

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----	Dan TWeedie	2023-01-09 - Created proc for new POS Web Returns
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------get transaction details -- sql that replaces vwTransactionDetailsAll -- using temp tables instead of CTE

 if (object_id('tempdb..#TransactionShipmentWorking') is not null) drop table #TransactionShipmentWorking
  SELECT t.[TransactionNum]
      ,[ShipmentNumber]
  into #TransactionShipmentWorking
  FROM [WebOrderProcessing].[WM].[OMSTransactionDetails] td
  LEFT JOIN [WebOrderProcessing].[WM].[Transactions] t ON td.TransactionID = t.TransactionID
  WHERE ShipmentNumber IS NOT NULL
  GROUP BY TransactionNum, ShipmentNumber
  
  if (object_id('tempdb..#TransactionNoShipment') is not null) drop table #TransactionNoShipment
  SELECT t.[TransactionNum]
      ,td.[ShipmentNumber]
  into #TransactionNoShipment
  FROM [WebOrderProcessing].[WM].[OMSTransactionDetails] td
  LEFT JOIN [WebOrderProcessing].[WM].[Transactions] t ON td.TransactionID = t.TransactionID
  LEFT JOIN [WebOrderProcessing].[WM].[Orders] o ON t.TransactionID = o.TransactionID
  LEFT JOIN [WebOrderProcessing].[WM].[OrderItems] oi ON o.OrderID = oi.OrderID
  INNER JOIN [STL-SSIS-P-01].[IntegrationStaging].[WEB].[vwGiftCardDisplayNameLookup] v ON oi.sku = v.BABWProductID
  WHERE td.ShipmentNumber IS NULL
  GROUP BY TransactionNum, td.ShipmentNumber
 
 if (object_id('tempdb..#TransactionShipment') is not null) drop table #TransactionShipment
 SELECT *
 into #TransactionShipment
 FROM #TransactionNoShipment
  EXCEPT
  SELECT *
  FROM #TransactionShipmentWorking
  
  if (object_id('tempdb..#TransactionShipmentUnion') is not null) drop table #TransactionShipmentUnion
  SELECT *
  into #TransactionShipmentUnion
  FROM #TransactionShipmentWorking
  UNION
  SELECT *
  FROM #TransactionShipment
 
 --this took 20 minutes....then took 9 min
  if (object_id('tempdb..#TransactionDetailAll') is not null) drop table #TransactionDetailAll
 SELECT MAX([TansactionDetailID]) AS 'TansactionDetailID'
      ,[TransactionNum]
      ,[OrderNumber]
      ,[TransactionID]
      ,MAX([TransactionDate]) AS 'TransactionDate'
      ,MAX([SubTotal]) AS 'SubTotal'
      ,MAX([Shipping]) AS 'Shipping'
      ,MAX([ProcessingFee]) AS 'ProcessingFee'
      ,Max([Tax]) AS 'Tax'
      ,MAX([TotalCharges]) AS 'TotalCharges'
      ,[PaymentTransactionType]
      ,SUM([TransactionAmount]) AS 'TransactionAmount'
      ,MAX([OrderDiscount]) AS 'OrderDiscount'
      ,MAX([ItemDiscount]) AS 'ItemDiscount'
      ,MAX([InvoiceAmount]) AS 'InvoiceAmount'
      ,[InvoiceBillTo]
      ,[InvoiceNumber]
      ,[InvoiceDate]
      ,[CurrencyMultiplier]
      --,[BillToFName]
      --,[BillToLName]
      --,[BillToAddress1]
      --,[BillToAddress2]
      --,[BillToCity]
      --,[BillToState]
      --,[BillToPostalCode]
      --,[BillToCountry]
      ,[BillToEmail]
      --,[BillToPhone]
      --,[ShipToFName]
      --,[ShipToLName]
      --,[ShipToAddress1]
      --,[ShipToAddress2]
      --,[ShipToCity]
      --,[ShipToState]
      --,[ShipToPostalCode]
      --,[ShipToCountry]
      --,[ShipToEmail]
      --,[ShipToPhone]
      --,[OrderCustom1]
      --,[OrderCustom2]
      --,[OrderCustom3]
      --,[OrderCustom4]
      --,[OrderCustom5]
      ,[isSAProcessed]
      ,[OrderItemCount]
  into #TransactionDetailAll
  FROM [WebOrderProcessing].[WM].[vwTransactionDetailPayments_All_1_1]
  where datediff(dd, TransactionDate, getdate())<=30
  GROUP BY [TransactionNum]
      ,[OrderNumber]
      ,[TransactionID]
      ,[PaymentTransactionType]
      ,[InvoiceBillTo]
      ,[InvoiceNumber]
      ,[InvoiceDate]
      ,[CurrencyMultiplier]
      --,[BillToFName]
      --,[BillToLName]
      --,[BillToAddress1]
      --,[BillToAddress2]
      --,[BillToCity]
      --,[BillToState]
      --,[BillToPostalCode]
      --,[BillToCountry]
      ,[BillToEmail]
      --,[BillToPhone]
      --,[ShipToFName]
      --,[ShipToLName]
      --,[ShipToAddress1]
      --,[ShipToAddress2]
      --,[ShipToCity]
      --,[ShipToState]
      --,[ShipToPostalCode]
      --,[ShipToCountry]
      --,[ShipToEmail]
      --,[ShipToPhone]
      --,[OrderCustom1]
      --,[OrderCustom2]
      --,[OrderCustom3]
      --,[OrderCustom4]
      --,[OrderCustom5]
      ,[isSAProcessed]
      ,[OrderItemCount]
	 

	  if (object_id('tempdb..#tmpTransactionDetailAll') is not null) drop table #tmpTransactionDetailAll
	 SELECT DISTINCT tda.TransactionNum
      ,tda.OrderNumber
	  ,isnull((tda.TransactionNum + '_' + CAST(ts.ShipmentNumber AS varchar)),tda.TransactionNum) AS 'WMOrderNumber'
      ,tda.[TransactionID]
      ,ts.[ShipmentNumber]
 
      ,[TransactionDate]
      ,[SubTotal]
      ,[Shipping]
      ,[ProcessingFee]
      ,[Tax]
      ,[TotalCharges]
      ,[PaymentTransactionType]
      ,[TransactionAmount]
      ,[OrderDiscount]
      ,[ItemDiscount]
      ,[InvoiceAmount]
      ,[InvoiceBillTo]
      ,[InvoiceNumber]
      ,[InvoiceDate]
      ,[CurrencyMultiplier]
	--,[BillToFName]
 --   ,[BillToLName]
 --   ,[BillToAddress1]
 --   ,[BillToAddress2]
 --   ,[BillToCity]
 --   ,[BillToState]
 --   ,[BillToPostalCode]
 --   ,[BillToCountry]
    ,[BillToEmail]
 --   ,[BillToPhone]
 --   ,[ShipToFName]
 --   ,[ShipToLName]
 --   ,[ShipToAddress1]
 --   ,[ShipToAddress2]
 --   ,[ShipToCity]
 --   ,[ShipToState]
 --   ,[ShipToPostalCode]
 --   ,[ShipToCountry]
 --   ,[ShipToEmail]
 --   ,[ShipToPhone]
	--,[OrderCustom1]
 --   ,[OrderCustom2]
 --   ,[OrderCustom3]
 --   ,[OrderCustom4]
 --   ,[OrderCustom5]
	  ,[isSAProcessed]
	  into #tmpTransactionDetailAll
	  FROM #TransactionShipmentUnion ts
	  CROSS JOIN #TransactionDetailAll tda 
	  WHERE ts.TransactionNum = tda.TransactionNum-- AND tda.TransactionNum = 'U0255847'
	  ORDER BY TransactionDate

--------------------------------------- 

--sql used in vwDWFlashGaapWebV2 that is use to populate dw.Sales_GAAP_RawFromStoreServer for Accounting 'flash gaap sales
--except now includes additional details from columns above
		if (object_id('tempdb..#SettledOrders') is not null) drop table #SettledOrders
		select 
			sOrderNumber OrderNumber
		into #SettledOrders
		from BABWeCommerce.dbo.NSBTranslate_LogTrans with (nolock)
		where 1=1 
		and datediff(dd, dTimeStamp, getdate()) <= 30
		group by sOrderNumber

		if (object_id('tempdb..#SourceSite') is not null) drop table #SourceSite
		select 
			o.TransactionID,
			case when right(o.SourceSite,2) = 'US' then '0013' else '2013' end as LocationCode,
			case when right(o.SourceSite,2) = 'US' then 'US Web' else 'UK Web' end as LocationName,
			case when right(o.SourceSite,2) = 'US' then 13 else 2013 end as StoreNumber
		into #SourceSite
		from wm.Orders o with (nolock)
		where 1=1
		and exists (select so.OrderNumber from #SettledOrders so where left(so.OrderNumber,8) = left(o.OrderNum,8))
		group by 
			o.TransactionID, 
			o.SourceSite,
			cast(left(o.EnterpriseSellingID, 19) as varchar(19))

		if (object_id('tempdb..#RefNums') is not null) drop table #RefNums
		select 
			o.TransactionID, 
			cast(left(o.EnterpriseSellingID, 19) as varchar(19)) as ESReferenceNo
		into #RefNums
		from wm.Orders o with(nolock) 
		where 1=1
		and datediff(dd, o.OrderDate, getdate()) <= 30
		and o.EnterpriseSellingID is not NULL
		group by 
			o.TransactionID, 
			cast(left(o.EnterpriseSellingID, 19) as varchar(19))

        if (object_id('tempdb..#PartyExclude') is not null) drop table #PartyExclude
		select rf.TransactionID
		into #PartyExclude
		from babwpartyPlanner.dbo.PartyEnterpriseSellingXRef p with (nolock)
		join #RefNums rf on left(p.EnterpriseSellingID,19) = rf.ESReferenceNo

		if (object_id('tempdb..#SettledSales') is not null) drop table #SettledSales
		select 
			vw.TransactionID,
			vw.WMOrderNumber,
			vw.TransactionDate,
			vw.[InvoiceDate],
			vw.[InvoiceNumber],
			vw.[PaymentTransactionType],
			(vw.[InvoiceAmount]*vw.CurrencyMultiplier) InvoiceAmount,
			(vw.[SubTotal]*vw.CurrencyMultiplier) SubTotal,
			(vw.[Shipping]*vw.CurrencyMultiplier) Shipping,
			(vw.[ProcessingFee]*vw.CurrencyMultiplier) ProcessingFee,
			(vw.[Tax] *vw.CurrencyMultiplier) Tax,
			(vw.[TransactionAmount]*vw.CurrencyMultiplier) TransactionAmount,
			(vw.[OrderDiscount]*vw.CurrencyMultiplier) OrderDiscount,
			(vw.[ItemDiscount]*vw.CurrencyMultiplier) ItemDiscount,
			(vw.TotalCharges*vw.CurrencyMultiplier) TotalCharges
		into #SettledSales
		from #tmpTransactionDetailAll vw
		where 1=1
		and substring(vw.WMOrderNumber, 9,1) = '_'
		and vw.isSAProcessed = 1
		and vw.BillToEmail <> 'guest.services@buildabear.com'
		and exists (select so.OrderNumber from #SettledOrders so where left(so.OrderNumber,8) = left(vw.WMOrderNumber,8)) 
	
if (object_id('WebOrderProcessing..tmpWebSaleDetails') is not null) drop table tmpWebSaleDetails
select 
	ss.LocationCode,
	ss.LocationName,
	ss.TransactionID as RetailTransactionID,
	ss.StoreNumber,
	ss.TransactionID as RetailTransactionNumber,
	sss.TransactionID,
	sss.WMOrderNumber,
	sss.TransactionDate,
	sss.[InvoiceDate],
	sss.[InvoiceNumber],
	sss.[PaymentTransactionType],
	sss.InvoiceAmount,
	sss.SubTotal,
	sss.Shipping,
	sss.ProcessingFee,
	sss.Tax,
	sss.TransactionAmount,
	sss.OrderDiscount,
	sss.ItemDiscount,
	sss.TotalCharges
into tmpWebSaleDetails
from #SourceSite ss
join #SettledSales sss on ss.TransactionID=sss.TransactionID
where not exists (select pe.TransactionID from #PartyExclude pe where pe.TransactionID = ss.TransactionID)
```

