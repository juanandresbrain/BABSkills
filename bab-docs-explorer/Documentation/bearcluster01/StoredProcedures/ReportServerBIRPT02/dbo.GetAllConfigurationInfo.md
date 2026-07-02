# dbo.GetAllConfigurationInfo

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetAllConfigurationInfo"]
    dbo_ConfigurationInfo(["dbo.ConfigurationInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ConfigurationInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetAllConfigurationInfo]
AS
SELECT [Name], [Value]
FROM [ConfigurationInfo]
```

