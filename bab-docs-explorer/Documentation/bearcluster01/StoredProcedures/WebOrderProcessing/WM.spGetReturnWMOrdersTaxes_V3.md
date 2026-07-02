# WM.spGetReturnWMOrdersTaxes_V3

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetReturnWMOrdersTaxes_V3"]
    WM_OMSTransactionDetails(["WM.OMSTransactionDetails"]) --> SP
    WM_Orders(["WM.Orders"]) --> SP
    WM_Transactions(["WM.Transactions"]) --> SP
    WM_vwOrderOrderTransactionIdentifier(["WM.vwOrderOrderTransactionIdentifier"]) --> SP
    WM_vwTransactionDetailPayments_V2(["WM.vwTransactionDetailPayments_V2"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.OMSTransactionDetails |
| WM.Orders |
| WM.Transactions |
| WM.vwOrderOrderTransactionIdentifier |
| WM.vwTransactionDetailPayments_V2 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetReturnWMOrdersTaxes_V3]

-- =============================================================================================================
-- Name: spGetShippedWMOrdersTaxes
--
-- Description:	Get Shipped WM Orders Taxes for Sales Audit Translate
--
-- Output: 
--	
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		9/10/2017		Initial Creation
--		Ben Barud		10/16/2017		Added Canada Non-Taxable States to TaxJurisdiction exclusions
--		Ben Barud		10/25/2017		If tax is 0.0, exclude.
--		Ben Barud		10/25/2017		APO Tax Jurisdictions are coming in as AP.  Added case to change AP to APO.
--		Ben Barud		02/20/2018		No longer using vwSalesAuditTaxesForReturn_V2.  It would error out when joining
--									    to find orders with previous transactions.  Selecting everything into a temp
--										table and creating the view using CTE's
-- =============================================================================================================

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

  SET NOCOUNT ON;
  WITH OrderNumberPickupStore(OrderNumber, TransactionID, PickupStore)
  AS
  (
  SELECT MAX(o.OrderNum) AS OrderNumber
     ,td.TransactionID
     ,v.PickupStore
  FROM [WebOrderProcessing].[WM].[vwTransactionDetailPayments_V2] td
  INNER JOIN [WebOrderProcessing].[WM].[vwOrderOrderTransactionIdentifier] v ON td.TransactionID = v.TransactionID AND td.OrderTransactionIdentifier = v.OrderTransactionIdentifier
  INNER JOIN [WebOrderProcessing].[WM].[Orders] o ON v.TransactionID = o.TransactionID AND v.PickupStore = o.PickupStore AND OrderStatus IN ('Complete', 'Shipped', 'StorePickedForPickup')
  GROUP BY td.TransactionID, v.PickupStore
  ), WMOrdersWithPrevTrans (
	TransactionID
   ,OrderTransactionIdentifier
   ,PreviousOrderTransactionIdentifier
  )
  AS
  (
  SELECT td.[TransactionID]
		,td.OrderTransactionIdentifier AS 'OrderTransactionIdentifier'
		,MAX(ptd.OrderTransactionIdentifier) AS 'PreviousOrderTransactionIdentifier'
  FROM [WebOrderProcessing].[WM].[OMSTransactionDetails] td
  LEFT JOIN [WebOrderProcessing].[WM].[OMSTransactionDetails] ptd ON td.TransactionID = ptd.TransactionID AND ptd.OrderTransactionIdentifier < td.OrderTransactionIdentifier AND ptd.PaymentTransactionType <> td.PaymentTransactionType
  LEFT JOIN [WebOrderProcessing].[WM].[Transactions]	t ON td.TransactionID = t.TransactionID
  WHERE ptd.OrderTransactionIdentifier IS NOT NULL
  --WHERE ptd.TansactionDetailID IS NOT NULL AND td.PaymentTransactionType = 'return'
  --WHERE TransactionNum = '00041209' AND ptd.PaymentTransactionType NOT IN ('sales')
  GROUP BY td.[TransactionID], td.PaymentTransactionType, ptd.PaymentTransactionType, td.OrderTransactionIdentifier)
  , SalesAuditTaxesForReturn ( OrderNumber
							,TaxAmount
							,PreviousTaxAmount
							,TaxJurisdiction
							,TaxAuthority
							,TaxType
							,CurrencyMultiplier
							,PaymentTransactionType
							,TransactionID
							,OrderTransactionIdentifier
							,PreviousOrderTransactionIdentifier
  )
  AS
  (SELECT t.TransactionNum AS 'OrderNumber'
	    ,td.[Tax] AS 'TaxAmount'
		,ptd.[Tax] AS 'PreviousTaxAmount'
        ,[TaxJurisdiction]
        ,[TaxAuthority]
        ,[TaxType]
		,td.[CurrencyMultiplier]
		,td.[PaymentTransactionType]
		,t.TransactionID
		,td.OrderTransactionIdentifier AS 'OrderTransactionIdentifier'
		,ptd.OrderTransactionIdentifier AS 'PreviousOrderTransactionIdentifier'
  FROM WMOrdersWithPrevTrans cte
  LEFT JOIN [WebOrderProcessing].[WM].[OMSTransactionDetails] td ON td.TransactionID = cte.TransactionID AND td.OrderTransactionIdentifier = cte.OrderTransactionIdentifier
  LEFT JOIN [WebOrderProcessing].[WM].[OMSTransactionDetails]  ptd ON ptd.TransactionID = cte.TransactionID AND ptd.OrderTransactionIdentifier = cte.PreviousOrderTransactionIdentifier
  LEFT JOIN [WebOrderProcessing].[WM].[Transactions] t ON td.TransactionID = t.TransactionID
  )

	SELECT DISTINCT MAX(onps.[OrderNumber]) AS 'OrderNumber'
	      --,p.[OrderTransactionIdentifier]
          ,MAX(p.[PreviousTaxAmount]) AS 'TaxAmount'
          ,CASE
		    WHEN MAX([TaxJurisdiction]) = 'AP' THEN 'APO'
			ELSE MAX([TaxJurisdiction])
		   END AS 'TaxJurisdiction'
          ,MAX([TaxAuthority]) AS 'TaxAuthority'
          ,MAX([TaxType]) AS 'TaxType'
		  ,MAX(p.[CurrencyMultiplier]) AS 'CurrencyMultiplier'
		  ,v.PaymentTransactionType
	FROM OrderNumberPickupStore onps
    INNER JOIN [WebOrderProcessing].[WM].vwTransactionDetailPayments_V2 v ON onps.TransactionID = v.TransactionID AND v.PaymentTransactionType NOT IN ('credit')
	INNER JOIN [WebOrderProcessing].[WM].[vwOrderOrderTransactionIdentifier] o ON v.TransactionID = o.TransactionID AND v.OrderTransactionIdentifier = o.OrderTransactionIdentifier
	LEFT JOIN SalesAuditTaxesForReturn p ON p.TransactionID = o.TransactionID AND p.OrderTransactionIdentifier = o.OrderTransactionIdentifier
	--INNER JOIN [WebOrderProcessing].[WM].[Transactions] t ON v.TransactionID = t.TransactionID
	WHERE TaxAmount IS NOT NULL AND TaxJurisdiction NOT IN ('AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'EL', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'GB', 'UK', 'AB', 'BC', 'MB', 'NB', 'NS', 'NT', 'ON', 'QC', 'SK', 'NO')
	AND PreviousTaxAmount <> 0.00
	GROUP BY onps.PickupStore, v.TransactionID, v.PaymentTransactionType


	--SELECT DISTINCT c.[OrderNumber]
	--      ,p.[OrderTransactionIdentifier]
 --         ,p.[PreviousTaxAmount] AS 'TaxAmount'
 --         ,CASE
	--	    WHEN [TaxJurisdiction] = 'AP' THEN 'APO'
	--		ELSE [TaxJurisdiction]
	--	   END AS 'TaxJurisdiction'
 --         ,[TaxAuthority]
 --         ,[TaxType]
	--	  ,p.[CurrencyMultiplier] 
	--FROM [WebOrderProcessing].[WM].vwTransactionDetail_V2 c
	--LEFT JOIN [WebOrderProcessing].[WM].vwSalesAuditTaxesForReturn_V2 p ON p.TransactionID = c.TransactionID AND p.OrderTransactionIdentifier = c.TansactionDetailID
	----INNER JOIN [WebOrderProcessing].[WM].[Transactions] t ON v.TransactionID = t.TransactionID
	--WHERE TaxAmount IS NOT NULL AND TaxJurisdiction NOT IN ('AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'EL', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'GB', 'UK', 'AB', 'BC', 'MB', 'NB', 'NS', 'NT', 'ON', 'QC', 'SK', 'NO')
	--AND PreviousTaxAmount <> 0.00


	--WHERE TaxAmount IS NOT NULL AND TaxJurisdiction NOT IN ('GB', 'IE', 'DK', 'SE', 'DE', 'BE', 'FR', 'LU', 'NL', 'NO', 'UK', 'IT')
	--WHERE TaxJurisdiction NOT IN ('GB', 'IE', 'DK', 'SE') AND c.PaymentTransactionType IN ('Return')

	/*OLD LOGIC
    SELECT svs.[TransactionNum]
          ,[TaxAmount]
          ,[TaxJurisdiction]
          ,[TaxAuthority]
          ,[TaxType] 
	FROM [WebOrderProcessing].[WM].[Transactions] t
    LEFT JOIN [WebOrderProcessing].[WM].[vwTransactionsShipments_vs_Shipped] svs ON t.TransactionID = svs.TransactionID
    WHERE svs.ShipmentsCount = svs.ShippedCount
	*/
END
```

