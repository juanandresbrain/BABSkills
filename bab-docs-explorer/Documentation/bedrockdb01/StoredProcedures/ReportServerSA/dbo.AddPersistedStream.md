# dbo.AddPersistedStream

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddPersistedStream"]
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
    dbo_SessionData(["dbo.SessionData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PersistedStream |
| dbo.SessionData |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[AddPersistedStream]
@SessionID varchar(32),
@Index int
AS

DECLARE @RefCount int
DECLARE @id varchar(32)
DECLARE @ExpirationDate datetime

set @RefCount = 0
set @ExpirationDate = DATEADD(day, 2, GETDATE())

set @id = (select SessionID from [ReportServerSATempDB].dbo.SessionData where SessionID = @SessionID)

if @id is not null
begin
set @RefCount = 1
end

INSERT INTO [ReportServerSATempDB].dbo.PersistedStream (SessionID, [Index], [RefCount], [ExpirationDate]) VALUES (@SessionID, @Index, @RefCount, @ExpirationDate)
```

