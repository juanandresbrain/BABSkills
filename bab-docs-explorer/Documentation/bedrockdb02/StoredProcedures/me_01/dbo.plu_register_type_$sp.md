# dbo.plu_register_type_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_register_type_$sp"]
    dbo_register_type(["dbo.register_type"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.register_type |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_register_type_$sp]
	( @register_code NVARCHAR(6)
	, @register_type_id TINYINT OUTPUT, @lookup_days INT OUTPUT, @future_price_manag_flag BIT OUTPUT )
AS
			
DECLARE @line_id INT
		, @table_name NVARCHAR(30), @operation_name NVARCHAR(50)
		, @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000)
		, @error_severity SMALLINT, @error_state SMALLINT
		
/*
	Version		: 1.00
	Created		: Feb 2011
	Created by	: Sameer Patel
	Description	: Procedure called by other stored procedures to get register type information for a particular register code
				  
	Call from Stored procedures:
		-- plu_regen_location_$sp
		-- plu_hg_regen_location_$sp
		-- plu_common_location_$sp
	
HISTORY:
Date       		Name         	Def#		Desc
Feb 04,11		Sameer Patel	N/A			Initial Release
*/	

BEGIN TRY

	SET NOCOUNT ON
	
	SET @line_id = 10
	
	-- Get register_type_id and activation_days_number from register_type table for CRS register_type
	SELECT
		@register_type_id = register_type_id
		, @lookup_days = COALESCE(activation_days_number, 0), @future_price_manag_flag = future_price_manag_flag
	FROM
		register_type
	WHERE
		register_code = @register_code

END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1

	IF @line_id = 10
		SELECT  
			@table_name			= N'register_type'
			, @operation_name	= N'SELECT'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()
			
	RAISERROR (@error_msg, @error_severity, @error_state)			

END CATCH
```

