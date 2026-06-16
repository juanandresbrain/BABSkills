# Job: WMS_Report - Email Nightly Wave Summary

**Enabled:** Yes  
**Description:** Looks for wave's after 8:00 p.m. Eastern time and sends carton count details

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - Email Nightly Wave Summary"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
set nocount on   if (select count (*) from IntegrationStaging.[WMS].[vwNightlyWaveControl]) > 0     Begin      Insert IntegrationStaging.[WMS].[WaveControl] (WaveId, InsertDate)   select distinct WaveId, getdate() as InsertDate   from IntegrationStaging.[WMS].[vwNightlyWaveControl]     -- Call Details Report      exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name = '34D97780-1F2A-45DA-A3B4-550DE84D781C'       -- Call Summary Report    exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name = 'EE4A6C7E-A955-43F0-B19F-5F26A50DAFFA'            end     
```


