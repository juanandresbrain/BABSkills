# WM.spGetShippedWMOrderBillTo_V2

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetShippedWMOrderBillTo_V2"]
    WM_vwTransactionDetail_V2(["WM.vwTransactionDetail_V2"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.vwTransactionDetail_V2 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetShippedWMOrderBillTo_V2] 

-- =============================================================================================================
-- Name: WM.spGetShippedWMOrderBillTo
--
-- Description:	Get Shipped WM Orders Customer Bill To for Sales Audit Translate
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

	SELECT [OrderNumber]
	      ,[TransactionID]
          ,[BillToFName]
          ,[BillToLName]
          ,[BillToAddress1]
          ,ISNULL([BillToAddress2], '') AS 'BillToAddress2'
          ,[BillToCity]
          ,[BillToState]
          ,[BillToPostalCode]
          ,[BillToCountry]
          ,[BillToPhone]
          ,[BillToEmail]
	FROM [WebOrderProcessing].[WM].[vwTransactionDetail_V2]

	/*OLD LOGIC
    SELECT svs.[TransactionNum]
          ,[BillToFName]
          ,[BillToLName]
          ,[BillToAddress1]
          ,ISNULL([BillToAddress2], '') AS 'BillToAddress2'
          ,[BillToCity]
          ,[BillToState]
          ,[BillToPostalCode]
          ,[BillToCountry]
          ,[BillToPhone]
          ,[BillToEmail]
  FROM [WM].[Orders] o
  LEFT JOIN [WebOrderProcessing].[WM].[vwTransactionsShipments_vs_Shipped] svs ON o.TransactionID = svs.TransactionID
  WHERE svs.ShipmentsCount = svs.ShippedCount
  */
END
```

