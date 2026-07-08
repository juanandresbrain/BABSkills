# dbo.SetMachineName

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetMachineName"]
    dbo_Keys(["dbo.Keys"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Keys |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetMachineName]
@MachineName nvarchar(256),
@InstallationID uniqueidentifier
AS

UPDATE [dbo].[Keys]
SET MachineName = @MachineName
WHERE [InstallationID] = @InstallationID and [Client] = 1
```

