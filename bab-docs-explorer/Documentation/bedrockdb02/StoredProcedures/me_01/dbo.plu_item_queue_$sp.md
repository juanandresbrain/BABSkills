# dbo.plu_item_queue_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.plu_item_queue_$sp"]
    dbo_core_replication_queue(["dbo.core_replication_queue"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_upc(["dbo.upc"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.core_replication_queue |
| dbo.sku |
| dbo.upc |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[plu_item_queue_$sp]
( @start_queue_id DECIMAL(12), @end_queue_id DECIMAL(12) )
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
				  Determines what upcs to send to PLU
				  based on what is in the CRQ greater than @start_queue_id and less than @end_queue_id
				  
	Call from C++ code:
		-- File: PLUQueueDefUPC.cpp
		-- Class: CPLUQueueDefUPC
		-- Function: FullQueueSQLServer
	
HISTORY:
Date       		Name         	Def#		Desc
Feb 04,11		Sameer Patel	N/A			Initial Release
*/	

BEGIN TRY

	SET NOCOUNT ON

	SET @line_id = 10
	
	INSERT INTO #all_upc
		( upc_id
		, sku_id
		, style_id, style_color_id )
	SELECT DISTINCT
		Upc.upc_id
		, Sku.sku_id
		, Sku.style_id, Sku.style_color_id
	FROM
		core_replication_queue CoreReplicationQueue
	INNER JOIN upc Upc ON CoreReplicationQueue.entity_id = Upc.upc_id
	INNER JOIN sku Sku ON Upc.sku_id = Sku.sku_id
	LEFT OUTER JOIN #all_style_color_resend StyleColorResend ON Sku.style_color_id = StyleColorResend.style_color_id AND Sku.style_id = StyleColorResend.style_id
	WHERE
		CoreReplicationQueue.core_replication_queue_id > @start_queue_id AND CoreReplicationQueue.core_replication_queue_id <= @end_queue_id
		AND CoreReplicationQueue.entity_code = 361 AND CoreReplicationQueue.replication_action IN (N'I', N'U')
		AND StyleColorResend.style_color_id IS NULL

END TRY

BEGIN CATCH

	SELECT 
		@error_severity	= 16
		, @error_state = 1

	IF @line_id = 10
		SELECT  
			@table_name			= N'#all_upc'
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

