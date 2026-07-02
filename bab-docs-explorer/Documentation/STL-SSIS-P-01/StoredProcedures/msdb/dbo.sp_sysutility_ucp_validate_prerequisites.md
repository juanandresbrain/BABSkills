# dbo.sp_sysutility_ucp_validate_prerequisites

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sysutility_ucp_validate_prerequisites"]
    dbo_fn_sysutility_ucp_get_edition_is_ucp_capable_internal(["dbo.fn_sysutility_ucp_get_edition_is_ucp_capable_internal"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.fn_sysutility_ucp_get_edition_is_ucp_capable_internal |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_sysutility_ucp_validate_prerequisites]
WITH EXECUTE AS OWNER
AS
BEGIN
   IF (dbo.fn_sysutility_ucp_get_edition_is_ucp_capable_internal() = 1)
   BEGIN
      RAISERROR ('Instance is able to be used as a Utility Control Point.', 0, 1) WITH NOWAIT;
   END
   ELSE BEGIN
      DECLARE @edition nvarchar(128);
      SELECT @edition = CONVERT(nvarchar(128), SERVERPROPERTY('Edition'));
      RAISERROR(37004, -1, -1, @edition);
      RETURN(1);
   END;
END 

dbo,sp_target_server_summary,CREATE PROCEDURE sp_target_server_summary
  @target_server sysname = NULL
AS
BEGIN
  SET NOCOUNT ON

  SELECT server_id,
         server_name,
        'local_time' = DATEADD(SS, DATEDIFF(SS, last_poll_date, GETDATE()), local_time_at_last_poll),
         last_poll_date,
        'unread_instructions' = (SELECT COUNT(*)
                                 FROM msdb.dbo.sysdownloadlist sdl
                                 WHERE (UPPER(sdl.target_server) = UPPER(sts.server_name))
                                   AND (sdl.status = 0)),
        'blocked' = (SELECT COUNT(*)
                     FROM msdb.dbo.sysdownloadlist sdl
                     WHERE (UPPER(sdl.target_server) = UPPER(sts.server_name))
                       AND (sdl.error_message IS NOT NULL)),
         poll_interval
  FROM msdb.dbo.systargetservers sts
  WHERE ((@target_server IS NULL) OR (UPPER(@target_server) = UPPER(sts.server_name)))
END

dbo,sp_uniquetaskname,CREATE PROCEDURE sp_uniquetaskname
  @seed NVARCHAR(92)
AS
BEGIN
  DECLARE @newest_suffix INT

  SET NOCOUNT ON

  -- We're going to add a suffix of 8 characters so make sure the seed is at most 84 characters
  SELECT @seed = LTRIM(RTRIM(@seed))
  IF (DATALENGTH(@seed) > 0)
    SELECT @seed = SUBSTRING(@seed, 1, 84)

  -- Find the newest (highest) suffix so far
  SELECT @newest_suffix = MAX(CONVERT(INT, RIGHT(name, 8)))
  FROM msdb.dbo.sysjobs -- DON'T use sysjobs_view here!
  WHERE (name LIKE N'%[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')

  -- Generate the task name by appending the 'newest suffix' value (plus one) to the seed
  IF (@newest_suffix IS NOT NULL)
  BEGIN
    SELECT @newest_suffix = @newest_suffix + 1
    SELECT 'TaskName' = CONVERT(NVARCHAR(92), @seed + REPLICATE(N'0', 8 - (DATALENGTH(CONVERT(NVARCHAR, @newest_suffix)) / 2)) + CONVERT(NVARCHAR, @newest_suffix))
  END
  ELSE
    SELECT 'TaskName' = CONVERT(NVARCHAR(92), @seed + N'00000001')
END

dbo,sp_update_alert,CREATE PROCEDURE sp_update_alert
  @name                         sysname,
  @new_name                     sysname          = NULL,
  @enabled                      TINYINT          = NULL,
  @message_id                   INT              = NULL,
  @severity                     INT              = NULL,
  @delay_between_responses      INT              = NULL,
  @notification_message         NVARCHAR(512)    = NULL,
  @include_event_description_in TINYINT          = NULL, -- 0 = None, 1 = Email, 2 = Pager. 4 = NetSend, 7 = All
  @database_name                sysname          = NULL,
  @event_description_keyword    NVARCHAR(100)    = NULL,
  @job_id                       UNIQUEIDENTIFIER = NULL, -- If provided must NOT also provide job_name
  @job_name                     sysname          = NULL, -- If provided must NOT also provide job_id
  @occurrence_count             INT              = NULL, -- Can only be set to 0
  @count_reset_date             INT              = NULL,
  @count_reset_time             INT              = NULL,
  @last_occurrence_date         INT              = NULL, -- Can only be set to 0
  @last_occurrence_time         INT              = NULL, -- Can only be set to 0
  @last_response_date           INT              = NULL, -- Can only be set to 0
  @last_response_time           INT              = NULL, -- Can only be set to 0
  @raise_snmp_trap              TINYINT          = NULL,
  @performance_condition        NVARCHAR(512)    = NULL, -- New for 7.0
  @category_name                sysname          = NULL, -- New for 7.0
  @wmi_namespace           sysname         = NULL, -- New for 9.0
  @wmi_query               NVARCHAR(512)   = NULL  -- New for 9.0
AS
BEGIN
  DECLARE @x_enabled                   TINYINT
  DECLARE @x_message_id                INT
  DECLARE @x_severity                  INT
  DECLARE @x_delay_between_responses   INT
  DECLARE @x_notification_message      NVARCHAR(512)
  DECLARE @x_include_event_description TINYINT
  DECLARE @x_database_name             sysname
  DECLARE @x_event_description_keyword NVARCHAR(100)
  DECLARE @x_occurrence_count          INT
  DECLARE @x_count_reset_date          INT
  DECLARE @x_count_reset_time          INT
  DECLARE @x_last_occurrence_date      INT
  DECLARE @x_last_occurrence_time      INT
  DECLARE @x_last_response_date        INT
  DECLARE @x_last_response_time        INT
  DECLARE @x_flags                     INT
  DECLARE @x_performance_condition     NVARCHAR(512)
  DECLARE @x_job_id                    UNIQUEIDENTIFIER
  DECLARE @x_category_id               INT
  DECLARE @x_event_id                  INT
  DECLARE @x_wmi_namespace          sysname
  DECLARE @x_wmi_query              NVARCHAR(512)

  DECLARE @include_event_desc_code     TINYINT
  DECLARE @return_code                 INT
  DECLARE @duplicate_name              sysname
  DECLARE @category_id                 INT
  DECLARE @alert_id                    INT
  DECLARE @cached_attribute_modified   INT
  DECLARE @event_id                 INT

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @new_name                  = LTRIM(RTRIM(@new_name))
  SELECT @job_name                  = LTRIM(RTRIM(@job_name))
  SELECT @notification_message      = LTRIM(RTRIM(@notification_message))
  SELECT @database_name             = LTRIM(RTRIM(@database_name))
  SELECT @event_description_keyword = LTRIM(RTRIM(@event_description_keyword))
  SELECT @performance_condition     = LTRIM(RTRIM(@performance_condition))
  SELECT @category_name             = LTRIM(RTRIM(@category_name))

  -- Are we modifying an attribute which SQLServerAgent caches?
  IF ((@new_name                     IS NOT NULL) OR
      (@enabled                      IS NOT NULL) OR
      (@message_id                   IS NOT NULL) OR
      (@severity                     IS NOT NULL) OR
      (@delay_between_responses      IS NOT NULL) OR
      (@notification_message         IS NOT NULL) OR
      (@include_event_description_in IS NOT NULL) OR
      (@database_name                IS NOT NULL) OR
      (@event_description_keyword    IS NOT NULL) OR
      (@job_id                       IS NOT NULL) OR
      (@job_name                     IS NOT NULL) OR
      (@last_response_date           IS NOT NULL) OR
      (@last_response_time           IS NOT NULL) OR
      (@raise_snmp_trap              IS NOT NULL) OR
      (@performance_condition        IS NOT NULL) OR
      (@wmi_namespace             IS NOT NULL) OR
      (@wmi_query              IS NOT NULL))  
    SELECT @cached_attribute_modified = 1
  ELSE
    SELECT @cached_attribute_modified = 0

  -- Map a job_id of 0 to the real value we use to mean 'no job'
  IF (@job_id = CONVERT(UNIQUEIDENTIFIER, 0x00)) AND (@job_name IS NULL)
    SELECT @job_name = N''

  -- Only a sysadmin can do this
  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))
  BEGIN
    RAISERROR(15003, 16, 1, N'sysadmin')
    RETURN(1)
  END

  -- Check if SQLServerAgent is in the process of starting
  EXECUTE @return_code = msdb.dbo.sp_is_sqlagent_starting
  IF (@return_code <> 0)
    RETURN(1) -- Failure

  -- Check if this Alert exists
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysalerts
                  WHERE (name = @name)))
  BEGIN
    RAISERROR(14262, 16, 1, '@name', @name)
    RETURN(1)
  END

  -- Certain values (if supplied) may only be updated to 0
  IF (@occurrence_count <> 0)
  BEGIN
    RAISERROR(14266, -1, -1, '@occurrence_count', '0')
    RETURN(1) -- Failure
  END
  IF (@last_occurrence_date <> 0)
  BEGIN
    RAISERROR(14266, -1, -1, '@last_occurrence_date', '0')
    RETURN(1) -- Failure
  END
  IF (@last_occurrence_time <> 0)
  BEGIN
    RAISERROR(14266, -1, -1, '@last_occurrence_time', '0')
    RETURN(1) -- Failure
  END
  IF (@last_response_date <> 0)
  BEGIN
    RAISERROR(14266, -1, -1, '@last_response_date', '0')
    RETURN(1) -- Failure
  END
  IF (@last_response_time <> 0)
  BEGIN
    RAISERROR(14266, -1, -1, '@last_response_time', '0')
    RETURN(1) -- Failure
  END

  -- Get existing (@x_) values
  SELECT @alert_id                    = id,
         @x_enabled                   = enabled,
         @x_message_id                = message_id,
         @x_severity                  = severity,
         @x_delay_between_responses   = delay_between_responses,
         @x_notification_message      = notification_message,
         @x_include_event_description = include_event_description,
         @x_database_name             = database_name,
         @x_event_description_keyword = event_description_keyword,
         @x_occurrence_count          = occurrence_count,
         @x_count_reset_date          = count_reset_date,
         @x_count_reset_time          = count_reset_time,
         @x_job_id                    = job_id,
         @x_last_occurrence_date      = last_occurrence_date,
         @x_last_occurrence_time      = last_occurrence_time,
         @x_last_response_date        = last_response_date,
         @x_last_response_time        = last_response_time,
         @x_flags                     = flags,
         @x_performance_condition     = performance_condition,
         @x_category_id               = category_id,
       @x_event_id              = event_id
  FROM msdb.dbo.sysalerts
  WHERE (name = @name)
  
  SELECT @x_job_id = sjv.job_id
  FROM msdb.dbo.sysalerts    sa,
       msdb.dbo.sysjobs_view sjv
  WHERE (sa.job_id = sjv.job_id)
    AND (sa.name = @name)

  -- Fill out the values for all non-supplied parameters from the existsing values
  IF (@x_event_id = 8)
  BEGIN
   -- WMI alert type
   IF (@wmi_namespace IS NULL) SELECT @wmi_namespace = @x_database_name
   IF (@wmi_query IS NULL) SELECT @wmi_query = @x_performance_condition
  END
  ELSE
  BEGIN
   -- Non-WMI alert type
   IF (@database_name IS NULL) SELECT @database_name = @x_database_name
   IF (@performance_condition IS NULL) SELECT @performance_condition = @x_performance_condition
  END
   
  IF (@enabled                      IS NULL) SELECT @enabled                      = @x_enabled
  IF (@message_id                   IS NULL) SELECT @message_id                   = @x_message_id
  IF (@severity                     IS NULL) SELECT @severity                     = @x_severity
  IF (@delay_between_responses      IS NULL) SELECT @delay_between_responses      = @x_delay_between_responses
  IF (@notification_message         IS NULL) SELECT @notification_message         = @x_notification_message
  IF (@include_event_description_in IS NULL) SELECT @include_event_description_in = @x_include_event_description
  IF (@event_description_keyword    IS NULL) SELECT @event_description_keyword    = @x_event_description_keyword
  IF (@job_id IS NULL) AND (@job_name IS NULL) SELECT @job_id                     = @x_job_id
  IF (@occurrence_count             IS NULL) SELECT @occurrence_count             = @x_occurrence_count
  IF (@count_reset_date             IS NULL) SELECT @count_reset_date             = @x_count_reset_date
  IF (@count_reset_time             IS NULL) SELECT @count_reset_time             = @x_count_reset_time
  IF (@last_occurrence_date         IS NULL) SELECT @last_occurrence_date         = @x_last_occurrence_date
  IF (@last_occurrence_time         IS NULL) SELECT @last_occurrence_time         = @x_last_occurrence_time
  IF (@last_response_date           IS NULL) SELECT @last_response_date           = @x_last_response_date
  IF (@last_response_time           IS NULL) SELECT @last_response_time           = @x_last_response_time
  IF (@raise_snmp_trap              IS NULL) SELECT @raise_snmp_trap              = @x_flags & 0x1
  IF (@category_name                IS NULL) SELECT @category_name = name FROM msdb.dbo.syscategories WHERE (category_id = @x_category_id)

  IF (@category_name IS NULL)
  BEGIN
    SELECT @category_name = name
    FROM msdb.dbo.syscategories
    WHERE (category_id = 98)
  END

  -- Turn [nullable] empty string parameters into NULLs
  IF (@new_name                  = N'') SELECT @new_name                  = NULL
  IF (@notification_message      = N'') SELECT @notification_message      = NULL
  IF (@database_name             = N'') SELECT @database_name             = NULL
  IF (@event_description_keyword = N'') SELECT @event_description_keyword = NULL
  IF (@performance_condition     = N'') SELECT @performance_condition     = NULL
  IF (@wmi_namespace        = N'') SELECT @wmi_namespace         = NULL
  IF (@wmi_query            = N'') SELECT @wmi_query             = NULL

  -- Verify the Alert
  IF (@job_id = CONVERT(UNIQUEIDENTIFIER, 0x00))
    SELECT @job_id = NULL
  EXECUTE @return_code = sp_verify_alert @new_name,
                                         @message_id,
                                         @severity,
                                         @enabled,
                                         @delay_between_responses,
                                         @notification_message,
                                         @include_event_description_in,
                                         @database_name,
                                         @event_description_keyword,
                                         @job_id OUTPUT,
                                         @job_name OUTPUT,
                                         @occurrence_count,
                                         @raise_snmp_trap,
                                         @performance_condition,
                                         @category_name,
                                         @category_id OUTPUT,
                                         @count_reset_date,
                                         @count_reset_time,
                                         @wmi_namespace,
                                         @wmi_query,
                                     @event_id OUTPUT
  IF (@return_code <> 0)
    RETURN(1) -- Failure

  -- If the user didn't supply a NewName, use the old one.
  -- NOTE: This must be done AFTER sp_verify_alert.
  IF (@new_name IS NULL)
    SELECT @new_name = @name

  -- Turn the 1st 'flags' bit on or off accordingly
  IF (@raise_snmp_trap = 0)
    SELECT @x_flags = @x_flags & 0xFFFE
  ELSE
    SELECT @x_flags = @x_flags | 0x0001

  -- For WMI alerts replace 
  -- database_name with wmi_namespace and 
  -- performance_conditon with wmi_query
  -- so we can store them in those columns in sysalerts table
  IF (@event_id = 8)
  BEGIN
   SELECT @database_name = @wmi_namespace
   SELECT @performance_condition = @wmi_query
  END

  -- Check if this Alert already exists
  SELECT @duplicate_name = FORMATMESSAGE(14205)
  SELECT @duplicate_name = name
  FROM msdb.dbo.sysalerts
  WHERE ((event_id = 8) AND 
       (ISNULL(performance_condition, N'') = ISNULL(@performance_condition, N'')) AND
       (ISNULL(database_name, N'') = ISNULL(@database_name, N''))) OR
      ((ISNULL(event_id,1) <> 8) AND 
       (ISNULL(performance_condition, N'apples') = ISNULL(@performance_condition, N'oranges'))) OR 
      ((performance_condition IS NULL) AND
         (message_id = @message_id) AND
         (severity = @severity) AND
         (ISNULL(database_name, N'') = ISNULL(@database_name, N'')) AND
         (ISNULL(event_description_keyword, N'') = ISNULL(@event_description_keyword, N'')))
  IF (@duplicate_name <> FORMATMESSAGE(14205) AND @duplicate_name <> @name)
  BEGIN
    RAISERROR(14501, 16, 1, @duplicate_name)
    RETURN(1) -- Failure
  END

  -- Finally, do the actual UPDATE
  UPDATE msdb.dbo.sysalerts
  SET name                        = @new_name,
      message_id                  = @message_id,
      severity                    = @severity,
      enabled                     = @enabled,
      delay_between_responses     = @delay_between_responses,
      notification_message        = @notification_message,
      include_event_description   = @include_event_description_in,
      database_name               = @database_name,
      event_description_keyword   = @event_description_keyword,
      job_id                      = ISNULL(@job_id, CONVERT(UNIQUEIDENTIFIER, 0x00)),
      occurrence_count            = @occurrence_count,
      count_reset_date            = @count_reset_date,
      count_reset_time            = @count_reset_time,
      last_occurrence_date        = @last_occurrence_date,
      last_occurrence_time        = @last_occurrence_time,
      last_response_date          = @last_response_date,
      last_response_time          = @last_response_time,
      flags                       = @x_flags,
      performance_condition       = @performance_condition,
      category_id                 = @category_id,
      event_id               = @event_id
  WHERE (name = @name)

  -- Notify SQLServerAgent of the change
  IF (@cached_attribute_modified = 1)
    EXECUTE msdb.dbo.sp_sqlagent_notify @op_type     = N'A',
                                        @alert_id    = @alert_id,
                                        @action_type = N'U'
  RETURN(0) -- Success
