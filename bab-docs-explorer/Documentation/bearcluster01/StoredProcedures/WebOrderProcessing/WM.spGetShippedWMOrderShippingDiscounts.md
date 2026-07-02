# WM.spGetShippedWMOrderShippingDiscounts

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetShippedWMOrderShippingDiscounts"]
    WM_Orders(["WM.Orders"]) --> SP
    WM_ShippingDiscounts(["WM.ShippingDiscounts"]) --> SP
    WM_vwTransactionDetail(["WM.vwTransactionDetail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.Orders |
| WM.ShippingDiscounts |
| WM.vwTransactionDetail |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetShippedWMOrderShippingDiscounts] 

-- =============================================================================================================
-- Name: WM.spGetShippedWMOrderShippingDiscounts
--
-- Description:	Get Shipped WM Orders Shipping Discounts for Sales Audit Translate
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

	SELECT v.[OrderNumber]
      ,[PromoCode]
      ,[DiscountAmount]
      ,[DiscountName]
	  ,[CurrencyMultiplier]
	FROM [WebOrderProcessing].[WM].[vwTransactionDetail] v
	LEFT JOIN [WebOrderProcessing].[WM].[Orders] o ON v.TransactionID = o.TransactionID
	LEFT JOIN [WebOrderProcessing].[WM].[ShippingDiscounts] sd ON o.OrderID = sd.OrderID
	WHERE DiscountAmount IS NOT NULL

	/*OLD LOGIC
    SELECT [TransactionNum]
      ,[PromoCode]
      ,[DiscountAmount]
      ,[DiscountName]
    FROM [WebOrderProcessing].[WM].[ShippingDiscounts] sd
	LEFT JOIN [WebOrderProcessing].[WM].[Orders] o ON sd.OrderId = o.OrderId
    LEFT JOIN [WebOrderProcessing].[WM].[vwTransactionsShipments_vs_Shipped] svs ON o.TransactionID = svs.TransactionID
    WHERE svs.ShipmentsCount = svs.ShippedCount AND DiscountAmount IS NOT NULL
	*/
END
```

