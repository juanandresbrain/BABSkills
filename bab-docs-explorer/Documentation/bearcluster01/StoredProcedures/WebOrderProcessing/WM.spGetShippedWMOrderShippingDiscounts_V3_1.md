# WM.spGetShippedWMOrderShippingDiscounts_V3_1

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetShippedWMOrderShippingDiscounts_V3_1"]
    WM_ShippingDiscounts(["WM.ShippingDiscounts"]) --> SP
    WM_tmpOrderOrderTransactionIdentifier(["WM.tmpOrderOrderTransactionIdentifier"]) --> SP
    WM_vwTransactionDetailPayments_V2(["WM.vwTransactionDetailPayments_V2"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.ShippingDiscounts |
| WM.tmpOrderOrderTransactionIdentifier |
| WM.vwTransactionDetailPayments_V2 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetShippedWMOrderShippingDiscounts_V3_1] 

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

	SELECT DISTINCT o.[OrderNumber]
      ,[PromoCode]
      ,[DiscountAmount]
      ,[DiscountName]
	  ,[CurrencyMultiplier]
	FROM [WebOrderProcessing].[WM].[vwTransactionDetailPayments_V2] v
	INNER JOIN [WebOrderProcessing].[WM].[tmpOrderOrderTransactionIdentifier] o ON v.TransactionID = o.TransactionID AND v.OrderTransactionIdentifier = o.OrderTransactionIdentifier
	--LEFT JOIN [WebOrderProcessing].[WM].[Orders] o ON v.TransactionID = o.TransactionID
	LEFT JOIN [WebOrderProcessing].[WM].[ShippingDiscounts] sd ON o.OrderID = sd.OrderID
	WHERE DiscountAmount IS NOT NULL AND DiscountName NOT IN ('ShippingManualCredit')
	AND v.OmsTransactionType NOT IN ('OrderManualCredit', 'ShippingManualCredit', 'ItemManualCredit')

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

