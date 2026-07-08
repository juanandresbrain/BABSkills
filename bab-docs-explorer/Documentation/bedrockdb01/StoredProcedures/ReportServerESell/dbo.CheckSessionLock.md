# dbo.CheckSessionLock

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CheckSessionLock"]
    dbo_SessionLock(["dbo.SessionLock"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SessionLock |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CheckSessionLock]
@SessionID as varchar(32),
@LockVersion  int OUTPUT
AS
DECLARE @Selected nvarchar(32)
SELECT @Selected=SessionID, @LockVersion = LockVersion FROM [ReportServerESellTempDB].dbo.SessionLock WITH (ROWLOCK) WHERE SessionID = @SessionID
```

