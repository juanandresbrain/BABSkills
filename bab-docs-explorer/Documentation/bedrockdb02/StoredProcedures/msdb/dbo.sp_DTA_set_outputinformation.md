# dbo.sp_DTA_set_outputinformation

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_set_outputinformation"]
    dbo_DTA_output(["dbo.DTA_output"]) --> SP
    dbo_sp_DTA_check_permission(["dbo.sp_DTA_check_permission"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_output |
| dbo.sp_DTA_check_permission |

## Stored Procedure Code

```sql
create procedure sp_DTA_set_outputinformation
	@SessionID int,
	@TuningResults ntext,
	@FinishStatus tinyint
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
	
	Insert into [msdb].[dbo].[DTA_output]([SessionID], [TuningResults],[FinishStatus]) values(@SessionID,@TuningResults,@FinishStatus)
end
```

