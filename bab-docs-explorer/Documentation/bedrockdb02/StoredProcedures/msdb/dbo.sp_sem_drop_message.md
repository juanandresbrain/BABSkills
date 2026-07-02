# dbo.sp_sem_drop_message

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sem_drop_message"]
    dbo_spt_values(["dbo.spt_values"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.spt_values |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_sem_drop_message
  @msgnum int     = NULL,
  @lang   sysname = NULL -- Message language name
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
  EXECUTE @retval = master.dbo.sp_dropmessage @msgnum, @language_name
  RETURN(@retval)
END
```

