# dbo.DeleteExpiredPersistedStreams

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteExpiredPersistedStreams"]
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PersistedStream |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteExpiredPersistedStreams]
AS
SET NOCOUNT OFF
SET DEADLOCK_PRIORITY LOW
declare @now as datetime = GETDATE();
delete top (10) p
from [ReportServerESellTempDB].dbo.PersistedStream p with(readpast)
where p.RefCount = 0 AND p.ExpirationDate < @now;
```

