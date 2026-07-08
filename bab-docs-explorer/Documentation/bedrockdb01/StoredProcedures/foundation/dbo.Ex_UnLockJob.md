# dbo.Ex_UnLockJob

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_UnLockJob"]
    Ex_ServerMain(["Ex_ServerMain"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Ex_ServerMain |

## Stored Procedure Code

```sql
create proc Ex_UnLockJob @JobID int 
/*********************************************************/
/*	                                                 		*/
/*	    Author: Chris Carveth               		         */
/*	    Creation Date: 23-June-1998              		   */
/*	    Comments: Updates Ex_ServerMain locked       		*/
/*                                                       */
/*********************************************************/
AS 
	 
	UPDATE Ex_ServerMain 
	   SET locked = 0
    WHERE job_id = @JobID
```

