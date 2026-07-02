# WM.vwTransactionDetailPayments_BJB_DeleteAfter20180305

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WM.vwTransactionDetailPayments_BJB_DeleteAfter20180305"]
    WM_OMSTransactionDetails(["WM.OMSTransactionDetails"]) --> VIEW
    WM_Transactions(["WM.Transactions"]) --> VIEW
    WM_vwDistinctItemStatuses(["WM.vwDistinctItemStatuses"]) --> VIEW
    WM_vwDistinctOrderItems(["WM.vwDistinctOrderItems"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WM.OMSTransactionDetails |
| WM.Transactions |
| WM.vwDistinctItemStatuses |
| WM.vwDistinctOrderItems |

## View Code

```sql
CREATE VIEW [WM].[vwTransactionDetailPayments_BJB_DeleteAfter20180305]
AS

  WITH OrderItemsCount([TransactionID]
	    		   --,[OrderTransactionIdentifier]
				   ,[OrderItemCount])
  AS (SELECT [TransactionID]
		    --,MAX(ist.OrderTransactionIdentifier)
		    ,COUNT(TransactionID) AS 'OrderItemCount'
  FROM [WebOrderProcessing].[WM].[vwDistinctOrderItems] oi
  INNER JOIN [WebOrderProcessing].[WM].[vwDistinctItemStatuses] ist ON oi.OrderItemID = ist.OrderItemID
  --WHERE TransactionID = 275660
  GROUP BY [TransactionID])
  ,TransactionDetail(TansactionDetailID
                    ,TransactionNum
                    ,OrderNumber
                    ,[TransactionID]
                    --,[ShipmentNumber]
                    ,[OrderTransactionIdentifier]
                    ,[TransactionDate]
                    ,[SubTotal]
                    ,[Shipping]
                    ,[ProcessingFee]
                    ,[Tax]
                    ,[TotalCharges]
                    ,[PaymentTransactionType]
                    ,[PaymentType]
                    ,[TransactionAmount]
                    ,[OrderDiscount]
                    ,[ItemDiscount]
                    ,[InvoiceAmount]
                    ,[InvoiceBillTo]
                    ,[InvoiceNumber]
                    ,[InvoiceDate]
                    ,[Processor]
                    ,[CurrencyMultiplier]
                    --,[OmsTransactionType]
                    ,[PaymentGeneric1]
                    ,[PaymentGeneric2]
                    ,[PaymentGeneric3]
                    ,[PaymentGeneric4]
                    ,[PaymentGeneric5]
                    ,[TransactionGeneric1]
                    ,[TransactionGeneric2]
                    ,[TransactionGeneric3]
                    ,[TransactionGeneric4]
                    ,[TransactionGeneric5]
	                ,[BillToFName]
                    ,[BillToLName]
                    ,[BillToAddress1]
                    ,[BillToAddress2]
                    ,[BillToCity]
                    ,[BillToState]
                    ,[BillToPostalCode]
                    ,[BillToCountry]
                    ,[BillToEmail]
                    ,[BillToPhone]
                    ,[ShipToFName]
                    ,[ShipToLName]
                    ,[ShipToAddress1]
                    ,[ShipToAddress2]
                    ,[ShipToCity]
                    ,[ShipToState]
                    ,[ShipToPostalCode]
                    ,[ShipToCountry]
                    ,[ShipToEmail]
                    ,[ShipToPhone]
	                ,[OrderCustom1]
                    ,[OrderCustom2]
                    ,[OrderCustom3]
                    ,[OrderCustom4]
                    ,[OrderCustom5]
	                ,[isSAProcessed])
  AS(SELECT MAX(TansactionDetailID)
      ,t.TransactionNum
      ,t.TransactionNum + '_' + CAST(MAX(td.[OrderTransactionIdentifier]) AS VARCHAR) AS 'OrderNumber'
      ,td.[TransactionID]
	  --,ROW_NUMBER() OVER(PARTITION BY [TransactionNum] ORDER BY [PaymentType]) AS 'OrderTransactionIdentifier'
      --,MAX(td.[ShipmentNumber]) AS Sh
      ,MAX(td.[OrderTransactionIdentifier]) AS 'OrderTransactionIdentifier'
      ,[TransactionDate]
      ,SUM([SubTotal]*[CurrencyMultiplier]) AS 'SubTotal'
      ,SUM([Shipping]*[CurrencyMultiplier]) AS 'Shipping'
      ,SUM([ProcessingFee]*[CurrencyMultiplier]) AS 'ProcessingFee'
      ,SUM([Tax]*[CurrencyMultiplier]) AS 'Tax'
      ,SUM([TotalCharges]*[CurrencyMultiplier]) AS 'TotalCharges'
      ,MAX([PaymentTransactionType]) AS 'PaymentTransactionType'
      ,[PaymentType]
      ,SUM([TransactionAmount]*[CurrencyMultiplier]) AS 'TransactionAmount'
      ,SUM([OrderDiscount]*[CurrencyMultiplier]) AS 'OrderDiscount'
      ,SUM([ItemDiscount]*[CurrencyMultiplier]) AS 'ItemDiscount'
      ,SUM([InvoiceAmount]*[CurrencyMultiplier]) AS 'InvoiceAmount'
      ,[InvoiceBillTo]
      ,[InvoiceNumber]
      ,[InvoiceDate]
      ,[Processor]
      ,MAX([CurrencyMultiplier]) AS 'CurrencyMultiplier'
      --,[OmsTransactionType]
      ,[PaymentGeneric1]
      ,[PaymentGeneric2]
      ,[PaymentGeneric3]
      ,[PaymentGeneric4]
      ,[PaymentGeneric5]
      ,[TransactionGeneric1]
      ,[TransactionGeneric2]
      ,[TransactionGeneric3]
      ,[TransactionGeneric4]
      ,[TransactionGeneric5]
	  ,[BillToFName]
      ,[BillToLName]
      ,[BillToAddress1]
      ,[BillToAddress2]
      ,[BillToCity]
      ,[BillToState]
      ,[BillToPostalCode]
      ,[BillToCountry]
      ,[BillToEmail]
      ,[BillToPhone]
      ,[ShipToFName]
      ,[ShipToLName]
      ,[ShipToAddress1]
      ,[ShipToAddress2]
      ,[ShipToCity]
      ,[ShipToState]
      ,[ShipToPostalCode]
      ,[ShipToCountry]
      ,[ShipToEmail]
      ,[ShipToPhone]
	  ,[OrderCustom1]
      ,[OrderCustom2]
      ,[OrderCustom3]
      ,[OrderCustom4]
      ,[OrderCustom5]
	  ,[isSAProcessed]
  FROM [WebOrderProcessing].[WM].[OMSTransactionDetails] td
  LEFT JOIN [WebOrderProcessing].[WM].[Transactions] t ON td.TransactionID = t.TransactionID
  WHERE TransactionNum NOT LIKE '7_______'
  AND isSAProcessed = 0 
  --OR TransactionNum = 'W0203477'
  --AND TransactionNum = 'W0203477'
  --AND TransactionNum = 'W0047195'
  GROUP BY t.TransactionNum, td.[TransactionID], [TransactionDate]
      --, [PaymentTransactionType]
	  , [PaymentType], [InvoiceBillTo], [InvoiceNumber], [InvoiceDate], [Processor]
	  --, [CurrencyMultiplier]
	  --,[OmsTransactionType]
	  ,[PaymentGeneric1]
      ,[PaymentGeneric2], [PaymentGeneric3], [PaymentGeneric4], [PaymentGeneric5], [TransactionGeneric1], [TransactionGeneric2], [TransactionGeneric3], [TransactionGeneric4], [TransactionGeneric5]
	  ,[BillToFName], [BillToLName], [BillToAddress1], [BillToAddress2], [BillToCity], [BillToState], [BillToPostalCode], [BillToCountry], [BillToEmail], [BillToPhone], [ShipToFName], [ShipToLName]
      ,[ShipToAddress1], [ShipToAddress2], [ShipToCity], [ShipToState], [ShipToPostalCode], [ShipToCountry], [ShipToEmail], [ShipToPhone], [OrderCustom1], [OrderCustom2], [OrderCustom3]
      ,[OrderCustom4], [OrderCustom5], [isSAProcessed]
  )
  , TransactionDetailWithItemCount(TansactionDetailID
                    ,TransactionNum
                    ,OrderNumber
                    ,[TransactionID]
                    --,[ShipmentNumber]
                    ,[OrderTransactionIdentifier]
					--,[PaymentID]
                    ,[TransactionDate]
                    ,[SubTotal]
                    ,[Shipping]
                    ,[ProcessingFee]
                    ,[Tax]
                    ,[TotalCharges]
                    ,[PaymentTransactionType]
                    ,[PaymentType]
                    ,[TransactionAmount]
                    ,[OrderDiscount]
                    ,[ItemDiscount]
                    ,[InvoiceAmount]
                    ,[InvoiceBillTo]
                    ,[InvoiceNumber]
                    ,[InvoiceDate]
                    ,[Processor]
                    ,[CurrencyMultiplier]
                    --,[OmsTransactionType]
                    ,[PaymentGeneric1]
                    ,[PaymentGeneric2]
                    ,[PaymentGeneric3]
                    ,[PaymentGeneric4]
                    ,[PaymentGeneric5]
                    ,[TransactionGeneric1]
                    ,[TransactionGeneric2]
                    ,[TransactionGeneric3]
                    ,[TransactionGeneric4]
                    ,[TransactionGeneric5]
	                ,[BillToFName]
                    ,[BillToLName]
                    ,[BillToAddress1]
                    ,[BillToAddress2]
                    ,[BillToCity]
                    ,[BillToState]
                    ,[BillToPostalCode]
                    ,[BillToCountry]
                    ,[BillToEmail]
                    ,[BillToPhone]
                    ,[ShipToFName]
                    ,[ShipToLName]
                    ,[ShipToAddress1]
                    ,[ShipToAddress2]
                    ,[ShipToCity]
                    ,[ShipToState]
                    ,[ShipToPostalCode]
                    ,[ShipToCountry]
                    ,[ShipToEmail]
                    ,[ShipToPhone]
	                ,[OrderCustom1]
                    ,[OrderCustom2]
                    ,[OrderCustom3]
                    ,[OrderCustom4]
                    ,[OrderCustom5]
	                ,[isSAProcessed]
					,[OrderItemCount]
					)
  AS(SELECT td.*, ISNULL(oic.OrderItemCount, 0)
  FROM TransactionDetail td
  LEFT JOIN OrderItemsCount oic ON td.TransactionID = oic.TransactionID-- AND td.OrderTransactionIdentifier = oic.OrderTransactionIdentifier
  )
  SELECT TOP 100 PERCENT TansactionDetailID
                    ,TransactionNum
                    --,[OrderNumber] + '_' + CAST([OrderTransactionIdentifier] AS VARCHAR) AS 'OrderNumber'
					,[OrderNumber]
                    ,[TransactionID]
                    --,[ShipmentNumber]
                    ,[OrderTransactionIdentifier]
					--,ROW_NUMBER() OVER(PARTITION BY [OrderNumber] ORDER BY [PaymentType]) AS 'PaymentID'
                    ,[TransactionDate]
                    ,CASE 
					  WHEN [SubTotal] < 0 THEN [SubTotal] * -1
					  ELSE [SubTotal]
					 END AS 'SubTotal'
                    ,CASE 
					  WHEN [Shipping] < 0 THEN [Shipping] * -1
					  ELSE [Shipping]
					 END AS 'Shipping'
                    ,CASE 
					  WHEN [ProcessingFee] < 0 THEN [ProcessingFee] * -1
					  ELSE [ProcessingFee]
					 END AS 'ProcessingFee'
                    ,CASE 
					  WHEN [Tax] < 0 THEN [Tax] * -1
					  ELSE [Tax]
					 END AS 'Tax'
                    ,CASE 
					  WHEN [TotalCharges] < 0 THEN [TotalCharges] * -1
					  ELSE [TotalCharges]
					 END AS 'TotalCharges'
                    ,[PaymentTransactionType]
                    ,[PaymentType]
                    ,CASE
					  WHEN [TransactionAmount] < 0 THEN [TransactionAmount] * -1
					  ELSE [TransactionAmount]
					 END AS 'TransactionAmount'
                    ,CASE
					  WHEN [OrderDiscount] < 0 THEN [OrderDiscount] * -1
					  ELSE [OrderDiscount]
					 END AS 'OrderDiscount'
                    ,CASE
					  WHEN [ItemDiscount] < 0 THEN [ItemDiscount] * -1
					  ELSE [ItemDiscount]
					 END AS 'ItemDiscount'
                    ,CASE 
					  WHEN [InvoiceAmount] < 0 THEN [InvoiceAmount] * -1
					  ELSE [InvoiceAmount]
					 END AS 'InvoiceAmount'
                    ,[InvoiceBillTo]
                    ,[InvoiceNumber]
                    ,[InvoiceDate]
                    ,[Processor]
                    ,[CurrencyMultiplier]
                    --,[OmsTransactionType]
                    ,[PaymentGeneric1]
                    ,[PaymentGeneric2]
                    ,[PaymentGeneric3]
                    ,[PaymentGeneric4]
                    ,[PaymentGeneric5]
                    ,[TransactionGeneric1]
                    ,[TransactionGeneric2]
                    ,[TransactionGeneric3]
                    ,[TransactionGeneric4]
                    ,[TransactionGeneric5]
	                ,[BillToFName]
                    ,[BillToLName]
                    ,[BillToAddress1]
                    ,[BillToAddress2]
                    ,[BillToCity]
                    ,[BillToState]
                    ,[BillToPostalCode]
                    ,[BillToCountry]
                    ,[BillToEmail]
                    ,[BillToPhone]
                    ,[ShipToFName]
                    ,[ShipToLName]
                    ,[ShipToAddress1]
                    ,[ShipToAddress2]
                    ,[ShipToCity]
                    ,[ShipToState]
                    ,[ShipToPostalCode]
                    ,[ShipToCountry]
                    ,[ShipToEmail]
                    ,[ShipToPhone]
	                ,[OrderCustom1]
                    ,[OrderCustom2]
                    ,[OrderCustom3]
                    ,[OrderCustom4]
                    ,[OrderCustom5]
	                ,[isSAProcessed]
					,[OrderItemCount] 
  FROM TransactionDetailWithItemCount
  WHERE (OrderItemCount > 0 AND PaymentTransactionType IN ('sales', 'return')) OR PaymentTransactionType IN ('credit')
  ORDER BY TransactionDate, OrderNumber
```

