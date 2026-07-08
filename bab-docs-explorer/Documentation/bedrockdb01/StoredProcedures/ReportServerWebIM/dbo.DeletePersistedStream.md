# dbo.DeletePersistedStream

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeletePersistedStream"]
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PersistedStream |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeletePersistedStream]
@SessionID varchar(32),
@Index int
AS

delete from [ReportServerWebIMTempDB].dbo.PersistedStream where SessionID = @SessionID and [Index] = @Index
```

