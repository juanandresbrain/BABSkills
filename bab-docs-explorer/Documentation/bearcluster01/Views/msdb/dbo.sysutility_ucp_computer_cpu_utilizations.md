# dbo.sysutility_ucp_computer_cpu_utilizations

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysutility_ucp_computer_cpu_utilizations"]
    dbo_sysutility_ucp_computers(["dbo.sysutility_ucp_computers"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysutility_ucp_computers |

## View Code

```sql
CREATE VIEW [dbo].[sysutility_ucp_computer_cpu_utilizations]
AS
SELECT comp.physical_server_name AS physical_server_name, 
   10 AS under_utilization, 
   comp.processor_utilization AS current_utilization, 
   70 AS over_utilization
FROM	msdb.dbo.sysutility_ucp_computers AS comp

dbo,sysutility_ucp_computer_policies,CREATE VIEW dbo.sysutility_ucp_computer_policies AS
(    
    SELECT cp.physical_server_name
        , cp.computer_urn
        , cp.powershell_path
        , ISNULL(lp.policy_id, cp.policy_id) AS policy_id -- if exists get local (overridden) policy, else return global policy 
        , ISNULL(lp.is_global_policy, 1) AS is_global_policy
        , cp.resource_type
        , cp.target_type
        , cp.utilization_type
    FROM 
        (
            -- fetch the global policies 
            -- Should we be using "virtual_server_name" or "physical_server_name" here?
            SELECT co.physical_server_name AS physical_server_name
                , co.urn AS computer_urn
                , co.powershell_path AS powershell_path
                , gp.policy_id
                , gp.resource_type
                , gp.target_type
                , gp.utilization_type     
            FROM msdb.dbo.sysutility_ucp_computers co
                , msdb.dbo.sysutility_ucp_policies gp
            WHERE gp.rollup_object_type = 3  
                AND gp.is_global_policy = 1    
        ) cp
        LEFT JOIN msdb.dbo.sysutility_ucp_policies lp -- fetch the local policies (if exists)
        ON lp.rollup_object_urn = cp.computer_urn
            AND lp.rollup_object_type = 3
            AND lp.is_global_policy = 0
            AND lp.resource_type = cp.resource_type
            AND lp.target_type = cp.target_type
            AND lp.utilization_type = cp.utilization_type
)

dbo,sysutility_ucp_computers,CREATE VIEW dbo.sysutility_ucp_computers
AS
   SELECT  
       server_table.id AS computer_id    -- todo (VSTS #345036): This column will be removed
       , server_table.virtual_server_name AS virtual_server_name
       , server_table.physical_server_name AS physical_server_name
       , server_table.is_clustered_server AS is_clustered
       , server_table.percent_total_cpu_utilization AS processor_utilization
       , server_table.cpu_name AS cpu_name
       , server_table.cpu_max_clock_speed AS cpu_max_clock_speed
       , server_table.processing_time AS processing_time
       , urn
       , powershell_path       
   FROM    [dbo].[syn_sysutility_ucp_computers] as server_table

dbo,sysutility_ucp_configuration,CREATE VIEW [dbo].[sysutility_ucp_configuration]
AS
    SELECT     
        name,
        current_value
    FROM [dbo].[sysutility_ucp_configuration_internal]
```

