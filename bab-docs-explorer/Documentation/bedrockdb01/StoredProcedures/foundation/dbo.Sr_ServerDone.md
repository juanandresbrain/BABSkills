# dbo.Sr_ServerDone

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_ServerDone"]
    Sr_History(["Sr_History"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_History |

## Stored Procedure Code

```sql
create proc Sr_ServerDone @ExecutionID int
/*********************************************************/
/*	                                                 */
/*	    Author: Chris Carveth              		 */
/*	    Creation Date: 01-March-1999                 */
/*	    Comments: Updates Sr_History                 */
/*                                                       */
/*                                                       */
/*********************************************************/
AS 
DECLARE @result int
        
        SELECT @result = 0
        
        UPDATE Sr_History
           SET end_datetime = getdate(),
               duration = datediff(second, start_datetime, getdate())
         WHERE execution_id = @ExecutionID 
         
       
	

RETURN @result
```