END

dbo,sp_update_category,CREATE PROCEDURE sp_update_category
  @class    VARCHAR(8),  -- JOB or ALERT or OPERATOR
  @name     sysname,
  @new_name sysname
AS
BEGIN
  DECLARE @retval         INT
  DECLARE @category_id    INT
  DECLARE @category_class INT

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @class    = LTRIM(RTRIM(@class))
  SELECT @name     = LTRIM(RTRIM(@name))
  SELECT @new_name = LTRIM(RTRIM(@new_name))

  --turn empy parametrs tu null parameters
  IF @name = ''  SELECT @name = NULL

  EXECUTE @retval = sp_verify_category @class,
                                       NULL,
                                       @new_name,
                                       @category_class OUTPUT,
                                       NULL
  IF (@retval <> 0)
    RETURN(1) -- Failure

  --ID @name not null check id such a category exists
  --check name - it should exist if not null
  IF @name IS NOT NULL AND
     NOT EXISTS(SELECT * FROM msdb.dbo.syscategories WHERE name = @name 
      AND category_class = @category_class)
  BEGIN
      RAISERROR(14526, -1, -1, @name, @category_class)
      RETURN(1) -- Failure
  END  

  -- Check name
  SELECT @category_id = category_id
  FROM msdb.dbo.syscategories
  WHERE (category_class = @category_class)
    AND (name = @new_name)
  IF (@category_id IS NOT NULL)
  BEGIN
    RAISERROR(14261, -1, -1, '@new_name', @new_name)
    RETURN(1) -- Failure
  END

  -- Make sure that we're not updating one of the permanent categories (id's 0 - 99)
  IF (@category_id < 100)
  BEGIN
    RAISERROR(14276, -1, -1, @name, @class)
    RETURN(1) -- Failure
  END

  -- Update the category name
  UPDATE msdb.dbo.syscategories
  SET name = @new_name
  WHERE (category_class = @category_class)
    AND (name = @name)

  RETURN(@@error) -- 0 means success
