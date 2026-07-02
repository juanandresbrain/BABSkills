# WM.spGetShippedWMOrders_V3

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetShippedWMOrders_V3"]
    WM_Transactions(["WM.Transactions"]) --> SP
    WM_vwOrderNumPickupStore(["WM.vwOrderNumPickupStore"]) --> SP
    WM_vwOrderOrderTransactionIdentifier(["WM.vwOrderOrderTransactionIdentifier"]) --> SP
    WM_vwSalesAuditShippingForReturn(["WM.vwSalesAuditShippingForReturn"]) --> SP
    WM_vwTransactionDetailPayments_V2(["WM.vwTransactionDetailPayments_V2"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.Transactions |
| WM.vwOrderNumPickupStore |
| WM.vwOrderOrderTransactionIdentifier |
| WM.vwSalesAuditShippingForReturn |
| WM.vwTransactionDetailPayments_V2 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetShippedWMOrders_V3]

-- =============================================================================================================
-- Name: sp_GetShippedWMOrders
--
-- Description:	Get Shipped WM Orders for Sales Audit Translate
--
-- Output: 
--	
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		9/1/2017		Initial Creation
--		Ben Barud		11/29/2017		Added logic to resolve return shipping issue when orders are credited.
-- =============================================================================================================

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

		SELECT OrderNumber
	      ,MAX(OrderDate) AS 'OrderDate'
		  ,CASE
		     WHEN SourceSite IS NULL AND LEFT(MAX(OrderNumber), 1) = 'W' THEN 'BABW-US'
			 WHEN SourceSite IS NULL AND LEFT(MAX(OrderNumber), 1) = '1' AND ShipToCountry = 'GBR' THEN 'BABW-UK'
			 WHEN SourceSite IS NULL AND LEFT(MAX(OrderNumber), 1) = '1' THEN 'BABW-US'
			 WHEN SourceSite IS NULL AND LEFT(MAX(OrderNumber), 1) = '7' THEN 'BABW-US'
			 WHEN SourceSite IS NULL AND LEFT(MAX(OrderNumber), 1) = 'U' THEN 'BABW-UK'
			 ELSE SourceSite
		   END AS 'SourceSite'
		  ,MAX(ShippingAmount) AS ShippingAmount
		  ,MAX(PreviousShipping) AS PreviousShipping
		  ,LoyaltyNumber
		  ,CASE
		     WHEN PickupStore IS NULL AND LEFT(MAX(OrderNumber), 1) = 'W' THEN '0013'
			 WHEN PickupStore IS NULL AND LEFT(MAX(OrderNumber), 1) = '1' AND ShipToCountry = 'GBR' THEN '2013'
			 WHEN PickupStore IS NULL AND LEFT(MAX(OrderNumber), 1) = '1' THEN '0013'
			 WHEN PickupStore IS NULL AND LEFT(MAX(OrderNumber), 1) = '7' THEN '0013'
			 WHEN PickupStore IS NULL AND LEFT(MAX(OrderNumber), 1) = 'U' THEN '2013'
			 ELSE PickupStore
		   END AS 'PickupStore'
	--INTO #tmp
	FROM(
	SELECT onps.[OrderNumber]
          ,v.[TransactionDate] AS 'OrderDate'
          ,[SourceSite]
		  ,CASE
		    WHEN v.PaymentTransacTionType IN ('credit', 'return') THEN 0
			ELSE v.[Shipping]
		   END AS 'ShippingAmount'
		  --,v.[Shipping] AS 'ShippingAmount'
		  ,CASE
		    WHEN PaymentTransactionType IN ('sales', 'credit') THEN 0
			ELSE ISNULL(sv.[Shipping], 0) 
		   END AS 'PreviousShipping'
		  --,0 AS 'PreviousShipping'
		  ,t.ClientID AS 'LoyaltyNumber'
		  ,onps.PickupStore
		  ,v.ShipToCountry
	FROM [WebOrderProcessing].[WM].vwOrderNumPickupStore onps
    INNER JOIN [WebOrderProcessing].[WM].vwTransactionDetailPayments_V2 v ON onps.TransactionID = v.TransactionID AND v.OrderTransactionIdentifier = onps.OrderTransactionIdentifier
	INNER JOIN [WebOrderProcessing].[WM].[vwOrderOrderTransactionIdentifier] o ON v.TransactionID = o.TransactionID AND v.OrderTransactionIdentifier = o.OrderTransactionIdentifier
	LEFT JOIN [WebOrderProcessing].[WM].[vwSalesAuditShippingForReturn] sv ON v.TransactionID = sv.TransactionID AND sv.OrderTransactionIdentifier = v.TansactionDetailID
	LEFT JOIN [WebOrderProcessing].[WM].[Transactions] t ON v.TransactionID = t.TransactionID) AS innerQry
	GROUP BY OrderNumber, SourceSite, LoyaltyNumber, PickupStore, ShipToCountry

	/*OLD LOGIC
	SELECT DISTINCT v.[OrderNumber]
          ,v.[TransactionDate] AS 'OrderDate'
          ,[SourceSite]
		  ,v.[Shipping] AS 'ShippingAmount'
		  ,CASE
		    WHEN PaymentTransactionType = 'sales' THEN 0
			ELSE ISNULL(sv.[Shipping], 0) 
		   END AS 'PreviousShipping'
		  ,t.ClientID AS 'LoyaltyNumber'
	FROM [WebOrderProcessing].[WM].[vwTransactionDetail] v
	LEFT JOIN [WebOrderProcessing].[WM].[Orders] o ON v.TransactionID = o.TransactionID
	LEFT JOIN [WebOrderProcessing].[WM].[vwSalesAuditShippingForReturn] sv ON v.TransactionID = sv.TransactionID AND sv.OrderTransactionIdentifier = v.OrderTransactionIdentifier
	LEFT JOIN [WebOrderProcessing].[WM].[Transactions] t ON v.TransactionID = t.TransactionID
	*/


	/*OLD LOGIC
    --SELECT svs.[TransactionNum]
    --      ,[OrderDate]
    --      ,[SourceSite]
    --      ,[ShippingAmount]
    --FROM [WM].[Orders] o
    --LEFT JOIN [WebOrderProcessing].[WM].[vwTransactionsShipments_vs_Shipped] svs ON o.TransactionID = svs.TransactionID
    --WHERE svs.ShipmentsCount = svs.ShippedCount
	*/
END
```

