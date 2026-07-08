# dbo.util_change_liability_info_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_change_liability_info_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.util_change_liability_info_$sp 
                                
  AS
/*
PROC NAME: basic_nonsale_interface_$sp
     DESC: Builds nonsale interface table named basic_nonsale_interface
           to be used by smartload script bscintface.ict to generate an
           ASCII file which will then be used by BASIX program to create
 	   nonsale interface *IFNSS
           Table is built from if_interface_control, if_transaction_header,
    	   if_transaction_line, if_stock_control_detail, 
    	   line_object_action_association
  HISTORY:
Date	  Name		Defect	Desc
Dec18,01  Winnie       1-9Q1RX	Change process_step_log update statement for MSSQL compatibility.
Nov13,01  Winnie	8846	R3 Error handling, add logic to log process_log.
Mar09,01  Phu		7176    Split into several rows where units > 32767
May25,00  John G	5864 	Change '= NULL' to 'IS NULL' where applicable to mirror Oracle.
Mar21,00  Louise M  	6084	To pick up the right-most 4 digits of the transaction_no
Oct28,99  Phu		5535	Remove hard-coded carton distribution and transfer received line_object/line_action
JUL16,99  Louise M.	5029	Added the Return Reason code on RTV transactions in the identifier
				field of the header record (subcode 935, 'J')
Apr05,99  Daphna F	4422	Allow Layaways to interface to Basic Non-Sale
May29,98  Paul S	
Nov18,97  Phu T		n/a	Author  
*/

DECLARE
	@amt_per_unit			numeric(12,4),
	@basic_nonsale_type		char(1),
	@cashier_no			char(5),
	@count				numeric(12,0),
	@count_date			smalldatetime,
        @completed_workload		numeric(12,0),
	@cursor_open			tinyint,
	@entry_time			char(4),
	@errmsg 			varchar(255),
	@errno 				int,
	@first_batch			int,
	@identifier			char(20),
	@gross_line_amount		numeric(12,4),
	@if_entry_no			numeric(12,0),
	@last_retrieval_datetime 	datetime,
	@last_posting_datetime 		datetime,
	@line_id			numeric(5,0),
	@location_no			int,
	@loop_flag			smallint,
	@max_line_id			numeric(5,0),
	@merchandise_key		numeric(14,0),
	@message_id			int,
	@object_name			varchar(255),
	@operation_name			varchar(100),
	@other_store_no			int,
	@pos_discount_amount		numeric(12,4),
	@posting_in_progress 		tinyint,
	@prev_if_entry_no		numeric(12,0),
	@process_log_entry 		tinyint,
	@process_no 			smallint,
	@process_name			varchar(100),
	@process_timestamp 		float,
	@quantity			char(10),
	@quantity_num			numeric(10,0),
	@reference_no			varchar(20),
	@reference_type			tinyint,
	@register_no			char(5),
	@rows 				int,
	@row_count			int,
	@row_split 			int,
	@seq_no				smallint,
	@split_counter			smallint,
	@store_no			char(3),
	@subcode			char(3),
	@terminate_interface 		tinyint,
	@transaction_count 		numeric(12,0),
	@transaction_date		char(8),
	@transaction_no			char(4),
	@units				numeric(15,4),
	@unit_remainded			numeric(10,0),
	@upc_no				numeric(14,0),
	@vendor_no			varchar(6),
	@zero_filler			char(14)

SELECT 	@cursor_open = 0,
	@errmsg = NULL,
	@process_log_entry = 0,
	@process_no = 204,
	@process_timestamp = 0,
	@terminate_interface = 0,
	@transaction_count = 0,
	@zero_filler = '00000000000000',
	@process_name = 'basic_nonsale_interface_$sp',
	@message_id = 201068,
	@loop_flag = 0


CREATE TABLE #nonsale_base (
	transaction_date	char(8)		not null,
	store_no		char(3)		not null,
	register_no		char(5)		not null,
	transaction_no		char(4)		not null,
	cashier_no		char(5)		not null,
	entry_time		char(4)		not null,
	subcode			char(3)		not null,
	if_entry_no		numeric(12,0)	not null,
	line_id			numeric(5,0)	not null,
	basic_nonsale_type	char(1)		not null,
	gross_line_amount	numeric(12,4)	null,
	pos_discount_amount	numeric(12,4)	null,
	amt_per_unit		numeric(12,4)	null,
	reference_type		tinyint		null,
	reference_no		varchar(20)	null,
	upc_no			numeric(14,0)	null,
	units			numeric(15,4)	null,
	merchandise_key		numeric(14,0)	null,
	count_date		smalldatetime	null,
	other_store_no		int		null,
	location_no		int		null,
	vendor_no		varchar(6)	null )

SELECT @errno = @@error
IF @errno <> 0
  BEGIN
	SELECT @errmsg = 'Unable to create table #nonsale_base',
	       @object_name = '#nonsale_base',
	       @operation_name = 'CREATE'
	GOTO error
  END





RETURN

error:   /* Common error handler */

        EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
        @process_name, @object_name, @operation_name, 1, 1, 
        @process_log_entry, @process_timestamp, @transaction_count

	RETURN
```

