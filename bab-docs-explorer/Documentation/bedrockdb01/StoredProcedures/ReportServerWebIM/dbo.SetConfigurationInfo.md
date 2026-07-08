# dbo.SetConfigurationInfo

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetConfigurationInfo"]
    ConfigurationInfo(["ConfigurationInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ConfigurationInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetConfigurationInfo]
@Name nvarchar (260),
@Value ntext
AS
DELETE
FROM [ConfigurationInfo]
WHERE [Name] = @Name

IF @Value is not null BEGIN
   INSERT
   INTO ConfigurationInfo
   VALUES ( newid(), @Name, @Value )
END
```

