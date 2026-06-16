# Job: WEB - OrderMakeup Report

**Enabled:** Yes  
**Description:** Executes stored procedure WMS.spReportWebOrderMakeup at midnight and 3PM Bearhouse time/11PM and 2PM BQ time

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - OrderMakeup Report"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
EXEC WMS.spReportWebOrderMakeup
```


