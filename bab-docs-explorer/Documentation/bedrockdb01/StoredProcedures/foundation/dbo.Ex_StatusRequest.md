# dbo.Ex_StatusRequest

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_StatusRequest"]
    Ex_ServerThread(["Ex_ServerThread"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Ex_ServerThread |

## Stored Procedure Code

```sql
create proc Ex_StatusRequest @ThreadIndex int, @RequestedStatus int 
/*********************************************************/
/*	                                                 		*/
/*	    Author: Chris Carveth                        		*/
/*	    Creation Date: 29-June-1998                  		*/
/*	    Comments: Updates Ex_ServerThread           		*/
/*                                                       */
/*********************************************************/
AS 

	UPDATE Ex_ServerThread 
	   SET requested_status = @RequestedStatus
	 WHERE thread_index = @ThreadIndex
	   AND ISNULL(requested_status, 0) = 0
               
	IF @@rowcount = 1 
	   RETURN 1
	ELSE
	   RETURN 0
```

