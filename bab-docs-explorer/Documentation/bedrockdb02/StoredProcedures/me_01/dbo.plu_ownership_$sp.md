# dbo.plu_ownership_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_ownership_$sp"]
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.entity_attribute_set |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_ownership_$sp]
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
				  Determines which style/location combinations are valid to send down to PLU
				  
	Call from C++ code:
		-- File: PLUFileDefCommonSQLServer.cpp
		-- Class: CPLUFileDefCommonSQLServer
		-- Function: LoadFullRegenFileDefs
					 LoadHGRegenFileDefs
					 LoadStyleResendFileDefs
					 LoadStyleUpdateFileDefs
					 LoadUPCFileDefs
					 LoadPromoFileDefs
					 LoadPriceFileDefs
					 LoadStyleDeleteFileDefs
					 LoadUPCDeleteFileDefs
					 LoadCancelPromoFileDefs
		
	-- NOTE: The temp tables #plu_ownership, #location and #style exist

	IF NOT object_id('tempdb..#location') IS NULL
	DROP TABLE #location

	CREATE TABLE #location
		( id SMALLINT IDENTITY(1,1)
		, location_id SMALLINT, jurisdiction_id SMALLINT, pricing_group_id SMALLINT
		, language_id INT, register_type_id TINYINT
		, PRIMARY KEY (location_id, jurisdiction_id, pricing_group_id) )
	
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
	
	IF NOT object_id('tempdb..#plu_ownership') IS NULL
	DROP TABLE #plu_ownership

	CREATE TABLE #plu_ownership
		( location_id SMALLINT, register_type_id TINYINT
		, style_id DECIMAL(12)
		, PRIMARY KEY (location_id, style_id) )
	
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
	
	-- Create table for styles that can be sent down to PLU based on ownership attribute
		
	SET @line_id = 20
	
	IF NOT object_id(N'tempdb..#plu_ownership_style') IS NULL
	DROP TABLE #plu_ownership_style

	CREATE TABLE #plu_ownership_style
		( style_id DECIMAL(12)
		, style_attribute_id DECIMAL(12), style_attribute_set_id DECIMAL(12)
		, PRIMARY KEY (style_id, style_attribute_id, style_attribute_set_id) )
		
	-- Populate #plu_ownership_style with styles from #style table 
	-- that can be sent down to PLU based on style ownership attribute in #plu_shared_attribute table
		
	SET @line_id = 30
		
	INSERT INTO #plu_ownership_style
		( style_id
		, style_attribute_id, style_attribute_set_id )
	SELECT
		DISTINCT
			TempStyle.style_id
			, TempPluSharedAttribute.style_attribute_id, TempPluSharedAttribute.style_attribute_set_id
	FROM
		#style TempStyle
	CROSS JOIN #plu_shared_attribute TempPluSharedAttribute
	INNER JOIN entity_attribute_set EntityAttributeSet ON TempStyle.style_id = EntityAttributeSet.parent_id AND EntityAttributeSet.parent_type = 1
															AND TempPluSharedAttribute.style_attribute_id = EntityAttributeSet.attribute_id 
															AND TempPluSharedAttribute.style_attribute_set_id = EntityAttributeSet.attribute_set_id
											
	-- For each location											
	-- Populate #plu_ownership with styles from #plu_ownership_style table 
	-- that can be sent down to PLU based on location ownership attribute in #plu_shared_attribute table
	
	WHILE (@min_loc_id <= @max_loc_id)
	BEGIN

		SET @line_id = 40
		
		INSERT INTO #plu_ownership
			( location_id
			, style_id )
		SELECT
			TempLocation.location_id
			, TempPluOwnershipStyle.style_id
		FROM
			#plu_ownership_style TempPluOwnershipStyle
		INNER JOIN #location TempLocation ON TempLocation.id = @min_loc_id
		INNER JOIN #plu_shared_attribute TempPluSharedAttribute ON TempPluOwnershipStyle.style_attribute_id = TempPluSharedAttribute.style_attribute_id
																							AND TempPluOwnershipStyle.style_attribute_set_id = TempPluSharedAttribute.style_attribute_set_id
		INNER JOIN entity_attribute_set EntityAttributeSet ON TempLocation.location_id = EntityAttributeSet.parent_id AND EntityAttributeSet.parent_type = 2
																AND TempPluSharedAttribute.location_attribute_id = EntityAttributeSet.attribute_id 
																AND TempPluSharedAttribute.location_attribute_set_id = EntityAttributeSet.attribute_set_id
		
		SET @min_loc_id = @min_loc_id + 1
		
	END

END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1

	IF @line_id = 15
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
			@table_name			= N'#plu_ownership_style'
			, @operation_name	= N'CREATE TABLE'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 30
		SELECT  
			@table_name			= N'#plu_ownership_style'
			, @operation_name	= N'INSERT'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 40
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