END

dbo,sp_update_job,CREATE PROCEDURE sp_update_job
  @job_id                       UNIQUEIDENTIFIER = NULL, -- Must provide this or current_name
  @job_name                     sysname          = NULL, -- Must provide this or job_id
  @new_name                     sysname          = NULL,
  @enabled                      TINYINT          = NULL,
  @description                  NVARCHAR(512)    = NULL,
  @start_step_id                INT              = NULL,
  @category_name                sysname          = NULL,
  @owner_login_name             sysname          = NULL,
  @notify_level_eventlog        INT              = NULL,
  @notify_level_email           INT              = NULL,
  @notify_level_netsend         INT              = NULL,
  @notify_level_page            INT              = NULL,
  @notify_email_operator_name   sysname          = NULL,
  @notify_netsend_operator_name sysname          = NULL,
  @notify_page_operator_name    sysname          = NULL,
  @delete_level                 INT              = NULL,
  @automatic_post               BIT              = 1     -- Flag for SEM use only
AS
BEGIN
  DECLARE @retval                        INT
  DECLARE @category_id                   INT
  DECLARE @notify_email_operator_id      INT
  DECLARE @notify_netsend_operator_id    INT
  DECLARE @notify_page_operator_id       INT
  DECLARE @owner_sid                     VARBINARY(85)
  DECLARE @alert_id                      INT
  DECLARE @cached_attribute_modified     INT
  DECLARE @is_sysadmin                   INT
  DECLARE @current_owner                 sysname
  DECLARE @enable_only_used              INT

  DECLARE @x_new_name                    sysname
  DECLARE @x_enabled                     TINYINT
  DECLARE @x_description                 NVARCHAR(512)
  DECLARE @x_start_step_id               INT
  DECLARE @x_category_name               sysname
  DECLARE @x_category_id                 INT
  DECLARE @x_owner_sid                   VARBINARY(85)
  DECLARE @x_notify_level_eventlog       INT
  DECLARE @x_notify_level_email          INT
  DECLARE @x_notify_level_netsend        INT
  DECLARE @x_notify_level_page           INT
  DECLARE @x_notify_email_operator_name  sysname
  DECLARE @x_notify_netsnd_operator_name sysname
  DECLARE @x_notify_page_operator_name   sysname
  DECLARE @x_delete_level                INT
  DECLARE @x_originating_server_id       INT -- Not updatable
  DECLARE @x_master_server               BIT

  -- Remove any leading/trailing spaces from parameters (except @owner_login_name)
  SELECT @job_name                     = LTRIM(RTRIM(@job_name))
  SELECT @new_name                     = LTRIM(RTRIM(@new_name))
  SELECT @description                  = LTRIM(RTRIM(@description))
  SELECT @category_name                = LTRIM(RTRIM(@category_name))
  SELECT @notify_email_operator_name   = LTRIM(RTRIM(@notify_email_operator_name))
  SELECT @notify_netsend_operator_name = LTRIM(RTRIM(@notify_netsend_operator_name))
  SELECT @notify_page_operator_name    = LTRIM(RTRIM(@notify_page_operator_name))

  SET NOCOUNT ON

  EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                              '@job_id',
                                               @job_name OUTPUT,
                                               @job_id   OUTPUT
  IF (@retval <> 0)
    RETURN(1) -- Failure

  -- Are we modifying an attribute which SQLServerAgent caches?
  IF ((@new_name                     IS NOT NULL) OR
      (@enabled                      IS NOT NULL) OR
      (@start_step_id                IS NOT NULL) OR
      (@owner_login_name             IS NOT NULL) OR
      (@notify_level_eventlog        IS NOT NULL) OR
      (@notify_level_email           IS NOT NULL) OR
      (@notify_level_netsend         IS NOT NULL) OR
      (@notify_level_page            IS NOT NULL) OR
      (@notify_email_operator_name   IS NOT NULL) OR
      (@notify_netsend_operator_name IS NOT NULL) OR
      (@notify_page_operator_name    IS NOT NULL) OR
      (@delete_level                 IS NOT NULL))
    SELECT @cached_attribute_modified = 1
  ELSE
    SELECT @cached_attribute_modified = 0
    
  -- Is @enable the only parameter used beside jobname and jobid?
  IF ((@enabled                   IS NOT NULL) AND
     (@new_name                IS NULL) AND
     (@description                  IS NULL) AND
     (@start_step_id                IS NULL) AND
     (@category_name                IS NULL) AND
     (@owner_login_name             IS NULL) AND
     (@notify_level_eventlog        IS NULL) AND
     (@notify_level_email           IS NULL) AND
     (@notify_level_netsend         IS NULL) AND
     (@notify_level_page            IS NULL) AND
     (@notify_email_operator_name   IS NULL) AND
     (@notify_netsend_operator_name IS NULL) AND
     (@notify_page_operator_name    IS NULL) AND
     (@delete_level                 IS NULL))
    SELECT @enable_only_used = 1
  ELSE
    SELECT @enable_only_used = 0

  -- Set the x_ (existing) variables
  SELECT @x_new_name                    = sjv.name,
         @x_enabled                     = sjv.enabled,
         @x_description                 = sjv.description,
         @x_start_step_id               = sjv.start_step_id,
         @x_category_name               = sc.name,                  -- From syscategories
         @x_category_id                 = sc.category_id,           -- From syscategories
         @x_owner_sid                   = sjv.owner_sid,
         @x_notify_level_eventlog       = sjv.notify_level_eventlog,
         @x_notify_level_email          = sjv.notify_level_email,
         @x_notify_level_netsend        = sjv.notify_level_netsend,
         @x_notify_level_page           = sjv.notify_level_page,
         @x_notify_email_operator_name  = so1.name,                   -- From sysoperators
         @x_notify_netsnd_operator_name = so2.name,                   -- From sysoperators
         @x_notify_page_operator_name   = so3.name,                   -- From sysoperators
         @x_delete_level                = sjv.delete_level,
         @x_originating_server_id       = sjv.originating_server_id,
         @x_master_server               = master_server
  FROM msdb.dbo.sysjobs_view                 sjv
       LEFT OUTER JOIN msdb.dbo.sysoperators so1 ON (sjv.notify_email_operator_id = so1.id)
       LEFT OUTER JOIN msdb.dbo.sysoperators so2 ON (sjv.notify_netsend_operator_id = so2.id)
       LEFT OUTER JOIN msdb.dbo.sysoperators so3 ON (sjv.notify_page_operator_id = so3.id),
       msdb.dbo.syscategories                sc
  WHERE (sjv.job_id = @job_id)
    AND (sjv.category_id = sc.category_id)

  -- Check authority (only SQLServerAgent can modify a non-local job)
  IF ((@x_master_server = 1) AND (PROGRAM_NAME() NOT LIKE N'SQLAgent%') )
  BEGIN
    RAISERROR(14274, -1, -1)
    RETURN(1) -- Failure
  END
  
  -- Check permissions beyond what's checked by the sysjobs_view
  -- SQLAgentReader and SQLAgentOperator roles that can see all jobs
  -- cannot modify jobs they do not own
  IF ( (@x_owner_sid <> SUSER_SID())                  -- does not own the job
      AND (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1)   -- is not sysadmin
      AND (@enable_only_used <> 1 OR ISNULL(IS_MEMBER(N'SQLAgentOperatorRole'), 0) <> 1))
  BEGIN
   RAISERROR(14525, -1, -1);
   RETURN(1) -- Failure
  END

  -- Check job category, only sysadmin can modify mutli-server jobs        
  IF (EXISTS (SELECT * FROM msdb.dbo.syscategories WHERE (category_class = 1) -- Job
                                                     AND (category_type = 2) -- Multi-Server
                                                     AND (category_id = @x_category_id)
                                                     AND (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))) -- is not sysadmin
  BEGIN
     RAISERROR(14396, -1, -1);
     RETURN(1) -- Failure
  END          
            
  IF (@new_name = N'') SELECT @new_name = NULL

  -- Fill out the values for all non-supplied parameters from the existing values
  IF (@new_name                     IS NULL) SELECT @new_name                     = @x_new_name
  IF (@enabled                      IS NULL) SELECT @enabled                      = @x_enabled
  IF (@description                  IS NULL) SELECT @description                  = @x_description
  IF (@start_step_id                IS NULL) SELECT @start_step_id                = @x_start_step_id
  IF (@category_name                IS NULL) SELECT @category_name                = @x_category_name
  IF (@owner_sid                    IS NULL) SELECT @owner_sid                    = @x_owner_sid
  IF (@notify_level_eventlog        IS NULL) SELECT @notify_level_eventlog        = @x_notify_level_eventlog
  IF (@notify_level_email           IS NULL) SELECT @notify_level_email           = @x_notify_level_email
  IF (@notify_level_netsend         IS NULL) SELECT @notify_level_netsend         = @x_notify_level_netsend
  IF (@notify_level_page            IS NULL) SELECT @notify_level_page            = @x_notify_level_page
  IF (@notify_email_operator_name   IS NULL) SELECT @notify_email_operator_name   = @x_notify_email_operator_name
  IF (@notify_netsend_operator_name IS NULL) SELECT @notify_netsend_operator_name = @x_notify_netsnd_operator_name
  IF (@notify_page_operator_name    IS NULL) SELECT @notify_page_operator_name    = @x_notify_page_operator_name
  IF (@delete_level                 IS NULL) SELECT @delete_level                 = @x_delete_level

  -- If the SA is attempting to assign ownership of the job to someone else, then convert
  -- the login name to an ID
  IF (@owner_login_name = N'$(SQLAgentAccount)')  AND 
     (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1)
  BEGIN
    SELECT @owner_sid = 0xFFFFFFFF   
  END
  ELSE IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1) AND (@owner_login_name IS NOT NULL))
  BEGIN
    --force case insensitive comparation for NT users
    SELECT @owner_sid = SUSER_SID(@owner_login_name, 0) -- If @owner_login_name is invalid then SUSER_SID() will return NULL
  END

  -- Only the SA can re-assign jobs
  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1) AND (@owner_login_name IS NOT NULL))
    RAISERROR(14242, -1, -1)

  -- Ownership of a multi-server job cannot be assigned to a non-sysadmin
  IF (@owner_login_name IS NOT NULL) AND
     (EXISTS (SELECT *
              FROM msdb.dbo.sysjobs       sj,
                   msdb.dbo.sysjobservers sjs
              WHERE (sj.job_id = sjs.job_id)
                AND (sj.job_id = @job_id)
                AND (sjs.server_id <> 0)))
  BEGIN
    IF (@owner_login_name = N'$(SQLAgentAccount)') -- allow distributed jobs to be assigned to special account
    BEGIN
      SELECT @is_sysadmin = 1    
    END
    ELSE
    BEGIN
      SELECT @is_sysadmin = 0
      EXECUTE msdb.dbo.sp_sqlagent_has_server_access @login_name = @owner_login_name, @is_sysadmin_member = @is_sysadmin OUTPUT
    END

    IF (@is_sysadmin = 0)
    BEGIN
      SELECT @current_owner = dbo.SQLAGENT_SUSER_SNAME(@x_owner_sid)
      RAISERROR(14543, -1, -1, @current_owner, N'sysadmin')
      RETURN(1) -- Failure
    END
  END

  -- Turn [nullable] empty string parameters into NULLs
  IF (@description                  = N'') SELECT @description                  = NULL
  IF (@category_name                = N'') SELECT @category_name                = NULL
  IF (@notify_email_operator_name   = N'') SELECT @notify_email_operator_name   = NULL
  IF (@notify_netsend_operator_name = N'') SELECT @notify_netsend_operator_name = NULL
  IF (@notify_page_operator_name    = N'') SELECT @notify_page_operator_name    = NULL

  -- Check new values
  EXECUTE @retval = sp_verify_job @job_id,
                                  @new_name,
                                  @enabled,
                                  @start_step_id,
                                  @category_name,
                                  @owner_sid                  OUTPUT,
                                  @notify_level_eventlog,
                                  @notify_level_email         OUTPUT,
                                  @notify_level_netsend       OUTPUT,
                                  @notify_level_page          OUTPUT,
                                  @notify_email_operator_name,
                                  @notify_netsend_operator_name,
                                  @notify_page_operator_name,
                                  @delete_level,
                                  @category_id                OUTPUT,
                                  @notify_email_operator_id   OUTPUT,
                                  @notify_netsend_operator_id OUTPUT,
                                  @notify_page_operator_id    OUTPUT,
                                  NULL  
  IF (@retval <> 0)
    RETURN(1) -- Failure

  BEGIN TRANSACTION

  -- If the job is being re-assigned, modify sysjobsteps.database_user_name as necessary
  IF (@owner_login_name IS NOT NULL)
  BEGIN
    IF (EXISTS (SELECT *
                FROM msdb.dbo.sysjobsteps
                WHERE (job_id = @job_id)
                  AND (subsystem = N'TSQL')))
    BEGIN
      IF (EXISTS (SELECT *
                  FROM master.dbo.syslogins
                  WHERE (sid = @owner_sid)
                    AND (sysadmin <> 1)))
      BEGIN
        -- The job is being re-assigned to an non-SA
        UPDATE msdb.dbo.sysjobsteps
        SET database_user_name = NULL
        WHERE (job_id = @job_id)
          AND (subsystem = N'TSQL')
      END
    END
  END

  UPDATE msdb.dbo.sysjobs
  SET name                       = @new_name,
      enabled                    = @enabled,
      description                = @description,
      start_step_id              = @start_step_id,
      category_id                = @category_id,              -- Returned from sp_verify_job
      owner_sid                  = @owner_sid,
      notify_level_eventlog      = @notify_level_eventlog,
      notify_level_email         = @notify_level_email,
      notify_level_netsend       = @notify_level_netsend,
      notify_level_page          = @notify_level_page,
      notify_email_operator_id   = @notify_email_operator_id,   -- Returned from sp_verify_job
      notify_netsend_operator_id = @notify_netsend_operator_id, -- Returned from sp_verify_job
      notify_page_operator_id    = @notify_page_operator_id,    -- Returned from sp_verify_job
      delete_level               = @delete_level,
      version_number             = version_number + 1,  -- Update the job's version
      date_modified              = GETDATE()            -- Update the job's last-modified information
  WHERE (job_id = @job_id)
  SELECT @retval = @@error

  COMMIT TRANSACTION

  -- Always re-post the job if it's an auto-delete job (or if we're updating an auto-delete job
  -- to be non-auto-delete)
  IF (((SELECT delete_level
        FROM msdb.dbo.sysjobs
        WHERE (job_id = @job_id)) <> 0) OR
      ((@x_delete_level = 1) AND (@delete_level = 0)))
    EXECUTE msdb.dbo.sp_post_msx_operation 'INSERT', 'JOB', @job_id
  ELSE
  BEGIN
    -- Post the update to target servers
    IF (@automatic_post = 1)
      EXECUTE msdb.dbo.sp_post_msx_operation 'UPDATE', 'JOB', @job_id
  END

  -- Keep SQLServerAgent's cache in-sync
  -- NOTE: We only notify SQLServerAgent if we know the job has been cached and if
  --       attributes other than description or category have been changed (since
  --       SQLServerAgent doesn't cache these two)
  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysjobservers
              WHERE (job_id = @job_id)
                AND (server_id = 0)
                AND (@cached_attribute_modified = 1)))
    EXECUTE msdb.dbo.sp_sqlagent_notify @op_type     = N'J',
                                        @job_id      = @job_id,
                                        @action_type = N'U'

  -- If the name was changed, make SQLServerAgent re-cache any alerts that reference the job
  -- since the alert cache contains the job name
  IF ((@job_name <> @new_name) AND (EXISTS (SELECT *
                                            FROM msdb.dbo.sysalerts
                                            WHERE (job_id = @job_id))))
  BEGIN
    DECLARE sysalerts_cache_update CURSOR LOCAL
    FOR
    SELECT id
    FROM msdb.dbo.sysalerts
    WHERE (job_id = @job_id)

    OPEN sysalerts_cache_update
    FETCH NEXT FROM sysalerts_cache_update INTO @alert_id

    WHILE (@@fetch_status = 0)
    BEGIN
      EXECUTE msdb.dbo.sp_sqlagent_notify @op_type     = N'A',
                                          @alert_id    = @alert_id,
                                          @action_type = N'U'
      FETCH NEXT FROM sysalerts_cache_update INTO @alert_id
    END
    DEALLOCATE sysalerts_cache_update
  END

  RETURN(@retval) -- 0 means success
