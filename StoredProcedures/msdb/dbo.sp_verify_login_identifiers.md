# dbo.sp_verify_login_identifiers

**Database:** msdb  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_verify_login_identifiers"]
    SP --> NoRefs(["No table dependencies detected"])
```

## Table Dependencies

_No table references detected automatically._

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sp_verify_login_identifiers
   @login_name [nvarchar](256),
   @fixed_server_role [nvarchar](256),
   @msdb_role [nvarchar](256),
   @name [nvarchar](256) OUTPUT,
  @sid  varbinary(85)   OUTPUT,
   @flags   INT OUTPUT
AS
BEGIN
   DECLARE @retval         INT
    DECLARE @raise_error    bit
   SET NOCOUNT ON

   SELECT @flags = -1, @raise_error = 0
  SELECT @sid = NULL

  IF @login_name IS NOT NULL 
   BEGIN
      --check validity
      --use the new optional parameter of SUSER_SID to have a case insensitive comparation for NT users
    SELECT @sid = SUSER_SID(@login_name, 0)
      IF @sid IS NULL
      BEGIN
         RAISERROR(14520, -1, -1, @login_name)
         RETURN(1) -- Failure    
      END
      SELECT @name = @login_name, @flags = 0
   END
  
   IF COALESCE(@login_name, @fixed_server_role, @msdb_role) IS NULL
   BEGIN
      RAISERROR(14519, -1, -1)
      RETURN(1) -- Failure    
   END

  IF @fixed_server_role IS NOT NULL  AND @flags <> -1
      SELECT @raise_error = 1
   ELSE IF @fixed_server_role IS NOT NULL
   --check validity
   BEGIN
      -- IS_SRVROLEMEMBER return NULL for an invalid server role
      IF ISNULL(IS_SRVROLEMEMBER(@fixed_server_role), -1) = -1
      BEGIN
         RAISERROR(14521, -1, -1, @fixed_server_role)
         RETURN(1) -- Failure    
      END   
      SELECT @name = @fixed_server_role, @flags = 1
    SELECT @sid = SUSER_SID(@fixed_server_role)
   END
   
  IF @msdb_role IS NOT NULL  AND @flags <> -1
      SELECT @raise_error = 1
   ELSE IF @msdb_role IS NOT NULL
   BEGIN
      --check the correctness of msdb role
      IF ISNULL(IS_MEMBER(@msdb_role), -1) = -1 
      BEGIN
         RAISERROR(14522, -1, -1, @msdb_role)
         RETURN(1) -- Failure    
      END      
      SELECT @sid = sid from sys.database_principals
      WHERE  UPPER(@msdb_role collate SQL_Latin1_General_CP1_CS_AS) = UPPER(name collate SQL_Latin1_General_CP1_CS_AS)
    AND type = 'R'
    IF @sid IS NULL
      BEGIN
         RAISERROR(14522, -1, -1, @msdb_role)
         RETURN(1) -- Failure    
      END      
      SELECT @name = @msdb_role, @flags = 2
   END

   IF    @raise_error = 1
   BEGIN
      RAISERROR(14519, -1, -1)
      RETURN(1) -- Failure    
   END

  RETURN(0) -- Success
END

dbo,sp_verify_notification,CREATE PROCEDURE sp_verify_notification
  @alert_name          sysname,
  @operator_name       sysname,
  @notification_method TINYINT,
  @alert_id            INT OUTPUT,
  @operator_id         INT OUTPUT
AS
BEGIN
  DECLARE @res_valid_range NVARCHAR(100)

  SET NOCOUNT ON

  SELECT @res_valid_range = FORMATMESSAGE(14208)

  -- Remove any leading/trailing spaces from parameters
  SELECT @alert_name    = LTRIM(RTRIM(@alert_name))
  SELECT @operator_name = LTRIM(RTRIM(@operator_name))

  -- Check if the AlertName is valid
  SELECT @alert_id = id
  FROM msdb.dbo.sysalerts
  WHERE (name = @alert_name)

  IF (@alert_id IS NULL)
  BEGIN
    RAISERROR(14262, 16, 1, '@alert_name', @alert_name)
    RETURN(1) -- Failure
  END

  -- Check if the OperatorName is valid
  SELECT @operator_id = id
  FROM msdb.dbo.sysoperators
  WHERE (name = @operator_name)

  IF (@operator_id IS NULL)
  BEGIN
    RAISERROR(14262, 16, 1, '@operator_name', @operator_name)
    RETURN(1) -- Failure
  END

  -- If we're at a TSX, we disallow using operator 'MSXOperator'
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.systargetservers)) AND
     (@operator_name = N'MSXOperator')
  BEGIN
    RAISERROR(14251, -1, -1, @operator_name)
    RETURN(1) -- Failure
  END

  -- Check if the NotificationMethod is valid
  IF ((@notification_method < 1) OR (@notification_method > 7))
  BEGIN
    RAISERROR(14266, 16, 1, '@notification_method', @res_valid_range)
    RETURN(1) -- Failure
  END

  RETURN(0) -- Success
END

dbo,sp_verify_operator,CREATE PROCEDURE sp_verify_operator
  @name                      sysname,
  @enabled                   TINYINT,
  @pager_days                TINYINT,
  @weekday_pager_start_time  INT,
  @weekday_pager_end_time    INT,
  @saturday_pager_start_time INT,
  @saturday_pager_end_time   INT,
  @sunday_pager_start_time   INT,
  @sunday_pager_end_time     INT,
  @category_name             sysname,
  @category_id               INT OUTPUT
AS
BEGIN
  DECLARE @return_code     TINYINT
  DECLARE @res_valid_range NVARCHAR(100)

  SET NOCOUNT ON

  SELECT @res_valid_range = FORMATMESSAGE(14209)

  -- Remove any leading/trailing spaces from parameters
  SELECT @name          = LTRIM(RTRIM(@name))
  SELECT @category_name = LTRIM(RTRIM(@category_name))

  -- The name must be unique
  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysoperators
              WHERE (name = @name)))
  BEGIN
    RAISERROR(14261, 16, 1, '@name', @name)
    RETURN(1) -- Failure
  END

  -- Enabled must be 0 or 1
  IF (@enabled NOT IN (0, 1))
  BEGIN
    RAISERROR(14266, 16, 1, '@enabled', '0, 1')
    RETURN(1) -- Failure
  END

  -- Check PagerDays
  IF (@pager_days < 0) OR (@pager_days > 127)
  BEGIN
    RAISERROR(14266, 16, 1, '@pager_days', @res_valid_range)
    RETURN(1) -- Failure
  END

  -- Check Start/End Times
  EXECUTE @return_code = sp_verify_job_time @weekday_pager_start_time, '@weekday_pager_start_time'
  IF (@return_code <> 0)
    RETURN(1)

  EXECUTE @return_code = sp_verify_job_time @weekday_pager_end_time, '@weekday_pager_end_time'
  IF (@return_code <> 0)
    RETURN(1)

  EXECUTE @return_code = sp_verify_job_time @saturday_pager_start_time, '@saturday_pager_start_time'
  IF (@return_code <> 0)
    RETURN(1)

  EXECUTE @return_code = sp_verify_job_time @saturday_pager_end_time, '@saturday_pager_end_time'
  IF (@return_code <> 0)
    RETURN(1)

  EXECUTE @return_code = sp_verify_job_time @sunday_pager_start_time, '@sunday_pager_start_time'
  IF (@return_code <> 0)
    RETURN(1)

  EXECUTE @return_code = sp_verify_job_time @sunday_pager_end_time, '@sunday_pager_end_time'
  IF (@return_code <> 0)
    RETURN(1)

  -- Check category name
  IF (@category_name = N'[DEFAULT]')
    SELECT @category_id = 99
  ELSE
  BEGIN
    SELECT @category_id = category_id
    FROM msdb.dbo.syscategories
    WHERE (category_class = 3) -- Operators
      AND (category_type = 3) -- None
      AND (name = @category_name)
  END
  IF (@category_id IS NULL)
  BEGIN
    RAISERROR(14262, -1, -1, '@category_name', @category_name)
    RETURN(1) -- Failure
  END

  RETURN(0)
END
```

