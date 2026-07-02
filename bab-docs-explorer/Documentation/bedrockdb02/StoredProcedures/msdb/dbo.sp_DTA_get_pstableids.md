# dbo.sp_DTA_get_pstableids

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_get_pstableids"]
    dbo_DTA_reports_database(["dbo.DTA_reports_database"]) --> SP
    dbo_DTA_reports_partitionfunction(["dbo.DTA_reports_partitionfunction"]) --> SP
    dbo_DTA_reports_partitionscheme(["dbo.DTA_reports_partitionscheme"]) --> SP
    dbo_sp_DTA_check_permission(["dbo.sp_DTA_check_permission"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_reports_database |
| dbo.DTA_reports_partitionfunction |
| dbo.DTA_reports_partitionscheme |
| dbo.sp_DTA_check_permission |

## Stored Procedure Code

```sql
create procedure sp_DTA_get_pstableids
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

	select PartitionSchemeID,DatabaseName,PartitionSchemeName   
	from [msdb].[dbo].[DTA_reports_partitionfunction]  as PF, 
	[msdb].[dbo].[DTA_reports_partitionscheme]  as PS, 
	[msdb].[dbo].[DTA_reports_database] as D 
	where PS.PartitionFunctionID  = PF.PartitionFunctionID and 
	PF.DatabaseID = D.DatabaseID and D.SessionID = @SessionID	
	
end
```

