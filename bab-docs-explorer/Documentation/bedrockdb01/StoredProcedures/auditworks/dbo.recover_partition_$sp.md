# dbo.recover_partition_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.recover_partition_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.recover_partition_$sp @recover_partition_no int OUTPUT, @recover_trans_count int OUTPUT
AS

/*
Proc name: recover_partition_$sp
     Desc: To cleanup (_tempXXXX) or recover (_partXXXX) temporary tables that are used in partition_purge_archive_$sp if there are any.
           Called by partition_purge_archive_$sp.

HISTORY:
Date     Name            Defect# Description
May08,12 Vicci            134811 Handle possibility that the archive table's partition is not empty despite the fact that the _part table had
                                 not yet been dropped.  This would be the case if the exceptions had been re-inserted into the av table after its
                                 partition had been swapped out into _part but _part had not yet been dropped, i.e. if cleanup of the partition is 
                                 incomplete.
Aug04,08 Phu               95126 Initial development (requires SQL2005 or higher)

*/

DECLARE
  @cursor_open                           tinyint,
  @errmsg                                nvarchar(255),
  @errno                                 int,
  @exec_sql                              nvarchar(300),
  @message_id                            int,
  @object_name                           nvarchar(255),
  @operation_name                        nvarchar(100),
  @param_definition                      nvarchar(200),
  @partition_no                          int,
  @process_name                          nvarchar(100),  
  @process_no                            smallint,
  @table_name                            sysname,
  @tran_count                            int

SELECT
  @cursor_open = 0,
  @process_no = 39,
  @message_id = 201068,
  @process_name = 'recover_partition_$sp'

-- Note: no need to log process_log since there is at most one av_*temp* or av_*part* table to recover.
-- cleanup temporary table that is left from the last run
IF EXISTS (SELECT 1 FROM [sys].[objects] WHERE name LIKE 'av_%_temp[0-9][0-9][0-9][0-9]')
BEGIN
  SELECT name AS table_name
  INTO #cleanup_temp
  FROM sys.objects WHERE name LIKE 'av_%_temp[0-9][0-9][0-9][0-9]'

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Unable to create temporary table',
           @object_name = '#cleanup_temp',
           @operation_name = 'CREATE'
    GOTO error
  END

  DECLARE cleanup_temp_crsr CURSOR
  FOR
  SELECT table_name
  FROM #cleanup_temp

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Unable to declare cursor',
           @object_name = 'cleanup_temp_crsr',
           @operation_name = 'DECLARE'
    GOTO error
  END

  OPEN cleanup_temp_crsr

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Unable to open cursor',
           @object_name = 'cleanup_temp_crsr',
           @operation_name = 'OPEN'
    GOTO error
  END

  SELECT @cursor_open = 1

  WHILE 1 = 1
  BEGIN
    FETCH cleanup_temp_crsr INTO
      @table_name

    IF @@fetch_status != 0
      BREAK

    SELECT @exec_sql = 'DROP TABLE ' + @table_name
    EXEC sp_executesql @exec_sql
    SELECT @errno = @@error
    IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Unable to execute dynamic sql',
             @object_name = @exec_sql,
             @operation_name = 'EXECUTE'
      GOTO error
    END

  END -- while 1 = 1
  CLOSE cleanup_temp_crsr
  DEALLOCATE cleanup_temp_crsr
  SELECT @cursor_open = 0

  DROP TABLE #cleanup_temp

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Unable to drop temporary table',
           @object_name = '#cleanup_temp',
           @operation_name = 'DROP'
    GOTO error
  END

END -- IF EXISTS (SELECT 1 FROM [sys].[objects] WHERE name LIKE 'av_%_temp[0-9][0-9][0-9][0-9]')

