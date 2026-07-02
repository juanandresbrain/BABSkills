# WM.spGetPreviousWMOrderItemDiscounts

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetPreviousWMOrderItemDiscounts"]
    WM_ItemDiscounts(["WM.ItemDiscounts"]) --> SP
    WM_ItemStatus(["WM.ItemStatus"]) --> SP
    WM_OrderItems(["WM.OrderItems"]) --> SP
    WM_vwTransactionDetail(["WM.vwTransactionDetail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ItemDiscounts |
| WM.ItemStatus |
| WM.OrderItems |
| WM.vwTransactionDetail |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetPreviousWMOrderItemDiscounts] 

-- =============================================================================================================
-- Name: WM.spGetPreviousWMOrderItemDiscounts
--
-- Description:	Get Previous WM Orders Item Discounts for Sales Audit Translate
--
-- Output: 
--	
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		9/10/2017		Initial Creation
-- =============================================================================================================

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT DISTINCT[OrderNumber]
	      ,id.[OrderItemID]
          ,[PromoCode]
          ,[DiscountAmount]
          ,[IsOrderDiscount]
          ,[DiscountName]
		  ,v.CurrencyMultiplier
	FROM [WebOrderProcessing].[WM].[vwTransactionDetail] v
	LEFT JOIN [WebOrderProcessing].[WM].[OrderItems] oi ON v.TransactionID = oi.TransactionID
	RIGHT JOIN [WebOrderProcessing].[WM].[ItemStatus] ist ON oi.OrderItemID = ist.OrderItemID AND v.OrderTransactionIdentifier = ist.OrderTransactionIdentifier
	LEFT JOIN [WebOrderProcessing].[WM].[ItemDiscounts] id ON oi.OrderItemID = id.OrderItemID
	WHERE DiscountAmount IS NOT NULL AND ist.Status IN ('IR')

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

