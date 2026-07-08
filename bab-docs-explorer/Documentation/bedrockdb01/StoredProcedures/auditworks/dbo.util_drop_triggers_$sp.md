# dbo.util_drop_triggers_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_drop_triggers_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.util_drop_triggers_$sp @object_type char(2) = 'TR'

AS

/* Procedure Name: util_drop_triggers_$sp
   Desc: drop all triggers in a db or all triggers except those in a list.
         Used for installation/upgrade of peripheral db's and the consolidated archive db in
         a scaleout environment since trigger functionality is not wanted in those databases
         due to possible conflicts with master table replication. In the peripheral db's, a few triggers will 
         remain in order to support autorevalidation of certain types of i/f rejects.
         Called during SA_PERI upgrades from the drop_triggers upgrade script. 

         Valid input values: TR = drop all triggers except for a hardcoded list (used on perpiheral db's)
                             AV = used on consolidated archive db (does nothing in Oracle environment)

         In Mssql, some tm triggers will be dropped from the archive db because the tm tables reside in a separate
          tm db from the archive tables. The master tables in the archive db will be populated as a subscriber
          to rdbms replication. For Mssql, it is necessary to list more master table triggers (compared to Oracle) in the archive db
          on consolidated in order to trigger re-validation of i/f rejects, e.g. EMPLY, ORG
          due to table changes being replicated from the tm db to the archive db.

         Valid input values: TR = drop all tm triggers except for a hardcoded list (used on perpiheral db's)
                             AV = drop all tm triggers (used on consolidated archive db)

HISTORY
Date     Name            Defect Desc
Dec10,12 Paul            140415 Updated comments to match Oracle
Jun15,12 Vicci           136014 Add the following triggers to the list of those to keep:  
				'if_error_$trI', 'if_cleanup_status_$trI', 'Ex_Queue_$trI', 'parameter_general_$trU', 'rebuild_request_$trD', 
				'smartload_var_$trD', 'smartload_var_$trI', 'smartload_var_$trU', 'work_export_ad_hoc_query_$trI'
Aug21,09 Vicci           111639 keep parameter_general_replicate trigger on peripherals
Dec19,05 Paul           DV-1325 add triggers to the do not drop list
Aug11,05 Paul           DV-1312 add triggers to the do not drop list
Jun17,05 Paul           DV-1282 author

*/


DECLARE
        @cursor_open            tinyint,
        @errno                  int,
        @sql_command            nvarchar(2000),
        @name                   varchar(80),
	@object_name            varchar(255),
	@process_name           varchar(100),
	@operation_name         varchar(100),
	@message_id		int,
	@errmsg			varchar(255)

SELECT @process_name = 'util_drop_triggers_$sp',
       @message_id = 201068        


CREATE TABLE #work_object_list (
	object_name varchar(80) not null)

SELECT @errno = @@error 
IF @errno != 0 BEGIN 
     SELECT @errmsg = 'Failed to create #work_object_list' ,
	@object_name    = '#work_object_list',
	@operation_name = 'CREATE'          
     GOTO error 
END 

IF @object_type IN ('TR','AV')
  BEGIN
	INSERT #work_object_list (object_name)
	SELECT name
	  FROM sysobjects
	 WHERE type = 'TR'

	IF @object_type = 'TR'
	BEGIN -- exclude SA triggers that must not be deleted from peripheral db's

	 DELETE #work_object_list
	  WHERE object_name IN ('EMPLY_SA_$TRI', 'EMPLY_SA_$TRU', 'ORG_CHN_APLCTN_USG_SA_$TRI','ORG_CHN_APLCTN_USG_SA_$TRU',
	      'ORG_CHN_WRKSTN_SA_$TRI','ORG_CHN_WRKSTN_SA_$TRU','ORG_CHN_OPEN_HOUR_EXCPTN_SA_$TRI','ORG_CHN_OPEN_HOUR_EXCPTN_SA_$TRU',
	      'ORG_CHN_OPEN_HOUR_EXCPTN_SA_$TRD','card_identification_$trI','card_identification_$trU',
	      'card_type_$trI','card_type_$trU','check_digit_routine_$trD','check_digit_routine_$trI', 'check_digit_routine_$trU',
	      'interface_directory_$trU','line_object_action_associ_$trI','pos_deptclass_$trI','pos_deptclass_$trU',
	      'restricted_field_$trI','store_audit_status_$trU','store_settlement_data_$trI','store_settlement_data_$trU',
	      'transaction_missing_$trI','user_upc_$trI','user_upc_$trU', 'parameter_general_repl_$trUI',
	      'if_error_$trI', 'if_cleanup_status_$trI', 'Ex_Queue_$trI', 'parameter_general_$trU', 'rebuild_request_$trD', 
	      'smartload_var_$trD', 'smartload_var_$trI', 'smartload_var_$trU', 'work_export_ad_hoc_query_$trI')
	END

	IF @object_type = 'AV' /* delete most tm triggers from the archive db on the consolidated server */
	  SELECT @object_type = 'TR'
  END

SELECT @cursor_open = 0

DECLARE object_crsr CURSOR FAST_FORWARD
FOR
SELECT object_name
FROM #work_object_list

OPEN object_crsr

SELECT @errno = @@error
IF @errno != 0
BEGIN
  SELECT @errmsg         = 'Failed to open object_crsr',
         @object_name    = 'object_crsr',
         @operation_name = 'OPEN'
  GOTO error
END

SELECT @cursor_open = 1

WHILE 1 = 1
  BEGIN
      FETCH object_crsr INTO
        @name

      IF @@fetch_status <> 0
        BREAK

      SELECT @sql_command = 'drop trigger dbo.' + @name
      SELECT @sql_command

      EXEC sp_executesql @sql_command

      SELECT @errno = @@error
      IF @errno <> 0
        BEGIN
	  SELECT @object_name = 'sp_executesql',
		@operation_name = 'EXECUTE',
		@errmsg = 'Failed to execute dynamic SQL: ' + @sql_command
	  GOTO error
	END

  END -- while 1 = 1

CLOSE object_crsr
DEALLOCATE object_crsr
SELECT @cursor_open = 0


RETURN


error:   /* Common error handler */

  IF @cursor_open = 1
  BEGIN
    CLOSE object_crsr
    DEALLOCATE object_crsr
  END

  EXEC common_error_handling_$sp 0, @errno, @errmsg, 0, @message_id, @process_name,
       @object_name, @operation_name, 1, 1, 0, null, 0, null, null, null, null, null,
       null, 0, 0, 0
        
  RETURN
```

