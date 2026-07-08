# dbo.Sr_MachineDoneInterrupted

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_MachineDoneInterrupted"]
    Sr_History(["Sr_History"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sr_History |

## Stored Procedure Code

```sql
create proc Sr_MachineDoneInterrupted @ExecutionID int, @MachineID int, @ExitCode int
/*********************************************************/
/*	                                                 */
/*	    Author: Bing Zhu             		 */
/*	    Creation Date: 12-FEB-2001                   */
/*	    Comments: Updates Sr_History                 */
/*                                                       */
/*                                                       */
/*********************************************************/
/*
Amendments
Modified by		Date		Reason
------------------------------------------------------------------------
*/
AS 
DECLARE @result int
        
        SELECT @result = 0
        
        UPDATE Sr_History
           SET end_datetime = getdate(),
               duration = datediff(second, start_datetime, getdate()),
               exit_code = @ExitCode
         WHERE execution_id = @ExecutionID 
         

RETURN @result
```

