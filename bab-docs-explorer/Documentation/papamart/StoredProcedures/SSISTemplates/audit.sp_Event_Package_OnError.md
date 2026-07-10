# audit.sp_Event_Package_OnError

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["audit.sp_Event_Package_OnError"]
    audit_ExecutionLog(["audit.ExecutionLog"]) --> SP
    dbo_sysdtslog90(["dbo.sysdtslog90"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| audit.ExecutionLog |
| dbo.sysdtslog90 |

## Stored Procedure Code

```sql
CREATE procedure [audit].[sp_Event_Package_OnError]
	 @logID		int
	,@message	varchar(64) = null	--optional, for custom failures
with execute as caller
as
/**********************************************************************************************************
* SP Name:
*		audit.up_Event_Package_OnError
* Parameters:
*		 @logID		int
*		,@message	varchar(64) = null	--optional, for custom failures
*  
* Purpose:	This stored procedure logs an error entry in the custom event-log table.
*	Status = 0: Running (Incomplete)
*	Status = 1: Complete
*	Status = 2: Failed
*              
* Example:
		exec audit.up_Event_Package_OnError 1, 'Failed'
		select * from audit.ExecutionLog where LogID = 1
*              
* Revision Date/Time:
*	May 25, 2005	(G Dickinson)	- Authored
*
**********************************************************************************************************/
begin
	set nocount on
	
	declare
		 @failureTask		varchar(64)
		,@packageName		varchar(64)
		,@executionGuid		uniqueidentifier

	if @message is null begin
		select 
			 @packageName = upper(PackageName)
			,@executionGuid = ExecutionGuid
		from audit.ExecutionLog
		where LogID = @logID

		select top 1 @failureTask = source
		from dbo.sysdtslog90
		where executionid = @executionGuid
			and (upper(event) = 'ONERROR')
			and upper(source) <> @packageName
		order by endtime desc
	end else begin
		set @failureTask = @message
	end --if

	update audit.ExecutionLog set
		 EndTime = getdate()
		,Status = 2	--Failed
		,FailureTask = @failureTask
	where
		LogID = @logID

	set nocount off
end --proc
```

