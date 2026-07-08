# dbo.Ex_LockJob

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_LockJob"]
    Ex_ServerMain(["Ex_ServerMain"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Ex_ServerMain |

## Stored Procedure Code

```sql
create proc Ex_LockJob @JobID int 
/*********************************************************/
/*	                                                 		*/
/*	    Author: Chris Carveth                        		*/
/*	    Creation Date: 23-June-1998                  		*/
/*	    Comments: Updates Ex_ServerMain locked       		*/
/*                                                       */
/*********************************************************/
AS 
	 
	UPDATE Ex_ServerMain 
	   SET locked = 1
         WHERE job_id = @JobID
           AND executing = 0  
           AND locked = 0
               
	IF @@rowcount = 1 
	   RETURN 1
	ELSE
	   RETURN 0
```

