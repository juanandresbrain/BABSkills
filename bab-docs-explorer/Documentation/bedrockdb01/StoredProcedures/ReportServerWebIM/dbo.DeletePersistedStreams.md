# dbo.DeletePersistedStreams

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeletePersistedStreams"]
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PersistedStream |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeletePersistedStreams]
@SessionID varchar(32)
AS
SET NOCOUNT OFF
delete top (10) p
from [ReportServerWebIMTempDB].dbo.PersistedStream p
where p.SessionID = @SessionID;
```

