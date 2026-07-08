# dbo.CleanExpiredServerParameters

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanExpiredServerParameters"]
    dbo_ServerParametersInstance(["dbo.ServerParametersInstance"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ServerParametersInstance |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CleanExpiredServerParameters]
@ParametersCleaned INT OUTPUT
AS
  DECLARE @now as DATETIME
  SET @now = GETDATE()

DELETE FROM [dbo].[ServerParametersInstance] 
WHERE ServerParametersID IN 
(  SELECT TOP 20 ServerParametersID FROM [dbo].[ServerParametersInstance]
  WHERE Expiration < @now
)

SET @ParametersCleaned = @@ROWCOUNT
```

