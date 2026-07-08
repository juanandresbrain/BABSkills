# dbo.purge_work_tables_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.purge_work_tables_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc [dbo].[purge_work_tables_$sp] 
@process_id     binary(16), 
@user_id        int

AS

/* Procedure Name: purge_work_tables_$sp
   Desc: Drop front-end/report work tables that are more than 7 days old.
   Called by day_end_housekeeping_$sp.

HISTORY
Date     Name            Defect Desc
Sep19,12 Vicci           137944 Include tables prefixed with RS_ in list of those to clean up.
Jul22,08 Paul      87777/103266 Check for numeric in position 4 of table name to handle case insensitive collations
Jan22,08 Paul             94350 drop old S0_ and SA_ work tables
Oct11,06 Paul           DV-1344 author


*/


DECLARE
        @cursor_open            tinyint,
        @db_name		nvarchar(60),
        @errmsg			nvarchar(255),
        @errno                  int,
        @name			nvarchar(200),
	@object_name            nvarchar(255),
	@process_name           nvarchar(100),
	@operation_name         nvarchar(100),
	@purge_date		datetime,
	@message_id		int,
	@SQL_QRY		nvarchar(3000),
	@uid			smallint

SELECT @process_name = 'purge_work_tables_$sp',
       @message_id = 201068,
       @cursor_open = 0,
       @purge_date = DATEADD(dd,-7,getdate()),
       @db_name = db_name()         


DECLARE table_list_crsr CURSOR FAST_FORWARD
FOR
SELECT name, uid
FROM sysobjects
WHERE type = 'U'
AND crdate <= @purge_date
AND SUBSTRING(name,1,3) IN ('SA_', 'S0_', 'RS_')  --S0_ tables are those that list the stores in the user audit group
AND ISNUMERIC(SUBSTRING(name,4,1)) = 1 -- ensure that tablename contains a numeric in position 4

OPEN table_list_crsr

SELECT @errno = @@error
IF @errno != 0
BEGIN
  SELECT @errmsg         = 'Failed to open table_list_crsr',
         @object_name    = 'table_list_crsr',
         @operation_name = 'OPEN'
  GOTO error
END

SELECT @cursor_open = 1

-- Purge old work tables. uid=1 means dbo owns it.

WHILE 1 = 1
  BEGIN
      FETCH table_list_crsr INTO
        @name, @uid

      IF @@fetch_status <> 0
        BREAK

      IF @uid = 1 -- dbo
        SELECT @SQL_QRY = 'DROP TABLE dbo.' + @name
      ELSE
        SELECT @SQL_QRY = 'DROP TABLE ' + @db_name + '..' + @name

      EXEC sp_executesql @SQL_QRY

      SELECT @errno = @@error
      IF @errno <> 0
        BEGIN
         SELECT @object_name = 'sp_executesql',
		@operation_name = 'EXECUTE',
		@errmsg = 'Failed to execute exception sql: ' + @name
         GOTO error
        END

  END -- while 1 = 1

CLOSE table_list_crsr
DEALLOCATE table_list_crsr
SELECT @cursor_open = 0




RETURN


error:   /* Common error handler */

  IF @cursor_open = 1
  BEGIN
    CLOSE table_list_crsr
    DEALLOCATE table_list_crsr
  END

  EXEC common_error_handling_$sp 5, @errno, @errmsg, 0, @message_id, @process_name,
       @object_name, @operation_name, 1, 1, 0, null, 0, null, null, null, null, null,
       null, 0, @process_id, @user_id
        
  RETURN
```

