# dbo.transl_payroll_detail_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.transl_payroll_detail_$sp"]
    ORG_CHN(["ORG_CHN"]) --> SP
    auditworks_parameter(["auditworks_parameter"]) --> SP
    code_description(["code_description"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    language_dependent_description(["language_dependent_description"]) --> SP
    language_identification(["language_identification"]) --> SP
    transl_payroll_detail(["transl_payroll_detail"]) --> SP
    work_config_pos_code_vw(["work_config_pos_code_vw"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_CHN |
| auditworks_parameter |
| code_description |
| common_error_handling_$sp |
| language_dependent_description |
| language_identification |
| transl_payroll_detail |
| work_config_pos_code_vw |

## Stored Procedure Code

```sql
create proc dbo.transl_payroll_detail_$sp 
@process_id		binary(16),
@process_no		smallint,
@lookup_pass		tinyint,
@request_id             binary(16),
@auto_config_required   tinyint OUTPUT,
@errmsg                 nvarchar(255) OUTPUT


AS

/* 
PROC NAME: transl_payroll_detail_$sp
     DESC: This proc will try to replace any payroll_entry_type of -3 with code found in code_description 
           for code_type 29. If code is not found, a new one will be created by transl_auto_configure_$sp.
           This proc is called from transl_pre_processing and runs on each peripheral database. 
           
           *************************** MUST BE SCRIPTED WITH SET ANSI_NULLS ON ***************************
     
 HISTORY: 
Date      Name          Def# Desc
Feb01,13 Vicci        141488 Log identification of the transaction that was the source of the auto-config to the work_config_pos_code_vw.
Feb17,12 Vicci        133087 Remove references to CRDM datatypes from procs installed in multi-stream S/A databases where CRDM is not installed.
Oct25,06  Phu          77931 Fix outer join for SQL 2005 Mode 90.
May12,05  David      DV-1202 Author.

*/

DECLARE  
  @base_language_id             smallint,  
  @desc_update_count            int,
  @errno                        int,
  @fixed_count                  int,
  @issue_count                  int,
  @max_retry                    int,
  @message_id			int,
  @object_name			nvarchar(255),
  @operation_name		nvarchar(100),
  @process_name			nvarchar(100),
  @rows                         int,
  @try_no                       int,
  @wait_time                    nchar(8)

SELECT 
       @process_name = 'transl_payroll_detail_$sp',
       @message_id   = 201068,       
       @fixed_count = 0,
       @issue_count = 0,
       @desc_update_count = 0,
       @try_no = 0,
       @max_retry = 10,
       @wait_time = '00:00:10'
       
      
-- Find out how many rows exist with payroll_entry_type = -3
SELECT @issue_count = count(*)
  FROM transl_payroll_detail
 WHERE payroll_entry_type = -3
   AND lookup_pos_code IS NOT NULL

SELECT @errno = @@error
IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to select the issue_count.',
           @object_name = 'transl_payroll_detail',
	   @operation_name = 'SELECT'
    GOTO error
  END

-- There is now new code and description change (There will be no description changes if pos_descriptions are null)
IF @issue_count = 0 
AND NOT EXISTS (SELECT 1 FROM transl_payroll_detail
                 WHERE pos_description IS NOT NULL)  
  RETURN

                 
/* Get the count and also update those rows that already have S/A configuration. This also includes the rows that their 
   description changed at POS*/
UPDATE transl_payroll_detail
   SET payroll_entry_type = code
  FROM transl_payroll_detail t, code_description c
 WHERE t.payroll_entry_type = -3
   AND t.lookup_pos_code IS NOT NULL
   AND t.lookup_pos_code = ISNULL(c.alpha_code, CONVERT(nvarchar, code))
   AND c.code_type = 29

SELECT @errno = @@error,
       @fixed_count = @fixed_count + @@rowcount
IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to set the payroll_entry_type.',
           @object_name = 'transl_payroll_detail',
	   @operation_name = 'UPDATE'
    GOTO error
  END

/* If the proc has been called for the second time and the replication has been instantaneous, the issue_count will be equal
   to fixed count and the autoconfig is complete. 
   Note: The proc will be called for the second time when a new code is configured and now the corresponding
   transl tables needs to be updated with the new S/A config. The actual configuration which is a insert to our S/A master
   tables happens in TM database which in scaleout environment exist in different server. After successful insertion the rows
   get replicated to peripheral databases. Most of the time the replication is instantaneous, but there is always a chance
   that replication happens with delays so the proc has to wait for some delays and then try to update the transl tables again.
   As we do not want to wait for ever, maximum of retry will be defined and if we reach the max retry, a warning message
   will be issued to inform the user that the process was not able to auto configure all the rows and we process the next
   batch. */
   
   
IF @issue_count = @fixed_count AND @lookup_pass = 2
  RETURN

WHILE @issue_count <> @fixed_count AND @lookup_pass = 2 
BEGIN
  
  SELECT @try_no = @try_no + 1
  
  IF @try_no > @max_retry
BEGIN
      
      SELECT @errmsg = 'Maximum retry |1 has reached. The edit was not able to auto configure all the data.',
             @errno = 202015,
             @message_id = 202015,
             @object_name = 'transl_payroll_detail',
             @operation_name = 'update'
    
      EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 3, @message_id, @process_name,
                         @object_name, @operation_name, 1, NULL, NULL, NULL, NULL,
                                   @max_retry
      RETURN
    END
    
  WAITFOR DELAY @wait_time
  
  UPDATE transl_payroll_detail
     SET payroll_entry_type = code
    FROM transl_payroll_detail t, code_description c
   WHERE t.payroll_entry_type = -3
     AND t.lookup_pos_code IS NOT NULL
     AND t.lookup_pos_code = ISNULL(c.alpha_code, CONVERT(nvarchar, code))
     AND c.code_type = 29

  SELECT @errno = @@error,
         @fixed_count = @fixed_count + @@rowcount
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to set the payroll_entry_type.',
   	     @object_name = 'transl_payroll_detail',
	     @operation_name = 'UPDATE'
      GOTO error
    END

END --WHILE @issue_count <> @fixed_count AND @lookup_pass = 2


SELECT @base_language_id = IsNull(convert(smallint, par_value), 1033)
  FROM auditworks_parameter
 WHERE par_name = 'base_language_id'

SELECT @errno = @@error
IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to select the base_language_id.',
	   @object_name = 'auditworks_parameter',
	   @operation_name = 'SELECT'
    GOTO error
  END

IF @base_language_id IS NULL
  SELECT @base_language_id = 1033

    
IF EXISTS (SELECT 1
             FROM language_identification
            WHERE language_id <> 1033 and active_flag = 1) --Multi language is on
          
  BEGIN
    -- list of the rows that their description have changed.
    
    INSERT work_config_pos_code_vw(
           request_id,
           table_name,
           code_type,
           code,
           pos_description,
           language_id,
           resource_id,
           new_code_flag,
           desc_update_flag,
           transaction_line_string)
    SELECT @request_id,
           'code_description',
           29,
           c.code,
           t.pos_description,
           ISNULL(o.PRMRY_LANG_ID,@base_language_id),
           l.resource_id,
           0,
           1,
           MIN(convert(nvarchar, t.entry_date_time, 109) + '|' + convert(nvarchar, t.store_no)  + '|' + convert(nvarchar, t.register_no)  + '|' + t.transaction_series  + '|' +  convert(nvarchar, t.transaction_no) + '|' + convert(nvarchar, t.line_id))
      FROM transl_payroll_detail t,
           code_description c,
           ORG_CHN o,
           language_dependent_description l
     WHERE t.payroll_entry_type <> -3
       AND t.store_no = o.ORG_CHN_NUM
       AND ISNULL(o.PRMRY_LANG_ID,@base_language_id) = l.language_id
       AND c.code_type = 29
       AND t.payroll_entry_type = c.code
       AND c.resource_id = l.resource_id
       AND t.pos_description IS NOT NULL
       AND (t.pos_description <> l.system_description OR l.system_description IS NULL)
     GROUP BY c.code, t.pos_description, ISNULL(o.PRMRY_LANG_ID,@base_language_id), l.resource_id
     
     SELECT @errno = @@error,
            @desc_update_count = @@rowcount
     IF @errno != 0
       BEGIN
         SELECT @errmsg = 'Failed to insert the rows that their description has changed.(multi language)',
	        @object_name = 'work_config_pos_code_vw',
	        @operation_name = 'INSERT'
         GOTO error
       END
     
     IF @issue_count = @fixed_count AND @desc_update_count = 0
       RETURN
     ELSE 
       SELECT @auto_config_required = 1
           
    -- list of the new codes which need to be auto configured
    INSERT work_config_pos_code_vw(
           request_id,
           table_name,
           code_type,
           lookup_pos_code,
           pos_description,
           language_id,
           resource_id,
           new_code_flag,
           desc_update_flag,
           transaction_line_string)
    SELECT @request_id,
           'code_description',
           29,
           t.lookup_pos_code,
           t.pos_description,
           ISNULL(o.PRMRY_LANG_ID, @base_language_id),
           NULL,
           1,
           0,
           MIN(convert(nvarchar, t.entry_date_time, 109) + '|' + convert(nvarchar, t.store_no)  + '|' + convert(nvarchar, t.register_no)  + '|' + t.transaction_series  + '|' +  convert(nvarchar, t.transaction_no) + '|' + convert(nvarchar, t.line_id))
      FROM transl_payroll_detail t LEFT JOIN ORG_CHN o ON (t.store_no = o.ORG_CHN_NUM)
     WHERE t.payroll_entry_type = -3
       AND t.lookup_pos_code IS NOT NULL
     GROUP BY t.lookup_pos_code,
           t.pos_description,
           ISNULL(o.PRMRY_LANG_ID, @base_language_id)

    SELECT @errno = @@error
     IF @errno != 0
       BEGIN
         SELECT @errmsg = 'Failed to insert new codes which need to be auto configured.(multi language)',
	        @object_name = 'work_config_pos_code_vw',
	        @operation_name = 'INSERT'
         GOTO error
       END  
  END           

ELSE -- Multi language is off
  BEGIN
    -- list of the rows that their description have changed.
    INSERT work_config_pos_code_vw(
           request_id,
           table_name,
           code_type,
           code,
           pos_description,
           language_id,
           resource_id,
           new_code_flag,
           desc_update_flag,
           transaction_line_string)
    SELECT @request_id, 
           'code_description',
           29,
           c.code,
           t.pos_description,
           @base_language_id,
           c.resource_id,
           0,
           1,
           MIN(convert(nvarchar, t.entry_date_time, 109) + '|' + convert(nvarchar, t.store_no)  + '|' + convert(nvarchar, t.register_no)  + '|' + t.transaction_series  + '|' +  convert(nvarchar, t.transaction_no) + '|' + convert(nvarchar, t.line_id))
      FROM transl_payroll_detail t, code_description c
     WHERE t.payroll_entry_type <> -3
       AND t.payroll_entry_type = c.code
       AND c.code_type = 29 
       AND t.pos_description IS NOT NULL       
       AND (t.pos_description <> c.code_system_descr OR c.code_system_descr IS NULL)
     GROUP BY c.code, t.pos_description, c.resource_id
             
     SELECT @errno = @@error,
            @desc_update_count = @@rowcount
     IF @errno != 0
       BEGIN
         SELECT @errmsg = 'Failed to insert the rows that their description has changed.',
	        @object_name = 'work_config_pos_code_vw',
	        @operation_name = 'INSERT'
         GOTO error
       END
    
     IF @issue_count = @fixed_count AND @desc_update_count = 0
       RETURN
     ELSE 
       SELECT @auto_config_required = 1
              
    -- list of the new codes which need to be auto configured
    INSERT work_config_pos_code_vw(
           request_id,
           table_name,
           code_type,
           lookup_pos_code,
           pos_description,
           language_id,
           resource_id,
           new_code_flag,
           desc_update_flag,
           transaction_line_string)
    SELECT @request_id,
           'code_description',
           29,
           t.lookup_pos_code,
           t.pos_description,
           @base_language_id,
           NULL,
           1,
           0,
           MIN(convert(nvarchar, t.entry_date_time, 109) + '|' + convert(nvarchar, t.store_no)  + '|' + convert(nvarchar, t.register_no)  + '|' + t.transaction_series  + '|' +  convert(nvarchar, t.transaction_no) + '|' + convert(nvarchar, t.line_id))
      FROM transl_payroll_detail t
     WHERE t.payroll_entry_type = -3
       AND t.lookup_pos_code IS NOT NULL
     GROUP BY t.lookup_pos_code, t.pos_description

     SELECT @errno = @@error
     IF @errno != 0
       BEGIN
         SELECT @errmsg = 'Failed to insert new codes which need to be auto configured',
	        @object_name = 'work_config_pos_code_vw',
	        @operation_name = 'INSERT'
         GOTO error
       END
  END 


RETURN

error:
        
	  
	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, 1, 1, 0,
	null, 0, null, null, null, null, null, null, 0, @process_id, NULL
	
        RETURN
```

