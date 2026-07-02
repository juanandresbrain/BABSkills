# dbo.GetBatchRecords

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetBatchRecords"]
    dbo_Batch(["dbo.Batch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Batch |

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

