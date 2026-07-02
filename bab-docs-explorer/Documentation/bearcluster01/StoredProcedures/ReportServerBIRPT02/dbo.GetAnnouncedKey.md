# dbo.GetAnnouncedKey

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetAnnouncedKey"]
    dbo_Keys(["dbo.Keys"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Keys |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetAnnouncedKey]
@InstallationID uniqueidentifier
AS

select PublicKey, MachineName, InstanceName
from Keys
where InstallationID = @InstallationID and Client = 1
```

