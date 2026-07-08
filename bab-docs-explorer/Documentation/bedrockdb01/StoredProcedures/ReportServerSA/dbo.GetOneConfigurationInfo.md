# dbo.GetOneConfigurationInfo

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetOneConfigurationInfo"]
    ConfigurationInfo(["ConfigurationInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ConfigurationInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetOneConfigurationInfo]
@Name nvarchar (260)
AS
SELECT [Value]
FROM [ConfigurationInfo]
WHERE [Name] = @Name
```

