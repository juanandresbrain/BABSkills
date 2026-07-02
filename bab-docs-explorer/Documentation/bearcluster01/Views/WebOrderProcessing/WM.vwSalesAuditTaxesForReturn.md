# WM.vwSalesAuditTaxesForReturn

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwSalesAuditTaxesForReturn"]
    WM_OMSTransactionDetails(["WM.OMSTransactionDetails"]) --> VIEW
    WM_Transactions(["WM.Transactions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.OMSTransactionDetails |
| WM.Transactions |

## View Code

```sql
CREATE VIEW [WM].[vwSalesAuditTaxesForReturn]
AS

  WITH WMOrdersWithPrevTrans (
	TransactionID
   ,OrderTransactionIdentifier
   ,PreviousOrderTransactionIdentifier
  )
  AS
  (
  SELECT td.[TransactionID]
		,td.OrderTransactionIdentifier
		,MAX(ptd.OrderTransactionIdentifier) AS 'PreviousOrderTransactionIdentifier'
  FROM [WebOrderProcessing].[WM].[OMSTransactionDetails] td
  LEFT JOIN [WebOrderProcessing].[WM].[OMSTransactionDetails] ptd ON td.TransactionID = ptd.TransactionID AND ptd.OrderTransactionIdentifier < td.OrderTransactionIdentifier
  LEFT JOIN [WebOrderProcessing].[WM].[Transactions]	t ON td.TransactionID = t.TransactionID
  WHERE ptd.OrderTransactionIdentifier IS NOT NULL
  --WHERE TransactionNum = '00041209' AND ptd.PaymentTransactionType NOT IN ('sales')
  GROUP BY td.[TransactionID], td.OrderTransactionIdentifier)
  SELECT t.TransactionNum + '_' + CAST(td.[OrderTransactionIdentifier] AS VARCHAR) AS 'OrderNumber'
	    ,td.[Tax] AS 'TaxAmount'
		,ptd.[Tax] AS 'PreviousTaxAmount'
        ,[TaxJurisdiction]
        ,[TaxAuthority]
        ,[TaxType]
		,td.[CurrencyMultiplier]
		,td.[PaymentTransactionType]
		,t.TransactionID
		,td.[OrderTransactionIdentifier]
		,ptd.[OrderTransactionIdentifier] AS 'PreviousOrderTransactionIdentifier'
  FROM WMOrdersWithPrevTrans cte
  LEFT JOIN [WebOrderProcessing].[WM].[OMSTransactionDetails]  td ON td.TransactionID = cte.TransactionID AND td.OrderTransactionIdentifier = cte.OrderTransactionIdentifier
  LEFT JOIN [WebOrderProcessing].[WM].[OMSTransactionDetails]  ptd ON ptd.TransactionID = cte.TransactionID AND ptd.OrderTransactionIdentifier = cte.PreviousOrderTransactionIdentifier
  LEFT JOIN [WebOrderProcessing].[WM].[Transactions] t ON td.TransactionID = t.TransactionID
   --WHERE TaxJurisdiction NOT IN ('GB', 'IR') 
  
  

 -- SELECT t.TransactionNum + '_' + CAST(td.[OrderTransactionIdentifier] AS VARCHAR) AS 'OrderNumber'
	--    ,[Tax] AS 'TaxAmount'
 --       ,[TaxJurisdiction]
 --       ,[TaxAuthority]
 --       ,[TaxType]
	--	,[CurrencyMultiplier]
	--	,[PaymentTransactionType]
	--	,t.TransactionID
	--	,[OrderTransactionIdentifier]
 -- FROM [WebOrderProcessing].[WM].[OMSTransactionDetails] td
```

