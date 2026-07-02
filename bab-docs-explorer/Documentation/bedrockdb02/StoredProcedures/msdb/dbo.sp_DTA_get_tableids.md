# dbo.sp_DTA_get_tableids

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_get_tableids"]
    dbo_DTA_reports_database(["dbo.DTA_reports_database"]) --> SP
    dbo_DTA_reports_table(["dbo.DTA_reports_table"]) --> SP
    dbo_sp_DTA_check_permission(["dbo.sp_DTA_check_permission"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_reports_database |
| dbo.DTA_reports_table |
| dbo.sp_DTA_check_permission |

## Stored Procedure Code

```sql
create procedure sp_DTA_get_tableids
	@SessionID	int
as
begin
	declare @retval  int							
	set nocount on

	exec @retval =  sp_DTA_check_permission @SessionID

	if @retval = 1
	begin
		raiserror(31002,-1,-1)
		return(1)
	end	

	select TableID,DatabaseName,SchemaName,TableName 
	from [msdb].[dbo].[DTA_reports_table] as T,[msdb].[dbo].[DTA_reports_database] as D 
	where T.DatabaseID = D.DatabaseID and D.SessionID = @SessionID


end
```

