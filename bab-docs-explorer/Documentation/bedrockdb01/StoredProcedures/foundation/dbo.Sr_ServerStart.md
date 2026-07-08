# dbo.Sr_ServerStart

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_ServerStart"]
    Sr_History(["Sr_History"]) --> SP
    Sr_Parameter(["Sr_Parameter"]) --> SP
    Sv_GetNextID(["Sv_GetNextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_History |
| Sr_Parameter |
| Sv_GetNextID |

## Stored Procedure Code

```sql
create proc Sr_ServerStart @ServerID int, @ThreadCount int  
/*********************************************************/
/*	                                                 */
/*	    Author: Chris Carveth                        */
/*	    Creation Date: 01-March-1999                 */
/*	    Comments: Updates Sr_History                 */
/*                    Updates Sr_Job                     */
/*                                                       */
/*********************************************************/
AS 
DECLARE      @ExecutionID int, 
	     @already_running int, 
	     @auto_execute bit, 
	     @scheduled_executions int,
 	     @done_executions int,
 	     @HistoryDays int

	SELECT @HistoryDays = ABS(CONVERT(INT, tag_value))* -1 
	  FROM Sr_Parameter 
	 WHERE tag = 'HistoryDays'

	SELECT @HistoryDays = ISNULL(@HistoryDays, -7)

	DELETE Sr_History
	 WHERE start_datetime < dateadd(dd, @HistoryDays, getdate())


	EXEC @ExecutionID = Sv_GetNextID 15 	

	 
	INSERT INTO Sr_History (execution_id, job_id, server_id, thread_index, topic_id, db_group_id, 
			        object_id, start_datetime, sucessful, include_in_average)
  	     VALUES (@ExecutionID, 0, @ServerID, @ThreadCount, 0, 0, 0, getdate(), 0, 1)
	
RETURN @ExecutionID
```

