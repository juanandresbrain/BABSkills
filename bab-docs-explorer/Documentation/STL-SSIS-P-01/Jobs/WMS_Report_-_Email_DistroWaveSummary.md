# Job: WMS_Report - Email DistroWaveSummary

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Checks for Waves to hit the HA Integration table in last 30 minutes.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - Email DistroWaveSummary"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
if (select count (*) from IntegrationStaging.[WMS].[vwWaveLastThirtyMinutes]) > 0        Begin       exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name  = '44EF2281-EEB1-4E12-B2B2-904464C56CFA'      End
```


