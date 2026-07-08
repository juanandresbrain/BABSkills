# dbo.Ex_CleanQueue

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_CleanQueue"]
    Ex_Queue(["Ex_Queue"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Ex_Queue |

## Stored Procedure Code

```sql
create proc dbo.Ex_CleanQueue  @queue_arg nvarchar(5),  @from_arg nvarchar(14), @to_arg nvarchar(14)

/*
History:
Date     Name        Defect#  Desc
Sep03,14 Paul      TFS-83215  removed unnecessary commit that was causing Foundation housekeeping to report an error
Feb24,14 Paul         149193  modified error trap for SQL2012 compatability. Now installed by SA5.x instead of Site Manager.
Dec20,00 Chris C              author

*/
AS
DECLARE @queue_id         numeric(14,0),
        @from_serial_no   numeric(14,0),
        @to_serial_no     numeric(14,0),
        @max_serial_no    numeric(14,0),
        @errmsg           nvarchar(255),
        @errno            int,
        @return           int;

BEGIN TRY
    /* Init variables */
    SELECT @errmsg = 'Error caused by data in passed in arguments.';
    SELECT @queue_id = convert(numeric(14,0), @queue_arg),
           @from_serial_no = convert(numeric(14,0), @from_arg),
           @max_serial_no = convert(numeric(14,0), @to_arg);

    WHILE (@from_serial_no <= @max_serial_no and @from_serial_no <> -1)
    BEGIN
            select @to_serial_no = @from_serial_no + 2000,
                   @errmsg = 'Error deleting from Ex_Queue.';

            Delete Ex_Queue
                    where queue_id = @queue_id
                    and serial_no between @from_serial_no and @to_serial_no
                    and serial_no <= @max_serial_no;

            select @errmsg = 'Error selecting from_serial_no from Ex_Queue.';
            select @from_serial_no = isnull(min(serial_no), -1)
                From Ex_Queue
                where queue_id = @queue_id
                and serial_no > @to_serial_no;
    END; /* End of Loop */

    RETURN 1;

END TRY

BEGIN CATCH;
error:   /* Common error handler */

    SELECT @errno = ERROR_NUMBER();

    SELECT @errmsg = 'Ex_CleanQueue: ' + CONVERT(varchar, @errno) + COALESCE(@errmsg,' ');

    -- PRINT @errmsg;
    -- RAISERROR (@errmsg, 16, 1);

     -- return code zero when error occurs is expected by calling object
    RETURN 0;
END CATCH;
```

