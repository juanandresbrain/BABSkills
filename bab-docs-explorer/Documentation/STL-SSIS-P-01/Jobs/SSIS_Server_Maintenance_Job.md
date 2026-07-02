# Job: SSIS Server Maintenance Job

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Runs every day. The job removes operation records from the database that are outside the retention window and maintains a maximum number of versions per project.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SSIS Server Maintenance Job"]
    JOB --> SSIS_Server_Operation_Records_Maintenance_1["Step 1: SSIS Server Operation Records Maintenance [TSQL]"]`n    JOB --> SSIS_Server_Max_Version_Per_Project_Maintenance_2["Step 2: SSIS Server Max Version Per Project Maintenance [TSQL]"]`n```

## Steps

### Step 1: SSIS Server Operation Records Maintenance
**Subsystem:** TSQL  

```sql
   DECLARE @role int   SET @role = (SELECT [role] FROM [sys].[dm_hadr_availability_replica_states] hars INNER JOIN [sys].[availability_databases_cluster] adc ON hars.[group_id] = adc.[group_id] WHERE hars.[is_local] = 1 AND adc.[database_name] ='SSISDB')   IF DB_ID('SSISDB') IS NOT NULL AND (@role IS NULL OR @role = 1)    EXEC [SSISDB].[internal].[cleanup_server_retention_window]
```

### Step 2: SSIS Server Max Version Per Project Maintenance
**Subsystem:** TSQL  

```sql
   DECLARE @role int   SET @role = (SELECT [role] FROM [sys].[dm_hadr_availability_replica_states] hars INNER JOIN [sys].[availability_databases_cluster] adc ON hars.[group_id] = adc.[group_id] WHERE hars.[is_local] = 1 AND adc.[database_name] ='SSISDB')   IF DB_ID('SSISDB') IS NOT NULL AND (@role IS NULL OR @role = 1)    EXEC [SSISDB].[internal].[cleanup_server_project_version]
```


