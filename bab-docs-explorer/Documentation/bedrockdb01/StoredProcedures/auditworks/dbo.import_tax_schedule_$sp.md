# dbo.import_tax_schedule_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.import_tax_schedule_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    import_release_export_hold(["import_release_export_hold"]) --> SP
    import_tax_schedule(["import_tax_schedule"]) --> SP
    interface_status(["interface_status"]) --> SP
    master_table_subscription(["master_table_subscription"]) --> SP
    tax_schedule(["tax_schedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |
| import_release_export_hold |
| import_tax_schedule |
| interface_status |
| master_table_subscription |
| tax_schedule |

## Stored Procedure Code

```sql
create proc dbo.import_tax_schedule_$sp  
AS

/* 
PROC NAME: import_tax_schedule_$sp
     DESC: This program posts imported tax schedule data to the tax_schedule table. 


HISTORY:
Date     Name       Def# Desc
Sep29,14 Vicci     86335 Remove reliance on SET ANSI_NULLS being ON.
Mar18,13 Vicci    142035 Put export on hold until import completes. 
Sep21,10 Phu      121037 Fix error: String or binary data would be truncated
Mar12,08 Vicci  1-38MDAZ Author

*/

DECLARE
	@errmsg				nvarchar(2000),
	@errno				int,
	@process_no			smallint,
	@log_flag			tinyint,
	@object_name			nvarchar(255),
	@process_name			nvarchar(100),
	@operation_name			nvarchar(100),
	@message_id			int,
	@hold_datetime			datetime,
	@hold_placed			tinyint

SET CONCAT_NULL_YIELDS_NULL OFF	

SELECT @process_name = 'import_tax_schedule_$sp',
       @message_id = 201068,
       @log_flag = 1,  -- called from smartload
       @process_no = 7, -- standard import
       @hold_datetime = getdate()

BEGIN TRY
UPDATE interface_status
   SET hold_datetime = @hold_datetime
  FROM master_table_subscription m WITH (NOLOCK)
 WHERE m.table_name  = 'tax_schedule'
   AND m.update_timing = 5
   AND m.interface_id =  interface_status.interface_id
   AND interface_status.hold_datetime IS NULL
SELECT @hold_placed = sign(@@rowcount)END TRY
BEGIN CATCH
  SELECT @errno = ERROR_NUMBER(), @errmsg = ERROR_MESSAGE()
IF @errno != 0
BEGIN
  SELECT @errmsg = @errmsg + ' -Failed to place exports to interfaces subscribing to tax_schedule changes on hold while import runs',
         @object_name = 'interface_status',
         @operation_name = 'UPDATE'
  GOTO error
END
END CATCH
      

BEGIN TRY
DELETE tax_schedule
  FROM import_tax_schedule i
 WHERE tax_schedule.tax_schedule_id = i.tax_schedule_id
   AND i.entry_type = 'D'
END TRY
BEGIN CATCH
  SELECT @errno = ERROR_NUMBER(), @errmsg = ERROR_MESSAGE()
IF @errno != 0
BEGIN
  SELECT @errmsg = @errmsg + ' -Failed to remove tax schedules to be deleted',
	 @object_name = 'tax_schedule',
	 @operation_name = 'DELETE'
  GOTO error
END
END CATCH

--Keep only the last instructions concerning a given schedule
BEGIN TRY
DELETE import_tax_schedule
  FROM (SELECT tax_schedule_id, max(entry_id) max_entry_id
          FROM import_tax_schedule
         GROUP BY tax_schedule_id 
        HAVING count(entry_id) > 1) q
 WHERE import_tax_schedule.tax_schedule_id = q.tax_schedule_id
   AND import_tax_schedule.entry_id < q.max_entry_id
END TRY
BEGIN CATCH
  SELECT @errno = ERROR_NUMBER(), @errmsg = ERROR_MESSAGE()
IF @errno != 0
BEGIN
  SELECT @errmsg = @errmsg + ' -Failed to remove superceded entries from import table',
	 @object_name = 'import_tax_schedule',
	 @operation_name = 'DELETE'
  GOTO error
END
END CATCH

BEGIN TRY
UPDATE tax_schedule
   SET tax_schedule_description = LTRIM(RTRIM(i.tax_schedule_description)),
       tax_schedule_type = LTRIM(RTRIM(i.tax_schedule_type)),
       limit_to_tax_jurisdiction = i.limit_to_tax_jurisdiction
  FROM import_tax_schedule i
 WHERE tax_schedule.tax_schedule_id = i.tax_schedule_id
   AND i.entry_type <> 'D'
END TRY
BEGIN CATCH
  SELECT @errno = ERROR_NUMBER(), @errmsg = ERROR_MESSAGE()
IF @errno != 0
BEGIN
  SELECT @errmsg = @errmsg + ' -Failed to update tax schedules',
	 @object_name = 'tax_schedule',
	 @operation_name = 'UDPATE'
  GOTO error
END
END CATCH

BEGIN TRY
INSERT into tax_schedule(
       tax_schedule_id,
       tax_schedule_description,
       tax_schedule_type,
       limit_to_tax_jurisdiction)
SELECT tax_schedule_id,
       LTRIM(RTRIM(tax_schedule_description)),
       LTRIM(RTRIM(tax_schedule_type)),
       limit_to_tax_jurisdiction
  FROM import_tax_schedule i
 WHERE i.entry_type <> 'D'
   AND i.tax_schedule_id NOT IN (SELECT s.tax_schedule_id
                                   FROM tax_schedule s
                                  WHERE i.tax_schedule_id = s.tax_schedule_id)
END TRY
BEGIN CATCH
  SELECT @errno = ERROR_NUMBER(), @errmsg = ERROR_MESSAGE()
IF @errno != 0
BEGIN
  SELECT @errmsg = @errmsg + ' -Failed to create new tax schedules',
	 @object_name = 'tax_schedule',
	 @operation_name = 'INSERT'
  GOTO error
END
END CATCH

IF @hold_placed = 1
BEGIN
  INSERT INTO import_release_export_hold(
         interface_id,
         hold_datetime)
  SELECT DISTINCT interface_id, hold_datetime
    FROM interface_status i WITH (NOLOCK)
   WHERE i.hold_datetime = @hold_datetime
  SELECT @errno = @@error
  IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to create entries that ICT_IMPORT will export as interface hold release requests and process once done importing other files.',
           @object_name = 'import_release_export_hold',
           @operation_name = 'INSERT'
    GOTO error
  END

  --Note: when this line is printed, the import ICT will drop a release_export_hold.GO file into the directory with priority 9999 to cause release to be placed last on TO-Do list.  
  PRINT ':LOG ReleaseExportHold'  
END  --IF @hold_placed = 1

RETURN

error:   /* Common error handler. */

	IF @hold_placed = 1
	BEGIN
	  INSERT INTO import_release_export_hold(
	         interface_id,
	         hold_datetime)
	  SELECT DISTINCT interface_id, hold_datetime
	    FROM interface_status i WITH (NOLOCK)
	   WHERE i.hold_datetime = @hold_datetime

	  --Note: when this line is printed, the import ICT will drop a release_export_hold.GO file into the directory with priority 9999 to cause release to be placed last on TO-Do list.  
	  PRINT ':LOG ReleaseExportHold'  
	END  --IF @hold_placed = 1


	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, @log_flag

	RETURN
```

