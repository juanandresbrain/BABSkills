# audit.up_Event_Package_OnCount

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["audit.up_Event_Package_OnCount"]
    audit_StatisticLog(["audit.StatisticLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| audit.StatisticLog |

## Stored Procedure Code

```sql
CREATE procedure [audit].[up_Event_Package_OnCount]
	 @logID				int
	,@ComponentName		varchar(50)
	,@Rows				int
	,@TimeMS			int
	,@MinRowsPerSec		int = null
	,@MaxRowsPerSec		int = null
with execute as caller
as
/**********************************************************************************************************
* SP Name:
*		audit.up_Event_Package_OnCount
* Parameters:
*		 @logID				int
*		,@ComponentName		varchar(50)
*		,@Rows				int
*		,@TimeMS			int
*		,@MinRowsPerSec		int = null
*		,@MaxRowsPerSec		int = null
*  
* Purpose:	This stored procedure logs an entry to the custom RowCount-log table.
*              
* Example:
		exec audit.up_Event_Package_OnCount 0, 'Test', 100, 1000, 5, 50
		select * from audit.StatisticLog where LogID = 0
*              
* Revision Date/Time:
*	May 25, 2005	(G Dickinson)	- Authored
*	July 14, 2005	(G Dickinson)	- Implemented NULLs instead of 0's for invalid fields
*									- Added @Mean logic
*	August 09, 2005	(G Dickinson)	- Removed @Median, @Mode logic as it proved un-useful
*
**********************************************************************************************************/
begin
	set nocount on

	--Insert the record
	insert into audit.StatisticLog(
		LogID, ComponentName, Rows, TimeMS, MinRowsPerSec, MaxRowsPerSec
	) values (
		isnull(@logID, 0), @ComponentName, @Rows, @TimeMS, @MinRowsPerSec, @MaxRowsPerSec
	)

	set nocount off
end --proc
```

