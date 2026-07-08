# dbo.util_drop_tables_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_drop_tables_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.util_drop_tables_$sp 
AS

/* Procedure Name: util_drop_tables_$sp
   Desc: drop all SA n-tier work tables in a db that were created more than 2 days ago.
         Used to clean up work tables that were not dropped by n-tier.
         Called once per day from the SA dayend. 

HISTORY
Date     Name            Defect Desc
Jun20,05 Paul           DV-1282 author

*/


DECLARE
        @cursor_open            tinyint,
        @db_name		varchar(30),
        @errno                  int,
        @sql_command            nvarchar(2000),
        @name                   varchar(80),
	@object_name            varchar(255),
	@process_name           varchar(100),
	@operation_name         varchar(100),
	@message_id		int,
	@errmsg			varchar(255)

SELECT @process_name = 'util_drop_tables_$sp',
       @message_id = 201068,
       @db_name = db_name()   


CREATE TABLE #work_object_list (
	object_name varchar(80) not null)

SELECT @errno = @@error 
IF @errno != 0 BEGIN 
     SELECT @errmsg = 'Failed to create #work_object_list' ,
	@object_name    = '#work_object_list',
	@operation_name = 'CREATE'          
     GOTO error 
END 


INSERT #work_object_list (object_name)
SELECT name
  FROM sysobjects
 WHERE type = 'U'
   AND LEN(name) > 20
   AND (SUBSTRING(name,1,2) = 't_' OR SUBSTRING(name,1,3) = 'SA_')
   AND crdate < DATEADD(dd, -2, getdate())


SELECT @cursor_open = 0

DECLARE object_crsr CURSOR FAST_FORWARD
FOR
SELECT object_name
FROM #work_object_list

OPEN object_crsr

SELECT @errno = @@error
IF @errno != 0
BEGIN
  SELECT @errmsg         = 'Failed to open object_crsr',
         @object_name    = 'object_crsr',
         @operation_name = 'OPEN'
  GOTO error
END

SELECT @cursor_open = 1

WHILE 1 = 1
  BEGIN
      FETCH object_crsr INTO
        @name

      IF @@fetch_status <> 0
        BREAK

      SELECT @sql_command = 'drop table ' + @db_name + '.' + @name
      SELECT @sql_command

      EXEC sp_executesql @sql_command

      SELECT @errno = @@error
      IF @errno <> 0
        BEGIN
	  SELECT @object_name = 'sp_executesql',
		@operation_name = 'EXECUTE',
		@errmsg = 'Failed to execute dynamically SQL: ' + @sql_command
	  GOTO error
	END

  END -- while 1 = 1

CLOSE object_crsr
DEALLOCATE object_crsr
SELECT @cursor_open = 0


RETURN


error:   /* Common error handler */

  IF @cursor_open = 1
  BEGIN
    CLOSE object_crsr
    DEALLOCATE object_crsr
  END

  EXEC common_error_handling_$sp 0, @errno, @errmsg, 0, @message_id, @process_name,
       @object_name, @operation_name, 1, 1, 0, null, 0, null, null, null, null, null,
       null, 0, 0, 0
        
  RETURN
```

