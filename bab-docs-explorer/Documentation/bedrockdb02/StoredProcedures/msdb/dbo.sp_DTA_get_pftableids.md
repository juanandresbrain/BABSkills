# dbo.sp_DTA_get_pftableids

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_get_pftableids"]
    dbo_DTA_reports_database(["dbo.DTA_reports_database"]) --> SP
    dbo_DTA_reports_partitionfunction(["dbo.DTA_reports_partitionfunction"]) --> SP
    dbo_sp_DTA_check_permission(["dbo.sp_DTA_check_permission"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_reports_database |
| dbo.DTA_reports_partitionfunction |
| dbo.sp_DTA_check_permission |

## Stored Procedure Code

```sql
create procedure sp_DTA_get_pftableids
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

	select PartitionFunctionID ,DatabaseName ,PartitionFunctionName  
	from [msdb].[dbo].[DTA_reports_partitionfunction]  as PF,
	[msdb].[dbo].[DTA_reports_database] as D 
	where PF.DatabaseID = D.DatabaseID 
	and D.SessionID = @SessionID
	
end
```

