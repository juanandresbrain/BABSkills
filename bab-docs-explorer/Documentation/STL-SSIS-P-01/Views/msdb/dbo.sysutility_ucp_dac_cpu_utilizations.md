# dbo.sysutility_ucp_dac_cpu_utilizations

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysutility_ucp_dac_cpu_utilizations"]
    dbo_sysutility_ucp_deployed_dacs(["dbo.sysutility_ucp_deployed_dacs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysutility_ucp_deployed_dacs |

## View Code

```sql
CREATE VIEW [dbo].[sysutility_ucp_dac_cpu_utilizations]
AS
SELECT
   dac.dac_name AS dac_name, 
   dac.dac_server_instance_name AS server_instance_name, 
   10 AS under_utilization, 
   dac.dac_percent_total_cpu_utilization AS current_utilization, 
   70 AS over_utilization
 FROM	msdb.dbo.sysutility_ucp_deployed_dacs AS dac

dbo,sysutility_ucp_dac_database_file_space_health,	CREATE VIEW dbo.sysutility_ucp_dac_database_file_space_health 
	AS
	SELECT  t.dac_name
			, t.dac_server_instance_name
			, t.fg_name
			, t.file_type
			, (SELECT val FROM dbo.fn_sysutility_ucp_get_aggregated_health(t.over_utilized_count, t.under_utilized_count)) health_state
			, t.processing_time
	FROM msdb.dbo.sysutility_ucp_dac_file_space_health_internal AS t
	WHERE t.set_number = (SELECT latest_health_state_id FROM [msdb].[dbo].[sysutility_ucp_processing_state_internal])
```

