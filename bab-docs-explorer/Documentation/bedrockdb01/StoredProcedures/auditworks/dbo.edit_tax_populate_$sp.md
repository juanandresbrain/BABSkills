# dbo.edit_tax_populate_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.edit_tax_populate_$sp"]
    ORG_CHN(["ORG_CHN"]) --> SP
    auditworks_parameter(["auditworks_parameter"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    edit_verify_tax_jur__sp(["edit_verify_tax_jur_$sp"]) --> SP
    interface_applicability(["interface_applicability"]) --> SP
    tax_default(["tax_default"]) --> SP
    tax_jurisdiction(["tax_jurisdiction"]) --> SP
    tax_jurisdiction_post_code(["tax_jurisdiction_post_code"]) --> SP
    tax_level(["tax_level"]) --> SP
    transl_customer(["transl_customer"]) --> SP
    transl_discount_detail(["transl_discount_detail"]) --> SP
    transl_return_detail(["transl_return_detail"]) --> SP
    transl_stock_control_detail(["transl_stock_control_detail"]) --> SP
    transl_tax_override_detail(["transl_tax_override_detail"]) --> SP
    transl_transaction_line(["transl_transaction_line"]) --> SP
    transl_transaction_line_link(["transl_transaction_line_link"]) --> SP
    work_interface_reject_edit(["work_interface_reject_edit"]) --> SP
    work_merchandise_edit(["work_merchandise_edit"]) --> SP
    work_tax_detail(["work_tax_detail"]) --> SP
    work_tax_exception_jur(["work_tax_exception_jur"]) --> SP
    work_tax_post_template(["work_tax_post_template"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_CHN |
| auditworks_parameter |
| common_error_handling_$sp |
| edit_verify_tax_jur_$sp |
| interface_applicability |
| tax_default |
| tax_jurisdiction |
| tax_jurisdiction_post_code |
| tax_level |
| transl_customer |
| transl_discount_detail |
| transl_return_detail |
| transl_stock_control_detail |
| transl_tax_override_detail |
| transl_transaction_line |
| transl_transaction_line_link |
| work_interface_reject_edit |
| work_merchandise_edit |
| work_tax_detail |
| work_tax_exception_jur |
| work_tax_post_template |

## Stored Procedure Code

```sql
CREATE proc  dbo.edit_tax_populate_$sp (
  @edit_process_no                       int,
  @process_id                            binary(16),
  @function_no                           smallint,
  @applicability_method                  tinyint,
  @class_exception_flag                  tinyint,
  @sku_exception_flag                    tinyint,
  @style_exception_flag                  tinyint,
  @item_group_exception_flag             tinyint,
  @include_expense                       tinyint,
  @include_pickup                        tinyint,
  @unapplied_discounts_exist             tinyint,
  @tax_default_check                     tinyint = null,
  @exception_jurisdiction_check          tinyint = null,
  @errmsg                                nvarchar(2000) OUTPUT
)

AS

/*
PROC NAME: edit_tax_populate_$sp
     DESC: Populate tax info into work_tax_detail table from transl tables.
           Called by edit_pre_audit_tax_$sp.
           Tax details will be populated in sales_tax_populate_$sp for the post audit tax / manual functions.
           Tax details will be populated in sales_tax_rebuild_$sp for tax rebuilt.
     Unicode version.

IMPORTANT:
 Special scripting instructions are no longer necessary

  HISTORY:
Date     Name           Def#  Desc
Jun13,16 Vicci      DAOM-937  If a stock_control_detail attachment date or transl return detail attachment is greater than June 2079 (the max supported by a smalldatetime) then it causes error 298 so ignore them if they are future.
Jul15,15 Vicci    TFS-128531  Log UPC to work_tax_detail.
Jun29,15 Vicci    TFS-128115  Add missing code from 120654 to set fulfillment store;  this is required for consistency with 
                              sales_tax_populate_$sp since otherwise revalidation thinks changes have occurred.
Dec17,14 Paul          94103  use try catch
Jan07,11 Vicci        123998  Set track tax to false on alteration requests/cancellations are fed to Tax in addition to
                              alteration completions.
Dec14,10 Vicci        120654  Set return_from_store to fullfillment store so that its available to send to Avalara. 
Sep15,10 Vicci        120892  Add option to allocate transaction tax to item level on a per-order basis to support ES.
Aug17,10 Vicci        120255  Don't overlay the fulfillment store tax jurisdiction with that of the store in which the 
			      original purchase was made even if the fulfillment store tax jurisdiction matches that of
			      the store in which the return transaction was entered.
Mar03,10 Vicci        116582  Fix 109078.  Include header level "Customer Liability Load or Issuance" attachments in "from" table list.
Nov26,09 Vicci        114269  Set max_applied_by_line_id on tax line so that if by misfortune there is no merch/fee line to which the tax collected
                              may be applied it will still post to subledger thus avoiding an imbalance.
Sep21,09 Vicci        112842  Compensate for UI bug whereby tax_override_detail.taxable gets set to 100 when the attachment is viewed.
Jul21,09 Vicci        109078  Support having tax calculated on both order creation and fulfillment while only posting
                              one or the other to tax_tracking (in case of applicability_method = 0, if both
                              order and fulfillment have been configured to feed tax in interface applicability, tax will
                              be calculated on both but will feed tax-tracking upon fulfillment only).
                              Add recognition for header-level returns.
                              Add recognition of fulfillment store since tax charged based on store where merch will be picked up.
                              Add recognition for order placement date.
May30,08 Vicci        101675  Correct cleanup of work_tax_exception_jur
Mar25,08 Vicci      1-38MDAZ  Log units
Aug16,07 Paul        DV-1363  apply 81895 to SA5. added comments re #edit_tax_sent table.
Oct25,06 Phu           77931  Fix outer join for SQL 2005 Mode 90.
Mar28,05 Maryam      DV-1202  Handle the indirect association via line links. Handle send to customer as from_line_id 
                              is changed to be line_id. Support order pickups
Dec20,04 Maryam      DV-1191  Improve performance.
May18,04 David       DV-1071  Use ORG_CHN table instead of store_salesaudit, changed @process_id to binary(16)
Jan12,07 Vicci         81895  Support sale following loan, sale following rental, repair pickup, alteration pickup
Apr03,03 David          7319  Set SIGN of pos_discount_amount properly.
Mar04,03 Phu            6512  Avoid error: insert NULL into 'discount_amount' in #tax_post_main
Jan23,03 Phu            5933  Retrieve sent tax jurisdiction if zip code is defined
Dec19,02 Phu            5327  Post ordered trans to tax_detail, prorate tax collected to nontaxable if required
Dec10,02 Phu            5292  Retrieve tax override
Aug01,02 Phu  1-E3LUO  Retrieve tax_jurisdiction of sent transaction
Apr25,02 Phu         1-C9P5S  Pre Audit tax


*/

DECLARE
	@errno				int,
	@errmsg2			nvarchar(2000),
	@errline			int,
	@message_id			int,
	@object_name			nvarchar(255),
	@operation_name			nvarchar(100),
	@process_name			nvarchar(100),
	@rows				int,
	@trace_msg			nvarchar(255),
	@tax_allocation_by_refno	tinyint; 

SELECT	@message_id = 201068,
	@process_name = 'edit_tax_populate_$sp';

BEGIN TRY

SELECT @trace_msg = NCHAR(13) + NCHAR(10) + ':LOG && edit_tax_populate_$sp starts: ' + CONVERT(nchar, getdate(), 8);
PRINT @trace_msg;

IF EXISTS (SELECT * FROM auditworks_parameter WHERE par_name = 'reference_dependent_tax_alloc' AND par_value = '1')
  SELECT @tax_allocation_by_refno = 1;
ELSE
  SELECT @tax_allocation_by_refno = 0;

/* build temp table of transaction details. Use tax_jurisdiction from
   transl_tax_override_detail if available. Otherwise use default for store.
   Must build table from permanent empty table because of style_ref_id_datatype */

-- columns: transaction_no, register_no, entry_date_time, transaction_series are populated
-- and used by the edit only

  SELECT @errmsg = 'Failed to create temp table #tax_post_main.',
         @object_name = '#tax_post_main',
         @operation_name = 'CREATE'
SELECT transaction_id, line_id, store_no, transaction_date, line_object_type, line_object,
       class_code, gross_line_amount, discount_amount, amount_sign, gl_effect,
       store_tax_jurisdiction, tax_jurisdiction, style_reference_id, sku_id, upc_lookup_division,
       return_from_store, return_from_date, override_tax_category, tax_paid_flag, header_override_flag,
       all_tax_override_flag, transaction_no, register_no, entry_date_time, transaction_series, units, track_tax, 
       reference_type, reference_no, upc_no
INTO #tax_post_main 
FROM work_tax_post_template WITH (NOLOCK);

-- #edit_tax_sent table is no longer needed

SELECT @errmsg = 'Failed to insert #tax_post_main.',
         @object_name = '#tax_post_main',
         @operation_name = 'INSERT';

IF (@class_exception_flag = 1 OR @style_exception_flag = 1  OR @sku_exception_flag = 1 OR @item_group_exception_flag = 1)
  BEGIN
    IF @applicability_method = 0  -- based on interface_applicability
      INSERT #tax_post_main(
             transaction_id,
	     line_id,
	     store_no,
	     transaction_date,
	     line_object_type,
	     line_object,
	     class_code,
	     gross_line_amount,
	     discount_amount,
	     amount_sign,
	     gl_effect,
	     store_tax_jurisdiction,
	     tax_jurisdiction,
	     style_reference_id,
	     sku_id,
	     upc_lookup_division,
	     return_from_store,
	     return_from_date,
	     override_tax_category,
	     tax_paid_flag,
	     header_override_flag,
	     all_tax_override_flag,
	     units,
	     track_tax,
	     transaction_no,
	     register_no,
	     entry_date_time,
	     transaction_series,
	     reference_type,
	     reference_no,
	     upc_no)
      SELECT
             tt.transaction_id,
	     tl.line_id,
	     tt.store_no,
             tt.transaction_date,
	     tl.line_object_type,
	     tl.line_object,
	  COALESCE(md.class_code, 0),
	     tl.gross_line_amount,
	     tl.pos_discount_amount,
	     ((SIGN(1 + tl.db_cr_none) * 2) - 1) * tl.voiding_reversal_flag, -- amount_sign
	     tl.db_cr_none * -1 * tl.voiding_reversal_flag, -- gl_effect
	     tt.store_tax_jurisdiction,
	     MAX(COALESCE(tod.exception_tax_jurisdiction, todl.exception_tax_jurisdiction, tt.tod_tax_jurisdiction, f.TAX_JRSDCTN_CODE, tt.store_tax_jurisdiction)), -- tax_jurisdiction def 74673
	     COALESCE(md.style_reference_id,0),
	     COALESCE(md.sku_id,0),
	     COALESCE(md.upc_lookup_division,0),
	     CASE WHEN MAX(COALESCE(tod.exception_tax_jurisdiction, todl.exception_tax_jurisdiction, tt.tod_tax_jurisdiction)) IS NULL
	          THEN MAX(COALESCE(f.ORG_CHN_NUM, rd.return_from_store, rdl.return_from_store, rdh.return_from_store))
	          ELSE NULL
	     END return_from_store,
	     CASE WHEN MAX(COALESCE(o.count_date, ol.count_date, oh.count_date, rd.return_from_date, rdl.return_from_date, rdh.return_from_date)) > dateadd(dd, 1, getdate())
	          THEN NULL
	          ELSE MAX(COALESCE(o.count_date, ol.count_date, oh.count_date, rd.return_from_date, rdl.return_from_date, rdh.return_from_date)) 
	     END,
	     0, -- override_tax_category
	     (1 - SIGN(ABS(tl.line_object_type - 5 ))) *
	      ((1-SIGN(ABS(tl.line_action - 15))) + (1-SIGN(ABS(tl.line_action - 16))) )
	      + (1 - SIGN(ABS(tl.line_object_type - 7 ))), -- tax_paid_flag
	     COALESCE(tt.header_override_flag, (1 - SIGN (MIN(tod.line_id))), (3 - SIGN(MIN(todl.line_id)))), -- header_override_flag  -- def 74673
	     COALESCE(tt.all_tax_override_flag, (1 - SIGN (MIN(COALESCE(tod.tax_level, todl.tax_level))))), -- all_tax_override_flag  -- def 74673
	     COALESCE(md.units, 1),
	     CASE WHEN ex.line_action IS NOT NULL THEN 0 ELSE 1 END,  --track_tax
	     tt.transaction_no,
	     tt.register_no,
	     tt.entry_date_time,
	     tt.transaction_series,
	     CASE WHEN @tax_allocation_by_refno = 1 THEN tl.reference_type ELSE 0 END,
             CASE WHEN @tax_allocation_by_refno = 1 THEN COALESCE(tl.reference_no, '0') ELSE '0' END,
             COALESCE(md.upc_no, 0)
        FROM #tax_transactions tt WITH (NOLOCK)
	     INNER JOIN transl_transaction_line tl WITH (NOLOCK) 
	        ON tt.transaction_id = tl.transaction_id
	       AND tl.line_object_type IN (1, 2, 5, 7)   /* tax type*/
               AND tl.line_void_flag = 0  
	     INNER JOIN interface_applicability ia  WITH (NOLOCK)
	        ON tt.transaction_category = ia.transaction_category 
	       AND tl.line_object = ia.line_object 
	       AND tl.line_action = ia.line_action
	       AND ia.interface_id = 12
	     LEFT OUTER JOIN work_merchandise_edit md WITH (NOLOCK) 
                ON tl.transaction_id = md.transaction_id 
                AND tl.line_id = md.line_id
             LEFT OUTER JOIN transl_transaction_line_link tll  WITH (NOLOCK)
                ON tl.transaction_id = tll.transaction_id
                AND tl.line_id = tll.line_id  
             LEFT OUTER JOIN transl_tax_override_detail tod 
                ON tl.transaction_id = tod.transaction_id
                AND tl.line_id = tod.line_id
             LEFT OUTER JOIN transl_tax_override_detail todl WITH (NOLOCK)
                ON tll.transaction_id = todl.transaction_id
                AND tll.linked_line_id = todl.line_id
             LEFT OUTER JOIN transl_return_detail rd WITH (NOLOCK) 
                ON tl.transaction_id = rd.transaction_id
                AND tl.line_id = rd.line_id  
             LEFT OUTER JOIN transl_return_detail rdl  WITH (NOLOCK)
                ON tll.transaction_id = rdl.transaction_id
                AND tll.linked_line_id = rdl.line_id  
             LEFT OUTER JOIN transl_return_detail rdh  WITH (NOLOCK)
                ON tl.transaction_id = rdh.transaction_id
                AND 0 = rdh.line_id  
             LEFT OUTER JOIN transl_stock_control_detail o  WITH (NOLOCK)
                ON tt.store_no = o.store_no
                AND tt.register_no = o.register_no
                AND tt.entry_date_time = o.entry_date_time
                AND tt.transaction_series = o.transaction_series
                AND tt.transaction_no = o.transaction_no
                AND tl.line_id = o.line_id  
                AND o.display_def_id = 31
                AND o.count_date IS NOT NULL
                AND o.count_date < dateadd(dd, 1, getdate())
             LEFT OUTER JOIN transl_stock_control_detail ol  WITH (NOLOCK)
                ON tt.store_no = ol.store_no
                AND tt.register_no = ol.register_no
                AND tt.entry_date_time = ol.entry_date_time
                AND tt.transaction_series = ol.transaction_series
                AND tt.transaction_no = ol.transaction_no
              AND tll.linked_line_id = ol.line_id  
                AND ol.display_def_id = 31
                AND ol.count_date IS NOT NULL
             LEFT OUTER JOIN transl_stock_control_detail oh  WITH (NOLOCK)
                ON tt.store_no = oh.store_no
                AND tt.register_no = oh.register_no
                AND tt.entry_date_time = oh.entry_date_time
                AND tt.transaction_series = oh.transaction_series
                AND tt.transaction_no = oh.transaction_no
                AND 0 = oh.line_id  
                AND oh.display_def_id = 31
                AND oh.count_date IS NOT NULL
             LEFT OUTER JOIN ORG_CHN f  WITH (NOLOCK)
                ON md.fulfillment_store_no = f.ORG_CHN_NUM
             LEFT OUTER JOIN (SELECT DISTINCT ai1.transaction_category, 
                                     ai1.line_object, 
                                     ai1.line_action
                                FROM interface_applicability ai1
                                     INNER JOIN interface_applicability ai2
                                        ON ai2.interface_id = 12
                                       AND ai1.transaction_category = ai2.transaction_category
                                       AND ai1.line_object = ai2.line_object
                                       AND ai2.line_action in (201, 211, 142, 147, 90, 97, 147, 197, 198)
                                       AND (   (ai1.line_action in (7, 8) AND ai2.line_action in (142, 90))
                                            OR (ai1.line_action in (95, 96) AND ai2.line_action in (147, 97))
                                            OR (ai1.line_action in (101, 102) AND ai2.line_action = 201)
                                            OR (ai1.line_action in (111, 112) AND ai2.line_action = 211)
                                            OR (ai1.line_action in (191, 194) AND ai2.line_action = 197)
                                            OR (ai1.line_action in (192, 195) AND ai2.line_action = 198))
                               WHERE ai1.interface_id = 12
                                 AND ai1.line_action in (7, 8, 95, 96,101, 102, 111, 112, 191, 194, 192, 195) ) ex  --order and layaway creation to be ignore if pickup/delivery also set to feed to avoid double-counting
                ON tt.transaction_category = ex.transaction_category                
                AND tl.line_object = ex.line_object
                AND tl.line_action = ex.line_action
    GROUP BY tt.transaction_id,
	     tl.line_id,
	     tt.store_no,
             tt.transaction_date,
	     tl.line_object_type,
	     tl.line_object,
	     COALESCE(md.class_code, 0),
	     tl.gross_line_amount,
	     tl.pos_discount_amount,
	     ((SIGN(1 + tl.db_cr_none) * 2) - 1) * tl.voiding_reversal_flag,
	     tl.db_cr_none * -1 * tl.voiding_reversal_flag,
	     tt.store_tax_jurisdiction,
	     COALESCE(md.style_reference_id,0),
	     COALESCE(md.sku_id,0),
	     COALESCE(md.upc_lookup_division,0),
	     (1 - SIGN(ABS(tl.line_object_type - 5 ))) * 
	     ((1-SIGN(ABS(tl.line_action - 15))) + (1-SIGN(ABS(tl.line_action - 16)))) 
	     + (1 - SIGN(ABS(tl.line_object_type - 7 ))),
	     tt.header_override_flag,  -- def 74673
	     tt.all_tax_override_flag,   -- def 74673
             COALESCE(md.units, 1),
             CASE WHEN ex.line_action IS NOT NULL THEN 0 ELSE 1 END,
	     tt.transaction_no,
	     tt.register_no,
	     tt.entry_date_time,
	     tt.transaction_series,
	     CASE WHEN @tax_allocation_by_refno = 1 THEN tl.reference_type ELSE 0 END,
             CASE WHEN @tax_allocation_by_refno = 1 THEN COALESCE(tl.reference_no, '0') ELSE '0' END,
             COALESCE(md.upc_no, 0);
  ELSE 
      INSERT #tax_post_main(
	     transaction_id,
	     line_id,
	     store_no,
	     transaction_date,
	     line_object_type,
	     line_object,
	     class_code,
	     gross_line_amount,
	     discount_amount,
	     amount_sign,
	     gl_effect,
	     store_tax_jurisdiction,
	     tax_jurisdiction,
	     style_reference_id,
	     sku_id,
	     upc_lookup_division,
	     return_from_store,
	     return_from_date,
	     override_tax_category,
	     tax_paid_flag,
	     header_override_flag,
	     all_tax_override_flag,
	     units,
	     track_tax,
	     transaction_no,
	     register_no,
	     entry_date_time,
	     transaction_series,
	     reference_type,
	     reference_no,
	     upc_no)
      SELECT
             tl.transaction_id,
	     tl.line_id,
	     tt.store_no,
             tt.transaction_date,
	     tl.line_object_type,
	     tl.line_object,
	     COALESCE(md.class_code, 0),
	     tl.gross_line_amount,
	     tl.pos_discount_amount,
	     ((SIGN(1 + tl.db_cr_none) * 2) - 1) * tl.voiding_reversal_flag, -- amount_sign
	     tl.db_cr_none * -1 * tl.voiding_reversal_flag, -- gl_effect
	     tt.store_tax_jurisdiction,
	     MAX(COALESCE(tod.exception_tax_jurisdiction, todl.exception_tax_jurisdiction, tt.tod_tax_jurisdiction, f.TAX_JRSDCTN_CODE, tt.store_tax_jurisdiction)), -- tax_jurisdiction def 74673
	     COALESCE(md.style_reference_id,0),
	     COALESCE(md.sku_id,0),
	     COALESCE(md.upc_lookup_division,0),
	     CASE WHEN MAX(COALESCE(tod.exception_tax_jurisdiction, todl.exception_tax_jurisdiction, tt.tod_tax_jurisdiction)) IS NULL
	          THEN MAX(COALESCE(f.ORG_CHN_NUM, rd.return_from_store, rdl.return_from_store, rdh.return_from_store))
	          ELSE NULL
	     END,
	     CASE WHEN MAX(COALESCE(o.count_date, ol.count_date, oh.count_date, rd.return_from_date, rdl.return_from_date, rdh.return_from_date)) > dateadd(dd, 1, getdate())
	          THEN NULL
	          ELSE MAX(COALESCE(o.count_date, ol.count_date, oh.count_date, rd.return_from_date, rdl.return_from_date, rdh.return_from_date))
	     END,
	     0, -- override_tax_category
	     (1 - SIGN(ABS(tl.line_object_type - 5 ))) *
	      ((1-SIGN(ABS(tl.line_action - 15))) + (1-SIGN(ABS(tl.line_action - 16))) )
	      + (1 - SIGN(ABS(tl.line_object_type - 7 ))), -- tax_paid_flag
             COALESCE(tt.header_override_flag, (1 - SIGN (MIN(tod.line_id))), (3 - SIGN(MIN(todl.line_id)))), -- header_override_flag  -- def 74673
	     COALESCE(tt.all_tax_override_flag, (1 - SIGN (MIN(COALESCE(tod.tax_level, todl.tax_level))))), -- all_tax_override_flag  -- def 74673	     COALESCE(md.units, 1),
	     COALESCE(md.units, 1),
	     CASE WHEN @include_pickup = 1 AND tl.line_action IN ( 7, 95, 101, 111) THEN 0 ELSE 1 END,
	     tt.transaction_no,
	     tt.register_no,
	     tt.entry_date_time,
	     tt.transaction_series,
	     CASE WHEN @tax_allocation_by_refno = 1 THEN tl.reference_type ELSE 0 END,
             CASE WHEN @tax_allocation_by_refno = 1 THEN COALESCE(tl.reference_no, '0') ELSE '0' END,
             COALESCE(md.upc_no, 0)
        FROM #tax_transactions tt WITH (NOLOCK)
             INNER JOIN transl_transaction_line tl WITH (NOLOCK)
                ON tt.transaction_id = tl.transaction_id
                AND tl.line_object_type IN (1, 2, 5, 7 * @include_expense)   /* tax type*/
                AND tl.line_action not in (3, 4, 9, 10, 78, 79, 200, 203, 204, 210, 213, 214, 215, 223, 224, 225, 226, 227, 228, 191, 192, 193, 194, 195, 196, 32, 40, 41, 42, 43, 44, 45, 67, 74, 85, 100, 171, 172)
                AND (tl.line_action * @include_pickup) NOT IN ( 8, 96, 102, 112)
                AND (tl.line_action * (1 - @include_pickup)) NOT IN ( 90, 97, 98, 99, 201, 202, 211, 212, 142, 147)
                AND tl.line_void_flag = 0  
             LEFT OUTER JOIN work_merchandise_edit md WITH (NOLOCK)
                ON tl.transaction_id = md.transaction_id
                AND tl.line_id = md.line_id
             LEFT OUTER JOIN transl_transaction_line_link tll  WITH (NOLOCK)
                ON tl.transaction_id = tll.transaction_id
                AND tl.line_id = tll.line_id  
             LEFT OUTER JOIN transl_tax_override_detail tod 
                ON tl.transaction_id = tod.transaction_id
                AND tl.line_id = tod.line_id
             LEFT OUTER JOIN transl_tax_override_detail todl WITH (NOLOCK)
                ON tll.transaction_id = todl.transaction_id
              AND tll.linked_line_id = todl.line_id
             LEFT OUTER JOIN transl_return_detail rd WITH (NOLOCK) 
                ON tl.transaction_id = rd.transaction_id
               AND tl.line_id = rd.line_id  
             LEFT OUTER JOIN transl_return_detail rdl  WITH (NOLOCK)
                ON tll.transaction_id = rdl.transaction_id
                AND tll.linked_line_id = rdl.line_id  
             LEFT OUTER JOIN transl_return_detail rdh  WITH (NOLOCK)
                ON tl.transaction_id = rdh.transaction_id
                AND 0 = rdh.line_id  
             LEFT OUTER JOIN transl_stock_control_detail o  WITH (NOLOCK)
                ON tt.store_no = o.store_no
                AND tt.register_no = o.register_no
                AND tt.entry_date_time = o.entry_date_time
                AND tt.transaction_series = o.transaction_series
                AND tt.transaction_no = o.transaction_no
                AND tl.line_id = o.line_id  
                AND o.display_def_id = 31
                AND o.count_date IS NOT NULL
                AND o.count_date < dateadd(dd, 1, getdate())
             LEFT OUTER JOIN transl_stock_control_detail ol  WITH (NOLOCK)
                ON tt.store_no = ol.store_no
                AND tt.register_no = ol.register_no
                AND tt.entry_date_time = ol.entry_date_time
                AND tt.transaction_series = ol.transaction_series
                AND tt.transaction_no = ol.transaction_no
                AND tll.linked_line_id = ol.line_id  
                AND ol.display_def_id = 31
                AND ol.count_date IS NOT NULL
             LEFT OUTER JOIN transl_stock_control_detail oh  WITH (NOLOCK)
                ON tt.store_no = oh.store_no
                AND tt.register_no = oh.register_no
                AND tt.entry_date_time = oh.entry_date_time
                AND tt.transaction_series = oh.transaction_series
                AND tt.transaction_no = oh.transaction_no
                AND 0 = oh.line_id  
                AND oh.display_def_id = 31
                AND oh.count_date IS NOT NULL
             LEFT OUTER JOIN ORG_CHN f 
                ON md.fulfillment_store_no = f.ORG_CHN_NUM
    GROUP BY tl.transaction_id,
	     tl.line_id,
	     tt.store_no,
             tt.transaction_date,
	     tl.line_object_type,
	     tl.line_object,
	     COALESCE(md.class_code, 0),
	     tl.gross_line_amount,
	     tl.pos_discount_amount,
	     ((SIGN(1 + tl.db_cr_none) * 2) - 1) * tl.voiding_reversal_flag,
	     tl.db_cr_none * -1 * tl.voiding_reversal_flag,
	     tt.store_tax_jurisdiction,
	     COALESCE(md.style_reference_id,0),
	     COALESCE(md.sku_id,0),
	     COALESCE(md.upc_lookup_division,0),
	     (1 - SIGN(ABS(tl.line_object_type - 5 ))) * 
	     ((1-SIGN(ABS(tl.line_action - 15))) + (1-SIGN(ABS(tl.line_action - 16)))) 
	     + (1 - SIGN(ABS(tl.line_object_type - 7 ))),
	     tt.header_override_flag, -- def  74673
	     tt.all_tax_override_flag, -- def  74673
	     COALESCE(md.units, 1),
	     CASE WHEN @include_pickup = 1 AND tl.line_action IN ( 7, 95, 101, 111) THEN 0 ELSE 1 END,
	     tt.transaction_no,
	     tt.register_no,
	     tt.entry_date_time,
	     tt.transaction_series,
	     CASE WHEN @tax_allocation_by_refno = 1 THEN tl.reference_type ELSE 0 END,
             CASE WHEN @tax_allocation_by_refno = 1 THEN COALESCE(tl.reference_no, '0') ELSE '0' END,
             COALESCE(md.upc_no, 0);
  END; --(@class_exception_flag = 1 OR @style_exception_flag = 1  OR @sku_exception_flag = 1 OR @item_group_exception_flag = 1)
ELSE
  BEGIN
    IF @applicability_method = 0 -- based on interface_applicability
      INSERT #tax_post_main(
	     transaction_id,
	     line_id,
	     store_no,
	     transaction_date,
	     line_object_type,
	     line_object,
	     class_code,
	     gross_line_amount,
	     discount_amount,
	     amount_sign,
	     gl_effect,
	     store_tax_jurisdiction,
	     tax_jurisdiction,
	     style_reference_id,
	     sku_id,
	     upc_lookup_division,
	     return_from_store,
	     return_from_date,
	     override_tax_category,
	     tax_paid_flag,
	     header_override_flag,
	     all_tax_override_flag,
	     units,
	     track_tax,
	     transaction_no,
	     register_no,
	     entry_date_time,
	     transaction_series,
	     reference_type,
	     reference_no,
	     upc_no)
      SELECT
              tl.transaction_id,
	     tl.line_id,
	     tt.store_no,
              tt.transaction_date,
	     tl.line_object_type,
	     tl.line_object,
	     0, -- class_code
	     tl.gross_line_amount,
	     tl.pos_discount_amount,
	     ((SIGN(1 + tl.db_cr_none) * 2) - 1) * tl.voiding_reversal_flag, -- amount_sign
	     tl.db_cr_none * -1 * tl.voiding_reversal_flag, -- gl_effect
	     tt.store_tax_jurisdiction,
	     MAX(COALESCE(tod.exception_tax_jurisdiction, todl.exception_tax_jurisdiction, tt.tod_tax_jurisdiction, f.TAX_JRSDCTN_CODE, tt.store_tax_jurisdiction)), -- tax_jurisdiction def 74673
	     0, -- style_reference_id
	     0, -- sku_id
	     0, -- upc_lookup_division
	     CASE WHEN MAX(COALESCE(tod.exception_tax_jurisdiction, todl.exception_tax_jurisdiction, tt.tod_tax_jurisdiction)) IS NULL
	          THEN MAX(COALESCE(f.ORG_CHN_NUM, rd.return_from_store, rdl.return_from_store, rdh.return_from_store))
	          ELSE NULL
	     END,
	     CASE WHEN MAX(COALESCE(o.count_date, ol.count_date, oh.count_date, rd.return_from_date, rdl.return_from_date, rdh.return_from_date)) > dateadd(dd, 1, getdate())
	          THEN NULL
	          ELSE MAX(COALESCE(o.count_date, ol.count_date, oh.count_date, rd.return_from_date, rdl.return_from_date, rdh.return_from_date)) 
	     END,
	     0, -- override_tax_category
	     (1 - SIGN(ABS(tl.line_object_type - 5 ))) *
	     ((1-SIGN(ABS(tl.line_action - 15))) + (1-SIGN(ABS(tl.line_action - 16))) )
	      + (1 - SIGN(ABS(tl.line_object_type - 7 ))), -- tax_paid_flag
	     COALESCE(tt.header_override_flag, (1 - SIGN (MIN(tod.line_id))), (3 - SIGN(MIN(todl.line_id)))), -- header_override_flag  -- def 74673
	     COALESCE(tt.all_tax_override_flag, (1 - SIGN (MIN(COALESCE(tod.tax_level, todl.tax_level))))), -- all_tax_override_flag  -- def 74673
	     COALESCE(md.units, 1),
	     CASE WHEN ex.line_action IS NOT NULL THEN 0 ELSE 1 END,  --track_tax
	     tt.transaction_no,
	     tt.register_no,
	     tt.entry_date_time,
	     tt.transaction_series, 
	     CASE WHEN @tax_allocation_by_refno = 1 THEN tl.reference_type ELSE 0 END,
           CASE WHEN @tax_allocation_by_refno = 1 THEN COALESCE(tl.reference_no, '0') ELSE '0' END,
             0 --upc_no
        FROM #tax_transactions tt
             INNER JOIN transl_transaction_line tl
                 ON tt.transaction_id = tl.transaction_id
                 AND tl.line_object_type IN (1, 2, 5, 7)   /* tax type*/
                 AND tl.line_void_flag = 0
             INNER JOIN interface_applicability ia
                 ON tt.transaction_category = ia.transaction_category
                 AND tl.line_object = ia.line_object
                 AND tl.line_action = ia.line_action
                 AND ia.interface_id = 12
             LEFT OUTER JOIN work_merchandise_edit md   
                ON tl.transaction_id = md.transaction_id
                AND tl.line_id = md.line_id  
             LEFT OUTER JOIN transl_transaction_line_link tll  WITH (NOLOCK)
                ON tl.transaction_id = tll.transaction_id
                AND tl.line_id = tll.line_id  
   LEFT OUTER JOIN transl_tax_override_detail tod 
                ON tl.transaction_id = tod.transaction_id
                AND tl.line_id = tod.line_id
             LEFT OUTER JOIN transl_tax_override_detail todl WITH (NOLOCK)
               ON tll.transaction_id = todl.transaction_id
                AND tll.linked_line_id = todl.line_id
             LEFT OUTER JOIN transl_return_detail rd WITH (NOLOCK) 
                ON tl.transaction_id = rd.transaction_id
                AND tl.line_id = rd.line_id  
             LEFT OUTER JOIN transl_return_detail rdl  WITH (NOLOCK)
                ON tll.transaction_id = rdl.transaction_id
                AND tll.linked_line_id = rdl.line_id  
             LEFT OUTER JOIN transl_return_detail rdh  WITH (NOLOCK)
                ON tl.transaction_id = rdh.transaction_id
                AND 0 = rdh.line_id  
             LEFT OUTER JOIN transl_stock_control_detail o  WITH (NOLOCK)
                ON tt.store_no = o.store_no
                AND tt.register_no = o.register_no
                AND tt.entry_date_time = o.entry_date_time
                AND tt.transaction_series = o.transaction_series
                AND tt.transaction_no = o.transaction_no
                AND tl.line_id = o.line_id  
                AND o.display_def_id = 31
                AND o.count_date IS NOT NULL
                AND o.count_date < dateadd(dd, 1, getdate())
             LEFT OUTER JOIN transl_stock_control_detail ol  WITH (NOLOCK)
                ON tt.store_no = ol.store_no
                AND tt.register_no = ol.register_no
                AND tt.entry_date_time = ol.entry_date_time
                AND tt.transaction_series = ol.transaction_series
                AND tt.transaction_no = ol.transaction_no
                AND tll.linked_line_id = ol.line_id  
                AND ol.display_def_id = 31
                AND ol.count_date IS NOT NULL
             LEFT OUTER JOIN transl_stock_control_detail oh  WITH (NOLOCK)
                ON tt.store_no = oh.store_no
                AND tt.register_no = oh.register_no
                AND tt.entry_date_time = oh.entry_date_time
                AND tt.transaction_series = oh.transaction_series
                AND tt.transaction_no = oh.transaction_no
                AND 0 = oh.line_id  
                AND oh.display_def_id = 31
                AND oh.count_date IS NOT NULL
             LEFT OUTER JOIN ORG_CHN f  WITH (NOLOCK)
                ON md.fulfillment_store_no = f.ORG_CHN_NUM
             LEFT OUTER JOIN (SELECT DISTINCT ai1.transaction_category, 
                                     ai1.line_object, 
                                     ai1.line_action
                                FROM interface_applicability ai1
                                     INNER JOIN interface_applicability ai2
                                        ON ai2.interface_id = 12
                                       AND ai1.transaction_category = ai2.transaction_category
           AND ai1.line_object = ai2.line_object
                                       AND ai2.line_action in (201, 211, 142, 147, 90, 97, 147, 197, 198)
                                       AND (   (ai1.line_action in (7, 8) AND ai2.line_action in (142, 90))
                                            OR (ai1.line_action in (95, 96) AND ai2.line_action in (147, 97))
                                            OR (ai1.line_action in (101, 102) AND ai2.line_action = 201)
                                            OR (ai1.line_action in (111, 112) AND ai2.line_action = 211)
                                            OR (ai1.line_action in (191, 194) AND ai2.line_action = 197)
                                            OR (ai1.line_action in (192, 195) AND ai2.line_action = 198))
                               WHERE ai1.interface_id = 12
                                 AND ai1.line_action in (7, 8, 95, 96,101, 102, 111, 112, 191, 194, 192, 195) ) ex  --order and layaway creation to be ignore if pickup/delivery also set to feed to avoid double-counting
                ON tt.transaction_category = ex.transaction_category                
                AND tl.line_object = ex.line_object
                AND tl.line_action = ex.line_action
    GROUP BY tl.transaction_id,
	    tl.line_id,
	     tt.store_no,
             tt.transaction_date,
	     tl.line_object_type,
	     tl.line_object,
	     tl.gross_line_amount,
	     tl.pos_discount_amount,
	     ((SIGN(1 + tl.db_cr_none) * 2) - 1) * tl.voiding_reversal_flag,
	     tl.db_cr_none * -1 * tl.voiding_reversal_flag,
	     tt.store_tax_jurisdiction,
	     (1 - SIGN(ABS(tl.line_object_type - 5 ))) * ((1-SIGN(ABS(tl.line_action - 15))) + (1-SIGN(ABS(tl.line_action - 16))))
	     + (1 - SIGN(ABS(tl.line_object_type - 7 ))),
	     tt.header_override_flag, -- def 74673
	     tt.all_tax_override_flag,  -- def 74673
	     COALESCE(md.units, 1),
	     CASE WHEN ex.line_action IS NOT NULL THEN 0 ELSE 1 END,
	     tt.transaction_no,
	     tt.register_no,
	     tt.entry_date_time,
	     tt.transaction_series,
	     CASE WHEN @tax_allocation_by_refno = 1 THEN tl.reference_type ELSE 0 END,
             CASE WHEN @tax_allocation_by_refno = 1 THEN COALESCE(tl.reference_no, '0') ELSE '0' END;
    ELSE 
      INSERT #tax_post_main(
	     transaction_id,
	     line_id,
	     store_no,
	     transaction_date,
	     line_object_type,
	     line_object,
	     class_code,
	     gross_line_amount,
	     discount_amount,
	     amount_sign,
	     gl_effect,
	     store_tax_jurisdiction,
	     tax_jurisdiction,
	     style_reference_id,
	     sku_id,
	     upc_lookup_division,
	     return_from_store,
	     return_from_date,
	     override_tax_category,
	     tax_paid_flag,
	     header_override_flag,
	     all_tax_override_flag,
      	     units,
      	     track_tax,
	     transaction_no,
	     register_no,
	     entry_date_time,
	     transaction_series,
	     reference_type,
	     reference_no,
	     upc_no)
      SELECT
             tl.transaction_id,
	     tl.line_id,
	     tt.store_no,
             tt.transaction_date,
	     tl.line_object_type,
	     tl.line_object,
	     0, -- class_code
	     tl.gross_line_amount,
	     tl.pos_discount_amount,
	     ((SIGN(1 + tl.db_cr_none) * 2) - 1) * tl.voiding_reversal_flag, -- amount_sign
	     tl.db_cr_none * -1 * tl.voiding_reversal_flag, -- gl_effect
	     tt.store_tax_jurisdiction,
	     MAX(COALESCE(tod.exception_tax_jurisdiction, todl.exception_tax_jurisdiction, tt.tod_tax_jurisdiction, f.TAX_JRSDCTN_CODE, tt.store_tax_jurisdiction)), -- tax_jurisdiction def 74673
	     0, -- style_reference_id
	     0, -- sku_id
	     0, -- upc_lookup_division
	     CASE WHEN MAX(COALESCE(tod.exception_tax_jurisdiction, todl.exception_tax_jurisdiction, tt.tod_tax_jurisdiction)) IS NULL
	          THEN MAX(COALESCE(f.ORG_CHN_NUM, rd.return_from_store, rdl.return_from_store, rdh.return_from_store))
	          ELSE NULL
	     END,
	     CASE WHEN MAX(COALESCE(o.count_date, ol.count_date, oh.count_date, rd.return_from_date, rdl.return_from_date, rdh.return_from_date)) > dateadd(dd, 1, getdate())
	          THEN NULL
	          ELSE MAX(COALESCE(o.count_date, ol.count_date, oh.count_date, rd.return_from_date, rdl.return_from_date, rdh.return_from_date))
	     END,
	     0, -- override_tax_category
	     (1 - SIGN(ABS(tl.line_object_type - 5 ))) *
	      ((1-SIGN(ABS(tl.line_action - 15))) + (1-SIGN(ABS(tl.line_action - 16))) )
	      + (1 - SIGN(ABS(tl.line_object_type - 7 ))), -- tax_paid_flag
	     COALESCE(tt.header_override_flag, (1 - SIGN (MIN(tod.line_id))), (3 - SIGN(MIN(todl.line_id)))), -- header_override_flag  -- def 74673
	     COALESCE(tt.all_tax_override_flag, (1 - SIGN (MIN(COALESCE(tod.tax_level, todl.tax_level))))), -- all_tax_override_flag  -- def 74673
	     COALESCE(md.units, 1),
	     CASE WHEN @include_pickup = 1 AND tl.line_action IN ( 7, 95, 101, 111) THEN 0 ELSE 1 END,
	     tt.transaction_no,
	     tt.register_no,
	     tt.entry_date_time,
	     tt.transaction_series,
	     CASE WHEN @tax_allocation_by_refno = 1 THEN tl.reference_type ELSE 0 END,
             CASE WHEN @tax_allocation_by_refno = 1 THEN COALESCE(tl.reference_no, '0') ELSE '0' END,
             0 --upc_no
        FROM #tax_transactions tt
             INNER JOIN transl_transaction_line tl
                  ON tt.transaction_id = tl.transaction_id
                  AND tl.line_object_type IN (1, 2, 5, 7 * @include_expense)   /* tax type*/
                  AND tl.line_action not in (3, 4, 9, 10, 78, 79, 200, 203, 204, 210, 213, 214, 215, 223, 224, 225, 226, 227, 228, 191, 192, 193, 194, 195, 196, 32, 40, 41, 42, 43, 44, 45, 67, 74, 85, 100, 171, 172)
                  AND (tl.line_action * @include_pickup) NOT IN ( 8, 96, 102, 112)
                  AND (tl.line_action * (1 - @include_pickup)) NOT IN ( 90, 97, 98, 99, 201, 202, 211, 212, 142, 147)
                  AND tl.line_void_flag = 0
             LEFT OUTER JOIN work_merchandise_edit md   
                  ON tl.transaction_id = md.transaction_id
                  AND tl.line_id = md.line_id  
             LEFT OUTER JOIN transl_transaction_line_link tll  WITH (NOLOCK)
                ON tl.transaction_id = tll.transaction_id
                AND tl.line_id = tll.line_id  
             LEFT OUTER JOIN transl_tax_override_detail tod 
                ON tl.transaction_id = tod.transaction_id
                AND tl.line_id = tod.line_id
             LEFT OUTER JOIN transl_tax_override_detail todl WITH (NOLOCK)
                ON tll.transaction_id = todl.transaction_id
                AND tll.linked_line_id = todl.line_id
             LEFT OUTER JOIN transl_return_detail rd WITH (NOLOCK) 
                ON tl.transaction_id = rd.transaction_id
                AND tl.line_id = rd.line_id  
             LEFT OUTER JOIN transl_return_detail rdl  WITH (NOLOCK)
                 ON tll.transaction_id = rdl.transaction_id
                AND tll.linked_line_id = rdl.line_id  
             LEFT OUTER JOIN transl_return_detail rdh  WITH (NOLOCK)
                ON tl.transaction_id = rdh.transaction_id
                AND 0 = rdh.line_id  
             LEFT OUTER JOIN transl_stock_control_detail o  WITH (NOLOCK)
                ON tt.store_no = o.store_no
                AND tt.register_no = o.register_no
                AND tt.entry_date_time = o.entry_date_time
                AND tt.transaction_series = o.transaction_series
                AND tt.transaction_no = o.transaction_no
                AND tl.line_id = o.line_id  
                AND o.display_def_id = 31
                AND o.count_date IS NOT NULL
                AND o.count_date < dateadd(dd, 1, getdate())
             LEFT OUTER JOIN transl_stock_control_detail ol  WITH (NOLOCK)
                ON tt.store_no = ol.store_no
                AND tt.register_no = ol.register_no
                AND tt.entry_date_time = ol.entry_date_time
                AND tt.transaction_series = ol.transaction_series
       AND tt.transaction_no = ol.transaction_no
                AND tll.linked_line_id = ol.line_id  
                AND ol.display_def_id = 31
                AND ol.count_date IS NOT NULL
             LEFT OUTER JOIN transl_stock_control_detail oh  WITH (NOLOCK)
                ON tt.store_no = oh.store_no
                AND tt.register_no = oh.register_no
                AND tt.entry_date_time = oh.entry_date_time
                AND tt.transaction_series = oh.transaction_series
                AND tt.transaction_no = oh.transaction_no
                AND 0 = oh.line_id  
                AND oh.display_def_id = 31
                AND oh.count_date IS NOT NULL
             LEFT OUTER JOIN ORG_CHN f 
                ON md.fulfillment_store_no = f.ORG_CHN_NUM
    GROUP BY tl.transaction_id,
	     tl.line_id,
	     tt.store_no,
             tt.transaction_date,
	     tl.line_object_type,
	     tl.line_object,
	     tl.gross_line_amount,
	     tl.pos_discount_amount,
	     ((SIGN(1 + tl.db_cr_none) * 2) - 1) * tl.voiding_reversal_flag,
	     tl.db_cr_none * -1 * tl.voiding_reversal_flag,
	     tt.store_tax_jurisdiction,
	     (1 - SIGN(ABS(tl.line_object_type - 5 ))) * ((1-SIGN(ABS(tl.line_action - 15))) + (1-SIGN(ABS(tl.line_action - 16))))
	     + (1 - SIGN(ABS(tl.line_object_type - 7 ))),
	     tt.header_override_flag, -- def 74673
	     tt.all_tax_override_flag, -- def 74673
	     COALESCE(md.units, 1),
             CASE WHEN @include_pickup = 1 AND tl.line_action IN ( 7, 95, 101, 111) THEN 0 ELSE 1 END,
	     tt.transaction_no,
	     tt.register_no,
	     tt.entry_date_time,
	     tt.transaction_series, 
	     CASE WHEN @tax_allocation_by_refno = 1 THEN tl.reference_type ELSE 0 END,
             CASE WHEN @tax_allocation_by_refno = 1 THEN COALESCE(tl.reference_no, '0') ELSE '0' END;

END; -- else of if (@class_exception_flag = 1 OR @style_exception_flag = 1  OR @sku_exception_flag = 1 OR @item_group_exception_flag = 1)

SELECT @rows = @@rowcount;

IF @rows = 0
BEGIN
  DROP TABLE #tax_post_main;

  RETURN;
END; -- If @rows = 0

IF @unapplied_discounts_exist = 1
BEGIN
        SELECT @errmsg = 'Failed to update #tax_post_main (discount_amount).',
             @object_name = '#tax_post_main',
             @operation_name = 'UPDATE';
    UPDATE #tax_post_main
       SET discount_amount = (SELECT SUM(ABS(dd.pos_discount_amount - dd.pos_discount_amount_adj) * dd.discount_amount_sign)
                   FROM transl_discount_detail dd WITH (NOLOCK)
                              WHERE tpm.transaction_id = dd.transaction_id  
                              AND tpm.line_id = dd.line_id)
      FROM #tax_post_main tpm, transl_discount_detail tdd WITH (NOLOCK)
     WHERE tpm.line_object_type IN (1,2)
     AND tpm.transaction_id = tdd.transaction_id  
     AND tpm.line_id = tdd.line_id;
END; -- if @unapplied_discounts_exist = 1

/* For returns, use tax jurisdiction of return_from_store if no tax_override is present
   override_tax_category is used later to set the tax_category properly. */
  SELECT @errmsg = 'Failed to update #tax_post_main (tax_jurisdiction).',
         @object_name = '#tax_post_main',
         @operation_name = 'UPDATE';
UPDATE #tax_post_main
   SET tax_jurisdiction = ssa.TAX_JRSDCTN_CODE,
       override_tax_category = (FLOOR(override_tax_category / 100) * 100) + 2 -- tax_override
  FROM #tax_post_main tpm, ORG_CHN ssa
 WHERE tpm.store_no != tpm.return_from_store
   AND tpm.return_from_store = ssa.ORG_CHN_NUM
   AND tpm.tax_jurisdiction != ssa.TAX_JRSDCTN_CODE
   AND tpm.store_tax_jurisdiction = tpm.tax_jurisdiction  --don't override if already set by tod or fulfillment store
   AND (tpm.override_tax_category % 100) = 0; -- modulus

  SELECT @errmsg = 'Failed to update #tax_post_main (override_tax_category).';
UPDATE #tax_post_main
   SET override_tax_category = (FLOOR(override_tax_category / 100) * 100) + 2 -- tax_override
 WHERE store_tax_jurisdiction <> tax_jurisdiction 
   AND (override_tax_category % 100) = 0; -- modulus

/* Set tax_jurisdiction based on send-to customer */
    SELECT @errmsg = 'Failed to update #tax_post_main from header tax_jurisdiction.';
UPDATE #tax_post_main
   SET tax_jurisdiction = tj.tax_jurisdiction,
       override_tax_category = 1 -- send
  FROM #tax_post_main tt , transl_customer c WITH (NOLOCK), tax_jurisdiction tj
 WHERE tt.transaction_no = c.transaction_no
   AND tt.entry_date_time = c.entry_date_time
   AND tt.store_no = c.store_no
   AND tt.register_no = c.register_no
   AND tt.transaction_series = c.transaction_series
   AND 0 = c.line_id
   AND c.customer_role = 2    
   AND c.pos_tax_jurisdiction_code = tj.pos_tax_jurisdiction_code
   AND tj.pos_tax_jurisdiction_code IS NOT NULL --
   AND tt.tax_jurisdiction != tj.tax_jurisdiction;

-- repeat using transl_transaction_line_link
      SELECT @errmsg = 'Failed to update #tax_post_main from tax_jurisdiction via transaction line link.';
UPDATE #tax_post_main
   SET tax_jurisdiction = tj.tax_jurisdiction,
       override_tax_category = 1 -- send
  FROM #tax_post_main tt ,
       transl_transaction_line_link k WITH (NOLOCK), 
       transl_customer c WITH (NOLOCK),
       tax_jurisdiction tj
 WHERE tt.transaction_no = k.transaction_no
   AND tt.entry_date_time = k.entry_date_time
   AND tt.store_no = k.store_no
   AND tt.register_no = k.register_no
   AND tt.transaction_series = k.transaction_series
   AND tt.line_id = k.line_id 
   AND k.transaction_no = c.transaction_no
   AND k.entry_date_time = c.entry_date_time
   AND k.store_no = c.store_no
   AND k.register_no = c.register_no
   AND k.transaction_series = c.transaction_series
   AND k.linked_line_id = c.line_id 
   AND c.customer_role = 2    
   AND c.pos_tax_jurisdiction_code = tj.pos_tax_jurisdiction_code
   AND tj.pos_tax_jurisdiction_code IS NOT NULL --
   AND tt.tax_jurisdiction != tj.tax_jurisdiction;

-- repeat using direct line attachment
      SELECT @errmsg = 'Failed to update #tax_post_main from tax_jurisdiction.';
UPDATE #tax_post_main
   SET tax_jurisdiction = tj.tax_jurisdiction,
       override_tax_category = 1 -- send
  FROM #tax_post_main tt , transl_customer c WITH (NOLOCK), tax_jurisdiction tj
 WHERE tt.transaction_no = c.transaction_no
   AND tt.entry_date_time = c.entry_date_time
   AND tt.store_no = c.store_no
  AND tt.register_no = c.register_no
   AND tt.transaction_series = c.transaction_series
   AND tt.line_id = c.line_id
   AND c.customer_role = 2    
   AND c.pos_tax_jurisdiction_code = tj.pos_tax_jurisdiction_code
   AND tj.pos_tax_jurisdiction_code IS NOT NULL --
   AND tt.tax_jurisdiction != tj.tax_jurisdiction;

    SELECT @errmsg = 'Failed to update #tax_post_main from header tax_jurisdiction_post_code.';
UPDATE #tax_post_main
   SET tax_jurisdiction = tjp.tax_jurisdiction,
       override_tax_category = 1
  FROM #tax_post_main tt, transl_customer c WITH (NOLOCK), tax_jurisdiction_post_code tjp
 WHERE tt.transaction_no = c.transaction_no
   AND tt.entry_date_time = c.entry_date_time
   AND tt.store_no = c.store_no
   AND tt.register_no = c.register_no
   AND tt.transaction_series = c.transaction_series
   AND 0 = c.line_id
   AND c.customer_role = 2
   AND c.post_code >= tjp.from_post_code
   AND c.post_code <= tjp.to_post_code
   AND tt.tax_jurisdiction != tjp.tax_jurisdiction
   AND (c.pos_tax_jurisdiction_code IS NULL 
        OR c.pos_tax_jurisdiction_code 
         NOT IN (SELECT tj.pos_tax_jurisdiction_code
                FROM tax_jurisdiction tj
                WHERE tj.pos_tax_jurisdiction_code IS NOT NULL));

-- repeat using transl_transaction_line_link
     SELECT @errmsg = 'Failed to update #tax_post_main from tax_jurisdiction_post_code via transaction line link.';
UPDATE #tax_post_main
   SET tax_jurisdiction = tjp.tax_jurisdiction,
       override_tax_category = 1
  FROM #tax_post_main tt,
       transl_customer c WITH (NOLOCK),
       transl_transaction_line_link k WITH (NOLOCK),
       tax_jurisdiction_post_code tjp
 WHERE tt.transaction_no = k.transaction_no
   AND tt.entry_date_time = k.entry_date_time
   AND tt.store_no = k.store_no
   AND tt.register_no = k.register_no
   AND tt.transaction_series = k.transaction_series
   AND tt.line_id = k.line_id 
   AND k.transaction_no = c.transaction_no
   AND k.entry_date_time = c.entry_date_time
   AND k.store_no = c.store_no
   AND k.register_no = c.register_no
   AND k.transaction_series = c.transaction_series
   AND k.linked_line_id = c.line_id 
   AND c.customer_role = 2
   AND c.post_code >= tjp.from_post_code
   AND c.post_code <= tjp.to_post_code
   AND (c.pos_tax_jurisdiction_code IS NULL                      
        OR c.pos_tax_jurisdiction_code NOT IN (SELECT tj.pos_tax_jurisdiction_code
                                                 FROM tax_jurisdiction tj
                                                WHERE tj.pos_tax_jurisdiction_code IS NOT NULL))
   AND tt.tax_jurisdiction != tjp.tax_jurisdiction;
     
--repeat using direct line attachment
    SELECT @errmsg = 'Failed to update #tax_post_main from tax_jurisdiction_post_code.';
UPDATE #tax_post_main
   SET tax_jurisdiction = tjp.tax_jurisdiction,
       override_tax_category = 1
  FROM #tax_post_main tt, transl_customer c WITH (NOLOCK), tax_jurisdiction_post_code tjp
 WHERE tt.transaction_no = c.transaction_no
   AND tt.entry_date_time = c.entry_date_time
   AND tt.store_no = c.store_no
   AND tt.register_no = c.register_no
   AND tt.transaction_series = c.transaction_series
   AND tt.line_id = c.line_id
   AND c.customer_role = 2
   AND c.post_code >= tjp.from_post_code
   AND c.post_code <= tjp.to_post_code
   AND (c.pos_tax_jurisdiction_code IS NULL                      
        OR c.pos_tax_jurisdiction_code NOT IN (SELECT tj.pos_tax_jurisdiction_code
                                                 FROM tax_jurisdiction tj
                                                WHERE tj.pos_tax_jurisdiction_code IS NOT NULL))
   AND tt.tax_jurisdiction != tjp.tax_jurisdiction;

    SELECT @errmsg = 'Unable to delete work_tax_exception_jur table from #tax_post_main.',
         @object_name = 'work_tax_exception_jur',
         @operation_name = 'DELETE';
DELETE work_tax_exception_jur
  FROM #tax_post_main tpm WITH (NOLOCK), work_tax_exception_jur wt
 WHERE tpm.transaction_id = wt.transaction_id 
   AND tpm.line_id = wt.line_id;

    SELECT @errmsg = 'Unable to insert work_tax_exception_jur table.',
      @object_name = 'work_tax_exception_jur',
         @operation_name = 'INSERT';
INSERT work_tax_exception_jur(
  transaction_id,
  line_id,
  tax_jurisdiction)
SELECT
  transaction_id,
  line_id,
  tax_jurisdiction
FROM #tax_post_main WITH (NOLOCK)
WHERE tax_jurisdiction != store_tax_jurisdiction;

IF @exception_jurisdiction_check = 1 OR @tax_default_check = 1
BEGIN
     SELECT @errmsg = 'Unable to execute edit_verify_tax_jur_$sp.',
           @object_name = 'edit_verify_tax_jur_$sp',
           @operation_name = 'EXECUTE';
  EXEC edit_verify_tax_jur_$sp @exception_jurisdiction_check,
       @tax_default_check, @function_no, @edit_process_no, @errmsg OUTPUT;
END; -- if @exception_jurisdiction_check = 1 OR @tax_default_check = 1

   SELECT @errmsg = 'Unable to delete table work_tax_detail.',
         @object_name = 'work_tax_detail',
         @operation_name = 'DELETE';
DELETE FROM work_tax_detail
 WHERE process_id = @process_id;

    SELECT @errmsg = 'Failed to insert work_tax_detail.',
         @object_name = 'work_tax_detail',
         @operation_name = 'INSERT';
INSERT INTO work_tax_detail(
 process_id,
         transaction_id,
	 line_id,
	 transaction_date,
	 store_no,
	 amount,
	 tax_sign,
	 gl_effect,
	 line_object,
	 line_object_type,
	 tax_level,
	 tax_jurisdiction,
	 tax_category,
	 tax_rate_code,
	 combined_tax_rate,
	 threshold_amount,
	 tax_on_threshold_excess,
	 tax_on_full_amount,
	 taxable_merchandise_amount,
	 taxable_fee_amount,
	 taxable_expense_amount,
	 nontaxable_merchandise_amount,
	 nontaxable_fee_amount,
	 tax_amount_collected,
	 tax_amount_expected,
	 tax_amount_paid,
	 tax_on_tax_level,
	 tax_on_tax_rate_code,
	 tax_on_combined_rate,
	 taxable,
	 class_code,
	 style_reference_id, 
	 sku_id,
	 upc_lookup_division,
         below_threshold_combined_rate,
         return_from_date,
         override_tax_category,
         tax_paid_flag,
         header_override_flag,
         item_tax_strip_flag,
         all_tax_override_flag,
         units,
         track_tax,
         max_applied_by_line_id, --114269
         reference_type,
         reference_no,
         fulfillment_store_no,
         upc_no) 
SELECT
	 @process_id,
	 tpm.transaction_id,
	 tpm.line_id,
	 tpm.transaction_date,
	 tpm.store_no,
	 gross_line_amount - discount_amount,
	 amount_sign,
	 gl_effect,
	 tpm.line_object,
	 line_object_type,
	 COALESCE(td.tax_level, tl.tax_level),
	 tpm.tax_jurisdiction,
	 COALESCE(COALESCE(tod.tax_category, todl.tax_category) + (FLOOR(tpm.override_tax_category / 100) * 100), tpm.override_tax_category),
         COALESCE(td.tax_rate_code, 0),
	 0,
	 0,
	 0,
	 1,
	 0,
	 0,
	 0,
	 0,
	 0,
	 0,
	 0,
	 0,
	 0,
	 0,
	 0,
         COALESCE(CASE WHEN tod.taxable not in (0,1) THEN NULL ELSE tod.taxable END, CASE WHEN todl.taxable not in (0,1) THEN NULL ELSE todl.taxable END),  --compensate for UI bug
	 tpm.class_code,
	 tpm.style_reference_id, 
	 tpm.sku_id,
	 tpm.upc_lookup_division,
	 0,
         tpm.return_from_date,
         COALESCE(COALESCE(tod.tax_category, todl.tax_category) + (FLOOR(tpm.override_tax_category / 100) * 100), tpm.override_tax_category),
         tax_paid_flag,
         header_override_flag,
         0,
         all_tax_override_flag,
         CASE WHEN tpm.units = 0 THEN 1 ELSE ABS(tpm.units) END,
         tpm.track_tax, 
         CASE WHEN tpm.line_object_type = 5 THEN tpm.line_id ELSE NULL END, --114269 
         tpm.reference_type,
         tpm.reference_no,
         COALESCE(tpm.return_from_store, tpm.store_no),
         tpm.upc_no
  FROM #tax_post_main tpm WITH (NOLOCK)
    LEFT JOIN  tax_default td
      ON tpm.tax_jurisdiction = td.tax_jurisdiction
      AND tpm.line_object = td.line_object
      AND tpm.transaction_date >= td.effective_from_date
      AND (tpm.transaction_date <= td.effective_until_date OR td.effective_until_date IS NULL)
    LEFT JOIN transl_tax_override_detail tod  WITH (NOLOCK)   --note this join will fail for link lines since line_id will never = -1
      ON tpm.transaction_id = tod.transaction_id
      AND (tpm.line_id * (1 - header_override_flag)) = tod.line_id  
      AND (td.tax_level * (1 - all_tax_override_flag)) = tod.tax_level
    LEFT JOIN transl_tax_override_detail todl WITH (NOLOCK) --note this join will only happen for link lines
      ON tpm.transaction_id = todl.transaction_id
      AND tpm.header_override_flag = 2
      AND todl.line_id IN (SELECT linked_line_id 
                             FROM transl_transaction_line_link ll
                            WHERE tpm.transaction_id = ll.transaction_id
                              AND tpm.line_id = ll.line_id)
      AND (td.tax_level * (1 - all_tax_override_flag)) = todl.tax_level
    LEFT JOIN tax_level tl ON (tpm.line_object = tl.line_object)
 WHERE COALESCE(td.tax_level, tl.tax_level) IS NOT NULL;

    SELECT @errmsg = 'Failed to delete work_tax_detail from work_interface_reject_edit.',
         @object_name = 'work_tax_detail',
         @operation_name = 'DELETE';
DELETE work_tax_detail
  FROM work_tax_detail wt, work_interface_reject_edit ir WITH (NOLOCK)
 WHERE wt.process_id = @process_id
   AND wt.transaction_id = ir.transaction_id
   AND wt.line_id = ir.line_id
   AND ir.if_reject_reason IN (7,8);

/* drop table to release space in tempdb */
  SELECT @errmsg = 'Failed to drop temp table #tax_post_main.',
         @object_name = '#tax_post_main',
         @operation_name = 'DROP';
DROP TABLE #tax_post_main;


RETURN;


business_error:   /* Business Rule handler. */

	SELECT @errmsg2 = @errmsg;

	/* Could include similar cleanup code to system error trap when needed (example is from move_store_$sp).
	   However, could also exclude the cleanup code here since the outer system error catch should fire again after the exec below. */

	EXEC common_error_handling_$sp @function_no, @errno, @errmsg, 0, @message_id, 
	  @process_name, @object_name, @operation_name, 1, @edit_process_no;
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

	EXEC common_error_handling_$sp @function_no, @errno, @errmsg, 0, @message_id, 
	  @process_name, @object_name, @operation_name, 1, @edit_process_no;

	RETURN;
END CATCH;
```

