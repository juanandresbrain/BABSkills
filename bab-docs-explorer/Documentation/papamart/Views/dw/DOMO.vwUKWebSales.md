# DOMO.vwUKWebSales

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["DOMO.vwUKWebSales"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_ProductionOrder(["dbo.ProductionOrder"]) --> VIEW
    dbo_ProductionOrderItem(["dbo.ProductionOrderItem"]) --> VIEW
    dbo_ProductionStatus(["dbo.ProductionStatus"]) --> VIEW
    dbo_vwRPT_ProductionOrder(["dbo.vwRPT_ProductionOrder"]) --> VIEW
    dbo_vwRPT_ProductionOrderItem(["dbo.vwRPT_ProductionOrderItem"]) --> VIEW
    dbo_vwRPT_ProductionStatus(["dbo.vwRPT_ProductionStatus"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.ProductionOrder |
| dbo.ProductionOrderItem |
| dbo.ProductionStatus |
| dbo.vwRPT_ProductionOrder |
| dbo.vwRPT_ProductionOrderItem |
| dbo.vwRPT_ProductionStatus |

## View Code

```sql
CREATE VIEW [DOMO].[vwUKWebSales]

AS
-- =============================================================================================================
-- Name: [DOMO].[vwUKWebSales]
--
-- Description: UK Web Sales grouped by date and hour.
-- 
--
--
-- Dependencies: UK Web hourly Sales
--
-- Revision History
--		Name:				Date:			Comments:
--		Brian Byas			6/10/2016		Initial creation
--		Brian Byas			6/22/2016		Removed DPT and developed a beastmode in DOMO
--		Brian Byas			8/22/2016		Added OrdersLY, GAAP SalesLY, NonGAAPSalesLY Columns
-- =============================================================================================================




WITH Orders (actual_date,OrderHour,TotalOrders) AS (
		
		/*
		-- This query returns total orders to current report date and hour
		*/

		SELECT  dd.actual_date,DATEPART(hour, PO.ProductionOrderDateTimeCreated) AS OrderHour, COUNT(*) AS 'TotalOrders'
		FROM [KODIAK].[BABWPMS].dbo.ProductionOrder PO WITH (NOLOCK) INNER JOIN
		PAPAMART.[dw].[dbo].[date_dim] dd WITH(NOLOCK)
			ON CONVERT(VARCHAR(10),PO.ProductionOrderDateTimeCreated,101) = dd.actual_date AND DATEPART(hour, PO.ProductionOrderDateTimeCreated) BETWEEN 0 AND 24 
		WHERE PO.ProductionOrderDateTimeCreated BETWEEN CAST(dateadd(day,-1,CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00') as varchar(20)) AND CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00'
		AND PO.[ProductionOrderSiteCode] = 'BABW_UK'
		AND PO.ProductionOrderBillingFirstName <> 'House Order'
		GROUP BY dd.actual_date,DATEPART(hour, PO.ProductionOrderDateTimeCreated)
		),
OrdersLY (actual_date,OrderHour,TotalOrdersLY) AS (
		
		/*
		-- This query returns total ordersLY  to current report date and hour
		*/

		SELECT  dd.actual_date,DATEPART(hour, PO.ProductionOrderDateTimeCreated) AS OrderHour, COUNT(*) AS 'TotalOrdersLY'
		FROM [KODIAK].[BABWPMS].dbo.vwRPT_ProductionOrder PO WITH (NOLOCK) INNER JOIN
		PAPAMART.[dw].[dbo].[date_dim] dd WITH(NOLOCK)
			ON CONVERT(VARCHAR(10),PO.ProductionOrderDateTimeCreated,101) = dd.actual_date AND DATEPART(hour, PO.ProductionOrderDateTimeCreated) BETWEEN 0 AND 24 
		WHERE po.ProductionOrderDateTimeCreated BETWEEN CAST(dateadd(day,-364,CONVERT(VARCHAR,DATEADD(dd, -1,GETDATE()),101) + ' 00:00:00') as varchar(20))  AND CAST(dateadd(day,-364,CONVERT(VARCHAR,DATEADD(dd,-1,GETDATE()),101) + ' 23:59:59') as varchar(20))
		AND PO.[ProductionOrderSiteCode] = 'BABW_UK'
		AND PO.ProductionOrderBillingFirstName <> 'House Order'
		GROUP BY dd.actual_date,DATEPART(hour, PO.ProductionOrderDateTimeCreated)
		),
GAAPSalesAmount (actual_date,OrderHour,GAAPSales) AS(

		/*
		-- This query returns total GAAP orders $ to current report date and hour
		*/
		SELECT  a.actual_date,DATEPART(hour, a.ProductionOrderDateTimeCreated) AS OrderHour,SUM(a.ProductionOrderItemExtendedPrice + a.ProductionOrderShippingAndHandling) AS 'GAAPSales'
		FROM    ( SELECT    PO.ProductionOrderId,po.ProductionOrderDateTimeCreated,dd.actual_date,
		ISNULL(SUM(ISNULL(POI.ProductionOrderItemExtendedPrice,0)), 0) AS ProductionOrderItemExtendedPrice,
		ISNULL(PO.ProductionOrderShippingAndHandling,0) AS ProductionOrderShippingAndHandling
		FROM [KODIAK].[BABWPMS].dbo.ProductionOrder PO WITH (NOLOCK) INNER JOIN
		PAPAMART.[dw].[dbo].[date_dim] dd WITH(NOLOCK)
			ON CONVERT(VARCHAR(10),PO.ProductionOrderDateTimeCreated,101) = dd.actual_date AND DATEPART(hour, PO.ProductionOrderDateTimeCreated) BETWEEN 0 AND 24
		JOIN [KODIAK].[BABWPMS].dbo.ProductionStatus PS WITH (NOLOCK) ON PO.ProductionOrderId = PS.ProductionOrderId
		JOIN [KODIAK].[BABWPMS].dbo.ProductionOrderItem POI WITH (NOLOCK) ON PO.ProductionOrderId = POI.ProductionOrderId
		WHERE po.ProductionOrderDateTimeCreated BETWEEN CAST(dateadd(day,-1,CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00') as varchar(20)) AND CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00' 
		--WHERE po.ProductionOrderDateTimeCreated = CAST(dateadd(day,-1,CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00') as varchar(20))
		AND POI.ProductionOrderItemIsPhysicalGiftCard = 0
		AND POI.ProductionOrderItemIsVirtualGiftCard = 0
		AND PO.[ProductionOrderSiteCode] = 'BABW_UK'
		AND PO.ProductionOrderBillingFirstName <> 'House Order'
		AND PS.ProductionStatusActive = 1
		AND PS.ProductionStatusCode <> 'Canceled' 
		GROUP BY  PO.ProductionOrderId,
		PO.ProductionOrderShippingAndHandling,po.ProductionOrderDateTimeCreated,dd.actual_date
		) a
		 GROUP BY a.actual_date,DATEPART(hour, a.ProductionOrderDateTimeCreated)
		),
GAAPSalesAmountLY (actual_date,OrderHour,GAAPSalesLY) AS(

		/*
		-- This query returns total GAAPLY orders $ to current report date and hour
		*/
		SELECT  a.actual_date,DATEPART(hour, a.ProductionOrderDateTimeCreated) AS OrderHour,SUM(a.ProductionOrderItemExtendedPrice + a.ProductionOrderShippingAndHandling) AS 'GAAPSalesLY'
		FROM    ( SELECT    PO.ProductionOrderId,po.ProductionOrderDateTimeCreated,dd.actual_date,
		ISNULL(SUM(ISNULL(POI.ProductionOrderItemExtendedPrice,0)), 0) AS ProductionOrderItemExtendedPrice,
		ISNULL(PO.ProductionOrderShippingAndHandling,0) AS ProductionOrderShippingAndHandling
		FROM [KODIAK].[BABWPMS].dbo.vwRPT_ProductionOrder PO WITH (NOLOCK) INNER JOIN
		PAPAMART.[dw].[dbo].[date_dim] dd WITH(NOLOCK)
			ON CONVERT(VARCHAR(10),PO.ProductionOrderDateTimeCreated,101) = dd.actual_date AND DATEPART(hour, PO.ProductionOrderDateTimeCreated) BETWEEN 0 AND 24
		JOIN [KODIAK].[BABWPMS].dbo.vwRPT_ProductionStatus PS WITH (NOLOCK) ON PO.ProductionOrderId = PS.ProductionOrderId
		JOIN [KODIAK].[BABWPMS].dbo.vwRPT_ProductionOrderItem POI WITH (NOLOCK) ON PO.ProductionOrderId = POI.ProductionOrderId
		WHERE po.ProductionOrderDateTimeCreated BETWEEN CAST(dateadd(day,-364,CONVERT(VARCHAR,DATEADD(dd, -1,GETDATE()),101) + ' 00:00:00') as varchar(20))  AND CAST(dateadd(day,-364,CONVERT(VARCHAR,DATEADD(dd,-1,GETDATE()),101) + ' 23:59:59') as varchar(20))
		AND POI.ProductionOrderItemIsPhysicalGiftCard = 0
		AND POI.ProductionOrderItemIsVirtualGiftCard = 0
		AND PO.[ProductionOrderSiteCode] = 'BABW_UK'
		AND PO.ProductionOrderBillingFirstName <> 'House Order'
		AND PS.ProductionStatusActive = 1
		AND PS.ProductionStatusCode <> 'Canceled' 
		GROUP BY  PO.ProductionOrderId,
		PO.ProductionOrderShippingAndHandling,po.ProductionOrderDateTimeCreated,dd.actual_date
		) a
		 GROUP BY a.actual_date,DATEPART(hour, a.ProductionOrderDateTimeCreated)
		),
CASH (actual_date,OrderHour,Cash) AS (
		/*
		-- This query returns total Cash to current report date and hour
		*/
		
		SELECT  a.actual_date,DATEPART(hour, a.ProductionOrderDateTimeCreated) AS OrderHour,SUM(a.ProductionOrderItemExtendedPrice) AS 'Cash'
		FROM    ( SELECT    PO.ProductionOrderId,PO.ProductionOrderDateTimeCreated,dd.actual_date,
		ISNULL(SUM(ISNULL(POI.ProductionOrderItemExtendedPrice,0)), 0) AS ProductionOrderItemExtendedPrice
		FROM [KODIAK].[BABWPMS].dbo.ProductionOrder PO WITH (NOLOCK) LEFT JOIN
		PAPAMART.[dw].[dbo].[date_dim] dd WITH(NOLOCK)
			ON CONVERT(VARCHAR(10),PO.ProductionOrderDateTimeCreated,101) = dd.actual_date AND DATEPART(hour, PO.ProductionOrderDateTimeCreated) BETWEEN 0 AND 24
		JOIN [KODIAK].[BABWPMS].dbo.ProductionStatus PS WITH (NOLOCK) ON PO.ProductionOrderId = PS.ProductionOrderId
		JOIN [KODIAK].[BABWPMS].dbo.ProductionOrderItem POI WITH (NOLOCK) ON PO.ProductionOrderId = POI.ProductionOrderId
		WHERE po.ProductionOrderDateTimeCreated BETWEEN CAST(dateadd(day,-1,CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00') as varchar(20)) AND CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00'
		--WHERE po.ProductionOrderDateTimeCreated = CAST(dateadd(day,-1,CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00') as varchar(20))
		AND PO.[ProductionOrderSiteCode] = 'BABW_UK'
		AND PO.ProductionOrderBillingFirstName <> 'House Order'
		AND PS.ProductionStatusActive = 1
		AND PS.ProductionStatusCode <> 'Canceled' 
		GROUP BY  PO.ProductionOrderId,
		PO.ProductionOrderShippingAndHandling,PO.ProductionOrderDateTimeCreated,dd.actual_date
		) a
		GROUP BY a.actual_date,DATEPART(hour, a.ProductionOrderDateTimeCreated)
		),
CASHLY (actual_date,OrderHour,CashLY) AS (
		/*
		-- This query returns total Cash LY to current report date and hour
		*/
		
		SELECT  a.actual_date,DATEPART(hour, a.ProductionOrderDateTimeCreated) AS OrderHour,SUM(a.ProductionOrderItemExtendedPrice) AS 'Cash'
		FROM    ( SELECT    PO.ProductionOrderId,PO.ProductionOrderDateTimeCreated,dd.actual_date,
		ISNULL(SUM(ISNULL(POI.ProductionOrderItemExtendedPrice,0)), 0) AS ProductionOrderItemExtendedPrice
		FROM [KODIAK].[BABWPMS].dbo.vwRPT_ProductionOrder PO WITH (NOLOCK) INNER JOIN
		PAPAMART.[dw].[dbo].[date_dim] dd WITH(NOLOCK)
			ON CONVERT(VARCHAR(10),PO.ProductionOrderDateTimeCreated,101) = dd.actual_date AND DATEPART(hour, PO.ProductionOrderDateTimeCreated) BETWEEN 0 AND 24
		JOIN [KODIAK].[BABWPMS].dbo.vwRPT_ProductionStatus PS WITH (NOLOCK) ON PO.ProductionOrderId = PS.ProductionOrderId
		JOIN [KODIAK].[BABWPMS].dbo.vwRPT_ProductionOrderItem POI WITH (NOLOCK) ON PO.ProductionOrderId = POI.ProductionOrderId
		WHERE po.ProductionOrderDateTimeCreated BETWEEN CAST(dateadd(day,-364,CONVERT(VARCHAR,DATEADD(dd, -1,GETDATE()),101) + ' 00:00:00') as varchar(20))  AND CAST(dateadd(day,-364,CONVERT(VARCHAR,DATEADD(dd,-1,GETDATE()),101) + ' 23:59:59') as varchar(20))
		AND PO.[ProductionOrderSiteCode] = 'BABW_UK'
		AND PO.ProductionOrderBillingFirstName <> 'House Order'
		AND PS.ProductionStatusActive = 1
		AND PS.ProductionStatusCode <> 'Canceled' 
		GROUP BY  PO.ProductionOrderId,
		PO.ProductionOrderShippingAndHandling,PO.ProductionOrderDateTimeCreated,dd.actual_date
		) a
		GROUP BY a.actual_date,DATEPART(hour, a.ProductionOrderDateTimeCreated)
		),
HoursOfDay AS (
    SELECT 0 AS HoursOfDay,CAST(dateadd(day,-1,CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00') as varchar(20)) AS actual_date
    UNION ALL
    SELECT HoursOfDay + 1,CAST(dateadd(day,-1,CONVERT(VARCHAR,GETDATE(),101) + ' 0:00:00') as varchar(20)) AS actual_date
    FROM HoursOfDay 
    WHERE HoursOfDay + 1 < 24
		)

SELECT ISNULL(CAST(o.actual_date AS DATE),CONVERT(varchar,CAST(DATEADD(dd,-1,getdate()) AS DATE),120)) AS TransactionsDate,
		ISNULL(O.OrderHour,h.HoursOfDay) AS TransactionsHour,
		ISNULL(O.TotalOrders,0) AS TotalOrders ,
		ISNULL(OLY.TotalOrdersLY,0)AS TotalOrdersLY,
		ISNULL(GAP.GAAPSales,0) AS GAAPSales,
		ISNULL(GAPLY.GAAPSalesLY,0) AS GAAPSalesLY,
		ISNULL(C.Cash,0) AS NonGAAPSales,
		ISNULL(CLY.CashLY,0) AS NonGAAPSalesLY
FROM Orders O WITH (NOLOCK) RIGHT OUTER JOIN
	HoursOfDay h ON
		h.HoursOfDay = O.OrderHour LEFT  JOIN
	OrdersLY OLY WITH (NOLOCK) ON 
		CAST(DATEADD(dd,-364,h.actual_date) AS DATE) = CAST(OLY.actual_date AS DATE) 
		AND h.HoursOfDay = OLY.OrderHour LEFT  JOIN
	GAAPSalesAmount GAP WITH (NOLOCK) ON
		CAST(h.actual_date AS DATE) = CAST(GAP.actual_date AS DATE) 
		AND h.HoursOfDay = GAP.OrderHour LEFT  JOIN
	GAAPSalesAmountLY GAPLY WITH (NOLOCK) ON
		CAST(DATEADD(dd,-364,h.actual_date) AS DATE) = CAST(GAPLY.actual_date AS DATE)  
		AND h.HoursOfDay = GAPLY.OrderHour LEFT  JOIN
	CASH C ON
		CAST(h.actual_date AS DATE) = CAST(C.actual_date AS DATE) 
		AND h.HoursOfDay = C.OrderHour LEFT  JOIN
	CASHLY CLY ON
		CAST(DATEADD(dd,-364,h.actual_date) AS DATE) = CAST(CLY.actual_date AS DATE)  
		AND h.HoursOfDay = CLY.OrderHour


-- USE TO RELOAD ENTIRE DATASET
 --SELECT * FROM DWStaging.dbo.WebSales_Staging
```

