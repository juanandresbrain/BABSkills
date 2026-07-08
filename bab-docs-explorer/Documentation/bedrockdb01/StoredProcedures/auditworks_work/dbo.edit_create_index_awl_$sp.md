# dbo.edit_create_index_awl_$sp

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.edit_create_index_awl_$sp"]
    edit_duplicates_awl__sp(["edit_duplicates_awl_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| edit_duplicates_awl_$sp |

## Stored Procedure Code

```sql
create proc dbo.edit_create_index_awl_$sp     
AS

/* 
Proc Name: edit_create_index_<transl_>$sp
DESCRIPTION: 
  This proc is called at least once by edit.ict. First, to try to create indices on transl tables after the bulk copy. 
  (Indices were dropped by edit_initialize_awl_$sp prior to BCP.) 
  If duplicates are encountered when creating unique indices, SQL Server 2005 wil raise error 1505, 
  and the catch will trap it and then retry. This proc will silently return control to the ICT.
  The ICT is still checking for error 1505 in sql.out, but will not find any. The proc edit_duplicates_awl_$sp    
  removes duplicates from all the transl tables.
  Note: Some of the indices could already exist depending on where the duplicates were found. 
        The retry while loop is retained and is now functional due to using try catch.

HISTORY:
Date     Name        Def# Desc
Jun29,15 Vicci TFS-127298 Handle auto-config requests for customer_detail (where customer info-type is -3)
Dec17,13 Paul      145958 use try .. catch, use new raiserror for compatability with SQL 2012.
Jan24,11 Paul      124176 Create clustered index for transl_transaction_line to improve performance
				by minimizing bookmark lookups
May04,05 David    DV-1202 Add indexes on transl_geninfo_detail and transl_transaction_line_link.
                          Check if index exists first before trying to create it. 
                          Also changed the way duplicates are handled. See description.
Mar23,05 Maryam   DV-1202 Rename from_line_id to line_id.
Mar15,05 David    DV-1202 Change index on transl_stock_control_detail.
Jul01,04 Vicci	  29561   Add index for transl_pos_tax_detail
Nov25,02 HenryW   1-FVT15 To log message to smartload.log when this proc has successfully completed.
Nov05,01 Paul     8900    author

*/

DECLARE @errmsg			nvarchar(2000),
	@errno			int,
	@process_name		nvarchar(30),
	@retry			tinyint,
	@trace_msg		nvarchar(255),
	@abort_flag		smallint,
	@blank			nchar(1);

SELECT @abort_flag = 0,
       @process_name = 'edit_create_index_awl_$sp';

/* Create indices on transl tables (previously dropped before loading the transl tables) */

IF NOT EXISTS (select * from sysindexes where id = object_id('awl_authorization_detail') and name = 'awl_authorization_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl auth table';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_authorization_x0 ON
     dbo.awl_authorization_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =   COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 42;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (auth)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_customer') and name ='awl_customer_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl customer';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX  awl_customer_x0 ON
     dbo.awl_customer(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, customer_role);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 51;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (cust)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_customer_detail') and name ='awl_customer_detail_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl customer_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_customer_detail_x0 ON
     dbo.awl_customer_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, customer_role, customer_info_type, lookup_pos_code);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 52;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (cust detail)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_discount_detail') and name ='awl_discount_x0')
BEGIN
    SELECT @errmsg =  'Failed to create index on transl discount_detail';

    BEGIN TRY
     CREATE NONCLUSTERED INDEX awl_discount_x0 ON
     dbo.awl_discount_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id);

    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
        GOTO business_error;
    END CATCH;

END; -- if not exists (disc)

IF NOT EXISTS (select * from sysindexes where id = object_id('awl_line_note') and name = 'awl_line_note_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl line_note';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_line_note_x0 ON
     dbo.awl_line_note (transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, note_type);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 53;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (line_note)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_payroll_detail') and name ='awl_payroll_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl payroll_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_payroll_x0 ON
      dbo.awl_payroll_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id);
     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 46;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (payroll)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_post_void_detail') and name ='awl_post_void_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl post_void_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_post_void_x0 ON
      dbo.awl_post_void_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 45;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (post_void_detail)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_special_order_detail') and name ='awl_special_order_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl special_order_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_special_order_x0 ON
     dbo.awl_special_order_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 44;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (special_order_detail)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_stock_control_detail') and name ='awl_stock_control_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl stock_control_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_stock_control_x0 ON
     dbo.awl_stock_control_detail (transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, display_def_id);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 43;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (stock_control_detail)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_tax_override_detail') and name ='awl_tax_override_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl tax_override_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_tax_override_x0 ON
     dbo.awl_tax_override_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, tax_level);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 48;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (tax_override_detail)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_return_detail') and name ='awl_return_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl return_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_return_x0 ON
     dbo.awl_return_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 49;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (return_detail)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_transaction_line') and name ='awl_transaction_line_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl transaction_line';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE CLUSTERED INDEX awl_transaction_line_x0 ON
     dbo.awl_transaction_line(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 50;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (transaction_line)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_pos_tax_detail') and name ='awl_pos_tax_detail_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl pos_tax_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_pos_tax_detail_x0 ON
     dbo.awl_pos_tax_detail(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, tax_rate_id, tax_jurisdiction_id, tax_level);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 54;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (pos_tax_detail)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_geninfo_detail') and name ='awl_geninfo_detail_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl geninfo_detail';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_geninfo_detail_x0 ON
     dbo.awl_geninfo_detail (transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, form_name, field_name);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 55;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (geninfo_detail)


IF NOT EXISTS (select * from sysindexes where id = object_id('awl_transaction_line_link') and name ='awl_transaction_line_link_x0')
BEGIN
  SELECT @retry = 0,
	@errmsg =  'Failed to create index on transl transaction_line_link';

  WHILE @retry <= 1 AND @abort_flag = 0
  BEGIN
    BEGIN TRY
     CREATE UNIQUE NONCLUSTERED INDEX awl_transaction_line_link_x0 ON
     dbo.awl_transaction_line_link(transaction_no, entry_date_time, register_no, store_no, transaction_series, line_id, linked_line_id);

     SELECT @retry = 99;
    END TRY
    BEGIN CATCH;
      SELECT @errno = ERROR_NUMBER(),
		@errmsg =  COALESCE(@errmsg, @blank) + ERROR_MESSAGE();
      SELECT @retry = @retry + 1;
      IF @errno = 1505 AND @retry = 1 -- duplicate
        BEGIN
         EXEC edit_duplicates_awl_$sp 56;
        END;
      ELSE
        GOTO business_error;
    END CATCH;

  END; --   WHILE @retry <= 1
END; -- if not exists (transaction_line_link)


SELECT @trace_msg = NCHAR(13) + NCHAR(10) + ':LOG && edit create index completed: ' + CONVERT(nchar, getdate(), 8);
PRINT @trace_msg;

RETURN;

/* Any errors raised here will be captured in the edit smrtload.log file.
   Not using common error handling here because this proc runs in auditworks_work. */

business_error:
	SELECT @errmsg = CONVERT(nvarchar,@errno) + ':' + @process_name + ':' + COALESCE(@errmsg,@blank);

	RAISERROR (@errmsg, 16, 1);
	
	RETURN;
```

