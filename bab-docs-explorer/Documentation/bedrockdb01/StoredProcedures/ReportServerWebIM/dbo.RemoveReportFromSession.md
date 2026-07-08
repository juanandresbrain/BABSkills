# dbo.RemoveReportFromSession

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RemoveReportFromSession"]
    DereferenceSessionSnapshot(["DereferenceSessionSnapshot"]) --> SP
    GetUserID(["GetUserID"]) --> SP
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
    dbo_SessionData(["dbo.SessionData"]) --> SP
    dbo_SessionLock(["dbo.SessionLock"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| DereferenceSessionSnapshot |
| GetUserID |
| dbo.PersistedStream |
| dbo.SessionData |
| dbo.SessionLock |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[RemoveReportFromSession]
@SessionID as varchar(32),
@ReportPath as nvarchar(440), 
@OwnerSid as varbinary(85) = NULL,
@OwnerName as nvarchar(260),
@AuthType as int
AS

DECLARE @OwnerID uniqueidentifier
EXEC GetUserID @OwnerSid, @OwnerName, @AuthType, @OwnerID OUTPUT

EXEC DereferenceSessionSnapshot @SessionID, @OwnerID
   
DELETE
   SE
FROM
   [ReportServerWebIMTempDB].dbo.SessionData AS SE
WHERE
   SE.SessionID = @SessionID AND
   SE.ReportPath = @ReportPath AND
   SE.OwnerID = @OwnerID
   
DELETE FROM [ReportServerWebIMTempDB].dbo.SessionLock WHERE SessionID=@SessionID
   
-- Delete any persisted streams associated with this session
UPDATE PS
SET
    PS.RefCount = 0,
    PS.ExpirationDate = GETDATE()
FROM
    [ReportServerWebIMTempDB].dbo.PersistedStream AS PS
WHERE
    PS.SessionID = @SessionID
```

