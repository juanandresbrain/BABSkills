# dbo.edit_exceptions_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.edit_exceptions_$sp"]
    audit_status(["audit_status"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    exception_post__sp(["exception_post_$sp"]) --> SP
    exception_reason(["exception_reason"]) --> SP
    exception_rule(["exception_rule"]) --> SP
    line_object_action_association(["line_object_action_association"]) --> SP
    transaction_header(["transaction_header"]) --> SP
    transaction_line(["transaction_line"]) --> SP
    work_edit_batch_list(["work_edit_batch_list"]) --> SP
    work_exceptions(["work_exceptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| audit_status |
| common_error_handling_$sp |
| exception_post_$sp |
| exception_reason |
| exception_rule |
| line_object_action_association |
| transaction_header |
| transaction_line |
| work_edit_batch_list |
| work_exceptions |

## Stored Procedure Code

```sql
create proc dbo.edit_exceptions_$sp   @process_id binary(16),
  @user_id	int,
  @errmsg nvarchar(255) OUTPUT

AS

  /* 
    
    Proc Name : edit_exceptions_$sp
         Desc : To create entries in exception_reason for any transactions containing
                line_object/action/tran_category that are flagged as exceptions.
                Calculate/Recalculate exception_qty in audit_status.
                Called by edit_phase2_$sp.

    HISTORY

    Date     Name         Def#  Desc
    Dec05,14 Paul        94103  use try catch
    Aug11,09 Phu        111945  Fix unique constraint exception_reason_x0 when the new trans is edited phase2 for the same store date that was previously done phase2.
    Apr29,05 Paul      DV-1234  expand transaction_id to use tran_id_datatype
    Dec13,04 Maryam    DV-1191  Change select into temp to create temp tables and insert into.
    Dec02,04 Paul      DV-1181  look at actv flag in exception_rule, added nolock hints
    Sep23,04 David     DV-1146  Use user_id instead of user_name.
    Jul09,04 ShuZ      DV-1071  Expand user_name to nvarchar(50)    
    May05,04 Maryam    DV-1071  Receive @process_id and @user_name and pass it to the sub procs.
    Nov27,01 Ian K     1-97UU6  Edit Phase 2 batching for R3
    Nov13,00 Paul         6946  Do not look at edit_progress_flag
    Mar01,00 Phu          5900  Change @@fetch_status > 0 to @@fetch_status <> 0 for MS SQL compatibility
    Feb08,00 JimC         5955  Bumped version number to force re-save in B10 upgrade. 
    Apr23,98 Paul               V1.08 Last modified.
    Feb05,98 Paul               V1.07
    Author   Paul

  */
 
DECLARE 

  @cursor_open                    tinyint,
  @errmsg2                        nvarchar(2000),
  @errline                        int,
  @errno                          int,
  @rows                           int,
  @store_no                       int,
  @object_name                    nvarchar(255),
  @process_name                   nvarchar(100),
  @operation_name                 nvarchar(100),
  @process_no                     int,
  @message_id		       int;
  
  SELECT @process_name     = 'edit_exceptions_$sp',
         @process_no       = 5,
         @message_id       = 201068;

  BEGIN TRY

      SELECT @errmsg         = 'Failed to create temp table #exception_list',
           @object_name    = '#exception_list',
           @operation_name = 'CREATE TABLE';
  CREATE TABLE #exception_list(transaction_id numeric(14,0) not null, -- tran_id_datatype
                               line_id numeric(5,0) not null,
                               exception_reason smallint null,
                               exception_type tinyint not null);
                         
     SELECT @errmsg         = 'Failed to create temp table #transaction_list',
           @object_name    = '#transaction_list';
  CREATE TABLE #transaction_list (transaction_id numeric(14,0) not null); -- tran_id_datatype
                          
      SELECT @errmsg         = 'Failed to create temp table #exception_counts',
           @object_name    = '#exception_counts';
  CREATE TABLE #exception_counts(store_no int not null,
                                 register_no smallint not null,
                                 transaction_date smalldatetime not null,
                                 exception_count smallint not null);

    SELECT @errmsg         = 'Failed to insert into temp table #exception_list',
           @object_name    = '#exception_list',
           @operation_name = 'INSERT';
  INSERT INTO #exception_list(
         transaction_id,
         line_id,
         exception_reason,
         exception_type)
  SELECT tl.transaction_id,
         line_id,
         exception_reason,
         er.exception_type 
    FROM work_edit_batch_list sl WITH (NOLOCK), 
         transaction_header th WITH (NOLOCK),
         transaction_line tl WITH (NOLOCK), 
 line_object_action_association la, 
         exception_rule er
   WHERE sl.date_reject_id     = 0
     AND sl.transaction_date     = th.transaction_date
     AND sl.store_no             = th.store_no
     AND sl.register_no          = th.register_no
     AND th.sa_rejection_flag    = 0
     AND th.transaction_id       = tl.transaction_id
     AND tl.line_object          = la.line_object
     AND tl.line_action          = la.line_action
     AND th.transaction_category = la.transaction_category
     AND la.exception_reason    >= 1 
     AND la.exception_reason     = er.exception_rule 
     AND er.exception_type    >= 1
     AND er.ACTV = 1;

  SELECT @rows = @@rowcount;

  IF @rows >= 1
  BEGIN
    
    -- Get list of exception transactions
      SELECT @errmsg         = 'Failed to insert into table #transaction_list',
             @object_name    = '#transaction_list',
             @operation_name = 'INSERT';
    INSERT INTO #transaction_list(
           transaction_id)
    SELECT DISTINCT transaction_id
      FROM #exception_list WITH (NOLOCK)
     WHERE exception_type = 1;

    -- Avoid duplicating exceptions which already exist
    -- e.g. when a day has previously been partially edited
      SELECT @errmsg         = 'Failed to delete #exception_list',
             @object_name    = '#exception_list',
             @operation_name = 'DELETE';
    DELETE #exception_list
      FROM #exception_list el,
           exception_reason er 
     WHERE el.transaction_id = er.transaction_id;

      SELECT @errmsg         = 'Failed to update transaction_line',
             @object_name    = 'transaction_line',
             @operation_name = 'UPDATE';
    UPDATE transaction_line
       SET exception_flag = 1
      FROM #exception_list el WITH (NOLOCK), 
           transaction_line tl
     WHERE el.transaction_id = tl.transaction_id
       AND el.line_id        = tl.line_id 
       AND exception_type  = 1;

      SELECT @errmsg         = 'Failed to update transaction_header',
             @object_name    = 'transaction_header',
             @operation_name = 'UPDATE';
    UPDATE transaction_header
       SET exception_flag = 1
      FROM #transaction_list ls WITH (NOLOCK), 
           transaction_header th
     WHERE ls.transaction_id = th.transaction_id;


      SELECT @errmsg         = 'Failed to drop #transaction_list',
             @object_name    = '#transaction_list',
             @operation_name = 'DROP TABLE';
    DROP TABLE #transaction_list;

      SELECT @errmsg         = 'Failed to insert exception_reason',
             @object_name    = 'exception_reason',
             @operation_name = 'INSERT';
    INSERT exception_reason (
           transaction_id,
           line_id,
           violated_exception_rule,
           exception_type)
    SELECT transaction_id,
           line_id,
           exception_reason,
           exception_type
      FROM #exception_list WITH (NOLOCK);

  END; -- If @rows >= 1

      SELECT @errmsg         = 'Failed to drop #exception_list',
             @object_name    = '#exception_list',
             @operation_name = 'DROP TABLE';
  DROP TABLE #exception_list;

      SELECT @errmsg         = 'Failed to delete work_exceptions',
             @object_name    = 'work_exceptions',
             @operation_name = 'DELETE';
  DELETE work_exceptions
   WHERE process_id = @process_id;

    SELECT @errmsg         = 'Failed to open cursor exception_crsr',
           @object_name    = 'exception_crsr',
           @operation_name = 'OPEN';
  DECLARE exception_crsr CURSOR FAST_FORWARD
      FOR
    SELECT DISTINCT store_no
      FROM work_edit_batch_list WITH (NOLOCK);

  OPEN exception_crsr;
  SELECT @cursor_open = 1;

  WHILE 1=1
  BEGIN

    FETCH exception_crsr 
     INTO @store_no;

    IF @@fetch_status <> 0
      BREAK;

    -- Get list of transactions to evaluate
      SELECT @errmsg         = 'Failed to insert work_exceptions',
             @object_name    = 'work_exceptions',
             @operation_name = 'INSERT';
    INSERT work_exceptions (
           process_id,
           transaction_id )
    SELECT @process_id,
           transaction_id
      FROM work_edit_batch_list sl WITH (NOLOCK),
           transaction_header th WITH (NOLOCK)
     WHERE sl.store_no         = @store_no
       AND sl.transaction_date = th.transaction_date
       AND sl.store_no         = th.store_no
       AND sl.register_no      = th.register_no
       AND sl.date_reject_id   = th.date_reject_id
       AND sa_rejection_flag   = 0
       AND th.transaction_id NOT IN (SELECT e.transaction_id
                                     FROM exception_reason e, exception_rule er 
                                     WHERE e.violated_exception_rule = er.exception_rule
                                     AND er.SQL_QRY IS NOT NULL);

    -- Call user exception procedure
      SELECT @errmsg       = 'Failed to execute stored procedure exception_post_$sp',
             @object_name    = 'exception_post_$sp',
             @operation_name = 'EXECUTE';
    EXEC exception_post_$sp @process_id, @user_id, @errmsg OUTPUT;

      SELECT @errmsg         = 'Failed to delete work_exceptions (2)',
             @object_name    = 'work_exceptions',
             @operation_name = 'DELETE';
    DELETE work_exceptions
     WHERE process_id = @process_id;

  END; -- While 1=1 End of user exception cursor

  CLOSE exception_crsr;
  DEALLOCATE exception_crsr;
  SELECT @cursor_open = 0;
 
  -- Recalculate audit_status exception_qty
    SELECT @errmsg         = 'Failed to build temp table #exception_counts',
           @object_name    = '#exception_counts',
           @operation_name = 'INSERT';
  INSERT INTO #exception_counts(
         store_no,
         register_no,
         transaction_date,
         exception_count)
  SELECT sl.store_no,
         sl.register_no,
         sl.transaction_date,
         COUNT(th.transaction_id)    
    FROM work_edit_batch_list sl WITH (NOLOCK), 
         transaction_header th WITH (NOLOCK)
   WHERE sl.date_reject_id = 0
     AND sl.transaction_date = th.transaction_date
     AND sl.store_no = th.store_no
     AND sl.register_no = th.register_no
     AND exception_flag = 1
   GROUP BY sl.store_no, sl.transaction_date, sl.register_no;

    SELECT @errmsg         = 'Failed to update audit_status',
           @object_name    = 'audit_status',
           @operation_name = 'UPDATE';
  UPDATE audit_status
     SET exception_qty = ec.exception_count
    FROM #exception_counts ec WITH (NOLOCK), audit_status st
   WHERE ec.store_no         = st.store_no
     AND ec.register_no      = st.register_no
     AND ec.transaction_date = st.sales_date
     AND date_reject_id      = 0;


  RETURN;

  
business_error:   /* Business Rule handler. */

	SELECT @errmsg2 = @errmsg;

	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name,
	       @object_name, @operation_name, 1, 1, 0, null, 0, null, null, null, null, null, null,
	       0, @process_id, @user_id;
	  /* Note: when the exec above raises an error, that action also fires the system error trap (below) */
	RETURN;
END TRY

BEGIN CATCH; -- trap system errors
    /* common error handling. Appending proc name here because a rollback could occur if called within a transaction. */

        SELECT @errno = ERROR_NUMBER(),
		@errline = ERROR_LINE();

        SELECT @errmsg = CONVERT(nvarchar, @errno) + ':' + @process_name + ':' + CONVERT(nvarchar, @errline) + ':'
               + COALESCE(@errmsg, ' ') + ':' + ERROR_MESSAGE();

	 /* this condition will only be true when raise error in traps above fire this general catch */
	IF @errmsg2 IS NOT NULL
	  SELECT @errmsg = @errmsg2;

	IF @cursor_open = 1
	  BEGIN
	    CLOSE exception_crsr;
	    DEALLOCATE exception_crsr;
	 END;
	  
	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name,
	       @object_name, @operation_name, 1, 1, 0, null, 0, null, null, null, null, null, null,
	       0, @process_id, @user_id;

	RETURN;
END CATCH;
```

