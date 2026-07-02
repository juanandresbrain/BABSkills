# dbo.sp_get_message_description

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_get_message_description"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_get_message_description
  @error INT
AS
BEGIN
  IF EXISTS (SELECT * FROM master.dbo.sysmessages WHERE (error = @error) AND (msglangid = (SELECT msglangid FROM sys.syslanguages WHERE (langid = @@langid))))
    SELECT description FROM master.dbo.sysmessages WHERE (error = @error) AND (msglangid = (SELECT msglangid FROM sys.syslanguages WHERE (langid = @@langid)))
  ELSE
    SELECT description FROM master.dbo.sysmessages WHERE (error = @error) AND (msglangid = 1033)
END
```

