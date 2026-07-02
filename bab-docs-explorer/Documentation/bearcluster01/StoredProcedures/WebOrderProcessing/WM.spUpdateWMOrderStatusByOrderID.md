# WM.spUpdateWMOrderStatusByOrderID

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spUpdateWMOrderStatusByOrderID"]
    WM_OrderStatus(["WM.OrderStatus"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.OrderStatus |

## Stored Procedure Code

```sql
CREATE PROCEDURE WM.spUpdateWMOrderStatusByOrderID 
	@OrderID AS INT

-- =============================================================================================================
-- Name: spUpdateWMOrderStatusByOrderID
--
-- Description:	Update WM OrderStatus by OrderID
--
-- Output: 
--	
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		8/31/2017		Initial Creation
-- =============================================================================================================

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @currentOrderStatusID AS INT

	SELECT TOP 1 @currentOrderStatusID = OrderStatusID
	FROM WM.OrderStatus
	WHERE OrderID = @OrderID
	ORDER BY CurrentStatus DESC

	INSERT INTO WM.OrderStatus (OrderId, [Status], StatusDate, CurrentStatus)
	VALUES(@OrderID, 'SalesAuditComplete', GETDATE(), 1) 
	SELECT TOP 1 * FROM wm.OrderStatus

	UPDATE WM.OrderStatus
	SET CurrentStatus = 0
	WHERE OrderStatusId = @currentOrderStatusID

END
```

