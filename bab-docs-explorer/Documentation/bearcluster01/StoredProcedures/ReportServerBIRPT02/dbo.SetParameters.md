# dbo.SetParameters

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetParameters"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_FlushReportFromCache(["dbo.FlushReportFromCache"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.FlushReportFromCache |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetParameters]
@Path nvarchar (425),
@Parameter ntext
AS
UPDATE Catalog
SET [Parameter] = @Parameter
WHERE Path = @Path
EXEC FlushReportFromCache @Path
```

