# dbo.sp_syscollector_verify_event_log_id

**Database:** msdb  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_syscollector_verify_event_log_id"]
    dbo_syscollector_execution_log(["dbo.syscollector_execution_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.syscollector_execution_log |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_syscollector_verify_event_log_id]
    @log_id bigint,
    @allow_collection_set_id bit = 0
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @log_id_as_char VARCHAR(36)

    IF (@log_id IS NULL)
    BEGIN
        RAISERROR(14606, -1, -1, '@log_id')
        RETURN (1)
    END
    ELSE IF @allow_collection_set_id = 0
    BEGIN
        IF (NOT EXISTS (SELECT log_id FROM dbo.syscollector_execution_log WHERE log_id = @log_id AND package_id IS NOT NULL))
        BEGIN
            SELECT @log_id_as_char = CONVERT(VARCHAR(36), @log_id)

            RAISERROR(14262, -1, -1, '@log_id', @log_id_as_char)
            RETURN (1)
        END
    END
    ELSE
    BEGIN
        IF (NOT EXISTS (SELECT log_id FROM dbo.syscollector_execution_log WHERE log_id = @log_id))
        BEGIN
            SELECT @log_id_as_char = CONVERT(VARCHAR(36), @log_id)

            RAISERROR(14262, -1, -1, '@log_id', @log_id_as_char)
            RETURN (1)
        END
    END

    RETURN (0)
END

dbo,sp_sysdac_add_history_entry,CREATE PROCEDURE [dbo].[sp_sysdac_add_history_entry]  
    @sequence_id int,
    @instance_id UniqueIdentifier = NULL,
    @action_type tinyint = NULL,
    @action_status tinyint = NULL,
    @dac_object_type tinyint = NULL,
    @required bit = NULL,
    @dac_object_name_pretran sysname = N'',
    @dac_object_name_posttran sysname = N'',
    @sqlscript nvarchar(max) = N'',
    @payload varbinary(max) = NULL,
    @comments varchar(max) = N'',
    @error_string nvarchar(max) = N'',
    @action_id int = NULL OUTPUT
AS  
SET NOCOUNT ON;
BEGIN  
    DECLARE @retval INT  

    DECLARE @null_column sysname    
    SET @null_column = NULL

    IF (@instance_id IS NULL)
        SET @null_column = '@instance_id'
    ELSE IF (@action_type IS NULL)
        SET @null_column = '@action_type'
    ELSE IF (@action_status IS NULL)
        SET @null_column = '@action_status'
    ELSE IF (@dac_object_type IS NULL)
        SET @null_column = '@dac_object_type'
    ELSE IF (@required IS NULL)
        SET @null_column = '@required'

    IF @null_column IS NOT NULL
    BEGIN
        RAISERROR(14043, -1, -1, @null_column, 'sp_sysdac_add_history_entry')
        RETURN(1)
    END

    -- comments is optional. make sure it is non-null
    IF (@comments IS NULL)
    BEGIN
        SET @comments = N''
    END

    --- Ensure the user is either a db_creator or that the package being referred is visible via the package view. 
    --- For non-dbcreators, the package will only be visible if we are the associated dbo or sysadmin and the instance row exists
    IF ((dbo.fn_sysdac_is_dac_creator() != 1) AND
         (NOT EXISTS (SELECT * from dbo.sysdac_instances WHERE instance_id = @instance_id)))
    BEGIN
        RAISERROR(36004, -1, -1)
        RETURN(1)
    END
    
    BEGIN TRAN

    --If the action_id value is not set by the user, this is a new entry and the proc
    --should calculate the next value which is one more than the current max
    IF (@action_id IS NULL)
    BEGIN
        SET @action_id = (
            SELECT ISNULL(MAX(action_id) + 1, 0) 
            FROM dbo.sysdac_history_internal WITH (UPDLOCK, HOLDLOCK))        
    END

    INSERT INTO [dbo].[sysdac_history_internal]
        (action_id, sequence_id, instance_id, action_type, dac_object_type, action_status, required,
         dac_object_name_pretran, dac_object_name_posttran, sqlscript, payload, comments, error_string)
    VALUES
        (@action_id, @sequence_id, @instance_id, @action_type, @dac_object_type, @action_status, @required,
         @dac_object_name_pretran, @dac_object_name_posttran, @sqlscript, @payload, @comments, @error_string)

    COMMIT
    
    
    SELECT @retval = @@error
    RETURN(@retval)
END

dbo,sp_sysdac_add_instance,CREATE PROCEDURE [dbo].[sp_sysdac_add_instance]  
    @type_name sysname,
    @instance_id UniqueIdentifier = NULL,            
    @instance_name sysname,
    @type_version NVARCHAR(64) = NULL,
    @description nvarchar(4000) = N'',
    @type_stream varbinary(max)
AS  
SET NOCOUNT ON;
BEGIN  
    DECLARE @retval INT  

    DECLARE @null_column sysname    
    SET @null_column = NULL

    IF (@type_name IS NULL OR @type_name = N'')
        SET @null_column = '@type_name'
    ELSE IF (@instance_name IS NULL OR @instance_name = N'')
        SET @null_column = '@instance_name'
    ELSE IF (@instance_id IS NULL )
        SET @null_column = '@instance_id'
    ELSE IF( @type_version = N'')
        SET @null_column = '@type_version'
    ELSE IF( @type_stream IS NULL)
        SET @null_column = '@type_stream'
      

    IF @null_column IS NOT NULL
    BEGIN
        RAISERROR(14043, -1, -1, @null_column, 'sp_sysdac_add_instance')
        RETURN(1)
    END

    -- only users that can create a dac can add instances
    if (dbo.fn_sysdac_is_dac_creator() != 1)
    BEGIN
        RAISERROR(36010, -1, -1);
        RETURN(1); -- failure
    END
    
    --instance_name is unique
    IF EXISTS (SELECT * FROM dbo.sysdac_instances_internal WHERE instance_name = @instance_name) 
    BEGIN
        RAISERROR(36001, -1, -1, 'DacInstance', @instance_name)
        RETURN(1)
    END

    --Ensure that the database being referred exists
    IF NOT EXISTS (SELECT * from sys.sysdatabases WHERE name = @instance_name)
    BEGIN
        RAISERROR(36005, -1, -1, @instance_name)
        RETURN(1)
    END
  
    INSERT INTO [dbo].[sysdac_instances_internal]
        (instance_id, type_name, instance_name, type_version, description, type_stream)
    VALUES
        (@instance_id, @type_name, @instance_name, @type_version, @description, @type_stream)

    SELECT @retval = @@error
    RETURN(@retval)
END
```

