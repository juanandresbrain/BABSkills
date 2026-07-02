# dbo.CleanExpiredContentCache

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanExpiredContentCache"]
    dbo_ContentCache(["dbo.ContentCache"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ContentCache |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CleanExpiredContentCache]
AS
    SET DEADLOCK_PRIORITY LOW
    SET NOCOUNT ON
    DECLARE @now as datetime

    SET @now = DATEADD(minute, -1, GETDATE())

    DELETE
    FROM
       [ReportServerBIRPT02TempDB].dbo.[ContentCache]
    WHERE
       ExpirationDate < @now

    SELECT @@ROWCOUNT
```

