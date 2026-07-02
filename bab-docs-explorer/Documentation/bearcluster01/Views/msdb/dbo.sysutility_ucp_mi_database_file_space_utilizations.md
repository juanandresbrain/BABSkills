# dbo.sysutility_ucp_mi_database_file_space_utilizations

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysutility_ucp_mi_database_file_space_utilizations"]
    dbo_sysutility_ucp_database_files(["dbo.sysutility_ucp_database_files"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysutility_ucp_database_files |

## View Code

```sql
CREATE VIEW [dbo].[sysutility_ucp_mi_database_file_space_utilizations] AS
    SELECT	df.server_instance_name, 
            df.database_name, 
            df.filegroup_name,
            df.Name,
            df.volume_name,
            df.volume_device_id,
            df.FileName AS databasefile_name, 
            df.percent_utilization AS current_utilization, 
            df.UsedSpace AS used_space, 
            df.available_space AS available_space,
            10 AS under_utilization,  
            70 AS over_utilization,
            df.file_type,
            df.GrowthType AS growth_type	
    FROM	msdb.dbo.sysutility_ucp_database_files AS df

dbo,sysutility_ucp_mi_database_health,	CREATE VIEW dbo.sysutility_ucp_mi_database_health 
	AS
	SELECT t.server_instance_name,
			t.database_name,
			(SELECT val FROM dbo.fn_sysutility_ucp_get_aggregated_health(t.over_utilized_count, t.under_utilized_count)) health_state,
			t.processing_time
	FROM msdb.dbo.sysutility_ucp_mi_database_health_internal AS t
	WHERE t.set_number = (SELECT latest_health_state_id FROM [msdb].[dbo].[sysutility_ucp_processing_state_internal])

dbo,sysutility_ucp_mi_file_space_health,	CREATE VIEW dbo.sysutility_ucp_mi_file_space_health 
	AS
	SELECT t.server_instance_name,
			t.database_name,
			t.fg_name,
			t.file_type,
			(SELECT val FROM dbo.fn_sysutility_ucp_get_aggregated_health(t.over_utilized_count, t.under_utilized_count)) health_state,
			t.processing_time
	FROM msdb.dbo.sysutility_ucp_mi_file_space_health_internal AS t
	WHERE t.set_number = (SELECT latest_health_state_id FROM [msdb].[dbo].[sysutility_ucp_processing_state_internal])

dbo,sysutility_ucp_mi_health,CREATE VIEW dbo.sysutility_ucp_mi_health 
AS
SELECT t.mi_name
	   , (SELECT val FROM dbo.fn_sysutility_ucp_get_aggregated_health(t.is_volume_space_over_utilized, t.is_volume_space_under_utilized)) volume_space_health_state
	   , (SELECT val FROM dbo.fn_sysutility_ucp_get_aggregated_health(t.is_computer_processor_over_utilized, t.is_computer_processor_under_utilized)) computer_processor_health_state
	   , (SELECT val FROM dbo.fn_sysutility_ucp_get_aggregated_health(t.is_file_space_over_utilized, t.is_file_space_under_utilized)) file_space_health_state
	   , (SELECT val FROM dbo.fn_sysutility_ucp_get_aggregated_health(t.is_mi_processor_over_utilized, t.is_mi_processor_under_utilized)) mi_processor_health_state
	   , CASE WHEN (is_volume_space_over_utilized > 0) THEN CONVERT(BIT, 1) ELSE CONVERT(BIT, 0) END AS contains_over_utilized_volumes
	   , CASE WHEN (is_volume_space_under_utilized > 0) THEN CONVERT(BIT, 1) ELSE CONVERT(BIT, 0) END AS contains_under_utilized_volumes 
	   , CASE WHEN (is_file_space_over_utilized > 0) THEN CONVERT(BIT, 1) ELSE CONVERT(BIT, 0) END AS contains_over_utilized_databases
	   , CASE WHEN (is_file_space_under_utilized > 0) THEN CONVERT(BIT, 1) ELSE CONVERT(BIT, 0) END AS contains_under_utilized_databases
	   , t.is_policy_overridden
	   , t.processing_time
FROM msdb.dbo.sysutility_ucp_mi_health_internal AS t
WHERE t.set_number = (SELECT latest_health_state_id FROM [msdb].[dbo].[sysutility_ucp_processing_state_internal])

dbo,sysutility_ucp_mi_volume_space_health,	CREATE VIEW dbo.sysutility_ucp_mi_volume_space_health 
	AS
	SELECT t.physical_server_name,
			t.server_instance_name,
			t.volume_device_id,
			t.health_state,
			t.processing_time
	FROM msdb.dbo.sysutility_ucp_mi_volume_space_health_internal AS t
	WHERE t.set_number = (SELECT latest_health_state_id FROM [msdb].[dbo].[sysutility_ucp_processing_state_internal])
```

