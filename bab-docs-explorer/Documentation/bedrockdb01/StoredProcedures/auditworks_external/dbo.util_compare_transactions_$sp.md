# dbo.util_compare_transactions_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_compare_transactions_$sp"]
    authorization_detail(["authorization_detail"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    customer(["customer"]) --> SP
    customer_detail(["customer_detail"]) --> SP
    discount_detail(["discount_detail"]) --> SP
    if_rejection_reason(["if_rejection_reason"]) --> SP
    interface_control(["interface_control"]) --> SP
    line_note(["line_note"]) --> SP
    merchandise_detail(["merchandise_detail"]) --> SP
    payroll_detail(["payroll_detail"]) --> SP
    post_void_detail(["post_void_detail"]) --> SP
    return_detail(["return_detail"]) --> SP
    sa_rejection_reason(["sa_rejection_reason"]) --> SP
    special_order_detail(["special_order_detail"]) --> SP
    stock_control_detail(["stock_control_detail"]) --> SP
    tax_detail(["tax_detail"]) --> SP
    tax_override_detail(["tax_override_detail"]) --> SP
    transaction_header(["transaction_header"]) --> SP
    transaction_line(["transaction_line"]) --> SP
    util_capture_base_state__sp(["util_capture_base_state_$sp"]) --> SP
    util_compare_results__sp(["util_compare_results_$sp"]) --> SP
    util_comparison_current_state(["util_comparison_current_state"]) --> SP
    util_comparison_key(["util_comparison_key"]) --> SP
    util_comparison_result(["util_comparison_result"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| authorization_detail |
| common_error_handling_$sp |
| customer |
| customer_detail |
| discount_detail |
| if_rejection_reason |
| interface_control |
| line_note |
| merchandise_detail |
| payroll_detail |
| post_void_detail |
| return_detail |
| sa_rejection_reason |
| special_order_detail |
| stock_control_detail |
| tax_detail |
| tax_override_detail |
| transaction_header |
| transaction_line |
| util_capture_base_state_$sp |
| util_compare_results_$sp |
| util_comparison_current_state |
| util_comparison_key |
| util_comparison_result |

## Stored Procedure Code

```sql
create proc [dbo].[util_compare_transactions_$sp] 


@comparison_id int = 2,
@dump_result tinyint = 0,
@capture_base_state tinyint = 0,
@from_posting_date datetime = '01/01/2002',
@to_posting_date datetime = null,
@from_store_no int = null,
@from_transaction_date datetime = null,
@to_store_no int = null,
@to_transaction_date datetime = null,
@interface_id tinyint = null,
@status_message nvarchar(255) = null OUTPUT ,
@extra_count int = 0 OUTPUT,
@missing_count int = 0 OUTPUT,
@different_count int = 0 OUTPUT,
@minor_difference_count int = 0 OUTPUT,
@process_id int = NULL OUTPUT,
@errmsg nvarchar(255) = null OUTPUT
AS

/*
NAME:	util_compare_transactions_$sp
DESCRIPTION: To capture the content of the transaction table entries posted within the time
	     interval or for the store/date passed in, and compare it to a base state saved 
	     earlier.

NOTE:  entries resulting from Transaction Add will show as differences since the
entry_date_time which forms part of their key will likely change each time the test-case is
run.

HISTORY:
Date     Author       Defect Desc
Mar09,06 Paul        DV-1328 Apply 68027 to SA5
Mar22,05 Maryam      DV-1202 Rename from_line_id to line_id.
Jan28,05 Paul        48293/DV-1203 correctly set @to_posting_date
Sep23,04 Paul        DV-1146 remove updated_by_user_name
Feb15,06 Vicci	       68027 Add the display-def-id to the stock-control-detail key
Nov17,03 Phu           15801 Populate sku_id, reason, imrd, style_reference_id, display_def_id
Mar19,03 Vicci		6808 add missing sa_rejection and if_rejection reasons
Mar11,03 Winnie		6554 store approval_message in comparison_text2
Jan28,03 Vicci		5791 Support store/date range and interface_id
Jan21,02 Vicci       1-ADFD5 Create interface comparison utility
Jan09,03 Vicci          5503 Add tax_detail

*/
DECLARE @from_timestamp			float,
	@to_timestamp			float,
	@transaction_key		numeric(12,0),
	@cursor_open			tinyint,
	@errno				int,
	@message_id		        int,	
	@object_name			nvarchar(255),
	@operation_name			nvarchar(100),
	@print_message			nvarchar(255),
	@process_no			int,
	@process_name		        nvarchar(100),
	@sequence_no			int 	

SELECT @process_name = 'util_compare_transactions_$sp',
       @process_no = 36,
       @message_id = 201068,
       @to_posting_date = convert(datetime, '12/31/' + convert(nvarchar,datepart(yy, getdate()))),
       @process_id = IsNull(@process_id, @@spid),
       @sequence_no = 0

SELECT @from_timestamp = DATEPART ( mm, @from_posting_date ) * 100000000000.0
		+ DATEPART ( dd, @from_posting_date )* 1000000000.0
		+ DATEPART ( hh, @from_posting_date ) * 10000000.0
		+ DATEPART ( mi, @from_posting_date ) * 100000.0
		+ DATEPART ( ss, @from_posting_date ) * 1000.0
		+ DATEPART ( ms, @from_posting_date ),
       @to_timestamp = DATEPART ( mm, @to_posting_date ) * 100000000000.0
		+ DATEPART ( dd, @to_posting_date )* 1000000000.0
		+ DATEPART ( hh, @to_posting_date ) * 10000000.0
		+ DATEPART ( mi, @to_posting_date ) * 100000.0
		+ DATEPART ( ss, @to_posting_date ) * 1000.0
		+ DATEPART ( ms, @to_posting_date )

DELETE util_comparison_result
 WHERE process_id = @process_id
   OR comparison_id = @comparison_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to clean util_comparison_result',
             @object_name = 'util_comparison_result',
             @operation_name = 'DELETE'      
      GOTO error
    END

DELETE util_comparison_current_state
 WHERE process_id = @process_id
    OR comparison_id = @comparison_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to clean util_comparison_current_state',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'DELETE'      
      GOTO error
    END

DELETE util_comparison_key
 WHERE process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to clean util_comparison_key',
             @object_name = 'util_comparison_key',
             @operation_name = 'DELETE' 
      GOTO error
    END

IF @interface_id IS NULL
BEGIN
INSERT util_comparison_key(process_id, 
			   transaction_key,
			   sequence_datetime,
			   comparison_key)
SELECT @process_id,
transaction_id,
       entry_date_time,
       convert(nvarchar, store_no) + ' _ ' + convert(nvarchar, register_no) + ' _ ' + 
	              convert(nvarchar, transaction_date) + ' _ ' + convert(nvarchar, date_reject_id) + ' _ ' + 
	              convert(nvarchar, transaction_no) + ' _ ' + transaction_series + ' _ ' 
  FROM transaction_header
 WHERE (last_modified_date_time >= @from_posting_date OR edit_timestamp >= @from_timestamp)
   AND (last_modified_date_time < @to_posting_date OR edit_timestamp < @to_timestamp)
   AND store_no >= IsNull(@from_store_no,store_no)
   AND store_no <= IsNull(@to_store_no,store_no)
   AND transaction_date >= IsNull(@from_transaction_date,transaction_date)
   AND transaction_date <= IsNull(@to_transaction_date,transaction_date)

--Note:  transaction_date used instead of entry_date_time so that transaction-add test-case
--       differences may be reported as minor.

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to build list of transaction keys',
             @object_name = 'util_comparison_key',
             @operation_name = 'INSERT'      
      GOTO error
    END
END
ELSE
BEGIN
INSERT util_comparison_key(process_id, 
			   transaction_key,
			   sequence_datetime,
			   comparison_key)
SELECT DISTINCT @process_id,
       h.transaction_id,
       h.entry_date_time,
       convert(nvarchar, h.store_no) + ' _ ' + convert(nvarchar, h.register_no) + ' _ ' + 
	              convert(nvarchar, h.transaction_date) + ' _ ' + convert(nvarchar, h.date_reject_id) + ' _ ' + 
	              convert(nvarchar, h.transaction_no) + ' _ ' + h.transaction_series + ' _ ' 
  FROM transaction_header h, interface_control i
 WHERE (h.last_modified_date_time >= @from_posting_date OR h.edit_timestamp >= @from_timestamp)
   AND (h.last_modified_date_time < @to_posting_date OR h.edit_timestamp < @to_timestamp)
   AND h.store_no >= IsNull(@from_store_no,h.store_no)
   AND h.store_no <= IsNull(@to_store_no,h.store_no)
   AND h.transaction_date >= IsNull(@from_transaction_date,h.transaction_date)
   AND h.transaction_date <= IsNull(@to_transaction_date,h.transaction_date)
   AND h.transaction_id = i.transaction_id
   AND (i.interface_id = @interface_id OR @interface_id IS NULL)

--Note:  transaction_date used instead of entry_date_time so that transaction-add test-case
--       differences may be reported as minor.

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to build list of transaction keys',
             @object_name = 'util_comparison_key',
             @operation_name = 'INSERT'      
      GOTO error
    END
END

DECLARE multiple_key_cursor CURSOR
 FOR
  SELECT u.transaction_key
    FROM util_comparison_key u
   WHERE u.process_id = @process_id
     AND u.comparison_key IN (SELECT m.comparison_key
     			        FROM util_comparison_key m
			       WHERE m.process_id = @process_id
			       GROUP BY m.comparison_key
			       HAVING COUNT(m.transaction_key) <> 1)
   ORDER BY u.comparison_key, u.sequence_datetime
SELECT @errno = @@error
IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to declare multiple_key_cursor CURSOR',
 	   @object_name = 'multiple_key_cursor',
	   @operation_name = 'DECLARE'
    GOTO error
  END
   
OPEN multiple_key_cursor
SELECT @errno = @@error
IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to open multiple_key_cursor CURSOR',
 	   @object_name = 'multiple_key_cursor',
	   @operation_name = 'OPEN'
    GOTO error
  END

SELECT @cursor_open = 1

FETCH multiple_key_cursor
 INTO @transaction_key

WHILE @@fetch_status = 0
BEGIN
  SELECT @sequence_no = @sequence_no + 1
  UPDATE util_comparison_key
     SET comparison_key = comparison_key + convert(nvarchar, @sequence_no)
   WHERE process_id = @process_id 
     AND transaction_key = @transaction_key

  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to add a sequence number to the comparison-key',
 	   @object_name = 'util_comparison_key',
	   @operation_name = 'UPDATE'
    GOTO error
  END
   
FETCH multiple_key_cursor
 INTO @transaction_key

END /* while not end of multiple_key_cursor */

CLOSE multiple_key_cursor
DEALLOCATE multiple_key_cursor
SELECT @cursor_open = 0

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'transaction_header', 'Header Data', 
       u.comparison_key, 
       convert(nvarchar, cashier_no) + ' _ ' + 
	 convert(nvarchar, transaction_category) + ' _ ' + convert(nvarchar, tender_total) + ' _ ' + 
	 convert(nvarchar, transaction_void_flag) + ' _ ' + convert(nvarchar, customer_info_exists) + ' _ ' + 
	 convert(nvarchar, exception_flag) + ' _ ' + convert(nvarchar, deposit_declaration_flag) + ' _ ' + 
	 convert(nvarchar, sa_rejection_flag) + ' _ ' + convert(nvarchar, if_rejection_flag) + ' _ ' + 
	 convert(nvarchar, closeout_flag) + ' _ ' + convert(nvarchar, media_count_flag) + ' _ ' + 
	 convert(nvarchar, customer_modified_flag) + ' _ ' + convert(nvarchar, tax_override_flag) + ' _ ' +
	 pos_tax_jurisdiction + ' _ ' + convert(nvarchar, employee_no),
       transaction_remark,
       convert(nvarchar,h.entry_date_time, 9)
  FROM util_comparison_key u, transaction_header h
 WHERE u.transaction_key = h.transaction_id
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of transaction_header',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END
 
INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'interface_control', 'Interface Control', 
       u.comparison_key + ' _ ' + convert(nvarchar, interface_id),
       convert(nvarchar, interface_status_flag),
       null,
       null  
  FROM util_comparison_key u, interface_control i
 WHERE u.transaction_key = i.transaction_id
   AND u.process_id = @process_id
   AND (i.interface_id = @interface_id or @interface_id IS NULL)
   
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of interface_control',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'transaction_line', 'Transaction Lines', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id),
       convert(nvarchar, line_sequence) + ' _ ' + convert(nvarchar, line_object_type) + ' _ ' + 
       convert(nvarchar, line_object) + ' _ ' + convert(nvarchar, line_action) + ' _ ' + 
       convert(nvarchar, gross_line_amount) + ' _ ' + convert(nvarchar, pos_discount_amount) + ' _ ' + 
       convert(nvarchar, db_cr_none) + ' _ ' + convert(nvarchar, attachment_qty) + ' _ ' +        
       convert(nvarchar, exception_flag) + ' _ ' + convert(nvarchar, interface_rejection_flag) + ' _ ' +        
       convert(nvarchar, line_void_flag) + ' _ ' + convert(nvarchar, voiding_reversal_flag) + ' _ ' +        
       convert(nvarchar, reference_type) + ' _ ' + convert(nvarchar, reference_no),
       null,
       null  
  FROM util_comparison_key u, transaction_line l
 WHERE u.transaction_key = l.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of transaction_line',
          @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'merchandise_detail', 'Merchandise Information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id),
       convert(nvarchar, merchandise_category) + ' _ ' + convert(nvarchar, upc_lookup_division) + ' _ ' + 
       convert(nvarchar, upc_no) + ' _ ' + convert(nvarchar, units) + ' _ ' +        
       convert(nvarchar, salesperson) + ' _ ' + convert(nvarchar, salesperson2) + ' _ ' + 
       convert(nvarchar, sku_id) + ' _ ' + convert(nvarchar, style_reference_id) + ' _ ' + 
       convert(nvarchar, class_code) + ' _ ' + convert(nvarchar, subclass_code) + ' _ ' +        
       convert(nvarchar, price_override) + ' _ ' + convert(nvarchar, pos_iplu_missing) + ' _ ' +        
       convert(nvarchar, upc_on_file_flag) + ' _ ' + convert(nvarchar, pos_deptclass) + ' _ ' +        
       convert(nvarchar, ticket_price) + ' _ ' + convert(nvarchar, sold_at_price) + ' _ ' +
       convert(nvarchar, scanned) + ' _ ' + pos_identifier + ' _ ' + 
       convert(nvarchar, pos_identifier_type) + ' _ ' + convert(nvarchar, plu_price) + ' _ ' +
       convert(nvarchar, originating_store_no),
       null,
       null  
  FROM util_comparison_key u, merchandise_detail m
 WHERE u.transaction_key = m.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of merchandise_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'discount_detail', 'Discount Information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar, applied_by_line_id),
       convert(nvarchar, pos_discount_level) + ' _ ' + convert(nvarchar, pos_discount_type) + ' _ ' + 
       convert(nvarchar, pos_discount_amount) + ' _ ' + convert(nvarchar, applied_flag) + ' _ ' + 
       convert(nvarchar, pos_discount_serial_no),
       null,
       null  
  FROM util_comparison_key u, discount_detail d
 WHERE u.transaction_key = d.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of discount_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'authorization_detail', 'Authorization Information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id),
       card_type + ' _ ' + convert(nvarchar, authorization_no) + ' _ ' + 
       convert(nvarchar, expiry_date) + ' _ ' + convert(nvarchar, swipe_indicator) + ' _ ' + 
       license_no + ' _ ' + pos_state_code + ' _ ' + 
       convert(nvarchar, other_id_type) + ' _ ' + other_id + ' _ ' +
       convert(nvarchar, deferred_billing_date) + ' _ ' + convert(nvarchar, deferred_billing_plan) + ' _ ' + 
       convert(nvarchar, customer_signature_obtained),
       approval_message,
       null   
  FROM util_comparison_key u, authorization_detail a
 WHERE u.transaction_key = a.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of authorization_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'customer', 'Customer Information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar, customer_role),
       title + ' _ ' + first_name + ' _ ' + 
       last_name + ' _ ' + address_1 + ' _ ' + 
       address_2 + ' _ ' + city + ' _ ' + 
       county + ' _ ' + state + ' _ ' + 
       country + ' _ ' + post_code + ' _ ' + 
       telephone_no1 + ' _ ' + telephone_no2 + ' _ ' + 
       convert(nvarchar, customer_no) + ' _ ' + convert(nvarchar, more_info_flag) + ' _ ' + 
       pos_tax_jurisdiction_code + ' _ ' + fax + ' _ ' + email_address,
       null,
       null  
  FROM util_comparison_key u, customer c
 WHERE u.transaction_key = c.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of customer',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'customer_detail', 'Extra Customer Information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar, customer_role) + ' _ ' + convert(nvarchar, customer_info_type),
       customer_info,
       null,
       null  
  FROM util_comparison_key u, customer_detail c
 WHERE u.transaction_key = c.transaction_id
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of customer_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'line_note', 'Line Notes', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar, note_type),
       line_note,
       null,
       null  
  FROM util_comparison_key u, line_note c
 WHERE u.transaction_key = c.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of line_note',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'special_order_detail', 'Special Order information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id),
       convert(nvarchar, units) + ' _ ' + convert(nvarchar, salesperson) + ' _ ' + 
       merchandise_description + ' _ ' + expecting_delivery_on + ' _ ' + 
       color_description + ' _ ' + size_description + ' _ ' + 
       width_description + ' _ ' + vendor_name + ' _ ' + 
       vendor_style_description + ' _ ' + spo_class_description + ' _ ' + 
 vendor_no,
   null,
       null  
  FROM util_comparison_key u, special_order_detail o
 WHERE u.transaction_key = o.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of special_order_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'stock_control_detail', 'Stock Control information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar,display_def_id),
       convert(nvarchar, upc_no) + ' _ ' + convert(nvarchar, merchandise_key) + ' _ ' + 
       convert(nvarchar, initiated_by_host) + ' _ ' + convert(nvarchar, units) + ' _ ' + 
       convert(nvarchar, other_store_no) + ' _ ' + convert(nvarchar, location_no) + ' _ ' + 
       vendor_no + ' _ ' + convert(nvarchar, count_date) + ' _ ' + 
       pos_identifier + ' _ ' + convert(nvarchar, pos_identifier_type) + ' _ ' + 
       convert(nvarchar, pos_deptclass) + ' _ ' + convert(nvarchar, upc_lookup_division) + ' _ ' + 
       convert(nvarchar, originating_store_no) + ' _ ' +
       convert(nvarchar, display_def_id) + ' _ ' +
       convert(nvarchar, sku_id) + ' _ ' + reason + ' _ ' + imrd + ' _ ' +
       convert(nvarchar, style_reference_id),
       null,
       null  
  FROM util_comparison_key u, stock_control_detail s
 WHERE u.transaction_key = s.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of stock_control_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'tax_override_detail', 'Tax Override information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar, tax_level),
       convert(nvarchar, tax_category) + ' _ ' + convert(nvarchar, taxable) + ' _ ' +
       exception_tax_jurisdiction + ' _ ' + tax_exempt_no,
       null,
       null  
  FROM util_comparison_key u, tax_override_detail t
 WHERE u.transaction_key = t.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of tax_override_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'tax_detail', 'Tax Detail information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar, tax_level),
       tax_jurisdiction + ' _ ' + convert(nvarchar, tax_category) + ' _ ' + convert(nvarchar, tax_rate_code) + ' _ ' +
       convert(nvarchar, taxable_amount) + ' _ ' + convert(nvarchar, tax_amount) + ' _ ' + 
      convert(nvarchar, combined_rate) + ' _ ' + convert(nvarchar, nontaxable_amount) + ' _ ' + 
       convert(nvarchar, tax_amount_expected) + ' _ ' + convert(nvarchar, tax_on_tax_level) + ' _ ' + 
       convert(nvarchar, tax_on_combined_rate) + ' _ ' + convert(nvarchar, line_object_type) + ' _ ' + 
       convert(nvarchar, tax_strip_flag) + ' _ ' + convert(nvarchar, gl_effect),
       null,
       null  
  FROM util_comparison_key u, tax_detail t
 WHERE u.transaction_key = t.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of tax_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'return_detail', 'Return information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id),
       return_reason_message + ' _ ' + convert(nvarchar, return_reason_code) + ' _ ' + 
       convert(nvarchar, mdse_disposition_code) + ' _ ' + convert(nvarchar, via_warehouse_flag) + ' _ ' + 
       convert(nvarchar, original_salesperson) + ' _ ' + convert(nvarchar, original_salesperson2) + ' _ ' + 
       convert(nvarchar, return_from_store) + ' _ ' + convert(nvarchar, return_from_reg) + ' _ ' + 
       convert(nvarchar, return_from_date) + ' _ ' + convert(nvarchar, return_from_transno),
       null,
       null  
  FROM util_comparison_key u, return_detail r
 WHERE u.transaction_key = r.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of return_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'post_void_detail', 'Post Void information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id),
       convert(nvarchar, post_voided_register) + ' _ ' + convert(nvarchar, post_voided_trans_no) + ' _ ' + 
       convert(nvarchar, post_void_successful) + ' _ ' + convert(nvarchar, post_void_reason_code),
       null,
       null  
  FROM util_comparison_key u, post_void_detail v
 WHERE u.transaction_key = v.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of post_void_detail',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'payroll_detail', 'Payroll information', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id),
       convert(nvarchar, employee_no) + ' _ ' + convert(nvarchar, payroll_date) + ' _ ' + 
       convert(nvarchar, employee_payroll_id) + ' _ ' + convert(nvarchar, employee_type) + ' _ ' + 
       convert(nvarchar, payroll_entry_type),
       null,
       null  
  FROM util_comparison_key u, payroll_detail p
 WHERE u.transaction_key = p.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of payroll_detail',
             @object_name = 'util_comparison_current_state',
           @operation_name = 'INSERT'      
      GOTO error
    END
    
INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'sa_rejection_reason', 'S/A Rejection reason', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar, violated_sareject_rule),
       convert(nvarchar, line_object) + ' _ ' + convert(nvarchar, line_action) + ' _ ' + 
       convert(nvarchar, transaction_category),
       null,
       null  
  FROM util_comparison_key u, sa_rejection_reason r
 WHERE u.transaction_key = r.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of sa_rejection_reason',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END

INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT @process_id, @comparison_id, 'if_rejection_reason', 'I/F Rejection reason', 
       u.comparison_key + ' _ ' + convert(nvarchar, line_id) + ' _ ' + convert(nvarchar, if_reject_reason),
       convert(nvarchar, deferred) + ' _ ' + 
       memo1 + ' _ ' + memo2 + ' _ ' + memo3 + ' _ ' + 
       convert(nvarchar, lookup_key1),
       null,
       null  
  FROM util_comparison_key u, if_rejection_reason r
 WHERE u.transaction_key = r.transaction_id
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_rejection_reason',
             @object_name = 'util_comparison_current_state',
             @operation_name = 'INSERT'      
      GOTO error
    END


IF @capture_base_state <> 1
BEGIN
 EXEC util_compare_results_$sp @comparison_id, @status_message OUTPUT, @extra_count OUTPUT,
			      @missing_count OUTPUT, @different_count OUTPUT, 
			      @minor_difference_count OUTPUT, @process_id, @errmsg OUTPUT
 SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      IF @errmsg IS NULL /* then */
        SELECT @errmsg = 'Failed to obtain comparison of current results and base state'
      SELECT @object_name = 'util_compare_results_$sp',
             @operation_name = 'EXECUTE'
      GOTO error
    END
END
ELSE
BEGIN
 EXEC util_capture_base_state_$sp @comparison_id, @process_id, @errmsg OUTPUT
 SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      IF @errmsg IS NULL /* then */
        SELECT @errmsg = 'Failed to save current results as base state'
      SELECT @object_name = 'util_capture_base_state_$sp',
             @operation_name = 'EXECUTE'
      GOTO error
    END
END

IF @capture_base_state <> 1
BEGIN
 SELECT @print_message = ':LOG Results for process_id ' + convert(nvarchar,@process_id) + ', comparison_id ' +
 convert(nvarchar,@comparison_id) + ':  ' + @status_message + ' 
Extra entries = ' + convert(nvarchar,@extra_count) + '
Missing entries = ' + convert(nvarchar,@missing_count) + '
Different entries = ' + convert(nvarchar,@different_count) + '
Minor differences = ' + convert(nvarchar,@minor_difference_count)

 PRINT @print_message

 IF @dump_result = 1
  SELECT util_comparison_result.process_id, util_comparison_result.comparison_id, util_comparison_result.comparison_time, util_comparison_result.status, util_comparison_result.table_name, util_comparison_result.validation_area, util_comparison_result.comparison_key, util_comparison_result.comparison_text1, util_comparison_result.comparison_text2, util_comparison_result.comparison_text_minor, util_comparison_result.new_comparison_text1, util_comparison_result.new_comparison_text2, util_comparison_result.new_comparison_text_minor 
    FROM util_comparison_result
   WHERE process_id = @process_id
     AND comparison_id = @comparison_id
END

DELETE util_comparison_key
 WHERE process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to do final cleanup of util_comparison_key',
             @object_name = 'util_comparison_key',
             @operation_name = 'DELETE'      
      GOTO error
    END

RETURN

error:
	IF @cursor_open = 1
	  BEGIN
	   CLOSE multiple_key_cursor
	   DEALLOCATE multiple_key_cursor
	  END

	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, 1
	RETURN
```

