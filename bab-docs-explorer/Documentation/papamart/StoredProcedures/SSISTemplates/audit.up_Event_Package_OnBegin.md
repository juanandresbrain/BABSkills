# audit.up_Event_Package_OnBegin

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["audit.up_Event_Package_OnBegin"]
    audit_ExecutionLog(["audit.ExecutionLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| audit.ExecutionLog |

## Stored Procedure Code

```sql
CREATE procedure [audit].[up_Event_Package_OnBegin]
	 @ParentLogID		int
	,@Description		varchar(50) = null
	,@PackageName		varchar(50)
	,@PackageGuid		uniqueidentifier
	,@MachineName		varchar(50)
	,@ExecutionGuid		uniqueidentifier
	,@logicalDate		datetime
	,@operator			varchar(30)
	,@logID				int = null output
with execute as caller
as
/**********************************************************************************************************
* SP Name:
*		audit.up_Event_Package_OnBegin
* Parameters:
*		 @ParentLogID		int
*		,@Description		varchar(50) = null
*		,@PackageName		varchar(50)
*		,@PackageGuid		uniqueidentifier
*		,@MachineName		varchar(50)
*		,@ExecutionGuid		uniqueidentifier
*		,@logicalDate		datetime
*		,@operator			varchar(30)
*		,@logID				int = null output
*  
* Purpose:	This stored procedure logs a starting event to the custom event-log table
*              
* Example:
		declare @logID int
		exec audit.up_Event_Package_OnBegin 
			 0, 'Description'
			,'PackageName' ,'00000000-0000-0000-0000-000000000000'
			,'MachineName', '00000000-0000-0000-0000-000000000000'
			,'2004-01-01', null, @logID output
		select * from audit.ExecutionLog where LogID = @logID
*              
* Revision Date/Time:
*	May 25, 2005	(G Dickinson)	- Authored
*	August 10, 2005	(G Dickinson)	- Coalesce @logicalDate, @operator, commenting
*
**********************************************************************************************************/
begin
	set nocount on

	--Coalesce @logicalDate
	set @logicalDate = isnull(@logicalDate, getdate())

	--Coalesce @operator
	set @operator = nullif(ltrim(rtrim(@operator)), '')
	set @operator = isnull(@operator, suser_sname())

	--Root-level nodes should have a null parent
	if @ParentLogID <= 0 set @ParentLogID = null

	--Root-level nodes should not have a null Description
	set @Description = nullif(ltrim(rtrim(@Description)), '')
	if @Description is null and @ParentLogID is null set @Description = @PackageName

	--Insert the log record
	insert into audit.ExecutionLog(
		 ParentLogID
		,Description
		,PackageName
		,PackageGuid
		,MachineName
		,ExecutionGuid
		,LogicalDate
		,Operator
		,StartTime
		,EndTime
		,Status
		,FailureTask
	) values (
		 @ParentLogID
		,@Description
		,@PackageName
		,@PackageGuid
		,@MachineName
		,@ExecutionGuid
		,@logicalDate
		,@operator
		,getdate() --Note: This should NOT be @logicalDate
		,null
		,0	--InProcess
		,null
	)
	set @logID = scope_identity()

	set nocount off
end --proc
```

