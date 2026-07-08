# dbo.Sr_RemoveJob

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_RemoveJob"]
    Sr_Job(["Sr_Job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_Job |

## Stored Procedure Code

```sql
CREATE PROC dbo.Sr_RemoveJob @JobID int
/*********************************************************/
/*	                                                 */
/*	    Author: Tim Nishikawa                        */
/*	    Creation Date: 03-December-1999              */
/*	    Comments: Deletes job from Sr_Job and        */
/*                    cleans up Sr_History, Sr_Error,    */
/*                    and Sr_Trace.                      */
/*                                                       */
/*********************************************************/
/*
Amendments
Modified by		Date		Reason
------------------------------------------------------------------------
Tim N			01/19/2000	Removed delete statements which
					are handled by housekeeping job.
*/
AS
	/*
	DELETE Sr_Error 
	WHERE execution_id IN (SELECT execution_id
                       FROM Sr_History WHERE job_id = @JobID)
	
	DELETE Sr_Trace 
	WHERE execution_id IN (SELECT execution_id
                       FROM Sr_History WHERE job_id = @JobID)
	
	DELETE Sr_History
	WHERE job_id = @JobID
	*/

	DELETE Sr_Job
	WHERE job_id = @JobID
```

