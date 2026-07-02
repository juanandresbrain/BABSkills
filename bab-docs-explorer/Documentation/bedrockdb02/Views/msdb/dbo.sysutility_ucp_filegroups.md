# dbo.sysutility_ucp_filegroups

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysutility_ucp_filegroups"]
    dbo_syn_sysutility_ucp_filegroups(["dbo.syn_sysutility_ucp_filegroups"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.syn_sysutility_ucp_filegroups |

## View Code

```sql
CREATE VIEW dbo.sysutility_ucp_filegroups
AS
   SELECT  [S].[urn]
        , [S].[parent_urn]
        , [S].[Name]
        , [S].[server_instance_name]
        , [S].[database_name]
        , [S].[powershell_path]
        , [S].[processing_time]
        FROM [dbo].[syn_sysutility_ucp_filegroups] S

dbo,sysutility_ucp_instance_policies,CREATE VIEW dbo.sysutility_ucp_instance_policies AS
(    
    SELECT sp.server_instance_name 
        , sp.smo_server_urn
        , sp.utility_server_urn
        , sp.powershell_path
        , ISNULL(lp.policy_id, sp.policy_id) AS policy_id -- if exists get local (overridden) policy, else return global policy 
        , ISNULL(lp.is_global_policy, 1) AS is_global_policy
        , sp.resource_type
        , sp.target_type
        , sp.utilization_type
    FROM (
            -- fetch the global policies 
            SELECT sv.Name AS server_instance_name
                , sv.urn AS smo_server_urn
                , N'Utility[@Name=''' + CONVERT(SYSNAME, SERVERPROPERTY(N'ServerName')) + N''']/' + sv.urn AS utility_server_urn
                , sv.powershell_path AS powershell_path
                , gp.policy_id
                , gp.resource_type
                , gp.target_type
                , gp.utilization_type
            FROM msdb.dbo.sysutility_ucp_instances sv
                , msdb.dbo.sysutility_ucp_policies gp
            WHERE gp.rollup_object_type = 2  
                AND gp.is_global_policy = 1    
        ) sp
        LEFT JOIN msdb.dbo.sysutility_ucp_policies lp -- fetch the local policies (if exists)
        ON lp.rollup_object_urn = sp.utility_server_urn 
            AND lp.rollup_object_type = 2
            AND lp.is_global_policy = 0
            AND lp.resource_type = sp.resource_type
            AND lp.target_type = sp.target_type
            AND lp.utilization_type = sp.utilization_type
)

dbo,sysutility_ucp_instance_policy_type,CREATE VIEW dbo.sysutility_ucp_instance_policy_type AS
(  
    -- Target types
    -- computer_type = 1
    -- volume_type = 6

    -- Resource types
    -- processor_type = 3
    -- space_type = 1

    SELECT sv.Name AS server_instance_name
        , CASE WHEN ((0 < ip.is_policy_overridden) OR (0 < cp.is_policy_overridden)) THEN 1 ELSE 0 END AS is_policy_overridden
    FROM msdb.dbo.sysutility_ucp_instances sv
        , (SELECT server_instance_name , SUM(CASE WHEN 0 < is_global_policy THEN 0 ELSE 1 END) AS is_policy_overridden
           FROM msdb.dbo.sysutility_ucp_instance_policies 
           GROUP BY server_instance_name) ip 
        , (SELECT physical_server_name, SUM(CASE WHEN 0 < is_global_policy THEN 0 ELSE 1 END) AS is_policy_overridden
           FROM msdb.dbo.sysutility_ucp_computer_policies  
           GROUP BY physical_server_name) cp 
    WHERE ip.server_instance_name = sv.Name
        AND cp.physical_server_name = sv.ComputerNamePhysicalNetBIOS
) 

dbo,sysutility_ucp_instances,   CREATE VIEW dbo.sysutility_ucp_instances
   AS
   SELECT [urn]
, [powershell_path]   
, [processing_time]
, [batch_time] AS [collection_time]
, [AuditLevel]
, [BackupDirectory]
, [BrowserServiceAccount]
, [BrowserStartMode]
, [BuildClrVersionString]
, [BuildNumber]
, [Collation]
, [CollationID]
, [ComparisonStyle]
, [ComputerNamePhysicalNetBIOS]
, [DefaultFile]
, [DefaultLog]
, [Edition]
, [EngineEdition]
, [ErrorLogPath]
, [FilestreamShareName]
, [InstallDataDirectory]
, [InstallSharedDirectory]
, [InstanceName]
, [IsCaseSensitive]
, [IsClustered]
, [IsFullTextInstalled]
, [IsSingleUser]
, [Language]
, [MailProfile]
, [MasterDBLogPath]
, [MasterDBPath]
, [MaxPrecision]
, [Name]
, [NamedPipesEnabled]
, [NetName]
, [NumberOfLogFiles]
, [OSVersion]
, [PerfMonMode]
, [PhysicalMemory]
, [Platform]
, [Processors]
, [ProcessorUsage]
, [Product]
, [ProductLevel]
, [ResourceVersionString]
, [RootDirectory]
, [ServerType]
, [ServiceAccount]
, [ServiceInstanceId]
, [ServiceName]
, [ServiceStartMode]
, [SqlCharSet]
, [SqlCharSetName]
, [SqlDomainGroup]
, [SqlSortOrder]
, [SqlSortOrderName]
, [Status]
, [TapeLoadWaitTime]
, [TcpEnabled]
, [VersionMajor]
, [VersionMinor]
, [VersionString] 
   FROM dbo.syn_sysutility_ucp_smo_servers;

dbo,sysutility_ucp_logfiles,CREATE VIEW dbo.sysutility_ucp_logfiles
AS
SELECT  [S].[urn]
        , [S].[parent_urn]
        , [S].[Growth]
        , [S].[GrowthType]
        , [S].[MaxSize]
        , [S].[Name]
        , [S].[Size]
        , [S].[UsedSpace]
        , [S].[FileName]
        , [S].[VolumeFreeSpace]
        , [S].[server_instance_name]
        , [S].[database_name]
        , [S].[powershell_path]
        , [S].[volume_name]
        , [S].[volume_device_id]
        , [S].[physical_server_name]
        , [S].[available_space] -- in bytes
        , CASE WHEN [S].[available_space] = 0.0 THEN 0.0 ELSE ([S].[UsedSpace] * 100)/[S].[available_space] END AS percent_utilization
        , [S].[processing_time]
FROM [dbo].[syn_sysutility_ucp_logfiles] S

dbo,sysutility_ucp_managed_instances,CREATE VIEW [dbo].[sysutility_ucp_managed_instances]
AS
    SELECT     
        instance_id,
        instance_name,
        virtual_server_name,
        date_created,
        created_by,
        agent_proxy_account,
        cache_directory,
        management_state
    FROM [dbo].[sysutility_ucp_managed_instances_internal]
```

