# dbo.sysutility_ucp_databases

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysutility_ucp_databases"]
    dbo_syn_sysutility_ucp_databases(["dbo.syn_sysutility_ucp_databases"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.syn_sysutility_ucp_databases |

## View Code

```sql
CREATE VIEW dbo.sysutility_ucp_databases
AS
   SELECT	S.urn
        , S.parent_urn
        , S.Collation
        , S.CompatibilityLevel
        , S.CreateDate
        , S.EncryptionEnabled
        , S.Name
        , S.server_instance_name
        , S.powershell_path
        , S.RecoveryModel
        , [S].[Trustworthy]
        , [S].processing_time
        , S.state 
      FROM [dbo].[syn_sysutility_ucp_databases] AS S

dbo,sysutility_ucp_datafiles,CREATE VIEW dbo.sysutility_ucp_datafiles
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
        , [S].[filegroup_name]
        , [S].[powershell_path]
        , [S].[volume_name]
        , [S].[volume_device_id]
        , [S].[physical_server_name]
        , [S].[available_space] -- in bytes
        , CASE WHEN [S].[available_space] = 0.0 THEN 0.0 ELSE ([S].[UsedSpace] * 100)/[S].[available_space] END AS percent_utilization
        , [S].[processing_time]
FROM [dbo].[syn_sysutility_ucp_datafiles] S

dbo,sysutility_ucp_deployed_dacs,CREATE VIEW dbo.sysutility_ucp_deployed_dacs
AS
SELECT
   dacs.dac_id,    -- todo (VSTS #345036): This column will be removed
   dacs.dac_name,
   dacs.dac_deploy_date AS dac_deployed_date,
   dacs.dac_description AS dac_description,
   dacs.dac_percent_total_cpu_utilization AS dac_percent_total_cpu_utilization,
   dacs.server_instance_name AS dac_server_instance_name,
   dacs.physical_server_name AS dac_physical_server_name,
   dacs.batch_time AS dac_collection_time,
   dacs.processing_time AS dac_processing_time,
   dacs.urn,
   dacs.powershell_path
FROM dbo.syn_sysutility_ucp_dacs as dacs
--- The join operator removes those DACs in the managed instances which are unenrolled during
--- the time between two consecutive data collection. 
--- See VSTS #473462 for more information 
INNER JOIN dbo.sysutility_ucp_managed_instances as mis
ON dacs.server_instance_name = mis.instance_name;
```

