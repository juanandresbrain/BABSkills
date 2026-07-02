# dbo.CleanBatchRecords

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanBatchRecords"]
    dbo_Batch(["dbo.Batch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Batch |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CleanBatchRecords]
@MaxAgeMinutes int
AS
SET NOCOUNT OFF
DELETE FROM [Batch]
where BatchID in
   ( SELECT BatchID
     FROM [Batch]
     WHERE AddedOn < DATEADD(minute, -(@MaxAgeMinutes), GETUTCDATE()) )
```

