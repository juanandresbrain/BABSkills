# dbo.sp_sem_add_message

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sem_add_message"]
    dbo_spt_values(["dbo.spt_values"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.spt_values |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_sem_add_message
  @msgnum   INT           = NULL,
  @severity SMALLINT      = NULL,
  @msgtext  NVARCHAR(255) = NULL,
  @lang     sysname       = NULL, -- Message language name
  @with_log VARCHAR(5)    = 'FALSE',
  @replace  VARCHAR(7)    = NULL
AS
BEGIN
  DECLARE @retval        INT
  DECLARE @language_name sysname

  SET NOCOUNT ON

  SET ROWCOUNT 1
  SELECT @language_name = name
  FROM sys.syslanguages
  WHERE msglangid = (SELECT number
                     FROM master.dbo.spt_values
                     WHERE (type = 'LNG')
                       AND (name = @lang))
  SET ROWCOUNT 0

  SELECT @language_name = ISNULL(@language_name, 'us_english')
  EXECUTE @retval = master.dbo.sp_addmessage @msgnum, @severity, @msgtext, @language_name, @with_log, @replace
  RETURN(@retval)
END
```

