# dbo.GetDBVersion

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDBVersion"]
    dbo_ServerUpgradeHistory(["dbo.ServerUpgradeHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ServerUpgradeHistory |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetDBVersion]
    @DBVersion nvarchar(32) OUTPUT
    AS
    SET @DBVersion = (select top(1) [ServerVersion] from [dbo].[ServerUpgradeHistory] ORDER BY [UpgradeID] DESC)
```

