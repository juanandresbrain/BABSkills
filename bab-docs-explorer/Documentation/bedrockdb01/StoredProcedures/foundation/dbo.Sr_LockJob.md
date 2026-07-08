# dbo.Sr_LockJob

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_LockJob"]
    Sr_Job(["Sr_Job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_Job |

## Stored Procedure Code

```sql
create proc Sr_LockJob @JobID int 
/*********************************************************/
/*	                                                 		*/
/*	    Author: Chris Carveth                        		*/
/*	    Creation Date: 23-June-1998                  		*/
/*	    Comments: Updates Ex_ServerMain locked       		*/
/*                                                       */
/*********************************************************/
AS 
	 
	UPDATE Sr_Job 
	   SET locked = 1
         WHERE job_id = @JobID
           AND execution_id = 0  
           AND locked = 0
               
	IF @@rowcount = 1 
	   RETURN 1
	ELSE
	   RETURN 0
```

