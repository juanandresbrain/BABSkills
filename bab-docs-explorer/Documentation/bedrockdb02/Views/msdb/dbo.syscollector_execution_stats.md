# dbo.syscollector_execution_stats

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syscollector_execution_stats"]
    dbo_syscollector_execution_stats_internal(["dbo.syscollector_execution_stats_internal"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.syscollector_execution_stats_internal |

## View Code

```sql
CREATE VIEW [dbo].[syscollector_execution_stats] AS
    SELECT
        log_id,
        task_name,
        execution_row_count_in,
        execution_row_count_out,
        execution_row_count_errors,
        execution_time_ms,
        log_time
    FROM dbo.syscollector_execution_stats_internal

dbo,sysdac_instances,CREATE VIEW [dbo].[sysdac_instances]
AS
    SELECT
        -- this must be locked down because we use instance_id visability as a security gate
        case 
            when (dbo.fn_sysdac_is_currentuser_sa() = 1) then dac_instances.instance_id
            when sd.owner_sid = SUSER_SID() then dac_instances.instance_id
            else NULL
        end as instance_id,
        dac_instances.instance_name,
        dac_instances.type_name,
        dac_instances.type_version,
        dac_instances.description,
        case 
            when (dbo.fn_sysdac_is_currentuser_sa() = 1) then dac_instances.type_stream
            when sd.owner_sid = SUSER_SID() then dac_instances.type_stream
            else NULL
        end as type_stream,
        dac_instances.date_created,
        dac_instances.created_by,
        dac_instances.instance_name as database_name
    FROM sysdac_instances_internal dac_instances
    LEFT JOIN sys.databases sd
		ON dac_instances.instance_name = sd.name

dbo,sysdatatypemappings,CREATE VIEW dbo.sysdatatypemappings AS SELECT * FROM sys.fn_helpdatatypemap('%', '%', '%', '%', '%', '%', 0)
```