END

dbo,sp_update_jobschedule,CREATE PROCEDURE sp_update_jobschedule              -- This SP is deprecated by sp_update_schedule.
  @job_id                 UNIQUEIDENTIFIER = NULL,
  @job_name               sysname          = NULL,
  @name                   sysname,
  @new_name               sysname          = NULL,
  @enabled                TINYINT          = NULL,
  @freq_type              INT              = NULL,
  @freq_interval          INT              = NULL,
  @freq_subday_type       INT              = NULL,
  @freq_subday_interval   INT              = NULL,
  @freq_relative_interval INT              = NULL,
  @freq_recurrence_factor INT              = NULL,
  @active_start_date      INT              = NULL,
  @active_end_date        INT              = NULL,
  @active_start_time      INT              = NULL,
  @active_end_time        INT              = NULL,
  @automatic_post         BIT              = 1         -- If 1 will post notifications to all tsx servers to that run this job
AS
BEGIN
  DECLARE @retval                   INT
  DECLARE @sched_count              INT
  DECLARE @schedule_id              INT
  DECLARE @job_owner_sid            VARBINARY(85)
  DECLARE @enable_only_used         INT

  DECLARE @x_name                   sysname
  DECLARE @x_enabled                TINYINT
  DECLARE @x_freq_type              INT
  DECLARE @x_freq_interval          INT
  DECLARE @x_freq_subday_type       INT
  DECLARE @x_freq_subday_interval   INT
  DECLARE @x_freq_relative_interval INT
  DECLARE @x_freq_recurrence_factor INT
  DECLARE @x_active_start_date      INT
  DECLARE @x_active_end_date        INT
  DECLARE @x_active_start_time      INT
  DECLARE @x_active_end_time        INT
  DECLARE @owner_sid                VARBINARY(85)

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @name     = LTRIM(RTRIM(@name))
  SELECT @new_name = LTRIM(RTRIM(@new_name))

  -- Turn [nullable] empty string parameters into NULLs
  IF (@new_name = N'') SELECT @new_name = NULL

  -- Check authority (only SQLServerAgent can modify a schedule of a non-local job)
  EXECUTE @retval = sp_verify_jobproc_caller @job_id = @job_id, @program_name = 'SQLAgent%'
  IF (@retval <> 0)
    RETURN(@retval)

  -- Check that we can uniquely identify the job
  EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                              '@job_id',
                                               @job_name OUTPUT,
                                               @job_id   OUTPUT,
                                               @owner_sid = @job_owner_sid OUTPUT
  IF (@retval <> 0)
    RETURN(1) -- Failure
    
  -- Is @enable the only parameter used beside jobname and jobid?
  IF ((@enabled                   IS NOT NULL) AND
     (@name                 IS NULL) AND
     (@new_name                IS NULL) AND
      (@freq_type              IS NULL) AND
      (@freq_interval             IS NULL) AND
      (@freq_subday_type          IS NULL) AND
      (@freq_subday_interval      IS NULL) AND
      (@freq_relative_interval       IS NULL) AND
      (@freq_recurrence_factor       IS NULL) AND
      (@active_start_date         IS NULL) AND
      (@active_end_date           IS NULL) AND
      (@active_start_time         IS NULL) AND
      (@active_end_time           IS NULL))
    SELECT @enable_only_used = 1
  ELSE
    SELECT @enable_only_used = 0
    

  IF ((SUSER_SID() <> @job_owner_sid)
     AND (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1)
      AND (@enable_only_used <> 1 OR ISNULL(IS_MEMBER(N'SQLAgentOperatorRole'), 0) <> 1))
  BEGIN
   RAISERROR(14525, -1, -1)
   RETURN(1) -- Failure
  END

  -- Make sure the schedule_id can be uniquely identified and that it exists
  -- Note: It's safe use the values returned by the MIN() function because the SP errors out if more than 1 record exists
  SELECT @sched_count = COUNT(*),
         @schedule_id = MIN(sched.schedule_id),
         @owner_sid   = MIN(sched.owner_sid)
  FROM msdb.dbo.sysjobschedules as jsched
    JOIN msdb.dbo.sysschedules_localserver_view as sched
      ON jsched.schedule_id = sched.schedule_id
  WHERE (jsched.job_id = @job_id)
    AND (sched.name = @name)

  -- Need to use sp_update_schedule to update this ambiguous schedule name
  IF(@sched_count > 1)
  BEGIN
    RAISERROR(14375, -1, -1, @name, @job_name)
    RETURN(1) -- Failure
  END

  IF (@schedule_id IS NULL)
  BEGIN
   --raise an explicit message if the schedule does exist but isn't attached to this job
   IF EXISTS(SELECT * 
           FROM sysschedules_localserver_view
              WHERE (name = @name))
   BEGIN
      RAISERROR(14374, -1, -1, @name, @job_name)
   END
   ELSE
    BEGIN
      --If the schedule is from an MSX and a sysadmin is calling report a specific 'MSX' message
      IF(PROGRAM_NAME() NOT LIKE N'SQLAgent%' AND
         ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1 AND
         EXISTS(SELECT * 
                FROM msdb.dbo.sysschedules as sched
                  JOIN msdb.dbo.sysoriginatingservers_view as svr
                    ON sched.originating_server_id = svr.originating_server_id
                  JOIN msdb.dbo.sysjobschedules as js 
                    ON sched.schedule_id = js.schedule_id
                WHERE (svr.master_server = 1) AND
                      (sched.name = @name) AND
                      (js.job_id = @job_id)))
     BEGIN
       RAISERROR(14274, -1, -1)
     END
      ELSE
      BEGIN
        --Generic message that the schedule doesn't exist
        RAISERROR(14262, -1, -1, 'Schedule Name', @name)
      END
   END

   RETURN(1) -- Failure
  END

  -- Set the x_ (existing) variables
  SELECT @x_name                   = name,
         @x_enabled                = enabled,
         @x_freq_type              = freq_type,
         @x_freq_interval          = freq_interval,
         @x_freq_subday_type       = freq_subday_type,
         @x_freq_subday_interval   = freq_subday_interval,
         @x_freq_relative_interval = freq_relative_interval,
         @x_freq_recurrence_factor = freq_recurrence_factor,
         @x_active_start_date      = active_start_date,
         @x_active_end_date        = active_end_date,
         @x_active_start_time      = active_start_time,
         @x_active_end_time        = active_end_time
  FROM msdb.dbo.sysschedules_localserver_view
  WHERE (schedule_id = @schedule_id )

  
  -- Fill out the values for all non-supplied parameters from the existing values
  IF (@new_name               IS NULL) SELECT @new_name               = @x_name
  IF (@enabled                IS NULL) SELECT @enabled                = @x_enabled
  IF (@freq_type              IS NULL) SELECT @freq_type              = @x_freq_type
  IF (@freq_interval          IS NULL) SELECT @freq_interval          = @x_freq_interval
  IF (@freq_subday_type       IS NULL) SELECT @freq_subday_type       = @x_freq_subday_type
  IF (@freq_subday_interval   IS NULL) SELECT @freq_subday_interval   = @x_freq_subday_interval
  IF (@freq_relative_interval IS NULL) SELECT @freq_relative_interval = @x_freq_relative_interval
  IF (@freq_recurrence_factor IS NULL) SELECT @freq_recurrence_factor = @x_freq_recurrence_factor
  IF (@active_start_date      IS NULL) SELECT @active_start_date      = @x_active_start_date
  IF (@active_end_date        IS NULL) SELECT @active_end_date        = @x_active_end_date
  IF (@active_start_time      IS NULL) SELECT @active_start_time      = @x_active_start_time
  IF (@active_end_time        IS NULL) SELECT @active_end_time        = @x_active_end_time

  -- Check schedule (frequency and owner) parameters
  EXECUTE @retval = sp_verify_schedule @schedule_id             = @schedule_id,
                                       @name                    = @new_name,
                                       @enabled                 = @enabled,
                                       @freq_type               = @freq_type,
                                       @freq_interval           = @freq_interval            OUTPUT,
                                       @freq_subday_type        = @freq_subday_type         OUTPUT,
                                       @freq_subday_interval    = @freq_subday_interval     OUTPUT,
                                       @freq_relative_interval  = @freq_relative_interval   OUTPUT,
                                       @freq_recurrence_factor  = @freq_recurrence_factor   OUTPUT,
                                       @active_start_date       = @active_start_date        OUTPUT,
                                       @active_start_time       = @active_start_time        OUTPUT,
                                       @active_end_date         = @active_end_date          OUTPUT,
                                       @active_end_time         = @active_end_time          OUTPUT,
                                       @owner_sid               = @owner_sid
  IF (@retval <> 0)
    RETURN(1) -- Failure


  -- Update the JobSchedule
  UPDATE msdb.dbo.sysschedules
  SET name                   = @new_name,
      enabled                = @enabled,
      freq_type              = @freq_type,
      freq_interval          = @freq_interval,
      freq_subday_type       = @freq_subday_type,
      freq_subday_interval   = @freq_subday_interval,
      freq_relative_interval = @freq_relative_interval,
      freq_recurrence_factor = @freq_recurrence_factor,
      active_start_date      = @active_start_date,
      active_end_date        = @active_end_date,
      active_start_time      = @active_start_time,
      active_end_time        = @active_end_time,
      date_modified          = GETDATE(),
      version_number         = version_number + 1
  WHERE (schedule_id = @schedule_id)

  SELECT @retval = @@error

  -- Update the job's version/last-modified information
  UPDATE msdb.dbo.sysjobs
  SET version_number = version_number + 1,
      date_modified = GETDATE()
  WHERE (job_id = @job_id)

  -- Notify SQLServerAgent of the change, but only if we know the job has been cached
  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysjobservers
              WHERE (job_id = @job_id)
                AND (server_id = 0)))
  BEGIN
    EXECUTE msdb.dbo.sp_sqlagent_notify @op_type     = N'S',
                                        @job_id      = @job_id,
                                        @schedule_id = @schedule_id,
                                        @action_type = N'U'
  END

  -- For a multi-server job, remind the user that they need to call sp_post_msx_operation
  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysjobservers
              WHERE (job_id = @job_id)
                AND (server_id <> 0)))
    -- Instruct the tsx servers to pick up the altered schedule
    IF (@automatic_post = 1)
    BEGIN
      DECLARE @schedule_uid UNIQUEIDENTIFIER
      SELECT @schedule_uid = schedule_uid 
      FROM sysschedules 
      WHERE schedule_id = @schedule_id

      IF(NOT @schedule_uid IS NULL)
      BEGIN
        -- sp_post_msx_operation will do nothing if the schedule isn't assigned to any tsx machines 
        EXECUTE sp_post_msx_operation @operation = 'INSERT', @object_type = 'SCHEDULE', @schedule_uid = @schedule_uid
      END
    END
    ELSE
      RAISERROR(14547, 0, 1, N'INSERT', N'sp_post_msx_operation')

  -- Automatic addition and removal of -Continous parameter for replication agent
  EXECUTE sp_update_replication_job_parameter @job_id = @job_id,
                                              @old_freq_type = @x_freq_type,
                                              @new_freq_type = @freq_type

  RETURN(@retval) -- 0 means success
