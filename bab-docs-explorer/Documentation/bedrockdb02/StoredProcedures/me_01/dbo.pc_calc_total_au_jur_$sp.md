# dbo.pc_calc_total_au_jur_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.pc_calc_total_au_jur_$sp"]
    dbo_DestinationStyle(["dbo.DestinationStyle"]) --> SP
    dbo_ib_inventory_total(["dbo.ib_inventory_total"]) --> SP
    dbo_price_change_style(["dbo.price_change_style"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_Style(["dbo.Style"]) --> SP
    dbo_style_color(["dbo.style_color"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DestinationStyle |
| dbo.ib_inventory_total |
| dbo.price_change_style |
| dbo.sku |
| dbo.Style |
| dbo.style_color |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[pc_calc_total_au_jur_$sp]
AS
			
DECLARE @line_id INT
		, @table_name NVARCHAR(30), @operation_name NVARCHAR(50)
		, @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000)
		, @error_severity SMALLINT, @error_state SMALLINT
		
/*
	Version		: 1.00
	Created		: Feb 2011
	Created by	: Sameer Patel
	Description	: Handles calculation of total_affected_units column in price_change_style
					  for a price change document that was created for a single jurisdicition
				  
	Called by stored procedure pc_calc_total_affected_units_$sp
		-- NOTE: Temp tables not explcitly created in this procedure 
		-- were previously created in the calling stored procedure pc_calc_total_affected_units_$sp
	
HISTORY:
Date       		Name         	Def#			Desc
Sept26,11		Sameer Patel	1-47DGUL		the total units in the pcm worklist doesn't match the total units in the pcm header.
Oct 07,11		Sameer Patel	130297			the total units in the pcm worklist doesn't match the total units in the pcm header.
Oct 07,11		Sameer Patel	130300			the total units in the pcm worklist doesn't match the total units in the pcmhheader.
*/	

BEGIN TRY

	SET NOCOUNT ON

	--------------------------------------------------------------------------------------------------------------------------------------------------
	--------------------------------------------------------------------------------------------------------------------------------------------------
	-- Assume that the business object has been correctly calculated total_affected_units column in price_change_style table
	-- in the case where the old_price <> new_price
	
	-- Based on various test cases, the C++ code is somewhat "buggy" when we set the old_price = new_price in the price_change_style_loc
	-- Unfortunately, we have to go to IB in these case here to make sure units do not "overlap" 
	-- (i.e. double counting units when they are "affected" by two different lower level exceptions
	-- This procedure deals with a single jurisdiction
	-- This case is the most complex because we have to deal with the following cases
		-- color exceptions
		-- pricing group exceptions
		-- pricing group/color exceptions
		-- location exceptions
		-- location/color exceptions
	
	-- HOWEVER, we don't need to do extra work if there are no entries in price_change_style where the old_price = new_price
	SET @line_id = 10
	
	DECLARE @lv_count INT
	SELECT @lv_count = COALESCE(COUNT(*), 0) FROM #price_change_style	WHERE old_price = new_price
	
	IF (@lv_count > 0)
	BEGIN
	
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-- Create table that will store summarized affected units by style/pricing group/location/color
		-- We need this level of detail to account for the potential of "overlapping" exceptions
		SET @line_id = 20
		
		IF NOT object_id(N'tempdb..#au_by_pg_loc_color') IS NULL
		DROP TABLE #au_by_pg_loc_color
		
		CREATE TABLE #au_by_pg_loc_color
			( price_change_style_id DECIMAL(13), pricing_group_id SMALLINT, location_id SMALLINT, color_id SMALLINT
			, total_affected_units INT
			, PRIMARY KEY (price_change_style_id, pricing_group_id, location_id, color_id) )
			
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------------------------------------------------		
		-- CASE 1: COLOR EXCEPTION
		-- In the case where the old_price = new_price in the price_change_style table
		-- Get the entries from #price_change_style_color if there are any
		-- And there corresponding on hand values from ib_inventory_total
		-- Make sure the old_price <> new_price for the color exception (in #price_change_style_color)
		SET @line_id = 30
		
		INSERT INTO #au_by_pg_loc_color
			( price_change_style_id, pricing_group_id, location_id, color_id 
			, total_affected_units )
		SELECT
			StyleDetails.price_change_style_id, PGLocation.pricing_group_id, PGLocation.location_id, ColorDetails.color_id 
			, SUM(COALESCE(IB.total_on_hand_units, 0)) total_affected_units
		FROM
			#price_change_style StyleDetails
		CROSS JOIN #price_change_location PGLocation
		INNER JOIN #price_change_style_color ColorDetails ON StyleDetails.price_change_style_id = ColorDetails.price_change_style_id
		INNER JOIN style_color StyleColor ON StyleDetails.style_id = StyleColor.style_id AND ColorDetails.color_id = StyleColor.color_id
		INNER JOIN sku SkuDetails ON StyleColor.style_color_id = SkuDetails.style_color_id
		INNER JOIN ib_inventory_total IB ON SkuDetails.sku_id = IB.sku_id AND PGLocation.location_id = IB.location_id																																						
		WHERE
			StyleDetails.old_price = StyleDetails.new_price
			AND ColorDetails.old_price <> ColorDetails.new_price
		GROUP BY
			StyleDetails.price_change_style_id, PGLocation.pricing_group_id, PGLocation.location_id, ColorDetails.color_id 
			
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------------------------------------------------		
		-- CASE 2: PRICING GROUP EXCEPTION
		-- In the case where the old_price = new_price in the price_change_style table
		-- Get the entries from #price_change_style_pg if there are any
		-- And there corresponding on hand values from ib_inventory_total
		-- Make sure the old_price <> new_price for the color exception (in #price_change_style_pg)
		SET @line_id = 40
		
		INSERT INTO #au_by_pg_loc_color
			( price_change_style_id, pricing_group_id, location_id, color_id 
			, total_affected_units )
		SELECT
			StyleDetails.price_change_style_id, PGDetails.pricing_group_id, PGLocation.location_id, StyleColor.color_id 
			, SUM(COALESCE(IB.total_on_hand_units, 0)) total_affected_units
		FROM
			#price_change_style StyleDetails
		INNER JOIN #price_change_style_pg PGDetails ON StyleDetails.price_change_style_id = PGDetails.price_change_style_id
		INNER JOIN #price_change_location PGLocation ON PGDetails.pricing_group_id = PGLocation.pricing_group_id
		INNER JOIN style_color StyleColor ON StyleDetails.style_id = StyleColor.style_id
		LEFT OUTER JOIN #au_by_pg_loc_color Destination ON StyleDetails.price_change_style_id = Destination.price_change_style_id
																				AND PGDetails.pricing_group_id = Destination.pricing_group_id
																				AND PGLocation.location_id = Destination.location_id
																				AND StyleColor.color_id = Destination.color_id
		INNER JOIN sku SkuDetails ON StyleColor.style_color_id = SkuDetails.style_color_id
		INNER JOIN ib_inventory_total IB ON SkuDetails.sku_id = IB.sku_id AND PGLocation.location_id = IB.location_id																																						
		WHERE
			StyleDetails.old_price = StyleDetails.new_price
			AND PGDetails.old_price <> PGDetails.new_price
			AND Destination.price_change_style_id IS NULL
		GROUP BY
			StyleDetails.price_change_style_id, PGDetails.pricing_group_id, PGLocation.location_id, StyleColor.color_id
			
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------------------------------------------------		
		-- CASE 3: PRICING GROUP COLOR EXCEPTION
		-- In the case where the old_price = new_price in the price_change_style_pg table
		-- Get the entries from #price_change_stl_pg_col if there are any
		-- And there corresponding on hand values from ib_inventory_total
		-- Make sure the old_price <> new_price for the pricing group/color exception (in #price_change_stl_pg_col)
		SET @line_id = 50
		
		INSERT INTO #au_by_pg_loc_color
			( price_change_style_id, pricing_group_id, location_id, color_id 
			, total_affected_units )
		SELECT
			StyleDetails.price_change_style_id, PGColorDetails.pricing_group_id, PGLocation.location_id, PGColorDetails.color_id 
			, SUM(COALESCE(IB.total_on_hand_units, 0)) total_affected_units
		FROM
			#price_change_style StyleDetails		
		INNER JOIN #price_change_stl_pg_col PGColorDetails ON StyleDetails.price_change_style_id = PGColorDetails.price_change_style_id
		INNER JOIN #price_change_location PGLocation ON PGColorDetails.pricing_group_id = PGLocation.pricing_group_id
		INNER JOIN style_color StyleColor ON StyleDetails.style_id = StyleColor.style_id AND PGColorDetails.color_id = StyleColor.color_id
		LEFT OUTER JOIN #au_by_pg_loc_color Destination ON StyleDetails.price_change_style_id = Destination.price_change_style_id
																				AND PGColorDetails.pricing_group_id = Destination.pricing_group_id
																				AND PGLocation.location_id = Destination.location_id
																				AND StyleColor.color_id = Destination.color_id
		INNER JOIN sku SkuDetails ON StyleColor.style_color_id = SkuDetails.style_color_id
		INNER JOIN ib_inventory_total IB ON SkuDetails.sku_id = IB.sku_id AND PGLocation.location_id = IB.location_id																																						
		WHERE
			StyleDetails.old_price = StyleDetails.new_price
			AND PGColorDetails.old_price <> PGColorDetails.new_price
			AND Destination.price_change_style_id IS NULL
		GROUP BY
			StyleDetails.price_change_style_id, PGColorDetails.pricing_group_id, PGLocation.location_id, PGColorDetails.color_id 
		
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-- CASE 4: LOCATION EXCEPTION
		-- In the case where the old_price = new_price in the price_change_style_pg table
		-- Get the entries from #price_change_style_loc if there are any
		-- And there corresponding on hand values from ib_inventory_total
		-- Make sure the old_price <> new_price for the location exception (in #price_change_style_loc)
		-- Also make sure that we are not inserting an entry that already exists
		SET @line_id = 60
		
		INSERT INTO #au_by_pg_loc_color
			( price_change_style_id, pricing_group_id, location_id, color_id 
			, total_affected_units )
		SELECT
			StyleDetails.price_change_style_id, PGLocation.pricing_group_id, LocDetails.location_id, StyleColor.color_id 
			, SUM(COALESCE(IB.total_on_hand_units, 0)) total_affected_units
		FROM
			#price_change_style StyleDetails		
		INNER JOIN #price_change_style_loc LocDetails ON StyleDetails.price_change_style_id = LocDetails.price_change_style_id
		INNER JOIN #price_change_location PGLocation ON LocDetails.location_id = PGLocation.location_id
		INNER JOIN style_color StyleColor ON StyleDetails.style_id = StyleColor.style_id
		LEFT OUTER JOIN #au_by_pg_loc_color Destination ON StyleDetails.price_change_style_id = Destination.price_change_style_id
																				AND PGLocation.pricing_group_id = Destination.pricing_group_id
																				AND LocDetails.location_id = Destination.location_id
																				AND StyleColor.color_id = Destination.color_id
		INNER JOIN sku SkuDetails ON StyleColor.style_color_id = SkuDetails.style_color_id
		INNER JOIN ib_inventory_total IB ON SkuDetails.sku_id = IB.sku_id AND LocDetails.location_id = IB.location_id																																						
		WHERE
			StyleDetails.old_price = StyleDetails.new_price
			AND LocDetails.old_price <> LocDetails.new_price
			AND Destination.price_change_style_id IS NULL
		GROUP BY
			StyleDetails.price_change_style_id, PGLocation.pricing_group_id, LocDetails.location_id, StyleColor.color_id
		
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------------------------------------------------
		-- CASE 5: LOCATION COLOR EXCEPTION
		-- In the case where the old_price = new_price in the price_change_style_pg table
		-- Get the entries from #price_change_stl_col_loc if there are any
		-- And there corresponding on hand values from ib_inventory_total
		-- Make sure the old_price <> new_price for the location color exception (in #price_change_stl_col_loc)
		-- Also make sure that we are not inserting an entry that already exists
		SET @line_id = 70
		
		INSERT INTO #au_by_pg_loc_color
			( price_change_style_id, pricing_group_id, location_id, color_id 
			, total_affected_units )
		SELECT
			StyleDetails.price_change_style_id, PGLocation.pricing_group_id, LocColorDetails.location_id, LocColorDetails.color_id 
			, SUM(COALESCE(IB.total_on_hand_units, 0)) total_affected_units
		FROM
			#price_change_style StyleDetails		
		INNER JOIN #price_change_stl_col_loc LocColorDetails ON StyleDetails.price_change_style_id = LocColorDetails.price_change_style_id
		INNER JOIN #price_change_location PGLocation ON LocColorDetails.location_id = PGLocation.location_id
		INNER JOIN style_color StyleColor ON StyleDetails.style_id = StyleColor.style_id AND LocColorDetails.color_id = StyleColor.color_id
		LEFT OUTER JOIN #au_by_pg_loc_color Destination ON StyleDetails.price_change_style_id = Destination.price_change_style_id
																				AND PGLocation.pricing_group_id = Destination.pricing_group_id
																				AND LocColorDetails.location_id = Destination.location_id
																				AND StyleColor.color_id = Destination.color_id
		INNER JOIN sku SkuDetails ON StyleColor.style_color_id = SkuDetails.style_color_id
		INNER JOIN ib_inventory_total IB ON SkuDetails.sku_id = IB.sku_id AND LocColorDetails.location_id = IB.location_id																																						
		WHERE
			StyleDetails.old_price = StyleDetails.new_price
			AND LocColorDetails.old_price <> LocColorDetails.new_price
			AND Destination.price_change_style_id IS NULL
		GROUP BY
			StyleDetails.price_change_style_id, PGLocation.pricing_group_id, LocColorDetails.location_id, LocColorDetails.color_id

		-----------------------------------------------------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------------------------------------------------			
		-- Summarize the entries from #au_by_style
		SET @line_id = 80

		INSERT INTO #au_by_style
			( price_change_style_id
			, total_affected_units )
		SELECT
			price_change_style_id
			, SUM(total_affected_units)
		FROM
			#au_by_pg_loc_color
		GROUP BY
			price_change_style_id
			
	END			

	--------------------------------------------------------------------------------------------------------------------------------------------------
	--------------------------------------------------------------------------------------------------------------------------------------------------		
	-- Update #price_change_style table with total_affected_units column that has just been summarized
	SET @line_id = 90
	
	UPDATE Style
	SET
		Style.total_affected_units = StyleSummary.total_affected_units
	FROM
		#price_change_style Style
	INNER JOIN #au_by_style StyleSummary ON Style.price_change_style_id = StyleSummary.price_change_style_id	
	
	--------------------------------------------------------------------------------------------------------------------------------------------------
	--------------------------------------------------------------------------------------------------------------------------------------------------
	-- UPDATE actual price change tables
		
	-- price_change_style
	SET @line_id = 100
	
	UPDATE DestinationStyle
	SET
		DestinationStyle.total_affected_units = Style.total_affected_units
	FROM
		price_change_style DestinationStyle
	INNER JOIN #price_change_style Style ON DestinationStyle.price_change_style_id = Style.price_change_style_id
	
	--------------------------------------------------------------------------------------------------------------------------------------------------
	--------------------------------------------------------------------------------------------------------------------------------------------------
	
END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1

	IF @line_id = 10
		SELECT  
			@table_name			= N'#price_change_style'
			, @operation_name	= N'SELECT'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()	
									
	ELSE IF @line_id = 20
		SELECT  
			@table_name			= N'#au_by_pg_loc_color'
			, @operation_name	= N'CREATE TABLE'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 30
		SELECT  
			@table_name			= N'#au_by_pg_loc_color'
			, @operation_name	= N'INSERT - Color EX'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 40
		SELECT  
			@table_name			= N'#au_by_pg_loc_color'
			, @operation_name	= N'INSERT - PG EX'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 50
		SELECT  
			@table_name			= N'#au_by_pg_loc_color'
			, @operation_name	= N'INSERT - PG/Color EX'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()	

	ELSE IF @line_id = 60
		SELECT  
			@table_name			= N'#au_by_pg_loc_color'
			, @operation_name	= N'INSERT - Location EX'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 70
		SELECT  
			@table_name			= N'#au_by_pg_loc_color'
			, @operation_name	= N'INSERT - Location/Color EX'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 80
		SELECT  
			@table_name			= N'#au_by_style'
			, @operation_name	= N'INSERT'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()		

	ELSE IF @line_id = 90
		SELECT  
			@table_name			= N'#price_change_style'
			, @operation_name	= N'UPDATE'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()

	ELSE IF @line_id = 100
		SELECT  
			@table_name			= N'price_change_style'
			, @operation_name	= N'UPDATE'
			, @sql_err_num		= ERROR_NUMBER()
			, @error_msg		= N'Line Id = ' + CAST(@line_id AS NVARCHAR(4)) + N' '
									+ N' Table Name = ' + @table_name + N' '
									+ N' Operation Name = ' + @operation_name + N' '
									+ N' SQL Error Number = ' + CAST(@sql_err_num AS NVARCHAR(38)) + N' '
									+ N' Error Message = ' + ERROR_MESSAGE()		
			
	RAISERROR (@error_msg, @error_severity, @error_state)			

END CATCH
```

