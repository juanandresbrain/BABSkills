# dbo.sp_get_traceflag_status_internal

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_get_traceflag_status_internal"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_get_traceflag_status_internal
   @traceflag INT, 
   @status INT OUTPUT
AS
BEGIN
    SET @status = NULL

    IF(@traceflag IS NOT NULL)
    BEGIN
        DECLARE @traceStatus TABLE
        (
            TraceFlag int,
            [Status] int,
            [Global] int,
            [Session] int
        )
        INSERT INTO @traceStatus 
        EXEC ('DBCC TRACESTATUS (-1) WITH NO_INFOMSGS')
    
        SELECT @status = [Status]  
        FROM @traceStatus
        WHERE TraceFlag = @traceflag
    END
END
```

