# dbo.UpdateUsernameFromSID

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateUsernameFromSID"]
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Users |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdateUsernameFromSID]
AS
SET NOCOUNT OFF

DECLARE @TotalRecords BIGINT;
DECLARE @BatchSize INT = 100;
DECLARE @i BIGINT = 0;


SELECT ROW_NUMBER() OVER (ORDER BY ModifiedDate ASC) AS RowNumber, [Sid] INTO #SidsToUpdate FROM [dbo].[Users]
WHERE AuthType=1

SELECT @TotalRecords = MAX(RowNumber) FROM #SidsToUpdate

WHILE (@i <= @TotalRecords)
BEGIN

    UPDATE [dbo].[Users] SET UserName = COALESCE(SUSER_SNAME([Sid]), UserName), ModifiedDate = GETDATE()
    WHERE AuthType=1 AND [Sid] IN (SELECT [Sid] FROM #SidsToUpdate WHERE RowNumber >= @i AND RowNumber < @i + @BatchSize )

    SET @i = @i + @BatchSize
END

DROP TABLE #SidsToUpdate
```

