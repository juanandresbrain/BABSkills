# managed_backup.sp_get_striping_option

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["managed_backup.sp_get_striping_option"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE managed_backup.sp_get_striping_option
	@file_count			INT	=	1,
	@backup_file_path	NVARCHAR(512),
	@backup_locally		TINYINT,	-- 0 = To URL, 1 = To Disk
	@striping_option 	NVARCHAR(MAX) = NULL OUTPUT
AS
BEGIN
	IF((@file_count IS NULL) OR (@file_count <= 0))
	BEGIN
		RAISERROR ('@file_count should be non-NULL and greater than zero. Cannot complete managed backup operation.', -- Message text
				   17, -- Severity,
				   3); -- State
		RETURN
	END
	IF(@backup_file_path IS NULL)
	BEGIN
		RAISERROR ('@backup_file_path should be non-NULL for doing backup. Cannot complete managed backup operation.', -- Message text
				   17, -- Severity,
				   3); -- State
		RETURN
	END
	IF ((@backup_locally <> 1) AND (@backup_locally <> 0))
	BEGIN
		RAISERROR ('@backup_locally cannot have values other than 0 or 1. Cannot complete managed backup operation.', -- Message text
					17, -- Severity,
					2); -- State
		RETURN
	END
	ELSE
	BEGIN
		DECLARE @backup_target NVARCHAR(10)
		SET @backup_target = CASE WHEN @backup_locally = 0 THEN 'URL = N''' WHEN @backup_locally = 1 THEN 'DISK = N''' END
	
		IF ((@file_count = 1) OR (@file_count IS NULL))
		BEGIN
			SET	@striping_option = @backup_target + @backup_file_path + ''''
		END
		ELSE
		BEGIN
			DECLARE @ext NVARCHAR(10)
			IF (PATINDEX('%.log', @backup_file_path) > 0)
				SET @ext = '.log'
			ELSE
				SET @ext = '.bak'

			SET	@striping_option = @backup_target + REPLACE(@backup_file_path, @ext,'_1' + @ext) + ''''

			DECLARE @counter INT = 2

			WHILE (@counter <= @file_count)
			BEGIN
				DECLARE @replstr NVARCHAR(MAX)
					SET @replstr = '_' + CAST(@counter as NVARCHAR(MAX)) + @ext
					SET	@striping_option = @striping_option + ', ' + @backup_target + REPLACE(@backup_file_path, @ext, @replstr) + ''''

				SET @counter = @counter + 1
			END
		END
	END
END

managed_backup,sp_set_parameter,-- Set the value of an internal system flag. These values govern the behavior of smart-backup algorithms.
--
CREATE PROCEDURE managed_backup.sp_set_parameter
	@parameter_name NVARCHAR(128),
	@parameter_value NVARCHAR(128)
AS
BEGIN
	SET NOCOUNT ON

    IF (@parameter_name IS NULL) OR (LEN(@parameter_name) = 0)
	BEGIN
        RAISERROR (45204, 17, 1, N'@parameter_name', N'parameter name');
        RETURN
	END

    IF (@parameter_value IS NULL) OR (LEN(@parameter_value) = 0)
	BEGIN
        RAISERROR (45204, 17, 2, N'@parameter_value', N'parameter value');
        RETURN
	END

	SET @parameter_name = LTRIM(RTRIM(@parameter_name))
	IF (CHARINDEX(N' ', @parameter_name) > 0)
	BEGIN
        RAISERROR (45212, 17, 3, N'@parameter_name', N'parameter name');
        RETURN
	END
	
	DECLARE @parameter_value_base64 NVARCHAR(MAX)
	DECLARE @input VARBINARY(MAX);

	SET @input = CONVERT(VARBINARY(MAX), @parameter_value)
	SELECT @parameter_value_base64 = CAST(N'' as XML).value('xs:base64Binary(sql:variable("@input"))', 'NVARCHAR(MAX)')

	DECLARE @params NVARCHAR (512)
	SELECT @params = 'configure_backup_params' + ' ' + @parameter_name + ' ' + @parameter_value_base64
	EXEC managed_backup.sp_add_task_command @task_name = 'backup', @additional_params = @params
END
```

