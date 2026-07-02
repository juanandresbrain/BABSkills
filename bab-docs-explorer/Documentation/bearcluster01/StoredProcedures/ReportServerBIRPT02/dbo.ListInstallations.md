# dbo.ListInstallations

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ListInstallations"]
    dbo_Keys(["dbo.Keys"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Keys |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ListInstallations]
AS

SELECT
    [MachineName],
    [InstanceName],
    [InstallationID],
    CASE WHEN [SymmetricKey] IS null THEN 0 ELSE 1 END
FROM [dbo].[Keys]
WHERE [Client] = 1
```

