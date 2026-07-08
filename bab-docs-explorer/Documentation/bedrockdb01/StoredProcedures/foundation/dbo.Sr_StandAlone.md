# dbo.Sr_StandAlone

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_StandAlone"]
    Sr_Job(["Sr_Job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_Job |

## Stored Procedure Code

```sql
create proc dbo.Sr_StandAlone 

@JobID int, @TimeoutMinutes smallint 
/*********************************************************/
/*	                                                     */
/*	    Author: Chris Carveth                    		 */
/*	    Creation Date: 05-Nov-1999                       */
/*	    Comments:                                        */ 
/*                                                       */
/*                                                       */
/*********************************************************/
/*

@result = +1; -- Job completed Normally
@result = -1; -- Timeout waiting to lock job. Job is in use or in a bad state.
@result = -2; -- Timeout - Job never got picked up
@result = -3; -- Timeout waiting for our execution to complete
@result = -4; -- Job not found

Amendments
Modified by		Date		Reason
------------------------------------------------------------------------

*/

AS 
DECLARE @result smallint,
        @saved_scheduled_executions smallint,
        @saved_done_executions smallint,
        @saved_auto_execute bit,
        @saved_scheduling_mode int,
        @scheduled_executions smallint,
        @done_executions smallint,
        @execution_id int,
        @locked int, 
        @start_time smalldatetime,  
        @current_time smalldatetime  



	SELECT @start_time = getdate()
	
	WHILE 1=1
	BEGIN
	
		-- Compare start time to current time to verify if we should timout based on argument
		SELECT @current_time = getdate()
		If @current_time > dateadd(minute, @TimeoutMinutes, @start_time)
		begin
			SELECT @result = -1 -- Timeout waiting to lock job. Job is in Use or hung.
			break
		end 
	
		begin transaction
	
		-- Set the lock for the job if the job is not already locked and executing
		UPDATE Sr_Job 
		   SET locked = -1
		 WHERE job_id = @JobID
		   AND locked = 0 
		   AND execution_id = 0
		
		-- If @@rowcount = 0 then the update failed and we have to determine why
		IF (SELECT @@rowcount) = 0 
	    begin
		
			SELECT @locked = locked
			  FROM Sr_Job 
		 	 WHERE job_id = @JobID

			 -- If @locked <> 0 then the job was already locked when we tried to lock it.
			 -- Otherwise, the update failed when we tried to lock it for some other reason.
			 -- One possibility is that the job doesn't exist.
		 	 IF @@rowcount = 0 
		 	 begin
				rollback
		 	 	SELECT @result = -4 -- Job not found
				break
		 	 end
		 	 ELSE IF @locked <> 0 
		 	 begin
		 	 	rollback
		 	 	waitfor DELAY '0:0:30'
		 	 	continue
			 end
	
		end
		ELSE -- The update to lock the job succeeded
		begin
			break	
		end
	
	END	-- end of while
	
	If @result < 0 
		GOTO EndOfProc

	-- Commit the update that locks the job
	commit transaction 
	
	-- Save the original value of the scheduling columns
	SELECT @saved_scheduled_executions = scheduled_executions,
	       @saved_done_executions = done_executions,
	       @saved_auto_execute = auto_execute,
	       @saved_scheduling_mode = scheduling_mode 
	  FROM Sr_Job 
	 WHERE job_id = @JobID
	
	-- Change the scheduling columns to request that the job run a single execution
	UPDATE Sr_Job 
	   SET scheduling_mode = 2,
	       scheduled_executions = 1,
	       done_executions = 0,
	       auto_execute = 0, 
	       locked = 0
	 WHERE job_id = @JobID
	 
	SELECT @scheduled_executions = 1, 
	       @done_executions = 0, 
	       @execution_id = -1, 
	       @start_time = getdate(), 
	       @result = 1
	
	WHILE ((@done_executions < @scheduled_executions) OR @execution_id <> 0)
	begin
	
		-- Compare start time to current time to verify if we should timout based on argument
		SELECT @current_time = getdate()
		If @current_time > dateadd(minute, @TimeoutMinutes, @start_time)
		begin
			If @execution_id = 0 
			begin
				SELECT @result = -2 -- Timeout - Job never got picked up
				break
			end
			else
			begin
				SELECT @result = -3 -- Timeout waiting for our execution to complete
				break
			end
		end 

	 	waitfor DELAY '0:0:30'
		
		SELECT @execution_id = execution_id,
		       @done_executions = done_executions, 
		       @scheduled_executions = scheduled_executions
		  FROM Sr_Job 
	 	 WHERE job_id = @JobID
	 	 
	end -- end of while
	
	-- Reset the scheduling columns back to their original values
	UPDATE Sr_Job
	   SET scheduled_executions = @saved_scheduled_executions,
	       done_executions = @saved_done_executions,
	       auto_execute = @saved_auto_execute,
	       scheduling_mode = @saved_scheduling_mode
	 WHERE job_id = @JobID
	
EndOfProc:
RETURN @result
```

