# WM.spGetShippedWMOrderItemDiscounts_V3

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetShippedWMOrderItemDiscounts_V3"]
    WM_ItemDiscounts(["WM.ItemDiscounts"]) --> SP
    WM_ItemStatus(["WM.ItemStatus"]) --> SP
    WM_OrderItems(["WM.OrderItems"]) --> SP
    WM_vwOrderNumPickupStore(["WM.vwOrderNumPickupStore"]) --> SP
    WM_vwTransactionDetailPayments_V2(["WM.vwTransactionDetailPayments_V2"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ItemDiscounts |
| WM.ItemStatus |
| WM.OrderItems |
| WM.vwOrderNumPickupStore |
| WM.vwTransactionDetailPayments_V2 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetShippedWMOrderItemDiscounts_V3] 

-- =============================================================================================================
-- Name: WM.spGetShippedWMOrderItemDiscounts
--
-- Description:	Get Shipped WM Orders Item Discounts for Sales Audit Translate
--
-- Output: 
--	
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		09/10/2017		Initial Creation
--		Ben Barud		10/18/2017		Add logic to exlude discounts on bundle skus
-- =============================================================================================================

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	--WITH OrderNumberPickupStore(OrderNumber, TransactionID, PickupStore)
	--AS
	--(
	--SELECT MAX(v.OrderNumber) AS OrderNumber
	--      ,td.TransactionID
	--	  ,PickupStore
 --   FROM [WebOrderProcessing].[WM].[vwTransactionDetailPayments_V2] td
	--INNER JOIN [WebOrderProcessing].[WM].[vwOrderOrderTransactionIdentifier] v ON td.TransactionID = v.TransactionID AND td.OrderTransactionIdentifier = v.OrderTransactionIdentifier
	--GROUP BY td.TransactionID, PickupStore
	--)
	SELECT DISTINCT onps.[OrderNumber]
	      ,id.[OrderItemID]
          ,[PromoCode]
          ,[DiscountAmount]
          ,[IsOrderDiscount]
          ,[DiscountName]
		  ,v.CurrencyMultiplier
	FROM [WebOrderProcessing].[WM].vwOrderNumPickupStore onps
	INNER JOIN [WebOrderProcessing].[WM].[vwTransactionDetailPayments_V2] v ON onps.TransactionID = v.TransactionID AND onps.OrderTransactionIdentifier = v.OrderTransactionIdentifier
	--INNER JOIN [WebOrderProcessing].[WM].[Orders] o ON v.TransactionID = o.TransactionID --AND o.ShipmentNumber = v.ShipmentNumber
	INNER JOIN [WebOrderProcessing].[WM].[OrderItems] oi ON oi.TransactionID = v.TransactionID
	INNER JOIN [WebOrderProcessing].[WM].[ItemStatus] ist ON oi.OrderItemID = ist.OrderItemID AND v.OrderTransactionIdentifier = ist.OrderTransactionIdentifier AND [Status] NOT IN ('IN', 'RYVUpdated') --AND ist.CurrentStatus = 1
	INNER JOIN [WebOrderProcessing].[WM].[ItemDiscounts] id ON id.OrderItemID = ist.OrderItemID
	WHERE LEN(sku) <= 6 AND DiscountAmount IS NOT NULL AND PaymentTransactionType NOT IN ('credit') AND DiscountName NOT IN ('ItemManualCredit', 'OrderManualCredit')
	--AND oi.sku NOT LIKE ('_______%')

	/*OLD LOGIC
    SELECT [TransactionNum]
	      ,id.[OrderItemID]
          ,[PromoCode]
          ,[DiscountAmount]
          ,[IsOrderDiscount]
          ,[DiscountName]
    FROM [WM].[ItemDiscounts] id
	LEFT JOIN [WM].[OrderItems] oi ON id.OrderItemID = oi.OrderItemID
	LEFT JOIN [WebOrderProcessing].[WM].[Orders] o ON oi.OrderId = o.OrderId
    LEFT JOIN [WebOrderProcessing].[WM].[vwTransactionsShipments_vs_Shipped] svs ON o.TransactionID = svs.TransactionID
    WHERE svs.ShipmentsCount = svs.ShippedCount AND DiscountAmount IS NOT NULL
	*/
END
```

