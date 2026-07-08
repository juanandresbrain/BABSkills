# dbo.CleanBatchRecords

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanBatchRecords"]
    Batch(["Batch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Batch |

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

