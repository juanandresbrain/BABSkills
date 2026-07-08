# dbo.Sr_StatusRequest

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_StatusRequest"]
    Sr_Server(["Sr_Server"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_Server |

## Stored Procedure Code

```sql
create proc Sr_StatusRequest @ServerId int, @RequestedStatus int 
/*********************************************************/
/*	                                                 */
/*	    Author: Adam Whiston                         */
/*	    Creation Date: 1-April-1999  		 */
/*	    Comments: Updates Sr_Server        		 */
/*                                                       */
/*********************************************************/
AS 

	UPDATE Sr_Server
	   SET requested_status = @RequestedStatus
	 WHERE server_id = @ServerId
	   AND ISNULL(requested_status, 0) = 0
               
	IF @@rowcount = 1 
	   RETURN 1
	ELSE
	   RETURN 0
```

