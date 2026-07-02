# dbo.plu_crs_del_temp_output_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_crs_del_temp_output_$sp"]
    dbo_parameter_price_lookup(["dbo.parameter_price_lookup"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.parameter_price_lookup |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_crs_del_temp_output_$sp]
(@send_dept BIT, @send_style BIT, @send_item BIT)
AS
			
DECLARE @line_id INT
		, @table_name NVARCHAR(30), @operation_name NVARCHAR(50)
		, @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000)
		, @error_severity SMALLINT, @error_state SMALLINT

DECLARE
	@c_CRS_add_action NVARCHAR(1)
	, @c_CRS_delete_action NVARCHAR(1), @c_CRS_change_action NVARCHAR(1)
	, @c_CRS_sale_action NVARCHAR(1), @c_CRS_chg_field_action NVARCHAR(1)

SET @c_CRS_add_action = N'1'
SET @c_CRS_delete_action = N'2'
SET @c_CRS_change_action = N'3'
SET @c_CRS_sale_action = N'4'
SET @c_CRS_chg_field_action = N'5'

DECLARE
	@c_CRS_order_dept INT, @c_CRS_order_dept_class INT
	, @c_CRS_order_style INT, @c_CRS_order_style_promo INT, @c_CRS_order_style_modify INT
	, @c_CRS_order_item INT, @c_CRS_order_item_promo INT, @c_CRS_order_item_modify INT
	, @c_CRS_order_alt INT
	
SET @c_CRS_order_dept = 10
SET @c_CRS_order_dept_class = 20
SET @c_CRS_order_style = 30
SET @c_CRS_order_style_modify = 40
SET @c_CRS_order_style_promo = 50
SET @c_CRS_order_item = 60
SET @c_CRS_order_item_modify = 70
SET @c_CRS_order_item_promo = 80
SET @c_CRS_order_alt = 90

DECLARE
	@c_CRS_dept_record NVARCHAR(2)
	, @c_CRS_dept_class_record NVARCHAR(2)
	, @c_CRS_dept_tax_flag NVARCHAR(2)
	
SET @c_CRS_dept_record = N'03'
SET @c_CRS_dept_class_record = N'04'
SET @c_CRS_dept_tax_flag = REPLICATE(N' ', 2)

DECLARE
	@c_CRS_style_record NVARCHAR(2)
	, @c_CRS_item_record NVARCHAR(2)
	, @c_CRS_alt_record NVARCHAR(2)
	, @c_CRS_del_space VARCHAR

SET @c_CRS_style_record = N'08'
SET @c_CRS_item_record = N'01'
SET @c_CRS_alt_record = N'02'

SET @c_CRS_del_space = N' '

DECLARE @min_loc_id SMALLINT, @max_loc_id SMALLINT, @count INT

