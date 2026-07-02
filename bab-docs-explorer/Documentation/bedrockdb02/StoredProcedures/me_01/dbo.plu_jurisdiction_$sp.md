# dbo.plu_jurisdiction_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_jurisdiction_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_jurisdiction_$sp]
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
				  Populate a temp table of jurisdictions using locations in #location table
				  
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
					 LoadCancelPromoFileDefs
		
	The #jurisdiction temp table will be used in future procedures when retrieving permanent/promo prices.  
	This work is done by jurisdiction which is why we have an identity column on this table
	for the purposes of looping.
		
	-- NOTE: The temp tables #jurisdiction and #location exist
	
	IF NOT object_id('tempdb..#jurisdiction') IS NULL
	DROP TABLE #jurisdiction

	CREATE TABLE #jurisdiction
		( id SMALLINT IDENTITY(1,1)
		, jurisdiction_id SMALLINT
		, PRIMARY KEY (jurisdiction_id) )

	IF NOT object_id('tempdb..#location') IS NULL
	DROP TABLE #location

	CREATE TABLE #location
		( id SMALLINT IDENTITY(1,1)
		, location_id SMALLINT, jurisdiction_id SMALLINT, pricing_group_id SMALLINT
		, language_id INT, register_type_id TINYINT
		, PRIMARY KEY (location_id, jurisdiction_id, pricing_group_id) )
	
HISTORY:
Date       		Name         	Def#		Desc
Feb 04,11		Sameer Patel	N/A			Initial Release
*/	

BEGIN TRY

	SET NOCOUNT ON
	
	-- Get distinct jurisdictions from #location table

	SET @line_id = 10
	
	INSERT INTO #jurisdiction
		( jurisdiction_id )
	SELECT
		DISTINCT
			jurisdiction_id
	FROM
		#location
	ORDER BY 1

END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1
		
	IF @line_id = 10
		SELECT  
			@table_name			= N'#jurisdiction'
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

