# audit.up_Event_Package_OnCommand

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["audit.up_Event_Package_OnCommand"]
    audit_CommandLog(["audit.CommandLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| audit.CommandLog |

## Stored Procedure Code

```sql
CREATE procedure [audit].[up_Event_Package_OnCommand]
	 @Key				varchar(50)
	,@Type				varchar(50)
	,@Value				varchar(max)
	,@logID				int
with execute as caller
as
/**********************************************************************************************************
* SP Name:
*		audit.up_Event_Package_OnCommand
* Parameters:
*		 @Key		varchar(50)
*		,@Type		varchar(50)
*		,@Value		varchar(max)
*		,@logID		int
*  
* Purpose:	This stored procedure logs a command entry in the custom event-log table. A command is termed
*	as any large SQL or XMLA statement that the ETL performs. It is useful for debugging purposes to know
*	the exact text of the statement.
*              
* Example:
		exec audit.up_Event_Package_OnCommand 'Create Table', 'SQL', '...sql code...', 0
		select * from audit.CommandLog where LogID = 0
*              
* Revision Date/Time:
*	August 10, 2005	(G Dickinson)	- Authoring complete
*
**********************************************************************************************************/
begin
	set nocount on

	--Insert the log record
	insert into audit.CommandLog(
		 LogID
		,[Key]
		,[Type]
		,[Value]
    ) values (
		 isnull(@logID, 0)
		,@Key
		,@Type
		,@Value
	)

	set nocount off
end --proc
```

