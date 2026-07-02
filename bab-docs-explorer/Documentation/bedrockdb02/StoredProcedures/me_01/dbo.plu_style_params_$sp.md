# dbo.plu_style_params_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_style_params_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_style_params_$sp]
AS
			
DECLARE @line_id INT
		, @table_name NVARCHAR(30), @operation_name NVARCHAR(50)
		, @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000)
		, @error_severity SMALLINT, @error_state SMALLINT
		
/*
	Version		: 1.00
	Created		: Feb 2011
	Created by	: Sameer Patel
	Description	: Procedure called by Segment 1038 -- EDM & PROD to Price Look-Up File Generate (CRS)
				  Gets all ordered style records
				  These will go to all locations that require a regenerate
				  
	Call from C++ code:
		-- File: PLUFileDefCommonSQLServer.cpp
		-- Class: CPLUFileDefCommonSQLServer
		-- Function: LoadFullRegenFileDefs
		
	-- NOTE: The temp table #style, #dept, #dept_class and #tb_plu_key exist
	
	IF NOT object_id('tempdb..#style') IS NULL
	DROP TABLE #style

	CREATE TABLE #style
		( style_id DECIMAL(12), style_color_id DECIMAL(13), color_id SMALLINT
		, dept_id INT, dept_class_id INT
		, style_type TINYINT
		, plu_key NVARCHAR(20)
		, description NVARCHAR(24)
		, retail_price DECIMAL(14,2), style_location_retail_price DECIMAL(14,2)
		, PRIMARY KEY (style_id, style_color_id, color_id, dept_class_id) )
	
	IF NOT object_id('tempdb..#dept') IS NULL
	DROP TABLE #dept

	CREATE TABLE #dept
		( hierarchy_group_id INT, hierarchy_level_id INT
		, pos_dept_group_key NVARCHAR(10)
		, dept_no NVARCHAR(4)
		, description NVARCHAR(40)
		, PRIMARY KEY (hierarchy_group_id) )
	
	IF NOT object_id('tempdb..#dept') IS NULL
	DROP TABLE #dept_class

	CREATE TABLE #dept_class
		( hierarchy_group_id INT, hierarchy_level_id INT
		, pos_merch_group_key INT
		, description NVARCHAR(40)
		, PRIMARY KEY (hierarchy_group_id) )
		
	IF NOT object_id('tempdb..#tb_plu_key') IS NULL
	DROP TABLE #tb_plu_key

	CREATE TABLE #tb_plu_key
		( style_id DECIMAL(12), style_color_id DECIMAL(13)
		, plu_key NVARCHAR(20)
		, PRIMARY KEY (style_id, style_color_id) )		
	
HISTORY:
Date       		Name         	Def#		Desc
Feb 04,11		Sameer Patel	N/A			Initial Release
*/

DECLARE @min_loc_id SMALLINT, @max_loc_id SMALLINT

BEGIN TRY

	SET NOCOUNT ON

	-- Get minimum and maximum ids from #location table
	
	SET @line_id = 10
	
	SELECT 
		@min_loc_id = COALESCE(MIN(id), 0)
		, @max_loc_id = COALESCE(MAX(id), 0)
	FROM
		#location
		
	-- Return if there are no locations to generate		
	
	IF @max_loc_id = 0
		RETURN
		
	-- For each location		
	-- Populate #style_parameters by joining to #dept_parameters, #style and #location
	
	WHILE (@min_loc_id <= @max_loc_id)
	BEGIN

		SET @line_id = 20
		
		INSERT INTO #style_parameters
			( location_id, style_id
			, department_level
			, verify_price, qty_required, returnable, discountable
			, allow_employee_discount, allow_layaways, prompt_id
			, coalition_tax_code_id, limited_qty, generate_coupon_id, commission_id
			, user_flag_1, user_flag_2, user_flag_3, user_flag_4
			, tax_table_1, tax_table_2, tax_table_3, tax_table_4
			, tax_table_5, tax_table_6, tax_table_7, tax_table_8
			, tax_table_9, tax_table_10, tax_table_11, tax_table_12
			, tax_table_13, tax_table_14, tax_table_15, tax_table_16
			, photo, wave, prompt_form_name, quantity_key_allowed
			, print_additional_copy, print_retail, print_suggested_retail
			, validate_sale, allow_zero_price, linked_item_grp_id, prompt_additional_data )
		SELECT
			DISTINCT
				TempLocation.location_id, TempStyle.style_id
				, '0' department_level
				, TempDeptParameters.verify_price, TempDeptParameters.qty_required, TempDeptParameters.returnable, TempDeptParameters.discountable
				, TempDeptParameters.allow_employee_discount, TempDeptParameters.allow_layaways, prompt_id
				, TempDeptParameters.coalition_tax_code_id, TempDeptParameters.limited_qty, TempDeptParameters.generate_coupon_id, TempDeptParameters.commission_id
				, TempDeptParameters.user_flag_1, TempDeptParameters.user_flag_2, TempDeptParameters.user_flag_3, TempDeptParameters.user_flag_4
				, TempDeptParameters.tax_table_1, TempDeptParameters.tax_table_2, TempDeptParameters.tax_table_3, TempDeptParameters.tax_table_4
				, TempDeptParameters.tax_table_5, TempDeptParameters.tax_table_6, TempDeptParameters.tax_table_7, TempDeptParameters.tax_table_8
				, TempDeptParameters.tax_table_9, TempDeptParameters.tax_table_10, TempDeptParameters.tax_table_11, TempDeptParameters.tax_table_12
				, TempDeptParameters.tax_table_13, TempDeptParameters.tax_table_14, TempDeptParameters.tax_table_15, TempDeptParameters.tax_table_16
				, TempDeptParameters.photo, TempDeptParameters.wave, TempDeptParameters.prompt_form_name, TempDeptParameters.quantity_key_allowed
				, TempDeptParameters.print_additional_copy, TempDeptParameters.print_retail, TempDeptParameters.print_suggested_retail
				, TempDeptParameters.validate_sale, TempDeptParameters.allow_zero_price, TempDeptParameters.linked_item_grp_id, TempDeptParameters.prompt_additional_data
		FROM
			#style TempStyle
		INNER JOIN #location TempLocation ON TempLocation.id = @min_loc_id
		INNER JOIN #dept_parameters TempDeptParameters ON TempStyle.dept_class_id = TempDeptParameters.dept_class_id 
															AND TempLocation.location_id = TempDeptParameters.location_id
		
		SET @min_loc_id = @min_loc_id + 1
		
	END

END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1

	IF @line_id = 10
		SELECT  
			@table_name			= N'#location'
			, @operation_name	= N'SELECT'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 20
		SELECT  
			@table_name			= N'#style_parameters'
			, @operation_name	= N'INSERT'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 30
		SELECT  
			@table_name			= N'#plu_ownership'
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

