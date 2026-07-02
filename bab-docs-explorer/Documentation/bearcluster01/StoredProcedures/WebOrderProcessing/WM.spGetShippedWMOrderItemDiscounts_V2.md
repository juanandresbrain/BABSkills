# WM.spGetShippedWMOrderItemDiscounts_V2

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetShippedWMOrderItemDiscounts_V2"]
    WM_ItemDiscounts(["WM.ItemDiscounts"]) --> SP
    WM_vwDistinctItemStatuses(["WM.vwDistinctItemStatuses"]) --> SP
    WM_vwDistinctOrderItems(["WM.vwDistinctOrderItems"]) --> SP
    WM_vwTransactionDetail_V2(["WM.vwTransactionDetail_V2"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ItemDiscounts |
| WM.vwDistinctItemStatuses |
| WM.vwDistinctOrderItems |
| WM.vwTransactionDetail_V2 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetShippedWMOrderItemDiscounts_V2] 

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

	SELECT DISTINCT[OrderNumber]
	      ,id.[OrderItemID]
          ,[PromoCode]
          ,[DiscountAmount]
          ,[IsOrderDiscount]
          ,[DiscountName]
		  ,v.CurrencyMultiplier
	FROM [WebOrderProcessing].[WM].[vwTransactionDetail_V2] v
	LEFT JOIN [WebOrderProcessing].[WM].[vwDistinctOrderItems] oi ON v.TransactionID = oi.TransactionID
	RIGHT JOIN [WebOrderProcessing].[WM].[vwDistinctItemStatuses] ist ON oi.OrderItemID = ist.OrderItemID
	LEFT JOIN [WebOrderProcessing].[WM].[ItemDiscounts] id ON oi.OrderItemID = id.OrderItemID
	WHERE DiscountAmount IS NOT NULL AND PaymentTransactionType NOT IN ('Credit')
	AND oi.sku NOT LIKE ('_______%')

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

