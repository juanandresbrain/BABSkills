# dbo.sysalerts_performance_counters_view

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysalerts_performance_counters_view"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## View Code

```sql
CREATE VIEW sysalerts_performance_counters_view
AS
    -- Parse object_name 'SQLServer:Buffer Manager', exclude instance specific info; return as 'Buffer Manager'
    SELECT RTRIM(SUBSTRING(pc.object_name, CHARINDEX(':', pc.object_name)+1, DATALENGTH(pc.object_name))) AS 'object_name', 
            RTRIM(pc.counter_name) AS 'counter_name', 
            CASE WHEN pc.instance_name IS NULL
                THEN NULL
                ELSE RTRIM(pc.instance_name)
            END AS 'instance_name',
            pc.cntr_value,
            pc.cntr_type,
            SERVERPROPERTY('ServerName') AS 'server_name'
    FROM sys.dm_os_performance_counters pc

dbo,syscollector_collection_items,CREATE VIEW [dbo].[syscollector_collection_items]
AS
    SELECT
        i.collection_set_id,
        i.collection_item_id,
        i.collector_type_uid,
        CASE 
            WHEN i.name_id IS NULL THEN i.name 
            ELSE FORMATMESSAGE(i.name_id)
        END AS name,        
        i.frequency,
        i.parameters
    FROM 
        [dbo].[syscollector_collection_items_internal] i

dbo,syscollector_collection_sets,CREATE VIEW [dbo].[syscollector_collection_sets]
AS
    SELECT 
        s.collection_set_id,
        s.collection_set_uid,
        CASE 
            WHEN s.name_id IS NULL THEN s.name 
            ELSE FORMATMESSAGE(s.name_id)
        END AS name,        
        s.target,
        s.is_system,
        s.is_running,
        s.collection_mode,
        s.proxy_id,
        s.schedule_uid,
        s.collection_job_id,
        s.upload_job_id,
        s.logging_level,
        s.days_until_expiration,
        CASE 
            WHEN s.description_id IS NULL THEN s.description
            ELSE FORMATMESSAGE(s.description_id)
        END AS description,
        s.dump_on_any_error,
        s.dump_on_codes
    FROM 
        [dbo].[syscollector_collection_sets_internal] AS s

dbo,syscollector_collector_types,CREATE VIEW [dbo].[syscollector_collector_types]
AS
    SELECT 
        t.collector_type_uid,
        t.name,
        t.parameter_schema,
        t.parameter_formatter,
        s1.id AS collection_package_id,
        dbo.fn_syscollector_get_package_path(s1.id) AS collection_package_path,
        s1.name AS collection_package_name,
        s2.id AS upload_package_id,
        dbo.fn_syscollector_get_package_path(s2.id) AS upload_package_path,
        s2.name AS upload_package_name,
        t.is_system
    FROM 
        [dbo].[syscollector_collector_types_internal] AS t,
        sysssispackages s1,
        sysssispackages s2
    WHERE t.collection_package_folderid = s1.folderid
      AND t.collection_package_name = s1.name
      AND t.upload_package_folderid = s2.folderid
      AND t.upload_package_name = s2.name

dbo,syscollector_config_store,CREATE VIEW [dbo].[syscollector_config_store]
AS
    SELECT
        s.parameter_name,
        s.parameter_value
    FROM 
        [dbo].[syscollector_config_store_internal] s
```

