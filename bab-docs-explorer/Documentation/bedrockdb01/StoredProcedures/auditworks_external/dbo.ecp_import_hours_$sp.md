# dbo.ecp_import_hours_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ecp_import_hours_$sp"]
    auditworks_parameter(["auditworks_parameter"]) --> SP
    code_description(["code_description"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    ecp_import_hours(["ecp_import_hours"]) --> SP
    function_status(["function_status"]) --> SP
    input_payroll_detail(["input_payroll_detail"]) --> SP
    input_stock_control_detail(["input_stock_control_detail"]) --> SP
    input_transaction_hdr(["input_transaction_hdr"]) --> SP
    input_transaction_line(["input_transaction_line"]) --> SP
    interface_applicability(["interface_applicability"]) --> SP
    language_resource(["language_resource"]) --> SP
    line_object(["line_object"]) --> SP
    line_object_action_association(["line_object_action_association"]) --> SP
    line_object_action_attachment(["line_object_action_attachment"]) --> SP
    parameter_general(["parameter_general"]) --> SP
    process_error_log(["process_error_log"]) --> SP
    register(["register"]) --> SP
    reserve_input_id__sp(["reserve_input_id_$sp"]) --> SP
    reserve_transaction_no__sp(["reserve_transaction_no_$sp"]) --> SP
    submit_input_id__sp(["submit_input_id_$sp"]) --> SP
    transaction_generation_source(["transaction_generation_source"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| auditworks_parameter |
| code_description |
| common_error_handling_$sp |
| ecp_import_hours |
| function_status |
| input_payroll_detail |
| input_stock_control_detail |
| input_transaction_hdr |
| input_transaction_line |
| interface_applicability |
| language_resource |
| line_object |
| line_object_action_association |
| line_object_action_attachment |
| parameter_general |
| process_error_log |
| register |
| reserve_input_id_$sp |
| reserve_transaction_no_$sp |
| submit_input_id_$sp |
| transaction_generation_source |

## Stored Procedure Code

```sql
create proc dbo.ecp_import_hours_$sp 
AS
/* 
   NAME:    ecp_import_hours_$sp
   DESCR:   Imports payroll hour data and calls the cust_liability_processing_$sp 
            which in turn will populate the input tables with transaction information generated 
            based on the information imported. The transactions 
            generated will then flow through the normal edit to update the ECP application.
            Called by ICT_IMPORT smartload.
     
HISTORY:
Date      Name             Defect#  Description
Mar25,14  Vicci           150880    Add shift identifier, just for the sake of consistency with the Direct Feed Translate of TAE Export.  
Feb13,14  Vicci           149581    Avoid 'Cannot insert duplicate key row in object dbo.language_resource with unique index language_resource_x1.' error.
Apr20,12  Paul            134132    prevent error 2627 by setting dummy_transaction_category on insert
Feb28,12  Vicci           133336    Correct datatype of process_id since receiving procs are expecting a binary(16).
Dec18,08  Paul            106848    make compatible with SA5 by passing process_id, user_id to sub procs
Sep03,08  Vicci           104484    Add shift start/end time logging 
Apr30,08  Vicci            95521    Only do S/A 4.1 code via dynamic sql to avoid compilation errors in 5.0    
Feb04,08  Vicci            97607    Auto-verify process-errors upon successful completion.
Dec14,07  Vicci            95521    Only auto-create employee in S/A 4.1
Aug07,07  Vicci            85597    Don't create null employee types or selling areas
Jul11,07  Vicci            85597    Don't log a comma when neither first nor last name are provided
Mar02,07  Vicci            85597    Author
*/

DECLARE @auto_create_missing_empl	tinyint,
        @cursor_open			tinyint,
	@errmsg				nvarchar(2000),
	@errno				int,
	@errno2				int,
        @function_name	                varbinary(128),
	@import_row_count		int,
	@import_row_id			numeric(10,0),
	@input_id			numeric(12,0),
	@message_id			int,
	@max_import_row_id		numeric(10,0), 
	@min_import_row_id		numeric(10,0), 
        @max_lines_per_trans		smallint,
	@max_tran_no			int,
        @next_tran_no			int,
	@object_name			nvarchar(255),
	@operation_name			nvarchar(100),
	@process_name			nvarchar(100),
	@process_no 			smallint,
	@process_id  		        binary(16),
	@spid				int,
	@process_start_datetime		datetime,
	@rows				int,
	@row_no				int,
        @status			        smallint, 
        @store_no			int,
        @register_no			smallint,
        @cashier_no			int,
        @transaction_series		nchar(1),
        @transaction_category		tinyint,
        @trans_qty			int,
        @sql_command 			nvarchar(4000),
        @release_41			tinyint,
        @resource_id			numeric(12,0)

SELECT @function_name = convert(varbinary(128), 'ecp_import_hours_$sp'),
       @max_lines_per_trans = 100,
       @message_id = 201068,
       @operation_name = 'Unknown',
       @process_id = NEWID(), 		--TODO:  halted process recovery
       @spid = @@spid, 		--TODO:  halted process recovery
       @process_name = 'ecp_import_hours_$sp',
       @process_no = 51,
       @process_start_datetime = getdate(),
       @status = -1,
       @release_41 = 0

SET CONTEXT_INFO @function_name

IF EXISTS (SELECT 1
              FROM parameter_general
             WHERE release_no LIKE '4.1.%')
  SELECT @release_41 = 1

IF EXISTS (SELECT 1 
             FROM auditworks_parameter
            WHERE par_name = 'ecp_auto_create_missing_empl'
              AND par_value = '1'
              AND @release_41 = 1) -- not needed yet in SA5
BEGIN
  INSERT into code_description(                   --TODO S/A 5.1
         code_type,
         code,
         code_display_descr,
         code_meaning_control)
  SELECT DISTINCT 74,
         payroll_entry_selling_area_no, 
         'Unknown (' + CONVERT(nvarchar, payroll_entry_selling_area_no) + ')',
 'U'
    FROM ecp_import_hours
   WHERE payroll_entry_selling_area_no IS NOT NULL
     AND payroll_entry_selling_area_no NOT IN (SELECT sa.code
                                                 FROM code_description sa
                                                WHERE code_type = 74)
  SELECT @errno = @@error
  IF @errno != 0
 BEGIN
    SELECT @errmsg = 'Failed to create missing employee selling areas',
           @object_name = 'code_description',
    @operation_name = 'INSERT'
    GOTO error
  END       

  -- SA4.1
  SELECT @sql_command = '
  INSERT into employee_type(                   
         employee_type,
         employee_type_descr,
         regular_discount_rate,
         outlet_discount_rate)
  SELECT DISTINCT
         payroll_entry_position, 
         ''Unknown'',
         0, 0
    FROM ecp_import_hours
   WHERE payroll_entry_position IS NOT NULL
     AND payroll_entry_position NOT IN (SELECT et.employee_type
                                          FROM employee_type et)
  SELECT @errno = @@error'

  EXEC sp_executesql @sql_command, N'@errno int OUT', @errno OUT              
    SELECT @errno2 = @@error
    IF @errno <> 0 OR @errno2 <> 0
    BEGIN
      PRINT @sql_command
      IF @errno2 <> 0 SELECT @errno = @errno2
      SELECT @errmsg = 'Failed to create missing employee positions via dynamic SQL',
             @object_name = 'employee',
             @operation_name = 'INSERT'
        GOTO error
    END

  -- SA4.1
  SELECT @sql_command = '      
  INSERT into employee(employee_no,
         employee_first_name,
         employee_last_name,
         home_store_no,
         employee_type,
         verified,
         employee_department)
  SELECT employee_no, 
         MAX(substring(employee_first_name, 1, 20)), 
         MAX(substring(employee_last_name, 1, 20)),
         MAX(store_no),
         MAX(substring(payroll_entry_position, 1, 1)),
         0,
         MAX(payroll_entry_selling_area_no)
    FROM ecp_import_hours
   WHERE employee_no NOT IN (SELECT e.employee_no
                               FROM ecp_import_hours h
                                    INNER JOIN employee e
                                    ON h.employee_no = e.employee_no)
     AND employee_first_name IS NOT NULL
     AND employee_last_name IS NOT NULL
   GROUP BY employee_no
  SELECT @errno = @@error'

--  For SA5, could call inside a cursor after reading default country (proc can handle 2 or 3 char)
--  SELECT @sql_command = 'EXEC populate_EMPLY_$sp', @EMPLY_NUM, @FRST_NAME, @LAST_NAME, 1, null,
--    @PRMY_ORG_CHN_NUM, null, null, null, null, @CNTRY_CODE_ISO3, null, null
-- would also need to insert EMPLY_ORG_CHN_POSTN* tables

  EXEC sp_executesql @sql_command, N'@errno int OUT', @errno OUT              
    SELECT @errno2 = @@error
    IF @errno <> 0 OR @errno2 <> 0
    BEGIN
      PRINT @sql_command
      IF @errno2 <> 0 SELECT @errno = @errno2
      SELECT @errmsg = 'Failed to create missing employees via dynamic SQL',
             @object_name = 'employee',
             @operation_name = 'INSERT'
        GOTO error
    END
END  --IF ecp_auto_create_missing_empl = 1

SELECT @store_no = g.store_no,
       @register_no = r.register_no,
       @cashier_no = g.cashier_no,
       @transaction_series = g.transaction_series,
       @transaction_category = g.transaction_category
  FROM transaction_generation_source g
       LEFT OUTER JOIN register r         -- exists as a view in SA5
         ON g.store_no = r.store_no
        AND g.register_no = r.register_no
 WHERE process_no = @process_no    
SELECT @errno = @@error
IF @errno != 0
BEGIN
  SELECT @errmsg = 'Failed to select from transaction_generation_source.',
         @object_name = 'transaction_generation_source',
         @operation_name = 'SELECT'
  GOTO error
END 

IF @register_no IS NULL
BEGIN
  SELECT @errmsg = 'Transaction generation source table has not been set up',
         @errno = 201678,
         @message_id = 201678
  GOTO error
END        

SELECT @trans_qty = CEILING(CONVERT(FLOAT,COUNT(*))/@max_lines_per_trans)
  FROM ecp_import_hours
SELECT @errno = @@error
IF @errno != 0
BEGIN
  SELECT @errmsg = 'Failed to determine number of transactions to generate',
         @object_name = 'ecp_import_hours',
         @operation_name = 'SELECT'
  GOTO error
END 

IF @trans_qty = 0
  GOTO reset_exit

IF @release_41 = 1
  EXEC reserve_input_id_$sp null, @input_id OUTPUT, @errmsg OUTPUT, @process_no
ELSE
  EXEC reserve_input_id_$sp @process_id, null, null, @input_id OUTPUT, @errmsg OUTPUT, @process_no

SELECT @errno = @@error
IF @errno != 0
BEGIN
  IF @errmsg IS NULL -- 
    SELECT @errmsg = 'Failed to execute stored proc reserve_input_id_$sp.'
  SELECT @object_name = 'reserve_input_id_$sp',
         @operation_name = 'EXECUTE'
  GOTO error
END

IF @release_41 = 1  
  EXEC reserve_transaction_no_$sp @process_no, @store_no,@register_no,@transaction_series,
     @trans_qty, @max_tran_no OUTPUT, @next_tran_no OUTPUT, @errmsg OUTPUT
ELSE
  EXEC reserve_transaction_no_$sp @process_id, null, @process_no, @store_no, @register_no, @transaction_series,
     @trans_qty, @max_tran_no OUTPUT, @next_tran_no OUTPUT, @errmsg OUTPUT

SELECT @errno = @@error
IF @errno != 0
BEGIN
  IF @errmsg IS NULL --
    SELECT @errmsg = 'Failed to execute stored procedure reserve_transaction_no_$sp'
  SELECT @object_name = 'reserve_transaction_no_$sp',
         @operation_name = 'EXECUTE'
  GOTO error
END

IF NOT EXISTS (SELECT line_object 
                 FROM line_object
                WHERE line_object_type = 13 and line_object = 9059)
BEGIN
  SELECT @resource_id = NULL
  SELECT @resource_id = resource_id
    FROM language_resource
   WHERE table_name = 'line_object'
     AND table_key = '9059'
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Failed to determine if resource_id already exists. ',
  	   @object_name = 'language_resource',
	   @operation_name = 'SELECT'
    GOTO error
  END

  INSERT into line_object(line_object,
                        line_object_type,
                        line_object_description,
                        default_tax_rate_code,
                        lookup_pos_code,
                        pos_description_token_list,
                        resource_id)
  VALUES(9059,
         13,
         'Shift hours',
         0,
         '013.217.shiftDuration',
         'Shift hours',
         @resource_id)
    SELECT @errno = @@error
    IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Failed to insert line_object',
               @object_name = 'line_object',
               @operation_name = 'INSERT'
        GOTO error
      END 
END

IF NOT EXISTS (SELECT line_object
                 FROM line_object_action_association
                WHERE transaction_category = @transaction_category
                  AND line_object = 9059
                  AND line_action = 38)  
  BEGIN
    INSERT INTO line_object_action_association
           (transaction_category,
            line_object,
            line_action,
            line_object_type,
            db_cr_none,
            store_balance_group,
            reference_type,
            reference_no_option)
    SELECT @transaction_category,
           9059,
           38,
           13,
           0,
           0,
           217,
           1
    SELECT @errno = @@error
    IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Failed to insert line_object_action_association.',
               @object_name = 'line_object_action_association',
               @operation_name = 'INSERT'
        GOTO error
      END 
  END

IF NOT EXISTS (SELECT line_object
                 FROM line_object_action_attachment
                WHERE (transaction_category = @transaction_category
                       OR transaction_category IS NULL)
                  AND attachment_type = 3
                  AND line_object = 9059
                  AND line_action = 38
                  AND note_type = 58)
  BEGIN 
    INSERT INTO line_object_action_attachment
           (line_object,
            line_action,
            transaction_category,
            attachment_type,
            note_type,
            dummy_transaction_category)
    VALUES (9059,
            38,
            @transaction_category,
            3, 
            58,
            COALESCE(CONVERT(nvarchar,@transaction_category),'null'))                
    SELECT @errno = @@error
    IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Failed to insert line_object_action_attachment.',
               @object_name = 'line_object_action_attachment',
               @operation_name = 'INSERT'
        GOTO error
      END                                
  END          

IF NOT EXISTS (SELECT line_object
                 FROM line_object_action_attachment
                WHERE (transaction_category = @transaction_category
                       OR transaction_category IS NULL)
                  AND attachment_type = 6
            AND line_object = 9059
                  AND line_action = 38
                  AND note_type = 0)
  BEGIN 
    INSERT INTO line_object_action_attachment
           (line_object,
            line_action,
            transaction_category,
            attachment_type,
            note_type,
            attachment_mandatory,
            dummy_transaction_category)
    VALUES (9059,
            38,
            @transaction_category,
            6, 
            0,
            1,
            COALESCE(CONVERT(nvarchar,@transaction_category),'null'))                
    SELECT @errno = @@error
    IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Failed to insert line_object_action_attachment payroll detail.',
               @object_name = 'line_object_action_attachment',
               @operation_name = 'INSERT'
        GOTO error
      END                                
  END              

IF NOT EXISTS (SELECT line_object
                 FROM interface_applicability
                WHERE transaction_category = @transaction_category
                  AND interface_id = 44
                  AND line_object = 9059
     AND line_action = 38)
BEGIN 
  INSERT INTO interface_applicability
           (interface_id,
            line_object,
            line_action,
            transaction_category)
  VALUES (44,
           9059,
            38,
            @transaction_category)                
  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to insert interface_applicability for ECP hours feed',
           @object_name = 'interface_applicability',
           @operation_name = 'INSERT'
    GOTO error
  END                                
END   

INSERT INTO input_transaction_line (
       input_id, 
       store_no, 
       register_no, 
       entry_date_time, 
       transaction_series, 
       transaction_no, 
       line_id, 
       line_object, 
       line_action, 
       gross_line_amount, 
       reference_no)
SELECT @input_id, 
       @store_no, 
       @register_no, 
       @process_start_datetime, 
       @transaction_series, 
       (@next_tran_no + CONVERT(int, (entry_id-1)/@max_lines_per_trans)), 
       entry_id - CONVERT(int, (entry_id-1)/@max_lines_per_trans) * @max_lines_per_trans, 
       9059, 
       38, 
       hours,
       convert(nvarchar, period_end_datetime, 101) + ' ' +  convert(nvarchar, period_end_datetime, 108)
  FROM ecp_import_hours
SELECT @errno = @@error
IF @errno != 0 
BEGIN
  SELECT @errmsg = 'Failed to insert into input_transaction_line',
         @object_name = 'input_transaction_line',
         @operation_name = 'INSERT'
  GOTO error
END  

INSERT into input_stock_control_detail(
   input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       pos_deptclass,
       other_store_no,
       vendor_no,
       display_def_id,
       reason,
       count_date)
SELECT @input_id, 
       @store_no, 
       @register_no, 
       @process_start_datetime, 
       @transaction_series, 
       (@next_tran_no + CONVERT(int, (i.entry_id-1)/@max_lines_per_trans)), 
       i.entry_id - CONVERT(int, (i.entry_id-1)/@max_lines_per_trans) * @max_lines_per_trans, 
       i.payroll_entry_selling_area_no,
       i.store_no,
       CASE WHEN IsNull(i.employee_last_name, '') <> '' OR IsNull(i.employee_first_name, '') <> '' THEN IsNull(i.employee_last_name, '') + CASE WHEN IsNull(i.employee_last_name, '') <> '' THEN ', ' ELSE '' END + IsNull(i.employee_first_name, '') ELSE NULL END,
       58,
 '1',
       i.shift_start_datetime 
  FROM ecp_import_hours i
SELECT @errno = @@error
IF @errno != 0 
BEGIN
  SELECT @errmsg = 'Failed to insert into input_stock_control_detail',
         @object_name = 'input_stock_control_detail',
         @operation_name = 'INSERT'
  GOTO error
END  

INSERT into input_payroll_detail(
       input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       employee_no,
       payroll_date,
       employee_type,
       payroll_entry_type)
SELECT @input_id, 
       @store_no, 
       @register_no, 
       @process_start_datetime, 
       @transaction_series, 
       (@next_tran_no + CONVERT(int, (entry_id-1)/@max_lines_per_trans)), 
       entry_id - CONVERT(int, (entry_id-1)/@max_lines_per_trans) * @max_lines_per_trans, 
       employee_no, 
       period_end_datetime, 
       substring(payroll_entry_position, 1, CASE WHEN @release_41 = 1 THEN 1 ELSE 4 END),  
       IsNull(c.code, CASE WHEN Isnumeric(payroll_entry_hour_type_alpha) = 1 
                           THEN convert(smallint, payroll_entry_hour_type_alpha) 
                           ELSE NULL 
                           END)
  FROM ecp_import_hours i
  LEFT OUTER JOIN code_description c
       ON i.payroll_entry_hour_type_alpha = IsNull(c.alpha_code, convert(nvarchar, c.code))
       AND c.code_type = 29
SELECT @errno = @@error
IF @errno != 0 
BEGIN
  SELECT @errmsg = 'Failed to insert into input_payroll_detail',
         @object_name = 'input_payroll_detail',
         @operation_name = 'INSERT'
  GOTO error
END  

INSERT INTO input_transaction_hdr (
  	input_id, 
  	store_no, 
  	register_no, 
  	entry_date_time, 
  	transaction_series, 
  	transaction_no, 
  	cashier_no, 
  	transaction_category  )
SELECT
  	@input_id, 
  	@store_no, 
  	@register_no, 
  	@process_start_datetime, 
  	@transaction_series, 
  	transaction_no, 
  	@cashier_no, 
  	@transaction_category
  FROM input_transaction_line
 WHERE input_id = @input_id 
   AND line_id = 1
SELECT @errno = @@error
IF @errno != 0 
BEGIN
  SELECT @errmsg = 'Failed to insert into input_transaction_hdr',
         @object_name = 'input_transaction_hdr',
         @operation_name = 'INSERT'
  GOTO error
END  

IF @release_41 = 1
BEGIN
  UPDATE function_status
     SET status = 1
   WHERE process_id = @spid
     AND function_no = @process_no
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to update function_status',
  	   @object_name = 'function_status',
	   @operation_name = 'UPDATE'
    GOTO error
  END

  EXEC submit_input_id_$sp @input_id, @process_start_datetime OUTPUT, @errmsg OUTPUT
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to execute submit_input_is_$sp for S/A 4.1',
	   @object_name = 'submit_input_is_$sp',
	   @operation_name = 'EXEC'
    GOTO error
  END
END
ELSE
BEGIN
  UPDATE function_status
     SET status = 1
   WHERE process_id = @process_id
     AND function_no = @process_no
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to update function_status',
  	   @object_name = 'function_status',
	   @operation_name = 'UPDATE'
    GOTO error
  END

EXEC submit_input_id_$sp @process_id, null, @input_id, @process_start_datetime OUTPUT, @errmsg OUTPUT
  SELECT @errno = @@error
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to execute submit_input_is_$sp',
	   @object_name = 'submit_input_is_$sp',
	   @operation_name = 'EXEC'
    GOTO error
  END
END

UPDATE process_error_log
   SET verified = 1
 WHERE error_timestamp >= dateadd(dd, -30, getdate())
   AND process_no in (7, 51) --ecp import
   AND verified = 0
   AND (object_name = 'ecp_import_hours' OR process_name = 'ecp_import_hours_$sp')

reset_exit:
SELECT @function_name = convert(varbinary(128), 'Unknown')
SET CONTEXT_INFO @function_name
RETURN

error:   		-- common error handler 
        SELECT @function_name = convert(varbinary(128), 'Unknown')
        SET CONTEXT_INFO @function_name 

	IF @release_41 = 1	
	  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	       @process_name, @object_name, @operation_name, 1
	ELSE	
	   EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	        @process_name, @object_name, @operation_name, 1, 1, 0, null, 0, null, null, 
	        null, null, null, null, 0, @process_id, NULL

	RETURN
```

