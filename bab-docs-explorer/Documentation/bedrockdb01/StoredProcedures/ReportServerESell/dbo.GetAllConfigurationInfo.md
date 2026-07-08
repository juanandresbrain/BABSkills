# dbo.GetAllConfigurationInfo

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetAllConfigurationInfo"]
    ConfigurationInfo(["ConfigurationInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ConfigurationInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetAllConfigurationInfo]
AS
SELECT [Name], [Value]
FROM [ConfigurationInfo]
```

