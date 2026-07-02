# Job: WMS_Report - Shipped Not Received D365 Prep

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - Shipped Not Received D365 Prep"]
    JOB --> hourly_1["Step 1: hourly [TSQL]"]`n```

## Steps

### Step 1: hourly
**Subsystem:** TSQL  

```sql
exec [WMS].[spShippedNotReceivedStoreReportPrep] 
```


