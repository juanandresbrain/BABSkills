# dbo.DeleteBatchRecords

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteBatchRecords"]
    dbo_Batch(["dbo.Batch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Batch |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteBatchRecords]
@BatchID uniqueidentifier
AS
SET NOCOUNT OFF
DELETE
FROM [Batch]
WHERE BatchID = @BatchID
```

