# MerchandisingPlanning.vwETLBatchPerformanceHistory

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["MerchandisingPlanning.vwETLBatchPerformanceHistory"]
    MerchandisingPlanning_TXTDataLoad_ETLBatch(["MerchandisingPlanning.TXTDataLoad_ETLBatch"]) --> VIEW
    MerchandisingPlanning_TXTDataLoad_ETLBatchDetailLog(["MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| MerchandisingPlanning.TXTDataLoad_ETLBatch |
| MerchandisingPlanning.TXTDataLoad_ETLBatchDetailLog |

## View Code

```sql
/***********************************************************************************************
Object Name:			dbo.[[vwETLBatchPerformanceHistory]]
Description/Purpose:	view used for performance trend

-- Dependencies: 
--
-- Revision History
--		Name:					Date:			Comments:
--		Kevin Shyr			2015-07-22		Original Creation

**********************************************************************************************/
CREATE VIEW [MerchandisingPlanning].[vwETLBatchPerformanceHistory]
AS

SELECT d.ETLBatchDetailLogID
      ,d.ETLBatchID
      ,d.ETLStatusID
      ,d.StatementWithoutParameter
      ,d.ETLBatchDetailItemStartDateTime
      ,d.ETLBatchDetailItemEndDateTime
	  ,DATEDIFF(minute, d.ETLBatchDetailItemStartDateTime, d.ETLBatchDetailItemEndDateTime) AS BatchDetailDurationInMinutes
	  ,DATEPART(hour, d.ETLBatchDetailItemStartDateTime) AS BatchDetailStartHour
      ,d.BatchParameter_FiscalYear
      ,d.BatchParameter_FiscalWeek
      ,b.MaxConcurrentProcess
      ,b.ETLBatchStartDateTime
      ,b.ETLBatchEndDateTime
	  ,DATEDIFF(minute, b.ETLBatchStartDateTime, b.ETLBatchEndDateTime) AS BatchDurationInMinutes
	  ,DATEPART(hour, b.ETLBatchStartDateTime) AS BatchStartHour
      ,b.BatchParameter_StartFiscalYear
      ,b.BatchParameter_StartFiscalWeek
      ,b.BatchParameter_EndFiscalYear
      ,b.BatchParameter_EndFiscalWeek
FROM [MerchandisingPlanning].[TXTDataLoad_ETLBatchDetailLog] d WITH(NOLOCK)
	INNER JOIN [MerchandisingPlanning].[TXTDataLoad_ETLBatch] b WITH(NOLOCK)
		ON d.ETLBatchID = b.ETLBatchID
```