-- recover incomplete partition table that is left from the last run
IF EXISTS (SELECT 1 FROM [sys].[objects] WHERE name LIKE 'av_%_part[0-9][0-9][0-9][0-9]')
BEGIN
  SELECT name AS table_name
  INTO #recovery_part
  FROM sys.objects WHERE name LIKE 'av_%_part[0-9][0-9][0-9][0-9]'

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Unable to create temporary table',
           @object_name = '#recovery_part',
           @operation_name = 'CREATE'
    GOTO error
  END

  DECLARE recover_part_crsr CURSOR
  FOR
  SELECT table_name
  FROM #recovery_part

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Unable to declare cursor',
           @object_name = 'recover_part_crsr',
           @operation_name = 'DECLARE'
    GOTO error
  END

  OPEN recover_part_crsr

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Unable to open cursor',
           @object_name = 'recover_part_crsr',
           @operation_name = 'OPEN'
    GOTO error
  END

  SELECT @cursor_open = 2

  WHILE 2 = 2
  BEGIN
    FETCH recover_part_crsr INTO
      @table_name

    IF @@fetch_status != 0
      BREAK

    SELECT @tran_count = 0,
           @exec_sql = N'SELECT @row_count_out = COUNT(av_transaction_id) FROM ' + @table_name,
           @param_definition = N'@row_count_out int OUTPUT'

    EXECUTE sp_executesql @exec_sql, @param_definition, @row_count_out = @tran_count OUTPUT
    SELECT @errno = @@error
    IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Unable to execute dynamic sql',
             @object_name = @exec_sql,
             @operation_name = 'EXECUTE'
      GOTO error
    END

    SELECT @errno = 0
    IF @tran_count > 0
    BEGIN
      -- table_name is av_transaction_header_part0001, so partition_no is 1
      SELECT @partition_no = CONVERT(int, SUBSTRING(@table_name, LEN(@table_name) - 3, 4))

      -- SUBSTRING(@table_name, 1, LEN(@table_name) - 9) = av_transaction_header
      -- ALTER TABLE table_part0001 SWITCH PARTITION 1 to partition_table PARTITION 1 
      SELECT @exec_sql = 'ALTER TABLE ' + @table_name + ' SWITCH PARTITION ' + convert(nvarchar, @partition_no) + ' TO ' + SUBSTRING(@table_name, 1, LEN(@table_name) - 9) + ' PARTITION ' + convert(nvarchar, @partition_no)
      EXEC sp_executesql @exec_sql
      SELECT @errno = @@error
      IF @errno != 0 AND @errno != 4904  --4904 would happen if target table's partition isn't empty, i.e. if we got as far as moving the exception transactions back into the av table already, in which case there is no need to put back transaction we were going to delete anyhow.
      BEGIN
        SELECT @errmsg = 'Unable to execute dynamic sql',
               @object_name = @exec_sql,
               @operation_name = 'EXECUTE'
        GOTO error
      END
    END -- IF @tran_count IS NOT NULL

    IF @errno = 4904 AND SUBSTRING(@table_name, 1, 21) = 'av_transaction_header'  -- the presence of a left-behind av_transaction_header_partXXXX table signals that not all line/attachment tables for the partition have been cleaned yet
      SELECT @recover_partition_no = @partition_no, @recover_trans_count = @tran_count  --note:  there can only be 1 _partXXXX table existing at a time
      
    IF @errno != 4904 OR SUBSTRING(@table_name, 1, 21) <> 'av_transaction_header'  --since we are using the av_transaction_header_partXXXX table as our signal that not all line/attachment tables have been cleaned yet, we want to keep it around.
    --passing back the @recover_partition_no and @recover_trans_count variables is not sufficient since if an error were encountered yet again, 
    --there would be nothing found on the next dayend to signal that a recovery is required.
    BEGIN
      SELECT @exec_sql = 'DROP TABLE ' + @table_name
      EXEC sp_executesql @exec_sql
      SELECT @errno = @@error
      IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Unable to execute dynamic sql',
               @object_name = @exec_sql,
               @operation_name = 'EXECUTE'
        GOTO error
      END
    END
    
  END -- while 2 = 2
  CLOSE recover_part_crsr
  DEALLOCATE recover_part_crsr
  SELECT @cursor_open = 0

END -- IF EXISTS (SELECT 1 FROM [sys].[objects] WHERE name LIKE 'av_%_part[0-9][0-9][0-9][0-9]')


RETURN


error:

  IF @cursor_open = 2
  BEGIN
    CLOSE recover_part_crsr
    DEALLOCATE recover_part_crsr
    SELECT @cursor_open = 0
  END

  IF @cursor_open = 1
  BEGIN
    CLOSE cleanup_temp_crsr
    DEALLOCATE cleanup_temp_crsr
    SELECT @cursor_open = 0
  END

  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
  @process_name, @object_name, @operation_name, 1
  RETURN
```

