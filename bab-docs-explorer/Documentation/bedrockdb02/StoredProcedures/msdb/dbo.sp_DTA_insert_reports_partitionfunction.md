# dbo.sp_DTA_insert_reports_partitionfunction

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_insert_reports_partitionfunction"]
    dbo_DTA_reports_partitionfunction(["dbo.DTA_reports_partitionfunction"]) --> SP
    dbo_sp_DTA_check_permission(["dbo.sp_DTA_check_permission"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_reports_partitionfunction |
| dbo.sp_DTA_check_permission |

## Stored Procedure Code

```sql
create procedure sp_DTA_insert_reports_partitionfunction
	@SessionID	int,
	@DatabaseID int,
	@PartitionFunctionName sysname,
	@PartitionFunctionDefinition ntext
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
	
	Insert into [msdb].[dbo].[DTA_reports_partitionfunction]([DatabaseID],[PartitionFunctionName],[PartitionFunctionDefinition]) 
	values(@DatabaseID,@PartitionFunctionName,@PartitionFunctionDefinition)
end
```