END

dbo,sp_update_jobstep,CREATE PROCEDURE sp_update_jobstep
  @job_id                 UNIQUEIDENTIFIER = NULL, -- Must provide either this or job_name
  @job_name               sysname          = NULL, -- Not updatable (provided for identification purposes only)
  @step_id                INT,                     -- Not updatable (provided for identification purposes only)
  @step_name              sysname          = NULL,
  @subsystem              NVARCHAR(40)     = NULL,
  @command                NVARCHAR(max)    = NULL,
  @additional_parameters  NVARCHAR(max)    = NULL,
  @cmdexec_success_code   INT              = NULL,
  @on_success_action      TINYINT          = NULL,
  @on_success_step_id     INT              = NULL,
  @on_fail_action         TINYINT          = NULL,
  @on_fail_step_id        INT              = NULL,
  @server                 sysname          = NULL,
  @database_name          sysname          = NULL,
  @database_user_name     sysname          = NULL,
  @retry_attempts         INT              = NULL,
  @retry_interval         INT              = NULL,
  @os_run_priority        INT              = NULL,
  @output_file_name       NVARCHAR(200)    = NULL,
  @flags                  INT              = NULL,
  @proxy_id            int          = NULL,
  @proxy_name          sysname         = NULL
  -- mutual exclusive; must specify only one of above 2 parameters to 
  -- identify the proxy. 
