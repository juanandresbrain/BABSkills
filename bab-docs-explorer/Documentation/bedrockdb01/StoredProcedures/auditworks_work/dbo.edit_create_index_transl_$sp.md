# dbo.edit_create_index_transl_$sp

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.edit_create_index_transl_$sp"]
    edit_duplicates_transl__sp(["edit_duplicates_transl_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| edit_duplicates_transl_$sp |

## Stored Procedure Code

```sql
create proc dbo.edit_create_index_transl_$sp            
AS

/* 
Proc Name: edit_create_index_<transl>_$sp
DESCRIPTION: 
To create indices on transl tables after the bulk copy. Trap error 1505 (duplicates)
  when creating unique indices. If any duplicates are detected, remove the duplicates
  and insert an error message to <transl>_error. 
Called from smartload edit.ict file. 

HISTORY:
Date     Name   Def# Desc
Nov05,01 Paul   8900 author

*/

DECLARE @errmsg			varchar(255),
	@errno			int,
	@retry			tinyint

/* Create indices on transl tables (previously dropped before loading the transl tables) */

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX transl_authorization_x0 ON
   dbo.transl_authorization_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)

  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 42

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
  CREATE NONCLUSTERED INDEX transl_customer_x0 ON
   dbo.transl_customer(transaction_no, entry_date_time, register_no, store_no, transaction_series, from_line_id, customer_role)

  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 51

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
  CREATE UNIQUE NONCLUSTERED INDEX transl_customer_detail_x0 ON
   dbo.transl_customer_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, from_line_id, customer_role, customer_info_type)

  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 52

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

CREATE NONCLUSTERED INDEX transl_discount_x0 ON
 dbo.transl_discount_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)

SELECT @errno = @@error
IF @errno != 0
  BEGIN
   SELECT @errmsg = 'Failed to create index on transl table (discount)'
   GOTO error
  END

SELECT @retry = 0

WHILE @retry <= 1
BEGIN
  CREATE UNIQUE NONCLUSTERED INDEX transl_line_note_x0 ON
   dbo.transl_line_note(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, note_type)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 53

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
  CREATE UNIQUE NONCLUSTERED INDEX transl_payroll_x0 ON
   dbo.transl_payroll_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)

  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 46

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
  CREATE UNIQUE NONCLUSTERED INDEX transl_post_void_x0 ON
   dbo.transl_post_void_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 45

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
  CREATE UNIQUE NONCLUSTERED INDEX transl_special_order_x0 ON
   dbo.transl_special_order_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 44

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
  CREATE UNIQUE NONCLUSTERED INDEX transl_stock_control_x0 ON
   dbo.transl_stock_control_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 43

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
  CREATE UNIQUE NONCLUSTERED INDEX transl_tax_override_x0 ON
   dbo.transl_tax_override_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, tax_level)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 48

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
  CREATE UNIQUE NONCLUSTERED INDEX transl_return_x0 ON
   dbo.transl_return_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 49

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
  CREATE UNIQUE NONCLUSTERED INDEX transl_transaction_line_x0 ON
   dbo.transl_transaction_line(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id)
  SELECT @errno = @@error
  
  IF @errno = 0
    SELECT @retry = 2
  ELSE
    BEGIN
     SELECT @retry = @retry + 1
     IF @errno = 1505 AND @retry = 1 -- duplicate
       BEGIN
        EXEC edit_duplicates_transl_$sp 50

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

RETURN

error:
	IF @errno < 100000
	  SELECT @errno = @errno + 100000
	SELECT @errmsg = 'edit_create_index_transl_$sp: ' + @errmsg

	RAISERROR @errno @errmsg
	
	RETURN
```

