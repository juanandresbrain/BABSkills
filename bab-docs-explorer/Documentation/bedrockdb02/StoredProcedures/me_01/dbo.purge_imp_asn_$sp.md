# dbo.purge_imp_asn_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.purge_imp_asn_$sp"]
    dbo_imp_asn(["dbo.imp_asn"]) --> SP
    dbo_imp_asn_sku(["dbo.imp_asn_sku"]) --> SP
    dbo_import_batch_process(["dbo.import_batch_process"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.imp_asn |
| dbo.imp_asn_sku |
| dbo.import_batch_process |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[purge_imp_asn_$sp]

AS

/*
	Version		: 1.00
	Created		: 2010/10/01
	Created by	: Pierrette Lemay
	Description	: This procedure is part of the Import ASN process. 
				  It's called after the threads completed to process all the jobs part of the current posting process.
				  It deletes the rows from imp_asn and imp_asn_batch for all incomplete jobs. 
*/

BEGIN
	DECLARE @line_id SMALLINT, @job_type TINYINT, @job_id SMALLINT, @c_true BIT, @c_false BIT,  @job_count SMALLINT, @crs_job_flag BIT,
			@proc_name NVARCHAR(30), @table_name NVARCHAR(30), @range_start DECIMAL(24,0),
			@operation_name NVARCHAR(30), @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(4000), 
			@upper_imp_asn_id DECIMAL(12,0), @return_flag BIT, @current_job_id INT, @range_end DECIMAL(24,0)

	SELECT   @line_id		= 10
			, @job_type		= 10
			, @job_id		= -1
			, @proc_name	= N'purge_imp_asn_$sp'
			, @c_false		= 0
			, @c_true		= 1
			, @job_count	= 0
			, @crs_job_flag = 0;
 
	BEGIN TRY		
	
		DECLARE crs_jobs CURSOR FOR
		SELECT h.job_id, h.range_start, h.range_end
		FROM import_batch_process p, job_header h
		WHERE p.job_type = 10
		AND p.job_id = h.job_id
		AND p.job_type = h.job_type
		AND h.completed_flag = 1;
		
		-- Log progress if job_params.debug_flag is true 
		EXEC return_debug_flag_$sp @job_type, @return_flag OUT;
		IF @return_flag = @c_true
			EXEC job_progress_handler_$sp @job_type, @job_id, @proc_name, @line_id;	
		
		OPEN crs_jobs
		SET @crs_job_flag = 1

		FETCH NEXT FROM crs_jobs INTO @current_job_id, @range_start, @range_end

		WHILE @@FETCH_STATUS = 0
		BEGIN
			SET @line_id = 20;
			
			BEGIN TRAN
			
			DELETE imp_asn WHERE imp_asn_id BETWEEN @range_start AND @range_end;		
			DELETE imp_asn_sku WHERE imp_asn_id BETWEEN @range_start AND @range_end;
			
			COMMIT TRAN
			
			FETCH NEXT FROM crs_jobs INTO @current_job_id, @range_start, @range_end;
		END
      
      	CLOSE crs_jobs;
	    DEALLOCATE crs_jobs;
	    SET @crs_job_flag = 0;
		
		-- Log progress if job_params.debug_flag is true
		EXEC return_debug_flag_$sp @job_type, @return_flag OUT
		IF (@return_flag = @c_true)
			EXEC job_progress_handler_$sp @job_type, @job_id, @proc_name, @line_id 

	END TRY

	BEGIN CATCH
		-- Test if the transaction is uncommittable.
		IF (XACT_STATE()) = -1
			ROLLBACK TRANSACTION

		-- Test if the transaction is active and valid.
		IF (XACT_STATE()) = 1
			COMMIT TRANSACTION
			
		IF (@crs_job_flag = 1)
		BEGIN
			CLOSE crs_jobs;
			DEALLOCATE crs_jobs;
		END

		IF @line_id = 10	
			SELECT  @table_name			= N'job_header'
					, @operation_name	= N'OPEN CURSOR'
					, @error_msg		= ERROR_MESSAGE()
					, @sql_err_num		= ERROR_NUMBER()
		ELSE IF @line_id = 20
			SELECT  @table_name			= N'imp_asn'
					, @operation_name	= N'DELETE'
					, @sql_err_num		= ERROR_NUMBER()
					, @error_msg		= ERROR_MESSAGE()

		EXEC job_error_handler_$sp 
			@job_type 
			, @job_id 
			, @proc_name 
			, @line_id 
			, @sql_err_num 
			, @table_name 
			, @operation_name 
			, @error_msg 
			, @c_true
	END CATCH
END
```

