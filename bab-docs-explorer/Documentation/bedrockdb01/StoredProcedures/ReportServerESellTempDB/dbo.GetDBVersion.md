# dbo.GetDBVersion

**Database:** ReportServerESellTempDB  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDBVersion"]
    dbo_DBUpgradeHistory(["dbo.DBUpgradeHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DBUpgradeHistory |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetDBVersion]
    @DBVersion nvarchar(32) OUTPUT
    AS
    SET @DBVersion = (select top(1) [DbVersion]  from [dbo].[DBUpgradeHistory])
```