AS
BEGIN
  DECLARE @retval                 INT
  DECLARE @os_run_priority_code   INT
  DECLARE @step_id_as_char        VARCHAR(10)
  DECLARE @new_step_name          sysname
  DECLARE @x_step_name            sysname
  DECLARE @x_subsystem            NVARCHAR(40)
  DECLARE @x_command              NVARCHAR(max)
  DECLARE @x_flags                INT
  DECLARE @x_cmdexec_success_code INT
  DECLARE @x_on_success_action    TINYINT
  DECLARE @x_on_success_step_id   INT
  DECLARE @x_on_fail_action       TINYINT
  DECLARE @x_on_fail_step_id      INT
  DECLARE @x_server               sysname
  DECLARE @x_database_name        sysname
  DECLARE @x_database_user_name   sysname
  DECLARE @x_retry_attempts       INT
  DECLARE @x_retry_interval       INT
  DECLARE @x_os_run_priority      INT
  DECLARE @x_output_file_name     NVARCHAR(200)
  DECLARE @x_proxy_id             INT         
  DECLARE @x_last_run_outcome     TINYINT      -- Not updatable (but may be in future)
  DECLARE @x_last_run_duration    INT          -- Not updatable (but may be in future)
  DECLARE @x_last_run_retries     INT          -- Not updatable (but may be in future)
  DECLARE @x_last_run_date        INT          -- Not updatable (but may be in future)
  DECLARE @x_last_run_time        INT          -- Not updatable (but may be in future)

  DECLARE @new_proxy_id           INT
  DECLARE @subsystem_id           INT
  DECLARE @auto_proxy_name        sysname
  DECLARE @job_owner_sid        VARBINARY(85)
  
  SET NOCOUNT ON

  SELECT @new_proxy_id = NULL

  -- Remove any leading/trailing spaces from parameters
  SELECT @step_name          = LTRIM(RTRIM(@step_name))
  SELECT @subsystem          = LTRIM(RTRIM(@subsystem))
  SELECT @command            = LTRIM(RTRIM(@command))
  SELECT @server             = LTRIM(RTRIM(@server))
  SELECT @database_name      = LTRIM(RTRIM(@database_name))
  SELECT @database_user_name = LTRIM(RTRIM(@database_user_name))
  SELECT @output_file_name   = LTRIM(RTRIM(@output_file_name))
  SELECT @proxy_name         = LTRIM(RTRIM(@proxy_name))

  -- Make sure Dts is translated into new subsystem's name SSIS
  IF (@subsystem IS NOT NULL AND UPPER(@subsystem collate SQL_Latin1_General_CP1_CS_AS) = N'DTS')
  BEGIN
    SET @subsystem = N'SSIS'
  END

  -- Only sysadmin's or db_owner's of msdb can directly change
  -- an existing job step to use one of the replication
  -- subsystems
  IF (UPPER(@subsystem collate SQL_Latin1_General_CP1_CS_AS) IN
                        (N'DISTRIBUTION',
                         N'SNAPSHOT',
                         N'LOGREADER',
                         N'MERGE',
                         N'QUEUEREADER'))
  BEGIN
    IF NOT ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1) OR
            (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1) OR
            (UPPER(USER_NAME() collate SQL_Latin1_General_CP1_CS_AS) = N'DBO'))
    BEGIN
      RAISERROR(14260, -1, -1)
      RETURN(1) -- Failure
    END
  END

  EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                              '@job_id',
                                               @job_name OUTPUT,
                                               @job_id   OUTPUT,
                                               @owner_sid = @job_owner_sid OUTPUT
  IF (@retval <> 0)
    RETURN(1) -- Failure

  -- Check permissions beyond what's checked by the sysjobs_view
  -- SQLAgentReader and SQLAgentOperator roles that can see all jobs
  -- cannot modify jobs they do not own
  IF (@job_owner_sid <> SUSER_SID()                   -- does not own the job
     AND (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))   -- is not sysadmin
  BEGIN
   RAISERROR(14525, -1, -1);
   RETURN(1) -- Failure
  END

  -- Check that the step exists
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysjobsteps
                  WHERE (job_id = @job_id)
                    AND (step_id = @step_id)))
  BEGIN
    SELECT @step_id_as_char = CONVERT(VARCHAR(10), @step_id)
    RAISERROR(14262, -1, -1, '@step_id', @step_id_as_char)
    RETURN(1) -- Failure
  END

  -- check proxy identifiers only if a proxy has been provided
  -- @proxy_name = N'' is a special case to allow change of an existing proxy with NULL
  IF (@proxy_id IS NOT NULL) OR (@proxy_name IS NOT NULL AND @proxy_name <> N'') 
  BEGIN
    EXECUTE @retval = sp_verify_proxy_identifiers '@proxy_name',
                                                  '@proxy_id',
                                                   @proxy_name OUTPUT,
                                                   @proxy_id   OUTPUT
    IF (@retval <> 0)
      RETURN(1) -- Failure

     SELECT @new_proxy_id  = @proxy_id

  END

  -- Check authority (only SQLServerAgent can modify a step of a non-local job)
  EXECUTE @retval = sp_verify_jobproc_caller @job_id = @job_id, @program_name = N'SQLAgent%'
  IF (@retval <> 0)
    RETURN(@retval)

  -- Set the x_ (existing) variables
  SELECT @x_step_name            = step_name,
         @x_subsystem            = subsystem,
         @x_command              = command,
         @x_flags                = flags,
         @x_cmdexec_success_code = cmdexec_success_code,
         @x_on_success_action    = on_success_action,
         @x_on_success_step_id   = on_success_step_id,
         @x_on_fail_action       = on_fail_action,
         @x_on_fail_step_id      = on_fail_step_id,
         @x_server               = server,
         @x_database_name        = database_name,
         @x_database_user_name   = database_user_name,
         @x_retry_attempts       = retry_attempts,
         @x_retry_interval       = retry_interval,
         @x_os_run_priority      = os_run_priority,
         @x_output_file_name     = output_file_name,
         @x_proxy_id             = proxy_id,
         @x_last_run_outcome     = last_run_outcome,
         @x_last_run_duration    = last_run_duration,
         @x_last_run_retries     = last_run_retries,
         @x_last_run_date        = last_run_date,
         @x_last_run_time        = last_run_time
  FROM msdb.dbo.sysjobsteps
  WHERE (job_id = @job_id)
    AND (step_id = @step_id)

  IF ((@step_name IS NOT NULL) AND (@step_name <> @x_step_name))
    SELECT @new_step_name = @step_name

  -- Fill out the values for all non-supplied parameters from the existing values
  IF (@step_name            IS NULL) SELECT @step_name            = @x_step_name
  IF (@subsystem            IS NULL) SELECT @subsystem            = @x_subsystem
  IF (@command              IS NULL) SELECT @command              = @x_command
  IF (@flags                IS NULL) SELECT @flags                = @x_flags
  IF (@cmdexec_success_code IS NULL) SELECT @cmdexec_success_code = @x_cmdexec_success_code
  IF (@on_success_action    IS NULL) SELECT @on_success_action    = @x_on_success_action
  IF (@on_success_step_id   IS NULL) SELECT @on_success_step_id   = @x_on_success_step_id
  IF (@on_fail_action       IS NULL) SELECT @on_fail_action       = @x_on_fail_action
  IF (@on_fail_step_id      IS NULL) SELECT @on_fail_step_id      = @x_on_fail_step_id
  IF (@server               IS NULL) SELECT @server               = @x_server
  IF (@database_name        IS NULL) SELECT @database_name        = @x_database_name
  IF (@database_user_name   IS NULL) SELECT @database_user_name   = @x_database_user_name
  IF (@retry_attempts       IS NULL) SELECT @retry_attempts       = @x_retry_attempts
  IF (@retry_interval       IS NULL) SELECT @retry_interval       = @x_retry_interval
  IF (@os_run_priority      IS NULL) SELECT @os_run_priority      = @x_os_run_priority
  IF (@output_file_name     IS NULL) SELECT @output_file_name     = @x_output_file_name
  IF (@proxy_id             IS NULL) SELECT @new_proxy_id         = @x_proxy_id

  --if an empty proxy_name is supplied the proxy is removed
  IF @proxy_name = N'' SELECT @new_proxy_id = NULL
  -- Turn [nullable] empty string parameters into NULLs
  IF (@command            = N'') SELECT @command            = NULL
  IF (@server             = N'') SELECT @server             = NULL
  IF (@database_name      = N'') SELECT @database_name      = NULL
  IF (@database_user_name = N'') SELECT @database_user_name = NULL
  IF (@output_file_name   = N'') SELECT @output_file_name   = NULL


  -- Check new values
  EXECUTE @retval = sp_verify_jobstep @job_id,
                                      @step_id,
                                      @new_step_name,
                                      @subsystem,
                                      @command,
                                      @server,
                                      @on_success_action,
                                      @on_success_step_id,
                                      @on_fail_action,
                                      @on_fail_step_id,
                                      @os_run_priority,
                                      @database_name      OUTPUT,
                                      @database_user_name OUTPUT,
                                      @flags,
                                      @output_file_name,
                                               @new_proxy_id
  IF (@retval <> 0)
    RETURN(1) -- Failure

  BEGIN TRANSACTION

    -- Update the job's version/last-modified information
    UPDATE msdb.dbo.sysjobs
    SET version_number = version_number + 1,
        date_modified = GETDATE()
    WHERE (job_id = @job_id)

    -- Update the step
    UPDATE msdb.dbo.sysjobsteps
    SET step_name             = @step_name,
        subsystem             = @subsystem,
        command               = @command,
        flags                 = @flags,
        additional_parameters = @additional_parameters,
        cmdexec_success_code  = @cmdexec_success_code,
        on_success_action     = @on_success_action,
        on_success_step_id    = @on_success_step_id,
        on_fail_action        = @on_fail_action,
        on_fail_step_id       = @on_fail_step_id,
        server                = @server,
        database_name         = @database_name,
        database_user_name    = @database_user_name,
        retry_attempts        = @retry_attempts,
        retry_interval        = @retry_interval,
        os_run_priority       = @os_run_priority,
        output_file_name      = @output_file_name,
        last_run_outcome      = @x_last_run_outcome,
        last_run_duration     = @x_last_run_duration,
        last_run_retries      = @x_last_run_retries,
        last_run_date         = @x_last_run_date,
        last_run_time         = @x_last_run_time,
          proxy_id                 = @new_proxy_id
    WHERE (job_id = @job_id)
      AND (step_id = @step_id)


  COMMIT TRANSACTION

  -- For a multi-server job, push changes to the target servers
  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysjobservers
              WHERE (job_id = @job_id)
                AND (server_id <> 0)))
  BEGIN
    EXECUTE msdb.dbo.sp_post_msx_operation 'INSERT', 'JOB', @job_id
  END

  RETURN(0) -- Success
