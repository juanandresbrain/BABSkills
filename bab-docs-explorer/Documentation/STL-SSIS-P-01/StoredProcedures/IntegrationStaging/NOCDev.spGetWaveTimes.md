# NOCDev.spGetWaveTimes

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["NOCDev.spGetWaveTimes"]
    WM_WaveJob(["WM.WaveJob"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.WaveJob |

## Stored Procedure Code

```sql
CREATE proc [NOCDev].[spGetWaveTimes]

as

-------------------------------------------------------------------------					
-- 2021-11-10 - Brandon Hickey - Created Proc
-------------------------------------------------------------------------

set nocount on


  SELECT TOP (1000) [WaveID]
      ,[WaveNum]
      ,[WaveComplete]
      ,DATEADD(mi, DATEDIFF(mi, GETUTCDATE(), GETDATE()),[ReleasedDateAndTime]) AS ReleasedDateAndTime
      ,[PickTicketJobDateAndTime]
  FROM [BEARCLUSTER01.SQL.BUILDABEAR.COM].[WebOrderProcessing].[WM].[WaveJob]
  WHERE ReleasedDateAndTime > DATEADD(DAY, -1, GETDATE())
  ORDER BY 1 DESC
```

