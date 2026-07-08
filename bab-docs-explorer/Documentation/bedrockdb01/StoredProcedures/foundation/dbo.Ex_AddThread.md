# dbo.Ex_AddThread

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_AddThread"]
    Ex_ServerThread(["Ex_ServerThread"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Ex_ServerThread |

## Stored Procedure Code

```sql
create proc Ex_AddThread /*********************************************************/
/*	                                                 		*/
/*	    Author: Chris Carveth                        		*/
/*	    Creation Date: 29-June-1998                  		*/
/*	    Comments: Adds a Thread to Ex_ServerThread   		*/
/*                                                       */
/*********************************************************/
AS 
	DECLARE @new_index int 

	SELECT @new_index = MAX(thread_index) + 1
	 FROM Ex_ServerThread     

	INSERT Ex_ServerThread (thread_index, active, curr_status, curr_execution_id, requested_status)
	              VALUES ( @new_index, 1, 0, 0, 0)
               
	IF @@rowcount = 1 
	   RETURN @new_index
	ELSE
	   RETURN 0
```

