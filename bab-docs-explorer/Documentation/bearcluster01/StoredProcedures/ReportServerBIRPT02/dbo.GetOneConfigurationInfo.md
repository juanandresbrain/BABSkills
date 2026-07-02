# dbo.GetOneConfigurationInfo

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetOneConfigurationInfo"]
    dbo_ConfigurationInfo(["dbo.ConfigurationInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ConfigurationInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetOneConfigurationInfo]
@Name nvarchar (260)
AS
SELECT [Value]
FROM [ConfigurationInfo]
WHERE [Name] = @Name
```

