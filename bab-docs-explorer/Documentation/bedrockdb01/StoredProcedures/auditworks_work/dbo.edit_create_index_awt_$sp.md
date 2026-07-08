# dbo.edit_create_index_awt_$sp

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.edit_create_index_awt_$sp"]
    edit_duplicates_awt__sp(["edit_duplicates_awt_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| edit_duplicates_awt_$sp |

## Stored Procedure Code

```sql
create proc dbo.edit_create_index_awt_$sp            
AS

/* 
Proc Name: edit_create_index_<transl>_$sp
DESCRIPTION: 
To create indices on transl tables after the bulk copy. Trap error 1505 (duplicates)
  when creating unique indices. If any duplicates are detected, remove the duplicates
  and insert an error message to <transl>_error. 
Called from smartload edit.ict file. 

HISTORY:
Date     Name     Def# 	  Desc
Nov25,02 HenryW   1-FVT15 To log message to smartload.log when this proc has successfully completed.
Nov05,01 Paul     8900    author

*/

DECLARE @errmsg			varchar(255),
	@errno			int,
	@retry			tinyint,
	@trace_msg		varchar(255)

/* Create indices on transl tables (previously dropped before loading the transl tables) */

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_authorization_x0 ON
   dbo.awt_authorization_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)

  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 42

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_awt_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE NONCLUSTERED INDEX awt_customer_x0 ON
   dbo.awt_customer(transaction_no, entry_date_time, register_no, store_no, transaction_series, from_line_id, customer_role)

  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 51

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_customer_detail_x0 ON
   dbo.awt_customer_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, from_line_id, customer_role, customer_info_type)

  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 52

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

CREATE NONCLUSTERED INDEX awt_discount_x0 ON
 dbo.awt_discount_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)

SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to create index on transl table (discount)'
   GOTO error
  END

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_line_note_x0 ON
   dbo.awt_line_note(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, note_type)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 53

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_payroll_x0 ON
   dbo.awt_payroll_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)

  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 46

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_post_void_x0 ON
   dbo.awt_post_void_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 45

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_special_order_x0 ON
   dbo.awt_special_order_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 44

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_stock_control_x0 ON
   dbo.awt_stock_control_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 43

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_tax_override_x0 ON
   dbo.awt_tax_override_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, tax_level)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 48

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_return_x0 ON
   dbo.awt_return_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 49

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX awt_transaction_line_x0 ON
   dbo.awt_transaction_line(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_awt_$sp 50

        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
           SELECT @errmsg = 'Failed to exec edit_duplicates_transl_$sp'
           GOTO error
          END
       END -- 1505
     ELSE
       BEGIN
        SELECT @errmsg = 'Failed to create index on transl table'
        GOTO error
       END
    END -- If @errno != 0
  
END -- While @retry <= 1


SELECT @trace_msg = CHAR(13) + CHAR(10) + ':LOG && edit create index completed: ' + CONVERT(char, getdate(), 8)
PRINT @trace_msg

RETURN

error:
	IF @errno < 100000
	  SELECT @errno = @errno + 100000
	SELECT @errmsg = 'edit_create_index_awt_$sp: ' + @errmsg

	RAISERROR @errno @errmsg
	
	RETURN
```

