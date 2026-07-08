# dbo.GetBatchRecords

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetBatchRecords"]
    Batch(["Batch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Batch |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetBatchRecords]
@BatchID uniqueidentifier
AS
SELECT [Action], Item, Parent, Param, BoolParam, Content, Properties
FROM [Batch]
WHERE BatchID = @BatchID
ORDER BY AddedOn
```

