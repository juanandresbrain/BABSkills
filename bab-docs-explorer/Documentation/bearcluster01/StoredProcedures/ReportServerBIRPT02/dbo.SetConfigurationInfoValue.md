# dbo.SetConfigurationInfoValue

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetConfigurationInfoValue"]
    dbo_ConfigurationInfo(["dbo.ConfigurationInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ConfigurationInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetConfigurationInfoValue]
@ConfigValue nvarchar (260),
@ConfigName nvarchar (260)
AS

UPDATE [dbo].[ConfigurationInfo]
SET [Value] = @ConfigValue
WHERE [Name] = @ConfigName
```

