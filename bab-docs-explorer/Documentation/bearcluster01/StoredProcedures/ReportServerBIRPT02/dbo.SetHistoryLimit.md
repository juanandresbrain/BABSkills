# dbo.SetHistoryLimit

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetHistoryLimit"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetHistoryLimit]
@Path nvarchar (425),
@SnapshotLimit int = NULL
AS
UPDATE Catalog
SET SnapshotLimit=@SnapshotLimit
WHERE Path = @Path
```

