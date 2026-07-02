# dbo.plu_group_param_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_group_param_$sp"]
    dbo_group_permutation_plu(["dbo.group_permutation_plu"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.group_permutation_plu |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_group_param_$sp]
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
				  Gets plu group parameters and rearranges them into rows instead of columns
				  
	Call from C++ code:
		-- File: PLUFileDefGlobalSQLServer.cpp
		-- Class: CPLUFileDefGlobalSQLServer
		-- Function: LoadFileDefs
		
	-- NOTE: The temp table #plu_group_param exists
		
	IF NOT object_id('tempdb..#plu_group_param') IS NULL
	DROP TABLE #plu_group_param

	CREATE TABLE #plu_group_param
		( group_permutation_plu_id DECIMAL(12), parameter_plu_id TINYINT
		, parameter_plu NVARCHAR(255)
		, PRIMARY KEY (group_permutation_plu_id, parameter_plu_id) )	
	
HISTORY:
Date       		Name         	Def#		Desc
Feb 04,11		Sameer Patel	N/A			Initial Release
*/	

BEGIN TRY

	SET NOCOUNT ON

	-- Gets plu group parameters and rearranges them into rows instead of columns
	
	SET @line_id = 10
	
	INSERT INTO #plu_group_param
		( group_permutation_plu_id, parameter_plu_id, parameter_plu )
	SELECT group_permutation_plu_id, 1 parameter_plu_id, CAST(parameter_plu_1 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 2 parameter_plu_id, CAST(parameter_plu_2 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 3 parameter_plu_id, CAST(parameter_plu_3 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 4 parameter_plu_id, CAST(parameter_plu_4 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 5 parameter_plu_id, CAST(parameter_plu_5 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 6 parameter_plu_id, CAST(parameter_plu_6 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 7 parameter_plu_id, CAST(parameter_plu_7 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 8 parameter_plu_id, CAST(parameter_plu_8 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 9 parameter_plu_id, CAST(parameter_plu_9 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 10 parameter_plu_id, CAST(parameter_plu_10 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 11 parameter_plu_id, CAST(parameter_plu_11 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 12 parameter_plu_id, CAST(parameter_plu_12 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 13 parameter_plu_id, CAST(parameter_plu_13 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 14 parameter_plu_id, CAST(parameter_plu_14 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 15 parameter_plu_id, CAST(parameter_plu_15 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 16 parameter_plu_id, CAST(parameter_plu_16 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 17 parameter_plu_id, CAST(parameter_plu_17 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 18 parameter_plu_id, CAST(parameter_plu_18 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 19 parameter_plu_id, CAST(parameter_plu_19 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 20 parameter_plu_id, CAST(parameter_plu_20 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 21 parameter_plu_id, CAST(parameter_plu_21 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 22 parameter_plu_id, CAST(parameter_plu_22 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 23 parameter_plu_id, CAST(parameter_plu_23 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 24 parameter_plu_id, CAST(parameter_plu_24 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 25 parameter_plu_id, CAST(parameter_plu_25 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 26 parameter_plu_id, CAST(parameter_plu_26 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 27 parameter_plu_id, CAST(parameter_plu_27 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 28 parameter_plu_id, CAST(parameter_plu_28 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 29 parameter_plu_id, CAST(parameter_plu_29 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 30 parameter_plu_id, CAST(parameter_plu_30 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 31 parameter_plu_id, CAST(parameter_plu_31 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 32 parameter_plu_id, CAST(parameter_plu_32 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 33 parameter_plu_id, CAST(parameter_plu_33 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 34 parameter_plu_id, CAST(parameter_plu_34 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 35 parameter_plu_id, CAST(parameter_plu_35 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 36 parameter_plu_id, CAST(parameter_plu_36 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 37 parameter_plu_id, CAST(parameter_plu_37 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 38 parameter_plu_id, CAST(parameter_plu_38 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 39 parameter_plu_id, CAST(parameter_plu_39 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 40 parameter_plu_id, CAST(parameter_plu_40 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 41 parameter_plu_id, CAST(parameter_plu_41 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 42 parameter_plu_id, CAST(parameter_plu_42 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 
	UNION ALL
	SELECT group_permutation_plu_id, 43 parameter_plu_id, CAST(parameter_plu_43 AS NVARCHAR(255)) parameter_plu FROM group_permutation_plu 

END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1

	IF @line_id = 10
		SELECT  
			@table_name			= N'#plu_group_param'
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

