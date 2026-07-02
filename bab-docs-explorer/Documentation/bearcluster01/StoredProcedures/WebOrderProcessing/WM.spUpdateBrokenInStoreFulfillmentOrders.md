# WM.spUpdateBrokenInStoreFulfillmentOrders

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spUpdateBrokenInStoreFulfillmentOrders"]
    WM_Orders(["WM.Orders"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.Orders |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [WM].[spUpdateBrokenInStoreFulfillmentOrders] 

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	UPDATE o2
    SET o2.PickupStore = o1.PickupStore
    FROM [WebOrderProcessing].[WM].[Orders] o1 WITH (NOLOCK)
    INNER JOIN [WebOrderProcessing].[WM].[Orders] o2 WITH (NOLOCK) ON o1.OrderNumber = o2.OrderNumber AND o1.ShipmentNumber > o2.ShipmentNumber 
    --WHERE o1.PickupStore <> o2.PickupStore AND o2.ShipmentNumber = 0 AND o2.PickupStore NOT IN ('0013') AND o1.OrderStatus NOT IN ('Complete') AND o1.OrderStatus = ('Shipped')
    WHERE o1.PickupStore <> o2.PickupStore AND o2.ShipmentNumber = 0 
    --AND o2.PickupStore NOT IN ('0013') 
    AND o2.OrderStatus IN ('Complete') 
    AND o1.OrderStatus = ('Shipped')
  
END


WM,spUpdateBrokenOrderItems,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [WM].[spUpdateBrokenOrderItems] 

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	  WITH newItems ([OrderItemID], [OrderId], [ItemDescription], [Note], [Height], [Weight], [FurColor], [EyeColor])
	  AS
	  (
	  SELECT oi.[OrderItemID], oi.[OrderId], [ItemDescription], [Note], [Height], [Weight], [FurColor], [EyeColor]
	  FROM [WebOrderProcessing].[WM].[OrderItems] oi
	  INNER JOIN [WebOrderProcessing].[WM].ItemStatus ist ON oi.OrderItemID = ist.OrderItemID AND oi.OrderId = ist.OrderID
	  WHERE [Status] = 'IN' AND StatusDate > DATEADD(DAY, -1, GETDATE()) 
	  --AND oi.OrderItemID = 24790203
	  ), pWaveItems ([OrderItemID], [OrderId], [ItemDescription], [Note], [Height], [Weight], [FurColor], [EyeColor])
	  AS
	  (
	  SELECT oi.[OrderItemID], MAX(oi.[OrderId]), [ItemDescription], [Note], [Height], [Weight], [FurColor], [EyeColor]
	  FROM [WebOrderProcessing].[WM].[OrderItems] oi
	  INNER JOIN [WebOrderProcessing].[WM].ItemStatus ist ON oi.OrderItemID = ist.OrderItemID AND oi.OrderId = ist.OrderID
	  WHERE [Status] = 'IWVP' AND StatusDate > DATEADD(DAY, -1, GETDATE()) 
	  --AND oi.OrderItemID = 24790203
	  GROUP BY oi.[OrderItemID], [ItemDescription], [Note], [Height],[Weight], [FurColor], [EyeColor]
	  )
	  UPDATE new
	  SET new.[Note] = pending.[Note], new.[Height] = pending.[Height], new.[Weight] = pending.[Weight], new.[FurColor] = pending.[FurColor], new.[EyeColor] = pending.[EyeColor]
	  FROM newItems new
	  INNER JOIN pWaveItems pending ON new.OrderItemID = pending.OrderItemID

	  /*
	  /
	  /  BJB 20231207 Added to temporarily resolve issue with Merry Mission Movie Purchases
	  /
	  */

	  UPDATE [WebOrderProcessing].[WM].[ItemStatus]
	  SET OrderTransactionIdentifier = 1
	  WHERE [Status] = 'MP' AND OrderTransactionIdentifier = -1

	  UPDATE [WebOrderProcessing].[WM].[Orders]
	  SET OrderStatus = 'Complete'
	  WHERE OrderId IN (SELECT o.[OrderID]
		FROM [WebOrderProcessing].[WM].[vwOrderItemStatusPivot_V2] v
		INNER JOIN [WebOrderProcessing].[WM].[Orders] o ON v.OrderID = o.OrderID
		WHERE hasMP = 1 AND hasIZDT = 0
	  ) AND OrderStatus = 'Pending'

	  --


	  UPDATE [WebOrderProcessing].[WM].[OMSTransactionDetails]
	  SET isSAProcessed = 1
      WHERE isSAProcessed = 0 --AND PaymentType = 'Adyen' AND PaymentGeneric1 = 'null'
END
```

