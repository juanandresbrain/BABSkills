# dbo.plu_deleted_item_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_deleted_item_$sp"]
    dbo_deleted_upc(["dbo.deleted_upc"]) --> SP
    dbo_parameter_price_lookup(["dbo.parameter_price_lookup"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.deleted_upc |
| dbo.parameter_price_lookup |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_deleted_item_$sp]
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
				  Gets sku and upc information for records in #all_upc_delete table
				  
	Call from C++ code:
		-- File: PLUFileDefCommonSQLServer.cpp
		-- Class: CPLUFileDefCommonSQLServer
		-- Function: LoadUPCDeleteFileDefs
	
HISTORY:
Date       		Name         	Def#		Desc
Feb 04,11		Sameer Patel	N/A			Initial Release
*/	

BEGIN TRY

	SET NOCOUNT ON

	SET @line_id = 10	

	INSERT INTO #item
		( upc_number )
	SELECT
		DISTINCT
			DeletedUpc.upc_number
	FROM
		#all_upc_delete TempDeletedUpc
	CROSS JOIN parameter_price_lookup ParameterPriceLookup
	INNER JOIN deleted_upc DeletedUpc ON TempDeletedUpc.upc_id = DeletedUpc.upc_id
		
END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1

	IF @line_id = 10
		SELECT  
			@table_name			= N'#item'
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

