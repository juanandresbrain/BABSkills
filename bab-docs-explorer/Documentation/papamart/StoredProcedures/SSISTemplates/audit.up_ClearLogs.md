# audit.up_ClearLogs

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["audit.up_ClearLogs"]
    audit_CommandLog(["audit.CommandLog"]) --> SP
    audit_ExecutionLog(["audit.ExecutionLog"]) --> SP
    audit_ProcessLog(["audit.ProcessLog"]) --> SP
    audit_StatisticLog(["audit.StatisticLog"]) --> SP
    dbo_sysdtslog90(["dbo.sysdtslog90"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| audit.CommandLog |
| audit.ExecutionLog |
| audit.ProcessLog |
| audit.StatisticLog |
| dbo.sysdtslog90 |

## Stored Procedure Code

```sql
create procedure [audit].[up_ClearLogs]
with execute as caller
as
begin
	set nocount on

	truncate table audit.CommandLog
	truncate table audit.ExecutionLog
	truncate table audit.ProcessLog
	truncate table audit.StatisticLog
	truncate table dbo.sysdtslog90

	set nocount off
end --proc
```

