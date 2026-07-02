# dbo.syspolicy_system_health_state

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syspolicy_system_health_state"]
    dbo_syspolicy_system_health_state_internal(["dbo.syspolicy_system_health_state_internal"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.syspolicy_system_health_state_internal |

## View Code

```sql
CREATE VIEW [dbo].[syspolicy_system_health_state]
AS
    SELECT 
        health_state_id,
        policy_id,
        last_run_date,
        target_query_expression_with_id,
        target_query_expression,
        result
    FROM [dbo].[syspolicy_system_health_state_internal]

dbo,syspolicy_target_set_levels,CREATE VIEW [dbo].[syspolicy_target_set_levels]
AS
    SELECT     
        target_set_level_id,
        target_set_id,
        type_skeleton,
        condition_id,
        level_name
    FROM [dbo].[syspolicy_target_set_levels_internal]

dbo,syspolicy_target_sets,CREATE VIEW [dbo].[syspolicy_target_sets]
AS
    SELECT     
        target_set_id,
        object_set_id,
        type_skeleton,
        type,
        enabled
    FROM [dbo].[syspolicy_target_sets_internal]

dbo,sysproxyloginsubsystem_view,CREATE VIEW sysproxyloginsubsystem_view
AS
SELECT ps.subsystem_id AS subsystem_id, pl.proxy_id AS proxy_id, pl.sid AS sid, pl.flags AS flags
FROM sysproxylogin pl JOIN sysproxysubsystem ps ON pl.proxy_id = ps.proxy_id

dbo,sysschedules_localserver_view,CREATE VIEW sysschedules_localserver_view
AS
SELECT sched.schedule_id,
       sched.schedule_uid,
       sched.originating_server_id,
       sched.name,
       sched.owner_sid,
       sched.enabled,
       sched.freq_type,
       sched.freq_interval,
       sched.freq_subday_type,
       sched.freq_subday_interval,
       sched.freq_relative_interval,
       sched.freq_recurrence_factor,
       sched.active_start_date,
       sched.active_end_date,
       sched.active_start_time,
       sched.active_end_time,
       sched.date_created,
       sched.date_modified,
       sched.version_number,
       svr.originating_server,
       svr.master_server
FROM msdb.dbo.sysschedules as sched
    JOIN msdb.dbo.sysoriginatingservers_view as svr
    ON sched.originating_server_id = svr.originating_server_id
WHERE (svr.master_server = 0)
  AND ( (sched.owner_sid = SUSER_SID())
        OR (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1)
      OR (ISNULL(IS_MEMBER(N'SQLAgentReaderRole'), 0) = 1)
      )

dbo,systargetservers_view,CREATE VIEW systargetservers_view
AS
SELECT server_id,
       server_name,
       enlist_date,
       last_poll_date
FROM msdb.dbo.systargetservers
UNION
SELECT 0,
       CONVERT(sysname, SERVERPROPERTY('ServerName')),
       CONVERT(DATETIME, N'19981113', 112),
       CONVERT(DATETIME, N'19981113', 112)

dbo,sysutility_mi_configuration,CREATE VIEW [dbo].[sysutility_mi_configuration]
AS
    SELECT config.ucp_instance_name, config.mdw_database_name, t.upload_schema_version
    FROM 
    -- The upload_schema_version represents the contract between the UCP and MI for data upload
    -- Change this value when a breaking change with a (downlevel) UCP may be introduced in the MI
    -- upload code.
    (SELECT 100 AS upload_schema_version) t
    LEFT OUTER JOIN
    [dbo].[sysutility_mi_configuration_internal] config
    ON 1=1

dbo,sysutility_ucp_aggregated_dac_health,CREATE VIEW dbo.sysutility_ucp_aggregated_dac_health 
AS
SELECT t.dac_count
	   , t.dac_healthy_count
	   , t.dac_unhealthy_count
	   , t.dac_over_utilize_count
	   , t.dac_under_utilize_count
	   , t.dac_on_over_utilized_computer_count
	   , t.dac_on_under_utilized_computer_count
	   , t.dac_with_files_on_over_utilized_volume_count
	   , t.dac_with_files_on_under_utilized_volume_count
	   , t.dac_with_over_utilized_file_count
	   , t.dac_with_under_utilized_file_count
	   , t.dac_with_over_utilized_processor_count
	   , t.dac_with_under_utilized_processor_count
FROM msdb.dbo.sysutility_ucp_aggregated_dac_health_internal AS t
WHERE t.set_number = (SELECT latest_health_state_id FROM [msdb].[dbo].[sysutility_ucp_processing_state_internal])        

dbo,sysutility_ucp_aggregated_mi_health,CREATE VIEW dbo.sysutility_ucp_aggregated_mi_health 
AS
SELECT t.mi_count
	   , t.mi_healthy_count
	   , t.mi_unhealthy_count
	   , t.mi_over_utilize_count
	   , t.mi_under_utilize_count
	   , t.mi_on_over_utilized_computer_count
	   , t.mi_on_under_utilized_computer_count
	   , t.mi_with_files_on_over_utilized_volume_count
	   , t.mi_with_files_on_under_utilized_volume_count
	   , t.mi_with_over_utilized_file_count
	   , t.mi_with_under_utilized_file_count
	   , t.mi_with_over_utilized_processor_count
	   , t.mi_with_under_utilized_processor_count
FROM msdb.dbo.sysutility_ucp_aggregated_mi_health_internal AS t
WHERE t.set_number = (SELECT latest_health_state_id FROM [msdb].[dbo].[sysutility_ucp_processing_state_internal])

dbo,sysutility_ucp_computer_cpu_health,	CREATE VIEW dbo.sysutility_ucp_computer_cpu_health 
	AS
	SELECT t.physical_server_name,
			t.health_state,
			t.processing_time
	FROM msdb.dbo.sysutility_ucp_computer_cpu_health_internal AS t
	WHERE t.set_number = (SELECT latest_health_state_id FROM [msdb].[dbo].[sysutility_ucp_processing_state_internal])
```