END

dbo,sp_update_log_shipping_monitor_info,CREATE PROCEDURE sp_update_log_shipping_monitor_info
  @primary_server_name                 sysname,
  @primary_database_name               sysname,
  @secondary_server_name               sysname,
  @secondary_database_name             sysname,
  @backup_threshold                    INT = NULL,
  @backup_threshold_alert              INT = NULL,
  @backup_threshold_alert_enabled      BIT = NULL,
  @backup_outage_start_time            INT = NULL,
  @backup_outage_end_time              INT = NULL,
  @backup_outage_weekday_mask          INT = NULL,
  @copy_enabled                        BIT = NULL,
  @load_enabled                        BIT = NULL,
  @out_of_sync_threshold               INT = NULL,
  @out_of_sync_threshold_alert         INT = NULL,
  @out_of_sync_threshold_alert_enabled BIT = NULL,
  @out_of_sync_outage_start_time       INT = NULL,
  @out_of_sync_outage_end_time         INT = NULL,
  @out_of_sync_outage_weekday_mask     INT = NULL
AS BEGIN
  SET NOCOUNT ON
  DECLARE @_backup_threshold                    INT
  DECLARE @_backup_threshold_alert              INT
  DECLARE @_backup_threshold_alert_enabled      BIT
  DECLARE @_backup_outage_start_time            INT
  DECLARE @_backup_outage_end_time              INT
  DECLARE @_backup_outage_weekday_mask          INT
  DECLARE @_copy_enabled                        BIT
  DECLARE @_load_enabled                        BIT
  DECLARE @_out_of_sync_threshold               INT
  DECLARE @_out_of_sync_threshold_alert         INT
  DECLARE @_out_of_sync_threshold_alert_enabled BIT
  DECLARE @_out_of_sync_outage_start_time       INT
  DECLARE @_out_of_sync_outage_end_time         INT
  DECLARE @_out_of_sync_outage_weekday_mask     INT

  -- check that the primary exists
  IF (NOT EXISTS (SELECT * FROM msdb.dbo.log_shipping_primaries WHERE primary_server_name = @primary_server_name AND primary_database_name = @primary_database_name))
  BEGIN
    DECLARE @pp sysname
    SELECT @pp = @primary_server_name + N'.' + @primary_database_name
    RAISERROR (14262, 16, 1, N'primary_server_name.primary_database_name', @pp)
    RETURN (1) -- error
  END

  -- check that the secondary exists
  IF (NOT EXISTS (SELECT * FROM msdb.dbo.log_shipping_secondaries WHERE secondary_server_name = @secondary_server_name AND secondary_database_name = @secondary_database_name))
  BEGIN
    DECLARE @sp sysname
    SELECT @sp = @secondary_server_name + N'.' + @secondary_database_name
    RAISERROR (14262, 16, 1, N'secondary_server_name.secondary_database_name', @sp)
    RETURN (1) -- error
  END

  -- load the original variables

 SELECT
    @_backup_threshold                    = backup_threshold,
    @_backup_threshold_alert              = p.threshold_alert,
    @_backup_threshold_alert_enabled      = p.threshold_alert_enabled,
    @_backup_outage_start_time            = p.planned_outage_start_time,
    @_backup_outage_end_time              = p.planned_outage_end_time,
    @_backup_outage_weekday_mask          = p.planned_outage_weekday_mask,
    @_copy_enabled                        = copy_enabled,
    @_load_enabled                        = load_enabled,
    @_out_of_sync_threshold               = out_of_sync_threshold,
    @_out_of_sync_threshold_alert         = s.threshold_alert,
    @_out_of_sync_threshold_alert_enabled = s.threshold_alert_enabled,
    @_out_of_sync_outage_start_time       = s.planned_outage_start_time,
    @_out_of_sync_outage_weekday_mask     = s.planned_outage_weekday_mask,
    @_out_of_sync_outage_end_time         = s.planned_outage_end_time
  FROM msdb.dbo.log_shipping_primaries p, msdb.dbo.log_shipping_secondaries s
  WHERE 
    p.primary_id            = s.primary_id           AND
    primary_server_name     = @primary_server_name   AND
    primary_database_name   = @primary_database_name AND
    secondary_server_name   = @secondary_server_name AND
    secondary_database_name = @secondary_database_name

  SELECT @_backup_threshold                    = ISNULL (@backup_threshold,                    @_backup_threshold)
  SELECT @_backup_threshold_alert              = ISNULL (@backup_threshold_alert,              @_backup_threshold_alert)
  SELECT @_backup_threshold_alert_enabled      = ISNULL (@backup_threshold_alert_enabled,      @_backup_threshold_alert_enabled)
  SELECT @_backup_outage_start_time            = ISNULL (@backup_outage_start_time,            @_backup_outage_start_time)
  SELECT @_backup_outage_end_time              = ISNULL (@backup_outage_end_time,              @_backup_outage_end_time)
  SELECT @_backup_outage_weekday_mask          = ISNULL (@backup_outage_weekday_mask,          @_backup_outage_weekday_mask)
  SELECT @_copy_enabled                        = ISNULL (@copy_enabled,                        @_copy_enabled)
  SELECT @_load_enabled                        = ISNULL (@load_enabled,                        @_load_enabled)
  SELECT @_out_of_sync_threshold               = ISNULL (@out_of_sync_threshold,               @_out_of_sync_threshold)
  SELECT @_out_of_sync_threshold_alert         = ISNULL (@out_of_sync_threshold_alert,         @_out_of_sync_threshold_alert)
  SELECT @_out_of_sync_threshold_alert_enabled = ISNULL (@out_of_sync_threshold_alert_enabled, @_out_of_sync_threshold_alert_enabled)
  SELECT @_out_of_sync_outage_start_time       = ISNULL (@out_of_sync_outage_start_time,       @_out_of_sync_outage_start_time)
  SELECT @_out_of_sync_outage_end_time         = ISNULL (@out_of_sync_outage_end_time,         @_out_of_sync_outage_end_time)
  SELECT @_out_of_sync_outage_weekday_mask     = ISNULL (@out_of_sync_outage_weekday_mask,     @_out_of_sync_outage_weekday_mask)

  -- updates
  UPDATE msdb.dbo.log_shipping_primaries SET
    backup_threshold            = @_backup_threshold,
    threshold_alert             = @_backup_threshold_alert,
    threshold_alert_enabled     = @_backup_threshold_alert_enabled,
    planned_outage_start_time   = @_backup_outage_start_time,
    planned_outage_end_time     = @_backup_outage_end_time,
    planned_outage_weekday_mask = @_backup_outage_weekday_mask
  WHERE primary_server_name = @primary_server_name AND primary_database_name = @primary_database_name

  UPDATE msdb.dbo.log_shipping_secondaries SET
    copy_enabled                = @_copy_enabled,
    load_enabled                = @_load_enabled,
    out_of_sync_threshold       = @_out_of_sync_threshold,
    threshold_alert             = @_out_of_sync_threshold_alert,
    threshold_alert_enabled     = @_out_of_sync_threshold_alert_enabled,
    planned_outage_start_time   = @_out_of_sync_outage_start_time,
    planned_outage_end_time     = @_out_of_sync_outage_weekday_mask,
    planned_outage_weekday_mask = @_out_of_sync_outage_end_time
  WHERE secondary_server_name = @secondary_server_name AND secondary_database_name = @secondary_database_name
RETURN(0)
END

dbo,sp_update_notification,CREATE PROCEDURE sp_update_notification
  @alert_name          sysname,
  @operator_name       sysname,
  @notification_method TINYINT -- 1 = Email, 2 = Pager, 4 = NetSend, 7 = All
AS
BEGIN
  DECLARE @alert_id             INT
  DECLARE @operator_id          INT
  DECLARE @notification         NVARCHAR(512)
  DECLARE @retval               INT
  DECLARE @old_has_notification INT
  DECLARE @new_has_notification INT
  DECLARE @res_notification     NVARCHAR(100)

  SET NOCOUNT ON

  SELECT @res_notification = FORMATMESSAGE(14210)

  -- Remove any leading/trailing spaces from parameters
  SELECT @alert_name    = LTRIM(RTRIM(@alert_name))
  SELECT @operator_name = LTRIM(RTRIM(@operator_name))

  -- Only a sysadmin can do this
  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))
  BEGIN
    RAISERROR(15003, 16, 1, N'sysadmin')
    RETURN(1) -- Failure
  END

  -- Check if the Notification is valid
  EXECUTE sp_verify_notification @alert_name,
                                 @operator_name,
                                 @notification_method,
                                 @alert_id     OUTPUT,
                                 @operator_id  OUTPUT

  -- Check if this notification exists
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysnotifications
                  WHERE (alert_id = @alert_id)
                    AND (operator_id = @operator_id)))
  BEGIN
    SELECT @notification = @alert_name + N' / ' + @operator_name
    RAISERROR(14262, 16, 1, @res_notification, @notification)
    RETURN(1) -- Failure
  END

  SELECT @old_has_notification = has_notification
  FROM msdb.dbo.sysalerts
  WHERE (id = @alert_id)

  -- Do the UPDATE
  UPDATE msdb.dbo.sysnotifications
  SET notification_method = @notification_method
  WHERE (alert_id = @alert_id)
    AND (operator_id = @operator_id)

  SELECT @retval = @@error

  SELECT @new_has_notification = has_notification
  FROM msdb.dbo.sysalerts
  WHERE (id = @alert_id)

  -- Notify SQLServerAgent of the change - if any - to has_notifications
  IF (@old_has_notification <> @new_has_notification)
    EXECUTE msdb.dbo.sp_sqlagent_notify @op_type       = N'A',
                                          @alert_id    = @alert_id,
                                          @action_type = N'U'

  RETURN(@retval) -- 0 means success
END

