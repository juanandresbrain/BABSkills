# dbo.plu_cu_resend_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_cu_resend_$sp"]
    dbo_plu_style_color(["dbo.plu_style_color"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.plu_style_color |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_cu_resend_$sp]
AS
			
DECLARE @line_id INT
		, @table_name NVARCHAR(30), @operation_name NVARCHAR(50)
		, @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000)
		, @error_severity SMALLINT, @error_state SMALLINT

BEGIN TRY

	SET NOCOUNT ON

	SET @line_id = 10
	
	INSERT INTO plu_style_color
		( style_color_id, validate_flag )
	SELECT
		d.style_color_id, 1 validate_flag
	FROM
		#all_style_color_resend d
	LEFT OUTER JOIN plu_style_color p ON d.style_color_id = p.style_color_id
	WHERE
		p.style_color_id IS NULL		

END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1

	IF @line_id = 10
		SELECT  
			@table_name			= N'crs_plu_style_color'
			, @operation_name	= N'INSERT'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()
			
	RAISERROR (@error_msg, @error_severity, @error_state)			

END CATCH
```

