# WMS.vwSalesOrderStatusUpdateWaved_All

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwSalesOrderStatusUpdateWaved_All"]
    WMS_SalesOrderStatusUpdateWaved(["WMS.SalesOrderStatusUpdateWaved"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.SalesOrderStatusUpdateWaved |

## View Code

```sql
CREATE view [WMS].[vwSalesOrderStatusUpdateWaved_All]

AS



WITH [SalesOrderStatusUpdateWavedWork1] ([WaveId]
      ,[ReleasedDateAndTime]
      ,[Warehouse]
      ,[ShipmentStatus]
      ,[MasterTrackingNumber]
      ,[ItemId]
      ,[SalesPoolId]
      ,[DeckSalesOrderReferenceNumber]
      ,[OrderNum]
	  ,[ServiceBusSequence]
	  ,[ContainerId]
	  ,WaveNum)
AS
(
SELECT [WaveId]
      ,[ReleasedDateAndTime]
      ,[Warehouse]
      ,[ShipmentStatus]
      ,[MasterTrackingNumber]
      ,[ItemId]
      ,[SalesPoolId]
      ,[DeckSalesOrderReferenceNumber]
      ,[OrderNum]
	  ,[ServiceBusSequence]
	  ,[ContainerId]
	  ,CAST(RIGHT([WaveId], 9) AS INT) AS WaveNum
  FROM [IntegrationStaging].[WMS].[SalesOrderStatusUpdateWaved] WITH (NOLOCK)
  --WHERE ReleasedDateAndTime > DATEADD(DAY, -3, GETUTCDATE())
), workIDs (WorkId, ServiceBusSequence, ItemId)
AS
(
SELECT [WorkId]
      ,[ServiceBusSequence]
	  ,[ItemId]
  FROM [IntegrationStaging].[WMS].[SalesOrderStatusUpdateWaved] WITH (NOLOCK)
  --WHERE ReleasedDateAndTime > DATEADD(DAY, -3, GETUTCDATE())
),SalesOrderStatusUpdateWavedWork2 ([WaveId]
      ,[ReleasedDateAndTime]
      ,[Warehouse]
      ,[ShipmentStatus]
      ,[MasterTrackingNumber]
      ,[ItemId]
      ,[SalesPoolId]
      ,[DeckSalesOrderReferenceNumber]
      ,[OrderNum]
      ,[ServiceBusSequence]
	  ,[ContainerId]
	  ,WaveNum)
AS
(
SELECT [WaveId]
      ,[ReleasedDateAndTime]
      ,[Warehouse]
      ,[ShipmentStatus]
      ,[MasterTrackingNumber]
      ,[ItemId]
      ,[SalesPoolId]
      ,[DeckSalesOrderReferenceNumber]
      ,[OrderNum]
      ,MAX([ServiceBusSequence]) AS [ServiceBusSequence]
	  ,[ContainerId]
	  ,WaveNum
  FROM SalesOrderStatusUpdateWavedWork1
  GROUP BY [WaveId]
      ,[ReleasedDateAndTime]
      ,[Warehouse]
      ,[ShipmentStatus]
      ,[MasterTrackingNumber]
      ,[ItemId]
      ,[SalesPoolId]
      ,[DeckSalesOrderReferenceNumber]
      ,[OrderNum]
	  ,[ContainerId]
	  ,WaveNum
)
SELECT [WaveId]
      ,[ReleasedDateAndTime]
      ,[Warehouse]
      ,[ShipmentStatus]
      ,[MasterTrackingNumber]
      ,w2.[ItemId]
      ,[SalesPoolId]
      ,[DeckSalesOrderReferenceNumber]
      ,[OrderNum]
      ,w.[WorkId]
	  ,[ContainerId]
	  ,WaveNum
  FROM SalesOrderStatusUpdateWavedWork2 w2
  INNER JOIN workIDs w ON w2.ServiceBusSequence = w.ServiceBusSequence AND w2.ItemId = w.ItemId
```