dbo,sp_update_operator,CREATE PROCEDURE sp_update_operator
  @name                      sysname,
  @new_name                  sysname       = NULL,
  @enabled                   TINYINT       = NULL,
  @email_address             NVARCHAR(100) = NULL,
  @pager_address             NVARCHAR(100) = NULL,
  @weekday_pager_start_time  INT           = NULL, -- HHMMSS using 24 hour clock
  @weekday_pager_end_time    INT           = NULL, -- As above
  @saturday_pager_start_time INT           = NULL, -- As above
  @saturday_pager_end_time   INT           = NULL, -- As above
  @sunday_pager_start_time   INT           = NULL, -- As above
  @sunday_pager_end_time     INT           = NULL, -- As above
  @pager_days                TINYINT       = NULL,
  @netsend_address           NVARCHAR(100) = NULL, -- New for 7.0
  @category_name             sysname       = NULL  -- New for 7.0
AS
BEGIN
  DECLARE @x_enabled                   TINYINT
  DECLARE @x_email_address             NVARCHAR(100)
  DECLARE @x_pager_address             NVARCHAR(100)
  DECLARE @x_weekday_pager_start_time  INT
  DECLARE @x_weekday_pager_end_time    INT
  DECLARE @x_saturday_pager_start_time INT
  DECLARE @x_saturday_pager_end_time   INT
  DECLARE @x_sunday_pager_start_time   INT
  DECLARE @x_sunday_pager_end_time     INT
  DECLARE @x_pager_days                TINYINT
  DECLARE @x_netsend_address           NVARCHAR(100)
  DECLARE @x_category_id               INT

  DECLARE @return_code                 INT
  DECLARE @notification_method         INT
  DECLARE @alert_fail_safe_operator    sysname
  DECLARE @current_msx_server          sysname
  DECLARE @category_id                 INT

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @name            = LTRIM(RTRIM(@name))
  SELECT @new_name        = LTRIM(RTRIM(@new_name))
  SELECT @email_address   = LTRIM(RTRIM(@email_address))
  SELECT @pager_address   = LTRIM(RTRIM(@pager_address))
  SELECT @netsend_address = LTRIM(RTRIM(@netsend_address))
  SELECT @category_name   = LTRIM(RTRIM(@category_name))

  -- Only a sysadmin can do this
  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))
  BEGIN
    RAISERROR(15003, 16, 1, N'sysadmin')
    RETURN(1) -- Failure
  END

  -- Check if this Operator exists
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysoperators
                  WHERE (name = @name)))
  BEGIN
    RAISERROR(14262, 16, 1, '@name', @name)
    RETURN(1) -- Failure
  END

  -- Check if this operator is 'MSXOperator'
  IF (@name = N'MSXOperator')
  BEGIN
    -- Disallow the update operation if we're at a TSX for all callers other than xp_msx_enlist
    EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',
                                           N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                           N'MSXServerName',
                                           @current_msx_server OUTPUT,
                                           N'no_output'
    IF ((@current_msx_server IS NOT NULL) AND (PROGRAM_NAME() <> N'xp_msx_enlist'))
    BEGIN
      RAISERROR(14223, 16, 1, 'MSXOperator', 'TSX')
      RETURN(1) -- Failure
    END
  END

  -- Get existing (@x_) operator property values
  SELECT @x_enabled                   = enabled,
         @x_email_address             = email_address,
         @x_pager_address             = pager_address,
         @x_weekday_pager_start_time  = weekday_pager_start_time,
         @x_weekday_pager_end_time    = weekday_pager_end_time,
         @x_saturday_pager_start_time = saturday_pager_start_time,
         @x_saturday_pager_end_time   = saturday_pager_end_time,
         @x_sunday_pager_start_time   = sunday_pager_start_time,
         @x_sunday_pager_end_time     = sunday_pager_end_time,
         @x_pager_days                = pager_days,
         @x_netsend_address           = netsend_address,
         @x_category_id               = category_id
  FROM msdb.dbo.sysoperators
  WHERE (name = @name)

  -- Fill out the values for all non-supplied parameters from the existsing values
  IF (@enabled                   IS NULL) SELECT @enabled                   = @x_enabled
  IF (@email_address             IS NULL) SELECT @email_address             = @x_email_address
  IF (@pager_address             IS NULL) SELECT @pager_address             = @x_pager_address
  IF (@weekday_pager_start_time  IS NULL) SELECT @weekday_pager_start_time  = @x_weekday_pager_start_time
  IF (@weekday_pager_end_time    IS NULL) SELECT @weekday_pager_end_time    = @x_weekday_pager_end_time
  IF (@saturday_pager_start_time IS NULL) SELECT @saturday_pager_start_time = @x_saturday_pager_start_time
  IF (@saturday_pager_end_time   IS NULL) SELECT @saturday_pager_end_time   = @x_saturday_pager_end_time
  IF (@sunday_pager_start_time   IS NULL) SELECT @sunday_pager_start_time   = @x_sunday_pager_start_time
  IF (@sunday_pager_end_time     IS NULL) SELECT @sunday_pager_end_time     = @x_sunday_pager_end_time
  IF (@pager_days                IS NULL) SELECT @pager_days                = @x_pager_days
  IF (@netsend_address           IS NULL) SELECT @netsend_address           = @x_netsend_address
  IF (@category_name             IS NULL) SELECT @category_name = name FROM msdb.dbo.syscategories WHERE (category_id = @x_category_id)

  IF (@category_name IS NULL)
  BEGIN
    SELECT @category_name = name
    FROM msdb.dbo.syscategories
    WHERE (category_id = 99)
  END

  -- Turn [nullable] empty string parameters into NULLs
  IF (@email_address   = N'') SELECT @email_address   = NULL
  IF (@pager_address   = N'') SELECT @pager_address   = NULL
  IF (@netsend_address = N'') SELECT @netsend_address = NULL
  IF (@category_name   = N'') SELECT @category_name   = NULL

  -- Verify the operator
  EXECUTE @return_code = sp_verify_operator @new_name,
                                            @enabled,
                                            @pager_days,
                                            @weekday_pager_start_time,
                                            @weekday_pager_end_time,
                                            @saturday_pager_start_time,
                                            @saturday_pager_end_time,
                                            @sunday_pager_start_time,
                                            @sunday_pager_end_time,
                                            @category_name,
                                            @category_id OUTPUT
  IF (@return_code <> 0)
    RETURN(1) -- Failure

  -- If no new name is supplied, use the old one
  -- NOTE: We must do this AFTER calling sp_verify_operator.
  IF (@new_name IS NULL)
    SELECT @new_name = @name
  ELSE
  BEGIN
    -- You can't rename the MSXOperator
    IF (@name = N'MSXOperator')
    BEGIN
      RAISERROR(14222, 16, 1, 'MSXOperator')
      RETURN(1) -- Failure
    END
  END

  -- Do the UPDATE
  UPDATE msdb.dbo.sysoperators
  SET name                      = @new_name,
      enabled                   = @enabled,
      email_address             = @email_address,
      pager_address             = @pager_address,
      weekday_pager_start_time  = @weekday_pager_start_time,
      weekday_pager_end_time    = @weekday_pager_end_time,
      saturday_pager_start_time = @saturday_pager_start_time,
      saturday_pager_end_time   = @saturday_pager_end_time,
      sunday_pager_start_time   = @sunday_pager_start_time,
      sunday_pager_end_time     = @sunday_pager_end_time,
      pager_days                = @pager_days,
      netsend_address           = @netsend_address,
      category_id               = @category_id
  WHERE (name = @name)

  -- Check if the operator is 'MSXOperator', in which case we need to re-enlist all the targets
  -- so that they will download the new MSXOperator details
  IF ((@name = N'MSXOperator') AND ((SELECT COUNT(*) FROM msdb.dbo.systargetservers) > 0))
    EXECUTE msdb.dbo.sp_post_msx_operation 'RE-ENLIST', 'SERVER', 0x00

  -- Check if this operator is the FailSafe Operator
  EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',
                                         N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                         N'AlertFailSafeOperator',
                                         @alert_fail_safe_operator OUTPUT,
                                         N'no_output'

  -- If it is, we update the 4 'AlertFailSafe...' registry entries and AlertNotificationMethod
  IF (LTRIM(RTRIM(@alert_fail_safe_operator)) = @name)
  BEGIN
    -- Update AlertFailSafeX values
    EXECUTE master.dbo.xp_instance_regwrite N'HKEY_LOCAL_MACHINE',
                                            N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                            N'AlertFailSafeOperator',
                                            N'REG_SZ',
                                            @new_name
    EXECUTE master.dbo.xp_instance_regwrite N'HKEY_LOCAL_MACHINE',
                                            N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                            N'AlertFailSafeEmailAddress',
                                            N'REG_SZ',
                                            @email_address
    EXECUTE master.dbo.xp_instance_regwrite N'HKEY_LOCAL_MACHINE',
                                            N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                            N'AlertFailSafePagerAddress',
                                            N'REG_SZ',
                                            @pager_address
    EXECUTE master.dbo.xp_instance_regwrite N'HKEY_LOCAL_MACHINE',
                                            N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                            N'AlertFailSafeNetSendAddress',
                                            N'REG_SZ',
                                            @netsend_address

    -- Update AlertNotificationMethod values
    EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',
                                           N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                           N'AlertNotificationMethod',
                                           @notification_method OUTPUT,
                                           N'no_output'
    IF (LTRIM(RTRIM(@email_address)) IS NULL)
      SELECT @notification_method = @notification_method & ~1
    IF (LTRIM(RTRIM(@pager_address)) IS NULL)
      SELECT @notification_method = @notification_method & ~2
    IF (LTRIM(RTRIM(@netsend_address)) IS NULL)
      SELECT @notification_method = @notification_method & ~4
    EXECUTE master.dbo.xp_instance_regwrite N'HKEY_LOCAL_MACHINE',
                                            N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                            N'AlertNotificationMethod',
                                            N'REG_DWORD',
                                            @notification_method

    -- And finally, let SQLServerAgent know of the changes
    EXECUTE msdb.dbo.sp_sqlagent_notify @op_type = N'G'
  END

  RETURN(0) -- Success
END
```

