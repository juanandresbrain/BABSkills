# dbo.DeleteBatchRecords

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteBatchRecords"]
    Batch(["Batch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Batch |

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

