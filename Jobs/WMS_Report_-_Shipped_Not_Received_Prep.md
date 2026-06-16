# Job: WMS_Report - Shipped Not Received Prep

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - Shipped Not Received Prep"]
    JOB --> hourly_data_refresh_1["Step 1: hourly data refresh [TSQL]"]`n    JOB --> hourly_detail_refresh_2["Step 2: hourly detail refresh [TSQL]"]`n```

## Steps

### Step 1: hourly data refresh
**Subsystem:** TSQL  

```sql
exec [WMS].[spShippedNotReceivedReportPrep]
```

### Step 2: hourly detail refresh
**Subsystem:** TSQL  

```sql
exec [WMS].[spShippedNotReceivedReportDetailPrep]
```


