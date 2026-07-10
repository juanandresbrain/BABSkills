# admin.up_SetLogicalDate

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["admin.up_SetLogicalDate"]
    admin_Configuration(["admin.Configuration"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| admin.Configuration |

## Stored Procedure Code

```sql
CREATE procedure [admin].[up_SetLogicalDate]
	@date	datetime
with execute as caller
as
/**********************************************************************************************************
* SP Name:
*		admin.up_SetLogicalDate
* Parameters:
*		 @date	datetime
*  
* Purpose:	This stored procedure sets the LogicalDate in the configuration table. Passing in a null @date 
*	parameter serves to increment the existing value in the table by 1. Passing in a non-null @date resets 
*	the value in the table.
*              
* Example:
	exec etl.up_DimItem_SCD1 1, null
*              
* Revision Date/Time:
*	July 25, 2005	(G Dickinson)	- Authored
*
**********************************************************************************************************
*/
begin
	set nocount on

	--Set the configuration filter value
	declare @filter nvarchar(255)
	set @filter = upper(N'LogicalDate')

	--A null @date implies an increment: @date = @date + 1
	if @date is null begin
		--Fetch the existing date
		select @date = convert(datetime, ConfiguredValue) 
		from admin.Configuration
		where upper(ConfigurationFilter) = @filter
		--Increment it
		set @date = @date + 1
	end --if

	--Write the new @date to the table
	update admin.Configuration 
	set ConfiguredValue = replace(convert(varchar(10), @date, 102), '.', '-')
	where upper(ConfigurationFilter) = @filter

	set nocount off
end --proc
```

