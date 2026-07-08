# dbo.util_compare_interfaces_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_compare_interfaces_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    if_authorization_detail(["if_authorization_detail"]) --> SP
    if_customer(["if_customer"]) --> SP
    if_customer_detail(["if_customer_detail"]) --> SP
    if_discount_detail(["if_discount_detail"]) --> SP
    if_interface_control(["if_interface_control"]) --> SP
    if_line_note(["if_line_note"]) --> SP
    if_merchandise_detail(["if_merchandise_detail"]) --> SP
    if_payroll_detail(["if_payroll_detail"]) --> SP
    if_post_void_detail(["if_post_void_detail"]) --> SP
    if_return_detail(["if_return_detail"]) --> SP
    if_special_order_detail(["if_special_order_detail"]) --> SP
    if_stock_control_detail(["if_stock_control_detail"]) --> SP
    if_tax_detail(["if_tax_detail"]) --> SP
    if_tax_override_detail(["if_tax_override_detail"]) --> SP
    if_transaction_header(["if_transaction_header"]) --> SP
    if_transaction_line(["if_transaction_line"]) --> SP
    util_capture_base_state__sp(["util_capture_base_state_$sp"]) --> SP
    util_compare_results__sp(["util_compare_results_$sp"]) --> SP
    util_comparison_current_state(["util_comparison_current_state"]) --> SP
    util_comparison_key(["util_comparison_key"]) --> SP
    util_comparison_result(["util_comparison_result"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |
| if_authorization_detail |
| if_customer |
| if_customer_detail |
| if_discount_detail |
| if_interface_control |
| if_line_note |
| if_merchandise_detail |
| if_payroll_detail |
| if_post_void_detail |
| if_return_detail |
| if_special_order_detail |
| if_stock_control_detail |
| if_tax_detail |
| if_tax_override_detail |
| if_transaction_header |
| if_transaction_line |
| util_capture_base_state_$sp |
| util_compare_results_$sp |
| util_comparison_current_state |
| util_comparison_key |
| util_comparison_result |

## Stored Procedure Code

```sql
create proc dbo.util_compare_interfaces_$sp 

@comparison_id int = 1,
@dump_result tinyint = 0,
@capture_base_state tinyint = 0,
@from_interface_posting_date datetime = '01/01/2002',
@to_interface_posting_date datetime = null,
@from_store_no int = null,
@from_transaction_date datetime = null,
@to_store_no int = null,
@to_transaction_date datetime = null,
@interface_id tinyint = null,
@status_message varchar(255) = null OUTPUT ,
@extra_count int = 0 OUTPUT,
@missing_count int = 0 OUTPUT,
@different_count int = 0 OUTPUT,
@minor_difference_count int = 0 OUTPUT,
@process_id int = NULL OUTPUT,
@errmsg varchar(255) = null OUTPUT
AS

/*
NAME:	util_compare_interfaces_$sp
DESCRIPTION: To capture the content of the interface table entries posted within the time
	     interval or for the store/date passed in, and compare it to a base state saved 
	     earlier.

NOTE:  entries resulting from Transaction Add will show as differences since the
entry_date_time which forms part of their key will likely change each time the test-case is
run.

HISTORY:
Date     Author       Defect Desc
Mar02,06 David       DV-1328 Add display_def_id to key of stock_control_detail.
Mar22,05 Maryam      DV-1202 Rename from_line_id to line_id.
Jan28,05 Paul        48293/DV-1203 correctly set @to_interface_posting_date
Sep23,04 Paul        DV-1146 remove updated_by_user_name
Nov17,03 Phu           15801 Populate sku_id, reason, imrd, style_reference_id, display_def_id
Mar14,03 Vicci		6554 correct interface_id recognition and move approval_message to text2
Jan28,03 Vicci		5791 support from/to store and date and specification of interface_id
Jan21,02 Vicci       1-ADFD5 Create interface comparison utility
Jan09,03 Vicci          5503 Add if_tax_detail

*/

DECLARE
	@transaction_key		numeric(12,0),
	@cursor_open			tinyint,
	@errno				int,
	@message_id		        int,	
	@object_name			varchar(255),
	@operation_name			varchar(100),
	@print_message			varchar(255),
	@process_no			int,
	@process_name		        varchar(100),
	@rows				int,
	@sequence_no			int 	

SELECT @process_name = 'util_compare_interfaces_$sp',
       @process_no = 36,
       @message_id = 201068,
       @to_interface_posting_date = convert(datetime, '12/31/' + convert(varchar,datepart(yy, getdate()))),
       @process_id = IsNull(@process_id, @@spid),
       @sequence_no = 0

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

INSERT util_comparison_key(process_id, 
			   transaction_key,
			   sequence_datetime)
SELECT @process_id,
       i.if_entry_no,
       min(i.interface_posting_date)
  FROM if_interface_control i
 WHERE i.interface_posting_date >= @from_interface_posting_date
   AND i.interface_posting_date < @to_interface_posting_date
   AND (i.interface_id = @interface_id or @interface_id is null)
 GROUP BY if_entry_no

SELECT @errno = @@error, @rows = @@rowcount
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to build list of transaction keys',
             @object_name = 'util_comparison_key',
             @operation_name = 'INSERT'      
      GOTO error
    END

--Note:  transaction_date used instead of entry_date_time so that transaction-add test-case
--       differences may be reported as minor.
UPDATE util_comparison_key
   SET comparison_key = CONVERT(varchar, h.store_no) + ' _ ' + CONVERT(varchar, h.register_no) + ' _ ' + 
	  CONVERT(varchar, h.transaction_date) + ' _ ' + CONVERT(varchar, h.date_reject_id) + ' _ ' + 
	              CONVERT(varchar, h.transaction_no) + ' _ ' + h.transaction_series + ' _ ' 
  FROM util_comparison_key u,
       if_transaction_header h
 WHERE u.process_id = @process_id
   AND u.transaction_key = h.if_entry_no
   AND store_no >= IsNull(@from_store_no,store_no)
   AND store_no <= IsNull(@to_store_no,store_no)
   AND transaction_date >= IsNull(@from_transaction_date,transaction_date)
   AND transaction_date <= IsNull(@to_transaction_date,transaction_date)


SELECT @errno = @@error, @rows = @@rowcount
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to build list of comparison keys',
             @object_name = 'util_comparison_key',
             @operation_name = 'UPDATE'      
      GOTO error
    END

DELETE util_comparison_key
 WHERE process_id = @process_id
   AND comparison_key IS NULL --
 SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to restrict list of comparison keys to selected store/date',
             @object_name = 'util_comparison_key',
             @operation_name = 'DELETE'      
      GOTO error
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
     SET comparison_key = comparison_key + CONVERT(varchar, @sequence_no)
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
SELECT @process_id, @comparison_id, 'if_transaction_header', 'Header Data', 
       u.comparison_key, 
       CONVERT(varchar, cashier_no) + ' _ ' + 
	 CONVERT(varchar, transaction_category) + ' _ ' + CONVERT(varchar, tender_total) + ' _ ' + 
	 CONVERT(varchar, transaction_void_flag) + ' _ ' + CONVERT(varchar, customer_info_exists) + ' _ ' + 
	 CONVERT(varchar, exception_flag) + ' _ ' + CONVERT(varchar, deposit_declaration_flag) + ' _ ' + 
	 CONVERT(varchar, closeout_flag) + ' _ ' + CONVERT(varchar, media_count_flag) + ' _ ' + 
	 CONVERT(varchar, customer_modified_flag) + ' _ ' + CONVERT(varchar, tax_override_flag) + ' _ ' + 
	 pos_tax_jurisdiction + ' _ ' + CONVERT(varchar, employee_no) + ' _ ' + 
	 CONVERT(varchar, source_process_no) + ' _ ' + CONVERT(varchar,sign(transaction_id)),
       transaction_remark,
       CONVERT(varchar,h.entry_date_time, 9)
  FROM util_comparison_key u, if_transaction_header h
 WHERE u.transaction_key = h.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_transaction_header',
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
SELECT @process_id, @comparison_id, 'if_interface_control', 'Interface Control', 
       u.comparison_key + ' _ ' + CONVERT(varchar, interface_id),
       CONVERT(varchar, interface_control_flag) + ' _ ' + CONVERT(varchar, effective_date),
       null,
       null  
  FROM util_comparison_key u, if_interface_control i
 WHERE u.transaction_key = i.if_entry_no
   AND u.process_id = @process_id
   AND (i.interface_id = @interface_id or @interface_id is null)

SELECT @errno = @@error, @rows = @@rowcount
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_interface_control',
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
SELECT @process_id, @comparison_id, 'if_transaction_line', 'Transaction Lines', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id),
       CONVERT(varchar, line_sequence) + ' _ ' + CONVERT(varchar, line_object_type) + ' _ ' + 
       CONVERT(varchar, line_object) + ' _ ' + CONVERT(varchar, line_action) + ' _ ' + 
       CONVERT(varchar, gross_line_amount) + ' _ ' + CONVERT(varchar, pos_discount_amount) + ' _ ' + 
       CONVERT(varchar, db_cr_none) + ' _ ' + CONVERT(varchar, attachment_qty) + ' _ ' +        
       CONVERT(varchar, exception_flag) + ' _ ' + CONVERT(varchar, interface_rejection_flag) + ' _ ' +        
       CONVERT(varchar, line_void_flag) + ' _ ' + CONVERT(varchar, voiding_reversal_flag) + ' _ ' +        
       CONVERT(varchar, reference_type) + ' _ ' + CONVERT(varchar, reference_no),
       null,
       null  
  FROM util_comparison_key u, if_transaction_line l
 WHERE u.transaction_key = l.if_entry_no
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_transaction_line',
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
SELECT @process_id, @comparison_id, 'if_merchandise_detail', 'Merchandise Information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id),
       CONVERT(varchar, merchandise_category) + ' _ ' + CONVERT(varchar, upc_lookup_division) + ' _ ' + 
       CONVERT(varchar, upc_no) + ' _ ' + CONVERT(varchar, units) + ' _ ' +        
       CONVERT(varchar, salesperson) + ' _ ' + CONVERT(varchar, salesperson2) + ' _ ' + 
       CONVERT(varchar, sku_id) + ' _ ' + CONVERT(varchar, style_reference_id) + ' _ ' + 
       CONVERT(varchar, class_code) + ' _ ' + CONVERT(varchar, subclass_code) + ' _ ' +        
       CONVERT(varchar, price_override) + ' _ ' + CONVERT(varchar, pos_iplu_missing) + ' _ ' +     
       CONVERT(varchar, upc_on_file_flag) + ' _ ' + CONVERT(varchar, pos_deptclass) + ' _ ' +        
       CONVERT(varchar, ticket_price) + ' _ ' + CONVERT(varchar, sold_at_price) + ' _ ' +
       CONVERT(varchar, scanned) + ' _ ' + pos_identifier + ' _ ' + 
       CONVERT(varchar, pos_identifier_type) + ' _ ' + CONVERT(varchar, plu_price) + ' _ ' +
       CONVERT(varchar, originating_store_no),
       null,
       null  
  FROM util_comparison_key u, if_merchandise_detail m
 WHERE u.transaction_key = m.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_merchandise_detail',
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
SELECT @process_id, @comparison_id, 'if_discount_detail', 'Discount Information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id) + ' _ ' + CONVERT(varchar, applied_by_line_id),
       CONVERT(varchar, pos_discount_level) + ' _ ' + CONVERT(varchar, pos_discount_type) + ' _ ' + 
       CONVERT(varchar, pos_discount_amount) + ' _ ' + CONVERT(varchar, applied_flag) + ' _ ' + 
       CONVERT(varchar, pos_discount_serial_no),
       null,
       null  
  FROM util_comparison_key u, if_discount_detail d
 WHERE u.transaction_key = d.if_entry_no
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_discount_detail',
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
SELECT @process_id, @comparison_id, 'if_authorization_detail', 'Authorization Information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id),
       card_type + ' _ ' + CONVERT(varchar, authorization_no) + ' _ ' + 
       CONVERT(varchar, expiry_date) + ' _ ' + CONVERT(varchar, swipe_indicator) + ' _ ' + 
        license_no + ' _ ' + pos_state_code + ' _ ' + 
       CONVERT(varchar, other_id_type) + ' _ ' + other_id + ' _ ' +
       CONVERT(varchar, deferred_billing_date) + ' _ ' + CONVERT(varchar, deferred_billing_plan) + ' _ ' + 
       CONVERT(varchar, customer_signature_obtained),
       approval_message,
       null   
  FROM util_comparison_key u, if_authorization_detail a
 WHERE u.transaction_key = a.if_entry_no
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_authorization_detail',
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
SELECT @process_id, @comparison_id, 'if_customer', 'Customer Information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id) + ' _ ' + CONVERT(varchar, customer_role),
       title + ' _ ' + first_name + ' _ ' + 
       last_name + ' _ ' + address_1 + ' _ ' + 
       address_2 + ' _ ' + city + ' _ ' + 
       county + ' _ ' + state + ' _ ' + 
       country + ' _ ' + post_code + ' _ ' + 
       telephone_no1 + ' _ ' + telephone_no2 + ' _ ' + 
       CONVERT(varchar, customer_no) + ' _ ' + CONVERT(varchar, more_info_flag) + ' _ ' + 
       pos_tax_jurisdiction_code + ' _ ' + fax + ' _ ' + email_address,
       null,
       null  
  FROM util_comparison_key u, if_customer c
 WHERE u.transaction_key = c.if_entry_no
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_customer',
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
SELECT @process_id, @comparison_id, 'if_customer_detail', 'Extra Customer Information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id) + ' _ ' + CONVERT(varchar, customer_role) + ' _ ' + CONVERT(varchar, customer_info_type),
       customer_info,
       null,
       null  
  FROM util_comparison_key u, if_customer_detail c
 WHERE u.transaction_key = c.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_customer_detail',
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
SELECT @process_id, @comparison_id, 'if_line_note', 'Line Notes', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id) + ' _ ' + CONVERT(varchar, note_type),
       line_note,
       null,
       null  
  FROM util_comparison_key u, if_line_note c
 WHERE u.transaction_key = c.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_line_note',
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
SELECT @process_id, @comparison_id, 'if_special_order_detail', 'Special Order information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id),
       CONVERT(varchar, units) + ' _ ' + CONVERT(varchar, salesperson) + ' _ ' + 
       merchandise_description + ' _ ' + expecting_delivery_on + ' _ ' + 
       color_description + ' _ ' + size_description + ' _ ' + 
       width_description + ' _ ' + vendor_name + ' _ ' + 
       vendor_style_description + ' _ ' + spo_class_description + ' _ ' + 
       vendor_no,
       null,
       null   
  FROM util_comparison_key u, if_special_order_detail o
 WHERE u.transaction_key = o.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_special_order_detail',
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
SELECT @process_id, @comparison_id, 'if_stock_control_detail', 'Stock Control information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id) + ' _ ' + CONVERT(varchar, display_def_id),
       CONVERT(varchar, upc_no) + ' _ ' + CONVERT(varchar, merchandise_key) + ' _ ' + 
       CONVERT(varchar, initiated_by_host) + ' _ ' + CONVERT(varchar, units) + ' _ ' + 
       CONVERT(varchar, other_store_no) + ' _ ' + CONVERT(varchar, location_no) + ' _ ' + 
       vendor_no + ' _ ' + CONVERT(varchar, count_date) + ' _ ' + 
       pos_identifier + ' _ ' + CONVERT(varchar, pos_identifier_type) + ' _ ' + 
       CONVERT(varchar, pos_deptclass) + ' _ ' + CONVERT(varchar, upc_lookup_division) + ' _ ' + 
       CONVERT(varchar, originating_store_no) + ' _ ' +
       CONVERT(varchar, display_def_id) + ' _ ' +
       CONVERT(varchar, sku_id) + ' _ ' + reason + ' _ ' + imrd + ' _ ' +
       CONVERT(varchar, style_reference_id),
       null,
       null  
  FROM util_comparison_key u, if_stock_control_detail s
 WHERE u.transaction_key = s.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_stock_control_detail',
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
SELECT @process_id, @comparison_id, 'if_tax_override_detail', 'Tax Override information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id) + ' _ ' + CONVERT(varchar, tax_level),
       CONVERT(varchar, tax_category) + ' _ ' + CONVERT(varchar, taxable) + ' _ ' +
       exception_tax_jurisdiction + ' _ ' + tax_exempt_no,
       null,
       null  
  FROM util_comparison_key u, if_tax_override_detail t
 WHERE u.transaction_key = t.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_tax_override_detail',
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
SELECT @process_id, @comparison_id, 'if_tax_detail', 'Tax Detail information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id) + ' _ ' + CONVERT(varchar, tax_level),
       tax_jurisdiction + ' _ ' + CONVERT(varchar, tax_category) + ' _ ' + CONVERT(varchar, tax_rate_code) + ' _ ' +
       CONVERT(varchar, taxable_amount) + ' _ ' + CONVERT(varchar, tax_amount) + ' _ ' + 
       CONVERT(varchar, combined_rate) + ' _ ' + CONVERT(varchar, nontaxable_amount) + ' _ ' + 
       CONVERT(varchar, tax_amount_expected) + ' _ ' + CONVERT(varchar, tax_on_tax_level) + ' _ ' + 
       CONVERT(varchar, tax_on_combined_rate) + ' _ ' + CONVERT(varchar, line_object_type) + ' _ ' + 
       CONVERT(varchar, tax_strip_flag) + ' _ ' + CONVERT(varchar, gl_effect),
       null,
       null  
  FROM util_comparison_key u, if_tax_detail t
 WHERE u.transaction_key = t.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_tax_detail',
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
SELECT @process_id, @comparison_id, 'if_return_detail', 'Return information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id),
       return_reason_message + ' _ ' + CONVERT(varchar, return_reason_code) + ' _ ' + 
       CONVERT(varchar, mdse_disposition_code) + ' _ ' + CONVERT(varchar, via_warehouse_flag) + ' _ ' + 
       CONVERT(varchar, original_salesperson) + ' _ ' + CONVERT(varchar, original_salesperson2) + ' _ ' + 
       CONVERT(varchar, return_from_store) + ' _ ' + CONVERT(varchar, return_from_reg) + ' _ ' + 
       CONVERT(varchar, return_from_date) + ' _ ' + CONVERT(varchar, return_from_transno),
       null,
       null  
  FROM util_comparison_key u, if_return_detail r
 WHERE u.transaction_key = r.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_return_detail',
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
SELECT @process_id, @comparison_id, 'if_post_void_detail', 'Post Void information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id),
       CONVERT(varchar, post_voided_register) + ' _ ' + CONVERT(varchar, post_voided_trans_no) + ' _ ' + 
       CONVERT(varchar, post_void_successful) + ' _ ' + CONVERT(varchar, post_void_reason_code),
       null,
       null  
  FROM util_comparison_key u, if_post_void_detail v
 WHERE u.transaction_key = v.if_entry_no
   AND u.process_id = @process_id

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_post_void_detail',
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
SELECT @process_id, @comparison_id, 'if_payroll_detail', 'Payroll information', 
       u.comparison_key + ' _ ' + CONVERT(varchar, line_id),
       CONVERT(varchar, employee_no) + ' _ ' + CONVERT(varchar, payroll_date) + ' _ ' + 
       CONVERT(varchar, employee_payroll_id) + ' _ ' + CONVERT(varchar, employee_type) + ' _ ' + 
       CONVERT(varchar, payroll_entry_type),
       null,
       null  
  FROM util_comparison_key u, if_payroll_detail p
 WHERE u.transaction_key = p.if_entry_no
   AND u.process_id = @process_id
SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_payroll_detail',
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
 SELECT @print_message = ':LOG Results for process_id ' + CONVERT(varchar,@process_id) + ', comparison_id ' +
 CONVERT(varchar,@comparison_id) + ':  ' + @status_message + ' 
Extra entries = ' + CONVERT(varchar,@extra_count) + '
Missing entries = ' + CONVERT(varchar,@missing_count) + '
Different entries = ' + CONVERT(varchar,@different_count) + '
Minor differences = ' + CONVERT(varchar,@minor_difference_count)

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

