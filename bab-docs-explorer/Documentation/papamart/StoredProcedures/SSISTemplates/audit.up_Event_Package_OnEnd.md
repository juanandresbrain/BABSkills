# audit.up_Event_Package_OnEnd

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["audit.up_Event_Package_OnEnd"]
    audit_ExecutionLog(["audit.ExecutionLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| audit.ExecutionLog |

## Stored Procedure Code

```sql
CREATE procedure [audit].[up_Event_Package_OnEnd]
	 @logID				int
with execute as caller
as
/**********************************************************************************************************
* SP Name:
*		audit.up_Event_Package_OnEnd
* Parameters:
*		@logID			int
*  
* Purpose:	This stored procedure updates an existing entry in the custom event-log table. It flags the
*	execution run as complete.
*	Status = 0: Running (Incomplete)
*	Status = 1: Complete
*	Status = 2: Failed
*              
* Example:
		declare @logID int
		set @logID = 0
		exec audit.up_Event_Package_OnEnd @logID
		select * from audit.ExecutionLog where LogID = @logID
*              
* Revision Date/Time:
*	May 25, 2005	(G Dickinson)	- Authored
*
**********************************************************************************************************/
begin
	set nocount on

	update audit.ExecutionLog set
		 EndTime = getdate() --Note: This should NOT be @logicalDate
		,Status = case
			when Status = 0 then 1	--Complete
			else Status
		end --case
	where 
		LogID = @logID

	set nocount off
end --proc
```

