# dbo.sp_DTA_set_progressinformation

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_set_progressinformation"]
    dbo_DTA_progress(["dbo.DTA_progress"]) --> SP
    dbo_sp_DTA_check_permission(["dbo.sp_DTA_check_permission"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_progress |
| dbo.sp_DTA_check_permission |

## Stored Procedure Code

```sql
create procedure sp_DTA_set_progressinformation
	@SessionID int,
	@WorkloadConsumption int,
	@TuningStage int,
	@EstImprovement int,
	@ConsumingWorkLoadMessage nvarchar(256) = N'',
	@PerformingAnalysisMessage nvarchar(256)= N'',
	@GeneratingReportsMessage nvarchar(256)= N''


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
	update [msdb].[dbo].[DTA_progress]
	set WorkloadConsumption = @WorkloadConsumption,
	EstImprovement = @EstImprovement,
	ProgressEventTime = GetDate(),
	ConsumingWorkLoadMessage =	@ConsumingWorkLoadMessage ,
	PerformingAnalysisMessage =	@PerformingAnalysisMessage,
	GeneratingReportsMessage =	@GeneratingReportsMessage
	where SessionID=@SessionID
	and TuningStage = @TuningStage
end
```

