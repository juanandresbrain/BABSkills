# dbo.job_error_handler_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.job_error_handler_$sp"]
    dbo_job_error(["dbo.job_error"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error |

## Stored Procedure Code

```sql
create proc [dbo].[job_error_handler_$sp] 	( @job_type INT
	, @job_id INT 
	, @proc_name NVARCHAR(80)
	, @line_id SMALLINT
	, @sql_err_num DECIMAL(38,0) 
	, @object_name NVARCHAR(30) 
	, @operation_name NVARCHAR(30) 
	, @error_msg NVARCHAR(4000)
	, @raise_flag BIT)

AS


/*    	Version		: 1.00 	Date		: 2007/04/24	Created by	: Pierrette Lemay
	Description : Common error handling procedure for jobs
			Logs errors to the job_error table 
			Raises application errors depending on raise_flag passed in
	Input parameter: contains all the values of the columns to be inserted in job_error except error_timestamp 
			 that is default to the current datetime. 
			 The calling procedure must provide values for the following columns:
				- job_type (mandatory)
				- job_id (mandatory)
				- proc_name (mandatory)
				- line_id (optional)
				- sql_err_num (optional)			
				- object_name (optional)
				- operation_name (optional)
				- error_msg (optional)
	History: Version 1.01 Date 2010/10,13 Modified the CATCH block IF XACT_STATE() = -1 instead of IF XACT_STATE() <> -1.
*/

BEGIN
	DECLARE @error_message NVARCHAR(1000), @error_severity SMALLINT, @error_state SMALLINT, @done BIT
	SELECT @error_message	= N'An error occurred during the Posting and is logged in the job_error table.'
		 , @error_severity	= 16
		 , @error_state		= 1

	IF @@TRANCOUNT <> 0
        -- Procedure called when there was an active transaction that failed. This transaction must be Rollback
		-- and we want to start a new transaction in order to write this error to the job_error table
		ROLLBACK TRANSACTION

     BEGIN TRY
		-- Procedure must start its own transaction.
        BEGIN TRANSACTION

		INSERT INTO job_error 
				(job_type
				, job_id 
				, proc_name 
				, line_id 
				, error_timestamp 
				, sql_err_num 
				, object_name
				, operation_name 
				, error_msg)
		VALUES ( @job_type
				, @job_id	
				, @proc_name 
				, @line_id 
				, GETDATE() 
				, @sql_err_num 
				, @object_name
				, @operation_name 
				, @error_msg)
	
		COMMIT TRANSACTION

		-- Here we want to force the execution to go in the Catch block in order to manage
		-- the behavior of the raise_flag.
		RAISERROR (@error_msg, @error_severity, @error_state)

	END TRY
	BEGIN CATCH
        IF @@TRANCOUNT <> 0 -- Transaction failed trying to de the insert into job_error
		BEGIN
			IF XACT_STATE() = 1
				-- There is an active ransaction committable 
				COMMIT TRANSACTION
            IF XACT_STATE() = -1
                -- The session has an active transaction, but an error 
				-- has occurred that has caused the transaction to be classified as an uncommittable transaction
                ROLLBACK TRANSACTION 
		END

		IF @raise_flag = 1
			RAISERROR (@error_message, @error_severity, @error_state)

	END CATCH
END
```

