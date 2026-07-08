# dbo.oim_store_ship_rcpt_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.oim_store_ship_rcpt_$sp"]
    EMPLY(["EMPLY"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    if_stock_control_detail(["if_stock_control_detail"]) --> SP
    if_transaction_line(["if_transaction_line"]) --> SP
    oim_store_ship_rcpt(["oim_store_ship_rcpt"]) --> SP
    oim_store_ship_rcpt_dtl(["oim_store_ship_rcpt_dtl"]) --> SP
    work_oim_entity(["work_oim_entity"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| EMPLY |
| common_error_handling_$sp |
| if_stock_control_detail |
| if_transaction_line |
| oim_store_ship_rcpt |
| oim_store_ship_rcpt_dtl |
| work_oim_entity |

## Stored Procedure Code

```sql
create proc [dbo].[oim_store_ship_rcpt_$sp] 

AS

/*
Proc name: oim_store_ship_rcpt_$sp
     Desc: To post Store Shipment Receipt details.
           Called by mew_stock_export_$sp
 
HISTORY:
Date     Name             Defect  Desc
Oct25,06 Phu              77931   Fix outer join for SQL 2005 Mode 90.
Sep21,06 Paul             76719   apply 75320, 1-34YHBK to SA5
May27,05 Paul             DV-1254 apply 54763 to SA5 
Apr28.04 Brett C          DV-1071 change employee table to EMPLY
Sep21,06 Paul             75320   avoid possible concat null problem
Sep08,05 ShuZ          1-34YHBK   Only allow line_sequence > 0 to be populated
May25,05 Daphna           54763   Populate weight and unit_weight_code 
Sep09,03 Phu              15801   Initial development

*/

DECLARE
  @errmsg                       nvarchar(255),
  @errno                        int,
  @exit_loop                    tinyint,
  @message_id                   int,
  @object_name                  nvarchar(255),
  @operation_name               nvarchar(100),
  @process_name                 nvarchar(100),
  @process_no                   int,
  @rows                         int

SELECT @message_id = 201068,
       @process_name = 'oim_store_ship_rcpt_$sp',
       @process_no = 209,
       @exit_loop = 0

WHILE @exit_loop = 0
BEGIN
  INSERT INTO oim_store_ship_rcpt (
    oim_store_ship_rcpt_id, document_no, receive_date,
    performed_by, line_id)
  SELECT
    w.transaction_id, w.reference_no, ISNULL(w.count_date, w.transaction_date),
    convert(nvarchar, w.cashier_no) + ' ' + ISNULL(LTRIM(e.FRST_NAME + ' ' + e.LAST_NAME),' '), w.min_line_id
  FROM work_oim_entity w LEFT JOIN EMPLY e ON (w.cashier_no = e.EMPLY_NUM)
  WHERE w.entity_code = 140

  SELECT @errno = @@error
  IF @errno = 2601  -- duplicate error on insert
  BEGIN 
    DELETE oim_store_ship_rcpt
    FROM oim_store_ship_rcpt oim, work_oim_entity w
    WHERE w.entity_code = 140
    AND w.transaction_id = oim.oim_store_ship_rcpt_id

    SELECT @errno = @@error
    IF @errno <> 0
    BEGIN
      SELECT @errmsg = 'Unable to delete duplicate key in oim_store_ship_rcpt',
             @object_name = 'oim_store_ship_rcpt',
             @operation_name = 'DELETE'
      GOTO error
    END

    DELETE oim_store_ship_rcpt_dtl
    FROM oim_store_ship_rcpt_dtl oim, work_oim_entity w
    WHERE w.entity_code = 140
    AND w.transaction_id = oim.oim_store_ship_rcpt_id

    SELECT @errno = @@error
    IF @errno <> 0
    BEGIN
      SELECT @errmsg = 'Unable to delete duplicate key in oim_store_ship_rcpt_dtl',
             @object_name = 'oim_store_ship_rcpt_dtl',
             @operation_name = 'DELETE'
      GOTO error
    END
  END -- @errno = 2601 duplicate
  ELSE
  IF @errno <> 0
  BEGIN
    SELECT @errmsg = 'Unable to insert oim_store_ship_rcpt',
           @object_name = 'oim_store_ship_rcpt',
           @operation_name = 'INSERT'
    GOTO error
  END
  ELSE
    SELECT @exit_loop = 1
END -- while @exit_loop = 0

UPDATE oim_store_ship_rcpt
SET weight = s.units,
    unit_weight_code = SUBSTRING(s.imrd, 1, 10)    
FROM oim_store_ship_rcpt oim, work_oim_entity w, if_stock_control_detail s, if_transaction_line l
WHERE w.entity_code = 140
AND w.if_entry_no = s.if_entry_no
AND s.display_def_id = 37 -- shipment info
AND s.if_entry_no = l.if_entry_no
AND s.line_id = l.line_id
AND l.line_void_flag = 0
AND l.line_sequence > 0
AND w.transaction_id = oim.oim_store_ship_rcpt_id

SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Unable to set weight, unit_weight_code',
         @object_name = 'oim_store_ship_rcpt',
         @operation_name = 'UPDATE'
  GOTO error
END

INSERT INTO oim_store_ship_rcpt_dtl (
  oim_store_ship_rcpt_id, sku_id, carton_no,
  units_received, force_flag, line_id)
SELECT
  w.transaction_id, s.sku_id, l.reference_no,
  SUM(CONVERT(INT, s.units * l.voiding_reversal_flag)), MAX(w.if_rejection_rules_overriden), MIN(l.line_id)
FROM work_oim_entity w, if_transaction_line l, if_stock_control_detail s
WHERE w.entity_code = 140 
AND w.if_entry_no = s.if_entry_no
AND s.display_def_id = 36 -- stock item detail
AND s.if_entry_no = l.if_entry_no
AND s.line_id = l.line_id
AND l.line_void_flag = 0
AND l.line_sequence > 0
GROUP BY w.transaction_id, s.sku_id, l.reference_no

SELECT @errno = @@error
IF @errno <> 0
BEGIN
  SELECT @errmsg = 'Unable to insert oim_store_ship_rcpt_dtl',
         @object_name = 'oim_store_ship_rcpt_dtl',
         @operation_name = 'INSERT'
  GOTO error
END


RETURN


error:

  EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, @process_name, @object_name, @operation_name, 1
  RETURN
```

