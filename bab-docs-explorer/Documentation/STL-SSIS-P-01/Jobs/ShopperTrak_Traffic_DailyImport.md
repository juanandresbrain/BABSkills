# Job: ShopperTrak Traffic DailyImport

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Runs WinSCP command to get ShopperTrak files and move them to the remote archive.  Runs SSIS packages to move the data into Staging and then into DW Fact table.  Runs stored procedure to archive source files after x days (Currently off)

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ShopperTrak Traffic DailyImport"]
    JOB --> SSIS___Traffic_Control_Table_Merge__WinSCP__Stage_Merge_Traffic_Data_1["Step 1: SSIS - Traffic Control Table Merge, WinSCP, Stage\Merge Traffic Data [SSIS]"]`n    JOB --> ReloadHasTraffic_2["Step 2: ReloadHasTraffic [TSQL]"]`n    JOB --> Start_Job___stl_sql_p_04_SQL2008R2___ShopperTrak___Reload_Partitions_and_Email_Process_Summary_3["Step 3: Start Job - stl-sql-p-04\SQL2008R2 - ShopperTrak - Reload Partitions and Email Process Summary [TSQL]"]`n    JOB --> Start_Job___AzureProcessing_TrafficFact_4["Step 4: Start Job - AzureProcessing_TrafficFact [TSQL]"]`n```

## Steps

### Step 1: SSIS - Traffic Control Table Merge, WinSCP, Stage\Merge Traffic Data
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ShopperTrak\ShopperTrackFactETL\ShopperTrackFactETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10093 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: ReloadHasTraffic
**Subsystem:** TSQL  

```sql
exec papamart.dw.dbo.spReloadHasTraffic
```

### Step 3: Start Job - stl-sql-p-04\SQL2008R2 - ShopperTrak - Reload Partitions and Email Process Summary
**Subsystem:** TSQL  

```sql
EXEC [stl-sql-p-04\SQL2008R2].msdb.dbo.sp_start_job @job_name='ShopperTrak - Reload Partitions and Email Process Summary'
```

### Step 4: Start Job - AzureProcessing_TrafficFact
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_TrafficFact'
```


