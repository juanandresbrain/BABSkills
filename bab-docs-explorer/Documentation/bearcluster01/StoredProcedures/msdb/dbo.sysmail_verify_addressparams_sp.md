# dbo.sysmail_verify_addressparams_sp

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sysmail_verify_addressparams_sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sysmail_verify_addressparams_sp
  @address          VARCHAR(MAX),
  @parameter_name   NVARCHAR(32)
AS
  IF ((@address IS NOT NULL) AND (@address != N''))
  BEGIN
    DECLARE @commaIndex int
    SET @commaIndex = CHARINDEX(',', @address)
    IF (@commaIndex > 0)
    BEGIN
      -- Comma is the wrong format to separate addresses. Users should use the semicolon ";".
      RAISERROR(14613, 16, 1, @parameter_name, @address)
      RETURN(1)        
    END
  END

  RETURN(0) -- SUCCESS
```

