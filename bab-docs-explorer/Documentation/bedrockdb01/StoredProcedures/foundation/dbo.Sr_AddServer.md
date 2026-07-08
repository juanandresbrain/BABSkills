# dbo.Sr_AddServer

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_AddServer"]
    Sr_Server(["Sr_Server"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_Server |

## Stored Procedure Code

```sql
create proc dbo.Sr_AddServer 

@MachineID int
/*********************************************************/
/*	                                                 */
/*	    Author: Adam Whiston                         */
/*	    Creation Date: 19-Feb-1999                   */
/*	    Comments: Adds a Server to Sr_Server	 */
/*                                                       */
/*********************************************************/

/*
Amendments
Modified by		Date		Reason
------------------------------------------------------------------------
Tim			26-Aug-1999	removed WHERE clause from SELECT 
                                        statement that gets next server_id
Andrea Nagy		17-Sep-99	Added the new field AUTOSTART to the Insert
*/

AS 
	DECLARE @new_id int 

	begin transaction
	SELECT @new_id = isnull(MAX(server_id),0) + 1 
	       FROM Sr_Server WITH(HOLDLOCK)
	     /* WHERE machine_id = @MachineID	*/
				
	INSERT Sr_Server (server_id, server_name, any_job, max_jobs, curr_status, requested_status, machine_id, autostart)
	VALUES (@new_id, 'Server ' + cast(@new_id as varchar(255)), 0, 1, 3, NULL, @MachineID, 1)
        
	IF @@rowcount <> 1
	   SELECT @new_id = 0

        commit transaction   
        
	RETURN @new_id
```