DECLARE @current_date AS DATETIME
SET @current_date = CAST(FLOOR(CAST(GETDATE() AS FLOAT)) AS DATETIME)

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
	-- Populate ##plu_temp_output table
	
	WHILE (@min_loc_id <= @max_loc_id)
	BEGIN
		
		-- Only send department records if @send_dept = 1
		
		IF @send_dept = 1
		BEGIN

			-- Insert department class delete records into temp output table

			SET @line_id = 20
		
			INSERT INTO ##plu_temp_output
				( location_id
				, row_data
				, export_order )
			SELECT
				TempLocation.location_id
				, @c_CRS_dept_class_record + @c_CRS_delete_action
					+ CONVERT(NCHAR(4), LEFT(TempDeptClass.pos_merch_group_key, 4) + REPLICATE(N' ', 4 - LEN(LEFT(TempDeptClass.pos_merch_group_key, 4))))
					+ CONVERT(NCHAR(4), LEFT(TempDept.pos_dept_group_key, 4) + REPLICATE(N' ', 4 - LEN(LEFT(TempDept.pos_dept_group_key, 4))))
					+ @c_CRS_del_space
				, @c_CRS_order_dept_class
			FROM
				#dept_class TempDeptClass
			CROSS JOIN parameter_price_lookup ParameterPriceLookup
			INNER JOIN #location TempLocation ON TempLocation.id = @min_loc_id

			-- Insert department delete records into temp output table

			SET @line_id = 30
		
			INSERT INTO ##plu_temp_output
				( location_id
				, row_data
				, export_order )
			SELECT
				TempLocation.location_id
				, @c_CRS_dept_record + @c_CRS_delete_action
					+ CONVERT(NCHAR(4), LEFT(TempDept.pos_dept_group_key, 4) + REPLICATE(N' ', 4 - LEN(LEFT(TempDept.pos_dept_group_key, 4))))
					+ @c_CRS_del_space
				, @c_CRS_order_dept
			FROM
				#dept TempDept
			CROSS JOIN parameter_price_lookup ParameterPriceLookup
			INNER JOIN #location TempLocation ON TempLocation.id = @min_loc_id
																			
		END -- @send_dept = 1
		
		-- Only send style records if @send_style = 1
		
		IF @send_style = 1
		BEGIN

			-- Insert style delete records into temp output table

			SET @line_id = 40
		
			INSERT INTO ##plu_temp_output
				( location_id
				, row_data
				, export_order )
			SELECT
				TempLocation.location_id
				, @c_CRS_style_record + @c_CRS_delete_action
					+ CASE 
						WHEN TempStyle.plu_key LIKE '%[^A-Z]%' THEN LEFT(TempStyle.plu_key, 24)  + REPLICATE(N' ', 24 - LEN(LEFT(TempStyle.plu_key, 24)))
						ELSE LEFT(RIGHT(REPLICATE(N'0', ParameterPriceLookup.item_no_lookup_length) + TempStyle.plu_key, ParameterPriceLookup.item_no_lookup_length) + REPLICATE(N' ', 24), 24)
					  END 
					+ @c_CRS_del_space
				, @c_CRS_order_item
			FROM
				#style TempStyle
			CROSS JOIN parameter_price_lookup ParameterPriceLookup
			INNER JOIN #location TempLocation ON TempLocation.id = @min_loc_id
																			
		END -- @send_style = 1
		
		-- Only send item records if @send_item = 1
		
		IF @send_item = 1
		BEGIN
		
			-- Insert item delete records into temp output table
		
			SET @line_id = 50
		
			INSERT INTO ##plu_temp_output
				( location_id
				, row_data
				, export_order )
			SELECT
				TempLocation.location_id
				, @c_CRS_item_record + @c_CRS_delete_action
					+ CASE SIGN(ParameterPriceLookup.item_no_lookup_length - LEN(CONVERT( NVARCHAR(20), TempItem.sku_id )))
						WHEN 1 THEN REPLICATE(N'0', ParameterPriceLookup.item_no_lookup_length - LEN(CONVERT( NVARCHAR(20), TempItem.sku_id )))
						ELSE N'' END +
					  TempItem.upc_number +
					  REPLICATE(N' ', 24 - CASE SIGN(ParameterPriceLookup.item_no_lookup_length - LEN(CONVERT( NVARCHAR(20), TempItem.sku_id )))
						WHEN 1 THEN ParameterPriceLookup.item_no_lookup_length
						ELSE LEN(TempItem.upc_number) END) +
					+ @c_CRS_del_space
				, @c_CRS_order_item
			FROM
				#item TempItem
			CROSS JOIN parameter_price_lookup ParameterPriceLookup
			INNER JOIN #location TempLocation ON TempLocation.id = @min_loc_id
			
			-- Insert alternate delete records into temp output table
			
			SET @line_id = 60
		
			INSERT INTO ##plu_temp_output
				( location_id
				, row_data
				, export_order )
			SELECT
				TempLocation.location_id
				, @c_CRS_alt_record + @c_CRS_delete_action
					+ CASE SIGN(ParameterPriceLookup.upc_no_lookup_length - LEN(TempItem.upc_number))
						WHEN 1 THEN REPLICATE(N'0', ParameterPriceLookup.upc_no_lookup_length - LEN(TempItem.upc_number))
						ELSE N'' END +
					  TempItem.upc_number +
					  REPLICATE(N' ', 24 - CASE SIGN(ParameterPriceLookup.upc_no_lookup_length - LEN(TempItem.upc_number))
						WHEN 1 THEN ParameterPriceLookup.upc_no_lookup_length
						ELSE LEN(TempItem.upc_number) END) +
					+ @c_CRS_del_space
				, @c_CRS_order_item
			FROM
				#item TempItem
			CROSS JOIN parameter_price_lookup ParameterPriceLookup
			INNER JOIN #location TempLocation ON TempLocation.id = @min_loc_id
																			
		END -- @send_item = 1
		
		--------------------------------------------------------------------------------------------------------------------------------------------------------------------
		--------------------------------------------------------------------------------------------------------------------------------------------------------------------
		
		SET @min_loc_id = @min_loc_id + 1
		
	END
	
	-- Truncate temp tables for use in future queues
	
	SET @line_id = 130
	
	TRUNCATE TABLE #location
	
	--, @send_style BIT, @send_item BIT
	
	IF (@send_dept = 1)
	BEGIN
	
		SET @line_id = 160

		TRUNCATE TABLE #dept

		SET @line_id = 170

		TRUNCATE TABLE #dept_class
	
	END
	
	IF (@send_style = 1)
	BEGIN
	
		SET @line_id = 190

		TRUNCATE TABLE #style
	
	END

	IF (@send_item = 1)
	BEGIN

		SET @line_id = 240
	
		TRUNCATE TABLE #item
	
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
			@table_name			= N'##plu_temp_output'
			, @operation_name	= N'INSERT - department class records'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 30
		SELECT  
			@table_name			= N'##plu_temp_output'
			, @operation_name	= N'INSERT - department records'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 40
		SELECT  
			@table_name			= N'##plu_temp_output'
			, @operation_name	= N'INSERT - style records'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 50
		SELECT  
			@table_name			= N'##plu_temp_output'
			, @operation_name	= N'INSERT - item records'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 60
		SELECT  
			@table_name			= N'##plu_temp_output'
			, @operation_name	= N'INSERT - alternate records'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()
			
	RAISERROR (@error_msg, @error_severity, @error_state)			

END CATCH
```

