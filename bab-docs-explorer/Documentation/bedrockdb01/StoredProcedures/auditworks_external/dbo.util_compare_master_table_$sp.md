# dbo.util_compare_master_table_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_compare_master_table_$sp"]
    card_type(["card_type"]) --> SP
    code_description(["code_description"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    cust_liab_active_validation(["cust_liab_active_validation"]) --> SP
    cust_liability_reference_type(["cust_liability_reference_type"]) --> SP
    cust_liability_type(["cust_liability_type"]) --> SP
    department_rollout_lookup(["department_rollout_lookup"]) --> SP
    geninfo_lookup(["geninfo_lookup"]) --> SP
    gl_account_segment_lookup(["gl_account_segment_lookup"]) --> SP
    if_rejection_reassignment(["if_rejection_reassignment"]) --> SP
    interface_applicability(["interface_applicability"]) --> SP
    line_object(["line_object"]) --> SP
    line_object_action_association(["line_object_action_association"]) --> SP
    line_object_action_attachment(["line_object_action_attachment"]) --> SP
    line_object_action_lookup(["line_object_action_lookup"]) --> SP
    line_object_lookup(["line_object_lookup"]) --> SP
    media_parameter_object(["media_parameter_object"]) --> SP
    reference_type_validation(["reference_type_validation"]) --> SP
    restricted_field(["restricted_field"]) --> SP
    stock_control_display_def(["stock_control_display_def"]) --> SP
    tax_default(["tax_default"]) --> SP
    tax_level(["tax_level"]) --> SP
    util_capture_base_state__sp(["util_capture_base_state_$sp"]) --> SP
    util_compare_results__sp(["util_compare_results_$sp"]) --> SP
    util_comparison_current_state(["util_comparison_current_state"]) --> SP
    util_comparison_result(["util_comparison_result"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| card_type |
| code_description |
| common_error_handling_$sp |
| cust_liab_active_validation |
| cust_liability_reference_type |
| cust_liability_type |
| department_rollout_lookup |
| geninfo_lookup |
| gl_account_segment_lookup |
| if_rejection_reassignment |
| interface_applicability |
| line_object |
| line_object_action_association |
| line_object_action_attachment |
| line_object_action_lookup |
| line_object_lookup |
| media_parameter_object |
| reference_type_validation |
| restricted_field |
| stock_control_display_def |
| tax_default |
| tax_level |
| util_capture_base_state_$sp |
| util_compare_results_$sp |
| util_comparison_current_state |
| util_comparison_result |

## Stored Procedure Code

```sql
create proc [dbo].[util_compare_master_table_$sp] 
@comparison_id int = 1,
@dump_result tinyint = 0,
@capture_base_state tinyint = 0,
@status_message nvarchar(255) = null OUTPUT ,
@extra_count int = 0 OUTPUT,
@missing_count int = 0 OUTPUT,
@different_count int = 0 OUTPUT,
@minor_difference_count int = 0 OUTPUT,
@process_id int = NULL OUTPUT,
@errmsg nvarchar(255) = null OUTPUT
AS

/*
NAME:	util_compare_master_table_$sp
DESCRIPTION: To capture the content of master tables that are auto-configured, and compare it
	     to a base state saved earlier.

HISTORY:
Date     Author       Defect# Desc
Feb21,06 David        DV-1328 Author 
*/

DECLARE 
	@errno				int,
	@message_id		        int,	
	@object_name			nvarchar(255),
	@operation_name			nvarchar(100),
	@print_message			nvarchar(255),
	@process_no			int,
	@process_name		        nvarchar(100),
	@sequence_no			int 	

SET NOCOUNT ON

SELECT @process_name = 'util_compare_master_table_$sp',
       @process_no = 36,
       @message_id = 201068,
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


INSERT INTO util_comparison_current_state( 
  		process_id, comparison_id, table_name, validation_area, 
  		comparison_key, 
  		comparison_text1, 
  		comparison_text2,
  		comparison_text_minor)
SELECT  @process_id, @comparison_id, 'line_object', 'Line Object', 
        convert(nvarchar, line_object),
        convert(nvarchar, line_object_type) 
        + ' _ ' + convert(nvarchar, line_object_description) 
        + ' _ ' + convert(nvarchar, default_tax_rate_code) 
        + ' _ ' + convert(nvarchar, object_export_code) 
        + ' _ ' + convert(nvarchar, tax_item_group_id) 
        + ' _ ' + convert(nvarchar, proration_method)
        + ' _ ' + convert(nvarchar, lookup_pos_code),
        convert(nvarchar, pos_description_token_list)
        + ' _ ' + convert(nvarchar, disregard_pos_descr_change)
        + ' _ ' + convert(nvarchar, lookup_partial_pos_code)
        + ' _ ' + convert(nvarchar, active_flag)
        + ' _ ' + convert(nvarchar, auto_config_verified),
	NULL --
  FROM line_object

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of line_object',
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
SELECT  @process_id, @comparison_id, 'line_object_action_association', 'Line Object Action Association', 
        convert(nvarchar, transaction_category) 
        + ' _ ' + convert(nvarchar, line_object) 
        + ' _ ' + convert(nvarchar, line_action),
        convert(nvarchar, line_object_type) 
        + ' _ ' + convert(nvarchar, db_cr_none) 
        + ' _ ' + convert(nvarchar, gl_account_segment1)
        + ' _ ' + convert(nvarchar, gl_account_segment2)
        + ' _ ' + convert(nvarchar, gl_account_segment3)
        + ' _ ' + convert(nvarchar, gl_account_segment4)
        + ' _ ' + convert(nvarchar, gl_account_segment5)
 + ' _ ' + convert(nvarchar, gl_account_segment6)
        + ' _ ' + convert(nvarchar, gl_account_segment7)
        + ' _ ' + convert(nvarchar, gl_account_segment8)
        + ' _ ' + convert(nvarchar, lookup_segment1)
        + ' _ ' + convert(nvarchar, lookup_segment2)
        + ' _ ' + convert(nvarchar, lookup_segment3)
        + ' _ ' + convert(nvarchar, lookup_segment4)
        + ' _ ' + convert(nvarchar, lookup_segment5)
        + ' _ ' + convert(nvarchar, lookup_segment6)
        + ' _ ' + convert(nvarchar, lookup_segment7)
        + ' _ ' + convert(nvarchar, lookup_segment8),
        convert(nvarchar, reference_type)
        + ' _ ' + convert(nvarchar, discountable_group)
        + ' _ ' + convert(nvarchar, media_category)
        + ' _ ' + convert(nvarchar, exception_reason)
        + ' _ ' + convert(nvarchar, basic_subcode)
        + ' _ ' + convert(nvarchar, update_register_activity)
        + ' _ ' + convert(nvarchar, store_balance_group)
        + ' _ ' + convert(nvarchar, reference_no_option)
        + ' _ ' + convert(nvarchar, available_as_link_attachment)
        + ' _ ' + convert(nvarchar, active_flag)
        + ' _ ' + convert(nvarchar, auto_config_verified),
	NULL --
  FROM line_object_action_association

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of line_object_action_association',
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
SELECT  @process_id, @comparison_id, 'line_object_action_attachment', 'Line Attachments', 
        convert(nvarchar, IsNull(transaction_category,0)) 
        + ' _ ' + convert(nvarchar, line_object) 
        + ' _ ' + convert(nvarchar, line_action)
        + ' _ ' + convert(nvarchar, attachment_type)
        + ' _ ' + convert(nvarchar, note_type),
        convert(nvarchar, merchandise_category)
        + ' _ ' + convert(nvarchar, upc_lookup_division)
        + ' _ ' + convert(nvarchar, attachment_mandatory)
        + ' _ ' + convert(nvarchar, transaction_category)
        + ' _ ' + convert(nvarchar, auto_config_verified),
	NULL,
	NULL --
  FROM line_object_action_attachment

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of line_object_action_attachment',
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
SELECT  @process_id, @comparison_id, 'line_object_action_lookup', 'Line Object Action Lookup', 
        convert(nvarchar, lookup_code_type) 
        + ' _ ' + convert(nvarchar, lookup_line_object) 
        + ' _ ' + convert(nvarchar, lookup_line_action)
        + ' _ ' + convert(nvarchar, lookup_pos_code),
        convert(nvarchar, line_object)
        + ' _ ' + convert(nvarchar, line_action)
        + ' _ ' + convert(nvarchar, discount_reversal_flag),
	NULL,
	NULL --
  FROM line_object_action_lookup

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of line_object_action_lookup',
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
SELECT  @process_id, @comparison_id, 'line_object_lookup', 'Line Object Lookup', 
        convert(nvarchar, lookup_line_object) 
+ ' _ ' + convert(nvarchar, store_no),
        convert(nvarchar, line_object),
	NULL,
	NULL --
  FROM line_object_lookup

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of line_object_lookup',
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
SELECT  @process_id, @comparison_id, 'interface_applicability', 'I/F Applicability', 
        convert(nvarchar, transaction_category) 
        + ' _ ' + convert(nvarchar, line_object) 
        + ' _ ' + convert(nvarchar, line_action)
        + ' _ ' + convert(nvarchar, interface_id),
	NULL,
	NULL,
	NULL --
  FROM interface_applicability

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of interface_applicability',
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
SELECT  @process_id, @comparison_id, 'if_rejection_reassignment', 'I/F Rejection Reassignment', 
        convert(nvarchar, if_reject_reason) 
        + ' _ ' + convert(nvarchar, line_object) 
        + ' _ ' + convert(nvarchar, line_action),
        convert(nvarchar, reassign_line_object)
        + ' _ ' + convert(nvarchar, reassign_line_action),
	NULL,
	NULL --
  FROM if_rejection_reassignment

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of if_rejection_reassignment',
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
SELECT  @process_id, @comparison_id, 'card_type', 'Card Type',
        convert(nvarchar, card_type),
        convert(nvarchar, line_object)
        + ' _ ' + convert(nvarchar, check_digit_routine_number)
        + ' _ ' + convert(nvarchar, payment_line_object)
        + ' _ ' + convert(nvarchar, gl_replacement_value)
        + ' _ ' + convert(nvarchar, code_meaning_control),
	NULL,
	card_type_description
  FROM card_type

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of card_type',
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
SELECT  @process_id, @comparison_id, 'reference_type_validation', 'Reference Type Validation',
        convert(nvarchar, reference_type)
        + ' _ ' + convert(nvarchar, validation_type),
        convert(nvarchar, edit_active_flag)
        + ' _ ' + convert(nvarchar, manual_active_flag),
	NULL,
	NULL --
  FROM reference_type_validation

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of reference_type_validation',
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
SELECT  @process_id, @comparison_id, 'restricted_field', 'Restricted Field',
        convert(nvarchar, field_name)
        + ' _ ' + convert(nvarchar, field_value),
        convert(nvarchar, restriction_level)
        + ' _ ' + convert(nvarchar, active_flag),
	NULL,
	NULL --
  FROM restricted_field

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of restricted_field',
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
SELECT  @process_id, @comparison_id, 'cust_liability_reference_type', 'C/L Reference Type',
        convert(nvarchar, reference_type),
        convert(nvarchar, reference_range_lookup)
        + ' _ ' + convert(nvarchar, default_tracking_id)
        + ' _ ' + convert(nvarchar, reference_no_datatype)
        + ' _ ' + convert(nvarchar, reference_no_length)
        + ' _ ' + convert(nvarchar, check_digit_routine_number)
        + ' _ ' + convert(nvarchar, unique_by_store_key)
        + ' _ ' + convert(nvarchar, history_days)
        + ' _ ' + convert(nvarchar, history_cleanup_criteria)
        + ' _ ' + convert(nvarchar, low_stock_qty),
        convert(nvarchar, pos_lookup)
        + ' _ ' + convert(nvarchar, pos_amount_1_source_column_no)
        + ' _ ' + convert(nvarchar, pos_amount_2_source_column_no)
        + ' _ ' + convert(nvarchar, pos_amount_3_source_column_no)
        + ' _ ' + convert(nvarchar, stock_flag)
        + ' _ ' + convert(nvarchar, track_detail_flag)
        + ' _ ' + convert(nvarchar, employee_tracking_id)
        + ' _ ' + convert(nvarchar, import_tracking_id)
        + ' _ ' + convert(nvarchar, currency_id),
	NULL --
  FROM cust_liability_reference_type

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of cust_liability_reference_type',
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
SELECT  @process_id, @comparison_id, 'cust_liability_type', 'C/L Type',
        convert(nvarchar, reference_type)
        + ' _ ' + convert(nvarchar, tracking_id),
        convert(nvarchar, expiry_days)
        + ' _ ' + convert(nvarchar, customer_liability_group)
        + ' _ ' + convert(nvarchar, active_flag)
        + ' _ ' + convert(nvarchar, copy_from_reference_type),
	NULL,
	tracking_id_description
  FROM cust_liability_type

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of cust_liability_type',
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
SELECT  @process_id, @comparison_id, 'cust_liab_active_validation', 'C/L Active Validation',
        convert(nvarchar, reference_type)
        + ' _ ' + convert(nvarchar, tracking_id)
        + ' _ ' + convert(nvarchar, validation_id),
        convert(nvarchar, priority_no),
	NULL,
	NULL --
  FROM cust_liab_active_validation

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of cust_liab_active_validation',
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
SELECT  @process_id, @comparison_id, 'department_rollout_lookup', 'Department Rollout Lookup',
        convert(nvarchar, source_line_object)
        + ' _ ' + convert(nvarchar, pos_deptclass),
        convert(nvarchar, destination_line_object),
	NULL,
	NULL --
  FROM department_rollout_lookup

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of department_rollout_lookup',
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
SELECT  @process_id, @comparison_id, 'gl_account_segment_lookup', 'G/L A/C Segment Lookup',
        convert(nvarchar, lookup_type)
        + ' _ ' + convert(nvarchar, lookup_from_value),
        convert(nvarchar, lookup_to_value)
        + ' _ ' + convert(nvarchar, gl_replacement_value),
	NULL,
	NULL --
  FROM gl_account_segment_lookup

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of gl_account_segment_lookup',
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
SELECT  @process_id, @comparison_id, 'media_parameter_object', 'Media Parameter Object',
        convert(nvarchar, media_parameter_set_no)
        + ' _ ' + convert(nvarchar, line_object)
        + ' _ ' + convert(nvarchar, rec_type),
        convert(nvarchar, rec_group_line_object),
	NULL,
	NULL --
  FROM media_parameter_object

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of media_parameter_object',
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
SELECT  @process_id, @comparison_id, 'tax_level', 'Tax Level',
        convert(nvarchar, line_object),
        convert(nvarchar, tax_level),
	NULL,
	NULL --
  FROM tax_level

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of tax_level',
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
SELECT  @process_id, @comparison_id, 'tax_default', 'Tax Default',
        convert(nvarchar, tax_jurisdiction)
        + ' _ ' + convert(nvarchar, line_object)
        + ' _ ' + convert(nvarchar, tax_level)
        + ' _ ' + convert(nvarchar, effective_from_date, 9),
        convert(nvarchar, tax_rate_code)
        + ' _ ' + convert(nvarchar, effective_until_date, 9)
        + ' _ ' + convert(nvarchar, inserted_by_trigger),
	NULL,
	NULL --
  FROM tax_default

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of tax_default',
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
SELECT  @process_id, @comparison_id, 'code_description', 'Code Description',
        convert(nvarchar, code_type)
        + ' _ ' + convert(nvarchar, code),
        convert(nvarchar, code_display_descr)
        + ' _ ' + convert(nvarchar, code_meaning_control)
        + ' _ ' + convert(nvarchar, min_compatible_exe)
        + ' _ ' + convert(nvarchar, alpha_code)
        + ' _ ' + convert(nvarchar, active_flag)
        + ' _ ' + convert(nvarchar, auto_config_verified),
	code_system_descr,
	NULL --
  FROM code_description
 WHERE code_meaning_control = 'U' -- user entries only

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of code_description',
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
SELECT  @process_id, @comparison_id, 'stock_control_display_def', 'Information Set',
        convert(nvarchar, display_def_id),
        convert(nvarchar, upc_no_fe_resource_id)
        + ' _ ' + convert(nvarchar, merchandise_key_fe_resource_id)
        + ' _ ' + convert(nvarchar, initiated_by_fe_resource_id)
        + ' _ ' + convert(nvarchar, units_fe_resource_id)
        + ' _ ' + convert(nvarchar, other_store_no_fe_resource_id)
        + ' _ ' + convert(nvarchar, location_no_fe_resource_id)
        + ' _ ' + convert(nvarchar, vendor_no_fe_resource_id)
        + ' _ ' + convert(nvarchar, count_date_fe_resource_id)
        + ' _ ' + convert(nvarchar, pos_identifier_fe_resource_id)
        + ' _ ' + convert(nvarchar, pos_id_type_fe_resource_id)
        + ' _ ' + convert(nvarchar, pos_deptclass_fe_resource_id)
        + ' _ ' + convert(nvarchar, upc_division_fe_resource_id)
        + ' _ ' + convert(nvarchar, originating_str_fe_resource_id),
        convert(nvarchar, upc_no_code_type)
        + ' _ ' + convert(nvarchar, merchandise_key_code_type)
        + ' _ ' + convert(nvarchar, units_code_type)
        + ' _ ' + convert(nvarchar, other_store_no_code_type)
        + ' _ ' + convert(nvarchar, location_no_code_type)
        + ' _ ' + convert(nvarchar, pos_id_type_code_type)
        + ' _ ' + convert(nvarchar, pos_deptclass_code_type)
        + ' _ ' + convert(nvarchar, upc_division_code_type)
        + ' _ ' + convert(nvarchar, originating_str_code_type)
        + ' _ ' + convert(nvarchar, initiated_by_code_type)
        + ' _ ' + convert(nvarchar, imrd_fe_resource_id)
        + ' _ ' + convert(nvarchar, imrd_code_type)
        + ' _ ' + convert(nvarchar, reason_fe_resource_id)
        + ' _ ' + convert(nvarchar, reason_code_type)
        + ' _ ' + convert(nvarchar, active_flag)
        + ' _ ' + convert(nvarchar, units_reversal_factor)
        + ' _ ' + convert(nvarchar, vendor_no_code_type)
        + ' _ ' + convert(nvarchar, pos_identifier_code_type),
	display_def_descr
  FROM stock_control_display_def

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of stock_control_display_def',
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
SELECT  @process_id, @comparison_id, 'geninfo_lookup', 'Geninfo Lookup',
        convert(nvarchar, form_name)
        + ' _ ' + convert(nvarchar, field_name),
        convert(nvarchar, field_datatype)
        + ' _ ' + convert(nvarchar, display_def_id)
        + ' _ ' + convert(nvarchar, column_name)
        + ' _ ' + convert(nvarchar, auto_config_verified)
        + ' _ ' + convert(nvarchar, form_code),
        convert(nvarchar, count_date_flag)
        + ' _ ' + convert(nvarchar, imrd_flag)
        + ' _ ' + convert(nvarchar, initiated_by_host_flag)
        + ' _ ' + convert(nvarchar, location_no_flag)
        + ' _ ' + convert(nvarchar, merchandise_key_flag)
        + ' _ ' + convert(nvarchar, originating_store_no_flag)
        + ' _ ' + convert(nvarchar, other_store_no_flag)
        + ' _ ' + convert(nvarchar, pos_deptclass_flag)
        + ' _ ' + convert(nvarchar, pos_identifier_flag)
        + ' _ ' + convert(nvarchar, reason_flag)
        + ' _ ' + convert(nvarchar, units_flag)
        + ' _ ' + convert(nvarchar, upc_no_flag)
        + ' _ ' + convert(nvarchar, vendor_no_flag),
	NULL --
  FROM geninfo_lookup

SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to list current content of geninfo_lookup',
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

SET NOCOUNT ON

RETURN

error:

	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, 1
	RETURN
```

